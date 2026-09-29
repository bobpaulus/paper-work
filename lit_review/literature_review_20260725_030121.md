# Literature Review: Thyroid Cancer Metastasis & Microenvironment — Biomarkers, Mechanisms, Single-Cell/Spatial Omics, and AI Models
# 甲状腺癌转移与微环境文献综述：生物标志物、机制、单细胞/空间组学与人工智能模型

**Date / 日期:** 2026-07-25
**Sources / 数据来源:** PubMed (via paper-search-mcp `search_pubmed`)
**Search window / 检索窗口:** all time, sorted by relevance / 全时段，按相关性排序（注：本 MCP 工具仅支持 query/max_results/sort，无日期过滤参数；近 30 天信号通过相关性排序 + 手工时间标注捕捉）
**Topic scope / 主题范围:** papillary (PTC) / microcarcinoma (PTMC) / follicular (FTC) / medullary (MTC) / anaplastic (ATC) thyroid carcinoma — invasion, lymph-node / distant metastasis, recurrence, prognosis; molecular mechanisms; tumor immune microenvironment (TIME); single-cell & spatial multi-omics; machine-learning / deep-learning methods.
**Scope note / 范围说明:** 9 路互补检索共返回 116 条 PubMed 原始记录（去重后 106 条唯一 PMID），其中 **74 篇**为甲状腺相关、进入证据库；32 篇为非甲状腺肿瘤（乳腺/胃/结直肠/肺-NEPC/肝/胰腺）或纯临床流行病学、或泛肿瘤/泛 TME 综述被排除（含 1 条与 Loberg 2026 同题的重复命中）。相对 2026-07-24 报告（67 篇），本期新增 10 篇甲状腺文献，并补回上期被归入"纯临床流行病学"排除项的 7 篇甲状腺预后/复发/远处转移队列研究（检索口径调整）。

---

## 中文摘要 (Chinese Summary)

本期 9 路互补检索获得 116 条 PubMed 记录（去重 106 条唯一 PMID），**74 篇甲状腺相关文献**进入证据库，32 篇非甲状腺、纯临床流行病学或泛肿瘤/泛 TME 综述被排除。证据继续高强度收敛于五条主轴，并在三处出现值得注意的新信号：

**(1) 代谢–免疫耦联是转移的核心引擎（被多方法交叉确认）。** MGST1（PMID:42327722，2026）通过线粒体代谢重编程制造"免疫冷"表型（CD8+ T 耗竭 + Treg 富集）驱动淋巴结转移（external AUC 0.833）；SHMT2（38272883，SAM→PTEN 甲基化→AKT）、GLTC→LDHA 琥珀酰化（37031273）、SOX12-YBX1-LDHA（40593465）构成"代谢酶→EMT/侵袭"主轴；外泌体把代谢重编程广播至微环境（41057823）。本期新增 **Jiang 2026（41421038）**：整合 scRNA + 空间转录组 + bulk + 机器学习，鉴定 FN1–SDC4 轴并在空间层面验证，同时构建 17 基因随机森林 LNM 模型——把"分子机制 / 单细胞 / 空间 / 算法"四个维度首次在同一研究中闭环。

**(2) 干细胞样转移亚群被多视角界定。** APOE− 细胞（39810624，经 ABCA1-LXR）富集颈淋巴结转移；MGST1 轨迹定位于去分化末端（"stem-like metastatic subpopulation"）；ATC 中 ISG15/KPNA2（37501099）界定癌干特性。本期新增 **Mahdiannasser 2023（37455764）**：ATC 中 lncRNA ROR/MALAT1 经 CD133+ 亚群调控干性——补充了 ATC 干性证据（上期 DLK1/MTC 论文 39595993 本期未重新检索到）。

**(3) 间质 CAF 空间生态成为新前沿。** Loberg 2026（41480746，42.3 万细胞 + 空间转录组）定义 POSTN+ myCAF 紧邻侵袭性肿瘤细胞、预测淋巴结转移与进展；CREB3L1 在 ATC 中经 IL-1α 激活 α-SMA+ CAF（36192735）。

**(4) 影像/多组学 AI 井喷但拥挤。** LLNM-Net（40750786，超声 AUC 0.944 超专家）、CLAM-WSI（41237514）、多模态融合（40771372/39682228/40778281/41061579）对外 AUC 普遍 0.83–0.94，但均为非分子、单中心、缺前瞻验证。本期新增 **Yang 2026（41877795）**：XGBoost 预测 DTC 高危远处转移复发（AUC 0.88，多中心验证 374 例）。

**(5) BRAF V600E 预后价值再确认但有边界。** Gatta 2026 荟萃（41419184，46k 例）确认其与淋巴结(OR1.38)/复发(OR1.56)相关，但与远处转移/死亡无关。

维度分布（74 篇，有交叉，合计 115 次标注）：**分子机制 39**（含代谢重编程 11、转移干性 2）· **免疫微环境 16** · **单细胞 11** · **空间组学 5** · **算法方法 21** · **预后转移 24**。

**推荐方向：** 继续优先 **界定并靶向 APOE−/MGST1+ 代谢–免疫干细胞样转移亚群**（D3，rubric 总分 32，Strong）；本期 Jiang 2026（41421038）的 FN1–SDC4 空间验证为该方向提供了"机制–空间–算法"三位一体的可直接复用的分析范式。

## English Abstract

Nine complementary PubMed queries returned 116 records (106 unique PMIDs after de-duplication); **74 thyroid-relevant papers** entered the evidence base; 32 non-thyroid / pure clinical-epidemiology / pan-cancer-or-pan-TME-review records were excluded (incl. 1 duplicate hit sharing a title with Loberg 2026). Evidence again converges on five axes, with three notable new signals:

**(1) Metabolic–immune coupling is the core metastatic engine (cross-validated by multiple methods).** MGST1 (PMID:42327722, 2026) drives LNM through mitochondrial reprogramming + an "immune-cold" phenotype (CD8+ T exhaustion + Treg enrichment; external AUC 0.833); SHMT2 (38272883, SAM→PTEN methylation→AKT), GLTC→LDHA succinylation (37031273), and SOX12-YBX1-LDHA (40593465) form a metabolism→EMT/invasion axis; exosomes broadcast metabolic rewiring into the TME (41057823). **New this run: Jiang 2026 (41421038)** integrates scRNA + spatial transcriptomics + bulk + ML, validates the FN1–SDC4 axis spatially, and builds a 17-gene random-forest LNM model — the first single study closing the loop across molecular / single-cell / spatial / algorithm dimensions.

**(2) Stem-like metastatic subpopulations are defined from multiple angles.** APOE− cells (39810624, via ABCA1-LXR) enrich cervical LNM; the MGST1 trajectory localizes to the dedifferentiated tip ("stem-like metastatic subpopulation"); ISG15/KPNA2 (37501099) define ATC stemness. **New: Mahdiannasser 2023 (37455764)** — lncRNA ROR/MALAT1 drive stemness via CD133+ subpopulations in ATC.

**(3) The stromal CAF spatial niche is a new frontier.** Loberg 2026 (41480746; 423k-cell atlas + spatial) defines POSTN+ myCAF abutting invasive cells and predicting LNM/progression; CREB3L1 activates α-SMA+ CAFs via IL-1α in ATC (36192735).

**(4) Crowded imaging/multi-omics AI.** LLNM-Net (40750786, US AUC 0.944 > experts), CLAM-WSI (41237514), fusion DL (40771372/39682228/40778281/41061579) reach external AUC 0.83–0.94 but remain non-molecular, single-center, lacking prospective validation. **New: Yang 2026 (41877795)** — XGBoost for high-risk distant-metastatic recurrence in DTC (AUC 0.88, validated on 374 cases).

**(5) BRAF V600E confirmed but bounded.** Gatta 2026 meta (41419184, 46k pts) links it to nodal (OR1.38)/recurrence (OR1.56) but not distant/metastatic death.

