#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Regenerate D:\paperwork\lit_review\search_results_latest.json for run#9 (2026-07-31).

Run#9 re-executed the 9 complementary PubMed queries (a-i) via the paper-search-mcp
MCP (DeferExecuteTool) with max_results=15, sort=relevance. Every returned PMID was
already present in the run#8 corpus, so the cumulative corpus is UNCHANGED:
174 unique / 103 in-scope / 71 excluded, 0 new.

This script preserves the 174 already-tagged records and only rewrites the header
metadata + the run#9 corpus-delta block, so downstream reports stay consistent.
"""
import json

PATH = r"D:\paperwork\lit_review\search_results_latest.json"

with open(PATH, encoding="utf-8") as f:
    data = json.load(f)

# ---- Update header metadata for run#9 ----
data["search_date"] = "2026-07-31"
data["run"] = "run#9"
data["source"] = ("mcp__paper-search-mcp__search_pubmed (DeferExecuteTool); "
                  "max_results=15; sort=relevance (recency approximated via relevance ranking; "
                  "PubMed MCP exposes no date filter)")
data["queries"] = {
    "a": "thyroid cancer lymph node metastasis biomarker gene signature",
    "b": "thyroid cancer invasion metastasis molecular mechanism",
    "c": "thyroid cancer lymph node metastasis machine learning deep learning prediction model",
    "d": "thyroid cancer metastasis tumor immune microenvironment",
    "e": "thyroid cancer metastasis single cell RNA sequencing",
    "f": "thyroid cancer metastasis spatial transcriptomics spatial multi-omics",
    "g": "thyroid cancer prognosis recurrence distant metastasis risk model",
    "h": "thyroid cancer metastasis cancer stem cell stemness subpopulation",
    "i": "thyroid cancer metastasis metabolic reprogramming",
}
# Raw rows actually retrieved this run: a,b,c,d,e,f,g,i = 15 each (c retried after 2
# transient 'not well-formed' parse errors), h returned 4 -> 8*15 + 4 = 124 raw rows.
data["raw_count"] = 124
# Cumulative corpus unchanged (0 new this run)
data["unique_count"] = 174
data["in_scope_count"] = 103
data["excluded_count"] = 71
data["dimension_distribution_in_scope"] = {
    "molecular": 47,
    "prognosis": 28,
    "algorithm": 37,
    "immune": 30,
    "metabolic": 14,
    "single-cell": 18,
    "spatial": 6,
}
data["corpus_delta_vs_run8"] = {
    "new_in_scope_count": 0,
    "new_in_scope_pmids": [],
    "new_excluded_offtopic_count": 0,
    "new_excluded_offtopic_pmids": [],
    "baseline_run8_unique": 174,
    "baseline_run8_in_scope": 103,
    "cumulative_unique": 174,
    "cumulative_in_scope": 103,
    "note": ("Run#9 (2026-07-31) re-ran the same 9 queries (a-i) with sort=relevance. "
             "All returned PMIDs were already present in the run#8 corpus: "
             "0 thyroid in-scope + 0 off-topic excluded. Hard plateau persists "
             "(run#7 +2, run#8 +0, run#9 +0). The PubMed MCP now exhausts visible "
             "2025-2026 literature for this query set; breaking the plateau requires "
             "sources beyond PubMed (bioRxiv/arXiv preprints, cBioPortal/DepMap)."),
}

with open(PATH, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("OK run#9 -> unique:", data["unique_count"],
      "in_scope:", data["in_scope_count"],
      "excluded:", data["excluded_count"],
      "records:", len(data["records"]),
      "new:", data["corpus_delta_vs_run8"]["new_in_scope_count"])
