# -*- coding: utf-8 -*-
"""
Run #29 补充回填（2026-10-17 执行）
=====================================
背景：Run #29 因「NCBI 不可达」误判跳过 PMID 回填，遗留 12 条「待编目」。
2026-10-17 定位真实根因为 Windows Schannel 吊销检查（非网络故障）：
  - curl 需 --ssl-no-revoke
  - Python urllib 走 OpenSSL，默认不查吊销 → 本脚本直接使用 urllib，天然规避

相对旧版 _pmid_backfill_ncbi.py 的改进：
  1. **HTTP 429 退避重试**（真实限流，非网络故障）：3 s / 6 s / 12 s，最多 3 次
  2. **标题回退加校验**：esearch 命中后拉 esummary 取真实标题，difflib 相似度 >= 0.88 才采信
     （旧版直接取第一个结果，有误配风险）
  3. 回填后把 PMID 同步传播到时间戳副本与 _new.json
  4. 输出命中明细，便于人工抽查

绝不编造 PMID：查不到即留空。
"""
import json, time, difflib, urllib.parse, urllib.request, sys

BASE = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
UA = {"User-Agent": "thyroid-lit-review/1.0 (mailto:bobpaul@126.com)"}
SLEEP = 0.4          # 无 key 时 <=3 req/s
BACKOFF = [3, 6, 12] # 429 退避

SKIP_DOI_TOKENS = ("preprints", "rs.3.rs-", "zenodo", "figshare", "dvn/",
                   "ssrn", "biorxiv", "medrxiv", "researchsquare", "inplasy")


def _get(url, tries=len(BACKOFF) + 1):
    """带 429 退避的 GET。返回 str；彻底失败返回 None。"""
    for n in range(tries):
        try:
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=25) as r:
                return r.read().decode("utf-8", "ignore")
        except urllib.error.HTTPError as e:
            if e.code == 429:
                wait = BACKOFF[n] if n < len(BACKOFF) else 20
                print("      [429] backoff %ss (try %d)" % (wait, n + 1), flush=True)
                time.sleep(wait)
                continue
            return None
        except Exception as e:
            print("      [ERR] %s: %s" % (type(e).__name__, str(e)[:70]), flush=True)
            time.sleep(1)
    return None


def esearch(term):
    url = BASE + "esearch.fcgi?" + urllib.parse.urlencode(
        {"db": "pubmed", "term": term, "retmode": "json", "retmax": 3})
    txt = _get(url)
    if not txt:
        return []
    try:
        return json.loads(txt).get("esearchresult", {}).get("idlist", [])
    except Exception:
        return []


def esummary_title(pmid):
    url = BASE + "esummary.fcgi?" + urllib.parse.urlencode(
        {"db": "pubmed", "id": pmid, "retmode": "json"})
    txt = _get(url)
    if not txt:
        return None
    try:
        return json.loads(txt)["result"][str(pmid)]["title"]
    except Exception:
        return None


def norm(t):
    return "".join(c for c in (t or "").lower() if c.isalnum() or c == " ").strip()


def pmid_by_title(title):
    """标题回退：命中后必须回查真实标题并校验相似度，防止误配。"""
    q = (title or "").strip()
    if len(q) < 40:
        return None, 0.0
    ids = esearch('"%s"[Title]' % q[:150].replace('"', ""))
    time.sleep(SLEEP)
    if not ids:
        return None, 0.0
    real = esummary_title(ids[0])
    time.sleep(SLEEP)
    if not real:
        return None, 0.0
    sim = difflib.SequenceMatcher(None, norm(q), norm(real)).ratio()
    return (ids[0], sim) if sim >= 0.88 else (None, sim)


def main():
    path = "search_results_latest.json"
    d = json.load(open(path, encoding="utf-8"))
    recs = d["records"]
    todo = [r for r in recs if not r.get("pmid") and r.get("doi")]
    print("total=%d  missing_pmid_with_doi=%d" % (len(recs), len(todo)), flush=True)

    hit_doi, hit_title, skipped, miss = 0, 0, 0, []
    for i, r in enumerate(todo):
        doi = (r.get("doi") or "").strip()
        low = doi.lower()
        if any(k in low for k in SKIP_DOI_TOKENS):
            skipped += 1
            continue

        pmid, src = None, None
        ids = esearch("%s[DOI]" % doi)
        time.sleep(SLEEP)
        if ids:
            pmid, src = ids[0], "DOI"
            hit_doi += 1

        if not pmid:
            p, sim = pmid_by_title(r.get("title"))
            if p:
                pmid, src = p, "title(sim=%.2f)" % sim
                hit_title += 1

        if pmid:
            r["pmid"] = pmid
            r["pmid_source"] = "NCBI-eutils-backfill-20261017"
            print("  [%d/%d] %s  PMID %s  <- %s | %s"
                  % (i + 1, len(todo), doi[:42], pmid, src, (r.get("title") or "")[:52]),
                  flush=True)
        else:
            miss.append((doi, (r.get("title") or "")[:60]))

        if (i + 1) % 20 == 0:
            print("  ... %d/%d  doi=%d title=%d skipped=%d"
                  % (i + 1, len(todo), hit_doi, hit_title, skipped), flush=True)

    json.dump(d, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=2)

    # ---- 传播到时间戳副本与 _new.json（按 DOI 对齐）----
    by_doi = {r.get("doi"): r.get("pmid") for r in recs if r.get("doi") and r.get("pmid")}
    for tgt in ("search_results_20261016_030414.json", "search_results_20261016_030414_new.json"):
        try:
            t = json.load(open(tgt, encoding="utf-8"))
            trs = t["records"] if isinstance(t, dict) and "records" in t else t
            n = 0
            for r in trs:
                if not r.get("pmid") and by_doi.get(r.get("doi")):
                    r["pmid"] = by_doi[r["doi"]]
                    r["pmid_source"] = "NCBI-eutils-backfill-20261017"
                    n += 1
            json.dump(t, open(tgt, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
            print("  propagated %d PMID -> %s" % (n, tgt), flush=True)
        except FileNotFoundError:
            print("  (skip, not found) %s" % tgt, flush=True)

    remaining = sum(1 for r in recs if not r.get("pmid"))
    print("\nDONE  doi_hit=%d  title_hit=%d  skipped(preprint/dataset)=%d  still_missing=%d/%d"
          % (hit_doi, hit_title, skipped, remaining, len(recs)), flush=True)
    print("\n--- 仍未编目（多半为极新文献，属正常滞后，不可编造）---")
    for doi, t in miss[:40]:
        print("  %s | %s" % (doi[:52], t))


if __name__ == "__main__":
    main()