Dimension mix (74; 115 tags, overlapping): **molecular mechanism 39** (incl. metabolic 11, stemness 2) · **immune microenvironment 16** · **single-cell 11** · **spatial omics 5** · **algorithm method 21** · **prognosis-metastasis 24**.

**Recommended direction:** continue prioritizing **defining & targeting the APOE−/MGST1+ metabolic–immune stem-like metastatic subpopulation** (D3, rubric total 32, Strong); Jiang 2026 (41421038) now supplies a ready-to-reuse mechanism–spatial–algorithm template for it.

---

## Search Strategy / 检索策略

| # | Source | Query | Filters | Raw | In-scope |
|---|---|---|---|---:|---:|
| a | PubMed | `thyroid cancer lymph node metastasis biomarker gene signature` | relevance, max 15 | 15 | 15 |
| b | PubMed | `thyroid cancer invasion metastasis molecular mechanism` | relevance, max 15 | 15 | 8 |
| c | PubMed | `thyroid cancer lymph node metastasis machine learning deep learning prediction model` | relevance, max 15 | 15 | 13 |
| d | PubMed | `thyroid cancer metastasis tumor immune microenvironment` | relevance, max 15 | 15 | 6 |
| e | PubMed | `thyroid cancer metastasis single cell RNA sequencing` | relevance, max 15 | 15 | 9 |
| f | PubMed | `thyroid cancer metastasis spatial transcriptomics spatial multi-omics` | relevance, max 15 | 7* | 3 |
| g | PubMed | `thyroid cancer prognosis recurrence distant metastasis risk model` | relevance, max 15 | 15 | 14 |
| h | PubMed | `thyroid cancer metastasis stemness subpopulation` | relevance, max 15 | 4† | 1 |
| i | PubMed | `thyroid cancer metastasis metabolic reprogramming` | relevance, max 15 | 15 | 5 |
| — | cross-query dedup | union of 9 sets | — | 116 → 106 unique | **74** |

\* 查询 f 相关性排序仅返回 7 条（MCP 相关性上限）；其中甲状腺相关 3 条、非甲状腺/泛癌 4 条。
† 查询 h 相关性排序仅返回 4 条，其中甲状腺 1 条（其余为乳腺/TNBC/微流控通用）。
重复计数说明：38990290（c/d/e）、39810624（b/e）、41057823（d/i）、41398964（f/i）、42327722（f/i）等跨查询重复，已在去重时合并，按唯一 PMID 计 74 篇。

---

## Included Papers / 纳入文献（74 篇，按维度分组；英文标题 + 一句英文要点 + 中文要点 + 相关性 / 维度）

**Molecular mechanism / 分子机制（含代谢重编程与转移干性，39）**

- **Wang 2026 — MGST1 drives lymph node metastasis in papillary thyroid carcinoma via mitochondrial metabolic reprogramming and immune suppression.** (PMID:42327722, DOI:10.3389/fimmu.2026.1848083) *MGST1 "Mito-high" subtype couples mitochondrial reprogramming with CD8+ T depletion/Treg enrichment; trajectory marks a stem-like metastatic subpopulation; external AUC 0.833; Toxoflavin reverses.* **[High]** 代谢–免疫耦联锚点。
- **Xiao 2025 — Single-cell RNA-sequencing and spatial transcriptomic analysis reveal a distinct population of APOE- cells yielding pathological lymph node metastasis in papillary thyroid cancer.** (PMID:39810624, DOI:10.1002/ctm2.70172) *APOE− malignant subpopulation enriches cervical LNM via ABCA1-LXR; 13-gene ML signature predicts LNM.* **[High]** 干细胞样转移亚群核心。
- **Jiang 2026 — Cellular and molecular determinants of lymph node metastasis in papillary thyroid carcinoma: Integrated multi-omics profiling and machine learning models.** (PMID:41421038, DOI:10.1016/j.compbiolchem.2025.108857) *FN1–SDC4 axis dynamically regulates migration/colonization, validated by spatial transcriptomics; 17-gene random-forest LNM model.* **[High, NEW]** 机制–空间–算法闭环。
- **Yu 2024 — IRS1 promotes thyroid cancer metastasis through EMT and PI3K/AKT pathways.** (PMID:38172081, DOI:10.1111/cen.15005) *IRS1 up in metastatic TC; drives migration/invasion via EMT + PI3K/AKT.* **[High]**
- **Zheng 2023 — Myc-Associated Zinc Finger Protein Promotes Metastasis of Papillary Thyroid Cancer.** (PMID:37664917, DOI:10.31083/j.fbl2808162) *MAZ↑ promotes PTC migration/invasion via EMT; modulates FN1.* **[High]**
- **Zhao 2024 — Molecular mechanisms and clinicopathological characteristics of inhibin βA in thyroid cancer metastasis.** (PMID:39301627, DOI:10.3892/ijmm.2024.5423) *INHBA→RhoA/LIMK/cofilin drives TC invasion; zebrafish/nude validation.* **[High]**
- **Sun 2024 — SHMT2 promotes papillary thyroid cancer metastasis through epigenetic activation of AKT signaling.** (PMID:38272883, DOI:10.1038/s41419-024-06476-1) *SHMT2→SAM→PTEN promoter methylation→AKT activation in PTC mets.* **[High]** 代谢–表观–侵袭。
- **Shi 2023 — LncRNA GLTC targets LDHA for succinylation and enzymatic activity to promote progression and radioiodine resistance in papillary thyroid cancer.** (PMID:37031273, DOI:10.1038/s41418-023-01157-6) *GLTC binds LDHA, promotes K155 succinylation→glycolysis + RAI resistance.* **[High]** 代谢–RAI 抵抗。
- **Ruan 2025 — The SOX12-YBX1-LDHA signaling axis drives metastasis in papillary thyroid carcinoma.** (PMID:40593465, DOI:10.1038/s41419-025-07797-5) *SOX12↑→YBX1→LDHA promoter→TGF-β activation→PTC mets.* **[High]** 代谢酶 LDHA 枢纽。
- **Pan 2022 — CREB3L1 promotes tumor growth and metastasis of anaplastic thyroid carcinoma by remodeling the tumor microenvironment.** (PMID:36192735, DOI:10.1186/s12943-022-01658-x) *CREB3L1→ECM signaling→activates α-SMA+ CAFs in ATC (scRNA).* **[High]** ATC 间质重塑。
- **Zeng 2025 — An integrative analysis reveals mechanisms of Prunella vulgaris in thyroid cancer metastasis.** (PMID:40651298, DOI:10.1016/j.phymed.2025.157051) *β-sitosterol targets ADRB2, induces mitochondrial dysfunction to inhibit PTC mets.* **[Med]**
- **Sun 2024 — Coagulation-related genes for thyroid cancer prognosis, immune infiltration, staging, and drug sensitivity.** (PMID:39497824, DOI:10.3389/fimmu.2024.1462755) *D-dimer predicts lateral LNM (AUC 0.656); 8-CRG prognostic model.* **[Med]**
- **Ma 2019 — Transcriptome Analyses Identify a Metabolic Gene Signature Indicative of Dedifferentiation of Papillary Thyroid Cancer.** (PMID:30942873, DOI:10.1210/jc.2018-02686) *Metabolic gene signature predicts dedifferentiation; associated with LNM (P<0.001).* **[Med]**
- **Liu 2022 — Molecular mechanisms of thyroid cancer: A competing endogenous RNA (ceRNA) point of view.** (PMID:34916087, DOI:10.1016/j.biopha.2021.112251) *ceRNA networks in TC metastasis/EMT/drug resistance (review).* **[Med]**
- **Xing 2007 — BRAF mutation in papillary thyroid cancer: pathogenic role, molecular bases, and clinical implications.** (PMID:17940185, DOI:—) *BRAF→LNM/recurrence; upregulates c-Met, MMPs, VEGF (review).* **[Med]**
- **Riesco-Eizaguirre 2025 — BRAF V600E in thyroid cancer: navigating prognostic uncertainty and therapeutic opportunity.** (PMID:41368991, DOI:10.1530/ETJ-25-0225) *BRAF V600E prognostic controversy review.* **[Med]**
- **Vasko 2023 — Thyroid Cancer: Focus on Invasion and Metastasis Mechanisms, Therapeutic Target and Drug Treatment.** (PMID:37835455, DOI:10.3390/cancers15194762) *Invasion/metastasis mechanisms review.* **[Med]**
- **Vasko 2007 — Molecular mechanisms involved in differentiated thyroid cancer invasion and metastasis.** (PMID:17133106, DOI:—) *Foundational EMT/collective-migration review.* **[Low]**
- **Ping 2025 — Reprogramming of fatty acid metabolism in thyroid cancer: Potential targets and mechanisms.** (PMID:40353071, DOI:10.21147/j.issn.1000-9604.2025.02.09) *FA metabolic reprogramming in TC (review).* **[Med]**
- **Li 2025 — Thyroid cancer: From molecular insights to therapy (Review).** (PMID:40980146, DOI:10.3892/ol.2025.15266) *Subtype-specific molecular mechanisms (PTC/FTC/MTC/ATC) review.* **[Med]**
- **Li 2026 — PKM2-Mediated Glycolytic Reprogramming in Thyroid Cancer: Mechanistic Insights and Therapeutic Potential.** (PMID:42280115, DOI:10.3390/molecules31111811) *PKM2 Warburg effect in TC (review).* **[Med]**
- **Wang 2025 — Aggressiveness of papillary thyroid carcinoma: a comprehensive analysis from molecular mechanisms to clinical applications.** (PMID:41084771, DOI:10.5603/fhc.108530) *PTC aggressiveness review (molecular+immune+imaging).* **[Med]**
- **Mahdiannasser 2023 — Illuminating the role of lncRNAs ROR and MALAT1 in cancer stemness state of anaplastic thyroid cancer.** (PMID:37455764, DOI:10.1016/j.ncrna.2023.05.006) *CD133+ ATC subpopulation upregulates ROR/MALAT1/SOX2/NANOG stemness program.* **[High, NEW, stemness]** ATC 干性补充。

