# -*- coding: utf-8 -*-
import json,urllib.request,urllib.parse,time
def q(query,page=1,ps=50):
    url="https://www.ebi.ac.uk/europepmc/webservices/rest/search?"+urllib.parse.urlencode(
        {"query":query,"format":"json","page":page,"pageSize":ps,"sort":"P_PDATE_D desc"})
    req=urllib.request.Request(url,headers={"User-Agent":"lit-review/1.0"})
    with urllib.request.urlopen(req,timeout=40) as r:
        return json.loads(r.read().decode("utf-8"))
QS={
 "SC":'(TITLE:"thyroid") AND (TITLE:"single-cell" OR TITLE:"single cell" OR ABSTRACT:"scRNA-seq") AND (PUB_YEAR:2026)',
 "SP":'(TITLE:"thyroid") AND (TITLE:"spatial" OR ABSTRACT:"spatial transcriptomics") AND (PUB_YEAR:2026)',
 "IM":'(TITLE:"thyroid") AND (TITLE:"tumor microenvironment" OR TITLE:"tumour microenvironment" OR TITLE:"macrophage") AND (PUB_YEAR:2026)',
}
base=set()
for f in ('search_results_latest.json',):
    d=json.load(open(f,encoding='utf-8'))
    for r in d.get('records',[]):
        if r.get('doi'): base.add(r['doi'].lower())
        t=(r.get('title') or '').lower()[:60]
        if t: base.add(t)
mine=set()
for r in json.load(open('_run24_merged.json',encoding='utf-8')):
    if r.get('doi'): mine.add(r['doi'].lower())
res={}
for k,v in QS.items():
    try:
        d=q(v)
        hits=d.get("hitCount",0)
        items=[]
        for it in d.get("resultList",{}).get("result",[]):
            doi=(it.get("doi") or "").lower()
            ti=(it.get("title") or "").lower()[:60]
            if doi in base or doi in mine or ti in base: continue
            items.append(dict(title=it.get("title"),doi=it.get("doi"),pmid=it.get("pmid"),
                              journal=it.get("journalTitle"),date=it.get("firstPublicationDate"),
                              isPreprint=it.get("source")=="PPR",abstract=(it.get("abstractText") or "")[:400]))
        res[k]=dict(hitCount=hits,candidates=items)
        print(f"[{k}] hit={hits} 候选新={len(items)}")
        for it in items[:12]: print("   -",it['date'],it['title'][:110],"|",it['doi'])
    except Exception as e:
        res[k]=dict(error=str(e)); print(f"[{k}] FAIL {e}")
    time.sleep(1)
json.dump(res,open('search_results_20260918_epmc.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
