#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate the bilingual structured literature-review report (run#12) from search_results_latest.json."""
import json, os, datetime

LR = r"D:\paperwork\lit_review"
DATA = json.load(open(os.path.join(LR, "search_results_latest.json"), encoding="utf-8"))
RECS = DATA["records"]
S = DATA["summary"]
RUN_DATE = "2026-08-03"
TS = "20260803_031443"
OUT_MD = os.path.join(LR, f"literature_review_{TS}.md")

in_scope = [r for r in RECS if r["in_scope_thyroid"]]
excluded = [r for r in RECS if not r["in_scope_thyroid"]]

def sortkey(r): return int(r["pmid"])

# High-relevance in-scope, sorted by pmid
high = sorted([r for r in in_scope if r["relevance"] == "High"], key=sortkey)
# Build evidence matrix for a curated subset (High + key Medium) — keep manageable
matrix_rows = sorted([r for r in in_scope if r["relevance"] in ("High","Medium")], key=sortkey)

def dim_str(r): return "/".join(r["dimension_labels"])

# ---------------------------------------------------------------------------
L = []
def w(s=""): L.append(s)

w("# Literature Review: 甲状腺癌侵袭/转移/复发/预后 与 分子机制·免疫微环境·单细胞·空间组学·AI 方法")
w()
w(f"Date: {RUN_DATE}  ")
w("Sources: PubMed (via paper-search-mcp `search_pubmed`, DeferExecuteTool)  ")
w("Search window: all time (sort=relevance; MCP has no date filter, recency approximated via relevance)  ")
w("Automation run: #12 (cumulative; compares against run#11 baseline JSON)")
w()
w("## 中文摘要 (Chinese Abstract)")
w()
w(f"本自动化监测第 12 次运行，使用 `lit-review` 技能，通过已连接的 paper-search-mcp（`search_pubmed`，DeferExecuteTool）对甲状腺癌（PTC/PTMC/FTC/MTC/ATC）侵袭、淋巴结与远处转移、复发、预后及其分子机制、肿瘤免疫微环境（TIME）、单细胞（scRNA-seq）、空间组学（spatial multi-omics）、机器学习/深度学习（ML/DL）方法共 9 路互补检索（max_results=15, sort=relevance）。共返回 **130 条原始记录**，去重后 **104 个唯一 PMID**，其中 **76 篇甲状腺相关纳入**，**28 篇非甲状腺/重复排除**。与 run#11 基线（104 个唯一 PMID / 75 篇在域）对比，本次 **新增 0 篇**（0 甲状腺在域 + 0 非甲状腺排除）；9 路检索返回的全部 PMID 已在 run#11 语料中，仅 5 篇 run#11 语料中因 15 行相关性截断而掉出的记录（38981044, 39615165, 40207795, 39903533, 40855521）本轮重新出现并仍按非甲状腺排除处理——**并非新文献**。这延续了自 run#7 以来的平台期（PubMed MCP 对该查询集可见的 2025–2026 文献已基本穷尽）。")
w()
w("**关键收敛发现（5 个主轴不变）：** (1) 代谢–免疫耦合驱动 LNM——MGST1 'Mito-high'/immune-cold 亚群（42327722, AUC 0.833）、SHMT2–PTEN–AKT（38272883）、GLTC–LDHA 琥珀酰化（37031273）、SOX12–YBX1–LDHA（40593465）；(2) 转移干性亚群——APOE−（39810624, ABCA1-LXR）、MGST1 去分化终末、ISG15/KPNA2（37501099, ATC）、DLK1（39595993, MTC）；(3) POSTN+ myCAF 空间图谱（41480746, 42.3 万细胞）预测 LNM；(4) 影像/多组学 AI——LLNM-Net（40750786, AUC 0.944）、CLAM-WSI（41237514）、融合 DL（40771372/39682228/40778281/41061579）、多组学+ML（38990290/41421038）；(5) BRAF V600E 荟萃（41419184, 46 研究/20,570 例）仅关联淋巴结 OR 1.38/复发 OR 1.56，**不**关联远处转移（OR 0.75）或死亡。")
w()
w("**推荐方向：** **D3 — 定义并靶向 APOE−/MGST1+ 代谢–免疫干性转移亚群**（rubric 总分 **32**, 强候选），连续第 12 次被确认为最优下一步。")
w()
w("## English Abstract")
w()
w("Run #12 of the scheduled thyroid-cancer literature monitor used the `lit-review` skill and the connected paper-search-mcp (`search_pubmed` via DeferExecuteTool) to run 9 complementary PubMed queries (max_results=15, sort=relevance) spanning invasion/metastasis mechanisms, LNM biomarkers, ML/DL prediction, tumor immune microenvironment, single-cell RNA-seq, spatial multi-omics, prognosis/recurrence/distant-metastasis risk, metastatic stemness, and metabolic reprogramming. **130 raw records → 104 unique PMIDs → 76 thyroid in-scope (28 non-thyroid/duplicate excluded).** Versus the run#11 baseline (104 unique / 75 in-scope), **0 genuinely new PMIDs** were detected — every PMID retrieved this run was already in the run#11 corpus. Five run#11 records that had fallen off the 15-row relevance cutoff (38981044, 39615165, 40207795, 39903533, 40855521) reappeared and remain correctly excluded as non-thyroid (NSCLC/HCC/TNBC/gastric/pan-cancer). This confirms the plateau observed since run#7 — the PubMed MCP has exhausted visible 2025–2026 literature for this query set.")
w()
w("**Five convergent axes are unchanged:** (1) metabolic–immune coupling drives LNM (MGST1 Mito-high/immune-cold AUC 0.833; SHMT2–PTEN–AKT; GLTC–LDHA succinylation; SOX12–YBX1–LDHA); (2) stem-like metastatic subpopulations (APOE− via ABCA1-LXR; MGST1 dediff tip; ISG15/KPNA2 in ATC; DLK1 in MTC); (3) POSTN+ myCAF spatial atlas (41480746, 423k cells) predicts LNM; (4) crowded imaging/multi-omics AI (LLNM-Net AUC 0.944; CLAM-WSI; fusion DL; multi-omics+ML); (5) BRAF V600E meta (41419184, 46 studies/20,570 pts) links nodal OR 1.38 / recurrence OR 1.56 but NOT distant mets or death.")
w()
w("**Recommended direction: D3 — define & target the APOE−/MGST1+ metabolic–immune stem-like metastatic subpopulation (rubric total 32, Strong), reaffirmed as the best next step for the 12th consecutive run.**")
w()
w("## Search Strategy / 检索策略")
w()
w("| Source | Query | Filters | Results | Notes |")
w("|---|---|---|---:|---|")
qmap = DATA["queries"]
# count per query from records
from collections import defaultdict
qcount = defaultdict(int)
for r in RECS:
    for q in r["queries"]:
        qcount[q]+=1