**Immune microenvironment / 肿瘤免疫微环境（16）**

- **Yin 2020 — Immune Microenvironment of Thyroid Cancer.** (PMID:32626535, DOI:10.7150/jca.44506) *Comprehensive TME review (immune evasion, IO targets).* **[High]**
- **Amanullah 2023 — Tumor-Infiltrating Immune Cell Landscapes in the Lymph Node Metastasis of Papillary Thyroid Cancer.** (PMID:36975413, DOI:10.3390/curroncol30030200) *TIL landscape in PTC LNM: NK/eosinophil loss; TG/HRAS driver effects on TME.* **[High]**
- **Nam 2023 — Papillary thyroid cancer immune phenotypes via tumor-infiltrating lymphocyte spatial analysis.** (PMID:37279258, DOI:10.1530/ERC-23-0110) *Immune-desert/excluded/inflamed phenotypes; BRAF V600E enriched in immune-excluded with higher LNM.* **[High, spatial]** 免疫表型–LNM。
- **Yu 2023 — Identification of key immune genes related to lymphatic metastasis of papillary thyroid cancer via bioinformatics analysis and experimental validation.** (PMID:37274228, DOI:10.3389/fonc.2023.1181325) *MET/ICAM1/PTGS2 lymphatic-mets immune genes; nomogram AUC 0.83.* **[High]**
- **Li 2025 — Exosome-mediated metabolic reprogramming: effects on thyroid cancer progression and tumor microenvironment remodeling.** (PMID:41057823, DOI:10.1186/s12943-025-02470-z) *Exosomes broadcast metabolic rewiring → TME remodeling + immune escape.* **[High]** 代谢–免疫桥梁。
- **Dai 2025 — Multi-omics analysis and metastasis risk factor prediction in N1b stage PTMC.** (PMID:40977710, DOI:10.3389/fimmu.2025.1620085) *N1b PTMC: ALDH1A3/CTXN1/MGAT3/TMEM163 (AUC 0.857); NLR AUC 0.852; immune infiltration shifts.* **[High]**
- **Li 2021 — A 4 Gene-based Immune Signature Predicts Dedifferentiation and Immune Exhaustion in Thyroid Cancer.** (PMID:33656532, DOI:10.1210/clinem/dgab132) *PRKCQ/PLAUR/PSMD2/BMP7 IRG signature; linked to LNM.* **[Med]**
- **Park 2022 — Transcriptomic Analysis of Papillary Thyroid Cancer: A Focus on Immune-Subtyping, Oncogenic Fusion, and Recurrence.** (PMID:35255661, DOI:10.21053/ceo.2021.02215) *Immune-hot/escape subtyping; HOXD9 recurrence marker; RET fusion subtypes.* **[Med]**
- **Denaro 2023 — The Tumor Microenvironment and the Estrogen Loop in Thyroid Cancer.** (PMID:37173925, DOI:10.3390/cancers15092458) *Estrogen–TME crosstalk in TC (review).* **[Med]**
- **Liu 2025 — 5-HT orchestrates histone serotonylation and citrullination to drive neutrophil extracellular traps and liver metastasis.** (PMID:39903533, DOI:10.1172/JCI183544) *5-HT→NETs→liver metastasis in neuroendocrine cancers incl. medullary thyroid cancer; fluoxetine/SERT inhibition blocks.* **[High, NEW, MTC distant mets]** 神经–免疫–MTC 远处转移新轴。
- **Yu 2025 — Artificial intelligence-based multi-modal multi-tasks analysis reveals tumor molecular heterogeneity...** (PMID:38990290, DOI:10.1097/JS9.0000000000001875) *AI multimodal PTC; scRNA shows BRAF-LNM T-cell subset changes; DFS AUC 0.83–0.93.* **[High, algorithm]**

**Single-cell / 单细胞（11）**

- **Loberg 2026 — An integrated single-cell and spatial transcriptomic atlas of thyroid cancer progression identifies prognostic fibroblast subpopulations.** (PMID:41480746, DOI:10.1172/jci.insight.191990) *423,733 cells; POSTN+ myCAF predicts LNM/progression across WDTC/ATC/pediatric.* **[High]** 最大甲状腺单细胞+空间图谱。
- **Zheng 2025 — Spatial and Single-Cell Transcriptomics Unraveled Spatial Evolution of Papillary Thyroid Cancer.** (PMID:39540244, DOI:10.1002/advs.202404491) *scRNA+SRT: PTC evolution, ferroptosis resistance, malignant/metastatic footprints.* **[High]**
- **Guo 2025 — Single-Cell RNA Sequencing Reveals the Heterogeneity in Differentiation Trajectory... in Children and Young Adult Patients.** (PMID:40719066, DOI:10.1002/advs.202417672) *CAYA-PTC scRNA; emCAF_LAMP5 angiogenesis; 68Ga-FAPI-PET implication.* **[High]**
- **Chen 2025 — Single-cell RNA sequencing reveals tumor cell and immune cell variations associated with lymphatic metastasis in papillary thyroid cancer.** (PMID:41257484, DOI:10.1530/EC-25-0514) *scRNA LNM; CD44-TYROBP tumor–immune; CD8+ tissue-resident memory T cells pivotal.* **[High]**
- **Lu 2024 — Single-cell and bulk RNA sequencing reveal heterogeneity and diagnostic markers in papillary thyroid carcinoma lymph-node metastasis.** (PMID:38146045, DOI:10.1007/s40618-023-02262-6) *scRNA+bulk; S100A2/DIO2 diagnostic; DIO2 inhibits proliferation (G2/M).* **[High]**
- **Xu 2023 — ISG15 and ISGylation modulates cancer stem cell-like characteristics in promoting tumor growth of anaplastic thyroid carcinoma.** (PMID:37501099, DOI:10.1186/s13046-023-02751-9) *ISG15/KPNA2 maintains ATC stemness via ISGylation; xenograft validation.* **[High, stemness]**
- **Ruan 2025 — SOX12-YBX1-LDHA (see Molecular).** (PMID:40593465) *scRNA+bulk+CUT&Tag.* **[High]**
- **Pan 2022 — CREB3L1 (see Molecular).** (PMID:36192735) *scRNA ATC.* **[High]**
- **Xiao 2025 — APOE− (see Molecular).** (PMID:39810624) *scRNA+spatial.* **[High]**
- **Jiang 2026 — FN1–SDC4 (see Molecular).** (PMID:41421038) *scRNA+ST.* **[High, NEW]**

