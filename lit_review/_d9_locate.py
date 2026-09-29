#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""D9 pre-research: locate public datasets referenced by Run #22 report.
OpenAlex (stable) for theme works + Zenodo API for the two deposits.
"""
import json, time, urllib.parse, urllib.request

MAIL = "lit-review@local"
def get(url, retries=2, timeout=20):
    last = None
    for _ in range(retries + 1):
        try:
            req = urllib.request.Request(url, headers={
                "User-Agent": f"lit-review (mailto:{MAIL})", "Accept": "application/json"})
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return json.loads(r.read().decode("utf-8"))
        except Exception as e:
            last = e; time.sleep(1.2)
    return {"_error": str(last)}

OUT = "d9_dataset_inventory.json"
inv = {"themes": {}, "zenodo_deposits": {}}

themes = {
    "SPP1_TAM_PTC": "SPP1 macrophage papillary thyroid carcinoma lymph node metastasis",
    "POSTN_myCAF_spatial": "POSTN myCAF spatial transcriptomics thyroid carcinoma",
    "paired_primary_LNM_scRNA": "paired primary lymph node metastasis single cell thyroid carcinoma",
    "TREM2_macrophage_thyroid": "TREM2 macrophage thyroid carcinoma spatial",
}
for name, q in themes.items():
    url = ("https://api.openalex.org/works?search="
           + urllib.parse.quote(q)
           + "&filter=from_publication_date:2024-01-01&sort=relevance_score:desc&per-page=6")
    d = get(url)
    rows = []
    if "results" in d:
        for w in d["results"]:
            rows.append({
                "title": (w.get("title") or "")[:160],
                "doi": (w.get("doi") or ""),
                "year": (w.get("publication_year") or ""),
                "cited_by": w.get("cited_by_count", 0),
                "oa": (w.get("open_access") or {}).get("oa_status"),
                "is_preprint": (w.get("type") == "preprint"),
                "ids": w.get("ids", {}),
            })
    inv["themes"][name] = rows
    print(f"[{name}] hits={len(rows)}")
    for r in rows[:3]:
        print(f"   {r['year']} {r['cited_by']}cit {r['oa']}  {r['title'][:80]}")
    time.sleep(0.5)

# Zenodo deposits referenced in report
for label, rec_id in [("SPP1_TAM_multiomics", "22290057"),
                      ("TLS_spatial_archive", "22661715")]:
    z = get(f"https://zenodo.org/api/records/{rec_id}")
    if "metadata" in z:
        md = z["metadata"]
        files = [f.get("key") for f in z.get("files", [])]
        inv["zenodo_deposits"][label] = {
            "rec_id": rec_id,
            "title": md.get("title"),
            "upload_type": md.get("upload_type"),
            "resource_type": (md.get("resource_type") or {}).get("type"),
            "doi": z.get("doi"),
            "license": (md.get("license") or {}).get("id") if isinstance(md.get("license"), dict) else md.get("license"),
            "files": files[:20],
            "n_files": len(files),
        }
        print(f"[Zenodo {label}] {md.get('title')} | type={md.get('upload_type')} | files={len(files)}")
    else:
        inv["zenodo_deposits"][label] = {"_error": z.get("_error")}
        print(f"[Zenodo {label}] ERROR {z.get('_error')}")

json.dump(inv, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print(f"\nWrote {OUT}")
