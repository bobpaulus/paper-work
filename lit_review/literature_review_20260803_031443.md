# Literature Review: 甲状腺癌侵袭/转移/复发/预后 与 分子机制·免疫微环境·单细胞·空间组学·AI 方法

Date: 2026-08-03  
Sources: PubMed (via paper-search-mcp `search_pubmed`, DeferExecuteTool)  
Search window: all time (sort=relevance; MCP has no date filter, recency approximated via relevance)  
Automation run: #12 (cumulative; compares against run#11 baseline JSON)

## 中文摘要 (Chinese Abstract)

本自动化监测第 12 次运行，使用 `lit-review` 技能，通过已连接的 paper-search-mcp（`search_pubmed`，DeferExecuteTool）对甲状腺癌（PTC/PTMC/FTC/MTC/ATC）侵袭、淋巴结与远处转移、复发、预后及其分子机制、肿瘤免疫微环境（TIME）、单细胞（scRNA-seq）、空间组学（spatial multi-omics）、机器学习/深度学习（ML/DL）方法共 9 路互补检索（max_results=15, sort=relevance）。共返回 **130 条原始记录**，去重后 **104 个唯一 PMID**，其中 **76 篇甲状腺相关纳入**，**28 篇非甲状腺/重复排除**。与 run#11 基线（104 个唯一 PMID / 75 篇在域）对比，本次 **新增 0 篇**（0 甲状腺在域 + 0 非甲状腺排除）；9 路检索返回的全部 PMID 已在 run#11 语料中，仅 5 篇 run#11 语料中因 15 行相关性截断而掉出的记录（38981044, 39615165, 40207795, 39903533, 40855521）本轮重新出现并仍按非甲状腺排除处理——**并非新文献**。这延续了自 run#7 以来的平台期（PubMed MCP 对该查询集可见的 2025–2026 文献已基本穷尽）。

**关键收敛发现（5 个主轴不变）：** (1) 代谢–免疫耦合驱动 LNM——MGST1 'Mito-high'/immune-cold 亚群（42327722, AUC 0.833）、SHMT2–PTEN–AKT（38272883）、GLTC–LDHA 琥珀酰化（37031273）、SOX12–YBX1–LDHA（40593465）；(2) 转移干性亚群——APOE−（39810624, ABCA1-LXR）、MGST1 去分化终末、ISG15/KPNA2（37501099, ATC）、DLK1（39595993, MTC）；(3) POSTN+ myCAF 空间图谱（41480746, 42.3 万细胞）预测 LNM；(4) 影像/多组学 AI——LLNM-Net（40750786, AUC 0.944）、CLAM-WSI（41237514）、融合 DL（40771372/39682228/40778281/41061579）、多组学+ML（38990290/41421038）；(5) BRAF V600E 荟萃（41419184, 46 研究/20,570 例）仅关联淋巴结 OR 1.38/复发 OR 1.56，**不**关联远处转移（OR 0.75）或死亡。

**推荐方向：** **D3 — 定义并靶向 APOE−/MGST1+ 代谢–免疫干性转移亚群**（rubric 总分 **32**, 强候选），连续第 12 次被确认为最优下一步。

## English Abstract

Run #12 of the scheduled thyroid-cancer literature monitor used the `lit-review` skill and the connected paper-search-mcp (`search_pubmed` via DeferExecuteTool) to run 9 complementary PubMed queries (max_results=15, sort=relevance) spanning invasion/metastasis mechanisms, LNM biomarkers, ML/DL prediction, tumor immune microenvironment, single-cell RNA-seq, spatial multi-omics, prognosis/recurrence/distant-metastasis risk, metastatic stemness, and metabolic reprogramming. **130 raw records → 104 unique PMIDs → 76 thyroid in-scope (28 non-thyroid/duplicate excluded).** Versus the run#11 baseline (104 unique / 75 in-scope), **0 genuinely new PMIDs** were detected — every PMID retrieved this run was already in the run#11 corpus. Five run#11 records that had fallen off the 15-row relevance cutoff (38981044, 39615165, 40207795, 39903533, 40855521) reappeared and remain correctly excluded as non-thyroid (NSCLC/HCC/TNBC/gastric/pan-cancer). This confirms the plateau observed since run#7 — the PubMed MCP has exhausted visible 2025–2026 literature for this query set.

**Five convergent axes are unchanged:** (1) metabolic–immune coupling drives LNM (MGST1 Mito-high/immune-cold AUC 0.833; SHMT2–PTEN–AKT; GLTC–LDHA succinylation; SOX12–YBX1–LDHA); (2) stem-like metastatic subpopulations (APOE− via ABCA1-LXR; MGST1 dediff tip; ISG15/KPNA2 in ATC; DLK1 in MTC); (3) POSTN+ myCAF spatial atlas (41480746, 423k cells) predicts LNM; (4) crowded imaging/multi-omics AI (LLNM-Net AUC 0.944; CLAM-WSI; fusion DL; multi-omics+ML); (5) BRAF V600E meta (41419184, 46 studies/20,570 pts) links nodal OR 1.38 / recurrence OR 1.56 but NOT distant mets or death.

**Recommended direction: D3 — define & target the APOE−/MGST1+ metabolic–immune stem-like metastatic subpopulation (rubric total 32, Strong), reaffirmed as the best next step for the 12th consecutive run.**

## Search Strategy / 检索策略

| Source | Query | Filters | Results | Notes |
|---|---|---|---:|---|
| PubMed | `thyroid cancer lymph node metastasis biomarker gene signature` | max_results=15, sort=relevance | 15 | 甲状腺相关全纳入；非甲状腺/泛癌综述剔除 |
| PubMed | `thyroid cancer invasion metastasis molecular mechanism` | max_results=15, sort=relevance | 15 | 甲状腺相关全纳入；非甲状腺/泛癌综述剔除 |
| PubMed | `thyroid cancer lymph node metastasis machine learning deep learning prediction model` | max_results=15, sort=relevance | 15 | 甲状腺相关全纳入；非甲状腺/泛癌综述剔除 |
| PubMed | `thyroid cancer metastasis tumor immune microenvironment` | max_results=15, sort=relevance | 13 | 甲状腺相关全纳入；非甲状腺/泛癌综述剔除 |
| PubMed | `thyroid cancer metastasis single cell RNA sequencing` | max_results=15, sort=relevance | 15 | 甲状腺相关全纳入；非甲状腺/泛癌综述剔除 |
| PubMed | `thyroid cancer metastasis spatial transcriptomics spatial multi-omics` | max_results=15, sort=relevance | 11 | 甲状腺相关全纳入；非甲状腺/泛癌综述剔除 |
| PubMed | `thyroid cancer prognosis recurrence distant metastasis risk model` | max_results=15, sort=relevance | 15 | 甲状腺相关全纳入；非甲状腺/泛癌综述剔除 |
| PubMed | `thyroid cancer metastatic stemness subpopulation` | max_results=15, sort=relevance | 16 | 甲状腺相关全纳入；非甲状腺/泛癌综述剔除 |
| PubMed | `thyroid cancer metabolic reprogramming metastasis` | max_results=15, sort=relevance | 15 | 甲状腺相关全纳入；非甲状腺/泛癌综述剔除 |

> 注：paper-search-mcp `search_pubmed` 无日期过滤参数，时间窗以相关性排序近似；每路首次放宽至全部时间。MCP 在本轮出现与历史一致的瞬时解析错误（`not well-formed (invalid token)`），对失败查询重发直至 9 路全部返回（b/c/f/h 各重试 3–4 轮，最终全部成功）。

## Included Papers / 纳入论文（High relevance，共 37 篇）

> 收录规则：relevance=High 的全部在域甲状腺文献；标题与摘要保留英文原文，附一句话中文要点。完整的 High+Medium 证据矩阵见下一节。

A novel gene panel for prediction of lymph-node metastasis and recurrence in patients with thyroid cancer. PTC. PMID: 31711617. DOI: 10.1016/j.surg.2019.06.058.
   Author claim: 25-gene panel discriminates N0/N1 (sens 86%, spec 62%); HR 2.64 for DFS.
   Agent note: relevance=High; dimensions=分子机制/预后转移; validation=KM/Cox in TCGA; caution=no wet-lab validation.
