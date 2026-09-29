# -*- coding: utf-8 -*-
"""Run #25: D3 定向深挖 — 基线查重 + 摘要抽取 + 扩检"""
import json, urllib.request, urllib.parse, time, re, unicodedata
MAILTO = "lit-review@local"

def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": f"lit-review/1.0 (mailto:{MAILTO})"})
    with urllib.request.urlopen(req, timeout=35) as r:
        return json.loads(r.read().decode("utf-8"))

def norm(t):
    t = re.sub(r"</?[a-zA-Z]+>", "", (t or "")).strip()
    t = unicodedata.normalize("NFKD", t).lower()
    return re.sub(r"[^a-z0-9]+", "", t)[:90]

base = json.load(open('search_results_latest.json', encoding='utf-8'))
base_doi, base_ti = set(), set()
for r in base.get('records', []):
    if r.get('doi'): base_doi.add(r['doi'].lower())
    if r.get('title'): base_ti.add(norm(r['title']))
print('基线', len(base.get('records', [])), '条')

QUERIES = {
 "D3-MGST1": 'title_and_abstract.search:thyroid AND MGST1',
 "D3-APOE": 'title_and_abstract.search:(thyroid) AND (APOE OR "apolipoprotein E")',
 "D3-lipid": 'title_and_abstract.search:("thyroid cancer" OR "thyroid carcinoma") AND ("lipid metabolism" OR "lipid metabolic" OR "metabolic reprogramming")',
 "D3-immunomet": 'title_and_abstract.search:("thyroid carcinoma" OR "thyroid cancer") AND ("immunometabolism" OR "metabolic-immune" OR "immune metabolic")',
 "SP-review": 'title_and_abstract.search:(thyroid) AND ("spatial transcriptomics" OR "spatial omics")',
 "SC-atlas": 'title_and_abstract.search:("thyroid carcinoma" OR "thyroid cancer") AND ("single-cell" OR "single nucleus" OR scRNA-seq)',
 "ME-ferro": 'title_and_abstract.search:("thyroid carcinoma" OR "thyroid cancer" OR "anaplastic thyroid") AND (ferroptosis OR cuproptosis)',
}

def rebuild(inv):
    if not inv: return ""
    pos = {}
    for w, idxs in inv.items():
        for i in idxs: pos[i] = w
    return " ".join(pos[i] for i in sorted(pos)) if pos else ""

out = {}
for name, f in QUERIES.items():
    url = ("https://api.openalex.org/works?filter=" + urllib.parse.quote(f) +
           ",from_publication_date:2026-01-01&sort=publication_date:desc&per-page=30&mailto=" + MAILTO)
    try:
        d = get(url)
    except Exception as e:
        print(name, "FAIL", e); time.sleep(1); continue
    items, newcnt = [], 0
    for w in d.get("results", []):
        title = w.get("title") or ""
        doi = (w.get("doi") or "").replace("https://doi.org/", "")
        isnew = (doi.lower() not in base_doi) and (norm(title) not in base_ti)
        if isnew: newcnt += 1
        items.append(dict(title=title, doi=doi, date=w.get("publication_date"),
                          pmid=((w.get("ids") or {}).get("pmid") or "").rsplit("/", 1)[-1] or None,
                          type=w.get("type"), preprint=w.get("type") == "preprint",
                          oa=(w.get("open_access") or {}).get("oa_status"),
                          venue=((w.get("primary_location") or {}).get("source") or {}).get("display_name"),
                          cited=w.get("cited_by_count", 0), is_new=isnew,
                          abstract=rebuild(w.get("abstract_inverted_index"))[:1200]))
    out[name] = dict(count=d["meta"]["count"], new=newcnt, items=items)
    print(f"[{name}] hit={d['meta']['count']} 新={newcnt}")
    for it in items:
        if it["is_new"] and it["date"] and it["date"] >= "2026-06-01":
            print("   NEW", it["date"], it["title"][:118], "|", it["doi"], "| PMID", it["pmid"], "|", it["oa"])
    time.sleep(0.6)

json.dump(out, open("search_results_20260925_d3deep.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
