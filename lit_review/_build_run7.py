# -*- coding: utf-8 -*-
"""Run #7 corpus builder.

Merges run#6 baseline (search_results_latest.json, 170 unique / 101 in-scope /
69 excluded) with the genuinely NEW records surfaced by the run#7 pub_date recency
sweep. Writes a cumulative search_results_latest.json with corpus_delta_vs_run6.
"""
import json, datetime

BASE = "search_results_latest.json"
with open(BASE, "r", encoding="utf-8") as f:
    base = json.load(f)

base_records = base["records"]
base_pmids = { (r.get("paper_id") or r.get("pmid")) for r in base_records }
base_inscope = { (r.get("paper_id") or r.get("pmid")) for r in base_records if r.get("in_scope") }

# ---- GENUINELY NEW records surfaced by run#7 (NOT in run#6 corpus) ----
new_inscope = [
 {"paper_id":"42510113","title":"Integrated Bioinformatics and Experimental Validation Reveal the Diagnostic and Prognostic Value of SMDT1 in Thyroid Carcinoma.","authors":"Liu T; Wu H; Chen Z; Zhao W","abstract":"SMDT1 is an essential regulator of the mitochondrial calcium uniporter complex that may influence tumor progression, but its role in thyroid carcinoma is unclear. We investigated SMDT1 expression, clinical significance, and biological functions in thyroid carcinoma. Public databases analyzed SMDT1 expression, diagnostic/prognostic value, co-expression, functional enrichment, protein interactions, and immune infiltration. SMDT1 was validated in 50 paired PTC and adjacent non-tumorous tissues. In vitro SMDT1 overexpression in PTC cell lines followed by qRT-PCR, WB, CCK-8, colony formation, wound healing, and Transwell. SMDT1 was significantly downregulated in thyroid carcinoma, PTC tissues, and PTC cell lines. Low SMDT1 was associated with lymph node metastasis and shorter disease-free survival. Functional analyses linked SMDT1 with mitochondrial calcium transport, oxidative phosphorylation, apoptosis, cellular senescence, and immune infiltration, including CD8+ T cells and activated NK cells. SMDT1 overexpression suppressed PTC proliferation, colony formation, migration, invasion. SMDT1 may function as a tumor suppressor in thyroid carcinoma with diagnostic/prognostic value via mitochondrial calcium homeostasis, metabolic regulation, and immune microenvironment remodeling.","doi":"10.3390/diagnostics16142250","published_date":"2026-01-01","url":"https://pubmed.ncbi.nlm.nih.gov/42510113/","source_queries":["d"],"in_scope":True,"relevance":"High","dimensions":["molecular","metabolic","immune"]},
 {"paper_id":"39213698","title":"The U-shaped association between age at diagnosis and recurrence in patients with papillary thyroid carcinoma: A retrospective single-institution cohort study.","authors":"Huang H; Liu Y; Yan D; Liu W; Liu S","abstract":"Age is a significant predictor of papillary thyroid carcinoma (PTC). We examined the relationship between age at diagnosis and recurrence in PTC. Records of PTC patients treated 2010-2018 at a cancer referral center in China were retrospectively reviewed. HRs and 95% CIs for RFS, LRRFS and DMFS were assessed using Cox models and restricted cubic splines. 13,758 patients included; median follow-up 60 months; 687 recurrences; 90 deaths. Adjusted RCS revealed a U-shaped association between age and RFS, LRRFS, and DMFS. Both younger (<=30) and older (>=55) patients had significantly lower RFS/LRRFS than middle-aged (31-54); older patients had lower DMFS. Confirms a U-shaped association between age at diagnosis and locoregional recurrence and distant metastasis risk.","doi":"10.1016/j.ejso.2024.108626","published_date":"2024-01-01","url":"https://pubmed.ncbi.nlm.nih.gov/39213698/","source_queries":["g"],"in_scope":True,"relevance":"Low","dimensions":["prognosis"]},
]

