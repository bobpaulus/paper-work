# -*- coding: utf-8 -*-
import json, re, unicodedata
from collections import Counter, OrderedDict

def norm(t):
    t = re.sub(r"</?[a-zA-Z]+>", "", (t or "")).strip()
    t = unicodedata.normalize("NFKD", t).lower()
    return re.sub(r"[^a-z0-9]+", "", t)[:90]

base = json.load(open('search_results_latest.json', encoding='utf-8'))
base_doi, base_ti, base_pm = set(), set(), set()
for r in base.get('records', []):
    if r.get('doi'): base_doi.add(r['doi'].lower())
    if r.get('title'): base_ti.add(norm(r['title']))
    if r.get('pmid'): base_pm.add(str(r['pmid']))
print('基线记录数', len(base.get('records', [])), '| doi键', len(base_doi))

store = OrderedDict()
for f in ('search_results_20260925_030100.json', 'search_results_20260925_90day.json'):
    d = json.load(open(f, encoding='utf-8'))
    for r in d['new_records']:
        k = norm(r['title'])
        if k in store:
            cur = store[k]
            for dd in r.get('dimensions', []):
                if dd not in cur['dimensions']: cur['dimensions'].append(dd)
            if r.get('pmid') and not cur.get('pmid'): cur['pmid'] = r['pmid']
            continue
        store[k] = r
print('OpenAlex 两路合并后唯一新增:', len(store))

out = list(store.values())
for r in out:
    r['dimension_labels'] = r.get('dimension_labels') or []
json.dump(out, open('_run25_oa_new.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

print('\n--- 全部新增（按日期倒序）---')
for r in sorted(out, key=lambda x: x['publication_date'] or '', reverse=True):
    tag = ' [PREPRINT]' if r.get('is_preprint') else ''
    print(f"{r['publication_date']} [{r['relevance']:<6}] {'/'.join(r.get('dimension_labels', []))}{tag} {r.get('type')}")
    print(f"   {r['title']}")
    print(f"   DOI {r.get('doi') or '-'} | PMID {r.get('pmid') or '待编目'} | {r.get('venue')} | OA={r.get('oa_status')} | cited={r.get('cited_by_count')}")