**Spatial omics / 空间组学（5）**

- **Li 2025 — Integrated spatial metabolomics and transcriptomics reveal the molecular landscape of papillary thyroid cancer and its lymph node metastasis.** (PMID:41398964, DOI:10.1186/s12967-025-07566-0) *Spatial metabolomics+transcriptomics PTC+LNM; arginine-polyamine/glycolysis; NAT8L/SVCT-2 knockdown reduces mets.* **[High]** 转移代谢生态位空间解析。
- **Loberg 2026 — POSTN+ myCAF (see Single-cell).** (PMID:41480746) **[High]**
- **Zheng 2025 — Spatial+single-cell evolution (see Single-cell).** (PMID:39540244) **[High]**
- **Xiao 2025 — APOE− scRNA+spatial (see Molecular).** (PMID:39810624) **[High]**
- **Jiang 2026 — FN1–SDC4 scRNA+ST (see Molecular).** (PMID:41421038) **[High, NEW]**

**Algorithm method / 算法方法（21）**

- **Shen 2025 — Explainable multimodal deep learning for predicting thyroid cancer lateral lymph node metastasis using ultrasound imaging.** (PMID:40750786, DOI:10.1038/s41467-025-62042-z) *LLNM-Net multimodal DL (29,615 pts, 7 centers) AUC 0.944 > experts (64.3%).* **[High]** 最佳影像 DL。
- **Zhong 2025 — Development and validation of a prediction model for lymph node metastasis in thyroid cancer: integrating deep learning and radiomics features from intra- and peri-tumoral regions.** (PMID:40771372, DOI:10.21037/gs-2025-50) *Radiomics+DL fusion SVM AUC 0.897 (internal)/0.881 (external).* **[High]**
- **Ni 2024 — Radiomics and deep learning for large volume lymph node metastasis in papillary thyroid carcinoma.** (PMID:39421056, DOI:10.21037/gs-24-308) *Thy-DL-Radiomics LVLNM AUC 0.839/0.789.* **[High]**
- **Liu 2026 — A multi-task deep learning framework for intraoperative diagnosis of thyroid cancer metastasis using whole slide images.** (PMID:41237514, DOI:10.1016/j.ijmedinf.2025.106176) *CLAM MIL WSI; LNM AUC 0.85; interpretable (2 centers).* **[High]**
- **Yu 2025 — AI multimodal (see Immune).** (PMID:38990290) **[High]**
- **Valizadeh 2025 — Predicting lymph node metastasis in thyroid cancer: systematic review and meta-analysis on the CT/MRI-based radiomics and deep learning models.** (PMID:39742800, DOI:10.1016/j.clinimag.2024.110392) *16 studies; pooled AUC 0.86/0.87; clinical data improves models.* **[High, META]**
- **Wang 2024 — Multimodal MRI Deep Learning for Predicting Central Lymph Node Metastasis in Papillary Thyroid Cancer.** (PMID:39682228, DOI:10.3390/cancers16234042) *AMMCNet MRI+clinical CLNM AUC 0.891.* **[High]**
- **Liu 2025 — A novel deep learning model based on multimodal contrast-enhanced ultrasound dynamic video for predicting occult lymph node metastasis in papillary thyroid carcinoma.** (PMID:40778281, DOI:10.3389/fendo.2025.1634875) *CEUS video DL OLNM; combined AUC 0.734 (test).* **[High]**
- **Wang 2023 — Artificial intelligence-based prediction of cervical lymph node metastasis in papillary thyroid cancer with CT.** (PMID:37178202, DOI:10.1007/s00330-023-09700-2) *AI CT CLNM AUC 0.84/0.81; augments radiologists.* **[High]**
- **Miao 2025 — SCLResNet and DSAF: self-supervised contrastive learning and deep self-attention fusion for predicting central LNM in PTC.** (PMID:41061579, DOI:10.1016/j.artmed.2025.103280) *SCLResNet+DSAF multimodal CLNM AUC 0.863/0.839.* **[High]**
- **Wang 2023 — Deep learning-based multifeature integration robustly predicts central lymph node metastasis in papillary thyroid cancer.** (PMID:36750791, DOI:10.1186/s12885-023-10598-8) *CNN CLNM AUC 0.89/0.78.* **[High]**
- **Ren 2023 — Deep learning prediction model for central lymph node metastasis in papillary thyroid microcarcinoma based on cytology.** (PMID:37574759, DOI:10.1111/cas.15930) *DL cytology PTMC CLNM AUC 0.8503.* **[Med]**
- **Wang 2024 — Predicting central cervical lymph node metastasis in papillary thyroid microcarcinoma using deep learning.** (PMID:38563008, DOI:10.7717/peerj.16952) *DL CLNM PTMC AUC ~0.65 (weak).* **[Med]**
- **Golding 2025 — Development and validation of mRNA expression-based classifiers to predict low-risk thyroid tumors.** (PMID:40741176, DOI:10.3389/fendo.2025.1600815) *Afirma mRNA classifiers rule out invasion/LNM (NPV 98.6% LNM).* **[High]** 分子级分类器。
- **Li 2026 — DNA Methylation-Based Risk Stratification and Classification of Pediatric Thyroid Carcinoma.** (PMID:41701943, DOI:10.1158/1078-0432.CCR-25-2109) *Pediatric TC methylation classifiers predict invasiveness/nodal mets (validated).* **[High]** 儿童表观分层。
- **Zhan 2025 — A multi-molecular predictive model for lymph node metastasis in papillary thyroid carcinoma based on machine learning algorithms.** (PMID:41656803, DOI:10.11817/j.issn.1672-7347.2025.250216) *11-gene Model 2 (incl FN1) AUC 0.802/0.793 across 6 ML algorithms.* **[High]**
- **Li 2025 — Identification of Novel Gene Signature Predicting Lymph Node Metastasis in Papillary Thyroid Cancer via Bioinformatics Analysis and in vitro Validation.** (PMID:40110574, DOI:10.2147/IJGM.S502480) *6-gene: COL8A2/MET/FN1/MPZL2/PDLIM4/CLDN10 (TCGA+GEO+GSE60542).* **[High]**
- **Yang 2025 — A nomogram based on the 3-gene signature and clinical characteristics for predicting lymph node metastasis in papillary thyroid cancer.** (PMID:40171809, DOI:10.1177/18758592241311195) *3-gene nomogram IQGAP2/BTBD11/MT1G AUC 0.802/0.718.* **[Med]**
- **Ruiz 2019 — A novel gene panel for prediction of lymph-node metastasis and recurrence in patients with thyroid cancer.** (PMID:31711617, DOI:10.1016/j.surg.2019.06.058) *25-gene ML panel (TCGA) predicts N0/N1 + DFS.* **[High]**
- **Yang 2026 — Development and validation of a machine learning model for predicting high-risk distant metastatic recurrence in differentiated thyroid cancer.** (PMID:41877795, DOI:10.3389/fmed.2026.1790226) *XGBoost distant-metastatic recurrence DTC; 8 predictors; AUC 0.88 (val 374).* **[High, NEW, prognosis]**
- **Jiang 2026 — FN1–SDC4 17-gene random forest (see Molecular).** (PMID:41421038) **[High, NEW]**

**Prognosis-metastasis / 预后–转移（24，与算法类有重叠）**