new_offtopic = [
 {"paper_id":"42199418","title":"Cancer metabolism: from the Warburg effect to precision therapy.","authors":"Wang C; Wang J; Miao L; Wei L; Liu X; Lu Y; Xiang L; Zhang M","abstract":"Pan-cancer review of metabolic reprogramming (glucose, glutamine, fatty acids) and anti-tumor immunity; no thyroid-specific data.","doi":"10.3389/fimmu.2026.1793553","published_date":"2026-01-01","url":"https://pubmed.ncbi.nlm.nih.gov/42199418/","source_queries":["i"],"in_scope":False,"relevance":"Excluded","dimensions":[]},
 {"paper_id":"42517063","title":"miR-1911-3p Regulates Malignant Biological Behaviors and Glycolytic Activity of Triple-Negative Breast Cancer via FBLN5.","authors":"Kong L; Zhang H; Sui X; Peng X; Sun T","abstract":"Triple-negative breast cancer mechanistic/metabolic study; non-thyroid.","doi":"10.2147/BCTT.S615715","published_date":"2026-01-01","url":"https://pubmed.ncbi.nlm.nih.gov/42517063/","source_queries":["b"],"in_scope":False,"relevance":"Excluded","dimensions":[]},
]

merged = list(base_records)
added_inscope = added_off = 0
for r in new_inscope:
    if r["paper_id"] not in base_pmids:
        merged.append(r); added_inscope += 1
for r in new_offtopic:
    if r["paper_id"] not in base_pmids:
        merged.append(r); added_off += 1

# Normalize dimension labels (defensive)
DIM_MAP = {"singlecell":"single-cell"}
for r in merged:
    if "dimensions" in r and isinstance(r["dimensions"], list):
        r["dimensions"] = [DIM_MAP.get(x, x) for x in r["dimensions"]]

all_pmids = [ (r.get("paper_id") or r.get("pmid")) for r in merged ]
unique = len(set(all_pmids))
inscope = [r for r in merged if r.get("in_scope")]
excluded = [r for r in merged if not r.get("in_scope")]

dims = ["molecular","immune","single-cell","spatial","algorithm","prognosis","metabolic"]
dim_count = {d:0 for d in dims}
for r in inscope:
    for d in r.get("dimensions",[]):
        if d in dim_count: dim_count[d]+=1

new_inscope_pmids = [r["paper_id"] for r in new_inscope]

corpus_delta = {
  "new_in_scope_count": added_inscope,
  "new_in_scope_pmids": new_inscope_pmids,
  "new_excluded_offtopic_count": added_off,
  "new_excluded_offtopic_pmids": [r["paper_id"] for r in new_offtopic if r["paper_id"] not in base_pmids],
  "baseline_run6_unique": len(base_records),
  "baseline_run6_in_scope": len(base_inscope),
  "cumulative_unique": unique,
  "cumulative_in_scope": len(inscope),
  "note": "Run#6 already executed a broad sort=pub_date recency sweep (114 raw -> 170 unique / 101 in-scope). Run#7 (1 day later) re-ran the same 9 queries with sort=pub_date; only 4 PMIDs were not already in the run#6 corpus: 2 thyroid in-scope (42510113 SMDT1 tumor-suppressor/metabolic-immune; 39213698 age-recurrence U-shape) and 2 off-topic excluded (42199418 pan-cancer metabolism review; 42517063 TNBC). Corpus now at plateau with only incremental accrual."
}

out = {
  "search_date": datetime.date.today().isoformat(),
  "run": "run#7",
  "source": "mcp__paper-search-mcp__search_pubmed (DeferExecuteTool); max_results=15; sort=pub_date (recency sweep)",
  "queries": {
    "a":"thyroid cancer lymph node metastasis biomarker gene signature",
    "b":"thyroid cancer invasion metastasis molecular mechanism",
    "c":"thyroid cancer lymph node metastasis machine learning deep learning prediction model",
    "d":"thyroid cancer metastasis tumor immune microenvironment",
    "e":"thyroid cancer metastasis single cell RNA sequencing",
    "f":"thyroid cancer metastasis spatial transcriptomics spatial multi-omics",
    "g":"thyroid cancer prognosis recurrence distant metastasis risk model",
    "h":"thyroid cancer metastatic stemness subpopulation",
    "i":"thyroid cancer metabolic reprogramming metastasis"
  },
  "raw_count": 135,
  "unique_count": unique,
  "in_scope_count": len(inscope),
  "excluded_count": len(excluded),
  "dimension_distribution_in_scope": dim_count,
  "corpus_delta_vs_run6": corpus_delta,
  "records": merged
}

with open("search_results_latest.json","w",encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)

print("MERGED unique:", unique, "| in-scope:", len(inscope), "| excluded:", len(excluded))
print("Added in-scope:", added_inscope, "| Added off-topic:", added_off)
print("Dimension distribution (in-scope, multi-tag):")
for d,c in dim_count.items(): print(f"  {d}: {c}")
print("New in-scope PMIDs:", new_inscope_pmids)
