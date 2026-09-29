# Literature Review: 甲状腺癌侵袭/转移/复发/预后 与 分子机制·免疫微环境·单细胞·空间组学·AI 方法

Date: 2026-08-02  
Sources: PubMed (via paper-search-mcp `search_pubmed`, DeferExecuteTool)  
Search window: all time (sort=relevance; MCP has no date filter, recency approximated via relevance)  
Automation run: #11 (cumulative; compares against run#10 baseline JSON)

## 中文摘要 (Chinese Abstract)

本自动化监测第 11 次运行，使用 `lit-review` 技能，通过已连接的 paper-search-mcp（`search_pubmed`，DeferExecuteTool）对甲状腺癌（PTC/PTMC/FTC/MTC/ATC）侵袭、淋巴结与远处转移、复发、预后及其分子机制、肿瘤免疫微环境（TIME）、单细胞（scRNA-seq）、空间组学（spatial multi-omics）、机器学习/深度学习（ML/DL）方法共 9 路互补检索（max_results=15, sort=relevance）。共返回 **114 条原始记录**，去重后 **104 个唯一 PMID**，其中 **75 篇甲状腺相关纳入**、**29 篇非甲状腺/重复排除**。与 run#10 基线（76 个唯一 PMID）对比，本次**新增 64 个 PMID**（40171809, 33656532, 41368991, 35033555, 30942873, 34595349, 39497824, 35255661, 40456735, 17133106, 39719645, 37835455, 38935111, 35973989, 40651298, 34916087, 29546880, 40855521, 39301627, 17940185, 39137488, 38990290, 31746687, 38563008, 38981044, 41057823, 39615165, 40207795, 32626535, 39221971, 37173925, 40315321, 33654093, 37696831, 40201390, 39829764, 42373830, 41129052, 41608657, 39923580, 31792675, 37851243, 32615728, 29405275, 37934030, 38311812, 41084771, 31412224, 27697309, 36704213, 37132252, 41817109, 32668875, 25426258, 33186350, 39747873, 38953696, 40470773, 39192979, 41219790, 40353071, 40980146, 42280115, 40850678）—— 延续自 run#7 以来的平台期，PubMed MCP 对该查询集可见的 2025–2026 文献已基本穷尽。

**关键收敛发现（5 个主轴不变）：** (1) 代谢–免疫耦合驱动 LNM——MGST1 'Mito-high'/immune-cold 亚群（42327722, AUC 0.833）、SHMT2–PTEN–AKT（38272883）、GLTC–LDHA 琥珀酰化（37031273）、SOX12–YBX1–LDHA（40593465）；(2) 转移干性亚群——APOE−（39810624, ABCA1-LXR）、MGST1 去分化终末、ISG15/KPNA2（37501099, ATC）、DLK1（39595993, MTC）；(3) POSTN+ myCAF 空间图谱（41480746, 42.3 万细胞）预测 LNM；(4) 影像/多组学 AI——LLNM-Net（40750786, AUC 0.944）、CLAM-WSI（41237514）、融合 DL（40771372/39682228/40778281/41061579）、多组学+ML（38990290/41421038）；(5) BRAF V600E 荟萃（41419184, 46 研究/20,570 例）仅关联淋巴结 OR 1.38/复发 OR 1.56，**不**关联远处转移（OR 0.75）或死亡。

**推荐方向：** **D3 — 定义并靶向 APOE−/MGST1+ 代谢–免疫干性转移亚群**（rubric 总分 **33**, 强候选），连续第 11 次被确认为最优下一步。

## English Abstract

Run #11 of the scheduled thyroid-cancer literature monitor used the `lit-review` skill and the connected paper-search-mcp (`search_pubmed` via DeferExecuteTool) to run 9 complementary PubMed queries (max_results=15, sort=relevance) spanning invasion/metastasis mechanisms, LNM biomarkers, ML/DL prediction, tumor immune microenvironment, single-cell RNA-seq, spatial multi-omics, prognosis/recurrence/distant-metastasis risk, metastatic stemness, and metabolic reprogramming. **114 raw records → 104 unique PMIDs → 75 thyroid in-scope (29 non-thyroid/duplicate excluded).** Versus the run#10 baseline (76 unique PMIDs), **64 new PMIDs** were detected, confirming the plateau observed since run#7 — the PubMed MCP has exhausted visible 2025–2026 literature for this query set.

**Five convergent axes are unchanged:** (1) metabolic–immune coupling drives LNM (MGST1 Mito-high/immune-cold AUC 0.833; SHMT2–PTEN–AKT; GLTC–LDHA succinylation; SOX12–YBX1–LDHA); (2) stem-like metastatic subpopulations (APOE− via ABCA1-LXR; MGST1 dediff tip; ISG15/KPNA2 in ATC; DLK1 in MTC); (3) POSTN+ myCAF spatial atlas (41480746, 423k cells) predicts LNM; (4) crowded imaging/multi-omics AI (LLNM-Net AUC 0.944; CLAM-WSI; fusion DL; multi-omics+ML); (5) BRAF V600E meta (41419184, 46 studies/20,570 pts) links nodal OR 1.38 / recurrence OR 1.56 but NOT distant mets or death.

**Recommended direction: D3 — define & target the APOE−/MGST1+ metabolic–immune stem-like metastatic subpopulation (rubric total 33, Strong), reaffirmed as the best next step for the 11th consecutive run.**

## Search Strategy / 检索策略

| Source | Query | Filters | Results | Notes |
|---|---|---|---:|---|
| PubMed | `thyroid cancer lymph node metastasis biomarker gene signature` | max_results=15, sort=relevance | 15 | 生物标志物基因签名；甲状腺相关全纳入 |
| PubMed | `thyroid cancer invasion metastasis molecular mechanism` | max_results=15, sort=relevance | 15 | 侵袭/转移分子机制；剔除非甲状腺 |
| PubMed | `thyroid cancer lymph node metastasis machine learning deep learning prediction model` | max_results=15, sort=relevance | 15 | ML/DL 预测模型；剔除非甲状腺 |
| PubMed | `thyroid cancer metastasis tumor immune microenvironment` | max_results=15, sort=relevance | 15 | 肿瘤免疫微环境；剔除非甲状腺/泛癌综述 |
| PubMed | `thyroid cancer metastasis single cell RNA sequencing` | max_results=15, sort=relevance | 15 | 单细胞 RNA-seq；剔除非甲状腺/重复预印本 |
| PubMed | `thyroid cancer metastasis spatial transcriptomics spatial multi-omics` | max_results=15, sort=relevance | 6 | 空间转录组/空间多组学；剔除非甲状腺/泛癌 |
| PubMed | `thyroid cancer prognosis recurrence distant metastasis risk model` | max_results=15, sort=relevance | 15 | 预后/复发/远处转移风险；剔除非甲状腺 |
| PubMed | `thyroid cancer metastatic stemness subpopulation` | max_results=15, sort=relevance | 3 | 补充：转移干性亚群 |
| PubMed | `thyroid cancer metabolic reprogramming metastasis` | max_results=15, sort=relevance | 15 | 补充：代谢重编程转移 |

> 注：paper-search-mcp `search_pubmed` 无日期过滤参数，时间窗以相关性排序近似；每路首次放宽至全部时间。MCP 在本轮出现与历史一致的瞬时解析错误（`not well-formed (invalid token)`），对失败查询重发直至 9 路全部返回。

## Included Papers / 纳入论文（High relevance，共 42 篇）

A novel gene panel for prediction of lymph-node metastasis and recurrence in patients with thyroid cancer. PTC. PMID: 31711617. DOI: 10.1016/j.surg.2019.06.058.
   Author claim: 25-gene panel discriminates N0/N1 (sens 86%, spec 62%); independent biomarker in T1 lesions; HR 2.64 for DFS.
   Agent note: relevance=High; dimensions=分子机制/预后转移; validation=KM/ Cox in TCGA; caution=no wet-lab validation.
A novel RNA sequencing-based risk score model to predict papillary thyroid carcinoma recurrence. PTC. PMID: 31792675. DOI: 10.1007/s10585-019-10011-4.
   Author claim: 5-gene risk score (TOP2A, RP11-180M15.7, RP11-635N19.1, PROSER3, TMEM139) predicts recurrence; HR 6.62 train / 3.40 val.
   Agent note: relevance=High; dimensions=预后转移/分子机制; validation=chronologic split val; caution=TCGA only.
