# -*- coding: utf-8 -*-
"""Build search_results_latest.json for lit-review run #5 (2026-07-27).

This run executed 9 complementary PubMed queries via the LIVE paper-search-mcp
`search_pubmed` (DeferExecuteTool), max_results=15, sort=relevance.

Key fact vs run #4 (2026-07-26): the relevance-ranked corpus is STABLE.
- All 9 queries returned the same in-scope thyroid papers as run #4.
- The ONLY delta is a relevance-tail drift in query b: `17940185`
  (BRAF V600E PTC review) dropped out of the top-15; in its place entered
  `42330341` (gastric-cancer perineural invasion, OFF-TOPIC, excluded).
- No NEW in-scope thyroid primary literature surfaced across the 7+2 queries.

JSON strategy: start from the run #4 curated corpus (70 in-scope thyroid +
35 excluded off-topic), KEEP 17940185 flagged as "relevance-tail drift /
retained for continuity", and ADD 42330341 as a new excluded record.
Result: 106 unique records, 70 in-scope, 36 excluded.
"""
import json, datetime

SRC = r"D:\paperwork\lit_review\search_results_latest.json"
OUT = r"D:\paperwork\lit_review\search_results_latest.json"

with open(SRC, encoding="utf-8") as f:
    data = json.load(f)

records = data["records"]

# Flag the BRAF review that drifted out of query b top-15 this run.
for r in records:
    if r["pmid"] == "17940185":
        r["note"] = (r.get("note", "") +
            " [run#5: not in query b top-15 this run (relevance-tail drift); "
            "retained from run#4 monitored corpus for continuity]")

# Add the new off-topic tail hit from query b this run.
new_offtopic = {
    "pmid": "42330341",
    "title": "Neuron-Derived MIF Engages VCAM1 to Fuel a Self-Amplifying CXCL8 Loop That Drives Perineural Invasion and Metastasis in Gastric Cancer.",
    "doi": "10.1002/advs.76195",
    "year": 2026,
    "disease": "gastric",
    "queries": ["b"],
    "relevance": "Low",
    "dimensions": ["offtopic"],
    "in_scope": False,
    "note": "Gastric-cancer perineural invasion (MIF-VCAM1-CXCL8), non-thyroid. Entered query b top-15 this run, displacing 17940185 (relevance drift); excluded."
}
records.append(new_offtopic)

unique = len(records)
in_scope = sum(1 for r in records if r["in_scope"])
excluded = unique - in_scope

out = {
    "search_date": "2026-07-27",
    "run": 5,
    "source": "PubMed via paper-search-mcp search_pubmed (DeferExecuteTool) — LIVE retrieval, no fabricated PMID/DOI",
    "queries": {
        "a": "thyroid cancer lymph node metastasis biomarker gene signature",
        "b": "thyroid cancer invasion metastasis molecular mechanism",
        "c": "thyroid cancer lymph node metastasis machine learning deep learning prediction model",
        "d": "thyroid cancer metastasis tumor immune microenvironment",
        "e": "thyroid cancer metastasis single cell RNA sequencing",
        "f": "thyroid cancer metastasis spatial transcriptomics spatial multi-omics",
        "g": "thyroid cancer prognosis recurrence distant metastasis risk model",
        "h": "thyroid cancer metastatic stemness subpopulation",
        "i": "thyroid cancer metabolic reprogramming metastasis",
    },
    "raw_count": unique,
    "unique_count": unique,
    "in_scope_count": in_scope,
    "excluded_count": excluded,
    "corpus_delta_vs_run4": {
        "new_in_scope": [],
        "new_excluded_offtopic": ["42330341"],
        "drifted_out_top15_but_retained": ["17940185"],
        "summary": "Stable corpus. No new in-scope thyroid literature; 1 relevance-tail swap in query b (gastric off-topic in, BRAF review to tail-limbo)."
    },
    "records": records,
}

with open(OUT, "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)

print("records:", unique, "in_scope:", in_scope, "excluded:", excluded)