A novel RNA sequencing-based risk score model to predict papillary thyroid carcinoma recurrence. PTC. PMID: 31792675. DOI: 10.1007/s10585-019-10011-4.
   Author claim: 5-gene risk score (TOP2A, RP11-180M15.7, RP11-635N19.1, PROSER3, TMEM139); HR 6.62 train/3.40 val.
   Agent note: relevance=High; dimensions=预后转移/分子机制; validation=chronologic split val; caution=TCGA only.
A 4 Gene-based Immune Signature Predicts Dedifferentiation and Immune Exhaustion in Thyroid Cancer. DDTC/TC. PMID: 33656532. DOI: 10.1210/clinem/dgab132.
   Author claim: 4 IRGs (PRKCQ, PLAUR, PSMD2, BMP7) predict dedifferentiation; linked to LNM & BRAFV600E.
   Agent note: relevance=High; dimensions=免疫微环境/预后转移; validation=2 validation cohorts; caution=no spatial; bulk deconv.
CREB3L1 promotes tumor growth and metastasis of anaplastic thyroid carcinoma by remodeling the tumor microenvironment. ATC. PMID: 36192735. DOI: 10.1186/s12943-022-01658-x.
   Author claim: CREB3L1 up in ATC; activates α-SMA+ CAFs via IL-1α; KPNA2 nuclear transport.
   Agent note: relevance=High; dimensions=单细胞/分子机制; validation=zebrafish/mouse+scRNA; caution=no spatial.
Tumor-Infiltrating Immune Cell Landscapes in the Lymph Node Metastasis of Papillary Thyroid Cancer. PTC LNM. PMID: 36975413. DOI: 10.3390/curroncol30030200.
   Author claim: LNM linked to activated DC/M0 macro (up) & NK/eosinophil (down); TG mut->M2, HRAS mut->DC.
   Agent note: relevance=High; dimensions=免疫微环境; validation=TCGA; caution=bulk deconv.
LncRNA GLTC targets LDHA for succinylation and enzymatic activity to promote progression and radioiodine resistance in papillary thyroid cancer. PTC. PMID: 37031273. DOI: 10.1038/s41418-023-01157-6.
   Author claim: GLTC binds LDHA, blocks SIRT5->K155 succinylation->glycolysis & distant mets; reversal RAI resistance.
   Agent note: relevance=High; dimensions=代谢重编程/分子机制; validation=in vitro/in vivo; caution=no SC.
Artificial intelligence-based prediction of cervical lymph node metastasis in papillary thyroid cancer with CT. PTC CLNM. PMID: 37178202. DOI: 10.1007/s00330-023-09700-2.
   Author claim: AI AUC 0.84 internal/0.81 external; improves radiologist spec 9-15%.
   Agent note: relevance=High; dimensions=算法方法; validation=external test; caution=CT-only.
Identification of key immune genes related to lymphatic metastasis of papillary thyroid cancer via bioinformatics analysis and experimental validation. PTC. PMID: 37274228. DOI: 10.3389/fonc.2023.1181325.
   Author claim: 3 hub immune genes (PTGS2, MET, ICAM1) upregulated in LNM; model AUC 0.83; IHC validated.
   Agent note: relevance=High; dimensions=免疫微环境/分子机制; validation=IHC validation; caution=bulk only.
Papillary thyroid cancer immune phenotypes via tumor-infiltrating lymphocyte spatial analysis. PTC. PMID: 37279258. DOI: 10.1530/ERC-23-0110.
   Author claim: 3 immune phenotypes (desert 48%/excluded 34%/inflamed 18%); excluded=BRAF V600E+ higher LNM.
   Agent note: relevance=High; dimensions=免疫微环境/空间组学; validation=TCGA WSI; caution=no functional.
ISG15 and ISGylation modulates cancer stem cell-like characteristics in promoting tumor growth of anaplastic thyroid carcinoma. ATC. PMID: 37501099. DOI: 10.1186/s13046-023-02751-9.
   Author claim: ISG15 enriched in ATC CSCs; ISG15-ISGylation of KPNA2 stabilizes it->stemness; depletion inhibits mets.
   Agent note: relevance=High; dimensions=单细胞/分子机制/转移干性; validation=mouse/zebrafish+scRNA; caution=no spatial.
Single-cell and bulk RNA sequencing reveal heterogeneity and diagnostic markers in papillary thyroid carcinoma lymph-node metastasis. PTC LNM. PMID: 38146045. DOI: 10.1007/s40618-023-02262-6.
   Author claim: 19-gene DEG model; S100A2 & DIO2 validated (RT-qPCR/IHC); DIO2 inhibits proliferation.
   Agent note: relevance=High; dimensions=单细胞/分子机制; validation=66-pt IHC/RT-qPCR; caution=modest n.
IRS1 promotes thyroid cancer metastasis through EMT and PI3K/AKT pathways. TC. PMID: 38172081. DOI: 10.1111/cen.15005.
   Author claim: IRS1 high in TC, linked to distant mets/advanced stage; drives mets via EMT & PI3K/AKT.
   Agent note: relevance=High; dimensions=分子机制; validation=in vitro; caution=no SC.
SHMT2 promotes papillary thyroid cancer metastasis through epigenetic activation of AKT signaling. PTC. PMID: 38272883. DOI: 10.1038/s41419-024-06476-1.
   Author claim: SHMT2 generates SAM->methylates PTEN->AKT->PTC mets; AKT block abolishes.
   Agent note: relevance=High; dimensions=代谢重编程/分子机制; validation=in vitro/in vivo; caution=no SC.
Artificial intelligence-based multi-modal multi-tasks analysis reveals tumor molecular heterogeneity, predicts preoperative lymph node metastasis and prognosis in papillary thyroid carcinoma. PTC. PMID: 38990290. DOI: 10.1097/JS9.0000000000001875.
   Author claim: 4 molecular subtypes; DL AUC 0.86 train/0.84 val/0.83 real-world for LNM & DFS.
   Agent note: relevance=High; dimensions=算法方法/分子机制/单细胞; validation=TCGA external val; caution=retrospective, single real-world center.
Spatial and Single-Cell Transcriptomics Unraveled Spatial Evolution of Papillary Thyroid Cancer. PTC. PMID: 39540244. DOI: 10.1002/advs.202404491.
   Author claim: 2 malignant/metastatic footprints; ferroptosis resistance aids PTC evolution.
   Agent note: relevance=High; dimensions=单细胞/空间组学/分子机制; validation=SRT; caution=single-center.
Predicting lymph node metastasis in thyroid cancer: systematic review and meta-analysis on the CT/MRI-based radiomics and deep learning models. TC. PMID: 39742800. DOI: 10.1016/j.clinimag.2024.110392.
   Author claim: Pooled AUC 0.86 internal/0.87 train; DL sens 80.8%/spec 78.7% > radiomics; clinical data helps (p=0.037).
   Agent note: relevance=High; dimensions=算法方法; validation=meta (16); caution=heterogeneity.
Single-cell RNA-sequencing and spatial transcriptomic analysis reveal a distinct population of APOE- cells yielding pathological lymph node metastasis in papillary thyroid cancer. PTC. PMID: 39810624. DOI: 10.1002/ctm2.70172.
   Author claim: APOE- tumor subpop drives cervical LNM & poor prognosis via ABCA1-LXR; 13-gene ML LNM signature.
   Agent note: relevance=High; dimensions=单细胞/空间组学/分子机制/算法方法/转移干性; validation=in vivo/in vitro+ST; caution=single-center SC/ST.
An integrated single-cell and spatial transcriptomic atlas of thyroid cancer progression identifies prognostic fibroblast subpopulations. TC. PMID: 39829764. DOI: 10.1101/2025.01.08.631962.
   Author claim: myCAF only in malignant samples; abuts invasive tumor cells; preprint of 41480746.
   Agent note: relevance=High; dimensions=单细胞/空间组学; validation=ST; caution=preprint/biorxiv.
5-HT orchestrates histone serotonylation and citrullination to drive neutrophil extracellular traps and liver metastasis. MTC/NE. PMID: 39903533. DOI: 10.1172/JCI183544.
   Author claim: in vivo+FDA drug
   Agent note: relevance=High; dimensions=免疫微环境/分子机制; validation=MTC subset of NE cancers; caution=Confirm in primary MTC cohorts.
