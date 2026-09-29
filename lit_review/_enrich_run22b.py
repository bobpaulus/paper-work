#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Robust enrichment: Crossref + Unpaywall for High/key DOIs.
Flushes to search_results_20260911_enrich.json after EVERY item so partial
progress survives hangs/timeouts. Per-request timeout 15s, 1 retry.
"""
import json, time, urllib.parse, urllib.request

MAIL = "lit-review@local"
OUT = "search_results_20260911_enrich.json"

def get(url, retries=1, timeout=15):
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

items = [
    ("10.3390/cancers18182918", "IL1beta/SMDT1-MAPK PTC"),
    ("10.1186/s12885-026-16883-6", "systemic inflammatory/immune DTC"),
    ("10.5281/zenodo.22290057", "SPP1+ TAM AI multi-omics"),
    ("10.3389/fimmu.2026.1916192", "TIME thyroid vs colorectal"),
    ("10.1016/j.mcp.2026.102086", "creatine/alpha-linolenic acid metabolomics"),
    ("10.3389/fonc.2026.1810543", "SYTL5 DTC"),
    ("10.1530/erc-26-0026", "DKK1 PTC/FTC"),
    ("10.1002/path.70116", "miR-145-3p MTC metastatic"),
    ("10.1002/cam4.72220", "UTMD CSF-1 macrophage ferroptosis PTC"),
    ("10.1002/adbi.70156", "MAPK synthetic inhibitors perspective"),
    ("10.3389/fendo.2026.1853172", "nomogram occult CLNM PTMC"),
    ("10.1371/journal.pone.0355343", "68Ga-FAPI-04 PET/CT DTC"),
]

out = {}
for doi, label in items:
    rec = {"label": label, "doi": doi}
    try:
        c = get(f"https://api.crossref.org/works/{urllib.parse.quote(doi, safe='')}")
        if "message" in c:
            m = c["message"]
            rec["crossref_title"] = (m.get("title") or [""])[0]
            rec["crossref_journal"] = ((m.get("container-title") or [""])[0] or "")
            rec["crossref_year"] = (m.get("published") or {}).get("date-parts", [[""]])[0][0]
            rec["crossref_type"] = m.get("type")
            rec["crossref_pmid"] = m.get("pmid")
        else:
            rec["crossref_error"] = c.get("_error")
    except Exception as e:
        rec["crossref_error"] = str(e)
    try:
        u = get(f"https://api.unpaywall.org/v2/{urllib.parse.quote(doi, safe='')}?email={MAIL}")
        if "doi" in u:
            rec["unpaywall_oa_status"] = u.get("oa_status")
            rec["unpaywall_oa_url"] = (u.get("best_oa_location") or {}).get("pdf_url")
            rec["unpaywall_journal_is_oa"] = u.get("journal_is_oa")
        else:
            rec["unpaywall_error"] = u.get("_error")
    except Exception as e:
        rec["unpaywall_error"] = str(e)
    out[doi] = rec
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print(f"OK {doi}  {label}", flush=True)

print("ENRICH_DONE", flush=True)
