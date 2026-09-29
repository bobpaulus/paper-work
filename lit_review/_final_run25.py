# -*- coding: utf-8 -*-
"""Run #25 最终合并：OpenAlex 主检 + Europe PMC 补检 + 定向深挖 -> 累积基线"""
import json, re, unicodedata
from collections import Counter, OrderedDict
from datetime import datetime

def norm(t):
    t = re.sub(r"</?[a-zA-Z]+>", "", (t or "")).strip()
    t = unicodedata.normalize("NFKD", t).lower()
    return re.sub(r"[^a-z0-9]+", "", t)[:90]

base = json.load(open('search_results_latest.json', encoding='utf-8'))
base_recs = base.get('records', [])
base_doi = {r['doi'].lower() for r in base_recs if r.get('doi')}
base_ti = {norm(r['title']) for r in base_recs if r.get('title')}
print('基线', len(base_recs))

# ---------------- 1) OpenAlex 主检（30d+90d 合并）
oa = json.load(open('_run25_oa_new.json', encoding='utf-8'))

# ---------------- 2) Europe PMC 人工筛入
EPMC = [
 ("10.1126/sciadv.aee5417","MO/ME","High"),
 ("10.20945/2359-4292-2026-0083","MO/ME","Medium"),
 ("10.1002/smtd.71048","ME/AL","Medium"),
 ("10.1007/s00432-026-06538-1","ME/ST","Medium"),
 ("10.1186/s12957-026-04483-4","ME/PR","Medium"),
 ("10.1007/s00259-026-08100-0","PR/ME","Medium"),
 ("10.3390/ijms27146131","IM/ME","Medium"),
 ("10.1007/s12149-026-02252-7","PR/ME","Medium"),
 ("10.3390/cancers18132093","ME/IM","Low"),
 ("10.21037/gs-2026-0217","AL/PR","High"),
 ("10.1007/s10278-026-02236-z","AL","Medium"),
 ("10.1007/s10278-026-02208-3","AL","Medium"),
 ("10.21037/gs-2026-0304","AL/PR","Medium"),
 ("10.3390/metabo16080580","ME/IM","Low"),
 ("10.1007/s12149-026-02258-1","AL/PR","Medium"),
 ("10.1016/j.ctarc.2026.101434","MO/AL","Low"),
 ("10.1016/j.artmed.2026.103500","AL","Medium"),
 ("10.1097/mnm.0000000000002163","PR/AL","Medium"),
 ("10.1007/s13304-026-02781-w","AL","Low"),
 ("10.3791/72803","AL","Medium"),
 ("10.3389/fonc.2026.1858599","PR","Low"),
 ("10.1016/j.jasc.2026.07.001","PR/AL","Low"),
]
# ---------------- 3) 定向深挖筛入
DEEP = [
 ("10.3389/fimmu.2026.1848083","ME/IM/PR","High"),
 ("10.21037/tcr-2026-0796","MO/ME","High"),
 ("10.1016/j.canlet.2026.218650","ME/IM","High"),
 ("10.1186/s12885-026-16648-1","SC/IM","High"),
 ("10.1177/10507256261481666","IM/SC","High"),
 ("10.1186/s11658-026-00973-1","ME/ST","Medium"),
 ("10.3389/fmolb.2026.1875059","ME","Medium"),
 ("10.3389/fneur.2026.1921351","PR/ST","Low"),
 ("10.1097/md.0000000000050562","MO/PR","Low"),
 ("10.1038/s41420-026-03293-7","ME/ST","High"),
 ("10.3390/ijms27167305","IM/ST","Medium"),
 ("10.1007/s11010-026-05604-z","ME","Medium"),
 ("10.20944/preprints202608.0708.v1","ME/IM","Medium"),
 ("10.20944/preprints202608.0302.v1","SP","Medium"),
 ("10.36922/cp025320050","MO/PR","Low"),
 ("10.3390/ijms27136018","MO","Low"),
 ("10.1158/1078-0432.ccr-25-4488","SC/PR","High"),
]