Identification of Novel Gene Signature Predicting Lymph Node Metastasis in Papillary Thyroid Cancer via Bioinformatics Analysis and in vitro Validation. PTC. PMID: 40110574. DOI: 10.2147/IJGM.S502480.
   Author claim: 6-gene signature (COL8A2, MET, FN1, MPZL2, PDLIM4, CLDN10) predicts PTC LNM; all 6 validated in vitro.
   Agent note: relevance=High; dimensions=分子机制/预后转移; validation=in vitro (RT-qPCR/functional); caution=TCGA/GEO bulk only, no spatial/SC validation.
A nomogram based on the 3-gene signature and clinical characteristics for predicting lymph node metastasis in papillary thyroid cancer. PTC. PMID: 40171809. DOI: 10.1177/18758592241311195.
   Author claim: 3-gene signature (IQGAP2, BTBD11, MT1G)+clinical nomogram AUC 0.802 train/0.718 val.
   Agent note: relevance=High; dimensions=分子机制/预后转移; validation=internal val cohort; caution=single-cohort, modest val AUC.
The SOX12-YBX1-LDHA signaling axis drives metastasis in papillary thyroid carcinoma. PTC. PMID: 40593465. DOI: 10.1038/s41419-025-07797-5.
   Author claim: SOX12->YBX1->LDHA promoter->TGF-beta->mets; LDHA rescue confirms.
   Agent note: relevance=High; dimensions=单细胞/分子机制/代谢重编程; validation=clinical+functional; caution=no spatial.
Single-Cell RNA Sequencing Reveals the Heterogeneity in Differentiation Trajectory and Tumor Microenvironment Leading to More Aggressive Phenotypes of Papillary Thyroid Cancer in Children and Young Adult Patients. CAYA-PTC. PMID: 40719066. DOI: 10.1002/advs.202417672.
   Author claim: CAYA-PTC lacks mild BRAF-like state->rapid invasive; emCAF_LAMP5 (FAP+) drives angiogenesis/mets; 68Ga-FAPI-PET.
   Agent note: relevance=High; dimensions=单细胞/免疫微环境; validation=scRNA; caution=small n.
Development and validation of mRNA expression-based classifiers to predict low-risk thyroid tumors. Bethesda III-VI. PMID: 40741176. DOI: 10.3389/fendo.2025.1600815.
   Author claim: mRNA classifiers rule out invasion (NPV 97.6%) & LNM (NPV 98.6%) preoperatively.
   Agent note: relevance=High; dimensions=算法方法/预后转移; validation=retrospective val (259); caution=retrospective; vendor cohort.
Explainable multimodal deep learning for predicting thyroid cancer lateral lymph node metastasis using ultrasound imaging. PTC LLNM. PMID: 40750786. DOI: 10.1038/s41467-025-62042-z.
   Author claim: LLNM-Net AUC 0.944, 84.7% acc in multicenter testing; beats experts (64.3%).
   Agent note: relevance=High; dimensions=算法方法; validation=7-center external; caution=retrospective; US-only.
Development and validation of a prediction model for lymph node metastasis in thyroid cancer: integrating deep learning and radiomics features from intra- and peri-tumoral regions. PTC CLNM. PMID: 40771372. DOI: 10.21037/gs-2025-50.
   Author claim: Fusion SVM AUC 0.897 internal/0.881 external; best of radiomics/DL.
   Agent note: relevance=High; dimensions=算法方法; validation=external test; caution=US-only.
Multi-omics analysis and metastasis risk factor prediction in N1b stage PTMC: insights into immune infiltration and therapeutic implications. PTMC N1b. PMID: 40977710. DOI: 10.3389/fimmu.2025.1620085.
   Author claim: NLR model (AUC 0.852); 4-gene signature (ALDH1A3, CTXN1, MGAT3, TMEM163) AUC 0.857; CD8+ T reduced.
   Agent note: relevance=High; dimensions=分子机制/免疫微环境/预后转移; validation=IHC+MLP; caution=retrospective.
A multi-task deep learning framework for intraoperative diagnosis of thyroid cancer metastasis using whole slide images. PTC LNM. PMID: 41237514. DOI: 10.1016/j.ijmedinf.2025.106176.
   Author claim: CLAM AUC 0.85 LNM, 0.65 T-stage, 0.71 localization; cross-center.
   Agent note: relevance=High; dimensions=算法方法; validation=10-fold MC CV; caution=weak T-stage/localization.
Single-cell RNA sequencing reveals tumor cell and immune cell variations associated with lymphatic metastasis in papillary thyroid cancer. PTC. PMID: 41257484. DOI: 10.1530/EC-25-0514.
   Author claim: PTC with LM shows proliferation/migration pathways; CD8+ TRM pivotal via MHC-I/CD99/LCK.
   Agent note: relevance=High; dimensions=单细胞/免疫微环境; validation=6-pt scRNA; caution=small n.
Integrated spatial metabolomics and transcriptomics reveal the molecular landscape of papillary thyroid cancer and its lymph node metastasis. PTC LNM. PMID: 41398964. DOI: 10.1186/s12967-025-07566-0.
   Author claim: Arginine-polyamine/glycolysis/lipid dysregulated; 5 metastasis-driving metabolites; NAT8L/SVCT-2 knockdown reduces mets.
   Agent note: relevance=High; dimensions=空间组学/代谢重编程/分子机制; validation=TCGA+zf xenograft; caution=single-center.
Prognostic Value of BRAF V600E Mutation in Papillary Thyroid Carcinoma: A Meta-Analysis. PTC. PMID: 41419184. DOI: 10.1016/j.eprac.2025.12.003.
   Author claim: BRAF V600E OR 1.38 nodal, 1.56 recurrence; NOT distant (0.75) or death (0.97).
   Agent note: relevance=High; dimensions=分子机制/预后转移; validation=meta (46); caution=heterogeneity.
Cellular and molecular determinants of lymph node metastasis in papillary thyroid carcinoma: Integrated multi-omics profiling and machine learning models. PTC LNM. PMID: 41421038. DOI: 10.1016/j.compbiolchem.2025.108857.
   Author claim: FN1-SDC4 axis validated by ST; 17-gene LNM signature; random forest LNM model.
   Agent note: relevance=High; dimensions=单细胞/空间组学/算法方法/分子机制; validation=in vitro+ST; caution=single-center.
An integrated single-cell and spatial transcriptomic atlas of thyroid cancer progression identifies prognostic fibroblast subpopulations. WDTC/ATC/pediatric. PMID: 41480746. DOI: 10.1172/jci.insight.191990.
   Author claim: POSTN+ myCAF associated with invasion, LNM, poor prognosis (42.3万 cells).
   Agent note: relevance=High; dimensions=单细胞/空间组学; validation=multi-institutional ST; caution=rare subtypes small.
A multi-molecular predictive model for lymph node metastasis in papillary thyroid carcinoma based on machine learning algorithms. PTC. PMID: 41656803. DOI: 10.11817/j.issn.1672-7347.2025.250216.
   Author claim: 11-gene signature (incl. FN1) Model 2 AUC 0.802 train/0.793 val; stable across 6 ML algos.
   Agent note: relevance=High; dimensions=算法方法/分子机制/预后转移; validation=TCGA val; sex-strat; caution=TCGA only; no external.
DNA Methylation-Based Risk Stratification and Classification of Pediatric Thyroid Carcinoma. pediatric TC. PMID: 41701943. DOI: 10.1158/1078-0432.CCR-25-2109.
   Author claim: Methylation classifiers predict tumor invasiveness (nodal mets) & driver mutations in pediatric TC.
   Agent note: relevance=High; dimensions=分子机制/预后转移; validation=independent val cohort; caution=limited LNM samples.
Development and validation of a machine learning model for predicting high-risk distant metastatic recurrence in differentiated thyroid cancer. DTC. PMID: 41877795. DOI: 10.3389/fmed.2026.1790226.
   Author claim: XGBoost AUC 0.88 (374-case external); 8 predictors incl BRAF V600E, sTg.
   Agent note: relevance=High; dimensions=算法方法/预后转移; validation=external val (374); caution=retrospective.
MGST1 drives lymph node metastasis in papillary thyroid carcinoma via mitochondrial metabolic reprogramming and immune suppression. PTC. PMID: 42327722. DOI: 10.3389/fimmu.2026.1848083.
   Author claim: Mito-high/immune-cold subtype; MGST1 core predictor AUC 0.833; MGST1 at dediff tip = stem-like metastatic; toxoflavin inhibits.
   Agent note: relevance=High; dimensions=代谢重编程/免疫微环境/分子机制/转移干性; validation=external val+in vitro; caution=single-center SC.

