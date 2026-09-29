#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Retry only the Crossref lookups that failed (SSL handshake timeout) in the
prior enrichment run; merge into existing search_results_20260911_enrich.json."""
import json, time, urllib.parse, urllib.request

MAIL = "lit-review@local"
OUT = "search_results_20260911_enrich.json"

def get(url, retries=1, timeout=12):
    last = None
    for _ in range(retries + 1):
        try:
            req = urllib.request.Request(
                url,
                headers={"User-Agent": f"lit-review (mailto:{MAIL})",
                         "Accept": "application/json"})
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return json.loads(r.read().decode("utf-8"))
        except Exception as e:
            last = e
            time.sleep(1.0)
    return {"_error": str(last)}

# load existing
d = json.load(open(OUT, encoding="utf-8"))

failed = [doi for doi, rec in d.items() if rec.get("crossref_error")]
print(f"retrying {len(failed)} crossref lookups", flush=True)

for doi in failed:
    rec = d[doi]
    try:
        c = get(f"https://api.crossref.org/works/{urllib.parse.quote(doi, safe='')}")
        if "message" in c:
            m = c["message"]
            rec["crossref_title"] = (m.get("title") or [""])[0]
            rec["crossref_journal"] = ((m.get("container-title") or [""])[0] or "")
            rec["crossref_year"] = (m.get("published") or {}).get("date-parts", [[""]])[0][0]
            rec["crossref_type"] = m.get("type")
            rec["crossref_pmid"] = m.get("pmid")
            rec.pop("crossref_error", None)
            print(f"  OK {doi}", flush=True)
        else:
            rec["crossref_error"] = c.get("_error")
            print(f"  STILL_FAIL {doi}: {c.get('_error')}", flush=True)
    except Exception as e:
        rec["crossref_error"] = str(e)
        print(f"  EXC {doi}: {e}", flush=True)

json.dump(d, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("RETRY_DONE", flush=True)
