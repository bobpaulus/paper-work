# -*- coding: utf-8 -*-
"""Generate run#14 literature-review report + update JSON.

Run#14: paper-search-mcp `search_pubmed` fully degraded this run -- all 9
queries (a-i) failed across 3 retry rounds (27 DeferExecuteTool calls) with the
persistent `not well-formed (invalid token)` transient parse error. Per the
lit-review skill degradation clause, the entire corpus is inherited from the
run#13 authoritative baseline (104 unique / 76 in-scope / 28 excluded). 0 new
PMIDs detectable. This script (1) rewrites the run#13 report with the run#14
retrieval note + run-number updates, and (2) rewrites search_results_latest.json
metadata (preserving all 104 records) to mark all 9 queries failed and new_vs_run13=0.
"""
import json
import os
import io

BASE = r"D:\paperwork\lit_review"
SRC_REPORT = os.path.join(BASE, "literature_review_20260804_030119.md")
DST_REPORT = os.path.join(BASE, "literature_review_20260805_030159.md")
JSON_PATH = os.path.join(BASE, "search_results_latest.json")

# ----------------------------------------------------------------------------
# 1) Report text replacements (run#13 -> run#14)
# ----------------------------------------------------------------------------
with io.open(SRC_REPORT, "r", encoding="utf-8") as fh:
    text = fh.read()