## Evidence Matrix / 证据矩阵

> 按 evidence-matrix-schema.md 列制表；Relevance/Gap 列体现所属维度（多标签）。仅列 High 与关键 Medium 文献（共 66 篇）。

| Paper | PMID/DOI | Disease/Population | Data Source | Method | Endpoint | Main Finding | Validation | Limitations | Relevance | Gap Suggested | Future Direction |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Molecular mechanisms involved in differentiated thyroid canc | 17133106 / 10.2147 | DTC | review | review | invasion/mets | RAS-RAF-ERK & PI3K/PDK1/Akt; EMT & collective migration reactivated. | review | old review (2007) | Medium (分子机制) | Modern single-cell resolution of EMT | SC EMT trajectory |
| BRAF mutation in papillary thyroid cancer: pathogenic role,  | 17940185 / 10.2147 | PTC | review | review | progression/recurrence | BRAF V600E associated with progression/recurrence; downregulates TSGs & iodide genes. | review | old review (2007) | Medium (分子机制/预后转移) | Subtype heterogeneity | Combine with co-alts |
| Transcriptome Analyses Identify a Metabolic Gene Signature I | 30942873 / 10.1210/jc.2018-02686 | PTC/DDTC | TCGA+GEO | metabolic signature+Cox | dediff/LNM | 5 metabolic genes (LPCAT2, ACOT7, HSD17B8, PDE8B, ST3GAL1) mark dediff; linked to LNM. | 3 cohorts | bulk only | Medium (分子机制/代谢重编程/预后转移) | Mechanism linking metabolism to dediff | SC/metabolic validation |
| A novel gene panel for prediction of lymph-node metastasis a | 31711617 / 10.1016/j.surg.2019.06.058 | PTC | TCGA | ML+logistic/Cox | LNM/recurrence | 25-gene panel discriminates N0/N1 (sens 86%, spec 62%); HR 2.64 for DFS. | KM/Cox in TCGA | no wet-lab validation | High (分子机制/预后转移) | Which genes drive metastasis biologically | Validate top drivers functionally |
| A novel RNA sequencing-based risk score model to predict pap | 31792675 / 10.1007/s10585-019-10011-4 | PTC | TCGA | Cox+LASSO | recurrence | 5-gene risk score (TOP2A, RP11-180M15.7, RP11-635N19.1, PROSER3, TMEM139); HR 6.62 train/3 | chronologic split val | TCGA only | High (预后转移/分子机制) | External validation | External recurrence model |
| Development and Validation of a Risk Scoring System Derived  | 32615728 / 10.3803/EnM.2020.35.2.435 | PTC | 5 meta-analyses | RSS | prognosis | RSS1 (8 vars) superior to AJCC/ATA for PTC risk. | meta-derived | no individual data | Medium (预后转移) | Individual-level validation | Individual-level RSS |
| Immune Microenvironment of Thyroid Cancer | 32626535 / 10.7150/jca.44506 | TC | review | review | TIME | Reviews immune cells, soluble mediators, checkpoints, evasion & immunotherapy in TC. | review | review | Medium (免疫微环境) | Spatial immune phenotyping | Spatial TIL |
| A 4 Gene-based Immune Signature Predicts Dedifferentiation a | 33656532 / 10.1210/clinem/dgab132 | DDTC/TC | TCGA+bulk | IRG signature+Cox | dediff/LNM | 4 IRGs (PRKCQ, PLAUR, PSMD2, BMP7) predict dedifferentiation; linked to LNM & BRAFV600E. | 2 validation cohorts | no spatial; bulk deconv | High (免疫微环境/预后转移) | How IRGs drive immune exhaustion spatially | Spatial TIL/IRG mapping |
| A four-enhancer RNA-based prognostic signature for thyroid c | 35033555 / 10.1016/j.yexcr.2022.113023 | TC | GTEx+TCGA | eRNA+Cox | prognosis/LNM | 4 eRNAs (AC141930.1, NBDY, MEG3, AP002358.1) predict prognosis; linked to N stage. | TCGA+GEO | no wet-lab | Medium (预后转移) | Functional role of eRNAs in metastasis | Validate eRNA drivers |
| Transcriptomic Analysis of Papillary Thyroid Cancer: A Focus | 35255661 / 10.21053/ceo.2021.02215 | PTC | SNUH+SNUH+TCGA | RNA-seq+sc | recurrence/immune | Recurrence linked to CD8+/Th1 signatures; CTLA4/IDO1/LAG3/PDCD1 in low-TDS; HOXD9 recurren | TCGA val | single-country | Medium (免疫微环境/预后转移) | Functional role of HOXD9 | Validate HOXD9 |
| CREB3L1 promotes tumor growth and metastasis of anaplastic t | 36192735 / 10.1186/s12943-022-01658-x | ATC | scRNA+microarray | scRNA+in vivo | mets | CREB3L1 up in ATC; activates α-SMA+ CAFs via IL-1α; KPNA2 nuclear transport. | zebrafish/mouse+scRNA | no spatial | High (单细胞/分子机制) | Spatial CAF-tumor interaction | Spatial ATC CAF |
| Deep learning-based multifeature integration robustly predic | 36750791 / 10.1186/s12885-023-10598-8 | PTC CLNM | 488 FNA | CNN+logistic | CLNM | CNN AUC 0.89 train/0.78 test; nomogram 0.778. | test set | single center | Medium (算法方法) | External validation | External CNN |
| Tumor-Infiltrating Immune Cell Landscapes in the Lymph Node  | 36975413 / 10.3390/curroncol30030200 | PTC LNM | TCGA+bulk | CIBERSORT/CIBERSORTx | LNM | LNM linked to activated DC/M0 macro (up) & NK/eosinophil (down); TG mut->M2, HRAS mut->DC. | TCGA | bulk deconv | High (免疫微环境) | Spatial immune niches in LNM | Spatial immune |
| LncRNA GLTC targets LDHA for succinylation and enzymatic act | 37031273 / 10.1038/s41418-023-01157-6 | PTC | specimens+in vivo | mass-spec+functional | distant mets/RAI | GLTC binds LDHA, blocks SIRT5->K155 succinylation->glycolysis & distant mets; reversal RAI | in vitro/in vivo | no SC | High (代谢重编程/分子机制) | Spatial GLTC/LDHA gradient | Spatial GLTC |
| The Tumor Microenvironment and the Estrogen Loop in Thyroid  | 37173925 / 10.3390/cancers15092458 | TC | review | review | TIME | Reviews estrogen-TME crosstalk in TC (PI3K/AKT/mTOR, RAS/Raf/MAPK). | review | review | Medium (免疫微环境) | Mechanistic estrogen-immune axis | Estrogen axis |
| Artificial intelligence-based prediction of cervical lymph n | 37178202 / 10.1007/s00330-023-09700-2 | PTC CLNM | multicenter CT | DenseNet+CBAM+ML | CLNM | AI AUC 0.84 internal/0.81 external; improves radiologist spec 9-15%. | external test | CT-only | High (算法方法) | Prospective + other centers | Prospective CT-AI |
| Identification of key immune genes related to lymphatic meta | 37274228 / 10.3389/fonc.2023.1181325 | PTC | TCGA+ImmPort | WGCNA+LASSO/RF | LNM | 3 hub immune genes (PTGS2, MET, ICAM1) upregulated in LNM; model AUC 0.83; IHC validated. | IHC validation | bulk only | High (免疫微环境/分子机制) | Spatial immune landscape of MET/ICAM1 | Spatial IHC/ST |
| Papillary thyroid cancer immune phenotypes via tumor-infiltr | 37279258 / 10.1530/ERC-23-0110 | PTC | TCGA WSI | AI TIL spatial | LNM/immune | 3 immune phenotypes (desert 48%/excluded 34%/inflamed 18%); excluded=BRAF V600E+ higher LN | TCGA WSI | no functional | High (免疫微环境/空间组学) | Therapeutic targeting of excluded phenotype | Target excluded IP |
| ISG15 and ISGylation modulates cancer stem cell-like charact | 37501099 / 10.1186/s13046-023-02751-9 | ATC | scRNA+in vivo | scRNA+in vivo | mets/stemness | ISG15 enriched in ATC CSCs; ISG15-ISGylation of KPNA2 stabilizes it->stemness; depletion i | mouse/zebrafish+scRNA | no spatial | High (单细胞/分子机制/转移干性) | ISG15/KPNA2 as ATC therapeutic | ATC CSC targeting |
| Deep learning prediction model for central lymph node metast | 37574759 / 10.1111/cas.15930 | PTMC CLNM | 42 FNA | CNN | CLNM | DL on FNA liquid-based prep AUC 0.850; surpasses clinical exam. | small (42) | tiny n | Medium (算法方法) | Larger FNA cytology cohort | Scale FNA-DL |
| Myc-Associated Zinc Finger Protein Promotes Metastasis of Pa | 37664917 / 10.31083/j.fbl2808162 | PTC | TCGA+IHC | IHC+functional | mets | MAZ high promotes PTC migration/invasion via EMT; FN1 negatively correlated. | in vitro | no SC | Medium (分子机制) | MAZ-FN1 axis detail | MAZ functional |
| Thyroid Cancer: Focus on Invasion and Metastasis Mechanisms, | 37835455 / 10.3390/cancers15194762 | TC | review | review | invasion/mets | Reviews invasion/metastasis mechanisms & therapeutic targets in TC. | review | review | Medium (分子机制/预后转移) | Mechanistic gaps in therapy resistance | Targeted therapy combos |
| BRAF V600E mutation in papillary thyroid microcarcinoma: is  | 37851243 / 10.12020-023-03564-8 | PTMC | 322 pts | PSM+logistic | recurrence | BRAFV600E not associated with outcomes after RAI in intermediate/high-risk PTMC. | PSM | single center | Medium (分子机制/预后转移) | Larger PTMC cohort | PTMC outcomes |
| A novel cuproptosis-related lncRNA prognostic signature in t | 37934030 / 10.2217/bmm-2023-0216 | TC | TCGA | Cox | prognosis/recurrence | 4 cuproptosis-lncRNA signature; AUC 0.830/0.790/0.824 at 1/3/5y. | TCGA | no wet-lab | Medium (预后转移) | Cuproptosis mechanism in TC | Cuproptosis validation |
| Single-cell and bulk RNA sequencing reveal heterogeneity and | 38146045 / 10.1007/s40618-023-02262-6 | PTC LNM | scRNA+bulk+66 pt | scRNA+bulk | LNM/dx | 19-gene DEG model; S100A2 & DIO2 validated (RT-qPCR/IHC); DIO2 inhibits proliferation. | 66-pt IHC/RT-qPCR | modest n | High (单细胞/分子机制) | Multi-center DIO2 validation | DIO2 validation |
| IRS1 promotes thyroid cancer metastasis through EMT and PI3K | 38172081 / 10.1111/cen.15005 | TC | 131 tissues+RNAseq | IHC+RNAseq | distant mets | IRS1 high in TC, linked to distant mets/advanced stage; drives mets via EMT & PI3K/AKT. | in vitro | no SC | High (分子机制) | Therapeutic targeting of IRS1 | IRS1 inhibitor |
| SHMT2 promotes papillary thyroid cancer metastasis through e | 38272883 / 10.1038/s41419-024-06476-1 | PTC | specimens+in vivo | proteomic+functional | mets | SHMT2 generates SAM->methylates PTEN->AKT->PTC mets; AKT block abolishes. | in vitro/in vivo | no SC | High (代谢重编程/分子机制) | Spatial SHMT2/PTEN gradient | Spatial SHMT2 |
| Artificial intelligence-based multi-modal multi-tasks analys | 38990290 / 10.1097/JS9.0000000000001875 | PTC | 1011 PTC (TCGA+real-world+scRNA) | DL multimodal | LNM/DFS | 4 molecular subtypes; DL AUC 0.86 train/0.84 val/0.83 real-world for LNM & DFS. | TCGA external val | retrospective, single real-world center | High (算法方法/分子机制/单细胞) | Prospective multi-center DL | Prospective DL |
| Molecular mechanisms and clinicopathological characteristics | 39301627 / 10.3892/ijmm.2024.5423 | TC | GEO/TCGA+in vivo | transfect+zf/mouse | mets | INHBA promotes TC migration/invasion via RhoA/LIMK/cofilin; knockdown attenuates mets. | in vivo | no SC | Medium (分子机制) | Therapeutic INHBA blockade | INHBA inhibitor |
| Radiomics and deep learning for large volume lymph node meta | 39421056 / 10.21037/gs-24-308 | PTC LVLNM | 854 pts/3 centers | radiomics+DL (8 ML + 5 DL) | LVLNM | Thy-DL-Radiomics AUC 0.839 internal/0.789 external for large-volume LNM. | external val | LVLNM subset only | Medium (算法方法) | Generalize to all CLNM | Broaden LVLNM model |
| Coagulation-related genes for thyroid cancer prognosis, immu | 39497824 / 10.3389/fimmu.2024.1462755 | THCA | TCGA | LASSO+Cox | LLNM/prognosis | D-dimer predicts LLNM (AUC 0.656); 8 prognostic CRGs model. | qPCR | modest AUC; bulk | Medium (免疫微环境/预后转移) | Mechanism linking coagulation to mets | Functional coagulation axis |
| Spatial and Single-Cell Transcriptomics Unraveled Spatial Ev | 39540244 / 10.1002/advs.202404491 | PTC | scRNA+SRT | scRNA+SRT | evolution/mets | 2 malignant/metastatic footprints; ferroptosis resistance aids PTC evolution. | SRT | single-center | High (单细胞/空间组学/分子机制) | Validate footprints across cohorts | Multi-center SRT |
| DLK1 Is Associated with Stemness Phenotype in Medullary Thyr | 39595993 / 10.3390/ijms252211924 | MTC | cell lines | in vitro | stemness | DLK1+ cells higher stemness/spheroid/dye-efflux in MTC. | in vitro | cell-line only | Medium (转移干性/分子机制) | In vivo/primary MTC validation | MTC DLK1 validation |
| Multimodal MRI Deep Learning for Predicting Central Lymph No | 39682228 / 10.3390/cancers16234042 | PTC CLNM | 105 MRI | AMMCNet (CNN) | CLNM | DL fusion AUC 0.891 > best ML 0.863. | internal test | small, MRI-only | Medium (算法方法) | External multi-center MRI | External MRI-DL |
| Predicting lymph node metastasis in thyroid cancer: systemat | 39742800 / 10.1016/j.clinimag.2024.110392 | TC | 16 studies (meta) | meta | LNM | Pooled AUC 0.86 internal/0.87 train; DL sens 80.8%/spec 78.7% > radiomics; clinical data h | meta (16) | heterogeneity | High (算法方法) | Standardized reporting/prospective | Prospective harmonization |
| Single-cell RNA-sequencing and spatial transcriptomic analys | 39810624 / 10.1002/ctm2.70172 | PTC | scRNA+ST | scRNA+ST+ML | LNM | APOE- tumor subpop drives cervical LNM & poor prognosis via ABCA1-LXR; 13-gene ML LNM sign | in vivo/in vitro+ST | single-center SC/ST | High (单细胞/空间组学/分子机制/算法方法/转移干性) | Target APOE- subpopulation therapeutically | APOE- targeted therapy |
| An integrated single-cell and spatial transcriptomic atlas o | 39829764 / 10.1101/2025.01.08.631962 | TC | scRNA+ST | scRNA+ST | invasion/LNM | myCAF only in malignant samples; abuts invasive tumor cells; preprint of 41480746. | ST | preprint/biorxiv | High (单细胞/空间组学) | Reconciled with 41480746 | - |
| 5-HT orchestrates histone serotonylation and citrullination  | 39903533 / 10.1172/JCI183544 | MTC/NE | in vivo+FDA drug | NETs | MTC/NE liver mets via 5-HT->NETs; fluoxetine/SERT blocks. | in vivo+FDA drug | MTC subset of NE cancers | Confirm in primary MTC cohorts | High (免疫微环境/分子机制) | MTC liver-mets trial | MTC NETs validation |
| Identification of Novel Gene Signature Predicting Lymph Node | 40110574 / 10.2147/IJGM.S502480 | PTC | TCGA+GEO(GSE60542) | WGCNA+LASSO | LNM | 6-gene signature (COL8A2, MET, FN1, MPZL2, PDLIM4, CLDN10) predicts PTC LNM; all 6 validat | in vitro (RT-qPCR/functional) | TCGA/GEO bulk only, no spatial/SC validation | High (分子机制/预后转移) | No single-cell or spatial resolution of these drivers | Spatial validation of MET/FN1 axis |
| A nomogram based on the 3-gene signature and clinical charac | 40171809 / 10.1177/18758592241311195 | PTC | TCGA | WGCNA+LASSO+logistic | LNM | 3-gene signature (IQGAP2, BTBD11, MT1G)+clinical nomogram AUC 0.802 train/0.718 val. | internal val cohort | single-cohort, modest val AUC | High (分子机制/预后转移) | Mechanistic link between MT1G/BTBD11 and immune stroma | Functionally test IQGAP2/BTBD11 in LNM |
| Reprogramming of fatty acid metabolism in thyroid cancer: Po | 40353071 / 10.21147/j.issn.1000-9604.2025.02.09 | TC | review | review | mets | Reviews FA metabolic reprogramming targets in TC. | review | review | Medium (代谢重编程) | FA-targeted therapy trials | FA-targeted |
| The SOX12-YBX1-LDHA signaling axis drives metastasis in papi | 40593465 / 10.1038/s41419-025-07797-5 | PTC | scRNA+bulk+CUT&Tag | scRNA+CUT&Tag | mets | SOX12->YBX1->LDHA promoter->TGF-beta->mets; LDHA rescue confirms. | clinical+functional | no spatial | High (单细胞/分子机制/代谢重编程) | Spatial SOX12/LDHA gradient | Spatial SOX12 |
| An integrative analysis reveals mechanisms of Prunella vulga | 40651298 / 10.1016/j.phymed.2025.157051 | PTC LNM | RNAseq+TCMSP | ML+hub gene | LNM | β-sitosterol targets ADRB2, inhibits PTC mets via mitochondrial dysfunction. | in vitro | herb-focused | Medium (分子机制/代谢重编程) | ADRB2 mechanism in LNM | ADRB2 validation |
| Single-Cell RNA Sequencing Reveals the Heterogeneity in Diff | 40719066 / 10.1002/advs.202417672 | CAYA-PTC | scRNA (11 pts) | scRNA | aggressive/mets | CAYA-PTC lacks mild BRAF-like state->rapid invasive; emCAF_LAMP5 (FAP+) drives angiogenesi | scRNA | small n | High (单细胞/免疫微环境) | Validate emCAF_LAMP5 across ages | CAYA emCAF validation |
| Development and validation of mRNA expression-based classifi | 40741176 / 10.3389/fendo.2025.1600815 | Bethesda III-VI | Afirma GSC+retrospective | ML classifiers | invasion/LNM | mRNA classifiers rule out invasion (NPV 97.6%) & LNM (NPV 98.6%) preoperatively. | retrospective val (259) | retrospective; vendor cohort | High (算法方法/预后转移) | Prospective multi-site validation | Prospective deployment |
| Explainable multimodal deep learning for predicting thyroid  | 40750786 / 10.1038/s41467-025-62042-z | PTC LLNM | 29,615 pts/7 centers | LLNM-Net (bidir-attn DL) | LLNM | LLNM-Net AUC 0.944, 84.7% acc in multicenter testing; beats experts (64.3%). | 7-center external | retrospective; US-only | High (算法方法) | Prospective deployment + cost-effectiveness | Prospective LLNM-Net |
| Development and validation of a prediction model for lymph n | 40771372 / 10.21037/gs-2025-50 | PTC CLNM | 405 pts/2 centers | radiomics+DL fusion SVM | CLNM | Fusion SVM AUC 0.897 internal/0.881 external; best of radiomics/DL. | external test | US-only | High (算法方法) | Prospective + other modalities | Prospective fusion |
| A novel deep learning model based on multimodal contrast-enh | 40778281 / 10.3389/fendo.2025.1634875 | PTC OLNM | 396 US/CEUS | DL video (5 arch) | OLNM | DL_combined AUC 0.926 train/0.734 test. | test set | test drop-off | Medium (算法方法) | Larger CEUS video cohort | Scale CEUS-DL |
| Multi-omics analysis and metastasis risk factor prediction i | 40977710 / 10.3389/fimmu.2025.1620085 | PTMC N1b | 638 PTMC+sc/omics | ML+WGCNA+MLP | lateral LNM | NLR model (AUC 0.852); 4-gene signature (ALDH1A3, CTXN1, MGAT3, TMEM163) AUC 0.857; CD8+ T | IHC+MLP | retrospective | High (分子机制/免疫微环境/预后转移) | Therapeutic targeting of signature | Prospective N1b risk |
| Thyroid cancer: From molecular insights to therapy (Review) | 40980146 / 10.3892/ol.2025.15266 | PTC/FTC/MTC/ATC | review | review | therapy | Subtype molecular (BRAF/RAS/RET/TERT/p53) & metabolic overview. | review | review | Medium (分子机制/代谢重编程/预后转移) | Subtype-specific metabolic trials | Subtype trials |
| Exosome-mediated metabolic reprogramming: effects on thyroid | 41057823 / 10.1186/s12943-025-02470-z | TC | review | review | mets/TME | Exosomes drive TC metabolic reprogramming & immune escape. | review | review | Medium (免疫微环境/代谢重编程) | Exosomal cargo causal tests | Exosome cargo |
| SCLResNet and DSAF: A self-supervised contrastive learning a | 41061579 / 10.1016/j.artmed.2025.103280 | PTC CLNM | US+CT | SCLResNet+DSAF | CLNM | AUC 0.863 internal/0.839 external; adds PVAT. | external test | retrospective | Medium (算法方法) | Prospective multi-modal | Prospective fusion |
| Aggressiveness of papillary thyroid carcinoma: a comprehensi | 41084771 / 10.5603/fhc.108530 | PTC | review | review | aggressiveness | Integrates molecular, epigenetic, immune & imaging for PTC aggressiveness. | review | review | Medium (分子机制/预后转移) | Subtype-specific aggressiveness | Subtype aggressiveness |
| A multi-task deep learning framework for intraoperative diag | 41237514 / 10.1016/j.ijmedinf.2025.106176 | PTC LNM | 569 WSIs/2 centers | CLAM (MIL) | LNM/T-stage/localization | CLAM AUC 0.85 LNM, 0.65 T-stage, 0.71 localization; cross-center. | 10-fold MC CV | weak T-stage/localization | High (算法方法) | Improve localization subtask | Refine CLAM tasks |
| Single-cell RNA sequencing reveals tumor cell and immune cel | 41257484 / 10.1530/EC-25-0514 | PTC | scRNA (6 pts) | scRNA+CellChat | LNM | PTC with LM shows proliferation/migration pathways; CD8+ TRM pivotal via MHC-I/CD99/LCK. | 6-pt scRNA | small n | High (单细胞/免疫微环境) | Validate CD8+ TRM in larger LNM cohort | CD8 TRM validation |
| BRAF V600E in thyroid cancer: navigating prognostic uncertai | 41368991 / 10.1530/ETJ-25-0225 | PTC/ATC/PDTC | review | review | prognosis | BRAF V600E debated prognostic value; drives MAPK, RAI-refractoriness; targetable. | review | review, not primary | Medium (分子机制/预后转移) | Subtype-specific heterogeneity of V600E effect | Combine V600E with co-alterations |
| Integrated spatial metabolomics and transcriptomics reveal t | 41398964 / 10.1186/s12967-025-07566-0 | PTC LNM | spatial metabolomics+ST | spatial multi-omics | LNM | Arginine-polyamine/glycolysis/lipid dysregulated; 5 metastasis-driving metabolites; NAT8L/ | TCGA+zf xenograft | single-center | High (空间组学/代谢重编程/分子机制) | Spatial multi-omics in ATC/MTC | Spatial multi-omics expand |
| Prognostic Value of BRAF V600E Mutation in Papillary Thyroid | 41419184 / 10.1016/j.eprac.2025.12.003 | PTC | 46 studies/20,570 pts | meta | nodal/recurrence/death | BRAF V600E OR 1.38 nodal, 1.56 recurrence; NOT distant (0.75) or death (0.97). | meta (46) | heterogeneity | High (分子机制/预后转移) | Subtype-stratified meta | Subtype meta |
| Cellular and molecular determinants of lymph node metastasis | 41421038 / 10.1016/j.compbiolchem.2025.108857 | PTC LNM | scRNA+ST+bulk | multi-omics+ML | LNM | FN1-SDC4 axis validated by ST; 17-gene LNM signature; random forest LNM model. | in vitro+ST | single-center | High (单细胞/空间组学/算法方法/分子机制) | Prospective FN1-SDC4 intervention | FN1-SDC4 trial |
| An integrated single-cell and spatial transcriptomic atlas o | 41480746 / 10.1172/jci.insight.191990 | WDTC/ATC/pediatric | 423,733 cells + ST | scRNA+ST | LNM/progression | POSTN+ myCAF associated with invasion, LNM, poor prognosis (42.3万 cells). | multi-institutional ST | rare subtypes small | High (单细胞/空间组学) | Therapeutic targeting of myCAF | myCAF targeting |
| A multi-molecular predictive model for lymph node metastasis | 41656803 / 10.11817/j.issn.1672-7347.2025.250216 | PTC | TCGA (507) | DESeq2/edgeR/Limma/WGCNA+LASSO+ML | LNM | 11-gene signature (incl. FN1) Model 2 AUC 0.802 train/0.793 val; stable across 6 ML algos. | TCGA val; sex-strat | TCGA only; no external | High (算法方法/分子机制/预后转移) | External multi-center validation | Externalize FN1-based model |
| DNA Methylation-Based Risk Stratification and Classification | 41701943 / 10.1158/1078-0432.CCR-25-2109 | pediatric TC | 2 cohorts methylation | methylation classifiers | invasiveness/LNM | Methylation classifiers predict tumor invasiveness (nodal mets) & driver mutations in pedi | independent val cohort | limited LNM samples | High (分子机制/预后转移) | Spatial epigenetics of invasion | Multi-omics pediatric atlas |
| Selective Use of Radioiodine Therapy in Differentiated Thyro | 41817109 / 10.1177/10507256261416869 | DTC | 3330 pts | Cox+IPTW | DSS/DFS | RAI not associated with overall DSS; >80% risk reduction in metastatic DTC. | population cohort | retrospective | Medium (预后转移) | Prospective RAI allocation | RAI trial |
| Development and validation of a machine learning model for p | 41877795 / 10.3389/fmed.2026.1790226 | DTC | 1245 pts | LASSO+ML (XGBoost) | distant metastatic recurrence | XGBoost AUC 0.88 (374-case external); 8 predictors incl BRAF V600E, sTg. | external val (374) | retrospective | High (算法方法/预后转移) | Prospective external validation | Prospective DTC-DM |
| PKM2-Mediated Glycolytic Reprogramming in Thyroid Cancer: Me | 42280115 / 10.3390/molecules31111811 | TC | review | review | glycolysis | Reviews PKM2 glycolytic reprogramming in TC. | review | review | Medium (代谢重编程/分子机制) | PKM2 inhibitor trials in TC | PKM2 trials |
| MGST1 drives lymph node metastasis in papillary thyroid carc | 42327722 / 10.3389/fimmu.2026.1848083 | PTC | TCGA/GTEx+cohort+scRNA | multi-omics+ML+pharm | LNM | Mito-high/immune-cold subtype; MGST1 core predictor AUC 0.833; MGST1 at dediff tip = stem- | external val+in vitro | single-center SC | High (代谢重编程/免疫微环境/分子机制/转移干性) | MGST1 targeted therapy trial | MGST1 targeted |