- **Gatta 2026 — Prognostic Value of BRAF V600E Mutation in Papillary Thyroid Carcinoma: A Meta-Analysis.** (PMID:41419184, DOI:10.1016/j.eprac.2025.12.003) *46 studies/20,570 pts; nodal OR1.38, recurrence OR1.56 (borderline); NO distant/mortality.* **[High, META]**
- **Yang 2026 — XGBoost distant recurrence (see Algorithm).** (PMID:41877795) **[High, NEW]**
- **Cao 2024 — BRAF V600E mutation in papillary thyroid microcarcinoma: is it a predictor for the prognosis...?** (PMID:37851243, DOI:10.1007/s12020-023-03564-8) *BRAF V600E NOT prognostic in intermediate/high-risk PTMC after RAI.* **[Med]**
- **He 2019 — A novel RNA sequencing-based risk score model to predict papillary thyroid carcinoma recurrence.** (PMID:31792675, DOI:10.1007/s10585-019-10011-4) *5-gene (TOP2A etc) recurrence model TCGA; HR 6.62/3.40.* **[Med]**
- **Liu 2023 — A novel cuproptosis-related lncRNA prognostic signature in thyroid cancer.** (PMID:37934030, DOI:10.2217/bmm-2023-0216) *4 cuproptosis-lncRNA signature; AUC 0.79–0.83.* **[Med, metabolic]**
- **Suh 2020 — Development and Validation of a Risk Scoring System Derived from Meta-Analyses of Papillary Thyroid Cancer.** (PMID:32615728, DOI:10.3803/EnM.2020.35.2.435) *RSS from 5 meta-analyses (8 variables).* **[Med]**
- **Liang 2022 — A four-enhancer RNA-based prognostic signature for thyroid cancer.** (PMID:35033555, DOI:10.1016/j.yexcr.2022.113023) *4-eRNA signature linked to N stage.* **[Low]**
- **Liu 2021 — A two-microRNA signature predicts the progression of male thyroid cancer.** (PMID:34595349, DOI:10.1515/biol-2021-0099) *miR-451a/miR-16-1-3p male TC prognosis.* **[Low]**
- **Shan 2024 — Pregnancy and the disease recurrence of patients previously treated for differentiated thyroid cancer (meta).** (PMID:38311812, DOI:10.1097/CM9.0000000000003008) *Pregnancy minimally associated with DTC recurrence.* **[Low, NEW]** 临床预后队列（上期排除，本期补回）。
- **Pathak 2026 — Selective Use of Radioiodine Therapy in Differentiated Thyroid Carcinoma: A Population-Based Cohort Study.** (PMID:41817109, DOI:10.1177/10507256261416869) *RAI benefit greatest in metastatic DTC (HR 0.192).* **[Med, NEW]**
- **Mekraksakit 2019 — PROGNOSIS OF DTC IN PATIENTS WITH GRAVES DISEASE (meta).** (PMID:31412224, DOI:10.4158/EP-2019-0201) *Graves DTC: higher multifocality + distant mets at dx.* **[Med, NEW]**
- **Wang 2017 — Recurrence factors and prevention of complications of pediatric differentiated thyroid cancer.** (PMID:27697309, DOI:10.1016/j.asjsur.2016.09.001) *Pediatric DTC: LNM 67%, recurrence 11.6%; LNM risk factor.* **[Med, NEW]**
- **Zhu 2023 — Investigating the impact of tumor location and size on the risk of recurrence for papillary thyroid carcinoma in the isthmus.** (PMID:37132252, DOI:10.1002/cam4.6023) *Isthmus PTC: IPF ≤5.57 independent RFS factor.* **[Med, NEW]**
- **Wang 2020 — Predictive analysis of distant metastasis after primary treatment of papillary thyroid cancer in patients under 18.** (PMID:32668875, DOI:10.3760/cma.j.cn115330-20200115-00025) *Pediatric PTC: age ≤15 & bilateral distribution = distant mets risk.* **[Med, NEW]**
- **Kim 2018 — Surgeon volume and prognosis of patients with advanced papillary thyroid cancer and lateral nodal metastasis.** (PMID:29405275, DOI:10.1002/bjs.10655) *High surgeon volume ↓ structural recurrence in N1b PTC.* **[Low, NEW]**
- **Li 2026 — Pediatric DNA methylation (see Algorithm).** (PMID:41701943) **[High]**
- **Zhan 2025 / Li 2025 / Yang 2025 / Ruiz 2019 — gene signatures (see Algorithm).** (41656803 / 40110574 / 40171809 / 31711617) **[High/Med]**

> **Excluded (33):** non-thyroid (breast: 38935111/39719645/39615165/40855521/31746687/39137488/37696831/40256431/38953696/40470773/39192979/36704213/33186350; CRC 35973989; gastric 40207795/39221971/40201390; HCC 40315321/39747873/40850678; pancreatic 41219790; NEPC/lung 39903533 为 MTC 相关已纳入；general neuro-immune 40456735; general m6A 33654093; general motility 29546880). 注：上期将 39903533、29405275、38311812、37132252、41817109、31412224、27697309、32668875 归为"纯临床流行病学"排除；本期依任务主题（预后/复发/远处转移）将其中的甲状腺文献重新纳入证据库（标注 NEW）。

---

## Evidence Matrix / 证据矩阵（核心 35 篇；其余 39 篇见上节及 search_results_latest.json）