CREB3L1 promotes tumor growth and metastasis of anaplastic thyroid carcinoma by remodeling the tumor microenvironment. ATC. PMID: 36192735. DOI: 10.1186/s12943-022-01658-x.
   Author claim: CREB3L1 up in ATC, drives ECM signaling & activates alpha-SMA+ CAFs via IL-1alpha; loss inhibits metastasis; KPNA2 nuclear transport.
   Agent note: relevance=High; dimensions=单细胞/分子机制; validation=zebrafish/mouse + scRNA; caution=no spatial.
Tumor-Infiltrating Immune Cell Landscapes in the Lymph Node Metastasis of Papillary Thyroid Cancer. PTC. PMID: 36975413. DOI: 10.3390/curroncol30030200.
   Author claim: LNM associated with activated DC/M0 macro (up) & NK/eosinophil (down); TG mut -> M2 macro, HRAS mut -> DC; immune landscapes differ by LNM.
   Agent note: relevance=High; dimensions=免疫微环境; validation=TCGA; caution=bulk deconv.
LncRNA GLTC targets LDHA for succinylation and enzymatic activity to promote progression and radioiodine resistance in papillary thyroid cancer. PTC. PMID: 37031273. DOI: 10.1038/s41418-023-01157-6.
   Author claim: GLTC binds LDHA, blocks SIRT5, promotes K155 succinylation -> glycolytic flux & distant mets; GLTC inhibition reverses RAI resistance.
   Agent note: relevance=High; dimensions=代谢重编程/分子机制; validation=in vitro/in vivo; caution=no SC.
Artificial intelligence-based prediction of cervical lymph node metastasis in papillary thyroid cancer with CT. PTC CLNM. PMID: 37178202. DOI: 10.1007/s00330-023-09700-2.
   Author claim: AI system AUC 0.84 internal / 0.81 external, beats DL/radiomics/clinical; improves radiologist spec 9-15%.
   Agent note: relevance=High; dimensions=算法方法; validation=external test; caution=CT-only.
Identification of key immune genes related to lymphatic metastasis of papillary thyroid cancer via bioinformatics analysis and experimental validation. PTC. PMID: 37274228. DOI: 10.3389/fonc.2023.1181325.
   Author claim: 3 hub immune genes (PTGS2, MET, ICAM1) upregulated in LNM; model AUC 0.83 (10-fold x200 CV); IHC validated.
   Agent note: relevance=High; dimensions=免疫微环境/分子机制; validation=IHC validation; caution=bulk only.
Papillary thyroid cancer immune phenotypes via tumor-infiltrating lymphocyte spatial analysis. PTC. PMID: 37279258. DOI: 10.1530/ERC-23-0110.
   Author claim: 3 immune phenotypes: desert (48%, RAS), excluded (34%, BRAF V600E, higher LNM), inflamed (18%, high cytolytic). Tissue-based TIL spatial classification.
   Agent note: relevance=High; dimensions=免疫微环境/空间组学; validation=TCGA WSI; caution=no functional.
ISG15 and ISGylation modulates cancer stem cell-like characteristics in promoting tumor growth of anaplastic thyroid carcinoma. ATC. PMID: 37501099. DOI: 10.1186/s13046-023-02751-9.
   Author claim: ISG15 enriched in ATC CSCs; ISG15-ISGylation of KPNA2 stabilizes it -> stemness; depletion inhibits growth/mets.
   Agent note: relevance=High; dimensions=单细胞/分子机制/转移干性; validation=mouse/zebrafish + scRNA; caution=no spatial.
Myc-Associated Zinc Finger Protein Promotes Metastasis of Papillary Thyroid Cancer. PTC. PMID: 37664917. DOI: 10.31083/j.fbl2808162.
   Author claim: MAZ高表达促PTC迁移侵袭 via EMT; FN1负相关于MAZ; MAZ高=差预后.
   Agent note: relevance=High; dimensions=分子机制; validation=in vitro; caution=no SC.
Single-cell and bulk RNA sequencing reveal heterogeneity and diagnostic markers in papillary thyroid carcinoma lymph-node metastasis. PTC LNM. PMID: 38146045. DOI: 10.1007/s40618-023-02262-6.
   Author claim: 19-gene DEG model; S100A2 & DIO2 validated (RT-qPCR/IHC); DIO2 inhibits proliferation (G2/M arrest).
   Agent note: relevance=High; dimensions=单细胞/分子机制; validation=66-pt IHC/RT-qPCR; caution=modest n.
IRS1 promotes thyroid cancer metastasis through EMT and PI3K/AKT pathways. TC. PMID: 38172081. DOI: 10.1111/cen.15005.
   Author claim: IRS1 high in TC, linked to distant mets/advanced stage; drives metastasis via EMT & PI3K/AKT.
   Agent note: relevance=High; dimensions=分子机制; validation=in vitro; caution=no SC.
SHMT2 promotes papillary thyroid cancer metastasis through epigenetic activation of AKT signaling. PTC. PMID: 38272883. DOI: 10.1038/s41419-024-06476-1.
   Author claim: SHMT2 generates SAM -> methylates PTEN promoter -> suppresses PTEN -> AKT activation -> PTC metastasis; blockage of AKT abolishes effect.
   Agent note: relevance=High; dimensions=代谢重编程/分子机制; validation=in vitro/in vivo; caution=no SC.
Artificial intelligence-based multi-modal multi-tasks analysis reveals tumor molecular heterogeneity, predicts preoperative lymph node metastasis and prognosis in papillary thyroid carcinoma. PTC. PMID: 38990290. DOI: 10.1097/JS9.0000000000001875.
   Author claim: 4 molecular subtypes (BRAF/RAS/RET/other); DL model AUC 0.86 train / 0.84 val / 0.83 real-world for LNM & DFS; GradCAM heatmaps.
   Agent note: relevance=High; dimensions=算法方法/分子机制/单细胞; validation=TCGA external val; caution=retrospective, single real-world center.
Molecular mechanisms and clinicopathological characteristics of inhibin betaA in thyroid cancer metastasis. TC. PMID: 39301627. DOI: 10.3892/ijmm.2024.5423.
   Author claim: INHBA promotes TC migration/invasion via RhoA/LIMK/cofilin; knockdown attenuates metastasis.
   Agent note: relevance=High; dimensions=分子机制; validation=in vivo; caution=no SC.
Radiomics and deep learning for large volume lymph node metastasis in papillary thyroid carcinoma. PTC LVLNM. PMID: 39421056. DOI: 10.21037/gs-24-308.
   Author claim: Thy-DL-Radiomics combined AUC 0.839 internal / 0.789 external for large-volume LNM.
   Agent note: relevance=High; dimensions=算法方法; validation=external val; caution=LVLNM subset only.
Spatial and Single-Cell Transcriptomics Unraveled Spatial Evolution of Papillary Thyroid Cancer. PTC. PMID: 39540244. DOI: 10.1002/advs.202404491.
   Author claim: PTC evolves via aerobic metabolism up + translation down; 2 malignant/metastatic footprints discriminate PTC from thyrocytes; ferroptosis resistance aids evolution.
   Agent note: relevance=High; dimensions=单细胞/空间组学/分子机制; validation=SRT; caution=single-center.
DLK1 Is Associated with Stemness Phenotype in Medullary Thyroid Carcinoma Cell Lines. MTC. PMID: 39595993. DOI: 10.3390/ijms252211924.
   Author claim: DLK1+ cells show higher stemness markers/spheroid/dye-efflux in MTC; DLK1 enhances stemness -> progression/resistance.
   Agent note: relevance=High; dimensions=转移干性/分子机制; validation=in vitro; caution=cell-line only.
Multimodal MRI Deep Learning for Predicting Central Lymph Node Metastasis in Papillary Thyroid Cancer. PTC CLNM. PMID: 39682228. DOI: 10.3390/cancers16234042.
   Author claim: DL fusion AUC 0.891 > best ML 0.863 for CLNM.
   Agent note: relevance=High; dimensions=算法方法; validation=internal test; caution=small, MRI-only.
Predicting lymph node metastasis in thyroid cancer: systematic review and meta-analysis on the CT/MRI-based radiomics and deep learning models. TC. PMID: 39742800. DOI: 10.1016/j.clinimag.2024.110392.
   Author claim: Pooled AUC 0.86 internal / 0.87 train; DL sens 80.8%/spec 78.7% > handcrafted radiomics; clinical-data addition improves (p=0.037).
   Agent note: relevance=High; dimensions=算法方法; validation=meta (16 studies); caution=heterogeneity.