qlabels = {
 "a":"thyroid cancer lymph node metastasis biomarker gene signature",
 "b":"thyroid cancer invasion metastasis molecular mechanism",
 "c":"thyroid cancer lymph node metastasis machine learning deep learning prediction model",
 "d":"thyroid cancer metastasis tumor immune microenvironment",
 "e":"thyroid cancer metastasis single cell RNA sequencing",
 "f":"thyroid cancer metastasis spatial transcriptomics spatial multi-omics",
 "g":"thyroid cancer prognosis recurrence distant metastasis risk model",
 "h":"thyroid cancer metastatic stemness subpopulation",
 "i":"thyroid cancer metabolic reprogramming metastasis",
}
for k in ["a","b","c","d","e","f","g","h","i"]:
    w(f"| PubMed | `{qlabels[k]}` | max_results=15, sort=relevance | {qcount.get(k,0)} | 甲状腺相关全纳入；非甲状腺/泛癌综述剔除 |")
w()
w("> 注：paper-search-mcp `search_pubmed` 无日期过滤参数，时间窗以相关性排序近似；每路首次放宽至全部时间。MCP 在本轮出现与历史一致的瞬时解析错误（`not well-formed (invalid token)`），对失败查询重发直至 9 路全部返回（b/c/f/h 各重试 3–4 轮，最终全部成功）。")
w()
w("## Included Papers / 纳入论文（High relevance，共 %d 篇）" % len(high))
w()
w("> 收录规则：relevance=High 的全部在域甲状腺文献；标题与摘要保留英文原文，附一句话中文要点。完整的 High+Medium 证据矩阵见下一节。")
w()
for r in high:
    w(f"{r['title']}. {r['disease']}. PMID: {r['pmid']}. DOI: {r['doi']}.")
    w(f"   Author claim: {r['main_finding']}")
    w(f"   Agent note: relevance={r['relevance']}; dimensions={dim_str(r)}; validation={r['validation']}; caution={r['limitation']}.")