REPL = [
    # Header
    ("Automation run: #13 (cumulative; compares against run#12 baseline JSON)",
     "Automation run: #14 (cumulative; compares against run#13 baseline JSON)"),

    # Chinese abstract paragraph (full rewrite of run#13 sentence)
    ("本自动化监测第 13 次运行，使用 `lit-review` 技能，通过已连接的 paper-search-mcp（`search_pubmed`，DeferExecuteTool）对甲状腺癌（PTC/PTMC/FTC/MTC/ATC）侵袭、淋巴结与远处转移、复发、预后及其分子机制、肿瘤免疫微环境（TIME）、单细胞（scRNA-seq）、空间组学（spatial multi-omics）、机器学习/深度学习（ML/DL）方法共 9 路互补检索（max_results=15, sort=relevance）。共返回 **130 条原始记录**，去重后 **104 个唯一 PMID**，其中 **76 篇甲状腺相关纳入**，**28 篇非甲状腺/重复排除**。9 路检索中 a/b/c 三路本次成功实时返回，其 PMID 集合与 run#12 基线**完全一致**；d/e/f/g/h/i 六路在 6 轮重试中持续返回 `not well-formed (invalid token)` 瞬时解析错误（MCP 服务器端降级），按 `lit-review` 技能降级规则，该六路语料继承 run#12 权威基线。去重后仍为 **104 个唯一 PMID**，**76 篇甲状腺相关纳入**，**28 篇非甲状腺/重复排除**。与 run#12 基线（104 个唯一 PMID / 76 篇在域）对比，本次 **新增 0 篇**（0 甲状腺在域 + 0 非甲状腺排除）；这延续了自 run#7 以来的平台期（PubMed MCP 对该查询集可见的 2025–2026 文献已基本穷尽）。",
     "本自动化监测第 14 次运行，使用 `lit-review` 技能，通过已连接的 paper-search-mcp（`search_pubmed`，DeferExecuteTool）对甲状腺癌（PTC/PTMC/FTC/MTC/ATC）侵袭、淋巴结与远处转移、复发、预后及其分子机制、肿瘤免疫微环境（TIME）、单细胞（scRNA-seq）、空间组学（spatial multi-omics）、机器学习/深度学习（ML/DL）方法共 9 路互补检索（max_results=15, sort=relevance）。**本轮 9 路检索（a–i）在 3 轮重试（共 27 次调用）中全部持续返回 `not well-formed (invalid token)` 瞬时解析错误（MCP 服务器端完全降级），无可实时返回的原始记录**；按 `lit-review` 技能降级规则，全部语料继承 run#13 权威基线，即 **104 个唯一 PMID** / **76 篇甲状腺相关纳入** / **28 篇非甲状腺/重复排除**。与 run#13 基线（104 个唯一 PMID / 76 篇在域）对比，本次 **新增 0 篇**（0 甲状腺在域 + 0 非甲状腺排除）；这延续了自 run#7 以来的平台期（PubMed MCP 对该查询集可见的 2025–2026 文献已基本穷尽，且本轮工具完全不可用）。"),

    # Chinese abstract D3 consecutive count
    ("连续第 13 次被确认为最优下一步",
     "连续第 14 次被确认为最优下一步"),

    # English abstract paragraph (full rewrite)
    ("Run #13 of the scheduled thyroid-cancer literature monitor used the `lit-review` skill and the connected paper-search-mcp (`search_pubmed` via DeferExecuteTool) to run 9 complementary PubMed queries (max_results=15, sort=relevance) spanning invasion/metastasis mechanisms, LNM biomarkers, ML/DL prediction, tumor immune microenvironment, single-cell RNA-seq, spatial multi-omics, prognosis/recurrence/distant-metastasis risk, metastatic stemness, and metabolic reprogramming. **130 raw records → 104 unique PMIDs → 76 thyroid in-scope (28 non-thyroid/duplicate excluded).** Versus the run#12 baseline (104 unique / 76 in-scope), **0 genuinely new PMIDs** were detected — every PMID retrieved this run was already in the run#12 corpus (queries a/b/c live, identical; d/e/f/g/h/i inherited from run#12 baseline due to MCP degradation). This confirms the plateau observed since run#7 — the PubMed MCP has exhausted visible 2025–2026 literature for this query set.",
     "Run #14 of the scheduled thyroid-cancer literature monitor used the `lit-review` skill and the connected paper-search-mcp (`search_pubmed` via DeferExecuteTool) to run 9 complementary PubMed queries (max_results=15, sort=relevance) spanning invasion/metastasis mechanisms, LNM biomarkers, ML/DL prediction, tumor immune microenvironment, single-cell RNA-seq, spatial multi-omics, prognosis/recurrence/distant-metastasis risk, metastatic stemness, and metabolic reprogramming. **All 9 queries failed across 3 retry rounds (27 calls) with the persistent `not well-formed (invalid token)` transient parse error — the search_pubmed MCP was fully degraded this run**, so no live records were retrieved. Per the `lit-review` skill degradation clause, the entire corpus is inherited from the run#13 authoritative baseline: **104 unique PMIDs → 76 thyroid in-scope (28 non-thyroid/duplicate excluded).** Versus the run#13 baseline (104 unique / 76 in-scope), **0 genuinely new PMIDs** were detected — no retrieval was possible this run. This both confirms and extends the plateau observed since run#7 (now 8 consecutive zero-new runs, #7+2 → #8–#14), and shows the PubMed MCP is currently unusable for this query set."),

    # English abstract 13th -> 14th
    ("reaffirmed as the best next step for the 13th consecutive run.",
     "reaffirmed as the best next step for the 14th consecutive run."),

    # Search Strategy table + note block (full rewrite)
    ("| Source | Query | Filters | Results | Notes |\n|---|---|---|---:|---|\n| PubMed | `thyroid cancer lymph node metastasis biomarker gene signature` | max_results=15, sort=relevance | 15 | 甲状腺相关全纳入；非甲状腺/泛癌综述剔除 |\n| PubMed | `thyroid cancer invasion metastasis molecular mechanism` | max_results=15, sort=relevance | 15 | 甲状腺相关全纳入；非甲状腺/泛癌综述剔除 |\n| PubMed | `thyroid cancer lymph node metastasis machine learning deep learning prediction model` | max_results=15, sort=relevance | 15 | 甲状腺相关全纳入；非甲状腺/泛癌综述剔除 |\n| PubMed | `thyroid cancer metastasis tumor immune microenvironment` | max_results=15, sort=relevance | 13 | 甲状腺相关全纳入；非甲状腺/泛癌综述剔除 |\n| PubMed | `thyroid cancer metastasis single cell RNA sequencing` | max_results=15, sort=relevance | 15 | 甲状腺相关全纳入；非甲状腺/泛癌综述剔除 |\n| PubMed | `thyroid cancer metastasis spatial transcriptomics spatial multi-omics` | max_results=15, sort=relevance | 11 | 甲状腺相关全纳入；非甲状腺/泛癌综述剔除 |\n| PubMed | `thyroid cancer prognosis recurrence distant metastasis risk model` | max_results=15, sort=relevance | 15 | 甲状腺相关全纳入；非甲状腺/泛癌综述剔除 |\n| PubMed | `thyroid cancer metastatic stemness subpopulation` | max_results=15, sort=relevance | 16 | 甲状腺相关全纳入；非甲状腺/泛癌综述剔除 |\n| PubMed | `thyroid cancer metabolic reprogramming metastasis` | max_results=15, sort=relevance | 15 | 甲状腺相关全纳入；非甲状腺/泛癌综述剔除 |\n\n> 注：paper-search-mcp `search_pubmed` 无日期过滤参数，时间窗以相关性排序近似；每路首次放宽至全部时间。本轮（run#13）MCP 出现与历史一致的瞬时解析错误（`not well-formed (invalid token)`），但呈**查询特异性持久降级**：9 路中 a/b/c 三路成功实时返回（其 PMID 集合与 run#12 完全一致），而 d/e/f/g/h/i 六路在 6 轮重试中持续失败。按 `lit-review` 技能降级规则（工具不可用时，沿用既有证据矩阵与缺口分析），六路语料继承 run#12 权威基线；因平台期，语料规模与 run#12 一致。",
     "| Source | Query | Filters | Results | Notes |\n|---|---|---|---:|---|\n| PubMed | `thyroid cancer lymph node metastasis biomarker gene signature` | max_results=15, sort=relevance | inherited | MCP 完全降级，继承 run#13 基线 |\n| PubMed | `thyroid cancer invasion metastasis molecular mechanism` | max_results=15, sort=relevance | inherited | MCP 完全降级，继承 run#13 基线 |\n| PubMed | `thyroid cancer lymph node metastasis machine learning deep learning prediction model` | max_results=15, sort=relevance | inherited | MCP 完全降级，继承 run#13 基线 |\n| PubMed | `thyroid cancer metastasis tumor immune microenvironment` | max_results=15, sort=relevance | inherited | MCP 完全降级，继承 run#13 基线 |\n| PubMed | `thyroid cancer metastasis single cell RNA sequencing` | max_results=15, sort=relevance | inherited | MCP 完全降级，继承 run#13 基线 |\n| PubMed | `thyroid cancer metastasis spatial transcriptomics spatial multi-omics` | max_results=15, sort=relevance | inherited | MCP 完全降级，继承 run#13 基线 |\n| PubMed | `thyroid cancer prognosis recurrence distant metastasis risk model` | max_results=15, sort=relevance | inherited | MCP 完全降级，继承 run#13 基线 |\n| PubMed | `thyroid cancer metastatic stemness subpopulation` | max_results=15, sort=relevance | inherited | MCP 完全降级，继承 run#13 基线 |\n| PubMed | `thyroid cancer metabolic reprogramming metastasis` | max_results=15, sort=relevance | inherited | MCP 完全降级，继承 run#13 基线 |\n\n> 注：paper-search-mcp `search_pubmed` 无日期过滤参数，时间窗以相关性排序近似；每路首次放宽至全部时间。**本轮（run#14）MCP 出现完全降级**：9 路检索（a–i）在 3 轮重试（共 27 次 DeferExecuteTool 调用）中**全部**持续返回 `not well-formed (invalid token)` 瞬时解析错误，无一成功返回。按 `lit-review` 技能降级规则（工具不可用时，沿用既有证据矩阵与缺口分析），全部 9 路语料继承 run#13 权威基线；因长期平台期，语料规模与 run#13 完全一致（104/76/28）。**新增文献检测因工具不可用而无法进行。**"),

    # Recommended Next Direction consecutive count
    ("**D3 — 定义并靶向 APOE−/MGST1+ 代谢–免疫干性转移亚群（rubric 总分 32，强候选，连续第 13 次确认）。**",
     "**D3 — 定义并靶向 APOE−/MGST1+ 代谢–免疫干性转移亚群（rubric 总分 32，强候选，连续第 14 次确认）。**"),

    # Reproducibility note: Search date
    ("- Search date: 2026-08-04",
     "- Search date: 2026-08-05"),

    # Reproducibility note: New-vs-prior
    ("- New-vs-prior: 与 run#12 基线（104 唯一 PMID）机械比对——**新增 0**；a/b/c 三路实时返回集合与 run#12 完全一致，d/e/f/g/h/i 六路因 MCP 持久降级继承 run#12 基线（非新文献）。",
     "- New-vs-prior: 与 run#13 基线（104 唯一 PMID）机械比对——**新增 0**；本轮 9 路检索（a–i）全部因 MCP 完全降级（3 轮重试共 27 次调用均失败）继承 run#13 基线（非新文献），新增检测因工具不可用无法进行。"),

    # Reproducibility note: report file name
    ("  - 报告：`lit_review/literature_review_20260804_030119.md`",
     "  - 报告：`lit_review/literature_review_20260805_030159.md`"),

    # Reproducibility note: JSON note
    ("  - 原始+去重语料：`lit_review/search_results_latest.json`（130 raw / 104 unique / 76 in-scope / 28 excluded，含每篇 relevance+dimension+query 标签；run#13 新增 retrieval_status 字段标注 a/b/c 实时检索一致、d/e/f/g/h/i MCP 持久降级继承基线；new_vs_run12=0）",
     "  - 原始+去重语料：`lit_review/search_results_latest.json`（104 unique / 76 in-scope / 28 excluded，继承 run#13 权威基线；含每篇 relevance+dimension+query 标签；run#14 全 9 路 retrieval_status=failed_transient_not_well_formed，new_vs_run13=0，新增检测因 MCP 完全降级无法进行）"),

    # Reproducibility note: generator script
    ("  - 生成脚本：`lit_review/_build_run13.py`",
     "  - 生成脚本：`lit_review/_gen_run14.py`"),

    # Comparison section header
    ("## Comparison With Prior Report / 与历史报告差异（vs run#12）",
     "## Comparison With Prior Report / 与历史报告差异（vs run#13）"),

    # Comparison block body
    ("- **检索条数**：run#13 与 run#12 检索规模**完全一致**：130 条原始 → 去重 104 唯一 → 在域 76 → 排除 28；其中 a/b/c 三路为本次实时检索（与 run#12 基线 PMID 集合一致），d/e/f/g/h/i 六路因 MCP 持久降级继承 run#12 基线。\n- **新增文献**：**0 篇**（连续第 7 个平台期 run#7→#13；其中 #8–#13 均为 0 新增）。本轮 a/b/c 实时返回集合与 run#12 完全一致，d/e/f/g/h/i 六路继承 run#12 基线，**无新信号**。\n- **各维度分布（在域，多标签）**：分子机制 38 / 预后转移 31 / 代谢重编程 11 / 算法方法 18 / 免疫微环境 14 / 单细胞 12 / 空间组学 7 / 转移干性 5（run#12：38/31/11/18/14/12/7/5，本次与 run#12 完全一致，无维度漂移）。\n- **关键收敛发现**：5 个主轴**完全不变**；DTC 远处 vs LNM 解耦（BRAF V600E 荟萃 41419184 与 PD-L1 荟萃）再次确认。\n- **推荐方向**：**D3 — 定义并靶向 APOE−/MGST1+ 代谢–免疫干性转移亚群**（rubric 总分 **32**，强候选）——连续第 13 次确认，无反证。\n- **新信号/方向变化**：与 run#12 **相比无实质方向变化**；平台期建议（自 run#7 起反复提出）仍需落实——必须跳出 PubMed MCP：加入 bioRxiv/arXiv 预印本 + cBioPortal/DepMap + 收窄 ATC/MTC 与空间组学时间窗，并考虑将自动化频次由每日降为每周以节约配额。",
     "- **检索条数**：run#14 与 run#13 检索规模**完全一致**（继承）：104 唯一 PMID → 在域 76 → 排除 28。本轮 9 路检索（a–i）因 MCP 完全降级（3 轮重试共 27 次调用全部失败）**无任何实时返回**，全部语料继承 run#13 基线。\n- **新增文献**：**0 篇**（连续第 8 个平台期 run#7→#14；其中 #8–#14 均为 0 新增）。本轮 9 路检索全部继承 run#13 基线，**无新信号**，且因工具完全不可用，新增文献检测本身无法进行。\n- **各维度分布（在域，多标签）**：分子机制 38 / 预后转移 31 / 代谢重编程 11 / 算法方法 18 / 免疫微环境 14 / 单细胞 12 / 空间组学 7 / 转移干性 5（run#13：38/31/11/18/14/12/7/5，本次与 run#13 完全一致，无维度漂移）。\n- **关键收敛发现**：5 个主轴**完全不变**；DTC 远处 vs LNM 解耦（BRAF V600E 荟萃 41419184 与 PD-L1 荟萃）再次确认。\n- **推荐方向**：**D3 — 定义并靶向 APOE−/MGST1+ 代谢–免疫干性转移亚群**（rubric 总分 **32**，强候选）——连续第 14 次确认，无反证。\n- **新信号/方向变化**：与 run#13 **相比无实质方向变化**；平台期建议（自 run#7 起反复提出）仍需落实——必须跳出 PubMed MCP：加入 bioRxiv/arXiv 预印本 + cBioPortal/DepMap + 收窄 ATC/MTC 与空间组学时间窗，并考虑将自动化频次由每日降为每周以节约配额。本轮 MCP 完全降级进一步印证该工具已不可依赖。"),
]

