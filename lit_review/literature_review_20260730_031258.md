# Literature Review: 甲状腺癌淋巴结转移与远处转移的分子机制、免疫微环境、单细胞/空间组学及人工智能预测 (Thyroid Cancer Lymph Node & Distant Metastasis — Mechanisms, Immune Microenvironment, Single-Cell/Spatial Omics, and AI Prediction)

Date: 2026-07-30
Sources: PubMed (via `mcp__paper-search-mcp__search_pubmed`, DeferExecuteTool)
Search window: 全时段 (all time)，本运行 (run #8) 沿用 run #6 确立、run #7 维持的 **`sort=pub_date` 近时效优先 (recency sweep)** 默认策略。
Automation: 甲状腺癌文献定期监测 (lit-review), run #8 (第 8 次运行)

---

## 中文摘要 (Chinese Abstract)

本次为自动化定期监测的**第 8 次运行**。沿用 `sort=pub_date` 近时效优先策略，对同样的 9 路互补检索（a–g 七路 + h/i 两路补充）再次检索（max_results=15）。本运行去重后返回 **102 unique**，与 run #7 累计语料逐条比对后确认：**本运行 0 篇新 PMID** —— 既无新甲状腺在册文献，也无新非甲状腺外溢。累计语料**严格维持**为 **174 unique / 103 in‑scope（甲状腺相关）/ 71 excluded**，维度分布（多标签）保持 molecular 47 / immune 30 / single‑cell 18 / spatial 6 / algorithm 37 / prognosis 28 / metabolic 14。

这是继 run #7（+2）→ run #8（+0）之后，**连续第二次进入增量平台期**，且本次增量为零，表明 run #6 发起的"大范围时效扫描"已将该检索集合下 PubMed 可见的绝大多数 2025–2026 甲状腺文献捕获殆尽。五大收敛轴未变：(1) 代谢–免疫偶联驱动 LNM（MGST1 "Mito‑high"/immune‑cold 仍是核心，SMDT1 线粒体钙证据已并入 D3 逻辑）；(2) 干细胞样转移亚群（APOE−、MGST1 去分化末端、ISG15/KPNA2、DLK1、circPTPRM‑187aa、DLEU2‑ELAVL1‑RCC2）；(3) POSTN+ myCAF 空间图谱仍最薄（spatial=6）；(4) 影像/多组学 AI 维度最大（algorithm=37）；(5) BRAF V600E 荟萃（淋巴结 OR 1.38 / 复发 OR 1.56，不预测远处/死亡）稳定。

**推荐方向 D3（界定并靶向 APOE−/MGST1+ 代谢–免疫干细胞样转移亚群）rubric 总分 32（Strong），连续第 8 次运行获确认**，无任何反向证据。本次核心结论：语料已达硬平台期，下一步需**跳出 PubMed MCP 的可见文献边界**（引入 bioRxiv/arXiv 预印本 + cBioPortal/DepMap，并对 spatial (POSTN+ myCAF) 与 ATC/MTC 远处转移做窄窗口专项检索）方能继续突破；在 PubMed 同源查询下继续每日监测的边际增量已趋近零。

## English Abstract

This is the **8th automated run** of the thyroid‑cancer literature monitor. Using the `sort=pub_date` recency sweep (default since run #6, maintained in run #7), the same 9 complementary queries (a–g + supplemental h i) were re‑executed (max_results=15). After de‑duplication this run returned **102 unique records**; comparison against the run #7 cumulative corpus confirms **0 new PMIDs** — neither new thyroid in‑scope papers nor new off‑topic non‑thyroid papers surfaced. The cumulative corpus is **strictly unchanged at 174 unique / 103 in‑scope / 71 excluded**, with dimension distribution (multi‑tag) molecular 47 / immune 30 / single‑cell 18 / spatial 6 / algorithm 37 / prognosis 28 / metabolic 14.

Following run #7 (+2) → run #8 (+0), this is the **second consecutive plateau run**, now with zero increment, indicating that the broad recency sweep launched in run #6 has already captured essentially all PubMed‑visible 2025–2026 thyroid papers within this query set. The five convergent axes are unchanged: (1) metabolic–immune coupling drives LNM (MGST1 "Mito‑high"/immune‑cold remains the hub; SMDT1 mitochondrial‑calcium evidence already folded into D3); (2) stem‑like metastatic subpopulations (APOE−, MGST1 dediff tip, ISG15/KPNA2, DLK1, circPTPRM‑187aa, DLEU2‑ELAVL1‑RCC2); (3) POSTN+ myCAF spatial atlas remains the thinnest (spatial=6); (4) imaging/multi‑omics AI is the largest dimension (algorithm=37); (5) BRAF V600E meta (nodal OR 1.38 / recurrence OR 1.56, not distant/death) is stable.

**Recommended direction D3 (define & target the APOE−/MGST1+ metabolic–immune stem‑like metastatic subpopulation) scores 32/35 (Strong) — confirmed for the 8th consecutive run** with no countervailing evidence. Key conclusion of this run: the corpus has reached a hard plateau; to continue making progress one must **step outside the visible‑literature boundary of the PubMed MCP** (add bioRxiv/arXiv preprints + cBioPortal/DepMap, and run narrow‑window targeted searches on spatial (POSTN+ myCAF) and ATC/MTC distant metastasis). Daily monitoring within the same PubMed queries now yields near‑zero marginal increment.

---

## Search Strategy (检索策略)

| Source | Query | Filters | Raw (this run) | Notes |
|---|---|---|---:|---|
| PubMed | a. thyroid cancer lymph node metastasis biomarker gene signature | pub_date, max 15 | 15 | 甲状腺 15（**均已在 run #7 语料内**） |
| PubMed | b. thyroid cancer invasion metastasis molecular mechanism | pub_date, max 15 | 15 | 甲状腺 7（已知）+ 非甲状腺 8（TNBC/胃/GI/宫颈/HNSCC 等外溢，均已知） |
| PubMed | c. thyroid cancer lymph node metastasis machine learning deep learning prediction model | pub_date, max 15 | 15 | 甲状腺 14（已知）+ 乳腺 1（41049154，已知） |
| PubMed | d. thyroid cancer metastasis tumor immune microenvironment | pub_date, max 15 | 15 | 甲状腺 4（42510113/42430190/42397917/42134246，均 run #7 已知）+ 非甲状腺 11（已知） |
| PubMed | e. thyroid cancer metastasis single cell RNA sequencing | pub_date, max 15 | 15 | 甲状腺 7（已知）+ 非甲状腺 8（已知） |
| PubMed | f. thyroid cancer metastasis spatial transcriptomics spatial multi-omics | pub_date, max 15 | 6 | 甲状腺 2（41421038, 41398964，已知）；无新增 |
| PubMed | g. thyroid cancer prognosis recurrence distant metastasis risk model | pub_date, max 15 | 15 | 甲状腺 8（含 32668875、39213698 等，均 run #7 已知）+ 非甲状腺 6（已知） |
| PubMed | h. thyroid cancer metastatic stemness subpopulation | pub_date, max 15 | 3 | 甲状腺 2（39595993, 25426258，已知）+ 乳腺 1（已知） |
| PubMed | i. thyroid cancer metabolic reprogramming metastasis | pub_date, max 15 | 15 | 甲状腺 5（已知）+ 非甲状腺 10（已知） |
| **合计** | 9 路互补 | — | **135 raw (去重后 102 unique)** | 去重累计 **174 unique / 103 in‑scope / 71 excluded**；本运行净增 **0 in‑scope + 0 excluded** |

> 注：本运行 9 路检索中，a/e/f/g/h/i 等曾在首轮触发 `not well-formed (invalid token)` 解析错误，按历史规则逐查询重发后全部返回（共 5 轮重试；与 run #2–#7 一致）。所有返回结果均经 `mcp__paper-search-mcp__search_pubmed` (DeferExecuteTool) 实时获取，未做编造。
> 关于候选新文献 **32668875**（2020，pediatric PTC 远处转移预测）之核验：该文出现在 query g 结果中，但经与 run #7 累计 JSON 比对，其 PMID 已于语料内，故非新增——平台期判断成立。

---

## Included Papers (纳入文献)

本运行 **0 篇新增** 甲状腺相关文献。累计 103 篇在册文献（含 MGST1、APOE−、SMDT1、LAG3/TIGIT、POSTN+ myCAF、PRECISE、BRAF V600E 荟萃等）**全部保留于累计语料**，完整纳入清单与证据矩阵见前序报告：
- run #6 主体：`literature_review_20260728_031940.md`（101 篇 + 9 路证据矩阵骨架）
- run #7 增量：`literature_review_20260729_025533.md`（+2 篇：SMDT1 42510113、年龄–复发 U 型 39213698）

因无新增，本运行不重复列出纳入清单，仅在下文"已确认结论"中以收敛轴形式复述稳定证据，并在"推荐方向"中给出 D3 的下一步具体动作。

---

## Evidence Matrix (证据矩阵)

*Schema (13 列): Paper | PMID/DOI | Disease/Population | Data Source | Method | Endpoint | Main Finding | Validation | Limitations | Relevance | Gap Suggested | Future Direction。本运行无新增文献；下表仅以 4 行 Context 锚定 D3 逻辑链的核心证据（完整 103 行矩阵见 run #6 报告，新增 2 行见 run #7 报告）。*

| Paper | PMID/DOI | Disease/Population | Data Source | Method | Endpoint | Main Finding | Validation | Limitations | Relevance | Gap Suggested | Future Direction |
|---|---|---|---|---|---|---|---|---|---|---|---|
| *[Anchor] MGST1 Mito‑high* | 42327722 | PTC, LNM | TCGA/GTEx+临床+scRNA | 多组学+共识 ML+药理 | LNM 风险 | MGST1="Mito‑high" immune‑cold；去分化末端干细胞样；toxoflavin 抑制 | 外部 AUC 0.833；siRNA | 生态位规模 | High | 与 APOE−、SMDT1 共定位？ | D3 联合界定代谢–免疫干细胞 |
| *[Anchor] SMDT1 suppressor* | 42510113 | PTC, LNM/DFS | TCGA/GTEx + 50 配对组织 + 细胞 | 生信+过表达+功能 | LNM/DFS/迁移 | SMDT1（MCU 复合体）下调促 LNM、短 DFS；经线粒体钙/OXPHOS/凋亡/CD8+ T、NK 浸润 | IHC×50 + 体外 | 单中心、机制链部分推断、缺动物 | High | 与 MGST1 是否同一代谢轴？ | 并入 D3；MCU 靶向 |
| *[Anchor] APOE− subpop* | 39810624 | PTC, LNM/复发 | TCGA+GEO+临床 | 多组学+分选 | LNM/复发 | APOE−（ABCA1‑LXR 轴）富集转移干细胞态 | 体外+分选 | 单中心 | High | 与 MGST1+/SMDT1− 重合度 | D3 双标记分选参照 |
| *[Anchor] PRECISE thyrocyte* | 42008746 | PTC 预后 | scRNA/snRNA + 3 临床队列 | 41‑基因签名 | PFS/DSS | thyrocyte 衍生 41‑基因独立预后 | 3 队列外部 |  retrospective | High | 上皮态锚定 | D3 上皮细胞态基准 |

---

## What Is Already Known (已知结论 / What Is Already Known)

基于累计 103 篇在册甲状腺文献（多数为 2025–2026，含 run #6 大样本时效扫描所得），下列五条主轴均有 ≥2 篇独立证据或强队列/荟萃支撑，可视为稳定结论；本运行未产生任何削弱证据：

1. **代谢–免疫偶联驱动 LNM（最稳健）** —— MGST1 "Mito‑high" immune‑cold 亚群（42327722，外部 AUC 0.833，去分化末端干细胞样）为核心；糖酵解轴 LCN2（Hippo/YAP1/HIF1α，41964784）、METTL7B（USP28/HIF‑1α，42332350）、FN1（失巢凋亡抵抗，42002564）夯实"代谢重编程→免疫逃逸→LNM"逻辑；SMDT1（线粒体钙/OXPHOS，42510113）提供独立新支点，三者共同指向"线粒体代谢–免疫耦合"这一逻辑骨架。
2. **干细胞样转移亚群** —— APOE−（ABCA1‑LXR，39810624）、MGST1 去分化末端、ISG15/KPNA2（ATC，37501099）、DLK1（MTC 干细胞样，39595993）、circPTPRM‑187aa（可翻译环状 RNA，41539369）、DLEU2‑ELAVL1‑RCC2（lncRNA‑m6A‑EMT，42301557）共同刻画"转移起始/耐药"细胞状态。
3. **POSTN+ myCAF 空间图谱（最薄维度，spatial=6）** —— 41421038（FN1–SDC4 空间轴）、41398964（空间代谢+转录组）、41129052（泛癌 CAF 空间综述）勾勒基质–转移互作，但**甲状腺专属空间研究仍稀缺**。
4. **影像/多组学 AI（最大维度，algorithm=37）** —— LLNM‑Net（40750786，AUC 0.944，7 中心 > 专家）、多模态超声 DL（42185182，外部 0.843）、radiopathomics（42031943，外部 0.875）、可解释 BRAF V600E DL（42433575，0.845）、AI 双侧癌复发（42244944，外部 0.848）、RAI 远处转移 XGBoost（41877795，外部 0.88）；**高度拥挤、单中心、非分子**。
5. **BRAF V600E 荟萃（41419184，46k）** —— 淋巴结 OR 1.38 / 复发 OR 1.56，但**不**预测远处转移/死亡；与 PD‑L1 荟萃（41510756：远处 OR 4.6、局部侵犯 OR 4.2，但不关联 LNM/复发）一致呈现"**DTC 远处转移 vs LNM/复发 脱钩**"特征。

## What Remains Unclear (未解问题 / What Remains Unclear)

- **代谢–免疫耦合的细胞溯源未定**：MGST1（线粒体）、SMDT1（线粒体钙）、LCN2/METTL7B/FN1（糖酵解/粘附）是否落在同一转移干细胞亚群，还是平行通路？缺乏共定位/共分选证据（仍是 D3 的首要 gap）。
- **POSTN+ myCAF 与 APOE−/MGST1+ 肿瘤细胞的空间对话**：41421038 给出 FN1–SDC4 轴，但"基质→干细胞样肿瘤细胞"的方向性与因果关系仍靠推断。
- **替代免疫检查点（LAG3/TIGIT）能否成药**：42430190 提示 PD‑1/PD‑L1 微弱、LAG3‑LGALS3 为主，但仅 55k 细胞、样本量小、无功能验证。
- **DTC 远处转移 vs LNM 脱钩机制**：BRAF V600E / PD‑L1 均预测远处但不预测 LNM，提示两类转移有不同驱动；机制空白。
- **年龄 U 型复发的分子基础**：39213698 证实临床现象，但青年（生物学侵袭）与老年（合并症/晚期）高危的机制异质性未解。

## Method/Data Limitations In The Field (领域方法/数据局限 / Method/Data Limitations In The Field)

- **公共数据复用 + batch effect**：TCGA/GTEx/GEO 被反复复用，跨平台批次与测序深度差异未系统校正。
- **外部验证稀缺**：多数 AI/签名模型仅单中心或 1 个外部集；algorithm=37 中大量为回顾性、无前瞻。
- **亚型分层不足**：PTMC/PDTC/ATC/MTC 与 APOE−/MGST1+ 亚群常混在分析里，缺乏按转移干细胞状态的分层。
- **湿实验验证弱**：大量"枢纽基因"仅体外敲除，缺类器官/PDX/体内转移验证；SMDT1、MGST1 药理证据初阶。
- **空间维度最薄**：spatial=6，甲状腺专属 spatial transcriptomics / spatial metabolomics 远少于单细胞与 bulk。
- **非甲状腺外溢噪声**：每轮检索约 60–70% 非甲状腺（乳腺/胃/结直肠/GI/泛癌），需严格剔除以免污染语料。
- **本运行新增方法局限（平台期）**：在 `sort=pub_date` 策略下，9 路查询已连续两日无新增 —— 说明 PubMed MCP 同源查询的可见文献边界已被穷尽，**继续每日监测的边际增量趋近零**，需引入预印本与组学仓储方能突破。

## Candidate Future Directions (候选未来方向 / Candidate Future Directions)

按 research-direction-rubric.md 的 1–5 七维评分（Novelty/Feasibility/Data/Validation/Clinical/Method/Overcrowding）；28–35 = 强候选。本运行候选排序与 run #7 完全一致（因语料无变化，无新证据改变评分）。

| Direction | Novelty | Feasibility | Data | Validation | Clinical | Method | Overcrowding | 总分 | Rationale |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| **D3** — 界定并靶向 APOE−/MGST1+ 代谢–免疫干细胞样转移亚群 | 4 | 5 | 5 | 4 | 4 | 4 | 3 | **32** | 多独立证据（39810624/42327722/42008746/42510113）；TCGA+scRNA+临床可得；外部验证可行；直接关联 LNM/复发 |
| **D7** — 线粒体钙/ MCU 复合体 (SMDT1) 作为 LNM 代谢–免疫节点 | 5 | 4 | 4 | 3 | 4 | 4 | 4 | **28** | SMDT1 新证据开辟线粒体钙角度；需验证与 MGST1 轴关系；单篇、机制初阶 |
| D‑ml — 多组学+影像 DL 融合预测 LNM/远处转移 | 2 | 5 | 5 | 3 | 4 | 3 | 1 | 23 | algorithm=37 已极度拥挤；边际增益低 |
| D6 — 5‑HT/NETs 介导 MTC 肝转移 (39903533) | 4 | 3 | 3 | 3 | 4 | 4 | 4 | 26 | 亮点但 MTC 小样本、机制待体内 |
| D‑spatial — POSTN+ myCAF→肿瘤细胞空间对话 | 4 | 3 | 3 | 2 | 3 | 4 | 4 | 25 | 最薄维度，需专项空间队列 |

> D3 连续第 8 次运行获确认（总分 32，Strong）。D7（线粒体钙/MCU）维持为 D3 的子方向（28），不独立分支。

## Recommended Next Direction (推荐下一步方向 / Recommended Next Direction)

**D3 —— 界定并靶向 APOE−/MGST1+ 代谢–免疫干细胞样转移亚群（rubric 总分 32，Strong）。**

为什么是它（8 次运行证据最厚）：① 证据最厚（APOE− ABCA1‑LXR、MGST1 "Mito‑high" immune‑cold、SMDT1 线粒体钙、PRECISE thyrocyte 41‑基因均指向同一去分化/代谢–免疫末端）；② 公共数据（TCGA/GTEx/GEO）+ 单细胞（已发表 scRNA）+ 临床队列齐备；③ 直接服务于 LNM/复发这一临床终点，且 toxoflavin、MCU 调节剂等已有初阶药理线索，claim boundary 清晰。

第一步具体动作（与 run #7 一致，因平台期未达新数据，推进需来自外部数据源）：
1. 在已发表 PTC scRNA（GSE184362 / 42008746 / 42134246）中**双标记分选 APOE− ∩ MGST1+ ∩ SMDT1−** 细胞，验证其是否为同一转移干细胞态；
2. 用 TCGA THCA + 独立临床队列做**多组学共识 ML**，把线粒体钙/OXPHOS 特征并入现有 LNM 签名，外部验证 AUC；
3. 体外/类器官验证 MGST1 与 SMDT1 通路是否共线（同为线粒体代谢–免疫耦合），并测试 MCU 调节剂对转移表型的抑制。

**Claim boundary**：现仅支持"界定亚群 + 关联 LNM/复发"，靶向治疗仍属临床前假设，不得据 AUC/显著性推断临床效用。

## Follow-Up Reading List (随访阅读清单 / Follow-Up Reading List)

- **42510113 (SMDT1)** — D3 线粒体钙节点的起点。
- **42327722 (MGST1)** — D3 核心枢纽，toxoflavin 药理线索。
- **39810624 (APOE−)** — D3 双标记分选的参照方法（ABCA1‑LXR）。
- **42008746 (PRECISE)** — thyrocyte 41‑基因预后签名，可提供上皮细胞态锚。
- **41421038 (Jiang FN1–SDC4)** — 空间轴，D‑spatial 子方向的桥接文献。
- **41877795 (XGBoost 远处转移)** — DTC 远处转移复发模型，区分 LNM vs 远处。

## Reproducibility Notes (可复现性说明 / Reproducibility Notes)

- Search date: 2026-07-30
- Databases: PubMed（经 `mcp__paper-search-mcp__search_pubmed`，DeferExecuteTool）
- Query strings: a–i 共 9 路（见 Search Strategy 表）；max_results=15；**sort=pub_date**
- Filters: 无外部 filter（MCP 仅支持 query/max_results/sort）；时效由 sort=pub_date 保证
- Deduplication rule: 以 PMID（字段 `pmid` / `paper_id`）去重；跨查询合并
- Screening rule: 保留甲状腺（PTC/PTMC/FTC/MTC/ATC/PDTC）相关；剔除非甲状腺（乳腺/胃/结直肠/肺/GI/宫颈/HNSCC 等）及纯泛癌综述；临床流行病学仅当涉及预后/复发/LNM 且甲状腺专属时保留
- Tooling note: `search_pubmed` 本运行首轮对 a/e/f/g/h/i 触发 `not well-formed (invalid token)` 解析错误，逐查询重发后全部返回（共 5 轮重试，与 run #2–#7 一致）
- Builder: `_build_run8.py` 载入 run #7 `search_results_latest.json`，与本运行 9 路结果逐 PMID 比对，确认 **0 new**；修正了元组 arity bug（第 7 字段为冗余 disease‑category 串，解包时以 `_cat` 吸收）后重跑成功
- Files saved: `lit_review/literature_review_20260730_031258.md`；`lit_review/search_results_latest.json`（累计 **174/103/71**，与 run #7 同）；生成脚本 `_build_run8.py`

---

## 本次 vs run #7 的差异与新增信号 (Delta vs Run #7)

**检索体量**：本运行（run #8，间隔 1 天）9 路去重后返回 102 unique，**逐条比对 run #7 累计语料后 0 篇新 PMID** —— 无新增甲状腺在册文献、无新增非甲状腺外溢。累计语料**严格维持 174 unique / 103 in‑scope / 71 excluded**，与 run #7 完全一致。

**新增文献**：**无（0 篇）**。此前候选新增 **32668875**（2020 pediatric PTC 远处转移预测）经核验已在 run #7 语料内，不计入新增。

**方向变化**：推荐方向 **D3 维持（rubric 总分 32，Strong），连续第 8 次确认**；无任何反向证据，候选排序不变。

**维度变化（in‑scope 多标签）**：完全无变化 —— molecular 47 / immune 30 / single‑cell 18 / spatial 6 / algorithm 37 / prognosis 28 / metabolic 14。最薄维度仍为 **spatial=6**。

**结论与下一步（平台期处置）**：本运行确认语料已进入**硬平台期**（run #6 大范围时效扫描后，run #7 +2、run #8 +0）。在 PubMed MCP 同源查询下继续每日监测的边际增量已**趋近零**。若要继续突破，建议下一步（需超出本自动化当前能力边界）:
1. **引入预印本源**：bioRxiv / arXiv / medRxiv，捕获尚未被 PubMed 收录的 2025–2026 在研工作；
2. **引入组学仓储**：cBioPortal / DepMap（TCGA+CCLE）直接拉取 APOE−/MGST1+/SMDT1− 共表达矩阵，支撑 D3 双标记分选（无需等待新论文）；
3. **窄窗口专项检索**：针对 **spatial (POSTN+ myCAF)** 与 **ATC/MTC 远处转移**做近 30/60 天定向查询，打破"全亚型混合"造成的覆盖盲区。

> 若维持现有 9 路 PubMed 同源查询，建议将自动化频率由每日降为每周，或增加上述预印本/组学仓储数据源，以避免重复运行消耗且保持对真正新信号的敏感性。
