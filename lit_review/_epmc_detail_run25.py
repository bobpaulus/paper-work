# -*- coding: utf-8 -*-
import json, urllib.request, urllib.parse, time

DOIS = [
 "10.1126/sciadv.aee5417",
 "10.20945/2359-4292-2026-0083",
 "10.1002/smtd.71048",
 "10.1007/s00432-026-06538-1",
 "10.1186/s12957-026-04483-4",
 "10.1007/s00259-026-08100-0",
 "10.3390/ijms27146131",
 "10.1007/s12149-026-02252-7",
 "10.3390/cancers18132093",
 "10.21037/gs-2026-0217",
 "10.1007/s10278-026-02236-z",
 "10.1007/s10278-026-02208-3",
 "10.21037/gs-2026-0304",
 "10.3390/metabo16080580",
 "10.1007/s12149-026-02258-1",
 "10.1016/j.ctarc.2026.101434",
 "10.1016/j.artmed.2026.103500",
 "10.1097/mnm.0000000000002163",
 "10.1007/s13304-026-02781-w",
 "10.3791/72803",
 "10.3389/fonc.2026.1858599",
 "10.1016/j.jasc.2026.07.001",
]

def rebuild(inv):
    if not inv: return ""
    pos = {}
    for w, idxs in inv.items():
        for i in idxs: pos[i] = w
    return " ".join(pos[i] for i in sorted(pos)) if pos else ""

out = {}
for doi in DOIS:
    url = "https://api.openalex.org/works/doi:" + doi
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "lit-review (mailto:lit-review@local)"})
        with urllib.request.urlopen(req, timeout=40) as r:
            w = json.loads(r.read().decode("utf-8"))
    except Exception as e:
        print("FAIL", doi, e); time.sleep(1); continue
    ids = w.get("ids") or {}
    pmid = (ids.get("pmid") or "").rsplit("/", 1)[-1] or None
    out[doi] = dict(
        title=w.get("title"), pmid=pmid, doi=doi,
        date=w.get("publication_date"), type=w.get("type"),
        venue=((w.get("primary_location") or {}).get("source") or {}).get("display_name"),
        oa_status=(w.get("open_access") or {}).get("oa_status"),
        oa_url=(w.get("best_oa_location") or {}).get("pdf_url") or (w.get("best_oa_location") or {}).get("landing_page_url"),
        cited=w.get("cited_by_count", 0),
        abstract=rebuild(w.get("abstract_inverted_index"))[:1800],
    )
    print("==", doi, "|", out[doi]["date"], "|", out[doi]["venue"], "| OA", out[doi]["oa_status"])
    print("   ", (out[doi]["title"] or "")[:160])
    print("   ABS:", out[doi]["abstract"][:900])
    print()
    time.sleep(0.4)

json.dump(out, open("search_results_20260925_epmc_detail.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
