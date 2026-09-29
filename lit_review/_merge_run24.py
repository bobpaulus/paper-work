# -*- coding: utf-8 -*-
import json,re,shutil
from collections import Counter
def norm(t):
    t=re.sub(r'[^a-z0-9 ]',' ',(t or '').lower()); t=re.sub(r'\s+',' ',t).strip()
    return t[:70]
base=json.load(open('search_results_latest.json',encoding='utf-8'))
brecs=base['records']
print("baseline records:",len(brecs))
bkeys=set()
for r in brecs:
    if r.get('doi'): bkeys.add(r['doi'].lower())
    bkeys.add(norm(r.get('title')))

oa=json.load(open('_run24_merged.json',encoding='utf-8'))
ep=json.load(open('_epmc_pack_run24.json',encoding='utf-8'))

new=[]; seen=set(); dup_within=0
for r in oa+ep:
    ks=[norm(r.get('title'))]+([r['doi'].lower()] if r.get('doi') else [])
    k=ks[0]
    if k in bkeys or any(x in bkeys for x in ks): continue
    if k in seen: dup_within+=1; continue
    seen.add(k)
    if r.get('doi'): seen.add(r['doi'].lower())
    new.append(r)
print("candidate new (dedup vs baseline & within):",len(new),"| within-run dup dropped:",dup_within)

# PRECISE deposit 与正文合并（同文多版本）
dep=[r for r in new if (r.get('doi') or '').startswith('10.1158/1078-0432.c.8568781')]
art=[r for r in new if r.get('doi')=='10.1158/1078-0432.ccr-25-4488']
if dep and art:
    for d in dep:
        new.remove(d)
        art[0]['versions']=list(set(art[0].get('versions',[])+[d['doi']]))
    print("merged PRECISE deposit into article; new now:",len(new))

allrecs=brecs+new
out=dict(base)
out['search_date']="2026-09-18T23:20:00+08:00"
out['window_from']="2026-06-20 (90d OpenAlex) + 2026-08-19 (30d OpenAlex) + EuropePMC 2025-06..2026-09 补检"
out['new_records']=new
out['records']=allrecs
s=out['summary']=dict(
  unique_records=len(allrecs),
  new_this_run=len(new),
  new_openalex=len([r for r in new if r.get('source')!='EuropePMC']),
  new_europepmc=len([r for r in new if r.get('source')=='EuropePMC']),
  relevance=dict(Counter(r['relevance'] for r in new)),
  dimensions=dict(Counter(dl for r in new for dl in r['dimension_labels'])),
  preprints=sum(1 for r in new if r.get('is_preprint')),
  sources=dict(Counter(r.get('source','OpenAlex') for r in new)),
  note="Run #24: OpenAlex 30d(7)+90d(52 含 30d) 主源 + EuropePMC 交叉补检 23 条（OpenAlex 查询矩阵系统性漏检）。")
json.dump(out,open('search_results_20260918_232000.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
json.dump(out,open('search_results_latest.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
print("baseline ->",len(allrecs))
print(json.dumps(out['summary'],ensure_ascii=False,indent=1))