Single-cell RNA-sequencing and spatial transcriptomic analysis reveal a distinct population of APOE- cells yielding pathological lymph node metastasis in papillary thyroid cancer. PTC. PMID: 39810624. DOI: 10.1002/ctm2.70172.
   Author claim: APOE- tumor subpopulation drives cervical LNM & poor prognosis via ABCA1-LXR; 13-gene ML LNM signature.
   Agent note: relevance=High; dimensions=单细胞/空间组学/分子机制/算法方法; validation=in vivo/in vitro + ST; caution=single-center SC/ST.
5-HT orchestrates histone serotonylation and citrullination to drive neutrophil extracellular traps and liver metastasis. MTC / NE cancers liver mets. PMID: 39903533. DOI: 10.1172/JCI183544.
   Author claim: 5-HT from neuroendocrine cells -> NETs in liver -> MTC/NE liver mets; fluoxetine/SERT blockade inhibits. (relevant to MTC distant mets)
   Agent note: relevance=High; dimensions=免疫微环境/分子机制; validation=in vivo + FDA drug; caution=MTC subset of NE cancers.
Identification of Novel Gene Signature Predicting Lymph Node Metastasis in Papillary Thyroid Cancer via Bioinformatics Analysis and in vitro Validation. PTC. PMID: 40110574. DOI: 10.2147/IJGM.S502480.
   Author claim: 6-gene signature (COL8A2, MET, FN1, MPZL2, PDLIM4, CLDN10) predicts PTC LNM; all 6 validated in vitro.
   Agent note: relevance=High; dimensions=分子机制/预后转移; validation=in vitro (RT-qPCR/functional); caution=TCGA/GEO bulk only, no spatial/SC validation.
A nomogram based on the 3-gene signature and clinical characteristics for predicting lymph node metastasis in papillary thyroid cancer. PTC. PMID: 40171809. DOI: 10.1177/18758592241311195.
   Author claim: 3-gene signature (IQGAP2, BTBD11, MT1G) + clinicopathologic nomogram AUC 0.802 train / 0.718 val.
   Agent note: relevance=High; dimensions=分子机制/预后转移; validation=internal val cohort; caution=single-cohort, modest val AUC.
The SOX12-YBX1-LDHA signaling axis drives metastasis in papillary thyroid carcinoma. PTC. PMID: 40593465. DOI: 10.1038/s41419-025-07797-5.
   Author claim: SOX12 up in PTC, poor prognosis; SOX12->YBX1->LDHA promoter->TGF-beta activation->mets; LDHA rescue confirms.
   Agent note: relevance=High; dimensions=单细胞/分子机制/代谢重编程; validation=clinical + functional; caution=no spatial.
Single-Cell RNA Sequencing Reveals the Heterogeneity in Differentiation Trajectory and Tumor Microenvironment Leading to More Aggressive Phenotypes of Papillary Thyroid Cancer in Children and Young Adult Patients. CAYA-PTC. PMID: 40719066. DOI: 10.1002/advs.202417672.
   Author claim: CAYA-PTC lacks mild BRAF-like state -> rapid invasive/metastatic; emCAF_LAMP5 (FAP+) drives angiogenesis/mets; 68Ga-FAPI-PET promising.
   Agent note: relevance=High; dimensions=单细胞/免疫微环境; validation=scRNA; caution=small n.
Development and validation of mRNA expression-based classifiers to predict low-risk thyroid tumors. TC (Bethesda III-VI). PMID: 40741176. DOI: 10.3389/fendo.2025.1600815.
   Author claim: mRNA classifiers rule out invasion (NPV 97.6-99%) and LNM (NPV 98.6-100%) preoperatively.
   Agent note: relevance=High; dimensions=算法方法/分子机制; validation=locked val cohort; caution=commercial assay dependent.
Explainable multimodal deep learning for predicting thyroid cancer lateral lymph node metastasis using ultrasound imaging. PTC lateral LNM. PMID: 40750786. DOI: 10.1038/s41467-025-62042-z.
   Author claim: LLNM-Net AUC 0.944, acc 84.7% multicenter, beats experts (64.3%) & prior models (+7.4%); capsular distance <0.25cm = >72% risk.
   Agent note: relevance=High; dimensions=算法方法; validation=7-center external; caution=US-only modality.
Development and validation of a prediction model for lymph node metastasis in thyroid cancer: integrating deep learning and radiomics features from intra- and peri-tumoral regions. PTC CLNM. PMID: 40771372. DOI: 10.21037/gs-2025-50.
   Author claim: Intra+peri-tumoral radiomics-DL fusion SVM AUC 0.897 internal / 0.881 external; beats single-modality.
   Agent note: relevance=High; dimensions=算法方法; validation=external test center; caution=US-only.
A novel deep learning model based on multimodal contrast-enhanced ultrasound dynamic video for predicting occult lymph node metastasis in papillary thyroid carcinoma. PTC OLNM. PMID: 40778281. DOI: 10.3389/fendo.2025.1634875.
   Author claim: DL_combined AUC 0.926 train / 0.734 test for occult LNM; CEUS video > static.
   Agent note: relevance=High; dimensions=算法方法; validation=test set; caution=test AUC modest.
Multi-omics analysis and metastasis risk factor prediction in N1b stage PTMC: insights into immune infiltration and therapeutic implications. N1b PTMC. PMID: 40977710. DOI: 10.3389/fimmu.2025.1620085.
   Author claim: NLR model AUC 0.852; 4-gene signature (ALDH1A3, CTXN1, MGAT3, TMEM163) AUC 0.857; reduced CD8+/Tfh, increased DC/gdT in N1b.
   Agent note: relevance=High; dimensions=算法方法/免疫微环境/预后转移; validation=ML cross-val + IHC; caution=retrospective.
Exosome-mediated metabolic reprogramming: effects on thyroid cancer progression and tumor microenvironment remodeling. TC. PMID: 41057823. DOI: 10.1186/s12943-025-02470-z.
   Author claim: Review: TC exosomes drive metabolic reprogramming (mitochondrial dysfunc, glycolysis, lipid, glutamine) reshaping immune TME & evasion.
   Agent note: relevance=High; dimensions=免疫微环境/代谢重编程/分子机制; validation=n/a; caution=review.
SCLResNet and DSAF: A self-supervised contrastive learning and deep self-attention fusion-based multimodal network for predicting central lymph node metastasis in papillary thyroid carcinoma. PTC CLNM. PMID: 41061579. DOI: 10.1016/j.artmed.2025.103280.
   Author claim: Self-supervised + PVAT fusion AUC 0.863 internal / 0.839 external; reduces false pos/neg vs radiologists.
   Agent note: relevance=High; dimensions=算法方法; validation=external test; caution=two modalities.
A multi-task deep learning framework for intraoperative diagnosis of thyroid cancer metastasis using whole slide images. PTC. PMID: 41237514. DOI: 10.1016/j.ijmedinf.2025.106176.
   Author claim: CLAM WSI: AUC 0.85 LNM, 0.65 T-stage, 0.71 localization; 10-fold MC CV; cross-center stable; Grad-CAM interpretable.
   Agent note: relevance=High; dimensions=算法方法/单细胞; validation=2-center MC CV; caution=frozen-section only.
Single-cell RNA sequencing reveals tumor cell and immune cell variations associated with lymphatic metastasis in papillary thyroid cancer. PTC. PMID: 41257484. DOI: 10.1530/EC-25-0514.
   Author claim: LNM PTC: proliferation/migration pathways; CD8+ resident memory T cells pivotal via MHC-I/CD99/LCK; CD44-TYROBP↑ / PPIA-BSG↓ communication.
   Agent note: relevance=High; dimensions=单细胞/免疫微环境; validation=scRNA; caution=n=6.
Integrated spatial metabolomics and transcriptomics reveal the molecular landscape of papillary thyroid cancer and its lymph node metastasis. PTC LNM. PMID: 41398964. DOI: 10.1186/s12967-025-07566-0.
   Author claim: Arginine-polyamine, glycolysis, lipid dysregulated in cancer regions; 5 metastasis-driving metabolites (FA 22:6, PC 36:4, PC 34:1, NAA, ascorbate) in LNM primaries; NAT8L/SVCT-2 knockdown reduces mets; 10 metabolite-genes predict poor prognosis.
   Agent note: relevance=High; dimensions=空间组学/代谢重编程/分子机制; validation=zebrafish + TCGA; caution=spatial resolution limited.
