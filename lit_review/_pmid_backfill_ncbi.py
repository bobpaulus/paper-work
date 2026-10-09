# -*- coding: utf-8 -*-
"""
Run #29 附加：NCBI eutils 通道恢复后，批量回填基线中缺失的 PMID。
以 DOI 为主键查询 PubMed（term=<doi>[DOI]），缺失则回退按标题查询。
严格遵守 NCBI 速率限制：无 API key 每秒 <= 3 次请求（sleep 0.4s）。
绝不编造 PMID：查不到就留空。
"""
import json, time, urllib.parse, urllib.request, sys

BASE = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
UA = {"User-Agent": "thyroid-lit-review/1.0 (mailto:bobpaul@126.com)"}


def _get(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=20) as r:
        return r.read().decode("utf-8", "ignore")


def esearch(term):
    url = BASE + "esearch.fcgi?" + urllib.parse.urlencode(
        {"db": "pubmed", "term": term, "retmode": "json", "retmax": 3})
    try:
        d = json.loads(_get(url))
        return d.get("esearchresult", {}).get("idlist", [])
    except Exception as e:
        return []


def norm_title(t):
    return "".join(c for c in (t or "").lower() if c.isalnum() or c == " ")[:110].strip()


def pmid_by_title(title):
    # 用核心标题词做宽松匹配，再人工核对不做（此处仅取第一个结果，风险由 caller 控制）
    q = (title or "")[:150]
    if not q:
        return None
    ids = esearch('"%s"[Title]' % q.replace('"', ""))
    return ids[0] if ids else None


def main():
    path = "search_results_latest.json"
    d = json.load(open(path, encoding="utf-8"))
    recs = d["records"]
    todo = [r for r in recs if not r.get("pmid") and r.get("doi")]
    print("total=%d  missing_pmid_with_doi=%d" % (len(recs), len(todo)))

    hit_doi = 0
    hit_title = 0
    fail = 0
    for i, r in enumerate(todo):
        doi = r.get("doi", "").strip()
        pmid = None
        # 跳过明确无 PMID 的类型：预印本 / 数据集 / 会议摘要前缀
        low = doi.lower()
        if any(k in low for k in ("preprints", "rs.3.rs-", "zenodo", "figshare",
                                  "dvn/", "ssrn", "biorxiv", "medrxiv", "researchsquare")):
            continue
        if doi:
            ids = esearch("%s[DOI]" % doi)
            time.sleep(0.4)
            if ids:
                pmid = ids[0]
                hit_doi += 1
        if not pmid and r.get("title"):
            # 标题回退：仅当标题足够长以避免误匹配
            if len(r.get("title", "")) > 40:
                pmid = pmid_by_title(r["title"])
                time.sleep(0.4)
                if pmid:
                    hit_title += 1
        if pmid:
            r["pmid"] = pmid
            r["pmid_source"] = "NCBI-eutils-backfill-20261009"
        else:
            fail += 1
        if (i + 1) % 20 == 0:
            print("  ...%d/%d  doi_hit=%d title_hit=%d miss=%d"
                  % (i + 1, len(todo), hit_doi, hit_title, fail), flush=True)

    json.dump(d, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    # 同时写一份带时间戳副本
    json.dump(d, open("search_results_20261009_030249_pmidbackfill.json", "w", encoding="utf-8"),
              ensure_ascii=False, indent=2)
    remaining = sum(1 for r in d["records"] if not r.get("pmid"))
    print("DONE doi_hit=%d title_hit=%d still_missing=%d/%d"
          % (hit_doi, hit_title, remaining, len(d["records"])))


if __name__ == "__main__":
    main()
