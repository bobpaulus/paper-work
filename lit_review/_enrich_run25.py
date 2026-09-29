# -*- coding: utf-8 -*-
"""Run #25: Crossref 元数据校验 + Unpaywall OA 解析 + D3 定向复查 (APOE/MGST1) + PRECISE 主文定位"""
import json, urllib.request, urllib.parse, time

MAILTO = "lit-review@local"

def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": f"lit-review/1.0 (mailto:{MAILTO})"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read().decode("utf-8"))

HIGH = {
 "10.1186/s13044-026-00314-6": "Intratumor microbiota in thyroid cancer",
 "10.3389/fimmu.2026.1912827": "US radiomics immune-inflammatory CLNM PTC",
 "10.1177/15330338261490262": "US radiomics+DL LNM/BRAF PTC",
 "10.1126/sciadv.aee5417": "LOH germline complex I Warburg OCT",
 "10.20945/2359-4292-2026-0083": "GSEC/IGF2BP2/GLUT1 PTC glycolysis",
 "10.21037/gs-2026-0217": "radiomics transportability/calibration drift cN0 CLNM",
 "10.1007/s00330-026-12806-y": "CT habitat imaging occult CLNM",
 "10.1002/smtd.71048": "Au-mesoporous carbon serum metabolic fingerprint PTC",
 "10.1007/s00432-026-06538-1": "TAIII+Auranofin liposome ferroptosis ATC",
 "10.1007/s00259-026-08100-0": "FDG PET volumetric ATC prognosis",
}

res = {}
for doi, label in HIGH.items():
    row = {"label": label, "doi": doi}
    try:
        c = get(f"https://api.crossref.org/works/{urllib.parse.quote(doi)}")["message"]
        row["crossref"] = dict(
            title=(c.get("title") or [None])[0],
            container=(c.get("container-title") or [None])[0],
            publisher=c.get("publisher"),
            issued=c.get("issued", {}).get("date-parts"),
            type=c.get("type"),
            ref_count=c.get("reference-count"),
        )
        row["crossref_ok"] = True
    except Exception as e:
        row["crossref_ok"] = False
        row["crossref_err"] = str(e)[:120]
    time.sleep(0.5)
    try:
        u = get(f"https://api.unpaywall.org/v2/{urllib.parse.quote(doi)}?email={MAILTO}")
        row["unpaywall"] = dict(is_oa=u.get("is_oa"), oa_status=(u.get("oa_status") or {}).get if False else u.get("oa_status"),
                                best=(u.get("best_oa_location") or {}).get("url_for_pdf") or (u.get("best_oa_location") or {}).get("url"),
                                journal_is_oa=u.get("journal_is_oa"))
        row["unpaywall_ok"] = True
    except Exception as e:
        row["unpaywall_ok"] = False
        row["unpaywall_err"] = str(e)[:120]
    time.sleep(0.5)
    res[doi] = row
    print(doi, "| CR", row.get("crossref_ok"), "| UP", row.get("unpaywall_ok"), "|", label)

json.dump(res, open("search_results_20260925_enrich.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)

# ---------------- D3 定向复查：APOE / MGST1 ----------------
print("\n=== D3 定向复查 (APOE / MGST1 / 代谢-免疫干性亚群) ===")
D3Q = [
 ("D3-APOE", 'title_and_abstract.search:thyroid AND (APOE OR "apolipoprotein E")'),
 ("D3-MGST1", 'title_and_abstract.search:thyroid AND MGST1'),
 ("D3-lipid-stem", 'title_and_abstract.search:("thyroid cancer" OR "thyroid carcinoma") AND ("lipid metabolism" OR "metabolic") AND (stemness OR "cancer stem")'),
]
d3 = {}
for name, f in D3Q:
    url = ("https://api.openalex.org/works?filter=" + urllib.parse.quote(f) +
           "&sort=publication_date:desc&per-page=20&mailto=" + MAILTO)
    try:
        d = get(url)
        items = []
        for w in d.get("results", []):
            items.append(dict(title=w.get("title"), doi=(w.get("doi") or "").replace("https://doi.org/", ""),
                              date=w.get("publication_date"),
                              pmid=((w.get("ids") or {}).get("pmid") or "").rsplit("/", 1)[-1] or None,
                              venue=((w.get("primary_location") or {}).get("source") or {}).get("display_name")))
        d3[name] = dict(count=d["meta"]["count"], items=items)
        print(f"[{name}] hit={d['meta']['count']}")
        for it in items[:10]:
            print("   -", it["date"], (it["title"] or "")[:110], "|", it["doi"], "| PMID", it["pmid"])
    except Exception as e:
        d3[name] = dict(error=str(e)[:150]); print(f"[{name}] FAIL {e}")
    time.sleep(0.6)

# ---------------- PRECISE 主文定位 ----------------
print("\n=== PRECISE 主文定位 ===")
try:
    url = ("https://api.openalex.org/works?filter=" + urllib.parse.quote('title_and_abstract.search:PRECISE thyrocyte papillary thyroid carcinoma prognostic signature') +
           "&sort=publication_date:desc&per-page=6&mailto=" + MAILTO)
    d = get(url)
    for w in d.get("results", []):
        print("   -", w.get("publication_date"), (w.get("title") or "")[:130])
        print("     DOI", (w.get("doi") or "").replace("https://doi.org/", ""),
              "| PMID", ((w.get("ids") or {}).get("pmid") or "").rsplit("/", 1)[-1] or "待编目",
              "| OA", (w.get("open_access") or {}).get("oa_status"),
              "| venue", ((w.get("primary_location") or {}).get("source") or {}).get("display_name"))
    d3["PRECISE"] = [dict(title=w.get("title"), doi=(w.get("doi") or "").replace("https://doi.org/", ""),
                          date=w.get("publication_date"),
                          pmid=((w.get("ids") or {}).get("pmid") or "").rsplit("/", 1)[-1] or None,
                          oa=(w.get("open_access") or {}).get("oa_status"),
                          venue=((w.get("primary_location") or {}).get("source") or {}).get("display_name"))
                     for w in d.get("results", [])]
except Exception as e:
    print("PRECISE FAIL", e)

json.dump(d3, open("search_results_20260925_d3check.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