missing = []
for old, new in REPL:
    if old not in text:
        missing.append(old[:60])
if missing:
    raise SystemExit("FAILED to find old strings:\n" + "\n".join(missing))

for old, new in REPL:
    text = text.replace(old, new, 1)

with io.open(DST_REPORT, "w", encoding="utf-8") as fh:
    fh.write(text)
print("REPORT written:", DST_REPORT, "chars:", len(text))

# ----------------------------------------------------------------------------
# 2) JSON metadata update (preserve all 104 records)
# ----------------------------------------------------------------------------
with io.open(JSON_PATH, "r", encoding="utf-8") as fh:
    data = json.load(fh)

n_records = len(data.get("records", []))
assert n_records == 104, "expected 104 records, got %d" % n_records

data["search_date"] = "2026-08-05"
data["run"] = "run#14"
data["source"] = ("mcp__paper-search-mcp__search_pubmed (DeferExecuteTool); max_results=15; "
                  "sort=relevance; run#14: ALL 9 queries (a-i) failed across 3 retry rounds "
                  "(27 calls) with persistent `not well-formed (invalid token)` transient parse "
                  "error (server-side MCP fully degraded) -> entire corpus inherited from run#13 "
                  "authoritative baseline per lit-review skill degradation clause")

queries = data.get("queries", {})
data["queries"] = queries  # unchanged

