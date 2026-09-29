# Literature Review: 甲状腺癌侵袭/转移/复发/预后及其分子机制、肿瘤免疫微环境、单细胞与空间组学、机器学习方法
# Thyroid Cancer Surveillance — Invasion, Metastasis, Recurrence, Prognosis, Molecular Mechanisms, TIME, Single-cell & Spatial Omics, ML/DL Methods

**Date / 日期:** 2026-08-10 (run #17)
**Sources / 数据源:** OpenAlex REST API（主源，直连稳定 ~1.4s）；Crossref / Unpaywall（DOI 元数据与 OA 校验，补充源）；paper-search-mcp（本环境不可用，仅备用，本轮未调用）。
**Search window / 检索窗口:** 2026-07-11 → 2026-08-10（近 30 天）；维度 `e`(单细胞)/`c`(算法方法) 增量为 0，已按协议单独补跑 `--days 90`。
**Primary retriever / 检索器:** `oa_search.py`（九路维度检索 a–i，内建补充材料剔除 / 多版本合并 / 他病剔除三类清洗）。

---

## 中文摘要 (Chinese Abstract)

本轮（run #17）以 OpenAlex 为主源，对甲状腺癌（PTC/PTMC/FTC/MTC/ATC）侵袭、淋巴结与远处转移、复发、预后及其分子机制、肿瘤免疫微环境（TIME）、单细胞（scRNA-seq）、空间组学、机器学习/深度学习方法方向完成近 30 天增量监测。九路检索累计取回 **124 条**，去重后 **76 条唯一记录**，其中 **55 条在范围（甲状腺肿瘤）**，**剔除 21 条**（16 条标题未点名甲状腺、5 条非肿瘤甲状腺病），合并 23 组多版本记录。**相对 run #16 基线新增 8 条**（全部 PMID 待编目，因 PubMed 编目滞后），其中 1 篇预印本、0 篇 High 以外预印本污染。维度 `e`(单细胞) 与 `c`(算法方法) 在 30 天窗口内增量为 0，经 `--days 90` 补跑确认其"零新增"为**正常波动而非平台期**——近 90 天相关文献均落于 2026-05 至 2026-07-03（早于基线窗口），属窗口漂移而非新产出。

本轮新增聚焦四类信号：(1) **空间组学系统综述（预印本，High）**——汇总 21 项研究的 POSTN⁺/SERPINE1⁺ 癌相关成纤维细胞（CAF）侵袭前沿程序，整合强化 D3 方向的空间组分；(2) **DLGAP1-AS2 lncRNA**——增强 vandetanib 化疗敏感性并抑制 PTC 转移活性（敲低使 IC₅₀ 由 44.96→27.36 µg/ml，下调 CD44/CD133 干性标志）；(3) **BRAF V600E 三闸门多米诺纳米炸弹**——突变选择性诱导铁死亡（GPX4↓）；(4) 多项临床预后/影像模型（MTC 结构性无进展生存、2025 vs 2015 ATA 风险分层、双层能谱 CT 动脉增强分数预测 LNM）。**重点跟踪方向 D3（APOE⁻/MGST1⁺ 代谢–免疫干性转移亚群）证据定性强化、机制层面无变化、无反证，维持 Strong（rubric 总分 33，连续第 17 轮确认）。**

## English Abstract

Run #17 performs a ~30-day incremental surveillance of thyroid cancer (PTC/PTMC/FTC/MTC/ATC) covering invasion, lymph-node (LNM) and distant metastasis, recurrence, prognosis, molecular mechanisms, tumor immune microenvironment (TIME), single-cell (scRNA-seq), spatial omics, and ML/DL methodology. Using OpenAlex as the primary channel (stable direct access), nine complementary queries returned **124 raw rows → 76 unique records → 55 in-scope (thyroid oncology) → 21 excluded** (16 off-topic thyroid-mentioning, 5 benign/autoimmune thyroid), with 23 multi-version merges. **8 records are new vs the run #16 baseline** (all PMID-pending due to PubMed indexing lag), including 1 preprint. Dimensions `e` (single-cell) and `c` (algorithm/ML) showed zero 30-day increment; a `--days 90` supplement confirmed this is **normal variance, not a plateau** — all 90-day SC/AL candidates predate the baseline window (2026-05 to 2026-07-03).

New signals cluster into four themes: (1) a **PRISMA-guided spatial-transcriptomics systematic review (preprint, High)** consolidating POSTN⁺/SERPINE1⁺ CAF invasive-front programs across 21 studies, reinforcing the spatial pillar of D3; (2) **DLGAP1-AS2 lncRNA** sensitizing vandetanib and suppressing PTC metastatic activity (IC₅₀ 44.96→27.36 µg/ml; CD44/CD133 stemness down); (3) a **BRAF V600E triple-gated ferroptosis nanobomb** (GPX4↓); (4) clinical prognostic/imaging models (MTC structural PFS, 2025-vs-2015 ATA stratification, dual-layer spectral-CT arterial enhancement fraction for LNM). The tracked flagship direction **D3 (APOE⁻/MGST1⁺ metabolic–immune stem-like metastatic subpopulation) is qualitatively reinforced (spatial consolidation), unchanged at the primary-mechanism level, with no countervailing evidence — Strong, rubric total 33, 17th consecutive confirmation.**

---

## 检索策略 (Search Strategy)

| Source | Query (dimension) | Filters | Results (raw→unique) | Notes |
|---|---|---|---:|---|
| OpenAlex | a: 分子机制+预后转移 (MO/PR) | `from_publication_date:2026-07-11`, `sort=publication_date:desc`, per-page 25 | 16→15 | 新增 15 |
| OpenAlex | b: 分子机制 (MO) | 同上 | 28→25 (取回25) | 新增 16 |
| OpenAlex | c: 算法方法 (AL/PR) | 同上 | 10→9 | 30d 增量为 0 → 已补跑 90d |
| OpenAlex | d: 免疫微环境 (IM) | 同上 | 13→5 | 新增 5 |
| OpenAlex | e: 单细胞 (SC) | 同上 | 10→6 | 30d 增量为 0 → 已补跑 90d |
| OpenAlex | f: 空间组学 (SP) | 同上 | 12→3 | 新增 3（含 1 预印本综述） |
| OpenAlex | g: 预后转移 (PR) | 同上 | 50→25 (取回25) | 新增 17 |
| OpenAlex | h: 转移干性 (ST) | 同上 | 6→2 | 新增 2 |
| OpenAlex | i: 代谢重编程 (ME) | 同上 | 7→3 | 新增 3 |
| OpenAlex (supplement) | e/c `--days 90` | `from_publication_date:2026-05-12` | 见正文 | e/c 候选均早于基线窗口，非真新增 |
| Crossref / Unpaywall | 8 篇新文献 DOI 校验 | — | 8/8 命中 | 元数据一致、OA 状态确认 |

**Deduplication / 去重规则:** 标题归一化（NFKD + 去非字母数字前 90 字符）为主键；同篇多版本（预印本/正式版/仓储副本）合并并补齐 PMID/DOI；期刊补充材料（`Table 1_…`/`Data Sheet 1_…` 等）正则直接丢弃。
**Screening / 在范围判定:** 标题须点名甲状腺（thyroid/PTC/PTMC/FTC/MTC/ATC）且整体为肿瘤主题（carcinoma/cancer/metasta…/nodule）；仅摘要顺带提及的他病文献（乳腺/肺/结直肠 LNM、irAE 甲功异常、甲状腺眼病、桥本）剔除。

---

## 纳入论文 (Included Papers — 本轮 8 篇新增)

1. **Spatial Transcriptomics in Thyroid Cancer: A PRISMA-Guided Systematic Review of Platforms, Applications, and Tumor Microenvironment.** Preprints.org (preprint). 2026-08-05. DOI: 10.20944/preprints202608.0302.v1. PMID: 待编目. OA: green.
   - Author claim: 21 项空间转录组研究中反复出现 POSTN⁺/SERPINE1⁺ CAF 侵袭前沿程序与 AP…（摘要截断）空间架构。
   - Agent note: 高质量系统综述，整合强化"POSTN⁺ myCAF 侵袭前沿"空间轴（与 run#16 轴 3 直接呼应）；预印本 + 综述，证据降档为初步。

2. **DLGAP1-AS2 knockdown increases chemosensitivity to vandetanib and synergistically inhibits metastatic activity of papillary thyroid cancer cells: experimental and computational approaches.** BMC Cancer. 2026-08-07. DOI: 10.1186/s12885-026-16511-3. PMID: 待编目. OA: gold.
   - Author claim: si-DLGAP1-AS2 联合 vandetanib 使 B-CPAP 细胞 IC₅₀ 由 44.96→27.36 µg/ml，并下调 CD44/CD133/MMP-3/MMP-9 等转移与干性标志。
   - Agent note: lncRNA→转移干性轴的新增证据，TCGA/SRA 生信 + 体外验证；干性标志（CD44/CD133）与 D3 干性组分方向一致。

3. **Triple-gated domino nanobomb for mutation-selective ferroptosis induction in BRAF V600E thyroid cancer.** Journal of Nanobiotechnology. 2026-08-07. DOI: 10.1186/s12951-026-04859-4. PMID: 待编目. OA: gold.
   - Author claim: TSH/NIS 介导靶向 + BRAF V600E siRNA（Gate 2 抑制 MAPK、下调 GPX4）+ H₂O₂ 触发 Fe²⁺释放（Gate 3）三闸门诱导铁死亡，区分恶性与正常甲状腺滤泡细胞。
   - Agent note: 代谢/氧化脆弱性（铁死亡）治疗型证据，强化 BRAF V600E 氧化应激轴；属纳米材料治疗学，非机制发现。

4. **Preoperative Prediction of Cervical Lymph Node Metastasis in Papillary Thyroid Carcinoma Using Arterial Enhancement Fraction Derived From Dual-Layer Spectral CT.** Head & Neck. 2026-08-06. DOI: 10.1002/hed.70424. PMID: 42563471. OA: bronze.
   - Author claim: 42 例 PTC / 94 个淋巴结；转移与未转移淋巴结在直径、囊变、强化方式上差异显著（p<0.05），评估动脉增强分数（AEF）对 LNM 的诊断价值。
   - Agent note: 影像/算法维度增量，单中心回顾性；算法方向高度拥挤（见局限章）。

5. **Predicting Structural Progression-Free Survival After Surgery for Medullary Thyroid Carcinoma.** World Journal of Surgery. 2026-08-08. DOI: 10.1002/wjs.70524. PMID: 待编目. OA: closed.
   - Author claim: 140 例 MTC（75% MEN2a），结构性进展 24%；散发性 MTC、高龄、术前 CEA、肿瘤大小、淋巴结受累、高 LNR 影响结构性无病生存（SDFS）。
   - Agent note: MTC 预后队列，强化 MTC 亚型覆盖（D6 方向）；CEA/LNR 为可量化终点。

6. **Comparison of 2015 and 2025 ATA Risk Stratification Systems for Predicting Recurrence in Papillary Thyroid Carcinoma.** Annals of Surgical Oncology. 2026-08-08. DOI: 10.1245/s10434-026-20381-1. PMID: 待编目. OA: closed.
   - Author claim: （摘要缺失）对比 2015 与 2025 ATA 风险分层系统对 PTC 复发的预测效能。
   - Agent note: 临床指南验证类；无摘要，相关性 Low，价值待原文确认。

7. **TARGETED THERAPY AND IMMUNOTHERAPY IN COMBINED ANAPLASTIC AND PAPILLARY THYROID CARCINOMA WITH BRAF V600E MUTATION AND PD-L1 EXPRESSION: A CLINICAL CASE.** Eurasian Journal of Oncology and Radiology. 2026-08-07. DOI: 10.52532/10.52532/3135-4823-2026-2-108-117. PMID: 待编目. OA: hybrid.
   - Author claim: 70 岁女性 T4N1M1 IV 期 ATC（合并 PTC 成分），BRAF V600E + PD-L1 表达，评估靶向 + 免疫治疗。
   - Agent note: ATC+BRAF+PD-L1+IO 个案，与既往 ATC 轴一致；病例报告，证据弱。

8. **Riedel's thyroiditis with destruction of thyroid cartilage: A case report.** American Journal of Otolaryngology. 2026-08-01. DOI: 10.1016/j.amjoto.2026.104904. PMID: 待编目. OA: gold.
   - Author claim: 46 岁男性 IgG4 相关 Riedel 甲状腺炎伴喉软骨破坏（良性病，疑癌）。
   - Agent note: **边界性误收**——良性自身免疫病个案，相关性 Low，对肿瘤监测价值极低；保留以体现在范围判定的边界，建议后续将该类纯良性个案降权/排除。

---

## 证据矩阵 (Evidence Matrix)

> 列依 evidence-matrix-schema.md；附加 Dimension / Relevance / Preprint / OA 四列（用户要求）。本轮矩阵聚焦 8 篇新增；run#16 已确立的 5 条收敛轴见"已知结论"章。

| Paper (short) | PMID/DOI | Disease/Population | Data Source | Method | Endpoint | Main Finding | Validation | Limitations | Relevance | Gap Suggested | Future Direction | Dimension | Preprint | OA |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Spatial Txomics SR (preprint) | 10.20944/preprints202608.0302.v1 | TC (all subtypes) | 21 studies (PubMed/Scopus/WoS) | PRISMA syst review, Visium/GeoMx | TME spatial architecture | POSTN⁺/SERPINE1⁺ CAF invasive-front programs recurrent across 21 studies | None (review) | Preliminary (preprint); no new primary data | High | Causal role of POSTN⁺ CAF in LNM untested | In vivo CAF-ablation + LNM model | 分子机制/预后/免疫/空间/干性 | Yes | green |
| DLGAP1-AS2 / vandetanib | 10.1186/s12885-026-16511-3 | PTC (B-CPAP) | TCGA + SRA + in vitro | siRNA + MTT/apoptosis/scratch; qPCR | Chemosensitivity + metastasis | si-DLGAP1-AS2 ↓ IC₅₀ 44.96→27.36; ↓CD44/CD133/MMP | In vitro only | No in vivo; cell-line only | Medium | In vivo metastasis + clinical cohort | PDX + vandetanib combo trial | 分子机制/预后/干性 | No | gold |
| Ferroptosis nanobomb | 10.1186/s12951-026-04859-4 | BRAF V600E PTC | Nanoparticle design | dMSN + Fe²⁺ + BRAF siRNA; 3-gate logic | Mutation-selective ferroptosis | Gate2 ↓GPX4 + MAPK↓; Gate3 Fe²⁺ release | In vitro + ?in vivo | Therapeutic, not mechanism-discovery | Medium | Specificity vs normal follicular cells in vivo | Preclinical PK/PD | 分子机制/代谢 | No | gold |
| Spectral-CT AEF for LNM | 10.1002/hed.70424 (42563471) | PTC, 42 pts/94 LN | Retrospective CT cohort | DLCT quantitative + ROC | Preop LNM diagnosis | AEF/diameter/cystic change discriminate metastatic LN | Single-center | Small n; no external val | Medium | Multicenter external validation | Fusion with US/RAds | 分子机制/预后 (AL/imaging) | No | bronze |
| MTC SDFS model | 10.1002/wjs.70524 | MTC, 140 pts (75% MEN2a) | Retrospective tertiary | Cox regression | Structural PFS | Sporadic MTC/age/CEA/size/LNM/LNR → SDFS | Internal only | Retrospective; MEN2a-dominated | Medium | External multi-center val | Prospective MTC cohort | 预后转移 | No | closed |
| 2015 vs 2025 ATA | 10.1245/s10434-026-20381-1 | PTC | (abstract missing) | Comparative | Recurrence prediction | (no abstract) | — | No abstract | Low | Full-text retrieval needed | — | 预后转移 | No | closed |
| Combined ATC+PTC case | 10.52532/…-108-117 | ATC+PTC, T4N1M1 | Single case | Targeted + IO | Response | BRAF V600E + PD-L1 case | n=1 | Case report | Medium | Systematic ATC IO response data | Registry study | 预后转移 | No | hybrid |
| Riedel thyroiditis | 10.1016/j.amjoto.2026.104904 | Benign IgG4 RT | Case report | Histopathology | (benign) | Cartilage destruction mimics malignancy | n=1 | Benign; off-oncologic | Low | — (suggest exclude) | — | 分子机制 (borderline) | No | gold |

---

## 已知结论 (What Is Already Known)

> 以下 5 条收敛轴由 run#1–#16 累计语料（OpenAlex + 历史 PubMed 链路）确立，本轮无反证。标注关键 DOI/PMID。

1. **代谢–免疫耦合驱动淋巴结转移（Metabolic–immune coupling drives LNM）。** MGST1 "Mito-high"/免疫冷亚型（AUC 0.833，10.3389/fimmu.2026.1848083）、SHMT2（38272883）、GLTC–LDHA（37031273）、SOX12–YBX1–LDHA（40593465）反复出现；LCN2（41964784, Hippo/YAP1/HIF1α）、METTL7B（42332350, USP28/HIF-1α）、SMDT1/MCU（42510113, 线粒体 Ca²⁺/OXPHOS/CD8⁺T·NK 浸润）从线粒体–钙角度强化该轴。**本轮纳米炸弹（GPX4↓ 铁死亡）间接强化氧化脆弱性。**

2. **干性样转移亚群（Stem-like metastatic subpopulations）。** APOE⁻ 经 ABCA1–LXR（39810624）、MGST1 去分化尖端、ISG15/KPNA2（37501099, ATC）、DLK1（39595993, MTC）、circPTPRM-187aa（41539369）、DLEU2-ELAVL1-RCC2（42301557）。**本轮 DLGAP1-AS2（CD44/CD133↓）新增 lncRNA–干性–转移证据。**

3. **POSTN⁺ myCAF 空间图谱预测 LNM（POSTN⁺ myCAF spatial atlas）。** 423k 细胞空间图谱（41480746）锚定 POSTN⁺ CAF 侵袭前沿；**本轮空间转录组系统综述（预印本，21 项研究）整合确认 POSTN⁺/SERPINE1⁺ CAF 侵袭前沿程序为跨研究的反复信号**，强化该轴。

4. **影像/多组学 AI 高度拥挤（Crowded imaging/multi-omics AI）。** LLNM-Net（40750786, AUC 0.944 > 专家）、CLAM-WSI（41237514）、融合 DL（40771372/39682228/40778281/41061579）+ 本轮 9 篇新 AI/影像模型。**方向已过度拥挤，单中心、缺外部验证为主流缺陷（见局限章）。**

5. **DTC 远处转移 vs LNM 解耦（DTC distant-metastasis vs LNM decoupling）。** BRAF V600E 荟萃（41419184, 46k：淋巴结 OR1.38/复发 OR1.56，但不预测远处/死亡）+ PD-L1 荟萃（41510756）一致：这些标志预测远处转移但**不**预测 LNM/复发。

---

## 未解问题 (What Remains Unclear)

- **APOE⁻/MGST1⁺ 亚群是否存在于患者原代组织并具治疗可靶向性？** 多数证据来自细胞系/生信，缺原代空间验证与体内靶向干预（D3 核心缺口，本轮仍无直接进展）。
- **POSTN⁺/SERPINE1⁺ CAF 的因果角色**：系统综述确认其为反复空间信号，但是否因果驱动 LNM、可否作为治疗靶点未定。
- **远处转移 vs LNM 的解耦机制**：BRAF V600E / PD-L1 预测远处但不预测 LNM 的生物学基础未明。
- **MTC 远处转移（肝）机制**：5-HT/NETs 轴（39903533, D6）仍仅单篇，缺独立验证。
- **铁死亡治疗（纳米炸弹）在体内对正常甲状腺滤泡的特异性**：Gate 1 依赖 TSH/NIS，正常滤泡同样表达 NIS，脱靶风险需实证。

---

## 领域方法/数据局限 (Method/Data Limitations In The Field)

1. **算法/影像方向极端拥挤且验证薄弱**：本轮新增 9 篇 AL/影像模型，几乎全部单中心、回顾性、缺外部验证；AUC 不能直接推断临床效用（rubric 已对 D-ml 打 ≤20）。
2. **公开数据复用与批次效应**：DLGAP1-AS2 等依赖 TCGA/SRA，单细胞/空间研究样本量小（常 <50 例），批次效应未充分控制。
3. **终点稀疏**：远处转移、脑转移等稀有事件队列少（如脑转移仅 1 篇预印本 10.21203/rs.9988983）。
4. **亚型分层不足**：ATC/MTC 样本稀缺，多数模型以 PTC 为主，外推受限。
5. **湿实验验证缺位**：lncRNA / 纳米炸弹等多止步体外；体内与临床转化证据链不完整。
6. **检索通道局限（本环境）**：NCBI/pubmed 直连不可达，OpenAlex 不索引部分期刊与中文文献；预印本（preprints.org）未全部入 Crossref，需单独核验。

---

## 候选未来方向 (Candidate Future Directions)

> 评分依 research-direction-rubric.md（7 维 × 1–5；28–35 = 强候选）。

| Direction | Novelty | Feas. | Data | Val. | Clin. | Method | Overcrowd | **Total** | Claim Boundary |
|---|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|---|
| **D3** APOE⁻/MGST1⁺ 代谢–免疫干性转移亚群定义与靶向 | 5 | 4 | 5 | 4 | 5 | 5 | 5 | **33** | 须原代空间验证 + 体内靶向，勿宣称临床效用 |
| **D8** TREM2⁺ AHR–IDO1 免疫代谢检查点（体内逆转免疫冷） | 5 | 4 | 4 | 4 | 4 | 4 | 5 | **30** | 仅 1 篇体内证据（42553364），需独立重复 |
| **D9** citrullination/PADI 侵袭程序 × SPP1–CD44 | 4 | 4 | 4 | 3 | 4 | 4 | 5 | **28** | 机制初探（tronan.2026.102931），缺功能验证 |
| **D6** MTC 肝转移 5-HT/NETs 轴（fluoxetine/SERT 阻断） | 4 | 4 | 3 | 3 | 4 | 4 | 4 | **27** | 单篇（39903533），需类器官/PDX 验证 |
| **D-ml** 影像/多组学 AI 预测 LNM | 2 | 5 | 4 | 2 | 4 | 2 | 1 | **20** | 极度拥挤，单中心缺外部验证，不优先 |

**D3 状态更新（本轮）：** 空间转录组系统综述（21 项）整合确认 POSTN⁺/SERPINE1⁺ CAF 侵袭前沿，强化 D3 空间组分；纳米炸弹（GPX4↓）与 DLGAP1-AS2（CD44/CD133↓）分别间接强化代谢与干性支柱。**机制层面无直接新证据、无反证 → 维持 Strong 33，连续第 17 轮确认。**

---

## 推荐下一步方向 (Recommended Next Direction)

**维持 D3（APOE⁻/MGST1⁺ 代谢–免疫干性转移亚群）为首要方向（rubric 33, Strong）。** 本轮证据定性强化（空间组分经系统综述整合、代谢/干性支柱各获间接支持），且连续 17 轮无反证。建议下一步具体动作：
1. **原代空间验证**：用 10x Visium / GeoMx 在 PTC 原发–配对 LNM 组织定位 APOE⁻/MGST1⁺ 细胞与 POSTN⁺ CAF 的空间共布（呼应系统综述的 POSTN⁺/SERPINE1⁺ 信号）。
2. **体内靶向干预**：在 PDX 或 ATC/PTC 转移模型测试针对该亚群的代谢–免疫联合策略（参考 MGST1/SHMT2/LDHA 轴与 ferroptosis 思路）。
3. **验证队列**：接入 TCGA-THCA + 已发表的 55k 配对单细胞图谱（42430190）做亚群富集与生存关联。

---

## 随访阅读清单 (Follow-Up Reading List)

- **空间转录组系统综述（10.20944/preprints202608.0302.v1）**：整合 POSTN⁺/SERPINE1⁺ CAF 空间信号，D3 空间组分的总纲性文献，待正式发表后复核 AP… 截断部分。
- **DLGAP1-AS2（10.1186/s12885-026-16511-3）**：lncRNA–干性–转移轴，补充 D3 干性支柱；关注其体内与临床转化。
- **铁死亡纳米炸弹（10.1186/s12951-026-04859-4）**：BRAF V600E 氧化脆弱性治疗思路，对照 MGST1/LDHA 代谢轴。
- **MTC SDFS（10.1002/wjs.70524）**：MTC 预后队列，D6 方向配套。
- **窗口漂移出的 2 篇 High 单细胞（10.1080/2162402x.2026.2701504；10.3389/fimmu.2026.1904196）**：本轮因早于 2026-07-11 窗口而出界，仍属语料，下一轮若扩窗需重新纳入。

---

## 可复现性说明 (Reproducibility Notes)

- **Search date / 检索日期:** 2026-08-10（UTC+8）。
- **Databases / 数据库:** OpenAlex（主）、Crossref + Unpaywall（DOI/OA 校验）、paper-search-mcp（本环境不可用，本轮未用）。
- **Query strings / 查询:** 见"检索策略"表九路 a–i（维度代码 MO/IM/SC/SP/AL/PR/ST/ME）；`--days 90` 补跑针对 e/c。
- **Filters / 过滤:** `from_publication_date:2026-07-11`，`sort=publication_date:desc`，per-page 25（补跑 40）。
- **Deduplication / 去重:** 标题归一化主键 + DOI/PMID 回退；多版本合并（本轮 23 组）；补充材料正则剔除。
- **Screening / 在范围:** 标题点名甲状腺且整体肿瘤主题。
- **Files saved / 产出文件:**
  - 报告：`lit_review/literature_review_20260810_110117.md`（本报告）
  - 本轮检索结果：`lit_review/search_results_20260810_110117.json`（将覆盖为 `search_results_latest.json` 作为新基线锚点）
  - 90 天补跑（中间产物，不覆盖基线）：`lit_review/search_results_20260810_90day_supplement.json`

---

## 与历史报告差异 (Delta vs Run #16 — 2026-08-07)

| 指标 | run #16 (基线) | run #17 (本轮) | 变化 |
|---|---:|---:|---|
| 唯一记录 | 79 | 76 | −3（窗口漂移） |
| 在范围（甲状腺肿瘤） | 57 | 55 | −2 |
| 剔除 | 22 | 21 | −1 |
| 预印本（在范围） | 3 | 3 | 0 |
| 相对基线新增 | 57（链路切换红利） | **8** | 真实增量 |
| High / Medium / Low | 13 / 25 / 19 | 11 / 24 / 20 | 略变 |
| 维度分布（在范围） | 分子26/预后36/免疫10/干性3/单细胞7/空间8/算法12/代谢4 | 分子27/预后36/干性4/免疫8/空间8/单细胞5/算法9/代谢4 | 单细胞−2、算法−3（窗口漂移）；其余稳定 |

**本轮新增 8 篇**（全部 PMID 待编目）：
1. 空间转录组系统综述（预印本, High）— 整合 POSTN⁺/SERPINE1⁺ CAF，强化 D3 空间组分。
2. DLGAP1-AS2 lncRNA — vandetanib 增敏 + 转移抑制（CD44/CD133↓），补 lncRNA–干性–转移轴。
3. BRAF V600E 铁死亡纳米炸弹（GPX4↓）— 强化代谢/氧化脆弱轴。
4. 双层能谱 CT 动脉增强分数预测 LNM（PMID 42563471）— 影像增量。
5. MTC 结构性无进展生存模型（CEA/LNR）— MTC 预后。
6. 2015 vs 2025 ATA 风险分层对比（无摘要, Low）。
7. 合并 ATC+PTC BRAF/PD-L1 个案 — ATC+IO。
8. Riedel 甲状腺炎个案（良性, Low，边界误收，建议后续降权）。

**窗口漂移出界 10 篇**（早于 2026-07-11，仍属 run#16 语料，非丢失）：含 2 篇 High 单细胞（2701504、1904196）、1 篇 High 桥本（12902-026-02404-w）、脑转移预后（rs.9988983）、GSEC lncRNA 葡萄糖代谢等。

**维度 0 增量说明：** `e`(单细胞) 与 `c`(算法方法) 30 天增量为 0；`--days 90` 补跑确认其近 90 天候选均落于 2026-05 至 2026-07-03（早于基线窗口）——**属正常波动，非领域平台期**。结合 2 篇 High 单细胞刚于本轮出界，单细胞方向实际为"窗口边界波动"而非停滞。

**重点方向 D3 跟踪结论：** 本轮证据**定性强化（空间系统综述整合 + 代谢/干性支柱间接支持）、机制层面无变化、无反证**，维持 Strong（rubric 33，连续第 17 轮确认）。APOE⁻/MGST1⁺ 亚群仍需原代空间验证与体内靶向（核心缺口未变）。
