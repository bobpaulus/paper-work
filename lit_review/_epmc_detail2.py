# -*- coding: utf-8 -*-
import json,urllib.request,urllib.parse,time
DOIS=["10.1210/endocr/bqag012","10.1002/cam4.71766","10.1007/s12672-026-04601-4",
"10.1038/s41540-026-00663-w","10.2147/itt.s565624","10.1007/s10238-026-02101-x",
"10.1016/j.jpha.2025.101354","10.21203/rs.3.rs-9248842/v1","10.1038/s11010-026-05604-z"]
out=[]
for doi in DOIS:
    url="https://www.ebi.ac.uk/europepmc/webservices/rest/search?"+urllib.parse.urlencode(
        {"query":'DOI:"%s"'%doi,"format":"json","resultType":"core","pageSize":1})
    try:
        req=urllib.request.Request(url,headers={"User-Agent":"lit-review/1.0"})
        with urllib.request.urlopen(req,timeout=40) as r:
            d=json.loads(r.read().decode("utf-8"))
        res=d.get("resultList",{}).get("result",[])
        if not res: print("MISS",doi); continue
        it=res[0]
        rec=dict(doi=doi,pmid=it.get("pmid"),title=it.get("title"),
                 journal=(it.get("journalInfo",{}).get("journal",{}) or {}).get("title") or it.get("journalTitle"),
                 date=it.get("firstPublicationDate"),isPreprint=it.get("source")=="PPR",
                 abstract=(it.get("abstractText") or "")[:1400],isOA=it.get("isOpenAccess"))
        out.append(rec)
        print("="*70); print(rec['date'],'|',rec['journal'],'| PMID',rec['pmid'],'| OA',rec['isOA'],'| PPR',rec['isPreprint'])
        print("T:",rec['title']); print("A:",rec['abstract'][:1200])
    except Exception as e: print("FAIL",doi,e)
    time.sleep(0.6)
json.dump(out,open('_epmc_detail2_run24.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
print("saved",len(out))