data["corpus_note"] = ("Run#14: paper-search-mcp `search_pubmed` was fully degraded -- all 9 queries "
                       "(a-i) failed across 3 retry rounds (27 DeferExecuteTool calls) with the persistent "
                       "`not well-formed (invalid token)` transient parse error. Per the lit-review skill "
                       "degradation clause, the entire corpus is inherited from the run#13 authoritative "
                       "baseline (104 unique / 76 in-scope / 28 excluded). Dedup by PMID; in-scope thyroid "
                       "papers retained; off-topic excluded. Multi-tag dimensions per record. 0 new PMIDs "
                       "detectable (retrieval impossible this run).")

s = data["summary"]
s["raw_rows"] = 0  # no live retrieval this run
s["unique_pmids"] = 104
s["in_scope_thyroid"] = 76
s["excluded_nonthyroid_or_duplicate"] = 28
s["new_vs_run12_baseline"] = []
s["new_vs_run13_baseline"] = []
s["new_vs_run13"] = []
s["new_publications_reliable"] = 0
s["plateau_note"] = ("Hard plateau persists and extends (run#7+2 -> #8-#14 all 0 new). Run#14: ALL 9 queries "
                      "(a-i) failed across 3 retry rounds with persistent `not well-formed (invalid token)` "
                      "transient parse error (full MCP degradation) -> corpus fully inherited from run#13. "
                      "0 genuinely new thyroid papers vs run#13 104-corpus; new-detection impossible this run.")
s["retrieval_status"] = {q: "failed_transient_not_well_formed" for q in queries}

data["summary"] = s

with io.open(JSON_PATH, "w", encoding="utf-8") as fh:
    json.dump(data, fh, ensure_ascii=False, indent=2)
print("JSON updated:", JSON_PATH, "records:", n_records)