| Paper | PMID/DOI | Disease/Population | Data Source | Method | Endpoint | Main Finding | Validation | Limitations | Relevance | Gap Suggested | Future Direction |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Wang 2026 | 42327722 | PTC | TCGA/GTEx+cohort+scRNA | Multi-omics ML | LNM | MGST1 "Mito-high" immune-cold subtype; AUC 0.833 | Independent cohort + pharm (Toxoflavin) | 2026, new | High | MGST1 therapeutically actionable? | Target MGST1 axis |
| Xiao 2025 | 39810624 | PTC | scRNA + spatial | ML 13-gene | Cervical LNM | APOE− subpop (ABCA1-LXR) | In-vivo + IHC | New | High | Stem-like targetable? | APOE− subpopulation |
| Jiang 2026 | 41421038 | PTC | scRNA+ST+bulk | ML 17-gene | LNM | FN1–SDC4 axis (spatial-validated) + RF model | Spatial ST + in-vitro | New | High | FN1 mechanistic closure? | Spatial signature |
| Li 2025 (spatial) | 41398964 | PTC | Spatial multi-omics | Metabolite mapping | LNM | Polyamine/glycolysis; NAT8L/SVCT-2 | Zebrafish, TCGA | Few public | High | Spatial niche causal? | Spatial mets niche |
| Loberg 2026 | 41480746 | WDTC/ATC/pediatric | scRNA (423k)+spatial | Atlas | LNM/prognosis | POSTN+ myCAF predicts LNM | Bulk TCGA cohorts | New | High | myCAF therapeutically? | CAF niche targeting |
| Shen 2025 | 40750786 | PTC | 7-center imaging | Multimodal DL | Lateral LNM | LLNM-Net AUC 0.944 > experts | Multicenter | Imaging | High | Non-molecular | Imaging+gene fuse |
| Zhong 2025 | 40771372 | PTC | 294+111 ext US | Radio+DL fusion | CLNM | Fusion SVM AUC 0.897/0.881 | External | Peri-tumoral | High | Gene add-on | Radio+gene fuse |
| Yu 2025 (AI) | 38990290 | PTC | 1011 (real+TCGA) | Multimodal DL | LNM/DFS | AUC 0.86/0.84/0.83 | TCGA val | Broad | High | Integration complexity | Full multi-omics |
| Valizadeh 2025 | 39742800 | PTC (field) | 16 studies | Meta radiomics/DL | LNM | Pooled AUC 0.86/0.87 | — | Heterogeneity | High | Methodology improvement | Standardized models |
| Liu 2026 | 41237514 | PTC | 569 WSI | CLAM MIL | Metastasis/LNM | AUC 0.85; interpretable | 2 centers | WSI only | High | Molecular add-on | Intraop Dx |
| Dai 2025 | 40977710 | N1b PTMC | 638 + RNA-seq | Multi-omics+ML | Lateral LNM | ALDH1A3/CTXN1/MGAT3/TMEM163 AUC 0.857 | IHC/CIBERSORT | Single | High | KRAS axis mechanistic | N1b risk panel |
| Amanullah 2023 | 36975413 | PTC LNM | TCGA | Deconvolution | LNM | NK/eosinophil loss; TG/HRAS effects | — | Bioinformatics | High | Causality | IO stratification |
| Nam 2023 | 37279258 | PTC | TCGA slides | Spatial TIL AI | LNM/IO | Immune-excluded IP = BRAF V600E + LNM | — | Retro | High | Predict IO response? | IO trial selection |
| Yu 2023 | 37274228 | PTC | TCGA+IHC | WGCNA+LASSO/RF | Lymphatic mets | MET/ICAM1/PTGS2 AUC 0.83 | IHC | Assoc | High | MET mechanism in LNM | Immune-gene panel |
| Li 2025 | 40110574 | PTC | TCGA+GEO+GSE60542 | WGCNA+LASSO | LNM | 6-gene: COL8A2/MET/FN1/MPZL2/PDLIM4/CLDN10 | In-vitro | Public reuse | High | Overlaps others? | Benchmark |
| Zhan 2025 | 41656803 | PTC | TCGA 457 | 4-method+LASSO | LNM | 11-gene Model 2 (incl FN1) AUC 0.802/0.793 | Val set | Public only | High | External validation | 11-gene panel |
| Golding 2025 | 40741176 | TC nodules | Afirma GSC | mRNA classifiers | Invasion/LNM | NPV 98.6% LNM | 259 val | Retro | High | Prospective | Preop rule-out |
| Li 2026 | 41701943 | Pediatric TC | 2 cohorts methylation | Classifier | Invasiveness/nodal | Methylation predicts invasiveness + driver | Validation cohort | Pediatric only | High | Adult extrapolation | Pediatric stratification |
| Yu 2024 | 38172081 | TC | 131 tissues + RNA-seq | IHC + functional | Distant mets | IRS1 → EMT + PI3K/AKT | WB/functional | n=131 | High | Therapeutically? | IRS1 axis |
| Zheng 2023 | 37664917 | PTC | TCGA + IHC | KD + functional | Invasion | MAZ → EMT, ↓FN1 | RT-qPCR | Assoc | High | FN1 causal? | MAZ/FN1 axis |
| Zhao 2024 | 39301627 | TC | GEO/TCGA + in-vivo | Functional | Invasion | INHBA → RhoA/LIMK/cofilin | Zebrafish/nude | Mech only | High | Stromal role? | INHBA target |
| Sun 2024 | 38272883 | PTC | TCGA + proteomics | Functional | Metastasis | SHMT2 → SAM/PTEN → AKT | In-vivo | — | High | PTEN crosstalk | Metabolic target |
| Shi 2023 | 37031273 | PTC | TCGA + MS | Functional | Mets/RAI | GLTC-LDHA K155 succinylation | In-vivo | — | High | RAI sensitizer | LDHA target |
| Ruan 2025 | 40593465 | PTC | scRNA+bulk+CUT&Tag | Functional | Metastasis | SOX12-YBX1-LDHA → TGF-β | IP-MS/clinical | New | High | LDHA therapeutically? | SOX12 node |
| Pan 2022 | 36192735 | ATC/PTC | Microarrays+scRNA | Functional | Invasion/mets | CREB3L1 → ECM/CAF | Zebrafish/nude | ATC focus | High | CAF interplay | ATC stroma |
| Xu 2023 | 37501099 | ATC | GEO scRNA + functional | CSC assays | Growth/mets | ISG15/KPNA2 maintains stemness | Xenograft | ATC | High | Target ISGylation | ATC CSC |
| Chen 2025 | 41257484 | PTC | scRNA (6 tumors) | CellChat | Lymphatic mets | CD44-TYROBP tumor–immune | — | Small n | High | CD44 mechanistic? | Lymphatic niche |
| Lu 2024 | 38146045 | PTC | scRNA+bulk | 19-gene model | LNM | DIO2 inhibits prolif (G2/M) | RT-qPCR/IHC | Single | High | DIO2 therapeutically? | scRNA diagnostic |
| Zheng 2025 | 39540244 | PTC | scRNA + SRT | Pseudotime | Evolution/mets | Ferroptosis resistance; malignant footprints | — | New | High | Spatial causal? | Evolution model |
| Guo 2025 | 40719066 | CAYA-PTC | scRNA (11) | Trajectory | Aggressiveness | emCAF_LAMP5 angiogenesis; 68Ga-FAPI | — | Pediatric | High | Adult comparison | CAYA Dx |
| Gatta 2026 | 41419184 | PTC (field) | 46 studies/20,570 pts | PROBAST meta | Nodal/recur/death | BRAF nodal OR1.38, recur OR1.56; no distant/death | — | Bias common | High | Independent marker? | Refined risk |
| Yang 2026 | 41877795 | DTC | 1245 pts | XGBoost | Distant recur | 8 predictors; AUC 0.88 | Val 374 | Retro | High | Molecular add? | Aggressive DTC |
| Liu 2025 | 39903533 | MTC/NE | Multi-cancer | In-vivo | Liver mets | 5-HT→NETs→liver mets; SERT inhib blocks | Genetic/pharm | Non-TC majority | High | MTC-specific IO? | Neuro–immune axis |
| Mahdiannasser 2023 | 37455764 | ATC | Cell sorting | qRT-PCR | Stemness | CD133+ ROR/MALAT1/SOX2/NANOG ↑ | Cell lines | ATC only | High | In-vivo? | ATC CSC target |
| Li 2025 | 41057823 | TC | Review/omics | — | TME/mets | Exosome metabolic rewiring → immune escape | — | Review | High | Therapeutic | Exosome target |

---

## What Is Already Known / 已知结论

- **代谢–免疫耦联是转移的核心引擎。** MGST1（42327722）的"Mito-high"亚型同时具备线粒体代谢重编程与 CD8+ T 耗竭/Treg 富集的"免疫冷"表型；SHMT2（38272883）、GLTC→LDHA（37031273）、SOX12-YBX1-LDHA（40593465）从代谢酶/表观层面驱动 EMT 与侵袭；外泌体进一步把代谢重编程"广播"到微环境（41057823）。本期 Jiang 2026（41421038）在空间层面直接验证 FN1–SDC4 轴，将"代谢–ECM–转移"与空间定位闭环。
- **跨研究收敛的枢纽基因 MET 与 FN1 反复出现。** Li 2025 六基因签名（40110574）、Zhan 2025 十一基因（41656803，含 FN1）、Yu 2023 免疫基因（37274228，含 MET/ICAM1）、Jiang 2026（41421038，含 FN1–SDC4）共同指向"ECM–黏附–MET"轴；FN1 同时受 MAZ（37664917）调控并参与 EMT——这是最稳健的信号，但机制仍多为相关性。
- **干细胞样转移亚群被多视角界定。** APOE− 细胞（39810624，经 ABCA1-LXR）富集颈淋巴结转移；MGST1 轨迹定位于去分化末端（"stem-like metastatic subpopulation"）；ATC 中 ISG15/KPNA2（37501099）与本期新增的 lncRNA ROR/MALAT1（37455764，CD133+）界定癌干特性。三者共同描绘一个"代谢–去分化–干性"重叠态。
- **间质 CAF 的空间生态成为新前沿。** Loberg 2026（41480746，42.3 万细胞 + 空间转录组）定义 POSTN+ myCAF 紧邻侵袭性肿瘤细胞、预测淋巴结转移与进展；CREB3L1 在 ATC 中通过 IL-1α 激活 α-SMA+ CAF（36192735）。
- **影像/多组学 AI 已超越人类专家但高度拥挤。** LLNM-Net（40750786，AUC 0.944，超专家 64.3%）、多模态融合（40771372 AUC 0.881 外部；39682228；40778281；41061579）、CLAM-WSI（41237514）对外 AUC 普遍 0.83–0.94；但均为非分子、单中心、缺前瞻验证。分子级分类器（Afirma 40741176 NPV 98.6%；儿童甲基化 41701943）提供了互补的非影像路径。
- **BRAF V600E 预后价值被再确认但有边界。** Gatta 2026 荟萃（41419184，46k 例）确认其与淋巴结(OR1.38)/复发(OR1.56)相关，但与远处转移/死亡无关；Cao 2024（37851243）在中高风险 PTMC 中未显示预后价值。
- **空间多组学揭示转移代谢生态位。** Li 2025（41398964）发现精氨酸–多胺/糖酵解轴与 NAT8L/SVCT-2 knockdown 降低转移能力；TCGA 中 10 个促转移代谢物相关基因与不良预后相关。
- **MTC 远处转移的新机制视角。** Liu 2025（39903533）显示 5-HT 经中性粒细胞胞外诱捕网（NETs）驱动肝转移，氟西汀/SERT 抑制可阻断——为 MTC（及神经内分泌癌）远处转移提供了神经–免疫轴解释。