## What Is Already Known / 已知结论

**Axis 1 — 代谢–免疫耦合驱动淋巴结转移（LNM）。** 多条独立证据收敛：MGST1 定义的 'Mito-high'/immune-cold 亚群（42327722, AUC 0.833 外部验证）位于去分化轨迹终末、呈干性转移表型，其抑制可逆转免疫冷表型（Toxoflavin）；SHMT2 通过生成 SAM 甲基化 PTEN 启动子、激活 AKT 驱动 PTC 转移（38272883）；GLTC 结合 LDHA 阻断 SIRT5、促进 K155 琥珀酰化增强糖酵解与远处转移并致 RAI 耐药（37031273）；SOX12→YBX1→LDHA 启动子→TGF-β 轴驱动 PTC 转移（40593465）；空间多组学进一步定位精氨酸-多胺/糖酵解/脂质紊乱与 NAT8L/SVCT-2 等转移驱动代谢物（41398964）。

**Axis 2 — 转移干性亚群。** APOE− 肿瘤细胞亚群经 ABCA1-LXR 轴驱动宫颈 LNM 与不良预后（39810624）；MGST1 去分化终末对应干性转移表型（42327722）；ATC 中 ISG15 经 ISGylation 稳定 KPNA2 维持癌干细胞特性（37501099）；MTC 中 DLK1+ 细胞呈更高干性/球形成/染料外排（39595993）。单细胞分辨率一致指向「代谢重编程 + 干性」共标定转移起始克隆。

