#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Retry only Unpaywall lookups that failed (SSL handshake timeout) in prior
enrichment; merge into existing search_results_20260911_enrich.json."""
import json, time, urllib.parse, urllib.request

MAIL = "lit-review@local"
OUT = "search_results_20260911_enrich.json"

def get(url, retries=1, timeout=10):
    last = None
    for _ in range(retries + 1):
        try:
            req = urllib.request.Request(url, headers={
                "User-Agent": f"lit-review (mailto:{MAIL})", "Accept": "application/json"})
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return json.loads(r.read().decode("utf-8"))
        except Exception as e:
            last = e
            time.sleep(1.0)
    return {"_error": str(last)}

d = json.load(open(OUT, encoding="utf-8"))
failed = [doi for doi, rec in d.items() if rec.get("unpaywall_error")]
print(f"retrying {len(failed)} unpaywall lookups", flush=True)

for doi in failed:
    rec = d[doi]
    try:
        u = get(f"https://api.unpaywall.org/v2/{urllib.parse.quote(doi, safe='')}?email={MAIL}")
        if "doi" in u:
            rec["unpaywall_oa_status"] = u.get("oa_status")
            rec["unpaywall_oa_url"] = (u.get("best_oa_location") or {}).get("pdf_url")
            rec["unpaywall_journal_is_oa"] = u.get("journal_is_oa")
            rec.pop("unpaywall_error", None)
            print(f"  OK {doi} -> {u.get('oa_status')}", flush=True)
        else:
            rec["unpaywall_error"] = u.get("_error")
            print(f"  STILL_FAIL {doi}: {u.get('_error')}", flush=True)
    except Exception as e:
        rec["unpaywall_error"] = str(e)
        print(f"  EXC {doi}: {e}", flush=True)

json.dump(d, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("UNPAYWALL_RETRY_DONE", flush=True)