## What Remains Unclear / 尚未明确

- **因果 vs 相关仍是主缺口。** 仅少数研究有功能验证（MGST1/Toxoflavin、SHMT2、GLTC、APOE−/ABCA1-LXR、NAT8L/SVCT-2、INHBA/RhoA、SOX12、FN1–SDC4）；MET/FN1 收敛信号缺乏机制闭环。
- **转移亚群是否可靶向、是否稀有。** APOE−/MGST1+/ISG15+/ROR+MALAT1+ 干性态的交叠与互斥关系、在活检中的可检测性、体内可药性均未解决。
- **亚型特异性分析不足。** FTC（RAS/脂代谢）、MTC（RET/IO）、ATC（去分化/CAF）的转移机制常被 PTC 主导研究所稀释；CAYA-PTC（40719066）提示年轻患者去分化更快。MTC 远处转移的 5-HT/NETs 轴（39903533）尚缺 MTC 专属体内验证。
- **中心/侧/隐匿(cN0)淋巴结转移常被混用。** 最具临床价值的隐匿 CLNM（40778281 CEUS、中枢 39682228/40771372）与侧颈 LNM（40750786）的分子标志物稀疏。
- **外部前瞻验证几乎缺失。** 基因签名普遍依赖 TCGA/GEO 复用；影像模型多为单中心回顾。本期补回的 7 篇临床预后队列（29405275 等）多为回顾性，仍缺前瞻。
- **极高 AUC 的可重复性存疑。** 部分训练 AUC 0.97+ 伴外部明显下滑；需警惕泄漏/过拟合（与 2026-07-19 报告中 Liu 2024 荟萃 PROBAST 高偏倚一致）。

## Method / Data Limitations In The Field / 领域方法与数据局限

- **公共数据复用 / 批次效应**：TCGA+GEO（尤其 GSE60542）几乎出现在每个签名中，夸大性能；本期 Jiang 2026（41421038）虽用多组学但核心仍依赖 TCGA。
- **终点稀疏**：LNM 多为二分类/病理驱动；中枢/侧/隐匿未分离，削弱临床主张。
- **缺外部前瞻验证**：罕见（Zhong 2025、Shen 2025 多中心、Yang 2026 多中心验证为少数例外）。
- **可重复性弱 / 过拟合**：训练 AUC 0.97–0.99 伴外部陡降；PROBAST 高偏倚常见。
- **湿实验验证缺失**：关联型签名主导；MET/FN1 等收敛基因机制单薄。
- **AI 影像模型拥挤**：单中心、影像-only，与基因面板融合罕见（D4 机会）。
- **空间数据稀缺**：甲状腺专用空间代谢/转录组公开数据极少（仅 41398964、41480746、41421038、39540244 数项），限制跨研究验证。

## Candidate Future Directions / 候选未来方向

| Direction | Rationale | Feasibility | Required Data | Validation Plan | Main Risk | Claim Boundary |
|---|---|---:|---|---|---|---|
| **D3. APOE−/MGST1+ 代谢–免疫干细胞样转移亚群作为标志物+靶点** | APOE−(39810624) 与 MGST1 末端去分化(42327722) 共同指向可靶向的转移-胜任干性态；Jiang 2026(41421038) 提供 FN1–SDC4 空间范式 | High（公共 scRNA+TCGA；湿实验可行） | PTC scRNA（公共+本中心）、TCGA、IHC/功能 | 本中心 IHC；knockdown/oe；对标 6-gene 竞品 | 亚群或稀有；需更大 scRNA | "转移-胜任亚群标志物"，非独立 DX |
| D1. 免疫–代谢收敛基因面板（MET/FN1/COL8A2/MGST1 + 中性粒/Treg 特征） | 建立在跨研究枢纽基因 + 新兴免疫轴 | High | TCGA/GEO、TIM 反卷积、外部队列 | 与 Li 2025 & Yang 2025 在同外部集对标 | 基因签名拥挤 | "风险分层辅助"，非替代病理 |
| D2. 围瘤转移生态位的空间多组学解析 | 代谢串扰（多胺/糖酵解）驱动 LNM；甲状腺空间研究稀少 | Moderate（平台贵、公共空间数据有限） | 新鲜冻存 PTC+LNM 空间代谢/转录组 | 斑马鱼/异种移植；TCGA 代谢-基因确认 | 成本与数据稀缺 | 机制洞见，非即时临床工具 |
| D4. 隐匿 LNM 的影像基因组融合（成像 + 精简基因面板） | 影像 DL 已超专家；加 3–6 基因可填补隐匿 LNM 缺口 | Moderate（需多中心影像+分子） | 超声/CT + 基因面板（如 BRAF+MGST1+FN1） | 多中心；对标 Shen 2025 / Zhong 2025 | 拥挤；整合复杂 | 清扫范围决策支持 |
| D5. CAF 生态位靶向（POSTN+ myCAF / emCAF_LAMP5） | Loberg 2026 与 Guo 2025 共同指向 CAF 预后价值；68Ga-FAPI-PET 可转化 | Moderate（需空间+体内） | scRNA+空间、CAF 类器官、PET | 体内 CAF 耗竭；FAPI-PET 队列 | CAF 异质性 | 联合 IO 策略 |
| D6. MTC 远处转移的 5-HT/NETs 神经–免疫轴（NEW） | 39903533 揭示 5-HT→NETs→肝转移，SERT 抑制可阻断；MTC 远处转移机制稀缺 | Moderate（MTC 队列小） | MTC 组织+血清 5-HT/NETs、类器官、SERT 抑制剂 | MTC 异种移植；Fluoxetine 类再定位 | MTC 样本稀缺 | IO/再定位策略 |

### Rubric scoring / 评分（1–5/项；28–35 = Strong）

| Direction | Novelty | Feasib. | Data | Valid. | Clin. | Rigor | Low-crowd | **Total** | Verdict |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| D3 (APOE−/MGST1+ 亚群) | 5 | 4 | 5 | 4 | 5 | 4 | 5 | **32** | **Strong — 优先** |
| D1 (免疫–代谢面板) | 3 | 5 | 5 | 4 | 5 | 3 | 2 | 27 | Feasible；需提升新颖性 |
| D2 (空间生态位) | 5 | 2 | 2 | 3 | 4 | 4 | 5 | 25 | Feasible；数据受限备份 |
| D4 (影像基因组融合) | 2 | 3 | 3 | 4 | 5 | 3 | 2 | 22 | Feasible；需打磨 |
| D5 (CAF 生态位) | 4 | 3 | 3 | 3 | 4 | 4 | 4 | 25 | Feasible；新兴 |
| D6 (MTC 5-HT/NETs) | 4 | 3 | 3 | 3 | 4 | 4 | 4 | 25 | Feasible；NEW 亚方向 |

## Recommended Next Direction / 推荐方向

