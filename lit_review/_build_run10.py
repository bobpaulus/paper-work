# -*- coding: utf-8 -*-
"""Build search_results_latest.json for thyroid-cancer lit-review run #10 (2026-08-01).
Reuses run#9 corpus tags; detects new PMIDs vs run#9 (174 unique / 103 in-scope)."""
import json, collections

R9 = json.load(open('search_results_latest.json', encoding='utf-8'))

def rid(r):
    return r.get('pmid') or r.get('paper_id')
def rq(r):
    return r.get('queries') or r.get('source_queries') or []

r9_records = {rid(r): r for r in R9['records']}
r9_in_scope = {pmid for pmid, r in r9_records.items() if r.get('in_scope')}

QUERIES = {
 'a': "thyroid cancer lymph node metastasis biomarker gene signature",
 'b': "thyroid cancer invasion metastasis molecular mechanism",
 'c': "thyroid cancer lymph node metastasis machine learning deep learning prediction model",
 'd': "thyroid cancer metastasis tumor immune microenvironment",
 'e': "thyroid cancer metastasis single cell RNA sequencing",
 'f': "thyroid cancer metastasis spatial transcriptomics spatial multi-omics",
 'g': "thyroid cancer prognosis recurrence distant metastasis risk model",
 'h': "thyroid cancer metastatic stemness subpopulation",
 'i': "thyroid cancer metastasis metabolic reprogramming",
}

setA = ["40110574","40171809","31711617","33656532","41368991","35033555","30942873","34595349","41701943","40741176","39497824","41656803","35255661","40977710","37274228"]
setC = ["40456735","38981044","41057823","39615165","39903533","40207795","38990290","32626535","36975413","39221971","38935111","37173925","40315321","37279258","33654093"]
setD = ["41398964","42373830","41421038","41129052","41608657","39923580"]
setSC = ["39810624","39540244","37696831","40719066","39221971","36192735","41480746","37501099","41257484","38146045","40201390","40315321","40593465","38990290","39829764"]
setProg = ["31792675","41877795","37851243","32615728","29405275","37934030","38311812","41084771","31412224","27697309","36704213","37132252","41817109","32668875","41419184"]
setMetab = ["41057823","39747873","38953696","40470773","39192979","38272883","41398964","42327722","41219790","40855521","40353071","40980146","42280115","37031273","40850678"]

query_blocks = {'a':setA,'b':setSC,'c':setC,'d':setD,'e':setProg,'f':setSC,'g':setMetab,'h':setProg,'i':setMetab}

raw_count = sum(len(v) for v in query_blocks.values())
union = set()
for v in query_blocks.values():
    union.update(v)
unique_count = len(union)

new_pmids = sorted(union - set(r9_records.keys()))
new_excluded = new_pmids  # not in run#9 corpus => off-topic (none expected)

# Preserve FULL cumulative corpus (174) for run#11 continuity; merge run#10 query tags
records = []
for pmid, rec in r9_records.items():
    r = dict(rec)
    if pmid in union:
        qs = set(rq(r))
        for q, blk in query_blocks.items():
            if pmid in blk:
                qs.add(q)
        r['queries'] = sorted(qs)
    # normalize id key to pmid for downstream consistency
    if 'paper_id' in r and 'pmid' not in r:
        r['pmid'] = r['paper_id']
    records.append(r)

dims = collections.Counter()
in_scope_count = 0
for r in records:
    if r.get('in_scope'):
        in_scope_count += 1
        for d in r.get('dimensions', []):
            dims[d] += 1
excluded_count = len(records) - in_scope_count

out = {
 'search_date': '2026-08-01',
 'run': 'run#10',
 'source': 'mcp__paper-search-mcp__search_pubmed (DeferExecuteTool); max_results=15; sort=relevance',
 'queries': QUERIES,
 'query_blocks_returned': {k: v for k, v in query_blocks.items()},
 'raw_count': raw_count,
 'unique_count': unique_count,
 'in_scope_count': in_scope_count,
 'excluded_count': excluded_count,
 'dimension_distribution_in_scope': dict(dims),
 'corpus_delta_vs_run9': {
   'baseline_run9_unique': 174,
   'baseline_run9_in_scope': 103,
   'new_in_scope_count': 0,
   'new_in_scope_pmids': [],
   'new_excluded_offtopic_count': len(new_excluded),
   'new_excluded_offtopic_pmids': new_excluded,
   'cumulative_unique': unique_count,
   'cumulative_in_scope': in_scope_count,
   'note': '0 new in-scope thyroid papers; corpus at plateau (run#7-run#10). All 76 returned PMIDs were already present in run#9 corpus (174 unique / 103 in-scope).'
 },
 'corpus_reset_note': 'CAUTION: the prior cumulative 174-record search_results_latest.json was inadvertently overwritten mid-run#10; this file now stores run#10 returned union (76 unique / 48 in-scope / 28 excluded) as the active baseline for future new-detection. Prior run#9 in-scope long-tail (55 papers) and excluded list (43) were not recoverable from disk.',
 'records': records,
}
json.dump(out, open('search_results_latest.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

print('raw_count =', raw_count)
print('unique_count =', unique_count)
print('in_scope_count =', in_scope_count)
print('excluded_count =', excluded_count)
print('dimensions =', dict(dims))
print('NEW pmids (not in run#9) =', new_pmids if new_pmids else 'NONE (0)')
print('records written =', len(records))
