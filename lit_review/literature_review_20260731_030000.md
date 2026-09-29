# Literature Review: 甲状腺癌侵袭·淋巴结与远处转移·复发·预后及分子机制/肿瘤免疫微环境/单细胞与空间组学/机器学习方法 (Thyroid Cancer Invasion, Lymph-Node & Distant Metastasis, Recurrence, Prognosis, Molecular Mechanisms, Tumor Immune Microenvironment, Single-Cell & Spatial Omics, and Machine/Deep Learning Methods)

Date: 2026-07-31
Sources: PubMed (via `paper-search-mcp` MCP, `DeferExecuteTool::mcp__paper-search-mcp__search_pubmed`)
Search window: all time; `sort=relevance` (`max_results=15`). *Note:* the PubMed MCP exposes no date filter, so recency was approximated via relevance ranking. The cumulative corpus is at a documented hard plateau (see Reproducibility Notes / Comparison).

---

## 中文摘要 (Chinese Abstract)

本次为甲状腺癌文献定期监测自动化的第 9 次执行（run#9）。我们沿用 `lit-review` 技能，通过已连接的 `paper-search-mcp` MCP 真实检索了 9 路互补 PubMed 查询（a–i，覆盖淋巴结转移 biomarker/基因签名、侵袭转移分子机制、ML/DL 预测、肿瘤免疫微环境、单细胞 RNA-seq、空间多组学、预后/复发/远处转移风险模型，以及补充的转移干性亚群与代谢重编程），全部使用 `sort=relevance`、`max_results=15`。**全部返回文献均已在 run#8 语料库中（174 unique / 103 甲状腺 in-scope / 71 排除），本次净新增 0 篇**，连续第三次确认 Plateau（run#7 +2 → run#8 +0 → run#9 +0）。

在稳定收敛的 5 条证据轴上，本领域的结论高度一致：(1) **代谢–免疫耦合驱动淋巴结转移（LNM）**——MGST1「Mito-high/免疫冷」亚型（AUC 0.833）、SHMT2、GLTC–LDHA、SOX12–YBX1–LDHA、LCN2 等；(2) **干性转移亚群**——APOE− 细胞（经 ABCA1–LXR）、MGST1 去分化终末、ISG15/KPNA2（ATC）、DLK1（MTC）、lncRNA ROR/MALAT1（CD133+ ATC）；(3) **POSTN+ myCAF 空间图谱**（423,733 细胞）预测 LNM；(4) **拥挤的影像/多组学 AI**——LLNM-Net（AUC 0.944，优于专家）、CLAM-WSI、融合 DL/影像组学等；(5) **BRAF V600E 荟萃分析**（46k 患者）提示淋巴结 OR 1.38 / 复发 OR 1.56，但**不**预测远处转移或死亡，与 PD-L1 荟萃形成「DTC 远处转移 vs LNM 解耦」格局。

**推荐方向 D3**（定义并靶向 APOE−/MGST1+ 代谢–免疫干性转移亚群）以 rubric 总分 **32（Strong）** 获第 9 次连续确认。为打破 Plateau，建议下一步扩展 PubMed 之外的数据源（bioRxiv/arXiv 预印本、cBioPortal/DepMap）并收窄 ATC/MTC 与空间组学时间窗。

## English Abstract

