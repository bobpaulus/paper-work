#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
oa_search.py — 甲状腺癌文献监测的 OpenAlex 主检索器
（配合 lit-review skill 使用；替代本环境不可达的 NCBI eutils 直连）

背景 / 为什么是 OpenAlex：
  本机到 eutils.ncbi.nlm.nih.gov 与 pubmed.ncbi.nlm.nih.gov 网络不可达
  （2026-08-07 实测 4/4 超时，HTTP 000）。paper-search-mcp 走服务端代理
  尚可用但频繁返回 "not well-formed (invalid token)" 并截断结果。
  OpenAlex / Crossref / Unpaywall 直连稳定（~1.4s），且 OpenAlex 索引
  预印本、按发表日期排序，能捞到 PubMed 尚未编目的新文献。

用法:
  python oa_search.py --since 2026-07-08 --out search_results_run17.json
  python oa_search.py --days 30 --baseline search_results_latest.json
  python oa_search.py --days 90 --per-page 25          # 放宽窗口
"""

import argparse
import json
import re
import sys
import time
import unicodedata
import urllib.parse
import urllib.request
from collections import Counter, OrderedDict
from datetime import datetime, timedelta, timezone

OPENALEX = "https://api.openalex.org/works"
MAILTO = "lit-review@local"          # Crossref/OpenAlex "polite pool"
TIMEOUT = 45
SLEEP = 0.4                          # OpenAlex 无严格限速，礼貌间隔

# ---------------------------------------------------------------- 检索矩阵
# dim 代码: MO=分子机制 IM=免疫微环境 SC=单细胞 SP=空间组学
#           AL=算法方法 PR=预后转移 ST=干性/去分化 ME=代谢重编程
DIM_LABEL = {
    "MO": "分子机制", "IM": "免疫微环境", "SC": "单细胞", "SP": "空间组学",
    "AL": "算法方法", "PR": "预后转移", "ST": "转移干性", "ME": "代谢重编程",
}

THYROID = '(thyroid OR "papillary thyroid" OR PTC OR PTMC OR "follicular thyroid" OR "medullary thyroid" OR "anaplastic thyroid")'

QUERIES = OrderedDict([
    ("a", dict(dim=["MO", "PR"],
               q=f'{THYROID} AND (metastasis OR metastatic OR "lymph node") AND (biomarker OR "gene signature" OR signature)')),
    ("b", dict(dim=["MO"],
               q=f'{THYROID} AND (invasion OR metastasis) AND (mechanism OR pathway OR EMT OR "epithelial-mesenchymal")')),
    ("c", dict(dim=["AL", "PR"],
               q=f'{THYROID} AND (metastasis OR "lymph node") AND ("machine learning" OR "deep learning" OR radiomics OR nomogram OR "prediction model")')),
    ("d", dict(dim=["IM"],
               q=f'{THYROID} AND (metastasis OR metastatic) AND ("immune microenvironment" OR "tumor microenvironment" OR immune OR macrophage OR "T cell")')),
    ("e", dict(dim=["SC"],
               q=f'{THYROID} AND (metastasis OR metastatic OR heterogeneity) AND ("single-cell" OR scRNA-seq OR "single cell RNA")')),
    ("f", dict(dim=["SP"],
               q=f'{THYROID} AND ("spatial transcriptomic" OR "spatial transcriptomics" OR "spatial multi-omics" OR "spatial omics" OR Visium)')),
    ("g", dict(dim=["PR"],
               q=f'{THYROID} AND (prognosis OR recurrence OR "distant metastasis") AND ("risk model" OR "risk stratification" OR survival OR nomogram)')),
    ("h", dict(dim=["ST"],
               q=f'{THYROID} AND (metastasis OR metastatic) AND ("cancer stem cell" OR stemness OR dedifferentiation OR "tumor-initiating")')),
    ("i", dict(dim=["ME"],
               q=f'{THYROID} AND (metastasis OR metastatic OR progression) AND ("metabolic reprogramming" OR glycolysis OR "lipid metabolism" OR ferroptosis OR OXPHOS)')),
])

# 排除非甲状腺文献（乳腺/肺/结直肠 LNM 等）
OFF_TOPIC = re.compile(
    r"\b(breast|lung|colorect|gastric|esophag|hepatocell|pancrea|prostate|cervic|"
    r"ovarian|melanoma|glioma|bladder|renal cell|nasopharyng|oral squamous)\b", re.I)
THYROID_HIT = re.compile(r"thyroid|PTC\b|PTMC\b|\bFTC\b|\bMTC\b|\bATC\b", re.I)
# 必须是肿瘤主题（排除甲状腺功能亢进/眼病/桥本等非肿瘤研究）
CANCER_HIT = re.compile(
    r"carcinom|cancer|tumou?r|neoplas|malignan|oncolog|metasta|PTC\b|PTMC\b|"
    r"\bFTC\b|\bMTC\b|\bATC\b|nodule", re.I)
# 期刊补充材料被 OpenAlex 当作独立 work 索引 —— 必须剔除
SUPPLEMENT = re.compile(
    r"^(table|data\s*sheet|figure|image|supplementary|presentation|appendix|"
    r"additional file|supplemental)\s*\d*\s*[_:.]", re.I)


# ---------------------------------------------------------------- 工具函数
def http_json(url, params, retries=3):
    """带重试的 GET JSON。"""
    qs = urllib.parse.urlencode(params, quote_via=urllib.parse.quote)
    full = f"{url}?{qs}"
    last = None
    for i in range(retries):
        try:
            req = urllib.request.Request(
                full, headers={"User-Agent": f"lit-review-bot (mailto:{MAILTO})",
                               "Accept": "application/json"})
            with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
                return json.loads(r.read().decode("utf-8"))
        except Exception as e:                                   # noqa: BLE001
            last = e
            time.sleep(1.5 * (i + 1))
    print(f"  [WARN] 请求失败({last}): {full[:120]}", file=sys.stderr)
    return None


def clean_title(t):
    """OpenAlex 检索结果标题含 <b> 高亮标签。"""
    if not t:
        return ""
    return re.sub(r"</?[a-zA-Z]+>", "", t).strip()


def norm_key(t):
    """标题归一化，用于无 DOI 时去重。"""
    t = unicodedata.normalize("NFKD", clean_title(t)).lower()
    return re.sub(r"[^a-z0-9]+", "", t)[:90]


def rebuild_abstract(inv):
    """OpenAlex abstract 是倒排索引，需重建。"""
    if not inv:
        return ""
    pos = {}
    for word, idxs in inv.items():
        for i in idxs:
            pos[i] = word
    if not pos:
        return ""
    return " ".join(pos[i] for i in sorted(pos))


def score_relevance(rec):
    """High/Medium/Low：按维度命中数 + 是否研究型原著 + 是否近期。"""
    txt = (rec["title"] + " " + rec.get("abstract", "")).lower()
    hits = sum(bool(re.search(p, txt)) for p in [
        r"metasta", r"lymph node", r"single.cell|scrna", r"spatial",
        r"machine learning|deep learning|radiomics|nomogram",
        r"immune|microenvironment", r"prognos|recurrence|survival",
        r"stemness|stem cell|dedifferentiat", r"metabolic|glycolys|ferroptos",
    ])
    if rec.get("type") in ("review", "editorial", "letter"):
        hits -= 1
    if len(rec.get("queries", [])) >= 2:
        hits += 1
    return "High" if hits >= 4 else ("Medium" if hits >= 2 else "Low")


# ---------------------------------------------------------------- 主流程
def run(since, per_page, baseline_path, out_path, verbose=True):
    store = OrderedDict()
    qmeta = OrderedDict()

    for qid, spec in QUERIES.items():
        params = {
            "filter": f'title_and_abstract.search:{spec["q"]},from_publication_date:{since}',
            "sort": "publication_date:desc",
            "per-page": str(per_page),
            "mailto": MAILTO,
        }
        data = http_json(OPENALEX, params)
        time.sleep(SLEEP)
        if not data or "results" not in data:
            qmeta[qid] = dict(count=0, returned=0, status="FAILED", dims=spec["dim"])
            if verbose:
                print(f"[{qid}] FAILED")
            continue

        total = data["meta"]["count"]
        kept = 0
        for w in data["results"]:
            title = clean_title(w.get("title"))
            if not title or SUPPLEMENT.match(title):   # 跳过补充材料条目
                continue
            doi = (w.get("doi") or "").replace("https://doi.org/", "") or None
            # 先按标题归一化去重（同一论文常有预印本/正式版多个 DOI），
            # 无同名标题时才回落到 DOI 作为键
            tkey = norm_key(title)
            key = tkey if tkey else (doi.lower() if doi else None)
            if not key:
                continue

            if key in store:                       # 已有 → 合并维度/查询来源
                cur = store[key]
                if qid not in cur["queries"]:
                    cur["queries"].append(qid)
                for d in spec["dim"]:
                    if d not in cur["dimensions"]:
                        cur["dimensions"].append(d)
                # 同一论文的多个版本：补齐更权威的标识
                ids2 = w.get("ids") or {}
                pm2 = ids2.get("pmid", "")
                pm2 = pm2.rsplit("/", 1)[-1] if pm2 else None
                if pm2 and not cur.get("pmid"):
                    cur["pmid"] = pm2
                if doi and not cur.get("doi"):
                    cur["doi"] = doi
                cur["versions"] = cur.get("versions", 1) + 1
                continue

            ids = w.get("ids") or {}
            pmid = ids.get("pmid", "")
            pmid = pmid.rsplit("/", 1)[-1] if pmid else None
            abstract = rebuild_abstract(w.get("abstract_inverted_index"))
            blob = f"{title} {abstract}"

            # 在范围判定（严格）：标题须点名甲状腺，且整体须是肿瘤主题。
            # 仅摘要顺带提及 thyroid 的他病文献（如 irAE 甲功异常、
            # Thyroid Eye Disease、桥本甲状腺炎）由此剔除。
            in_scope = bool(THYROID_HIT.search(title)) and bool(CANCER_HIT.search(blob))
            if OFF_TOPIC.search(title) and not THYROID_HIT.search(title):
                in_scope = False
            exclude_reason = None
            if not in_scope:
                if not THYROID_HIT.search(title):
                    exclude_reason = "标题未点名甲状腺"
                elif not CANCER_HIT.search(blob):
                    exclude_reason = "非肿瘤主题（甲状腺良性/自身免疫病）"

            store[key] = {
                "pmid": pmid,
                "doi": doi,
                "openalex_id": (w.get("id") or "").rsplit("/", 1)[-1],
                "title": title,
                "abstract": abstract[:1500],
                "publication_date": w.get("publication_date"),
                "type": w.get("type"),
                "is_preprint": w.get("type") == "preprint",
                "venue": ((w.get("primary_location") or {}).get("source") or {}).get("display_name"),
                "oa_status": (w.get("open_access") or {}).get("oa_status"),
                "oa_url": (w.get("best_oa_location") or {}).get("pdf_url"),
                "cited_by_count": w.get("cited_by_count", 0),
                "in_scope_thyroid": in_scope,
                "exclude_reason": exclude_reason,
                "versions": 1,
                "queries": [qid],
                "dimensions": list(spec["dim"]),
            }
            kept += 1

        qmeta[qid] = dict(count=total, returned=len(data["results"]),
                          kept_new=kept, status="OK", dims=spec["dim"],
                          query=spec["q"])
        if verbose:
            print(f"[{qid}] {DIM_LABEL[spec['dim'][0]]:<6} 命中 {total:>5} | 取回 {len(data['results']):>3} | 新条目 {kept:>3}")

    # 打分 + 中文维度标签
    for r in store.values():
        r["relevance"] = score_relevance(r)
        r["dimension_labels"] = [DIM_LABEL[d] for d in r["dimensions"]]

    records = list(store.values())
    in_scope = [r for r in records if r["in_scope_thyroid"]]

    # ------------------------------------------------ 与基线比对
    base_pmids, base_dois, base_titles = set(), set(), set()
    if baseline_path:
        try:
            with open(baseline_path, encoding="utf-8") as f:
                b = json.load(f)
            for r in b.get("records", []):
                if r.get("pmid"):
                    base_pmids.add(str(r["pmid"]))
                if r.get("doi"):
                    base_dois.add(str(r["doi"]).lower())
                if r.get("title"):
                    base_titles.add(norm_key(r["title"]))
        except Exception as e:                                   # noqa: BLE001
            print(f"  [WARN] 基线读取失败: {e}", file=sys.stderr)

    def is_new(r):
        if r.get("pmid") and str(r["pmid"]) in base_pmids:
            return False
        if r.get("doi") and str(r["doi"]).lower() in base_dois:
            return False
        return norm_key(r["title"]) not in base_titles

    new_records = [r for r in in_scope if is_new(r)]

    dim_counter = Counter()
    for r in in_scope:
        for d in r["dimensions"]:
            dim_counter[DIM_LABEL[d]] += 1

    payload = {
        "search_date": datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds"),
        "primary_source": "OpenAlex REST API (api.openalex.org)",
        "source_note": ("本机 NCBI eutils / pubmed.ncbi.nlm.nih.gov 网络不可达（实测 HTTP 000 超时），"
                        "故以 OpenAlex 为主源；paper-search-mcp 仅作补充。"),
        "window_from": since,
        "queries": qmeta,
        "summary": {
            "unique_records": len(records),
            "in_scope_thyroid": len(in_scope),
            "excluded": len(records) - len(in_scope),
            "exclude_reasons": dict(Counter(
                r.get("exclude_reason") for r in records if not r["in_scope_thyroid"])),
            "multi_version_merged": sum(1 for r in records if r.get("versions", 1) > 1),
            "new_vs_baseline": len(new_records),
            "preprints": sum(r["is_preprint"] for r in in_scope),
            "relevance": dict(Counter(r["relevance"] for r in in_scope)),
            "dimensions": dict(dim_counter),
            "baseline_file": baseline_path,
            "baseline_size": len(base_pmids | base_dois),
        },
        "new_records": new_records,
        "records": records,
    }

    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)

    if verbose:
        s = payload["summary"]
        print("\n" + "=" * 62)
        print(f"唯一记录 {s['unique_records']} | 甲状腺在范围 {s['in_scope_thyroid']} | "
              f"预印本 {s['preprints']}")
        print(f"相对基线新增: {s['new_vs_baseline']}")
        print(f"相关性: {s['relevance']}")
        print(f"维度分布: {s['dimensions']}")
        print(f"→ {out_path}")
        if new_records:
            print("\n新增文献 (按日期倒序):")
            for r in sorted(new_records, key=lambda x: x["publication_date"] or "", reverse=True)[:25]:
                tag = "[preprint]" if r["is_preprint"] else ""
                print(f"  {r['publication_date']} [{r['relevance']:<6}] "
                      f"{'/'.join(r['dimension_labels'])} {tag}")
                print(f"     {r['title'][:100]}")
                print(f"     DOI:{r['doi'] or '-'}  PMID:{r['pmid'] or '待编目'}")
    return payload


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--since", help="起始发表日期 YYYY-MM-DD")
    p.add_argument("--days", type=int, default=30, help="回溯天数（--since 未给时生效）")
    p.add_argument("--per-page", type=int, default=25)
    p.add_argument("--baseline", default="search_results_latest.json")
    p.add_argument("--out", default=None)
    a = p.parse_args()

    since = a.since or (datetime.now() - timedelta(days=a.days)).strftime("%Y-%m-%d")
    out = a.out or f"search_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    print(f"OpenAlex 检索窗口: >= {since} | 每路上限 {a.per_page}\n" + "-" * 62)
    run(since, a.per_page, a.baseline, out)


if __name__ == "__main__":
    main()