**Axis 3 — 成纤维细胞生态位（CAF niche）。** 整合单细胞与空间转录组图谱（41480746, 42.3 万细胞；39829764 预印本）定义 POSTN+ myCAF 紧邻侵袭性肿瘤细胞、与 LNM 及进展相关；空间图谱（41421038）以 FN1–SDC4 轴经空间转录组验证 LNM 机制并给出 17 基因签名与随机森林模型。

**Axis 4 — 影像/多组学 AI 预测高度拥挤。** LLNM-Net 多模态 DL（40750786, AUC 0.944，29,615 例/7 中心，超越人类专家）；CLAM-WSI 术中诊断（41237514, AUC 0.85 LNM）；影像组学+DL 融合（40771372 AUC 0.881 外部、39682228、40778281、41061579）；多组学+ML（38990290 四分子亚型、41421038）。元分析（39742800）汇 16 研究：DL sens 80.8%/spec 78.7% 优于手工影像组学。

**Axis 5 — BRAF V600E 与预后的解耦。** 46 研究/20,570 例荟萃（41419184）确认 BRAF V600E 仅关联淋巴结 OR 1.38 与复发 OR 1.56，**不**关联远处转移（OR 0.75）或死亡（OR 0.97）；提示 BRAF 状态对「淋巴结/复发」与「远处转移/死亡」是不同生物学过程，临床决策中不应作为独立远处转移预后标志。