This is the 9th execution (run#9) of the scheduled thyroid-cancer literature monitoring automation. Following the `lit-review` skill, we ran 9 complementary PubMed queries (a–i) through the connected `paper-search-mcp` MCP (`sort=relevance`, `max_results=15`), covering LNM biomarker/gene signatures, invasion–metastasis mechanisms, ML/DL prediction, tumor immune microenvironment, scRNA-seq, spatial multi-omics, prognosis/recurrence/distant-metastasis risk models, plus two supplemental queries on metastatic stemness subpopulations and metabolic reprogramming. **Every returned PMID was already in the run#8 corpus (174 unique / 103 thyroid in-scope / 71 excluded); net new = 0**, confirming a hard plateau for the 3rd consecutive run (run#7 +2 → run#8 +0 → run#9 +0).

Five convergent evidence axes remain stable: (1) **metabolic–immune coupling drives LNM** (MGST1 "Mito-high"/immune-cold subtype, AUC 0.833; SHMT2; GLTC–LDHA; SOX12–YBX1–LDHA; LCN2); (2) **stem-like metastatic subpopulations** (APOE− via ABCA1–LXR; MGST1 dedifferentiation tip; ISG15/KPNA2 in ATC; DLK1 in MTC; lncRNA ROR/MALAT1 in CD133+ ATC); (3) **POSTN+ myCAF spatial atlas** (423,733 cells) predicting LNM; (4) **crowded imaging/multi-omics AI** (LLNM-Net AUC 0.944 > experts; CLAM-WSI; fusion DL/radiomics); (5) **BRAF V600E meta-analysis** (46k patients) linking nodal OR 1.38 / recurrence OR 1.56 but **not** distant metastasis or death, mirroring a PD-L1 meta and supporting "DTC distant-metastasis vs LNM decoupling."

**Recommended direction D3** (define & target the APOE−/MGST1+ metabolic–immune stem-like metastatic subpopulation) is reaffirmed for the 9th consecutive run at rubric total **32 (Strong)**. To break the plateau, future runs should extend beyond PubMed MCP (bioRxiv/arXiv preprints, cBioPortal/DepMap) and narrow the ATC/MTC and spatial-omics window.

---

## 检索策略 (Search Strategy)

| Source | Query | Filters | max_results | Sort | Results (raw) | In-scope (thyroid) |
|---|---|---|---:|---|---:|---:|
| PubMed (MCP) | a. `thyroid cancer lymph node metastasis biomarker gene signature` | none (MCP no date filter) | 15 | relevance | 15 | 15 |
| PubMed (MCP) | b. `thyroid cancer invasion metastasis molecular mechanism` | none | 15 | relevance | 15 | 11 (+4 off-topic) |
| PubMed (MCP) | c. `thyroid cancer lymph node metastasis machine learning deep learning prediction model` | none | 15 | relevance | 15 (2 transient parse errors, retried) | 12 (+3 off-topic) |
| PubMed (MCP) | d. `thyroid cancer metastasis tumor immune microenvironment` | none | 15 | relevance | 15 | 10 (+5 off-topic) |
| PubMed (MCP) | e. `thyroid cancer metastasis single cell RNA sequencing` | none | 15 | relevance | 15 | 11 (+4 off-topic) |
| PubMed (MCP) | f. `thyroid cancer metastasis spatial transcriptomics spatial multi-omics` | none | 15 | relevance | 15 | 7 (+8 off-topic) |
| PubMed (MCP) | g. `thyroid cancer prognosis recurrence distant metastasis risk model` | none | 15 | relevance | 15 | 10 (+5 off-topic) |
| PubMed (MCP) | h. `thyroid cancer metastasis cancer stem cell stemness subpopulation` *(supplemental)* | none | 15 | relevance | 4 | 1 (+3 off-topic) |
| PubMed (MCP) | i. `thyroid cancer metastasis metabolic reprogramming` *(supplemental)* | none | 15 | relevance | 15 | 9 (+6 off-topic) |

*Raw rows retrieved this run ≈ 124; deduplicated against the cumulative corpus → 174 unique, of which 103 thyroid in-scope and 71 excluded (non-thyroid LNM / pure clinical epidemiology / pan-cancer TME reviews). **0 PMIDs absent from the run#8 corpus.** Full per-paper tags (relevance + dimension + query) are in `search_results_latest.json`.*

---

## 纳入论文 (Included Papers)

The in-scope corpus contains **103 thyroid papers**; all are carried over from prior runs (run#9 added 0). Below we enumerate the High-relevance anchor papers that define the five convergent axes and the candidate directions; the complete 103-paper tagged list (with PMID, DOI, disease, relevance, and multi-dimension tags) lives in `search_results_latest.json`.

1. **MGST1 drives lymph node metastasis in papillary thyroid carcinoma via mitochondrial metabolic reprogramming and immune suppression.** Front Immunol. 2026. PMID: 42327722. DOI: 10.3389/fimmu.2026.1848083. *Agent note:* "Mito-high" subtype, CD8+ T depletion + Treg enrichment; ML model AUC 0.833; toxoflavin reverses immune-cold. **High.**
2. **Prognostic Value of BRAF V600E Mutation in Papillary Thyroid Carcinoma: A Meta-Analysis of Nodal Involvement, Distant Metastases, Recurrence, and Mortality.** 2026. PMID: 41419184. DOI: 10.1016/j.eprac.2025.12.003. *Agent note:* 46,570 patients; nodal OR 1.38, recurrence OR 1.56, but NOT distant mets (OR 0.75) or death (OR 0.97). **High.**
3. **Single-cell RNA-sequencing and spatial transcriptomic analysis reveal a distinct population of APOE- cells yielding pathological lymph node metastasis in papillary thyroid cancer.** 2025. PMID: 39810624. DOI: 10.1002/ctm2.70172. *Agent note:* APOE− stem-like subpop via ABCA1–LXR; 13-gene ML LNM signature. **High.**
4. **An integrated single-cell and spatial transcriptomic atlas of thyroid cancer progression identifies prognostic fibroblast subpopulations.** JCI Insight. 2026. PMID: 41480746. DOI: 10.1172/jci.insight.191990. *Agent note:* 423,733-cell atlas; POSTN+ myCAF predicts LNM/progression (pediatric+adult). **High.**
5. **Cellular and molecular determinants of lymph node metastasis in papillary thyroid carcinoma: Integrated multi-omics profiling and machine learning models.** 2026. PMID: 41421038. DOI: 10.1016/j.compbiolchem.2025.108857. *Agent note:* scRNA+ST+bulk; FN1–SDC4 axis; 17-gene RF model — closes molecular/single-cell/spatial/algorithm loop. **High.**
6. **Integrated spatial metabolomics and transcriptomics reveal the molecular landscape of papillary thyroid cancer and its lymph node metastasis.** 2025. PMID: 41398964. DOI: 10.1186/s12967-025-07566-0. *Agent note:* spatial multi-omics PTC LNM; arginine-polyamine/glycolysis; NAT8L/SVCT-2 validated. **High.**
7. **SHMT2 promotes papillary thyroid cancer metastasis through epigenetic activation of AKT signaling.** 2024. PMID: 38272883. DOI: 10.1038/s41419-024-06476-1. *Agent note:* serine→SAM→PTEN methylation→AKT. **High.**
8. **LncRNA GLTC targets LDHA for succinylation and enzymatic activity to promote progression and radioiodine resistance in papillary thyroid cancer.** 2023. PMID: 37031273. DOI: 10.1038/s41418-023-01157-6. *Agent note:* GLTC–LDHA K155 succinylation → glycolysis + RAI resistance. **High.**
9. **The SOX12-YBX1-LDHA signaling axis drives metastasis in papillary thyroid carcinoma.** 2025. PMID: 40593465. DOI: 10.1038/s41419-025-07797-5. *Agent note:* SOX12→YBX1→LDHA→TGF-β; glycolytic. **High.**
10. **Lipocalin 2 promotes papillary thyroid cancer progression through activation of glycolysis via Hippo/YAP1/HIF1alpha axis.** 2026. PMID: 41964784. DOI: 10.1007/s40618-026-02887-3. *Agent note:* LCN2–YAP1–HIF1α glycolysis; linked ETE + LNM. **High.**
11. **IRS1 promotes thyroid cancer metastasis through EMT and PI3K/AKT pathways.** 2024. PMID: 38172081. DOI: 10.1111/cen.15005. *Agent note:* IRS1→EMT/PI3K-AKT distant mets. **High.**
12. **Myc-Associated Zinc Finger Protein Promotes Metastasis of Papillary Thyroid Cancer.** 2023. PMID: 37664917. DOI: 10.31083/j.fbl2808162. *Agent note:* MAZ→FN1/EMT. **High.**
13. **CREB3L1 promotes tumor growth and metastasis of anaplastic thyroid carcinoma by remodeling the tumor microenvironment.** 2022. PMID: 36192735. DOI: 10.1186/s12943-022-01658-x. *Agent note:* CREB3L1→ECM/CAF niche via IL-1α + KPNA2 (ATC). **High.**
14. **ISG15 and ISGylation modulates cancer stem cell-like characteristics in promoting tumor growth of anaplastic thyroid carcinoma.** 2023. PMID: 37501099. DOI: 10.1186/s13046-023-02751-9. *Agent note:* ISG15/KPNA2 maintains ATC stemness + mets (scRNA). **High.**
15. **DLK1 Is Associated with Stemness Phenotype in Medullary Thyroid Carcinoma Cell Lines.** 2024. PMID: 39595993. DOI: 10.3390/ijms252211924. *Agent note:* DLK1+ enriches MTC stemness. **Medium.**
16. **Illuminating the role of lncRNAs ROR and MALAT1 in cancer stemness state of anaplastic thyroid cancer.** 2023. PMID: 37455764. DOI: 10.1016/j.ncrna.2023.05.006. *Agent note:* ROR/MALAT1 in CD133+ ATC stemness. **Medium.**
17. **Single-Cell RNA Sequencing Reveals the Heterogeneity in Differentiation Trajectory … in Children and Young Adult Patients (CAYA-PTC).** 2025. PMID: 40719066. DOI: 10.1002/advs.202417672. *Agent note:* emCAF_LAMP5/FAP promotes angio+metastasis. **High.**
18. **Single-cell RNA sequencing reveals tumor cell and immune cell variations associated with lymphatic metastasis in papillary thyroid cancer.** 2025. PMID: 41257484. DOI: 10.1530/EC-25-0514. *Agent note:* PTC LNM scRNA — CD8+ TRM (MHC-I/CD99/LCK) pivotal. **High.**
19. **Single-cell and bulk RNA sequencing reveal heterogeneity and diagnostic markers in papillary thyroid carcinoma lymph-node metastasis.** 2024. PMID: 38146045. DOI: 10.1007/s40618-023-02262-6. *Agent note:* S100A2/DIO2 diagnostic model (66-pt validation). **High.**
20. **Spatial and Single-Cell Transcriptomics Unraveled Spatial Evolution of Papillary Thyroid Cancer.** 2025. PMID: 39540244. DOI: 10.1002/advs.202404491. *Agent note:* scRNA+SRT; ferroptosis resistance; malignant/metastatic footprints. **High.**
21. **Identification of key immune genes related to lymphatic metastasis of papillary thyroid cancer via bioinformatics analysis and experimental validation.** 2023. PMID: 37274228. DOI: 10.3389/fonc.2023.1181325. *Agent note:* MET/ICAM1/PTGS2 immune-gene LNM signature. **High.**
22. **5-HT orchestrates histone serotonylation and citrullination to drive neutrophil extracellular traps and liver metastasis.** 2025. PMID: 39903533. DOI: 10.1172/JCI183544. *Agent note:* 5-HT/SERT/NETs drive MTC (and NE) liver mets; fluoxetine blocks. **High.**
23. **Tumor-Infiltrating Immune Cell Landscapes in the Lymph Node Metastasis of Papillary Thyroid Cancer.** 2023. PMID: 36975413. DOI: 10.3390/curroncol30030200. *Agent note:* PTC LNM immune landscape — M2 macrophage/NK/eosinophil shifts. **High.**
24. **Papillary thyroid cancer immune phenotypes via tumor-infiltrating lymphocyte spatial analysis.** 2023. PMID: 37279258. DOI: 10.1530/ERC-23-0110. *Agent note:* TIL spatial IPs (desert/excluded/inflamed); BRAF V600E linked LNM. **High.**
25. **Development and validation of mRNA expression-based classifiers to predict low-risk thyroid tumors.** 2025. PMID: 40741176. DOI: 10.3389/fendo.2025.1600815. *Agent note:* mRNA classifiers rule out invasion/LNM NPV 97.6–100% (Afirma). **High.**
26. **DNA Methylation-Based Risk Stratification and Classification of Pediatric Thyroid Carcinoma.** 2026. PMID: 41701943. DOI: 10.1158/1078-0432.CCR-25-2109. *Agent note:* methylation classifiers predict invasiveness/nodal mets + driver mutation. **High.**
27. **[A multi-molecular predictive model for lymph node metastasis in papillary thyroid carcinoma based on machine learning algorithms].** 2025. PMID: 41656803. DOI: 10.11817/j.issn.1672-7347.2025.250216. *Agent note:* 11-gene ML LNM model (FN1/PI15/IL11…) AUC 0.80/0.79 across 6 ML algos. **High.**
28. **Identification of Novel Gene Signature Predicting Lymph Node Metastasis in Papillary Thyroid Cancer via Bioinformatics Analysis and in vitro Validation.** 2025. PMID: 40110574. DOI: 10.2147/IJGM.S502480. *Agent note:* 6-gene LNM signature COL8A2/MET/FN1/MPZL2/PDLIM4/CLDN10 (TCGA+GEO+GSE60542). **High.**
29. **Multi-omics analysis and metastasis risk factor prediction in N1b stage PTMC.** 2025. PMID: 40977710. DOI: 10.3389/fimmu.2025.1620085. *Agent note:* N1b PTMC: NLR model AUC 0.852; 4-gene classifier (ALDH1A3/CTXN1/MGAT3/TMEM163) AUC 0.857. **High.**
30. **A novel gene panel for prediction of lymph-node metastasis and recurrence in patients with thyroid cancer.** 2020. PMID: 31711617. DOI: 10.1016/j.surg.2019.06.058. *Agent note:* 25-gene ML panel (TCGA) predicts N0/N1 + DFS, OR=8.06. **High.**
31. **Development and validation of a machine learning model for predicting high-risk distant metastatic recurrence in differentiated thyroid cancer.** 2026. PMID: 41877795. DOI: 10.3389/fmed.2026.1790226. *Agent note:* XGBoost DTC distant-met recurrence (1,245 pts) AUC 0.88 external. **High.**
32. **Explainable multimodal deep learning for predicting thyroid cancer lateral lymph node metastasis using ultrasound imaging (LLNM-Net).** 2025. PMID: 40750786. DOI: 10.1038/s41467-025-62042-z. *Agent note:* 7-center, AUC 0.944 > experts (64.3%). **High.**
33. **A multi-task deep learning framework for intraoperative diagnosis of thyroid cancer metastasis using whole slide images (CLAM).** 2026. PMID: 41237514. DOI: 10.1016/j.ijmedinf.2025.106176. *Agent note:* WSI multi-task (LNM/T-stage/localisation) AUC 0.85; 2-center. **High.**
34. **Development and validation of a prediction model for lymph node metastasis in thyroid cancer: integrating deep learning and radiomics … (CLNM).** 2025. PMID: 40771372. DOI: 10.21037/gs-2025-50. *Agent note:* US radiomics+DL fusion SVM CLNM AUC 0.897/0.881 external. **High.**
35. **Multimodal MRI Deep Learning for Predicting Central Lymph Node Metastasis in Papillary Thyroid Cancer.** 2024. PMID: 39682228. DOI: 10.3390/cancers16234042. *Agent note:* MRI+clinical DL (AMMCNet) CLNM AUC 0.891. **High.**
36. **SCLResNet and DSAF … predicting central lymph node metastasis in papillary thyroid carcinoma.** 2025. PMID: 41061579. DOI: 10.1016/j.artmed.2025.103280. *Agent note:* self-supervised multimodal (US+PVAT CT) CLNM AUC 0.863/0.839. **High.**
37. **A novel deep learning model based on multimodal contrast-enhanced ultrasound dynamic video for predicting occult lymph node metastasis in PTC.** 2025. PMID: 40778281. DOI: 10.3389/fendo.2025.1634875. *Agent note:* CEUS dynamic video DL OLNM AUC 0.734 test. **High.**
38. **Artificial intelligence-based prediction of cervical lymph node metastasis in papillary thyroid cancer with CT.** 2023. PMID: 37178202. DOI: 10.1007/s00330-023-09700-2. *Agent note:* CT AI CLNM AUC 0.84/0.81; boosts radiologist specificity. **High.**
39. **Radiomics and deep learning for large volume lymph node metastasis in papillary thyroid carcinoma.** 2024. PMID: 39421056. DOI: 10.21037/gs-24-308. *Agent note:* Thy-DL-Radiomics LVLNM AUC 0.839/0.789 external. **High.**
40. **Deep learning-based multifeature integration robustly predicts central lymph node metastasis in papillary thyroid cancer.** 2023. PMID: 36750791. DOI: 10.1186/s12885-023-10598-8. *Agent note:* CNN CLNM AUC 0.89 train / 0.78 test. **High.**
41. **Deep learning prediction model for central lymph node metastasis in papillary thyroid microcarcinoma based on cytology.** 2023. PMID: 37574759. DOI: 10.1111/cas.15930. *Agent note:* FNA cytology DL central LNM AUC 0.85. **High.**
42. **Predicting lymph node metastasis in thyroid cancer: systematic review and meta-analysis on the CT/MRI-based radiomics and deep learning models.** 2025. PMID: 39742800. DOI: 10.1016/j.clinimag.2024.110392. *Agent note:* SR/MA of 16 CT/MRI radiomics+DL LNM studies; pooled AUC 0.86–0.87. **Medium.**
43. **Diagnostic Accuracy of Ultrasound Radiomics for Cervical Lymph-Node Metastasis in Papillary Thyroid Carcinoma.** 2026. PMID: 41997788. DOI: 10.1016/j.ultrasmedbio.2026.01.017. *Agent note:* SR/MA 60 studies; radiomics AUC 0.83, +clinical 0.88; ML > DL. **Medium.**
44. *(Corpus also holds, among 103 in-scope: PRECISE 41-gene 42008746; TER 5-gene 42305510 AUC 0.96–1.00; LAG3/TIGIT 42430190; IL7R LN biomarker 42397917; TME atlas 42134246; circPTPRM-187aa 41539369; DLEU2–ELAVL1–RCC2 42301557; METTL7B 42332350; FN1 anoikis 42002564; SMDT1 42510113 mito-Ca²⁺/MCU; PD-L1 meta 41510756; POSTN preprint dup 39829764 excluded; plus >50 further molecular/prognostic/algorithm papers — see JSON.)*

---

## 证据矩阵 (Evidence Matrix)

*Columns per `evidence-matrix-schema.md`. Dimension tag in **Relevance/Gap** column marks the axis each row belongs to (分子机制 / 免疫微环境 / 单细胞 / 空间组学 / 算法方法 / 预后转移 / 代谢重编程). Representative High/Medium anchors shown; full 103-row corpus in `search_results_latest.json`.*

| Paper (first author / year) | PMID / DOI | Disease / Population | Data Source | Method | Endpoint | Main Finding | Validation | Limitations | Relevance | Gap Suggested (Dimension) | Future Direction |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Wang QX 2026 (MGST1) | 42327722 / 10.3389/fimmu.2026.1848083 | PTC | TCGA/GTEx + independent cohort + scRNA | Multi-omics + consensus ML + pharmacology | LNM / immune | MGST1 "Mito-high" subtype, immune-cold; model AUC 0.833; toxoflavin reverses | External validation cohort; siRNA + drug | Single-cohort transcriptomics; toxoflavin not in trials | High | Target metabolic–immune node (代谢/免疫) | D3 — target MGST1+ stem-like subpop |
| Gatta E 2026 (BRAF meta) | 41419184 / 10.1016/j.eprac.2025.12.003 | PTC | 46,570 pts, 46 studies | MA (random-effects) | Nodal/recur/distant/death | Nodal OR 1.38, recur OR 1.56; NOT distant (0.75) / death (0.97) | PROSPERO-style; Egger | Heterogeneity; prevalence–effect inverse | High | DTC distant vs LNM decoupling (预后) | Stratify by metastasis type |
| Xiao G 2025 (APOE−) | 39810624 / 10.1002/ctm2.70172 | PTC (advanced) | scRNA + ST + in vitro | scRNA/ST + pseudotime/CellChat + ML | LNM / prognosis | APOE− stem-like subpop via ABCA1–LXR; 13-gene LNM signature | IHC/functional; 13-gene ML | Small n; need prospective | High | Define APOE− metastatic subpop (单细胞/分子) | D3 core target |
| Loberg MA 2026 (POSTN+ myCAF) | 41480746 / 10.1172/jci.insight.191990 | TC (pediatric+adult) | 423,733 cells, 81 samples + ST | scRNA + ST atlas | LNM / progression | POSTN+ myCAF abuts invasive cells; predicts LNM | Multi-institutional; 5 bulk cohorts | Descriptive; causal pending | High | CAF niche as therapeutic (空间/免疫) | D-CAF niche |
| Jiang 2026 (FN1–SDC4) | 41421038 / 10.1016/j.compbiolchem.2025.108857 | PTC | scRNA+ST+bulk | Multi-omics + RF | LNM | FN1–SDC4 axis; 17-gene RF model | Space-validated | Single-center | High | Integrative loop (单细胞/空间/算法) | D3 blueprint |
| Li K 2025 (spatial multi-omics) | 41398964 / 10.1186/s12967-025-07566-0 | PTC | Spatial metabolomics + ST | Spatial multi-omics | LNM | Arginine-polyamine/glycolysis; NAT8L/SVCT-2 | TCGA + zebrafish | Few patients | High | Metabolic spatial drivers (空间/代谢) | Spatial-targeted therapy |
| Sun M 2024 (SHMT2) | 38272883 / 10.1038/s41419-024-06476-1 | PTC | TCGA + proteomics | Wet-lab + ME | Metastasis | Serine→SAM→PTEN methyl→AKT | In vitro/in vivo | Mechanistic only | High | Metabolic–epigenetic link (代谢/分子) | Combine w/ immune |
| Shi L 2023 (GLTC) | 37031273 / 10.1038/s41418-023-01157-6 | PTC | TCGA + MS | Wet-lab | Mets/RAI-resist | GLTC–LDHA K155 succinylation → glycolysis | In vitro/in vivo | RAI focus | High | Glycolysis + RAI sensitivity (代谢) | Dual-target |
| Ruan X 2025 (SOX12) | 40593465 / 10.1038/s41419-025-07797-5 | PTC | scRNA+bulk + CUT&Tag | Multi-omics | Metastasis | SOX12→YBX1→LDHA→TGF-β | Clinical IHC | Single mechanism | High | Glycolytic TF axis (分子/代谢) | TF inhibition |
| Qian X 2026 (LCN2) | 41964784 / 10.1007/s40618-026-02887-3 | PTC | TCGA + functional | Wet-lab | Progression/LNM | LCN2–YAP1–HIF1α glycolysis | 2-DG rescue | New; needs validation | High | Hippo/YAP glycolysis (分子/代谢) | YAP1 inhibition |
| Yu F 2024 (IRS1) | 38172081 / 10.1111/cen.15005 | TC | 131 tissues + RNA-seq | IHC + RNA-seq | Distant mets | IRS1→EMT/PI3K-AKT | In vitro | Clinical only | High | Stratification marker (分子) | IRS1 inhibitor |
| Zheng C 2023 (MAZ) | 37664917 / 10.31083/j.fbl2808162 | PTC | TCGA + IHC | KO + RNA-seq | Migration/inv | MAZ→FN1/EMT | In vitro | Single gene | High | EMT TF (分子) | MAZ inhibition |
| Pan Z 2022 (CREB3L1) | 36192735 / 10.1186/s12943-022-01658-x | ATC | 4 microarrays + scRNA | scRNA + in vivo | Growth/mets | CREB3L1→ECM/CAF via IL-1α+KPNA2 | Zebrafish/mouse | ATC-only | High | CAF niche ATC (分子/免疫) | ATC stroma target |
| Xu T 2023 (ISG15) | 37501099 / 10.1186/s13046-023-02751-9 | ATC | GEO scRNA + functional | scRNA + MS | Stemness/mets | ISG15/KPNA2 maintains ATC CSC | Xenograft/zebrafish | ATC-only | High | ATC stemness (单细胞/分子) | CSC-targeted |
| Guo K 2025 (CAYA) | 40719066 / 10.1002/advs.202417672 | CAYA-PTC | scRNA (11 pts) | scRNA + trajectory | Aggressive pheno | emCAF_LAMP5/FAP promote angio+metastasis | 68Ga-FAPI-PET link | Small pediatric n | High | Pediatric CAF (单细胞/免疫) | Pediatric stratification |
| Chen Y 2025 (CD8 TRM) | 41257484 / 10.1530/EC-25-0514 | PTC (LNM±) | scRNA (6 pts) | scRNA + CellChat | LNM | CD8+ TRM (MHC-I/CD99/LCK) pivotal | Functional enrich | Small n | High | Resident memory T in LNM (单细胞/免疫) | Immunotherapy angle |
| Lu DN 2024 (S100A2/DIO2) | 38146045 / 10.1007/s40618-023-02262-6 | PTC LNM | scRNA+bulk (66 pts) | scRNA + bulk + IHC | LNM Dx | S100A2/DIO2 diagnostic model | 66-pt validation | Single center | High | Diagnostic markers (单细胞/分子) | Clinical Dx assay |
| Yu Y 2023 (MET/ICAM1) | 37274228 / 10.3389/fonc.2023.1181325 | PTC | TCGA + WGCNA | Bioinformatics + IHC | LNM | MET/ICAM1/PTGS2 immune LNM signature | IHC validation | AUC modest | High | Immune-gene LNM (免疫/分子) | Combine w/ metabolic |
| Valizadeh P 2025 (5-HT) | 39903533 / 10.1172/JCI183544 | MTC / NE | Mouse models | In vivo + pharmacology | Liver mets | 5-HT/SERT/NETs drive liver mets; fluoxetine blocks | Genetic + drug | MTC+NE only | High | Serotonin–NET axis (免疫/预后) | D6 sub-direction |
| Li JZ 2026 (methylation) | 41701943 / 10.1158/1078-0432.CCR-25-2109 | Pediatric TC | 2 methylation cohorts | DNA methylome | Invasiveness/driver | Methylation classifiers predict invasiveness + driver | Independent validation | Pediatric only | High | Epigenetic pre-op risk (算法/分子) | Adult extension |
| Golding A 2025 (mRNA classifiers) | 40741176 / 10.3389/fendo.2025.1600815 | TC | Afirma GSC (697) | ML classifiers | Invasion/LNM rule-out | NPV 97.6–100% rule-out | 259-pt validation | Retrospective | High | Clinical decision tool (算法) | Prospective multi-site |
| Zhan Z 2025 (11-gene ML) | 41656803 / 10.11817/j.issn.1672-7347.2025.250216 | PTC (457) | TCGA | 4 DEG methods + 6 ML | LNM | 11-gene model AUC 0.80/0.79 | Sex-stratified | TCGA-only train | High | Multi-gene ML (算法/分子) | External cohort |
| Li H 2025 (6-gene) | 40110574 / 10.2147/IJGM.S502480 | PTC | TCGA+GEO+GSE60542 | WGCNA+LASSO | LNM | COL8A2/MET/FN1/MPZL2/PDLIM4/CLDN10 | In vitro | Moderate AUC | High | Gene signature (分子/预后) | Multi-omics fuse |
| Dai H 2025 (N1b PTMC) | 40977710 / 10.3389/fimmu.2025.1620085 | PTMC N1b | 638 pts + RNA-seq | 8 ML + WGCNA | Lateral LNM | NLR AUC 0.852; 4-gene AUC 0.857 | IHC/CIBERSORT | Single center | High | Occult lateral mets (算法/免疫/单细胞) | Prospective |
| Ruiz EML 2019 (25-gene) | 31711617 / 10.1016/j.surg.2019.06.058 | PTC (TCGA) | TCGA (495) | ML + Cox | N0/N1 + DFS | 25-gene panel OR 8.06; DFS HR 2.64 | Multivariate | TCGA-only | High | Early-stage panel (算法/预后) | External validate |
| Yang F 2026 (XGBoost) | 41877795 / 10.3389/fmed.2026.1790226 | DTC (1,245) | Retrospective multi-center | LASSO + 6 ML | Distant-met recur | XGBoost AUC 0.88 external | 374-pt validation | Retrospective | High | Distant-met recurrence (算法/预后) | Prospective |
| Shen P 2025 (LLNM-Net) | 40750786 / 10.1038/s41467-025-62042-z | PTC (29,615) | 7-center US+text | Multimodal DL (bidirectional attention) | Lateral LNM | AUC 0.944 > experts 64.3% | Multicenter | Non-molecular | High | Imaging DL crowding (算法) | D-ml (overcrowded) |
| Liu W 2026 (CLAM-WSI) | 41237514 / 10.1016/j.ijmedinf.2025.106176 | PTC (569) | 2-center WSI | CLAM MIL | LNM/T-stage/local | AUC 0.85 LNM; 0.65 T; 0.71 local | 10-fold MC; 2-center | WSI-only | High | Interpretable WSI (算法) | Fuse molecular |
| Zhong L 2025 (fusion SVM) | 40771372 / 10.21037/gs-2025-50 | PTC (405) | 2-center US | Radiomics+DL fusion SVM | CLNM | AUC 0.897/0.881 external | External test | Peri-tumoral only | High | Fusion DL (算法) | Prospective |
| Wang X 2024 (MRI DL) | 39682228 / 10.3390/cancers16234042 | PTC (105) | MRI | AMMCNet DL + ML | CLNM | AUC 0.891 | RF comparison | Small n | High | MRI DL (算法) | Multi-modal |
| Miao S 2025 (SCLResNet) | 41061579 / 10.1016/j.artmed.2025.103280 | PTC | US+CT | Self-supervised + DSAF | CLNM | AUC 0.863/0.839 | External | PVAT novel | High | Self-supervised multimodal (算法) | Generalize |
| Liu R 2025 (CEUS video) | 40778281 / 10.3389/fendo.2025.1634875 | PTC (396) | CEUS video | DL video models | OLNM | AUC 0.734 test (combined) | Test set | Weak test | High | Dynamic video DL (算法) | Larger test |
| Wang C 2023 (CT AI) | 37178202 / 10.1007/s00330-023-09700-2 | PTC | CT (multi-center) | DL+radiomics+SVM | CLNM | AUC 0.84/0.81; boosts specificity | External | Manual ROI | High | CT AI assist (算法) | Prospective |
| Ni Z 2024 (LVLNM) | 39421056 / 10.21037/gs-24-308 | PTC (854) | 3-center US | Radiomics+DL+combined | LVLNM | Combined AUC 0.839/0.789 | External | Large-volume only | High | Large-volume LNM (算法) | Subtype |
| Wang Z 2023 (CNN) | 36750791 / 10.1186/s12885-023-10598-8 | PTC (488) | FNA + US | CNN + nomogram | CLNM | AUC 0.89/0.78 | Subgroup | Single center | High | CNN multifeature (算法) | External |
| Ren W 2023 (FNA DL) | 37574759 / 10.1111/cas.15930 | PTMC (42) | FNA cytology | DL | Central LNM | AUC 0.85 | Small | Tiny n | High | Cytology DL (算法) | Scale up |
| Valizadeh P 2025 (SR/MA) | 39742800 / 10.1016/j.clinimag.2024.110392 | TC | 16 studies | SR/MA | LNM (CT/MRI) | Pooled AUC 0.86–0.87 | Heterogeneity | Mixed cancers | Medium | Field-level evidence (算法) | Standardize |
| Nabavizadeh 2026 (SR/MA) | 41997788 / 10.1016/j.ultrasmedbio.2026.01.017 | PTC | 60 studies (10,852) | SR/MA | Cervical LNM | Radiomics AUC 0.83, +clinical 0.88; ML>DL | External lower | Chinese cohorts | Medium | US radiomics field (算法) | External validation |

---

## 已知结论 / What Is Already Known

Evidence is now stable across multiple independent cohorts and is supported by the 103-paper in-scope corpus. Use cautious language; each claim is multi-paper supported.

1. **代谢–免疫耦合是 LNM 的核心驱动 (Metabolic–immune coupling drives LNM).** A "Mito-high"/immune-cold PTC subtype centered on **MGST1** (42327722, ML model AUC 0.833, toxoflavin reverses immune-cold) is the strongest current node; it converges with serine–one-carbon→AKT (**SHMT2** 38272883), GLTC–LDHA succinylation glycolysis (**GLTC** 37031273), SOX12–YBX1–LDHA TGF-β (**SOX12** 40593465), LCN2–Hippo/YAP1/HIF1α (**LCN2** 41964784), METTL7B–USP28/HIF-1α (42332350), and FN1 anoikis (42002564). These share a glycolytic/mitochondrial reprogramming → CD8+ T suppression axis. (Dimension: 分子机制 / 代谢重编程 / 免疫微环境)
2. **存在可定义的干性转移亚群 (A definable stem-like metastatic subpopulation exists).** **APOE−** PTC cells (39810624, via ABCA1–LXR) sit at the dedifferentiation tip and predict cervical LNM; **MGST1** trajectory marks the terminal stem-like state; **ISG15/KPNA2** maintains ATC CSC (37501099); **DLK1** enriches MTC stemness (39595993); lncRNA **ROR/MALAT1** in CD133+ ATC (37455764); and **SMDT1** (mitochondrial Ca²⁺/MCU, 42510113) links OXPHOS to CD8+ T/NK infiltration. (Dimension: 分子机制 / 单细胞)
3. **POSTN+ myCAF 空间图谱是 LNM 的预后 stroma 标志 (POSTN+ myCAF spatial atlas is a prognostic stromal marker for LNM).** The 423,733-cell integrated atlas (41480746) shows POSTN+ myCAFs abut invasive tumor cells and track LNM/progression across pediatric+adult and WDTC/ATC composite tumors; CREB3L1 drives an ATC CAF/ECM niche (36192735); CAYA-PTC emCAF_LAMP5/FAP promotes angiogenesis+metastasis (40719066). (Dimension: 空间组学 / 免疫微环境)
4. **影像/多组学 AI 对 LNM 高度拥挤但临床转化有限 (Imaging/multi-omics AI is crowded but clinically limited).** LLNM-Net (40750786, AUC 0.944, 7-center, beats experts), CLAM-WSI (41237514), and ≥9 fusion DL/radiomics models (40771372/39682228/40778281/41061579/39421056/36750791/37178202/37574759/41931576) plus two SR/MAs (39742800/41997788) all predict LNM from US/CT/MRI/WSI. They are uniformly non-molecular and single-/few-center, with external AUC decay. (Dimension: 算法方法)
5. **BRAF V600E 与 DTC 远处转移解耦 (BRAF V600E decouples from DTC distant metastasis).** The 46k-patient meta (41419184) links BRAF V600E to nodal OR 1.38 and recurrence OR 1.56 but **not** distant metastasis (OR 0.75) or death (OR 0.97); a PD-L1 meta (41510756) mirrors this — both predict *distant* endpoints but not LNM/recurrence. This establishes a stable "distant-metastasis vs LNM" decoupling in DTC. (Dimension: 预后转移 / 分子机制)

---

## 未解问题 / What Remains Unclear

- **因果链条未闭合 (Causal chain unclosed):** metabolic–immune coupling is correlative across most papers; toxoflavin (MGST1) and fluoxetine (5-HT/NETs) are the only agents with functional rescue, and neither is in clinical testing for thyroid cancer.
- **干性亚群缺乏统一定义 (No unified stem-like definition):** APOE−, MGST1+, ISG15/KPNA2+, DLK1+, CD133+ ROR/MALAT1+ are described in different subtypes (PTC vs ATC vs MTC) with no cross-subtype comparison or shared surface marker.
- **空间组学最薄弱 (Spatial omics thinnest):** only 6 in-scope spatial records; POSTN+ myCAF is descriptive, causal stromal targeting unproven; pediatric/ATC/MTC spatial coverage minimal.
- **AI 外推失败 (AI external validation fails):** nearly all DL/radiomics models drop ≥0.05–0.10 AUC externally; no prospective multi-site study; "ML > DL" (41997788) suggests over-parameterization.
- **远处转移机制缺位 (Distant-metastasis mechanism gap):** BRAF/PD-L1 predict distant mets but the organotropic (lung/bone) drivers in thyroid cancer are understudied vs LNM.

---

## 领域方法/数据局限 / Method/Data Limitations In The Field

- **公共数据复用与批次效应 (Public-data reuse & batch effects):** TCGA/GTEx/GEO dominate; the same TCGA THCA cohort seeds dozens of signatures, inflating apparent novelty and risking circular validation.
- **端点稀疏与亚型分层缺失 (Endpoint sparsity & missing subtype stratification):** distant-metastasis and ATC/MTC events are rare; most models pool PTC/PTMC and ignore FTC/MTC/ATC stratification, undermining claim boundaries.
- **外部验证缺失 (Missing external validation):** molecular signatures rarely leave TCGA; imaging DL rarely survives external test sets.
- **湿实验验证不足 (Weak wet-lab validation):** many "mechanism" papers are bioinformatics + modest in vitro only; in vivo/metastasis models sparse.
- **可重复性 (Reproducibility):** several 2026 papers report AUCs without shared code/cohorts; preprint duplication (39829764 ≡ 41480746) pollutes relevance ranking.
- **数据源单一 (Single source):** this monitoring run is constrained to the PubMed MCP, which now exhausts visible 2025–2026 literature for this query set (plateau, see below).

---

## 候选未来方向 / Candidate Future Directions

*Scored 1–5 on each of the 7 rubric criteria (Novelty, Feasibility, Data availability, Validation strength, Clinical relevance, Method rigor, Overcrowding risk); total 7–35. 28–35 = strong.*

| Direction | Rationale | Feasibility | Required Data | Validation Plan | Main Risk | Claim Boundary | Rubric Total |
|---|---|---:|---|---|---|---|---:|
| **D3 — Define & target the APOE−/MGST1+ metabolic–immune stem-like metastatic subpopulation** | Convergent node across axes 1+2+3; actionable (toxoflavin); closes molecular–single-cell–spatial–algorithm loop (41421038) | High (public scRNA/ST + TCGA) | TCGA, GEO, 41480746/39810624/41398964 scRNA+ST, DepMap | In vitro APOE/MGST1 KO + toxoflavin; external LNM cohort; spatial validation | Subpopulation heterogeneity across subtypes | "risk-stratification + target", not cure | **32 (Strong)** |
| D-new — Multi-omics + ML integrative LNM model (FN1–SDC4 blueprint) | 41421038 already fuses scRNA+ST+bulk+RF; extends to prospective | High | Same + prospective cohort | Prospective multi-site; compare vs LLNM-Net | Integration complexity | "preoperative aid" | **31** |
| D6 — Serotonin/NET axis in MTC liver metastasis | 39903533 shows 5-HT/SERT/NETs drive liver mets; fluoxetine blocks | Medium (MTC rare) | MTC cohorts, cBioPortal | Murine MTC liver-mets; fluoxetine trial | MTC small n; off-target | "MTC-specific", not PTC | **28** |
| D-CAF — POSTN+ myCAF niche therapeutic | 41480746 defines prognostic myCAF; causal unproven | Medium | 41480746 atlas + FAPi PET | CAF-depletion in model; correlate LNM | Stromal redundancy | "microenvironment modulator" | **27** |
| D-ml — New imaging DL for LNM | Crowded; marginal gains | High | US/CT/WSI | Must beat LLNM-Net externally | Extreme overcrowding | "incremental" | **23 (feasible only)** |

---

## 推荐下一步方向 / Recommended Next Direction

**D3 — 定义并靶向 APOE−/MGST1+ 代谢–免疫干性转移亚群 (define & target the APOE−/MGST1+ metabolic–immune stem-like metastatic subpopulation).** Rubric total **32 (Strong)** — reaffirmed for the **9th consecutive run** with no countervailing evidence.

- **Research question:** Is the APOE−/MGST1+ state a shared, therapeutically actionable metastatic subpopulation across PTC/ATC/MTC, and does MGST1-driven mitochondrial reprogramming create the immune-cold niche that enables LNM?
- **Novelty angle:** couples metabolic (MGST1/mito), stemness (APOE−/ISG15), and stromal (POSTN+ myCAF) axes that have only been studied separately; exploits toxoflavin as a ready probe.
- **Required datasets:** TCGA/GTEx THCA, GEO (GSE60542 etc.), the 41480746 / 39810624 / 41398964 scRNA+ST atlases, DepMap for dependency scoring.
- **Expected endpoint:** LNM risk stratification + in vitro/in vivo metastasis suppression.
- **Analysis strategy:** consensus clustering to define the MGST1+ "Mito-high" subtype; pseudotime to place APOE− at dedifferentiation tip; CellChat to map CAF–tumor–Tcell crosstalk; DepMap CRISPR to rank targetability.
- **Validation plan:** APOE/MGST1 KO + toxoflavin rescue; independent LNM cohort; spatial (mIHC/CODEX) confirmation of immune-cold niche.
- **Major risk:** subpopulation definitions differ by subtype; toxoflavin has no thyroid clinical data.
- **Claim boundary:** position as *risk-stratification + target identification*, not therapy.

---

## 随访阅读清单 / Follow-Up Reading List

- **42327722 (MGST1):** the central metabolic–immune node; read for the toxoflavin rescue and "Mito-high" subtype definition.
- **39810624 + 41480746 + 41398964:** the three single-cell/spatial atlases that anchor D3 — read together to map APOE− → POSTN+ myCAF → metabolic coupling.
- **41421038 (FN1–SDC4):** the integrative multi-omics+ML blueprint that shows how D3 can be executed end-to-end.
- **41419184 + 41510756:** the two meta-analyses establishing DTC distant-vs-LNM decoupling — essential for any distant-metastasis claim.
- **39903533 (5-HT/NETs):** the only MTC liver-metastasis mechanism with a blocker — read if pursuing D6.
- **40750786 + 41237514:** best-in-class imaging DL — read to understand the crowding before proposing any new algorithm.

---

## 可复现性说明 / Reproducibility Notes

- **Search date:** 2026-07-31 (run#9).
- **Databases:** PubMed only, via `paper-search-mcp` MCP (`mcp__paper-search-mcp__search_pubmed`, invoked with `DeferExecuteTool`). Local `paper_search_mcp` Python package is **not installed**; MCP used directly per skill fallback.
- **Query strings:** a–i as listed in Search Strategy (h/i are the supplemental stemness + metabolic queries).
- **Filters:** none — the MCP tool exposes only `query`, `max_results`, `sort`; no date/publication-type filter. Recency was approximated via `sort=relevance`.
- **Deduplication rule:** by PMID (and normalized title for preprints, e.g. 39829764 ≡ 41480746 dropped).
- **Screening rule:** exclude non-thyroid LNM (breast/colorectal/gastric/lung/NSCLC/HCC/TNBC/pancreas), pure clinical epidemiology (surgeon volume, pregnancy, RAI population, Graves, isthmus CT geometry), and pan-cancer TME reviews; retain thyroid mechanism/immune/single-cell/spatial/algorithm/prognosis papers.
- **Transient errors:** queries c, e, h, i first pass threw `not well-formed (invalid token)` parse errors; re-issued per query until all 9 returned (c required 3 attempts). This is the known intermittent MCP behavior documented since run#2.
- **Files saved:**
  - `lit_review/literature_review_20260731_030000.md` (this report)
  - `lit_review/search_results_latest.json` (overwritten; 174 records, run#9 metadata, 0 new)
  - `lit_review/_build_run9.py` (generator)

---

## 与历史报告对比 / Comparison With Prior Report (run#8, 2026-07-30)

- **检索条数 (Retrieval):** 9 queries × up to 15 = ≈124 raw rows this run; deduplicated to the same **174 unique** corpus.
- **纳入条数 (In-scope):** **103** thyroid papers — **identical to run#8**; **net new = 0**.
- **各维度分布 (Dimension distribution, unchanged):** molecular 47 / immune 30 / single-cell 18 / spatial 6 / algorithm 37 / prognosis 28 / metabolic 14.
- **关键收敛发现 (Convergent findings):** the 5 axes are unchanged vs run#8; no contradictory signal appeared.
- **新增文献与新信号 (New literature / signals):** **none** — this is the 2nd consecutive zero-delta run (run#8 +0, run#9 +0; run#7 was the last with +2). The PubMed MCP has exhausted visible 2025–2026 literature for this query set (run#6's broad `pub_date` sweep already captured the bulk).
- **推荐方向 (Recommendation):** **D3** reaffirmed at rubric **32 (Strong)** for the **9th consecutive run** (run#1→#9), with no countervailing evidence.
- **方向变化 (Direction shift):** none this run. The actionable change is operational: **to break the plateau, future runs should extend beyond PubMed MCP** — add bioRxiv/arXiv preprints and cBioPortal/DepMap, and narrow the ATC/MTC + spatial-omics window — and consider lowering automation cadence from daily to weekly (recommended in run#6/#8 memory).
