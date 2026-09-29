# -*- coding: utf-8 -*-
import json, urllib.request, urllib.parse, time

def q(query, page=1, ps=50):
    url = "https://www.ebi.ac.uk/europepmc/webservices/rest/search?" + urllib.parse.urlencode(
        {"query": query, "format": "json", "page": page, "pageSize": ps, "sort": "P_PDATE_D desc"})
    req = urllib.request.Request(url, headers={"User-Agent": "lit-review/1.0"})
    with urllib.request.urlopen(req, timeout=40) as r:
        return json.loads(r.read().decode("utf-8"))

QS = {
 "SC": '(TITLE:"thyroid") AND (TITLE:"single-cell" OR TITLE:"single cell" OR ABSTRACT:"scRNA-seq") AND (PUB_YEAR:2026)',
 "SP": '(TITLE:"thyroid") AND (TITLE:"spatial" OR ABSTRACT:"spatial transcriptomics") AND (PUB_YEAR:2026)',
 "IM": '(TITLE:"thyroid") AND (TITLE:"tumor microenvironment" OR TITLE:"tumour microenvironment" OR TITLE:"macrophage") AND (PUB_YEAR:2026)',
 "ME": '(TITLE:"thyroid") AND (TITLE:"metabolic" OR TITLE:"metabolism" OR TITLE:"ferroptosis" OR TITLE:"glycolysis") AND (PUB_YEAR:2026)',
 "AL": '(TITLE:"thyroid") AND (TITLE:"machine learning" OR TITLE:"deep learning" OR TITLE:"radiomics" OR TITLE:"nomogram") AND (PUB_YEAR:2026)',
 "ST": '(TITLE:"thyroid") AND (TITLE:"stemness" OR TITLE:"dedifferentiation" OR TITLE:"cancer stem cell") AND (PUB_YEAR:2026)',
}

def norm(t):
    return "".join(c for c in (t or "").lower() if c.isalnum())[:90]

base_doi, base_ti = set(), set()
d = json.load(open('search_results_latest.json', encoding='utf-8'))
for r in d.get('records', []):
    if r.get('doi'):
        base_doi.add(r['doi'].lower())
    if r.get('title'):
        base_ti.add(norm(r['title']))
# 本轮 OpenAlex 两路已捞到的也算已见
mine_doi, mine_ti = set(), set()
for f in ('search_results_20260925_030100.json', 'search_results_20260925_90day.json'):
    dd = json.load(open(f, encoding='utf-8'))
    for r in dd.get('records', []):
        if r.get('doi'):
            mine_doi.add(r['doi'].lower())
        if r.get('title'):
            mine_ti.add(norm(r['title']))

res = {}
for k, v in QS.items():
    try:
        dd = q(v)
        hits = dd.get("hitCount", 0)
        items = []
        for it in dd.get("resultList", {}).get("result", []):
            doi = (it.get("doi") or "").lower()
            ti = norm(it.get("title"))
            if (doi and doi in base_doi) or (doi and doi in mine_doi) or ti in base_ti or ti in mine_ti:
                continue
            items.append(dict(title=it.get("title"), doi=it.get("doi"), pmid=it.get("pmid"),
                              journal=it.get("journalTitle"), date=it.get("firstPublicationDate"),
                              isPreprint=it.get("source") == "PPR",
                              abstract=(it.get("abstractText") or "")[:600]))
        res[k] = dict(hitCount=hits, candidates=items)
        print(f"[{k}] hit={hits} 候选新={len(items)}")
        for it in items[:14]:
            print("   -", it['date'], it['title'][:110], "|", it['doi'], "| PMID", it['pmid'])
    except Exception as e:
        res[k] = dict(error=str(e))
        print(f"[{k}] FAIL {e}")
    time.sleep(1)

json.dump(res, open('search_results_20260925_epmc.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
