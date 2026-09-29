# -*- coding: utf-8 -*-
import json, urllib.request, urllib.parse, time, ssl
MAILTO="lit-review@local"
ctx=ssl.create_default_context(); ctx.check_hostname=False; ctx.verify_mode=ssl.CERT_NONE
def get(url,timeout=25):
    req=urllib.request.Request(url,headers={"User-Agent":f"lit-review/1.0 (mailto:{MAILTO})"})
    with urllib.request.urlopen(req,timeout=timeout,context=ctx) as r:
        return json.loads(r.read().decode("utf-8"))

recs=json.load(open('_run24_merged.json',encoding='utf-8'))
targets=[r for r in recs if r['relevance']=='High' and r.get('doi')]
# 追加两条重点补充：HOXC10-CCL2 TAM 预印本 / Science Advances 已在 High
extra=[r for r in recs if 'HOXC10' in (r['title'] or '') or 'DLL4' in (r['title'] or '') or 'PRECISE' in (r['title'] or '')]
seen={r['doi'] for r in targets}
for r in extra:
    if r.get('doi') and r['doi'] not in seen: targets.append(r); seen.add(r['doi'])

out=[]
for r in targets:
    doi=r['doi']; e={"doi":doi,"title":r['title'][:120]}
    # Crossref
    try:
        c=get("https://api.crossref.org/works/"+urllib.parse.quote(doi))
        m=c["message"]
        e["cr_title"]=m.get("title",[None])[0]
        e["cr_journal"]=(m.get("container-title") or [None])[0]
        e["cr_publisher"]=m.get("publisher")
        e["cr_type"]=m.get("type")
        e["cr_year"]=(m.get("issued",{}).get("date-parts") or [[None]])[0][0]
        e["cr_author"]=(m.get("author") or [{}])[0].get("family")
        e["cr_status"]="OK"
    except Exception as ex:
        e["cr_status"]="FAIL: %s"%ex
    time.sleep(0.5)
    # Unpaywall
    try:
        u=get("https://api.unpaywall.org/v2/"+urllib.parse.quote(doi)+"?email="+MAILTO)
        e["up_oa"]=u.get("is_oa"); e["up_status"]=u.get("oa_status")
        best=(u.get("best_oa_location") or {})
        e["up_pdf"]=best.get("url_for_pdf"); e["up_landing"]=best.get("url")
        e["up_journal"]=u.get("journal_name")
        e["up_status_api"]="OK"
    except Exception as ex:
        e["up_status_api"]="FAIL: %s"%ex
    time.sleep(0.5)
    out.append(e)
    print(doi, "| CR:",e.get("cr_status"), "| UP:",e.get("up_status_api"), "|", (e.get("cr_journal") or "")[:45], "|", e.get("up_status"))
json.dump(out,open('search_results_20260918_enrich.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
print("saved",len(out))
