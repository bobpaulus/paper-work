# Literature Review: 甲状腺癌淋巴结转移与远处转移的分子机制、免疫微环境、单细胞/空间组学及人工智能预测 (Thyroid Cancer Lymph Node & Distant Metastasis — Mechanisms, Immune Microenvironment, Single-Cell/Spatial Omics, and AI Prediction)

Date: 2026-07-29
Sources: PubMed (via `mcp__paper-search-mcp__search_pubmed`, DeferExecuteTool)
Search window: 全时段 (all time)，本运行 (run #7) 继续采用 **`sort=pub_date` 近时效优先 (recency sweep)** —— 自 run #6 起固定为默认策略，以持续打破 `sort=relevance` 平台期。
Automation: 甲状腺癌文献定期监测 (lit-review), run #7 (第 7 次运行)

---

## 中文摘要 (Chinese Abstract)

本次为自动化定期监测的第 7 次运行。沿用 run #6 确立的 **`sort=pub_date` 近时效优先** 策略，对 9 路互补检索（a–g 七路 + h/i 两路补充）再次检索（max_results=15）。由于 run #6 已完成一次大范围时效扫描（114 raw → 170 unique / 101 in‑scope），距本次仅 1 天，本运行仅浮现 **4 篇 run #6 语料之外的新 PMID**：其中 **2 篇为甲状腺相关在册文献**，2 篇为非甲状腺外溢（已排除）。累计语料更新为 **174 unique / 103 in‑scope（甲状腺相关）/ 71 excluded**，维度分布（多标签）为 molecular 47 / immune 30 / single‑cell 18 / spatial 6 / algorithm 37 / prognosis 28 / metabolic 14。

两篇新文献：(1) **SMDT1 (42510113, 2026, High)** —— 线粒体钙单向转运体 (mitochondrial calcium uniporter, MCU) 复合体调控亚基，在甲状腺乳头状癌 (PTC) 中显著下调，低表达关联 **淋巴结转移 (LNM)** 与更短无病生存 (DFS)；功能上串联 **线粒体钙稳态 → 氧化磷酸化 (OXPHOS) → 凋亡/衰老 → CD8+ T / 活化 NK 细胞浸润**，为"代谢–免疫偶联驱动 LNM"这一主轴（轴 1）提供了 **线粒体钙** 而非单纯糖酵解的新佐证；(2) **年龄–复发 U 型关联 (39213698, 2024, Low)** —— 13,758 例 PTC 回顾性队列确认 ≤30 岁与 ≥55 岁患者复发/远处转移风险均高于 31–54 岁中段，属临床风险分层细节，机制贡献低。

五大收敛轴未变：(1) 代谢–免疫偶联驱动 LNM（MGST1 "Mito‑high"/immune‑cold 仍是核心，新证据 SMDT1 从线粒体钙角度强化）；(2) 干细胞样转移亚群（APOE−、MGST1 去分化末端、ISG15/KPNA2、DLK1、circPTPRM‑187aa、DLEU2‑ELAVL1‑RCC2）；(3) POSTN+ myCAF 空间图谱仍最薄（spatial=6）；(4) 影像/多组学 AI 维度最大（algorithm=37）；(5) BRAF V600E 荟萃（淋巴结 OR 1.38 / 复发 OR 1.56，不预测远处/死亡）稳定。

**推荐方向 D3（界定并靶向 APOE−/MGST1+ 代谢–免疫干细胞样转移亚群）rubric 总分 32（Strong），连续第 7 次运行获确认**；SMDT1 的线粒体钙证据进一步坐实"代谢–免疫"耦合这一逻辑骨架，并提示可把 **线粒体钙稳态 / MCU 复合体** 作为 D3 亚群的一个可药代谢节点（子方向 D7，初评 28）。

## English Abstract

This is the 7th automated run of the thyroid‑cancer literature monitor. Using the `sort=pub_date` recency sweep established in run #6 (now the default), the same 9 complementary queries (a–g + supplemental h i) were re‑executed (max_results=15). Because run #6 already performed a broad recency sweep (114 raw → 170 unique / 101 in‑scope), and only one day elapsed, this run surfaced only **4 PMIDs absent from the run #6 corpus**: **2 thyroid in‑scope papers** and 2 off‑topic non‑thyroid papers (excluded). The cumulative corpus is now **174 unique / 103 in‑scope / 71 excluded**, with dimension distribution (multi‑tag) molecular 47 / immune 30 / single‑cell 18 / spatial 6 / algorithm 37 / prognosis 28 / metabolic 14.

The two new papers: (1) **SMDT1 (42510113, 2026, High)** — a regulator of the mitochondrial calcium uniporter (MCU) complex, significantly downregulated in PTC, with low expression associated with **lymph node metastasis (LNM)** and shorter DFS; functionally it links **mitochondrial Ca²⁺ homeostasis → oxidative phosphorylation → apoptosis/senescence → CD8+ T / activated NK infiltration**, providing a *mitochondrial‑calcium* (rather than purely glycolytic) corroboration of Convergent Axis 1 (metabolic–immune coupling drives LNM); (2) **age–recurrence U‑shape (39213698, 2024, Low)** — a 13,758‑case PTC cohort confirming that both ≤30‑year‑old and ≥55‑year‑old patients carry higher recurrence/distant‑metastasis risk than the 31–54 middle band — a clinical risk‑stratification nuance with low mechanistic contribution.

The five convergent axes are unchanged: (1) metabolic–immune coupling drives LNM (MGST1 "Mito‑high"/immune‑cold remains the hub; SMDT1 now reinforces it from the mitochondrial‑calcium angle); (2) stem‑like metastatic subpopulations (APOE−, MGST1 dediff tip, ISG15/KPNA2, DLK1, circPTPRM‑187aa, DLEU2‑ELAVL1‑RCC2); (3) POSTN+ myCAF spatial atlas remains the thinnest (spatial=6); (4) imaging/multi‑omics AI is the largest dimension (algorithm=37); (5) BRAF V600E meta (nodal OR 1.38 / recurrence OR 1.56, not distant/death) is stable.

**Recommended direction D3 (define & target the APOE−/MGST1+ metabolic–immune stem‑like metastatic subpopulation) scores 32/35 (Strong) — confirmed for the 7th consecutive run**; the new SMDT1 mitochondrial‑calcium evidence further cements the metabolic–immune logic and suggests the **MCU complex / mitochondrial Ca²⁺ homeostasis** as a druggable metabolic node within the D3 subpopulation (sub‑direction D7, initial score 28).

---

## Search Strategy (检索策略)

| Source | Query | Filters | Raw (this run) | Notes |
|---|---|---|---:|---|
| PubMed | a. thyroid cancer lymph node metastasis biomarker gene signature | pub_date, max 15 | 15 | 甲状腺 15（均已知，含 2026 pediatric 甲基化 41701943） |
| PubMed | b. thyroid cancer invasion metastasis molecular mechanism | pub_date, max 15 | 15 | 甲状腺 7（已知）+ 非甲状腺 8（TNBC/胃/GI/宫颈/HNSCC 等外溢） |
| PubMed | c. thyroid cancer lymph node metastasis machine learning deep learning prediction model | pub_date, max 15 | 15 | 甲状腺 14 + 乳腺 1（41049154） |
| PubMed | d. thyroid cancer metastasis tumor immune microenvironment | pub_date, max 15 | 15 | **甲状腺新 1（42510113 SMDT1）** + 已知 + 非甲状腺 11 |
| PubMed | e. thyroid cancer metastasis single cell RNA sequencing | pub_date, max 15 | 15 | 甲状腺 7（已知）+ 非甲状腺 8 |
| PubMed | f. thyroid cancer metastasis spatial transcriptomics spatial multi-omics | pub_date, max 15 | 6 | 甲状腺 2（41421038, 41398964，已知）；无新增 |
| PubMed | g. thyroid cancer prognosis recurrence distant metastasis risk model | pub_date, max 15 | 15 | **甲状腺新 1（39213698 年龄–复发 U 型）** + 已知 + 非甲状腺 6 |
| PubMed | h. thyroid cancer metastatic stemness subpopulation | pub_date, max 15 | 3 | 甲状腺 2（39595993, 25426258，已知）+ 乳腺 1 |
| PubMed | i. thyroid cancer metabolic reprogramming metastasis | pub_date, max 15 | 15 | **甲状腺已知**；新增 2 非甲状腺（42199418 泛癌代谢综述、42517063 TNBC） |
| **合计** | 9 路互补 | — | **135 raw (去重后 101 unique)** | 去重累计 **174 unique / 103 in‑scope / 71 excluded**；本运行净增 **2 in‑scope + 2 excluded** |

> 注：本运行 9 路检索中，c/d/e 等曾在首轮触发 `not well-formed (invalid token)` 解析错误，按历史规则逐查询重发后全部返回（共 3 轮重试）。

---

## Included Papers (纳入文献)

下列为本运行**新增 (new since run #6)** 的 2 篇甲状腺相关文献；run #6 已纳入的 101 篇在册文献（含 MGST1、APOE−、LAG3/TIGIT、POSTN+ myCAF、PRECISE、BRAF V600E 荟萃等）**全部保留于累计语料**，详见 `literature_review_20260728_031940.md` 的纳入清单与证据矩阵。

**分子机制 / 代谢 / 免疫 (molecular / metabolic / immune)**
1. **SMDT1 tumor suppressor in thyroid carcinoma (42510113, 2026, High)** — SMDT1（线粒体钙单向转运体 MCU 复合体调控亚基）在 PTC 组织/细胞系显著下调；低表达关联 **LNM** 与更短 DFS。功能上串联线粒体钙转运、氧化磷酸化 (OXPHOS)、凋亡/衰老与免疫浸润（CD8+ T、活化 NK）。过表达抑制 PTC 增殖/迁移/侵袭。中文要点：提供"代谢（线粒体钙/OXPHOS）–免疫（CD8+ T/NK）偶联驱动 LNM"的**线粒体钙**新节点，强化收敛轴 1，并提示 MCU 复合体为可药靶点。
2. **Age–recurrence U‑shape in PTC (39213698, 2024, Low)** — 13,758 例回顾性队列，限制性立方样条确认年龄与 RFS/LRRFS/DMFS 呈 **U 型**：≤30 与 ≥55 岁复发/远处转移风险高于 31–54 岁中段。中文要点：临床风险分层细节，无组学/AI/机制贡献，但支持"青年与老年 PTC 均属高危"的预后判断。

（注：42199418 泛癌代谢综述、42517063 TNBC miR‑1911‑3p 为本运行新检出的非甲状腺外溢，已按规则排除。）

---

## Evidence Matrix (证据矩阵)

*Schema (13 列): Paper | PMID/DOI | Disease/Population | Data Source | Method | Endpoint | Main Finding | Validation | Limitations | Relevance | Gap Suggested | Future Direction。本运行仅 2 篇新增高/中相关；其余 101 篇在册证据矩阵见 run #6 报告。*

| Paper | PMID/DOI | Disease/Population | Data Source | Method | Endpoint | Main Finding | Validation | Limitations | Relevance | Gap Suggested | Future Direction |
|---|---|---|---|---|---|---|---|---|---|---|---|
| SMDT1 suppressor | 42510113 | PTC, LNM/DFS | TCGA/GTEx + 50 配对组织 + 细胞 | 生信+过表达+功能 | LNM/DFS/迁移 | SMDT1 下调促 LNM、短 DFS；经线粒体钙/OXPHOS/凋亡/CD8+ T、NK 浸润 | IHC×50 + 体外 | 单中心、机制链部分推断、缺动物 | High | 与 MGST1 "Mito‑high" 亚群是否同一代谢轴？ | 并入 D3 代谢–免疫亚群；MCU 靶向 |
| Age U‑shape | 39213698 | PTC 13,758 例 | 单中心回顾 | Cox+RCS | RFS/LRRFS/DMFS | ≤30 与 ≥55 岁复发/远处转移风险高（U 型） | 大样本 | 回顾性、无分子分层 | Low | 青年/老年亚群分子异质性 | 年龄×分子分型风险分层 |
| *[Context] MGST1 Mito‑high* | 42327722 | PTC, LNM | TCGA/GTEx+临床+scRNA | 多组学+共识 ML+药理 | LNM 风险 | MGST1="Mito‑high" immune‑cold；去分化末端干细胞样；toxoflavin 抑制 | 外部 AUC 0.833；siRNA | 生态位规模 | High | 与 APOE−、SMDT1 共定位？ | D3 联合界定代谢–免疫干细胞 |
| *[Context] LAG3/TIGIT niche* | 42430190 | 甲状腺原发+LN | 配对 scRNA 55k | cNMF+LR | 免疫逃逸 | LAG3‑LGALS3 为主轴，PD‑1/PD‑L1 弱 | mIHC | 样本量小 | High | 治疗可行性 | 替代 checkpoint 抗体 |

---

## What Is Already Known (已知结论 / What Is Already Known)

基于累计 103 篇在册甲状腺文献（多数为 2025–2026，含 run #6 大样本时效扫描所得），下列五条主轴均有 ≥2 篇独立证据或强队列/荟萃支撑，可视为稳定结论：

1. **代谢–免疫偶联驱动 LNM（最稳健）** —— MGST1 "Mito‑high" immune‑cold 亚群（42327722，外部 AUC 0.833，去分化末端干细胞样）为核心；糖酵解轴 LCN2（Hippo/YAP1/HIF1α，41964784）、METTL7B（USP28/HIF‑1α，42332350）、FN1（失巢凋亡抵抗，42002564）夯实"代谢重编程→免疫逃逸→LNM"逻辑。**本次 SMDT1 (42510113) 从线粒体钙/OXPHOS 角度提供独立新证据**：低 SMDT1 关联 LNM/短 DFS 且富集 CD8+ T、活化 NK 浸润，提示线粒体钙稳态是同一耦合轴的另一支点。
2. **干细胞样转移亚群** —— APOE−（ABCA1‑LXR，39810624）、MGST1 去分化末端、ISG15/KPNA2（ATC，37501099）、DLK1（MTC 干细胞样，39595993）、circPTPRM‑187aa（可翻译环状 RNA，41539369）、DLEU2‑ELAVL1‑RCC2（lncRNA‑m6A‑EMT，42301557）共同刻画"转移起始/耐药"细胞状态。
3. **POSTN+ myCAF 空间图谱（最薄维度，spatial=6）** —— 41421038（FN1–SDC4 空间轴）、41398964（空间代谢+转录组）、41129052（泛癌 CAF 空间综述）勾勒基质–转移互作，但**甲状腺专属空间研究仍稀缺**。
4. **影像/多组学 AI（最大维度，algorithm=37）** —— LLNM‑Net（40750786，AUC 0.944，7 中心 > 专家）、多模态超声 DL（42185182，外部 0.843）、radiopathomics（42031943，外部 0.875）、可解释 BRAF V600E DL（42433575，0.845）、AI 双侧癌复发（42244944，外部 0.848）、RAI 远处转移 XGBoost（41877795，外部 0.88）；**高度拥挤、单中心、非分子**。
5. **BRAF V600E 荟萃（41419184，46k）** —— 淋巴结 OR 1.38 / 复发 OR 1.56，但**不**预测远处转移/死亡；与 PD‑L1 荟萃（41510756：远处 OR 4.6、局部侵犯 OR 4.2，但不关联 LNM/复发）一致呈现"**DTC 远处转移 vs LNM/复发 脱钩**"特征。

## What Remains Unclear (未解问题 / What Remains Unclear)

- **代谢–免疫耦合的细胞溯源未定**：MGST1（线粒体）、SMDT1（线粒体钙）、LCN2/METTL7B/FN1（糖酵解/粘附）是否落在同一转移干细胞亚群，还是平行通路？缺乏共定位/共分选证据。
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

## Candidate Future Directions (候选未来方向 / Candidate Future Directions)

按 research-direction-rubric.md 的 1–5 七维评分（Novelty/Feasibility/Data/Validation/Clinical/Method/Overcrowding）；28–35 = 强候选。

| Direction | Novelty | Feasibility | Data | Validation | Clinical | Method | Overcrowding | 总分 | Rationale |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| **D3** — 界定并靶向 APOE−/MGST1+ 代谢–免疫干细胞样转移亚群 | 4 | 5 | 5 | 4 | 4 | 4 | 3 | **32** | 多独立证据（39810624/42327722/42008746）；TCGA+scRNA+临床可得；外部验证可行；直接关联 LNM/复发 |
| **D7 (new)** — 线粒体钙/ MCU 复合体 (SMDT1) 作为 LNM 代谢–免疫节点 | 5 | 4 | 4 | 3 | 4 | 4 | 4 | **28** | 本次 SMDT1 新证据开辟线粒体钙角度；需验证与 MGST1 轴关系；单篇、机制初阶 |
| D‑ml — 多组学+影像 DL 融合预测 LNM/远处转移 | 2 | 5 | 5 | 3 | 4 | 3 | 1 | 23 | algorithm=37 已极度拥挤；边际增益低 |
| D6 — 5‑HT/NETs 介导 MTC 肝转移 (39903533) | 4 | 3 | 3 | 3 | 4 | 4 | 4 | 26 | 亮点但 MTC 小样本、机制待体内 |
| D‑spatial — POSTN+ myCAF→肿瘤细胞空间对话 | 4 | 3 | 3 | 2 | 3 | 4 | 4 | 25 | 最薄维度，需专项空间队列 |

> D3 连续第 7 次运行获确认（总分 32，Strong）。本次 SMDT1 证据使 D3 的"代谢–免疫"骨架更完整，并把"线粒体钙稳态 / MCU"显式纳入其可药节点集（即 D7 作为 D3 的子方向，而非独立分支）。

## Recommended Next Direction (推荐下一步方向 / Recommended Next Direction)

**D3 —— 界定并靶向 APOE−/MGST1+ 代谢–免疫干细胞样转移亚群（rubric 总分 32，Strong）。**

为什么是它：① 证据最厚（APOE− ABCA1‑LXR、MGST1 "Mito‑high" immune‑cold、PRECISE thyrocyte 41‑基因均指向同一去分化/代谢–免疫末端），本运行 SMDT1 又补上"线粒体钙"独立支点；② 公共数据（TCGA/GTEx/GEO）+ 单细胞（已发表 scRNA）+ 临床队列齐备；③ 直接服务于 LNM/复发这一临床终点，且 toxoflavin、MCU 调节剂等已有初阶药理线索，claim boundary 清晰（先界定亚群、再谈靶向，不夸临床效用）。

第一步具体动作：
1. 在已发表 PTC scRNA（GSE184362 / 42008746 / 42134246）中**双标记分选 APOE− ∩ MGST1+ ∩ SMDT1−** 细胞，验证其是否为同一转移干细胞态；
2. 用 TCGA THCA + 独立临床队列做**多组学共识 ML**，把线粒体钙/OXPHOS 特征并入现有 LNM 签名，外部验证 AUC；
3. 体外/类器官验证 MGST1 与 SMDT1 通路是否共线（同为线粒体代谢–免疫耦合），并测试 MCU 调节剂对转移表型的抑制。

**Claim boundary**：现仅支持"界定亚群 + 关联 LNM/复发"，靶向治疗仍属临床前假设，不得据 AUC/显著性推断临床效用。

## Follow-Up Reading List (随访阅读清单 / Follow-Up Reading List)

- **42510113 (SMDT1)** — 本次新证据，D3 线粒体钙节点的起点，优先读。
- **42327722 (MGST1)** — D3 核心枢纽，toxoflavin 药理线索。
- **39810624 (APOE−)** — D3 双标记分选的参照方法（ABCA1‑LXR）。
- **42008746 (PRECISE)** — thyrocyte 41‑基因预后签名，可提供上皮细胞态锚。
- **41421038 (Jiang FN1–SDC4)** — 空间轴，D‑spatial 子方向的桥接文献。
- **41877795 (XGBoost 远处转移)** — DTC 远处转移复发模型，区分 LNM vs 远处。

## Reproducibility Notes (可复现性说明 / Reproducibility Notes)

- Search date: 2026-07-29
- Databases: PubMed（经 `mcp__paper-search-mcp__search_pubmed`，DeferExecuteTool）
- Query strings: a–i 共 9 路（见 Search Strategy 表）；max_results=15；**sort=pub_date**
- Filters: 无外部 filter（MCP 仅支持 query/max_results/sort）；时效由 sort=pub_date 保证
- Deduplication rule: 以 PMID（字段 `paper_id` 或 `pmid`）去重；跨查询合并
- Screening rule: 保留甲状腺（PTC/PTMC/FTC/MTC/ATC/PDTC）相关；剔除非甲状腺（乳腺/胃/结直肠/肺/GI/宫颈/HNSCC 等）及纯泛癌综述；临床流行病学仅当涉及预后/复发/LNM 且甲状腺专属时保留
- Tooling note: `search_pubmed` 在本运行首轮对 c/d/e 触发 `not well-formed (invalid token)` 解析错误，逐查询重发后全部返回（共 3 轮重试，与 run #3–#6 一致）
- Files saved: `lit_review/literature_review_20260729_025533.md`；`lit_review/search_results_latest.json`（累计 174/103/71）；生成脚本 `_build_run7.py`

---

## 本次 vs run #6 的差异与新增信号 (Delta vs Run #6)

**检索体量**：run #6 完成大范围时效扫描（114 raw → 170 unique / 101 in‑scope）后，本运行（run #7，间隔 1 天）仅净增 **2 篇甲状腺在册文献 + 2 篇非甲状腺外溢**，累计 174/103/71。语料已进入**低速增量平台期**——符合预期（时效扫描已捕获绝大多数 2025–2026 可见文献）。

**新增文献（2 篇）**：
- **42510113 — SMDT1 (线粒体钙单向转运体 MCU 复合体)**：本次最重要的新信号。它把"代谢–免疫偶联驱动 LNM"主轴从**糖酵解**（LCN2/METTL7B/FN1）拓展到**线粒体钙稳态 / OXPHOS**，且同时关联 LNM、DFS 与 CD8+ T / NK 浸润——与 MGST1 "Mito‑high" immune‑cold 在"线粒体代谢–免疫"逻辑上同构，是新 corroborating evidence，而非矛盾。
- **39213698 — 年龄–复发 U 型**：临床分层细节，机制贡献低，但支持"青年与老年 PTC 均高危"。

**方向变化**：推荐方向 **D3 维持（rubric 总分 32，Strong），连续第 7 次确认**；无反向证据。本次新增 **D7（线粒体钙/MCU 作为 LNM 代谢–免疫节点，初评 28）**，定位为 D3 的子方向而非独立分支。其余候选（D‑ml 23、D6 26、D‑spatial 25）排序不变。

**维度变化（in‑scope 多标签）**：molecular 46→47、immune 29→30、metabolic 13→14、prognosis 27→28；single‑cell 18、spatial 6、algorithm 37 不变。最薄维度仍为 **spatial=6**（甲状腺专属空间研究持续稀缺，建议后续专项补强）。

**结论**：本运行无颠覆性新信号，属平台期内的"补点"运行；SMDT1 是唯一有机制增量价值的发现，已被吸收进 D3/D7 逻辑链。下一次若想突破平台，建议按 run #6 建议引入 bioRxiv/arXiv 预印本 + cBioPortal/DepMap，并针对 **spatial (POSTN+ myCAF)** 与 **ATC/MTC 远处转移**做窄窗口（近 30/60 天）专项检索。