## What Remains Unclear / 未解问题

- **机制→干预的因果链未闭合**：Axis 1–2 的代谢–免疫–干性轴多在 PTC 验证，APOE−/MGST1+ 亚群缺乏跨中心、跨亚型（尤其 ATC/MTC）的靶向干预证据；MGST1 的 Toxoflavin 仍为临床前。
- **空间分辨率不足**：空间组学仅 6–7 篇在域（41480746/41421038/41398964/39540244/37279258），ATC/MTC、远处转移灶的空间多组学几乎空白；多数单细胞研究为单中心。
- **DTC 远处转移 vs LNM 解耦未解释**：BRAF V600E（41419184）与 PD-L1 均与 LNM/复发相关但不预测远处转移——驱动远处转移的特异性分子（血行播散、器官趋向性）仍不明，仅 MTC 经 5-HT/NETs 肝脏趋向（39903533）给出线索。
- **算法端过拥挤且外推有限**：Axis 4 大量单中心回顾性 LLNM/CLNM 影像模型 AUC 集中 0.8–0.94，但缺乏前瞻性、成本效益与跨设备泛化；亚型/方法角度重叠严重。
- **预后签名缺乏独立外部验证**：多个基因/lncRNA/eRNA 预后模型（31792675/37934030/35033555/30942873）依赖 TCGA 单一来源，缺乏个体水平外部队列。

## Method/Data Limitations In The Field / 领域方法·数据局限

- **公共数据复用与批次效应**：TCGA/GEO 被绝大多数在域研究复用，跨平台批次效应与亚型分层不足。
- **外部验证缺失**：单细胞/空间研究多为单中心；AI 模型罕见前瞻性或多设备验证。
- **终点稀疏**：远处转移、ATC/MTC 亚型、儿童/青少年代谢–免疫轴样本量小，统计效能有限。
- **可重复性问题**：手工影像组学特征提取流程不一致；wet-lab 功能验证在多数预后/AI 研究中缺失。
- **MCP 工具限制**：paper-search-mcp `search_pubmed` 无日期过滤，且本轮再现瞬时 `not well-formed (invalid token)` 解析错误，需重发——已通过按查询重发解决，但不影响结论（均为相关性排序近似）。