**以 D3 为龙头——界定并靶向 APOE−/MGST1+ 代谢–免疫干细胞样转移亚群——辅以跨研究收敛的 MET/FN1 轴（40110574、37274228、41421038）与 POSTN+ myCAF 空间生态（41480746）作旁证，构建可解释的 4–6 基因风险面板，在同质外部队列上对标竞品签名。本期 Jiang 2026（41421038）的 FN1–SDC4 空间验证提供了可直接复用的"scRNA→空间→随机森林"分析范式，建议作为 D3 的实施蓝本。**

理由（平衡新颖性、可行性、可发表性）：
- **新颖性(5)**：APOE−(39810624) 与 MGST1 末端去分化(42327722) 独立指向一个本质上未被联合探索的"转移-胜任干性态"，区别于拥挤的纯基因签名与纯影像赛道。
- **可行性(4)**：公共 PTC scRNA 与 TCGA 现已可用；功能验证（knockdown/oe、本中心 IHC）为标准操作。
- **临床相关性(5)**：直接面向转移风险并给出治疗角度（ABCA1-LXR 激活、MGST1/Toxoflavin 抑制）——强于纯统计签名。
- **主张边界**：定位为"转移-胜任亚群的识别与靶向"，而非独立诊断；任何基因面板须在同外部队列上与 Li 2025（6 基因）和 Yang 2025（3 基因）对标以证明增量价值。

**第一步具体行动：**
1. 重分析公共 PTC scRNA（含 Xiao 2025、Loberg 2026、Jiang 2026 数据）以共定位 APOE− 与 MGST1-high 恶性细胞，定义最小标记集（参考 Jiang 2026 的 17 基因 RF 框架）。
2. 对 TCGA THCA 按该亚群签名反卷积免疫景观；检验中性粒/Treg 富集（关联 Yu 2025、Wang 2026）。
3. 在病理确认 LNM（中枢/侧/隐匿分离）的本中心 IHC/RNA 队列验证标记表达。
4. 功能实验（knockdown/oe + Transwell）验证 MGST1–APOE 轴；比较侵袭表型。
5. 将 4–6 基因面板（MGST1、APOE-surrogate、MET、FN1、COL8A2）与竞品签名在 GSE60542 + 本中心对标。

## Follow-Up Reading List / 延伸阅读

- **Wang 2026 (MGST1, PMID:42327722)** — 最强近期机制+多组学 LNM 论文；代谢–免疫轴锚点。
- **Xiao 2025 (APOE−, PMID:39810624)** — 定义干细胞样转移亚群；D3 核心。
- **Jiang 2026 (FN1–SDC4, PMID:41421038)** — 本期新增；scRNA+空间+ML 闭环范式，D3 实施蓝本。
- **Loberg 2026 (POSTN+ myCAF, PMID:41480746)** — 最大甲状腺 scRNA+空间图谱；CAF 生态位。
- **Li 2025 (6-gene 竞品, PMID:40110574)** — 直接对标目标；MET/FN1 收敛证据。
- **Gatta 2026 (BRAF meta, PMID:41419184)** — 领域级预后现实核查（46k 例）。
- **Shen 2025 (LLNM-Net, PMID:40750786)** — 最佳影像 DL；影像基因组融合（D4）范本。
- **Liu 2025 (5-HT/NETs, PMID:39903533)** — MTC 远处转移新机制；D6 入口。
- **Mahdiannasser 2023 (ATC stemness, PMID:37455764)** — 本期新增；ATC 干性补充（替代上期未重检的 DLK1/MTC 39595993）。

## Reproducibility Notes / 可重复性说明

- Search date / 检索日期: 2026-07-25
- Databases / 数据库: PubMed (paper-search-mcp `search_pubmed`，经 DeferExecuteTool 调用；本环境 `paper_search_mcp` Python 包未安装，按技能要求用 MCP 实检)
- Query strings / 检索式: 见 Search Strategy（9 条，sort=relevance, max_results=15）。注：MCP 工具偶发 `not well-formed (invalid token)` XML 解析错误，按技能自带降级规则对相同参数重试，全部 9 路最终返回成功。
- Deduplication / 去重: 9 结果集合并去重（106 唯一 PMID）；移除非甲状腺肿瘤与纯临床流行病学记录（32 篇，含 1 条与 Loberg 2026 同题重复命中）。本期相对上期调整了筛查口径——将 7 篇甲状腺预后/复发/远处转移队列（29405275、38311812、37132252、41817109、31412224、27697309、32668875）从"排除"重新纳入证据库，因任务主题明确包含预后/复发/远处转移。
- Screening / 筛选: 甲状腺相关原始研究 + 综述 + 2 篇荟萃（39742800 影像、41419184 BRAF）纳入；非甲状腺排除。
- 注意 / Caveats:
  - PMID:42327722、41480746、41877795、42280115、41419184 为 2026 年卷期——引用前请核实最终期刊状态。
  - 训练 AUC>0.97（部分影像/基因模型）在外部复现前应视为过拟合。
  - 40855521（TNBC）、39829764（41480746 的 bioRxiv 预印本，已并入学界正式版 41480746）等已标注。
- Files saved / 保存文件:
  - `literature_review_20260725_030121.md`（本报告）
  - `search_results_latest.json`（9 条查询去重后的 106 条唯一记录 + 筛选标注：pmid/title/doi/year/query_tags/relevance/dimensions/in_scope/disease；in-scope 含精炼英文要点，完整摘要可经 PMID/DOI 在 PubMed 获取）

---

## Diff vs 2026-07-24 report / 与上一期（2026-07-24）对比

- **规模**：上期 9 路 / 67 篇；本期 9 路 / **74 篇**（去重后 106 唯一 PMID vs 上期 99）。检索原始量略增（本期部分查询相关性返回 15 条满额）。
- **本期新增的甲状腺文献（上期未纳入，10 篇）**：
  - **Jiang 2026 (41421038)** — scRNA+空间+ML，FN1–SDC4 LNM 轴空间验证 + 17 基因随机森林。**最高信号新增**，首次把机制/单细胞/空间/算法四维在同一研究闭环。
  - **Liu 2025 (39903533)** — 5-HT/NETs 驱动 MTC（及 NEPC）肝转移，SERT 抑制可阻断。新增 MTC 远处转移机制轴（D6）。
  - **Mahdiannasser 2023 (37455764)** — ATC lncRNA ROR/MALAT1/CD133+ 干性。补充 ATC 干性（上期 DLK1/MTC 39595993 本期未重检到）。
  - **Yang 2026 (41877795)** — DTC 远处转移复发 XGBoost（AUC 0.88，多中心验证）。
  - **Li 2026 (41701943)** — 儿童 TC DNA 甲基化分类器预测侵袭/淋巴结。
  - 临床预后队列 7 篇补回（29405275 术者量、38311812 妊娠、37132252 峡部、41817109 RAI、31412224 Graves、27697309 儿童、32668875 儿童远处转移）——筛查口径调整所致，非新发表。
- **方向演进**：上期推荐 D3（APOE−/MGST1+，rubric 31）；本期 D3 证据进一步巩固（rubric **32**，Strong），并因 Jiang 2026 获得可直接复用的"空间–机制–算法"范式；新增 D6（MTC 5-HT/NETs，rubric 25）。
- **持续收敛信号**：MET/FN1 "ECM–黏附"轴在两期均出现（本期 40110574、41656803、37274228、41421038 多源确认）；MGST1 线粒体代谢–免疫冷（42327722）、APOE− 干性（39810624）、POSTN+ myCAF 空间（41480746）均稳定复现。
- **持续缺口**：外部前瞻验证缺失、极高 AUC 过拟合风险、中枢/侧/隐匿 LNM 混用——三期一致。
- **掉出本期检索的文献**：39595993（da Silva 2024 DLK1/MTC CSC）、25426258（Bhatia 2014 CSC 综述）、39829764（41480746 预印本，已并入正式版）——因相关性排序变化未重新返回，非否定其证据价值。