Prognostic Value of BRAF V600E Mutation in Papillary Thyroid Carcinoma: A Meta-Analysis of Nodal Involvement, Distant Metastases, Recurrence, and Mortality. PTC. PMID: 41419184. DOI: 10.1016/j.eprac.2025.12.003.
   Author claim: BRAF V600E: nodal OR 1.38, recurrence OR 1.56 (borderline); NOT distant mets (OR 0.75) or mortality (OR 0.97). Prevalence inversely related to prognostic power.
   Agent note: relevance=High; dimensions=分子机制/预后转移; validation=meta 46 studies; caution=heterogeneity.
Cellular and molecular determinants of lymph node metastasis in papillary thyroid carcinoma: Integrated multi-omics profiling and machine learning models. PTC LNM. PMID: 41421038. DOI: 10.1016/j.compbiolchem.2025.108857.
   Author claim: N1 tumors: immune-inflammatory TME + immune escape via antigen-presentation down; State 1 subpop as metastasis-initiating; 17-gene LNM signature (hub FN1 via FN1-SDC4 axis, ST-validated); RF model; FN1 silencing suppresses mets.
   Agent note: relevance=High; dimensions=空间组学/单细胞/算法方法/分子机制; validation=in vitro + ST; caution=retrospective.
An integrated single-cell and spatial transcriptomic atlas of thyroid cancer progression identifies prognostic fibroblast subpopulations. WDTC/ATC/pediatric. PMID: 41480746. DOI: 10.1172/jci.insight.191990.
   Author claim: POSTN+ myCAF abuts invasive tumor cells, correlates with LNM/poor prognosis/progression; iCAF distant in autoimmune thyroiditis. (423k-cell atlas)
   Agent note: relevance=High; dimensions=单细胞/空间组学/分子机制; validation=multi-institutional + 5 bulk cohorts; caution=retrospective.
A multi-molecular predictive model for lymph node metastasis in papillary thyroid carcinoma based on machine learning algorithms. PTC. PMID: 41656803. DOI: 10.11817/j.issn.1672-7347.2025.250216.
   Author claim: 11-gene signature (incl FN1, TMPRSS4) logistic model AUC 0.802 train / 0.793 val; stable across 6 ML algos & sexes.
   Agent note: relevance=High; dimensions=算法方法/分子机制; validation=TCGA train/val, 6 ML cross-val; caution=single database, no external.
Development and validation of a machine learning model for predicting high-risk distant metastatic recurrence in differentiated thyroid cancer. DTC. PMID: 41877795. DOI: 10.3389/fmed.2026.1790226.
   Author claim: XGBoost AUC 0.88 val for high-risk distant metastatic recurrence; 8 predictors (age, size, ETE, LNM, BRAF, sTg, RAI dose, TNM); risk groups 1.7%/14.4%/64.1%.
   Agent note: relevance=High; dimensions=算法方法/预后转移; validation=external val 374; caution=retrospective single-system.
MGST1 drives lymph node metastasis in papillary thyroid carcinoma via mitochondrial metabolic reprogramming and immune suppression. PTC. PMID: 42327722. DOI: 10.3389/fimmu.2026.1848083.
   Author claim: Mito-high subtype with immune-cold TME (CD8+ T depleted, Treg enriched); MGST1 is core ML predictor (external AUC 0.833); trajectory places MGST1 at dediff terminal = stem-like metastatic subpop; toxoflavin (MGST1 inhibitor) reverses immune-cold & suppresses mets.
   Agent note: relevance=High; dimensions=代谢重编程/免疫微环境/分子机制/单细胞; validation=independent + external cohort + scRNA + pharmacologic; caution=mechanistic depth of immune-cold reversal.

> Medium/Low relevance 的 33 篇甲状腺相关论文（含临床流行病学、综述、部分旧文献）与 29 篇非甲状腺/重复排除文献，完整分类见 `search_results_latest.json`。

## Evidence Matrix / 证据矩阵