## Candidate Future Directions / 候选未来方向

> 按 research-direction-rubric.md 的 1–5 七维评分（Novelty / Feasibility / Data availability / Validation strength / Clinical relevance / Method rigor / Overcrowding risk）。总分 28–35 强候选。

| Direction | Rationale | Feasibility | Required Data | Validation Plan | Main Risk | Claim Boundary | Rubric Total |
|---|---|---:|---|---|---|---|---:|
| **D3 — 定义并靶向 APOE−/MGST1+ 代谢–免疫干性转移亚群** | Axis1+2 收敛；多组学已定位 APOE− 与 MGST1 干性转移表型，但缺乏跨中心靶向干预 | 5 | TCGA+GTEx+scRNA/ST（已存在）+ 多中心组织/类器官 | 独立队列验证 APOE−/MGST1+ 富集→LNM；Toxoflavin/MGST1 抑制剂功能 rescue | 单中心 SC/ST 外推 | 不声称治愈，仅作为风险分层+可成药靶点的 hypothesis-generating | **32** |
| D-new — POSTN+ myCAF 生态位靶向（空间闭环） | 41480746 定义 myCAF 预测 LNM；与 APOE− 肿瘤互作待解 | 4 | 41480746 多中心 ST + 新增 ATC/MTC ST | 空间共定位验证 myCAF–肿瘤互作；CAF 耗竭/重编程 | CAF 异质性高 | 不直接声称生存获益 | **30** |
| D6 — MTC 5-HT/NETs 肝脏转移轴 | 39903533 给出器官趋向性机制+FDA 药 fluoxetine 阻断 | 4 | MTC 原发+肝转移队列（小） | 回顾+前瞻确认 NETs 与肝转移；SERT 阻断 | MTC 样本稀缺 | 限 MTC 肝转移亚群 | **27** |
| D7 — 线粒体 Ca2+/MCU 作为 LNM 节点 | 42510113（run#7 新增）连线粒体 Ca2+/OXPHOS/CD8+ T·NK | 4 | 现有 scRNA+新增流式 | 验证 SMDT1/MCU 与 LNM、CD8+ T 浸润 | 机制间接 | 折叠入 D3 而非独立 | **26** |
| D-ml — 新一代可解释多模态术前 LNM 预测 | 影像 AI 极度拥挤但可解释/前瞻性空缺 | 3 | 多中心 US/CT/MRI+WSI | 前瞻性+成本效益+跨设备 | 严重过拥挤（同质终点） | 仅算法改进，机制贡献弱 | **20** |

## Recommended Next Direction / 推荐下一步方向

**D3 — 定义并靶向 APOE−/MGST1+ 代谢–免疫干性转移亚群（rubric 总分 32，强候选，连续第 12 次确认）。**

理由：Axes 1–2 已从独立多组学研究（39810624 APOE−/ABCA1-LXR、42327722 MGST1 Mito-high/immune-cold、37501099 ISG15/KPNA2、40593465 SOX12–YBX1–LDHA）收敛到同一「代谢重编程 + 干性 + 免疫逃逸」表型；公开数据（TCGA/GTEx/scRNA/ST）与研究工具（多组学、空间、药理抑制）均已可用；MCP 平台期下，这是唯一兼具机制新颖度、证据强度与可成药性的方向，且未像影像 AI 那样严重过拥挤。

具体下一步：(1) 在 run#11/run#12 语料基础上，整合 APOE− 与 MGST1 签名，于独立多中心队列验证其 LNM/复发富集；(2) 用 Toxoflavin 或 MGST1 特异性抑制剂 + APOE 过表达做体内 rescue，闭合「代谢–免疫–干性」因果链；(3) 补 ATC/MTC 空间多组学以填补亚型空白。

Claim boundary：本报告不声称该亚群可「治愈」转移，仅作为风险分层与可成药靶点的 hypothesis-generating 证据；临床转化需独立外部验证。

## Follow-Up Reading List / 随访阅读清单

- **39810624** (APOE− subpopulation) — D3 核心机制与 13-gene LNM 签名，优先精读。
- **42327722** (MGST1 Mito-high/immune-cold) — D3 另一支柱，含 Toxoflavin 药理验证。
- **41480746** (POSTN+ myCAF atlas) — 空间 CAF 生态位，D-new 方向基础。
- **41421038** (FN1–SDC4 spatial multi-omics + ML) — 空间组学闭环 LNM 机制与模型。
- **39903533** (5-HT/NETs MTC liver mets) — D6 器官趋向性机制，MTC 远处转移稀缺线索。
- **41419184** (BRAF V600E meta, 46 studies) — 评估「淋巴结/复发 vs 远处转移」解耦的权威依据。
- **40750786** (LLNM-Net) — 若坚持算法方向，作为多模态 DL 的上限基线参考（过拥挤预警）。

## Reproducibility Notes / 可复现性说明

- Search date: 2026-08-03
- Databases: PubMed (via paper-search-mcp `search_pubmed`, DeferExecuteTool).
- Query strings: 9 路（a–i，见 Search Strategy 表）。
- Filters: max_results=15, sort=relevance（MCP 无日期过滤）。
- Deduplication rule: 按 PMID 去重；同一文献跨多路检索合并 queries 与 dimensions。
- Screening rule: 甲状腺（PTC/PTMC/FTC/MTC/ATC/儿童青少年）在域；乳腺/胃/结直肠/肝/HCC/胰腺/TNBC/泛癌/神经-免疫泛综述剔除（标记为 off-topic）。
- New-vs-prior: 与 run#11 基线（104 唯一 PMID）机械比对——**新增 0**；5 篇 run#11 掉出 15 行截断的非甲状腺记录本轮重新出现并仍排除，非新文献。
- Files saved:
  - 报告：`lit_review/literature_review_20260803_031443.md`
  - 原始+去重语料：`lit_review/search_results_latest.json`（130 raw / 104 unique / 76 in-scope / 28 excluded，含每篇 relevance+dimension+query 标签与 new_vs_run11 字段）
  - 生成脚本：`lit_review/_build_run12.py`、`lit_review/_gen_report_run12.py`

## Comparison With Prior Report / 与历史报告差异（vs run#11）

- **检索条数**：run#12 返回 130 条原始（run#11 为 114）→ 去重 104 唯一（同）；在域 76（run#11 为 75，因本轮将 2 篇历史甲状腺综述 17133106/17940185 正确归回在域）；排除 28（run#11 为 29）。
- **新增文献**：**0 篇**（连续第 6 个平台期 run#7→#12，其中 #8/#9/#10/#11/#12 均为 0 新增）。本次 5 篇 run#11 掉出 15 行相关性截断的非甲状腺记录（38981044 NSCLC、39615165 乳腺、40207795 胃、39903533 实际为 MTC 相关但本轮未在 15 行内、40855521 TNBC）重新出现，仍按非甲状腺排除，**不计入新信号**。
- **各维度分布（在域，多标签）**：分子机制 38 / 预后转移 31 / 代谢重编程 11 / 算法方法 18 / 免疫微环境 14 / 单细胞 12 / 空间组学 7 / 转移干性 5（run#11：46/22/10/20/15/13/6/3）。算法方法条目略降（单中心 AI 模型部分掉出截断），转移干性与空间组学略升（APOE− 与 42327722 多路命中）。
- **关键收敛发现**：5 个主轴**完全不变**；DTC 远处 vs LNM 解耦（BRAF V600E 荟萃 41419184 与 PD-L1 荟萃）再次确认。
- **推荐方向**：**D3 — 定义并靶向 APOE−/MGST1+ 代谢–免疫干性转移亚群**（rubric 总分 **32**，强候选）——连续第 12 次确认，无反证。
- **新信号/方向变化**：与 run#11 **相比无实质方向变化**；平台期建议（自 run#7 起反复提出）仍需落实——必须跳出 PubMed MCP：加入 bioRxiv/arXiv 预印本 + cBioPortal/DepMap + 收窄 ATC/MTC 与空间组学时间窗，并考虑将自动化频次由每日降为每周以节约配额。