DIM_LABEL = {"MO":"分子机制","IM":"免疫微环境","SC":"单细胞","SP":"空间组学",
             "AL":"算法方法","PR":"预后转移","ST":"转移干性","ME":"代谢重编程"}

# 元数据池：从各路 JSON 里取
pool = {}
def add(r):
    d = (r.get('doi') or '').lower()
    t = norm(r.get('title'))
    if d: pool[d] = r
    if t: pool[t] = r
for r in oa: add(r)
for f in ('search_results_20260925_epmc_detail.json','search_results_20260925_keyabs.json'):
    try:
        for k, v in json.load(open(f, encoding='utf-8')).items():
            v = dict(v); v.setdefault('doi', k); add(v)
    except Exception as e:
        print('pool load warn', f, e)
for f in ('search_results_20260925_d3deep.json',):
    d3 = json.load(open(f, encoding='utf-8'))
    for k, v in d3.items():
        for it in v.get('items', []): add(it)

final = OrderedDict()
def put(doi, dims, rel, src):
    if not doi: return
    dl = doi.lower()
    if dl in base_doi: return
    rec = pool.get(dl) or pool.get(norm(pool.get(dl, {}).get('title', '')))
    if rec is None:
        # 尝试按 doi 从 pool 匹配到 title 再取
        rec = {'doi': doi, 'title': None}
    tk = norm(rec.get('title') or doi)
    if tk in base_ti: return
    r = dict(rec)
    r['doi'] = doi
    r['dimensions'] = dims.split('/')
    r['dimension_labels'] = [DIM_LABEL[d] for d in dims.split('/')]
    r['relevance'] = rel
    r['run25_source'] = src
    r['in_scope_thyroid'] = True
    r['is_preprint'] = (r.get('type') == 'preprint') or ('preprints' in (r.get('doi') or ''))
    final[tk] = r

for r in oa:
    put(r.get('doi'), '/'.join(r.get('dimensions', [])), r.get('relevance'), 'OpenAlex')
for doi, dims, rel in EPMC: put(doi, dims, rel, 'EuropePMC')
for doi, dims, rel in DEEP: put(doi, dims, rel, 'OpenAlex-deep')

newlist = list(final.values())
print('本轮去重后唯一新增:', len(newlist))
print('来源分布:', dict(Counter(r['run25_source'] for r in newlist)))
print('相关性:', dict(Counter(r['relevance'] for r in newlist)))
print('预印本:', sum(1 for r in newlist if r.get('is_preprint')))
dc = Counter()
for r in newlist:
    for l in r['dimension_labels']: dc[l] += 1
print('维度分布:', dict(dc))
print('OA 状态:', dict(Counter(r.get('oa_status') for r in newlist)))

merged = base_recs + newlist
payload = dict(base)
payload['search_date'] = datetime.now().astimezone().isoformat(timespec='seconds')
payload['window_from'] = '2026-08-26 (主 30d) / 2026-06-27 (90d 补检) / EuropePMC PUB_YEAR:2026 / 定向深挖 2026-01-01 起'
payload['records'] = merged
payload['summary'] = dict(base.get('summary', {}),
    total_records=len(merged), run25_new=len(newlist),
    run25_source=dict(Counter(r['run25_source'] for r in newlist)),
    run25_relevance=dict(Counter(r['relevance'] for r in newlist)),
    run25_preprints=sum(1 for r in newlist if r.get('is_preprint')),
    run25_dimensions=dict(dc))
json.dump(payload, open('search_results_20260925_033000.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump(payload, open('search_results_latest.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump(newlist, open('search_results_20260925_new.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('累积基线:', len(merged))
print('\n--- 新增清单 ---')
for r in sorted(newlist, key=lambda x: x.get('publication_date') or '', reverse=True):
    print(f"{r.get('publication_date')} [{r['relevance']:<6}] {'/'.join(r['dimension_labels'])} {r['run25_source']} {'[PREPRINT]' if r.get('is_preprint') else ''}")
    print(f"   {(r.get('title') or '(no title)')[:120]}")
    print(f"   DOI {r.get('doi')} | PMID {r.get('pmid') or '待编目'} | {r.get('venue')}")
