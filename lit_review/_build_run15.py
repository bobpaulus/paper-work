#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Run #15 builder: load run#14 baseline JSON, append 2 newly surfaced in-scope
thyroid papers (32421354, 36974361), write updated search_results_latest.json."""
import json, datetime

SRC = "D:/paperwork/lit_review/search_results_latest.json"
d = json.load(open(SRC, encoding="utf-8"))
recs = d["records"]
base_set = {r["pmid"] for r in recs}

new_records = [
    {
        "pmid": "32421354",
        "title": "Metastatic propagation of thyroid cancer; organ tropism and major modulators.",
        "doi": "10.2217/fon-2019-0780",
        "in_scope_thyroid": True,
        "relevance": "Medium",
        "dimensions": ["MO", "PR"],
        "dimension_labels": ["分子机制", "预后转移"],
        "queries": ["i"],
        "disease": "Thyroid cancer (PTC/FTC/MTC/ATC) - review",
        "data_source": "Literature review (no primary dataset)",
        "method": "Narrative review",
        "endpoint": "Metastatic propagation / organ tropism",
        "main_finding": "Thyroid cancer metastatic spread is governed by signaling pathways, cell-division regulators, metabolic reprogramming factors, ECM remodelers, EMT modulators, epigenetic mechanisms, hypoxia and cytokines; identifies actionable targets for therapy.",
        "validation": "None (review)",
        "limitation": "Non-primary; consolidates known mechanisms, no new wet-lab data.",
        "gap": "Organ-tropism mechanisms (bone/lung/brain) remain underexplored; metabolic-ECM-EMT coupling not yet targetable in clinic.",
        "future_direction": "Target metabolic-reprogramming + ECM-remodeling + EMT coupling to prevent metastatic seeding.",
    },
    {
        "pmid": "36974361",
        "title": "Molecular Testing Predicts Incomplete Response to Initial Therapy in Differentiated Thyroid Carcinoma Without Lateral Neck or Distant Metastasis at Presentation: Retrospective Cohort Study.",
        "doi": "10.1089/thy.2023.0060",
        "in_scope_thyroid": True,
        "relevance": "Medium",
        "dimensions": ["PR", "MO"],
        "dimension_labels": ["预后转移", "分子机制"],
        "queries": ["g"],
        "disease": "Differentiated thyroid carcinoma (papillary), no lateral neck/distant mets at presentation",
        "data_source": "945-patient retrospective single-institution cohort",
        "method": "Logistic regression; c-statistic comparison of molecular testing (MT) vs ATA RSS",
        "endpoint": "Incomplete response to initial therapy / structural-biochemical recurrence",
        "main_finding": "Among 945 pts, recurrence 2.9%/6.7%/22.8% by ATA RSS low/intermediate/high; MT improved c-statistic by 27%, comparable to ATA RSS; tumor size was the only conventional preoperative predictor.",
        "validation": "Internal; benchmarked against ATA RSS gold standard",
        "limitation": "Retrospective, single institution; short median follow-up (18 mo); MT available in only 46.6% (440/945).",
        "gap": "Preoperative risk stratification for recurrence in node-/distant-met-negative DTC lacks integration of MT + clinicopathologic factors.",
        "future_direction": "Integrate molecular testing into preoperative risk-stratification algorithms; validate in multi-center prospective cohorts.",
    },
]

added = []
for r in new_records:
    if r["pmid"] not in base_set:
        recs.append(r)
        added.append(r["pmid"])

inscope = [r for r in recs if r.get("in_scope_thyroid")]
excl = [r for r in recs if not r.get("in_scope_thyroid")]

# update top-level meta
d["run"] = 15
d["search_date"] = "2026-08-06"
d["retrieval_status"] = "all_9_queries_live_ok_after_retries (a,b,c,d,e,f,g,h,i returned; c in round2, a/b/d/e/f/g/h/i via solo retry after parallel batch transient faults)"
d["new_vs_run14"] = added
d["corpus_reset_note"] = "Run#14 was a full MCP outage (0 live records). Run#15 re-ran all 9 queries live; 2 genuinely new in-scope thyroid papers surfaced, breaking the 8-run zero-new plateau."
d["summary"] = {
    "unique_total": len(recs),
    "in_scope": len(inscope),
    "excluded": len(excl),
    "new_vs_run14": added,
    "in_scope_relevance": {
        "High": sum(1 for r in inscope if r.get("relevance") == "High"),
        "Medium": sum(1 for r in inscope if r.get("relevance") == "Medium"),
        "Low": sum(1 for r in inscope if r.get("relevance") == "Low"),
    },
    "in_scope_dimensions": None,  # filled below
}
from collections import Counter
dim = Counter()
for r in inscope:
    for x in (r.get("dimensions") or []):
        dim[x] += 1
d["summary"]["in_scope_dimensions"] = dict(dim)

d["records"] = recs
json.dump(d, open(SRC, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("WROTE", SRC)
print("unique_total:", len(recs), "in_scope:", len(inscope), "excluded:", len(excl))
print("added:", added)
print("in-scope relevance:", d["summary"]["in_scope_relevance"])
print("in-scope dimensions:", dict(dim))
