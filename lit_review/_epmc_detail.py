# -*- coding: utf-8 -*-
import json,urllib.request,urllib.parse,time
DOIS=["10.1007/s12672-026-05061-6","10.1080/15476278.2026.2670152","10.1530/erc-26-0088",
"10.1002/path.70104","10.1002/cam4.72261","10.3390/ijms27167387","10.1093/gpbjnl/qzag060",
"10.1158/1078-0432.ccr-25-4488","10.1038/s41416-026-03467-1","10.1186/s13046-026-03675-w",
"10.1038/s41598-026-41927-z","10.1016/j.xcrm.2026.102661","10.1007/s12020-026-04552-4",
"10.1007/s00405-026-10456-w","10.1186/s13044-026-00306-6"]
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
        rec=dict(doi=doi,pmid=it.get("pmid"),title=it.get("title"),journal=it.get("journalInfo",{}).get("journal",{}).get("title") or it.get("journalTitle"),
                 date=it.get("firstPublicationDate"),isPreprint=it.get("source")=="PPR",
                 abstract=(it.get("abstractText") or "")[:1800],cited=it.get("citedByCount"),
                 isOA=it.get("isOpenAccess"),aff=(it.get("affiliation") or "")[:120])
        out.append(rec)
        print("="*70); print(rec['date'],'|',rec['journal'],'| PMID',rec['pmid'],'| OA',rec['isOA'],'| cited',rec['cited'])
        print("T:",rec['title']); print("A:",rec['abstract'][:1500])
    except Exception as e:
        print("FAIL",doi,e)
    time.sleep(0.6)
json.dump(out,open('_epmc_detail_run24.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
print("saved",len(out))
