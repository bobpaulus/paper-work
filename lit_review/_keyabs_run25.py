# -*- coding: utf-8 -*-
"""Run #25: 关键新证据摘要抽取"""
import json, urllib.request, urllib.parse, time
MAILTO = "lit-review@local"

def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": f"lit-review/1.0 (mailto:{MAILTO})"})
    with urllib.request.urlopen(req, timeout=35) as r:
        return json.loads(r.read().decode("utf-8"))

def rebuild(inv):
    if not inv: return ""
    pos = {}
    for w, idxs in inv.items():
        for i in idxs: pos[i] = w
    return " ".join(pos[i] for i in sorted(pos)) if pos else ""

TARGETS = [
 ("MGST1-LNM-PTC", "10.3389/fimmu.2026.1848083"),
 ("APOE-PINK1-mitophagy-PTC", "10.21037/tcr-2026-0796"),
 ("GPI-THBS1-ATC", "10.1016/j.canlet.2026.218650"),
 ("SPP1-TAM-ATC-scRNA", "10.1186/s12885-026-16648-1"),
 ("cGAS-STING-ATC", "10.1177/10507256261481666"),
 ("SGLT2-DPP-PTC", "10.3389/fmolb.2026.1875059"),
 ("BRAF-CNS-thyroid-brain-met", "10.3389/fneur.2026.1921351"),
 ("TCGA-TCM-PTC-APOE", "10.1097/md.0000000000050562"),
 ("PHGDH-dabrafenib-ATC", "10.1038/s41420-026-03293-7"),
 ("Microenv-plasticity-RAI", "10.3390/ijms27167305"),
 ("Cuproptosis-mito-TC", "10.1007/s11010-026-05604-z"),
 ("Lipid-metab-preprint", "10.20944/preprints202608.0708.v1"),
 ("SpatialTx-review-preprint", "10.20944/preprints202608.0302.v1"),
]

res = {}
for name, doi in TARGETS:
    try:
        w = get(f"https://api.openalex.org/works/doi:{urllib.parse.quote(doi)}")
    except Exception as e:
        print("FAIL", name, doi, str(e)[:100]); time.sleep(1); continue
    res[name] = dict(doi=doi, title=w.get("title"), date=w.get("publication_date"),
                     pmid=((w.get("ids") or {}).get("pmid") or "").rsplit("/", 1)[-1] or None,
                     type=w.get("type"), oa=(w.get("open_access") or {}).get("oa_status"),
                     venue=((w.get("primary_location") or {}).get("source") or {}).get("display_name"),
                     cited=w.get("cited_by_count", 0),
                     abstract=rebuild(w.get("abstract_inverted_index"))[:1700])
    r = res[name]
    print("==", name, "|", r["date"], "|", r["venue"], "| OA", r["oa"], "| PMID", r["pmid"] or "待编目")
    print("   ", (r["title"] or "")[:150])
    print("   ABS:", r["abstract"][:1000])
    print()
    time.sleep(0.4)

# HIF-1α / ferroptosis ATC 主文定位
print("=== HIF-1α ferroptosis ATC 主文定位 ===")
try:
    d = get("https://api.openalex.org/works?filter=" + urllib.parse.quote(
        'title_and_abstract.search:("anaplastic thyroid") AND (HIF-1 OR HIF1A) AND (ferroptosis OR ACSL4)') +
        "&sort=publication_date:desc&per-page=6&mailto=" + MAILTO)
    for w in d.get("results", []):
        print("   -", w.get("publication_date"), (w.get("title") or "")[:130])
        print("     DOI", (w.get("doi") or "").replace("https://doi.org/", ""),
              "| PMID", ((w.get("ids") or {}).get("pmid") or "").rsplit("/", 1)[-1] or "待编目",
              "| OA", (w.get("open_access") or {}).get("oa_status"))
except Exception as e:
    print("FAIL", e)

# Multi-omics causal thyroid women of reproductive age 主文定位
print("\n=== Multi-omics causal TC (women reproductive age) 主文定位 ===")
try:
    d = get("https://api.openalex.org/works?filter=" + urllib.parse.quote(
        'title_and_abstract.search:thyroid AND ("women of reproductive age" OR "reproductive age")') +
        "&sort=publication_date:desc&per-page=6&mailto=" + MAILTO)
    for w in d.get("results", []):
        print("   -", w.get("publication_date"), (w.get("title") or "")[:130])
        print("     DOI", (w.get("doi") or "").replace("https://doi.org/", ""),
              "| PMID", ((w.get("ids") or {}).get("pmid") or "").rsplit("/", 1)[-1] or "待编目",
              "| OA", (w.get("open_access") or {}).get("oa_status"))
except Exception as e:
    print("FAIL", e)

json.dump(res, open("search_results_20260925_keyabs.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