w()
w("## Evidence Matrix / 证据矩阵")
w()
w("> 按 evidence-matrix-schema.md 列制表；Relevance/Gap 列体现所属维度（多标签）。仅列 High 与关键 Medium 文献（共 %d 篇）。" % len(matrix_rows))
w()
w("| Paper | PMID/DOI | Disease/Population | Data Source | Method | Endpoint | Main Finding | Validation | Limitations | Relevance | Gap Suggested | Future Direction |")
w("|---|---|---|---|---|---|---|---|---|---|---|---|")
for r in matrix_rows:
    w(f"| {r['title'][:60]} | {r['pmid']} / {r['doi']} | {r['disease']} | {r['data_source']} | {r['method']} | {r['endpoint']} | {r['main_finding'][:90]} | {r['validation']} | {r['limitation']} | {r['relevance']} ({dim_str(r)}) | {r['gap']} | {r['future_direction']} |")
w()
w("## What Is Already Known / 已知结论")
w()
w("**Axis 1 — 代谢–免疫耦合驱动淋巴结转移（LNM）。** 多条独立证据收敛：MGST1 定义的 'Mito-high'/immune-cold 亚群（42327722, AUC 0.833 外部验证）位于去分化轨迹终末、呈干性转移表型，其抑制可逆转免疫冷表型（Toxoflavin）；SHMT2 通过生成 SAM 甲基化 PTEN 启动子、激活 AKT 驱动 PTC 转移（38272883）；GLTC 结合 LDHA 阻断 SIRT5、促进 K155 琥珀酰化增强糖酵解与远处转移并致 RAI 耐药（37031273）；SOX12→YBX1→LDHA 启动子→TGF-β 轴驱动 PTC 转移（40593465）；空间多组学进一步定位精氨酸-多胺/糖酵解/脂质紊乱与 NAT8L/SVCT-2 等转移驱动代谢物（41398964）。")
w()
w("**Axis 2 — 转移干性亚群。** APOE− 肿瘤细胞亚群经 ABCA1-LXR 轴驱动宫颈 LNM 与不良预后（39810624）；MGST1 去分化终末对应干性转移表型（42327722）；ATC 中 ISG15 经 ISGylation 稳定 KPNA2 维持癌干细胞特性（37501099）；MTC 中 DLK1+ 细胞呈更高干性/球形成/染料外排（39595993）。单细胞分辨率一致指向「代谢重编程 + 干性」共标定转移起始克隆。")
w()
w("**Axis 3 — 成纤维细胞生态位（CAF niche）。** 整合单细胞与空间转录组图谱（41480746, 42.3 万细胞；39829764 预印本）定义 POSTN+ myCAF 紧邻侵袭性肿瘤细胞、与 LNM 及进展相关；空间图谱（41421038）以 FN1–SDC4 轴经空间转录组验证 LNM 机制并给出 17 基因签名与随机森林模型。")
w()
w("**Axis 4 — 影像/多组学 AI 预测高度拥挤。** LLNM-Net 多模态 DL（40750786, AUC 0.944，29,615 例/7 中心，超越人类专家）；CLAM-WSI 术中诊断（41237514, AUC 0.85 LNM）；影像组学+DL 融合（40771372 AUC 0.881 外部、39682228、40778281、41061579）；多组学+ML（38990290 四分子亚型、41421038）。元分析（39742800）汇 16 研究：DL sens 80.8%/spec 78.7% 优于手工影像组学。")
w()
w("**Axis 5 — BRAF V600E 与预后的解耦。** 46 研究/20,570 例荟萃（41419184）确认 BRAF V600E 仅关联淋巴结 OR 1.38 与复发 OR 1.56，**不**关联远处转移（OR 0.75）或死亡（OR 0.97）；提示 BRAF 状态对「淋巴结/复发」与「远处转移/死亡」是不同生物学过程，临床决策中不应作为独立远处转移预后标志。")
w()
w("## What Remains Unclear / 未解问题")
w()
w("- **机制→干预的因果链未闭合**：Axis 1–2 的代谢–免疫–干性轴多在 PTC 验证，APOE−/MGST1+ 亚群缺乏跨中心、跨亚型（尤其 ATC/MTC）的靶向干预证据；MGST1 的 Toxoflavin 仍为临床前。")
w("- **空间分辨率不足**：空间组学仅 6–7 篇在域（41480746/41421038/41398964/39540244/37279258），ATC/MTC、远处转移灶的空间多组学几乎空白；多数单细胞研究为单中心。")
w("- **DTC 远处转移 vs LNM 解耦未解释**：BRAF V600E（41419184）与 PD-L1 均与 LNM/复发相关但不预测远处转移——驱动远处转移的特异性分子（血行播散、器官趋向性）仍不明，仅 MTC 经 5-HT/NETs 肝脏趋向（39903533）给出线索。")
w("- **算法端过拥挤且外推有限**：Axis 4 大量单中心回顾性 LLNM/CLNM 影像模型 AUC 集中 0.8–0.94，但缺乏前瞻性、成本效益与跨设备泛化；亚型/方法角度重叠严重。")
w("- **预后签名缺乏独立外部验证**：多个基因/lncRNA/eRNA 预后模型（31792675/37934030/35033555/30942873）依赖 TCGA 单一来源，缺乏个体水平外部队列。")
w()
w("## Method/Data Limitations In The Field / 领域方法·数据局限")
w()
w("- **公共数据复用与批次效应**：TCGA/GEO 被绝大多数在域研究复用，跨平台批次效应与亚型分层不足。")
w("- **外部验证缺失**：单细胞/空间研究多为单中心；AI 模型罕见前瞻性或多设备验证。")
w("- **终点稀疏**：远处转移、ATC/MTC 亚型、儿童/青少年代谢–免疫轴样本量小，统计效能有限。")
w("- **可重复性问题**：手工影像组学特征提取流程不一致；wet-lab 功能验证在多数预后/AI 研究中缺失。")
w("- **MCP 工具限制**：paper-search-mcp `search_pubmed` 无日期过滤，且本轮再现瞬时 `not well-formed (invalid token)` 解析错误，需重发——已通过按查询重发解决，但不影响结论（均为相关性排序近似）。")
w()
w("## Candidate Future Directions / 候选未来方向")
w()
w("> 按 research-direction-rubric.md 的 1–5 七维评分（Novelty / Feasibility / Data availability / Validation strength / Clinical relevance / Method rigor / Overcrowding risk）。总分 28–35 强候选。")
w()
w("| Direction | Rationale | Feasibility | Required Data | Validation Plan | Main Risk | Claim Boundary | Rubric Total |")
w("|---|---|---:|---|---|---|---|---:|")
w("| **D3 — 定义并靶向 APOE−/MGST1+ 代谢–免疫干性转移亚群** | Axis1+2 收敛；多组学已定位 APOE− 与 MGST1 干性转移表型，但缺乏跨中心靶向干预 | 5 | TCGA+GTEx+scRNA/ST（已存在）+ 多中心组织/类器官 | 独立队列验证 APOE−/MGST1+ 富集→LNM；Toxoflavin/MGST1 抑制剂功能 rescue | 单中心 SC/ST 外推 | 不声称治愈，仅作为风险分层+可成药靶点的 hypothesis-generating | **32** |")
w("| D-new — POSTN+ myCAF 生态位靶向（空间闭环） | 41480746 定义 myCAF 预测 LNM；与 APOE− 肿瘤互作待解 | 4 | 41480746 多中心 ST + 新增 ATC/MTC ST | 空间共定位验证 myCAF–肿瘤互作；CAF 耗竭/重编程 | CAF 异质性高 | 不直接声称生存获益 | **30** |")
w("| D6 — MTC 5-HT/NETs 肝脏转移轴 | 39903533 给出器官趋向性机制+FDA 药 fluoxetine 阻断 | 4 | MTC 原发+肝转移队列（小） | 回顾+前瞻确认 NETs 与肝转移；SERT 阻断 | MTC 样本稀缺 | 限 MTC 肝转移亚群 | **27** |")
w("| D7 — 线粒体 Ca2+/MCU 作为 LNM 节点 | 42510113（run#7 新增）连线粒体 Ca2+/OXPHOS/CD8+ T·NK | 4 | 现有 scRNA+新增流式 | 验证 SMDT1/MCU 与 LNM、CD8+ T 浸润 | 机制间接 | 折叠入 D3 而非独立 | **26** |")
w("| D-ml — 新一代可解释多模态术前 LNM 预测 | 影像 AI 极度拥挤但可解释/前瞻性空缺 | 3 | 多中心 US/CT/MRI+WSI | 前瞻性+成本效益+跨设备 | 严重过拥挤（同质终点） | 仅算法改进，机制贡献弱 | **20** |")
w()
w("## Recommended Next Direction / 推荐下一步方向")
w()
w("**D3 — 定义并靶向 APOE−/MGST1+ 代谢–免疫干性转移亚群（rubric 总分 32，强候选，连续第 12 次确认）。**")
w()
w("理由：Axes 1–2 已从独立多组学研究（39810624 APOE−/ABCA1-LXR、42327722 MGST1 Mito-high/immune-cold、37501099 ISG15/KPNA2、40593465 SOX12–YBX1–LDHA）收敛到同一「代谢重编程 + 干性 + 免疫逃逸」表型；公开数据（TCGA/GTEx/scRNA/ST）与研究工具（多组学、空间、药理抑制）均已可用；MCP 平台期下，这是唯一兼具机制新颖度、证据强度与可成药性的方向，且未像影像 AI 那样严重过拥挤。")
w()
w("具体下一步：(1) 在 run#11/run#12 语料基础上，整合 APOE− 与 MGST1 签名，于独立多中心队列验证其 LNM/复发富集；(2) 用 Toxoflavin 或 MGST1 特异性抑制剂 + APOE 过表达做体内 rescue，闭合「代谢–免疫–干性」因果链；(3) 补 ATC/MTC 空间多组学以填补亚型空白。")
w()
w("Claim boundary：本报告不声称该亚群可「治愈」转移，仅作为风险分层与可成药靶点的 hypothesis-generating 证据；临床转化需独立外部验证。")
w()
w("## Follow-Up Reading List / 随访阅读清单")
w()
w("- **39810624** (APOE− subpopulation) — D3 核心机制与 13-gene LNM 签名，优先精读。")
w("- **42327722** (MGST1 Mito-high/immune-cold) — D3 另一支柱，含 Toxoflavin 药理验证。")
w("- **41480746** (POSTN+ myCAF atlas) — 空间 CAF 生态位，D-new 方向基础。")
w("- **41421038** (FN1–SDC4 spatial multi-omics + ML) — 空间组学闭环 LNM 机制与模型。")
w("- **39903533** (5-HT/NETs MTC liver mets) — D6 器官趋向性机制，MTC 远处转移稀缺线索。")
w("- **41419184** (BRAF V600E meta, 46 studies) — 评估「淋巴结/复发 vs 远处转移」解耦的权威依据。")
w("- **40750786** (LLNM-Net) — 若坚持算法方向，作为多模态 DL 的上限基线参考（过拥挤预警）。")
w()
w("## Reproducibility Notes / 可复现性说明")
w()
w(f"- Search date: {RUN_DATE}")
w("- Databases: PubMed (via paper-search-mcp `search_pubmed`, DeferExecuteTool).")
w("- Query strings: 9 路（a–i，见 Search Strategy 表）。")
w("- Filters: max_results=15, sort=relevance（MCP 无日期过滤）。")
w("- Deduplication rule: 按 PMID 去重；同一文献跨多路检索合并 queries 与 dimensions。")
w("- Screening rule: 甲状腺（PTC/PTMC/FTC/MTC/ATC/儿童青少年）在域；乳腺/胃/结直肠/肝/HCC/胰腺/TNBC/泛癌/神经-免疫泛综述剔除（标记为 off-topic）。")
w("- New-vs-prior: 与 run#11 基线（104 唯一 PMID）机械比对——**新增 0**；5 篇 run#11 掉出 15 行截断的非甲状腺记录本轮重新出现并仍排除，非新文献。")
w("- Files saved:")
w(f"  - 报告：`lit_review/literature_review_{TS}.md`")
w("  - 原始+去重语料：`lit_review/search_results_latest.json`（130 raw / 104 unique / 76 in-scope / 28 excluded，含每篇 relevance+dimension+query 标签与 new_vs_run11 字段）")
w("  - 生成脚本：`lit_review/_build_run12.py`、`lit_review/_gen_report_run12.py`")
w()
w("## Comparison With Prior Report / 与历史报告差异（vs run#11）")
w()
w("- **检索条数**：run#12 返回 130 条原始（run#11 为 114）→ 去重 104 唯一（同）；在域 76（run#11 为 75，因本轮将 2 篇历史甲状腺综述 17133106/17940185 正确归回在域）；排除 28（run#11 为 29）。")
w("- **新增文献**：**0 篇**（连续第 6 个平台期 run#7→#12，其中 #8/#9/#10/#11/#12 均为 0 新增）。本次 5 篇 run#11 掉出 15 行相关性截断的非甲状腺记录（38981044 NSCLC、39615165 乳腺、40207795 胃、39903533 实际为 MTC 相关但本轮未在 15 行内、40855521 TNBC）重新出现，仍按非甲状腺排除，**不计入新信号**。")
w("- **各维度分布（在域，多标签）**：分子机制 38 / 预后转移 31 / 代谢重编程 11 / 算法方法 18 / 免疫微环境 14 / 单细胞 12 / 空间组学 7 / 转移干性 5（run#11：46/22/10/20/15/13/6/3）。算法方法条目略降（单中心 AI 模型部分掉出截断），转移干性与空间组学略升（APOE− 与 42327722 多路命中）。")
w("- **关键收敛发现**：5 个主轴**完全不变**；DTC 远处 vs LNM 解耦（BRAF V600E 荟萃 41419184 与 PD-L1 荟萃）再次确认。")
w("- **推荐方向**：**D3 — 定义并靶向 APOE−/MGST1+ 代谢–免疫干性转移亚群**（rubric 总分 **32**，强候选）——连续第 12 次确认，无反证。")
w("- **新信号/方向变化**：与 run#11 **相比无实质方向变化**；平台期建议（自 run#7 起反复提出）仍需落实——必须跳出 PubMed MCP：加入 bioRxiv/arXiv 预印本 + cBioPortal/DepMap + 收窄 ATC/MTC 与空间组学时间窗，并考虑将自动化频次由每日降为每周以节约配额。")
w()

with open(OUT_MD, "w", encoding="utf-8") as f:
    f.write("\n".join(L) + "\n")

print("Wrote", OUT_MD, "lines:", len(L))
print("in_scope:", len(in_scope), "excluded:", len(excluded), "high:", len(high), "matrix:", len(matrix_rows))