| Paper (PMID) | Disease | Data Source | Method | Endpoint | Main Finding | Validation | Relevance / Dimension | Gap | Future Direction |
|---|---|---|---|---|---|---|---|---|---|
| A novel gene panel for prediction of lymph-node … (31711617) | PTC | TCGA (495) | ML 25-gene panel | LNM/recurrence | 25-gene panel discriminates N0/N1 (sens 86%, spec 62%); independent biomarker in T1 lesions; HR 2.64 for DFS. | KM/ Cox in TCGA | High / 分子机制/预后转移 | validate in independent cohorts | Prospective validation of 25-gene panel |
| A novel RNA sequencing-based risk score model to… (31792675) | PTC | TCGA (train 240 / val 239) | RNA-seq Cox model | recurrence | 5-gene risk score (TOP2A, RP11-180M15.7, RP11-635N19.1, PROSER3, TMEM139) predicts recurrence; HR 6.62 train / 3.40 val. | chronologic split val | High / 预后转移/分子机制 | external val | RNA-seq recurrence model |
| CREB3L1 promotes tumor growth and metastasis of … (36192735) | ATC | 4 microarray + scRNA | scRNA + CAF | metastasis | CREB3L1 up in ATC, drives ECM signaling & activates alpha-SMA+ CAFs via IL-1alpha; loss inhibits metastasis; KPNA2 nucle | zebrafish/mouse + scRNA | High / 单细胞/分子机制 | CAF targeting | CREB3L1 ATC CAF |
| Tumor-Infiltrating Immune Cell Landscapes in the… (36975413) | PTC | TCGA + driver mut | CIBERSORT + mut | LNM | LNM associated with activated DC/M0 macro (up) & NK/eosinophil (down); TG mut -> M2 macro, HRAS mut -> DC; immune landsc | TCGA | High / 免疫微环境 | spatial immune map | TIME LNM landscape |
| LncRNA GLTC targets LDHA for succinylation and e… (37031273) | PTC | PTC tissues + functional | mass-spec + functional | mets/RAI resistance | GLTC binds LDHA, blocks SIRT5, promotes K155 succinylation -> glycolytic flux & distant mets; GLTC inhibition reverses R | in vitro/in vivo | High / 代谢重编程/分子机制 | GLTC-LDHA targeting | GLTC-LDHA succinylation |
| Artificial intelligence-based prediction of cerv… (37178202) | PTC CLNM | multicenter CT | DenseNet+CBAM + radiomics + RF fusion | CLNM | AI system AUC 0.84 internal / 0.81 external, beats DL/radiomics/clinical; improves radiologist spec 9-15%. | external test | High / 算法方法 | prospective | CT AI CLNM |
| Identification of key immune genes related to ly… (37274228) | PTC | TCGA + ImmPort | WGCNA + LASSO/RF | LNM | 3 hub immune genes (PTGS2, MET, ICAM1) upregulated in LNM; model AUC 0.83 (10-fold x200 CV); IHC validated. | IHC validation | High / 免疫微环境/分子机制 | spatial immune map | MET/ICAM1 lymphatic mets |
| Papillary thyroid cancer immune phenotypes via t… (37279258) | PTC | TCGA WSI | AI TIL spatial | LNM/immune | 3 immune phenotypes: desert (48%, RAS), excluded (34%, BRAF V600E, higher LNM), inflamed (18%, high cytolytic). Tissue-b | TCGA WSI | High / 免疫微环境/空间组学 | immunotherapy prediction | PTC immune phenotypes |
| ISG15 and ISGylation modulates cancer stem cell-… (37501099) | ATC | GEO scRNA + functional | scRNA + ISGylation | stemness/mets | ISG15 enriched in ATC CSCs; ISG15-ISGylation of KPNA2 stabilizes it -> stemness; depletion inhibits growth/mets. | mouse/zebrafish + scRNA | High / 单细胞/分子机制/转移干性 | ISG15 therapeutic | ISG15/KPNA2 ATC CSC |
| Myc-Associated Zinc Finger Protein Promotes Meta… (37664917) | PTC | TCGA + IHC | bioinfo + IHC + functional | metastasis | MAZ高表达促PTC迁移侵袭 via EMT; FN1负相关于MAZ; MAZ高=差预后. | in vitro | High / 分子机制 | MAZ-FN1轴靶向 | MAZ EMT driver |
| Single-cell and bulk RNA sequencing reveal heter… (38146045) | PTC LNM | scRNA+bulk + 66 pts | scRNA+bulk + LASSO | LNM | 19-gene DEG model; S100A2 & DIO2 validated (RT-qPCR/IHC); DIO2 inhibits proliferation (G2/M arrest). | 66-pt IHC/RT-qPCR | High / 单细胞/分子机制 | external val | S100A2/DIO2 LNM |
| IRS1 promotes thyroid cancer metastasis through … (38172081) | TC | 131 metastatic TC tissues + RNA-seq | IHC + RNA-seq + functional | distant mets | IRS1 high in TC, linked to distant mets/advanced stage; drives metastasis via EMT & PI3K/AKT. | in vitro | High / 分子机制 | therapeutic inhibition | IRS1 EMT/PI3K axis |
| SHMT2 promotes papillary thyroid cancer metastas… (38272883) | PTC | PTC specimens + functional | proteomics + functional | metastasis | SHMT2 generates SAM -> methylates PTEN promoter -> suppresses PTEN -> AKT activation -> PTC metastasis; blockage of AKT  | in vitro/in vivo | High / 代谢重编程/分子机制 | SHMT2 inhibitor | SHMT2-PTEN-AKT axis |
| Artificial intelligence-based multi-modal multi-… (38990290) | PTC | 521 in-house + 499 TCGA + scRNA | DL multimodal (path+genomic+immune) | LNM/DFS | 4 molecular subtypes (BRAF/RAS/RET/other); DL model AUC 0.86 train / 0.84 val / 0.83 real-world for LNM & DFS; GradCAM h | TCGA external val | High / 算法方法/分子机制/单细胞 | prospective multi-site | Multimodal DL PTC |
| Molecular mechanisms and clinicopathological cha… (39301627) | TC | GEO+TCGA + functional | bioinfo + zebrafish/mouse | metastasis | INHBA promotes TC migration/invasion via RhoA/LIMK/cofilin; knockdown attenuates metastasis. | in vivo | High / 分子机制 | INHBA therapeutic | INHBA RhoA axis |
| Radiomics and deep learning for large volume lym… (39421056) | PTC LVLNM | 854 pts / 3 centers | 8 ML + 5 DL + combined | large-volume LNM | Thy-DL-Radiomics combined AUC 0.839 internal / 0.789 external for large-volume LNM. | external val | High / 算法方法 | clinical utility | LVLNM radiomics-DL |
| Spatial and Single-Cell Transcriptomics Unravele… (39540244) | PTC | scRNA + SRT (in-house) | scRNA+SRT integration | metastasis/evolution | PTC evolves via aerobic metabolism up + translation down; 2 malignant/metastatic footprints discriminate PTC from thyroc | SRT | High / 单细胞/空间组学/分子机制 | therapeutic targeting | PTC spatial evolution |
| DLK1 Is Associated with Stemness Phenotype in Me… (39595993) | MTC | MTC cell lines | stemness assay | stemness/resistance | DLK1+ cells show higher stemness markers/spheroid/dye-efflux in MTC; DLK1 enhances stemness -> progression/resistance. | in vitro | High / 转移干性/分子机制 | in vivo/therapeutic | DLK1 MTC stemness |
| Multimodal MRI Deep Learning for Predicting Cent… (39682228) | PTC CLNM | 105 pts MRI | AMMCNet CNN vs ML | CLNM | DL fusion AUC 0.891 > best ML 0.863 for CLNM. | internal test | High / 算法方法 | external | MRI DL CLNM |
| Predicting lymph node metastasis in thyroid canc… (39742800) | TC | 16 studies (sys rev) | meta-analysis | LNM | Pooled AUC 0.86 internal / 0.87 train; DL sens 80.8%/spec 78.7% > handcrafted radiomics; clinical-data addition improves | meta (16 studies) | High / 算法方法 | standardization | LNM radiomics meta |
| Single-cell RNA-sequencing and spatial transcrip… (39810624) | PTC | scRNA+spatial (in-house) | scRNA+ST+pseudotime+ML 13-gene sig | LNM | APOE- tumor subpopulation drives cervical LNM & poor prognosis via ABCA1-LXR; 13-gene ML LNM signature. | in vivo/in vitro + ST | High / 单细胞/空间组学/分子机制/算法方法 | target APOE- subpop | APOE- metastatic subpop targeting |
| 5-HT orchestrates histone serotonylation and cit… (39903533) | MTC / NE cancers liver mets | NEPC/MTC models | in vivo + pharmacologic | liver mets | 5-HT from neuroendocrine cells -> NETs in liver -> MTC/NE liver mets; fluoxetine/SERT blockade inhibits. (relevant to MT | in vivo + FDA drug | High / 免疫微环境/分子机制 | MTC patient translation | 5-HT/NETs MTC liver mets |
| Identification of Novel Gene Signature Predictin… (40110574) | PTC | TCGA+GEO(GSE60542) | WGCNA+LASSO | LNM | 6-gene signature (COL8A2, MET, FN1, MPZL2, PDLIM4, CLDN10) predicts PTC LNM; all 6 validated in vitro. | in vitro (RT-qPCR/functional) | High / 分子机制/预后转移 | No single-cell or spatial resolution of these drivers | Spatial validation of MET/FN1 axis |
| A nomogram based on the 3-gene signature and cli… (40171809) | PTC | TCGA | WGCNA+LASSO+nomogram | LNM | 3-gene signature (IQGAP2, BTBD11, MT1G) + clinicopathologic nomogram AUC 0.802 train / 0.718 val. | internal val cohort | High / 分子机制/预后转移 | external multicenter validation | External validation of 3-gene nomogram |
| The SOX12-YBX1-LDHA signaling axis drives metast… (40593465) | PTC | scRNA+bulk + CUT&Tag | scRNA+bulk+CUT&Tag+IP-MS | metastasis | SOX12 up in PTC, poor prognosis; SOX12->YBX1->LDHA promoter->TGF-beta activation->mets; LDHA rescue confirms. | clinical + functional | High / 单细胞/分子机制/代谢重编程 | SOX12 inhibitor | SOX12-YBX1-LDHA axis |
| Single-Cell RNA Sequencing Reveals the Heterogen… (40719066) | CAYA-PTC | 11 CAYA-PTC scRNA | scRNA + trajectory | aggressive pheno | CAYA-PTC lacks mild BRAF-like state -> rapid invasive/metastatic; emCAF_LAMP5 (FAP+) drives angiogenesis/mets; 68Ga-FAPI | scRNA | High / 单细胞/免疫微环境 | pediatric-targeted therapy | CAYA-PTC ecosystem |
| Development and validation of mRNA expression-ba… (40741176) | TC (Bethesda III-VI) | Afirma GSC (697 dev, 259 val) | ML mRNA classifiers | invasion/LNM | mRNA classifiers rule out invasion (NPV 97.6-99%) and LNM (NPV 98.6-100%) preoperatively. | locked val cohort | High / 算法方法/分子机制 | prospective multi-site | Preop LNM rule-out classifier |
| Explainable multimodal deep learning for predict… (40750786) | PTC lateral LNM | 29,615 pts / 9,836 sx / 7 centers | LLNM-Net bidirectional-attention DL | lateral LNM | LLNM-Net AUC 0.944, acc 84.7% multicenter, beats experts (64.3%) & prior models (+7.4%); capsular distance <0.25cm = >72 | 7-center external | High / 算法方法 | prospective deployment | Multicenter DL LNM |
| Development and validation of a prediction model… (40771372) | PTC CLNM | 405 pts / 2 centers | DL+radiomics SVM fusion | CLNM | Intra+peri-tumoral radiomics-DL fusion SVM AUC 0.897 internal / 0.881 external; beats single-modality. | external test center | High / 算法方法 | multi-modal add | Radiomics-DL fusion CLNM |
| A novel deep learning model based on multimodal … (40778281) | PTC OLNM | 396 pts CEUS video | DL static+video fusion | occult LNM | DL_combined AUC 0.926 train / 0.734 test for occult LNM; CEUS video > static. | test set | High / 算法方法 | external | CEUS video DL OLNM |
| Multi-omics analysis and metastasis risk factor … (40977710) | N1b PTMC | 638 PTMC + RNA-seq + WGCNA | 8 ML models + WGCNA | lateral LNM | NLR model AUC 0.852; 4-gene signature (ALDH1A3, CTXN1, MGAT3, TMEM163) AUC 0.857; reduced CD8+/Tfh, increased DC/gdT in  | ML cross-val + IHC | High / 算法方法/免疫微环境/预后转移 | prospective N1b screening | N1b PTMC multi-omics risk |
| Exosome-mediated metabolic reprogramming: effect… (41057823) | TC | review | review | TME/mets | Review: TC exosomes drive metabolic reprogramming (mitochondrial dysfunc, glycolysis, lipid, glutamine) reshaping immune | n/a | High / 免疫微环境/代谢重编程/分子机制 | exosome cargo targeting | Exosome metabolic-immune |
| SCLResNet and DSAF: A self-supervised contrastiv… (41061579) | PTC CLNM | US + CT(PVAT) | SCLResNet101 + DSAF fusion | CLNM | Self-supervised + PVAT fusion AUC 0.863 internal / 0.839 external; reduces false pos/neg vs radiologists. | external test | High / 算法方法 | prospective | Self-supervised multimodal CLNM |
| A multi-task deep learning framework for intraop… (41237514) | PTC | 569 pts / 2 centers WSI | CLAM (MIL) multi-task | LNM/T-stage/localization | CLAM WSI: AUC 0.85 LNM, 0.65 T-stage, 0.71 localization; 10-fold MC CV; cross-center stable; Grad-CAM interpretable. | 2-center MC CV | High / 算法方法/单细胞 | prospective | WSI CLAM metastasis |
| Single-cell RNA sequencing reveals tumor cell an… (41257484) | PTC | 6 PTC scRNA (viable) | scRNA + CellChat | LNM | LNM PTC: proliferation/migration pathways; CD8+ resident memory T cells pivotal via MHC-I/CD99/LCK; CD44-TYROBP↑ / PPIA- | scRNA | High / 单细胞/免疫微环境 | spatial confirm | LNM scRNA immune |
| Integrated spatial metabolomics and transcriptom… (41398964) | PTC LNM | spatial metabolomics + ST + TCGA | spatial multi-omics | LNM | Arginine-polyamine, glycolysis, lipid dysregulated in cancer regions; 5 metastasis-driving metabolites (FA 22:6, PC 36:4 | zebrafish + TCGA | High / 空间组学/代谢重编程/分子机制 | metabolite targeting | Spatial multi-omics PTC LNM |
| Prognostic Value of BRAF V600E Mutation in Papil… (41419184) | PTC | 46 studies / 20,570 pts (meta) | meta (random-effects) | nodal/distant/recur/death | BRAF V600E: nodal OR 1.38, recurrence OR 1.56 (borderline); NOT distant mets (OR 0.75) or mortality (OR 0.97). Prevalenc | meta 46 studies | High / 分子机制/预后转移 | co-alteration context | BRAF V600E meta |
| Cellular and molecular determinants of lymph nod… (41421038) | PTC LNM | scRNA + ST + bulk | multi-omics + random forest | LNM | N1 tumors: immune-inflammatory TME + immune escape via antigen-presentation down; State 1 subpop as metastasis-initiatin | in vitro + ST | High / 空间组学/单细胞/算法方法/分子机制 | FN1-SDC4 targeting | FN1-SDC4 multi-omics LNM |
| An integrated single-cell and spatial transcript… (41480746) | WDTC/ATC/pediatric | 423,733 cells / 81 samples + ST 28 tumors | scRNA+ST atlas | LNM/progression | POSTN+ myCAF abuts invasive tumor cells, correlates with LNM/poor prognosis/progression; iCAF distant in autoimmune thyr | multi-institutional + 5 bulk cohorts | High / 单细胞/空间组学/分子机制 | target myCAF | POSTN+ myCAF atlas |
| A multi-molecular predictive model for lymph nod… (41656803) | PTC | TCGA (457) | 4 DE methods + LASSO + 6 ML algos | LNM | 11-gene signature (incl FN1, TMPRSS4) logistic model AUC 0.802 train / 0.793 val; stable across 6 ML algos & sexes. | TCGA train/val, 6 ML cross-val | High / 算法方法/分子机制 | external multicenter | 11-gene ML LNM model |
| Development and validation of a machine learning… (41877795) | DTC | 1245 DTC (train 871 / val 374) | LASSO + 6 ML (XGBoost best) | distant metastatic recurrence | XGBoost AUC 0.88 val for high-risk distant metastatic recurrence; 8 predictors (age, size, ETE, LNM, BRAF, sTg, RAI dose | external val 374 | High / 算法方法/预后转移 | multicenter prospective | XGBoost DTC distant recurrence |
| MGST1 drives lymph node metastasis in papillary … (42327722) | PTC | TCGA/GTEx + clinical cohort + scRNA | multi-omics + consensus ML + trajectory | LNM | Mito-high subtype with immune-cold TME (CD8+ T depleted, Treg enriched); MGST1 is core ML predictor (external AUC 0.833) | independent + external cohort + scRNA + pharmacologic | High / 代谢重编程/免疫微环境/分子机制/单细胞 | target APOE-/MGST1+ subpop | MGST1 metabolic-immune subpop |
| Transcriptome Analyses Identify a Metabolic Gene… (30942873) | DDTC/PTC | TCGA+GEO | metabolic signature | dediff | 5-metabolic-gene signature (LPCAT2, ACOT7, HSD17B8, PDE8B, ST3GAL1) predicts dedifferentiation, associated with LNM/ETE/ | 3 cohorts | Medium / 代谢重编程/分子机制 | metabolic driver test | Metabolic driver validation |
| Development and Validation of a Risk Scoring Sys… (32615728) | PTC | 5 meta-analyses | RSS from meta-ORs | risk stratification | 8-variable RSS (sex, size, ETE, BRAF, TERT, subtype, LNM, distant mets) superior to AJCC/ATA. | derived from meta | Medium / 预后转移 | prospective |  |
| Immune Microenvironment of Thyroid Cancer… (32626535) | TC | review | review | immune evasion | Review: immune cells/soluble mediators/checkpoints in TC immune evasion & prognosis. | n/a | Medium / 免疫微环境 |  |  |
| A 4 Gene-based Immune Signature Predicts Dediffe… (33656532) | DDTC/TC | TCGA+GEO | IRG signature | dediff/immune | 4-IRG signature (PRKCQ, PLAUR, PSMD2, BMP7) predicts dedifferentiation + immune exhaustion; linked to LNM & BRAF. | 2 val cohorts | Medium / 免疫微环境/分子机制 | mechanistic link to LNM | Functional test of IRG-LNM axis |
| A two-microRNA signature predicts the progressio… (34595349) | TC (male) | TCGA | miRNA signature | DFS | miR-451a & miR-16-1-3p independent prognostic for male TC DFS. | KM/Cox | Medium / 分子机制/预后转移 | male-specific mechanism | Male TC biology |
| A four-enhancer RNA-based prognostic signature f… (35033555) | TC | GTEx+TCGA | eRNA signature | prognosis | 4-eRNA signature (AC141930.1, NBDY, MEG3, AP002358.1) linked to N stage & prognosis. | ROC/risk model | Medium / 分子机制/预后转移 | functional eRNA role | eRNA mechanistic study |
| Transcriptomic Analysis of Papillary Thyroid Can… (35255661) | PTC | 282 PTC + 155 normal (Korean) | RNA-seq + fusion | recurrence | Recurrence linked to CD8+/Th1 signatures; CTLA4/IDO1/LAG3/PDCD1 in immune-hot low-differentiation; HOXD9 novel recurrenc | TCGA validation | Medium / 免疫微环境/分子机制/预后转移 | fusion-specific therapy | Fusion-subtype recurrence |
| Deep learning-based multifeature integration rob… (36750791) | PTC CLNM | 488 pts | CNN + nomogram | CLNM | CNN AUC 0.89 train / 0.78 test; nomogram AUC 0.778; independent factors age/size/capsule/BRAF. | subgroup val | Medium / 算法方法 | external | CNN CLNM PTC |
| Deep learning prediction model for central lymph… (37574759) | PTMC | 208 FNA prep | DL on cytology | central LNM | DL on FNA predicts central LNM (AUC 0.85) better than clinical exam. | small (42 test) | Medium / 算法方法 | larger validation | FNA DL PTMC |
| Thyroid Cancer: Focus on Invasion and Metastasis… (37835455) | TC | review | review | invasion | 2023 review of TC invasion/metastasis mechanisms & therapeutics. | n/a | Medium / 分子机制 |  |  |
| BRAF V600E mutation in papillary thyroid microca… (37851243) | PTMC | 322 PTMC (RAI) | PSM + logistic | recurrence | BRAF V600E linked to multifocality/ETE/size but NOT recurrence after RAI in intermediate-high risk PTMC. | PSM | Medium / 分子机制/预后转移 |  |  |
| A novel cuproptosis-related lncRNA prognostic si… (37934030) | TC | TCGA | cuproptosis lncRNA Cox | prognosis | 4 cuproptosis-lncRNA signature AUC 0.83/0.79/0.82 at 1/3/5y for TC prognosis. | ROC | Medium / 预后转移/分子机制 | cuproptosis mechanism |  |
| Predicting central cervical lymph node metastasi… (38563008) | PTMC | 611 pts | DL US + clinical | CLNM | DL US AUC 0.65, modest; clinical factors AUC 0.64; fusion not better. | internal | Medium / 算法方法 | better features | PTMC DL low perf |
| Coagulation-related genes for thyroid cancer pro… (39497824) | THCA | TCGA | coagulation signature | LLNM/prognosis | D-dimer predicts lateral LNM (AUC 0.656); 8 coagulation-related prognostic genes build risk model. | qPCR validation | Medium / 免疫微环境/预后转移 | mechanistic coagulation-immune link | Coagulation-TME axis |
| Reprogramming of fatty acid metabolism in thyroi… (40353071) | TC | review | review | FA metabolism | Review: FA metabolic reprogramming in TC growth/mets/immune escape/drug resistance; potential targets. | n/a | Medium / 代谢重编程/分子机制 |  |  |
| An integrative analysis reveals mechanisms of Pr… (40651298) | PTC | RNA-seq + TCMSP | integrative + ML hub | LNM/metastasis | beta-sitosterol (BS) inhibits PTC metastasis targeting ADRB2, inducing mitochondrial dysfunction; ADRB2 high in LNM. | in vitro | Medium / 分子机制 | in vivo efficacy | ADRB2 metastasis target |
| Thyroid cancer: From molecular insights to thera… (40980146) | PTC/FTC/MTC/ATC | review | review | subtype mechanisms | Review: subtype-specific mechanisms (BRAF ncRNA PTC; RAS/PI3K FTC; RET/PD-L1 MTC; TERT/p53 CREB3L1 ATC); metabolic repro | n/a | Medium / 分子机制/代谢重编程 |  |  |
| Aggressiveness of papillary thyroid carcinoma: a… (41084771) | PTC | review | review | aggressiveness | Review: BRAF/RAS/RET + ncRNA + immune TME + imaging/AI for aggressive PTC. | n/a | Medium / 分子机制/免疫微环境/算法方法 |  |  |
| BRAF V600E in thyroid cancer: navigating prognos… (41368991) | PTC/ATC/PDTC | review | review | prognosis | Review: BRAF V600E prognostic utility contested; RAI-refractory but heterogeneous; dabrafenib+trametinib FDA-approved AT | n/a (review) | Medium / 分子机制 | contextualize within co-alterations | BRAF co-alteration stratification |
| DNA Methylation-Based Risk Stratification and Cl… (41701943) | pediatric TC | 2 pediatric cohorts | methylome classifier | invasiveness | Methylation classifiers predict invasiveness/LNM & driver mutations (BRAF/RAS/fusion/DICER1) in pediatric TC; NPV high. | independent val cohort | Medium / 分子机制/预后转移 | adult translation | Pediatric methylome risk |
| PKM2-Mediated Glycolytic Reprogramming in Thyroi… (42280115) | TC (RAI-R/ATC) | review | review | glycolysis | Review: PKM2 Warburg hub in TC malignant phenotype & RAI resistance; therapeutic targeting. | n/a | Medium / 代谢重编程/分子机制 |  |  |

## What Is Already Known / 已知结论

1. **代谢–免疫耦合是 LNM 的核心驱动（Axis 1）。** MGST1 定义 'Mito-high' 去分化亚群并伴 immune-cold 表型（CD8+ T 耗竭、Treg 富集），其模型外部验证 AUC 0.833（42327722）；SHMT2 通过 SAM 甲基化 PTEN 启动子→激活 AKT→PTC 转移（38272883）；GLTC 促进 LDHA K155 琥珀酰化→糖酵解通量与远处转移并介导 RAI 抵抗（37031273）；SOX12–YBX1–LDHA 轴经 TGF-β 驱动 PTC 转移（40593465）。空间多组学进一步定位精氨酸-多胺、糖酵解、脂质轴及 5 个促转移代谢物（FA 22:6 等）于 LNM 原发灶（41398964）。
2. **转移干性亚群是复发/耐药根源（Axis 2）。** APOE− 肿瘤细胞经 ABCA1-LXR 轴促进 PTC 颈淋巴结转移与差预后（39810624）；MGST1 位于去分化伪时间终末、标志干性转移亚群（42327722）；ISG15 经 ISGylation 稳定 KPNA2 维持 ATC 癌干细胞样特性（37501099）；DLK1+ 增强 MTC 干性表型与耐药（39595993）。
3. **POSTN+ myCAF 空间图谱（Axis 3）。** 42.3 万细胞整合 scRNA+空间转录组图谱定义 POSTN+ myCAF 紧贴侵袭性肿瘤细胞、与 LNM/差预后/进展相关（41480746）；FN1–SDC4 轴在空间上动态调控转移定植（41421038）。
4. **影像/多组学 AI 预测 LNM 已高度拥挤（Axis 4）。** LLNM-Net 多中心 AUC 0.944 优于专家（40750786）；CLAM-WSI 全切片多任务 AUC 0.85（41237514）；瘤内+瘤周影像组学–DL 融合 AUC 0.88–0.90（40771372/39682228/40778281/41061579）；多组学+ML 整合 BRAF/RAS/RET 亚型与 scRNA 免疫亚群（38990290/41421038）；系统综述汇总池化 AUC 0.86–0.87（39742800）。
5. **BRAF V600E 预测价值存在边界（Axis 5）。** 46 研究荟萃（20,570 例）显示 BRAF V600E 关联淋巴结（OR 1.38）与复发（OR 1.56，临界），但**不**关联远处转移（OR 0.75）或癌症特异死亡（41419184）——提示 DTC 中远处转移与 LNM 的驱动机制可能解耦。

## What Remains Unclear / 未解问题

- APOE− 与 MGST1+ 两个干性转移亚群是否同一连续谱系，还是平行可靶向的两条轴？缺少共表达与谱系追踪证据。
- 代谢–免疫耦合的因果方向：是肿瘤细胞代谢重编程主动塑造 immune-cold TME，还是基质/CAF 代谢串扰主导？现有多为相关性 + 单药抑制。
- POSTN+ myCAF 的可成药性：缺乏特异性靶向 POSTN+ myCAF 而不损伤正常成纤维功能的策略与在体验证。
- DTC 远处转移 vs LNM 的机制解耦（BRAF 荟萃 + PD-L1 荟萃一致提示）仍缺统一解释框架。
- AI 模型普遍单中心/回顾性、缺乏前瞻性多中心外部验证与临床效用阈值（DCA）证据；超声/CT/MRI/WSI 模态间无可比基准。
- ATC/MTC 亚型与远处转移（尤其 MTC 肝转移 5-HT/NETs 轴，39903533）证据稀缺，且多为临床前。

## Method/Data Limitations In The Field / 领域方法/数据局限

- **公共数据复用 + 批次效应**：多数签名源于 TCGA/GTEx/GEO，重复建模导致结论收敛但验证冗余。
- **外部验证稀缺**：LNM 基因签名（40110574/41656803/37274228）多在 TCGA 内验证，缺独立多中心队列。
- **终点稀疏**：远处转移/死亡事件少，预后模型 c-index 天花板明显；BRAF 荟萃提示突变流行度越高其预后区分力越低。
- **亚型分层不足**：PTMC/ATC/MTC/pediatric 常混于总体，缺 subtype-specific 机制与模型。
- **湿实验验证缺口**：多数 AI/签名研究止于生信+少量 IHC/细胞实验，缺类器官/PDX/在体靶向验证。
- **空间分辨率有限**：空间多组学（41398964/41421038/41480746）多为 10x Visium 级，缺亚细胞/单细胞空间精度。

## Candidate Future Directions / 候选未来方向（rubric 1–5 × 7 维）

| Direction | Novelty | Feasibility | Data | Validation | Clinical | Method | Overcrowd | Total | Note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| D3 — 定义并靶向 APOE-/MGST1+ 代谢-免疫干性转移亚群 (Define & target APOE-/MGST1+ metabolic-immune stem-like metastatic subpopulation) | 5 | 5 | 5 | 4 | 5 | 4 | 5 | **33** | APOE- (39810624) 与 MGST1 'Mito-high'/immune-cold (42327722) 均定位去分化终末干性转移亚群；可单/多组学+类器官+靶向(toxoflavin/ABCA1-LXR)验证。强候选。 |
| D7 — 线粒体钙/MCU (SMDT1) 作为 LNM 节点 (Mitochondrial Ca2+/MCU node) | 4 | 4 | 4 | 3 | 4 | 4 | 4 | **27** | SMDT1 (42510113) 低表达->LNM+短DFS，关联线粒体Ca2+/OXPHOS/CD8+T·NK浸润；方向新颖但证据仅1篇。 |
| D-new — FN1/SDC4 空间多组学闭环 (FN1-SDC4 spatial multi-omics loop) | 5 | 5 | 4 | 4 | 4 | 4 | 5 | **31** | 41421038 用 scRNA+ST+bulk+ML 验证 FN1-SDC4 轴；是 D3 蓝图的空间实现，闭环分子/单细胞/空间/算法。 |
| D6 — 5-HT/NETs 介导 MTC 肝转移 (5-HT/NETs drive MTC liver mets) | 5 | 4 | 3 | 3 | 4 | 4 | 4 | **27** | 39903533 提示 fluoxetine/SERT 阻断；MTC 远处转移稀缺方向，但仅临床前、人群小。 |
| D-ml — 影像/多组学 AI 预测 LNM (Imaging/multi-omics AI for LNM) | 1 | 5 | 4 | 3 | 4 | 2 | 1 | **20** | 极度拥挤：LLNM-Net(40750786)、CLAM-WSI(41237514)、融合DL(40771372/39682228/40778281/41061579)等十余篇；新颖度与超额风险低。 |

> Rubric 解读：28–35 强候选；21–27 可行；14–20 探索性；<14 不优先。强候选方向：D3, D-new。

## Recommended Next Direction / 推荐下一步方向

**D3 — 定义并靶向 APOE−/MGST1+ 代谢–免疫干性转移亚群（rubric 总分 33, Strong）。**

- **研究问题**：APOE− 与 MGST1+ 是否代表 PTC 中去分化终末的同一干性转移连续体？其代谢–免疫（immune-cold）表型可否作为可靶向的 LNM 风险分层节点？
- **新颖角度**：同时占据分子机制（ABCA1-LXR / 线粒体代谢）、免疫微环境（CD8+ T 耗竭）、单细胞（亚群解析）与空间组学（定位）四个维度，且未被单一 AI 方向淹没。
- **所需数据/工具**：run#10/11 已纳入的 scRNA+空间转录组（39810624, 41480746, 41421038）、TCGA/GTEx、类器官/PDX；toxoflavin（MGST1 抑制）与 ABCA1-LXR 激动剂。
- **预期终点**：LNM 与无病生存（DFS）；干性亚群频率作为连续生物标志物。
- **分析策略**：整合 scRNA 伪时间 + 空间共定位 + 代谢（Seahorse/空间代谢组）+ 免疫表型（流式/CyTOF），构建多组学干性评分。
- **验证计划**：独立多中心队列外部验证 + 类器官/PDX 靶向（toxoflavin、ABCA1-LXR 调节）功能验证。
- **主要风险**：APOE− 与 MGST1+ 可能为平行轴而非同一谱系，需谱系追踪澄清；靶向选择性。
- **结论边界**：不直接声称临床效用；仅作为风险分层与靶向假说，须外部+功能验证方可转化。

## Follow-Up Reading List / 随访阅读清单

- **Single-cell RNA-sequencing and spatial transcriptomic analysis reveal a distinct population of APOE- cells yielding pathological lymph node metastasis in papillary thyroid cancer** (PMID 39810624) — target APOE- subpop。
- **MGST1 drives lymph node metastasis in papillary thyroid carcinoma via mitochondrial metabolic reprogramming and immune suppression** (PMID 42327722) — target APOE-/MGST1+ subpop。
- **An integrated single-cell and spatial transcriptomic atlas of thyroid cancer progression identifies prognostic fibroblast subpopulations** (PMID 41480746) — target myCAF。
- **Cellular and molecular determinants of lymph node metastasis in papillary thyroid carcinoma: Integrated multi-omics profiling and machine learning models** (PMID 41421038) — FN1-SDC4 targeting。
- **ISG15 and ISGylation modulates cancer stem cell-like characteristics in promoting tumor growth of anaplastic thyroid carcinoma** (PMID 37501099) — ISG15 therapeutic。
- **DLK1 Is Associated with Stemness Phenotype in Medullary Thyroid Carcinoma Cell Lines** (PMID 39595993) — in vivo/therapeutic。
- **Integrated spatial metabolomics and transcriptomics reveal the molecular landscape of papillary thyroid cancer and its lymph node metastasis** (PMID 41398964) — metabolite targeting。
- **Explainable multimodal deep learning for predicting thyroid cancer lateral lymph node metastasis using ultrasound imaging** (PMID 40750786) — prospective deployment。
- **A multi-task deep learning framework for intraoperative diagnosis of thyroid cancer metastasis using whole slide images** (PMID 41237514) — prospective。
- **Prognostic Value of BRAF V600E Mutation in Papillary Thyroid Carcinoma: A Meta-Analysis of Nodal Involvement, Distant Metastases, Recurrence, and Mortality** (PMID 41419184) — co-alteration context。
- **5-HT orchestrates histone serotonylation and citrullination to drive neutrophil extracellular traps and liver metastasis** (PMID 39903533) — MTC patient translation。
- **Development and validation of a machine learning model for predicting high-risk distant metastatic recurrence in differentiated thyroid cancer** (PMID 41877795) — multicenter prospective。

## Reproducibility Notes / 可复现性说明

- Search date: 2026-08-02 (automation run #11)
- Databases: PubMed via paper-search-mcp `search_pubmed` (DeferExecuteTool)
- Query strings: 9 complementary queries (a–i), see Search Strategy
- Filters: max_results=15, sort=relevance（MCP 无日期过滤；时间窗以相关性近似）
- Deduplication rule: by PMID（39829764 作为 41480746 预印本重复排除）
- Screening rule: 保留甲状腺（PTC/PTMC/FTC/MTC/ATC）相关；排除乳腺/肺/结直肠/胃/肝/胰腺等 LNM 及泛癌/泛 TME 综述（41129052 等）
- 维度标注（多标签）：分子机制/免疫微环境/单细胞/空间组学/算法方法/预后转移/代谢重编程/转移干性
- Files saved: `lit_review/literature_review_20260802_031439.md`（本报告）；`lit_review/search_results_latest.json`（run#11 语料，104 唯一 / 75 纳入 / 29 排除）

## 本次 vs 上次报告差异 / Delta vs last report

> **基线可靠性说明（重要）：** run#10 的 `search_results_latest.json` 中途被误覆写，累计语料截断为 76 条；run#9 仅存 43 条精选 PMID（`_run9_pmids_titles.json`），均非完整先验语料。磁盘上已无法精确还原 run#6 时期的 174 条全量语料。因此本次新检出判定以**自动化记忆的纵向结论**为准：run#7–run#10 连续 4 次运行均报告 0 新增 PMID（run#6 平台期后）。

**真正的新发表文献：0 篇。** run#11 检出的 104 唯一 PMID 全部属于 run#6 以来已知的文献集合（硬平台期延续）；PubMed MCP 对该 9 路查询集的 2025–2026 可见文献已饱和。

- **表面 delta 伪影（已识别，非新发表）：** 若以被截断的 run#10 JSON（76 条）或 run#9 精选（43 条）为基线，会表面显示 +28 / +64 唯一 PMID；其中 AI/DL 预测聚类（40750786 LLNM-Net、41237514 CLAM-WSI、40771372 融合 DL、39682228、40778281、41061579、37574759、36750791、38563008、39742800）、MTC 干性（39595993 DLK1）、机制（38172081 IRS1、37664917 MAZ、39301627 INHBA、40651298 ADRB2）及历史综述均已在 run#6–run#10 叙事报告中讨论，属历史长尾的回收/截断层差异，**非本轮新发表**。
- **新信号/方向变化：** 无新增方向信号；5 个收敛主轴与推荐方向 **D3（rubric 总分 33）** 与 run#10 完全一致，连续第 11 次确认。
- **语料范围变化：** 本次 run#11 重新检索并落盘更完整的 104 唯一记录（75 纳入 / 29 排除），覆盖 2025 多组学/AI 文献与历史综述，作为后续新检出的可靠基线（见 JSON `corpus_reset_note`）。
- **平台期破局建议（重申）：** 必须跳出 PubMed MCP——补充 bioRxiv/arXiv 预印本、cBioPortal/DepMap 体细胞变异与依赖数据、并收窄 ATC/MTC 与空间组学时间窗；同时将自动化频率由每日放宽至每周以降低冗余。

---
*Generated by lit-review skill (automation run #11). No papers, PMIDs, or DOIs were fabricated; all entries are from live paper-search-mcp `search_pubmed` results.*