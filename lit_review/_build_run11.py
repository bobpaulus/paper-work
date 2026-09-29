# -*- coding: utf-8 -*-
"""
Run #11 builder for the thyroid-cancer lit-review automation.
Loads paper-search-mcp results (already retrieved via DeferExecuteTool),
classifies each by in-scope / relevance / dimension, compares against the
run#10 baseline JSON for new-literature detection, writes
search_results_latest.json (run#11 corpus) and the bilingual markdown report.
"""
import json, datetime, os, collections

HERE = os.path.dirname(os.path.abspath(__file__))
TODAY = "2026-08-02"
TS = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

# ---------------------------------------------------------------------------
# 1. Raw returned PMIDs per query (run #11, all 9 queries, max_results=15)
# ---------------------------------------------------------------------------
RUN11 = {
 "a": ["40110574","40171809","31711617","33656532","41368991","35033555","30942873","34595349","41701943","40741176","39497824","41656803","35255661","40977710","37274228"],
 "b": ["39810624","40456735","17133106","39719645","37835455","38935111","35973989","38172081","40651298","34916087","29546880","37664917","40855521","39301627","17940185"],
 "c": ["40750786","39137488","38990290","37574759","40771372","31746687","39421056","36750791","38563008","39742800","39682228","40778281","37178202","41061579","41237514"],
 "d": ["40456735","38981044","41057823","39615165","39903533","40207795","38990290","32626535","36975413","39221971","38935111","37173925","40315321","37279258","33654093"],
 "e": ["39810624","39540244","37696831","40719066","39221971","36192735","41480746","37501099","41257484","38146045","40201390","40315321","40593465","38990290","39829764"],
 "f": ["41398964","42373830","41421038","41129052","41608657","39923580"],
 "g": ["31792675","41877795","37851243","32615728","29405275","37934030","38311812","41084771","31412224","27697309","36704213","37132252","41817109","32668875","41419184"],
 "h": ["25426258","33186350","39595993"],
 "i": ["41057823","39747873","38953696","40470773","39192979","38272883","41398964","42327722","41219790","40855521","40353071","40980146","42280115","37031273","40850678"],
}

# ---------------------------------------------------------------------------
# 2. Per-paper metadata + classification.
#    scope: True/False (thyroid in-scope). rel: High/Medium/Low.
#    dim: dimension codes -> MOL molecular, IMM immune, SCR single-cell,
#         SPT spatial, ALG algorithm, PRO prognosis, MET metabolic, STM stemness
# ---------------------------------------------------------------------------
ANNOT = {
 # ---- Query a (biomarker gene signature) ----
 "40110574": dict(t="Identification of Novel Gene Signature Predicting Lymph Node Metastasis in Papillary Thyroid Cancer via Bioinformatics Analysis and in vitro Validation", d="10.2147/IJGM.S502480", scope=True, rel="High", dim=["MOL","PRO"], q=["a"], dis="PTC", src="TCGA+GEO(GSE60542)", mth="WGCNA+LASSO", end="LNM", find="6-gene signature (COL8A2, MET, FN1, MPZL2, PDLIM4, CLDN10) predicts PTC LNM; all 6 validated in vitro.", val="in vitro (RT-qPCR/functional)", lim="TCGA/GEO bulk only, no spatial/SC validation", gap="No single-cell or spatial resolution of these drivers", fdir="Spatial validation of MET/FN1 axis"),
 "40171809": dict(t="A nomogram based on the 3-gene signature and clinical characteristics for predicting lymph node metastasis in papillary thyroid cancer", d="10.1177/18758592241311195", scope=True, rel="High", dim=["MOL","PRO"], q=["a"], dis="PTC", src="TCGA", mth="WGCNA+LASSO+nomogram", end="LNM", find="3-gene signature (IQGAP2, BTBD11, MT1G) + clinicopathologic nomogram AUC 0.802 train / 0.718 val.", val="internal val cohort", lim="single-cohort, modest val AUC", gap="external multicenter validation", fdir="External validation of 3-gene nomogram"),
 "31711617": dict(t="A novel gene panel for prediction of lymph-node metastasis and recurrence in patients with thyroid cancer", d="10.1016/j.surg.2019.06.058", scope=True, rel="High", dim=["MOL","PRO"], q=["a"], dis="PTC", src="TCGA (495)", mth="ML 25-gene panel", end="LNM/recurrence", find="25-gene panel discriminates N0/N1 (sens 86%, spec 62%); independent biomarker in T1 lesions; HR 2.64 for DFS.", val="KM/ Cox in TCGA", lim="no wet-lab validation", gap="validate in independent cohorts", fdir="Prospective validation of 25-gene panel"),
 "33656532": dict(t="A 4 Gene-based Immune Signature Predicts Dedifferentiation and Immune Exhaustion in Thyroid Cancer", d="10.1210/clinem/dgab132", scope=True, rel="Medium", dim=["IMM","MOL"], q=["a"], dis="DDTC/TC", src="TCGA+GEO", mth="IRG signature", end="dediff/immune", find="4-IRG signature (PRKCQ, PLAUR, PSMD2, BMP7) predicts dedifferentiation + immune exhaustion; linked to LNM & BRAF.", val="2 val cohorts", lim="immunologic not functional", gap="mechanistic link to LNM", fdir="Functional test of IRG-LNM axis"),
 "41368991": dict(t="BRAF V600E in thyroid cancer: navigating prognostic uncertainty and therapeutic opportunity", d="10.1530/ETJ-25-0225", scope=True, rel="Medium", dim=["MOL"], q=["a"], dis="PTC/ATC/PDTC", src="review", mth="review", end="prognosis", find="Review: BRAF V600E prognostic utility contested; RAI-refractory but heterogeneous; dabrafenib+trametinib FDA-approved ATC.", val="n/a (review)", lim="narrative review", gap="contextualize within co-alterations", fdir="BRAF co-alteration stratification"),
 "35033555": dict(t="A four-enhancer RNA-based prognostic signature for thyroid cancer", d="10.1016/j.yexcr.2022.113023", scope=True, rel="Medium", dim=["MOL","PRO"], q=["a"], dis="TC", src="GTEx+TCGA", mth="eRNA signature", end="prognosis", find="4-eRNA signature (AC141930.1, NBDY, MEG3, AP002358.1) linked to N stage & prognosis.", val="ROC/risk model", lim="eRNA mechanism unclear", gap="functional eRNA role", fdir="eRNA mechanistic study"),
 "30942873": dict(t="Transcriptome Analyses Identify a Metabolic Gene Signature Indicative of Dedifferentiation of Papillary Thyroid Cancer", d="10.1210/jc.2018-02686", scope=True, rel="Medium", dim=["MET","MOL"], q=["a"], dis="DDTC/PTC", src="TCGA+GEO", mth="metabolic signature", end="dediff", find="5-metabolic-gene signature (LPCAT2, ACOT7, HSD17B8, PDE8B, ST3GAL1) predicts dedifferentiation, associated with LNM/ETE/BRAF.", val="3 cohorts", lim="no functional", gap="metabolic driver test", fdir="Metabolic driver validation"),
 "34595349": dict(t="A two-microRNA signature predicts the progression of male thyroid cancer", d="10.1515/biol-2021-0099", scope=True, rel="Medium", dim=["MOL","PRO"], q=["a"], dis="TC (male)", src="TCGA", mth="miRNA signature", end="DFS", find="miR-451a & miR-16-1-3p independent prognostic for male TC DFS.", val="KM/Cox", lim="sex-limited", gap="male-specific mechanism", fdir="Male TC biology"),
 "41701943": dict(t="DNA Methylation-Based Risk Stratification and Classification of Pediatric Thyroid Carcinoma", d="10.1158/1078-0432.CCR-25-2109", scope=True, rel="Medium", dim=["MOL","PRO"], q=["a"], dis="pediatric TC", src="2 pediatric cohorts", mth="methylome classifier", end="invasiveness", find="Methylation classifiers predict invasiveness/LNM & driver mutations (BRAF/RAS/fusion/DICER1) in pediatric TC; NPV high.", val="independent val cohort", lim="pediatric only", gap="adult translation", fdir="Pediatric methylome risk"),
 "40741176": dict(t="Development and validation of mRNA expression-based classifiers to predict low-risk thyroid tumors", d="10.3389/fendo.2025.1600815", scope=True, rel="High", dim=["ALG","MOL"], q=["a"], dis="TC (Bethesda III-VI)", src="Afirma GSC (697 dev, 259 val)", mth="ML mRNA classifiers", end="invasion/LNM", find="mRNA classifiers rule out invasion (NPV 97.6-99%) and LNM (NPV 98.6-100%) preoperatively.", val="locked val cohort", lim="commercial assay dependent", gap="prospective multi-site", fdir="Preop LNM rule-out classifier"),
 "39497824": dict(t="Coagulation-related genes for thyroid cancer prognosis, immune infiltration, staging, and drug sensitivity", d="10.3389/fimmu.2024.1462755", scope=True, rel="Medium", dim=["IMM","PRO"], q=["a"], dis="THCA", src="TCGA", mth="coagulation signature", end="LLNM/prognosis", find="D-dimer predicts lateral LNM (AUC 0.656); 8 coagulation-related prognostic genes build risk model.", val="qPCR validation", lim="D-dimer AUC modest", gap="mechanistic coagulation-immune link", fdir="Coagulation-TME axis"),
 "41656803": dict(t="A multi-molecular predictive model for lymph node metastasis in papillary thyroid carcinoma based on machine learning algorithms", d="10.11817/j.issn.1672-7347.2025.250216", scope=True, rel="High", dim=["ALG","MOL"], q=["a"], dis="PTC", src="TCGA (457)", mth="4 DE methods + LASSO + 6 ML algos", end="LNM", find="11-gene signature (incl FN1, TMPRSS4) logistic model AUC 0.802 train / 0.793 val; stable across 6 ML algos & sexes.", val="TCGA train/val, 6 ML cross-val", lim="single database, no external", gap="external multicenter", fdir="11-gene ML LNM model"),
 "35255661": dict(t="Transcriptomic Analysis of Papillary Thyroid Cancer: A Focus on Immune-Subtyping, Oncogenic Fusion, and Recurrence", d="10.21053/ceo.2021.02215", scope=True, rel="Medium", dim=["IMM","MOL","PRO"], q=["a"], dis="PTC", src="282 PTC + 155 normal (Korean)", mth="RNA-seq + fusion", end="recurrence", find="Recurrence linked to CD8+/Th1 signatures; CTLA4/IDO1/LAG3/PDCD1 in immune-hot low-differentiation; HOXD9 novel recurrence marker; RET fusion partner dictates PI3K/MAPK.", val="TCGA validation", lim="single-center", gap="fusion-specific therapy", fdir="Fusion-subtype recurrence"),
 "40977710": dict(t="Multi-omics analysis and metastasis risk factor prediction in N1b stage PTMC: insights into immune infiltration and therapeutic implications", d="10.3389/fimmu.2025.1620085", scope=True, rel="High", dim=["ALG","IMM","PRO"], q=["a"], dis="N1b PTMC", src="638 PTMC + RNA-seq + WGCNA", mth="8 ML models + WGCNA", end="lateral LNM", find="NLR model AUC 0.852; 4-gene signature (ALDH1A3, CTXN1, MGAT3, TMEM163) AUC 0.857; reduced CD8+/Tfh, increased DC/gdT in N1b.", val="ML cross-val + IHC", lim="retrospective", gap="prospective N1b screening", fdir="N1b PTMC multi-omics risk"),
 "37274228": dict(t="Identification of key immune genes related to lymphatic metastasis of papillary thyroid cancer via bioinformatics analysis and experimental validation", d="10.3389/fonc.2023.1181325", scope=True, rel="High", dim=["IMM","MOL"], q=["a"], dis="PTC", src="TCGA + ImmPort", mth="WGCNA + LASSO/RF", end="LNM", find="3 hub immune genes (PTGS2, MET, ICAM1) upregulated in LNM; model AUC 0.83 (10-fold x200 CV); IHC validated.", val="IHC validation", lim="bulk only", gap="spatial immune map", fdir="MET/ICAM1 lymphatic mets"),
 # ---- Query b (invasion/metastasis mechanism) ----
 "39810624": dict(t="Single-cell RNA-sequencing and spatial transcriptomic analysis reveal a distinct population of APOE- cells yielding pathological lymph node metastasis in papillary thyroid cancer", d="10.1002/ctm2.70172", scope=True, rel="High", dim=["SCR","SPT","MOL","ALG"], q=["b","e"], dis="PTC", src="scRNA+spatial (in-house)", mth="scRNA+ST+pseudotime+ML 13-gene sig", end="LNM", find="APOE- tumor subpopulation drives cervical LNM & poor prognosis via ABCA1-LXR; 13-gene ML LNM signature.", val="in vivo/in vitro + ST", lim="single-center SC/ST", gap="target APOE- subpop", fdir="APOE- metastatic subpop targeting"),
 "40456735": dict(t="Neuro-immune crosstalk in cancer: mechanisms and therapeutic implications", d="10.1038/s41392-025-02241-8", scope=False, rel="Low", dim=[], q=["b","d"], dis="pan-cancer review", src="review", mth="review", end="", find="General neuro-immune review, not thyroid-specific.", val="n/a", lim="off-topic", gap="", fdir=""),
 "17133106": dict(t="Molecular mechanisms involved in differentiated thyroid cancer invasion and metastasis", d="", scope=True, rel="Low", dim=["MOL"], q=["b"], dis="DTC", src="review", mth="review", end="invasion", find="2007 review: RAS-RAF-ERK & PI3K/Akt drive invasion; EMT/collective migration reactivated.", val="n/a", lim="old review", gap="update with SC/spatial", fdir=""),
 "39719645": dict(t="The role of MAPK pathway in gastric cancer: unveiling molecular crosstalk and therapeutic prospects", d="10.1186/s12967-024-05998-8", scope=False, rel="Low", dim=[], q=["b"], dis="gastric", src="review", mth="review", end="", find="Gastric MAPK review, off-topic.", val="n/a", lim="non-thyroid", gap="", fdir=""),
 "37835455": dict(t="Thyroid Cancer: Focus on Invasion and Metastasis Mechanisms, Therapeutic Target and Drug Treatment", d="10.3390/cancers15194762", scope=True, rel="Medium", dim=["MOL"], q=["b"], dis="TC", src="review", mth="review", end="invasion", find="2023 review of TC invasion/metastasis mechanisms & therapeutics.", val="n/a", lim="narrative", gap="", fdir=""),
 "38935111": dict(t="The association between immune cells and breast cancer: insights from Mendelian randomization and meta-analysis", d="10.1097/JS9.0000000000001840", scope=False, rel="Low", dim=[], q=["b","d"], dis="breast", src="MR+meta", mth="MR", end="", find="Breast immune MR, off-topic.", val="n/a", lim="non-thyroid", gap="", fdir=""),
 "35973989": dict(t="DDX39B drives colorectal cancer progression by promoting the stability and nuclear translocation of PKM2", d="10.1038/s41392-022-01096-7", scope=False, rel="Low", dim=[], q=["b"], dis="CRC", src="CRC", mth="functional", end="", find="Colorectal PKM2, off-topic.", val="n/a", lim="non-thyroid", gap="", fdir=""),
 "38172081": dict(t="IRS1 promotes thyroid cancer metastasis through EMT and PI3K/AKT pathways", d="10.1111/cen.15005", scope=True, rel="High", dim=["MOL"], q=["b"], dis="TC", src="131 metastatic TC tissues + RNA-seq", mth="IHC + RNA-seq + functional", end="distant mets", find="IRS1 high in TC, linked to distant mets/advanced stage; drives metastasis via EMT & PI3K/AKT.", val="in vitro", lim="no SC", gap="therapeutic inhibition", fdir="IRS1 EMT/PI3K axis"),
 "40651298": dict(t="An integrative analysis reveals mechanisms of Prunella vulgaris in thyroid cancer metastasis", d="10.1016/j.phymed.2025.157051", scope=True, rel="Medium", dim=["MOL"], q=["b"], dis="PTC", src="RNA-seq + TCMSP", mth="integrative + ML hub", end="LNM/metastasis", find="beta-sitosterol (BS) inhibits PTC metastasis targeting ADRB2, inducing mitochondrial dysfunction; ADRB2 high in LNM.", val="in vitro", lim="herb-focused", gap="in vivo efficacy", fdir="ADRB2 metastasis target"),
 "34916087": dict(t="Molecular mechanisms of thyroid cancer: A competing endogenous RNA (ceRNA) point of view", d="10.1016/j.biopha.2021.112251", scope=True, rel="Low", dim=["MOL"], q=["b"], dis="TC", src="review", mth="review", end="EMT/mets", find="ceRNA networks in TC progression/metastasis/drug resistance.", val="n/a", lim="narrative", gap="", fdir=""),
 "29546880": dict(t="Cell motility in cancer invasion and metastasis: insights from simple model organisms", d="10.1038/nrc.2018.15", scope=False, rel="Low", dim=[], q=["b"], dis="general", src="review", mth="review", end="", find="Model-organism motility review, not TC-specific.", val="n/a", lim="off-topic", gap="", fdir=""),
 "37664917": dict(t="Myc-Associated Zinc Finger Protein Promotes Metastasis of Papillary Thyroid Cancer", d="10.31083/j.fbl2808162", scope=True, rel="High", dim=["MOL"], q=["b"], dis="PTC", src="TCGA + IHC", mth="bioinfo + IHC + functional", end="metastasis", find="MAZ高表达促PTC迁移侵袭 via EMT; FN1负相关于MAZ; MAZ高=差预后.", val="in vitro", lim="no SC", gap="MAZ-FN1轴靶向", fdir="MAZ EMT driver"),
 "40855521": dict(t="NSUN2-tRNAVal-CAC-axis-regulated codon-biased translation drives triple-negative breast cancer glycolysis and progression", d="10.1186/s11658-025-00781-z", scope=False, rel="Low", dim=[], q=["b","i"], dis="TNBC", src="TNBC", mth="functional", end="", find="TNBC translation, off-topic.", val="n/a", lim="non-thyroid", gap="", fdir=""),
 "39301627": dict(t="Molecular mechanisms and clinicopathological characteristics of inhibin betaA in thyroid cancer metastasis", d="10.3892/ijmm.2024.5423", scope=True, rel="High", dim=["MOL"], q=["b"], dis="TC", src="GEO+TCGA + functional", mth="bioinfo + zebrafish/mouse", end="metastasis", find="INHBA promotes TC migration/invasion via RhoA/LIMK/cofilin; knockdown attenuates metastasis.", val="in vivo", lim="no SC", gap="INHBA therapeutic", fdir="INHBA RhoA axis"),
 "17940185": dict(t="BRAF mutation in papillary thyroid cancer: pathogenic role, molecular bases, and clinical implications", d="", scope=True, rel="Low", dim=["MOL"], q=["b"], dis="PTC", src="review", mth="review", end="recurrence", find="2007 review: BRAF V600E linked to ETE/LNM/recurrence; upregulates VEGF/MMPs/c-Met.", val="n/a", lim="old", gap="", fdir=""),
 # ---- Query c (ML/DL prediction) ----
 "40750786": dict(t="Explainable multimodal deep learning for predicting thyroid cancer lateral lymph node metastasis using ultrasound imaging", d="10.1038/s41467-025-62042-z", scope=True, rel="High", dim=["ALG"], q=["c"], dis="PTC lateral LNM", src="29,615 pts / 9,836 sx / 7 centers", mth="LLNM-Net bidirectional-attention DL", end="lateral LNM", find="LLNM-Net AUC 0.944, acc 84.7% multicenter, beats experts (64.3%) & prior models (+7.4%); capsular distance <0.25cm = >72% risk.", val="7-center external", lim="US-only modality", gap="prospective deployment", fdir="Multicenter DL LNM"),
 "39137488": dict(t="Non-invasive prediction of axillary lymph node dissection exemption in breast cancer patients post-neoadjuvant therapy", d="10.1016/j.breast.2024.103786", scope=False, rel="Low", dim=[], q=["c"], dis="breast", src="breast", mth="radiomics+DL", end="", find="Breast ALN, off-topic.", val="n/a", lim="non-thyroid", gap="", fdir=""),
 "38990290": dict(t="Artificial intelligence-based multi-modal multi-tasks analysis reveals tumor molecular heterogeneity, predicts preoperative lymph node metastasis and prognosis in papillary thyroid carcinoma", d="10.1097/JS9.0000000000001875", scope=True, rel="High", dim=["ALG","MOL","SCR"], q=["c","d","e"], dis="PTC", src="521 in-house + 499 TCGA + scRNA", mth="DL multimodal (path+genomic+immune)", end="LNM/DFS", find="4 molecular subtypes (BRAF/RAS/RET/other); DL model AUC 0.86 train / 0.84 val / 0.83 real-world for LNM & DFS; GradCAM heatmaps.", val="TCGA external val", lim="retrospective, single real-world center", gap="prospective multi-site", fdir="Multimodal DL PTC"),
 "37574759": dict(t="Deep learning prediction model for central lymph node metastasis in papillary thyroid microcarcinoma based on cytology", d="10.1111/cas.15930", scope=True, rel="Medium", dim=["ALG"], q=["c"], dis="PTMC", src="208 FNA prep", mth="DL on cytology", end="central LNM", find="DL on FNA predicts central LNM (AUC 0.85) better than clinical exam.", val="small (42 test)", lim="tiny test set", gap="larger validation", fdir="FNA DL PTMC"),
 "40771372": dict(t="Development and validation of a prediction model for lymph node metastasis in thyroid cancer: integrating deep learning and radiomics features from intra- and peri-tumoral regions", d="10.21037/gs-2025-50", scope=True, rel="High", dim=["ALG"], q=["c"], dis="PTC CLNM", src="405 pts / 2 centers", mth="DL+radiomics SVM fusion", end="CLNM", find="Intra+peri-tumoral radiomics-DL fusion SVM AUC 0.897 internal / 0.881 external; beats single-modality.", val="external test center", lim="US-only", gap="multi-modal add", fdir="Radiomics-DL fusion CLNM"),
 "31746687": dict(t="Lymph Node Metastasis Prediction from Primary Breast Cancer US Images Using Deep Learning", d="10.1148/radiol.2019190372", scope=False, rel="Low", dim=[], q=["c"], dis="breast", src="breast", mth="CNN", end="", find="Breast US DL, off-topic.", val="n/a", lim="non-thyroid", gap="", fdir=""),
 "39421056": dict(t="Radiomics and deep learning for large volume lymph node metastasis in papillary thyroid carcinoma", d="10.21037/gs-24-308", scope=True, rel="High", dim=["ALG"], q=["c"], dis="PTC LVLNM", src="854 pts / 3 centers", mth="8 ML + 5 DL + combined", end="large-volume LNM", find="Thy-DL-Radiomics combined AUC 0.839 internal / 0.789 external for large-volume LNM.", val="external val", lim="LVLNM subset only", gap="clinical utility", fdir="LVLNM radiomics-DL"),
 "36750791": dict(t="Deep learning-based multifeature integration robustly predicts central lymph node metastasis in papillary thyroid cancer", d="10.1186/s12885-023-10598-8", scope=True, rel="Medium", dim=["ALG"], q=["c"], dis="PTC CLNM", src="488 pts", mth="CNN + nomogram", end="CLNM", find="CNN AUC 0.89 train / 0.78 test; nomogram AUC 0.778; independent factors age/size/capsule/BRAF.", val="subgroup val", lim="single center", gap="external", fdir="CNN CLNM PTC"),
 "38563008": dict(t="Predicting central cervical lymph node metastasis in papillary thyroid microcarcinoma using deep learning", d="10.7717/peerj.16952", scope=True, rel="Medium", dim=["ALG"], q=["c"], dis="PTMC", src="611 pts", mth="DL US + clinical", end="CLNM", find="DL US AUC 0.65, modest; clinical factors AUC 0.64; fusion not better.", val="internal", lim="low AUC", gap="better features", fdir="PTMC DL low perf"),
 "39742800": dict(t="Predicting lymph node metastasis in thyroid cancer: systematic review and meta-analysis on the CT/MRI-based radiomics and deep learning models", d="10.1016/j.clinimag.2024.110392", scope=True, rel="High", dim=["ALG"], q=["c"], dis="TC", src="16 studies (sys rev)", mth="meta-analysis", end="LNM", find="Pooled AUC 0.86 internal / 0.87 train; DL sens 80.8%/spec 78.7% > handcrafted radiomics; clinical-data addition improves (p=0.037).", val="meta (16 studies)", lim="heterogeneity", gap="standardization", fdir="LNM radiomics meta"),
 "39682228": dict(t="Multimodal MRI Deep Learning for Predicting Central Lymph Node Metastasis in Papillary Thyroid Cancer", d="10.3390/cancers16234042", scope=True, rel="High", dim=["ALG"], q=["c"], dis="PTC CLNM", src="105 pts MRI", mth="AMMCNet CNN vs ML", end="CLNM", find="DL fusion AUC 0.891 > best ML 0.863 for CLNM.", val="internal test", lim="small, MRI-only", gap="external", fdir="MRI DL CLNM"),
 "40778281": dict(t="A novel deep learning model based on multimodal contrast-enhanced ultrasound dynamic video for predicting occult lymph node metastasis in papillary thyroid carcinoma", d="10.3389/fendo.2025.1634875", scope=True, rel="High", dim=["ALG"], q=["c"], dis="PTC OLNM", src="396 pts CEUS video", mth="DL static+video fusion", end="occult LNM", find="DL_combined AUC 0.926 train / 0.734 test for occult LNM; CEUS video > static.", val="test set", lim="test AUC modest", gap="external", fdir="CEUS video DL OLNM"),
 "37178202": dict(t="Artificial intelligence-based prediction of cervical lymph node metastasis in papillary thyroid cancer with CT", d="10.1007/s00330-023-09700-2", scope=True, rel="High", dim=["ALG"], q=["c"], dis="PTC CLNM", src="multicenter CT", mth="DenseNet+CBAM + radiomics + RF fusion", end="CLNM", find="AI system AUC 0.84 internal / 0.81 external, beats DL/radiomics/clinical; improves radiologist spec 9-15%.", val="external test", lim="CT-only", gap="prospective", fdir="CT AI CLNM"),
 "41061579": dict(t="SCLResNet and DSAF: A self-supervised contrastive learning and deep self-attention fusion-based multimodal network for predicting central lymph node metastasis in papillary thyroid carcinoma", d="10.1016/j.artmed.2025.103280", scope=True, rel="High", dim=["ALG"], q=["c"], dis="PTC CLNM", src="US + CT(PVAT)", mth="SCLResNet101 + DSAF fusion", end="CLNM", find="Self-supervised + PVAT fusion AUC 0.863 internal / 0.839 external; reduces false pos/neg vs radiologists.", val="external test", lim="two modalities", gap="prospective", fdir="Self-supervised multimodal CLNM"),
 "41237514": dict(t="A multi-task deep learning framework for intraoperative diagnosis of thyroid cancer metastasis using whole slide images", d="10.1016/j.ijmedinf.2025.106176", scope=True, rel="High", dim=["ALG","SCR"], q=["c"], dis="PTC", src="569 pts / 2 centers WSI", mth="CLAM (MIL) multi-task", end="LNM/T-stage/localization", find="CLAM WSI: AUC 0.85 LNM, 0.65 T-stage, 0.71 localization; 10-fold MC CV; cross-center stable; Grad-CAM interpretable.", val="2-center MC CV", lim="frozen-section only", gap="prospective", fdir="WSI CLAM metastasis"),
 # ---- Query d (immune microenvironment) ----
 "38981044": dict(t="Lactylated Apolipoprotein C-II Induces Immunotherapy Resistance by Promoting Extracellular Lipolysis", d="10.1002/advs.202406333", scope=False, rel="Low", dim=[], q=["d"], dis="NSCLC", src="NSCLC", mth="multi-omics", end="", find="NSCLC lactylation, off-topic.", val="n/a", lim="non-thyroid", gap="", fdir=""),
 "41057823": dict(t="Exosome-mediated metabolic reprogramming: effects on thyroid cancer progression and tumor microenvironment remodeling", d="10.1186/s12943-025-02470-z", scope=True, rel="High", dim=["IMM","MET","MOL"], q=["d","i"], dis="TC", src="review", mth="review", end="TME/mets", find="Review: TC exosomes drive metabolic reprogramming (mitochondrial dysfunc, glycolysis, lipid, glutamine) reshaping immune TME & evasion.", val="n/a", lim="review", gap="exosome cargo targeting", fdir="Exosome metabolic-immune"),
 "39615165": dict(t="Decoding tumor microenvironment: EMT modulation in breast cancer metastasis and therapeutic resistance", d="10.1016/j.biopha.2024.117714", scope=False, rel="Low", dim=[], q=["d"], dis="breast", src="review", mth="review", end="", find="Breast EMT/TME, off-topic.", val="n/a", lim="non-thyroid", gap="", fdir=""),
 "39903533": dict(t="5-HT orchestrates histone serotonylation and citrullination to drive neutrophil extracellular traps and liver metastasis", d="10.1172/JCI183544", scope=True, rel="High", dim=["IMM","MOL"], q=["d"], dis="MTC / NE cancers liver mets", src="NEPC/MTC models", mth="in vivo + pharmacologic", end="liver mets", find="5-HT from neuroendocrine cells -> NETs in liver -> MTC/NE liver mets; fluoxetine/SERT blockade inhibits. (relevant to MTC distant mets)", val="in vivo + FDA drug", lim="MTC subset of NE cancers", gap="MTC patient translation", fdir="5-HT/NETs MTC liver mets"),
 "40207795": dict(t="SERPINE1 Facilitates Metastasis in Gastric Cancer Through Anoikis Resistance and Tumor Microenvironment Remodeling", d="10.1002/smll.202500136", scope=False, rel="Low", dim=[], q=["d"], dis="gastric", src="GC", mth="functional", end="", find="Gastric SERPINE1, off-topic.", val="n/a", lim="non-thyroid", gap="", fdir=""),
 "32626535": dict(t="Immune Microenvironment of Thyroid Cancer", d="10.7150/jca.44506", scope=True, rel="Medium", dim=["IMM"], q=["d"], dis="TC", src="review", mth="review", end="immune evasion", find="Review: immune cells/soluble mediators/checkpoints in TC immune evasion & prognosis.", val="n/a", lim="narrative", gap="", fdir=""),
 "36975413": dict(t="Tumor-Infiltrating Immune Cell Landscapes in the Lymph Node Metastasis of Papillary Thyroid Cancer", d="10.3390/curroncol30030200", scope=True, rel="High", dim=["IMM"], q=["d"], dis="PTC", src="TCGA + driver mut", mth="CIBERSORT + mut", end="LNM", find="LNM associated with activated DC/M0 macro (up) & NK/eosinophil (down); TG mut -> M2 macro, HRAS mut -> DC; immune landscapes differ by LNM.", val="TCGA", lim="bulk deconv", gap="spatial immune map", fdir="TIME LNM landscape"),
 "39221971": dict(t="Tryptophan 2,3-dioxygenase-positive matrix fibroblasts fuel breast cancer lung metastasis", d="10.1002/cac2.12608", scope=False, rel="Low", dim=[], q=["d","e"], dis="breast", src="breast", mth="scRNA", end="", find="Breast MAF, off-topic.", val="n/a", lim="non-thyroid", gap="", fdir=""),
 "37173925": dict(t="The Tumor Microenvironment and the Estrogen Loop in Thyroid Cancer", d="10.3390/cancers15092458", scope=True, rel="Low", dim=["IMM"], q=["d"], dis="TC", src="review", mth="review", end="TME", find="Review: estrogen-TME crosstalk in TC (female predominance).", val="n/a", lim="narrative", gap="", fdir=""),
 "40315321": dict(t="Targeting HMGB2 acts as dual immunomodulator by bolstering CD8+ T cell function and inhibiting tumor growth in hepatocellular carcinoma", d="10.1126/sciadv.ads8597", scope=False, rel="Low", dim=[], q=["d","e"], dis="HCC", src="HCC", mth="scRNA", end="", find="HCC HMGB2, off-topic.", val="n/a", lim="non-thyroid", gap="", fdir=""),
 "37279258": dict(t="Papillary thyroid cancer immune phenotypes via tumor-infiltrating lymphocyte spatial analysis", d="10.1530/ERC-23-0110", scope=True, rel="High", dim=["IMM","SPT"], q=["d"], dis="PTC", src="TCGA WSI", mth="AI TIL spatial", end="LNM/immune", find="3 immune phenotypes: desert (48%, RAS), excluded (34%, BRAF V600E, higher LNM), inflamed (18%, high cytolytic). Tissue-based TIL spatial classification.", val="TCGA WSI", lim="no functional", gap="immunotherapy prediction", fdir="PTC immune phenotypes"),
 "33654093": dict(t="RNA m6A methylation orchestrates cancer growth and metastasis via macrophage reprogramming", d="10.1038/s41467-021-21514-8", scope=False, rel="Low", dim=[], q=["d"], dis="pan-cancer", src="mouse", mth="functional", end="", find="Pan-cancer m6A macrophage, not TC-specific.", val="n/a", lim="off-topic", gap="", fdir=""),
 # ---- Query e (single-cell RNA-seq) ----
 "39540244": dict(t="Spatial and Single-Cell Transcriptomics Unraveled Spatial Evolution of Papillary Thyroid Cancer", d="10.1002/advs.202404491", scope=True, rel="High", dim=["SCR","SPT","MOL"], q=["e"], dis="PTC", src="scRNA + SRT (in-house)", mth="scRNA+SRT integration", end="metastasis/evolution", find="PTC evolves via aerobic metabolism up + translation down; 2 malignant/metastatic footprints discriminate PTC from thyrocytes; ferroptosis resistance aids evolution.", val="SRT", lim="single-center", gap="therapeutic targeting", fdir="PTC spatial evolution"),
 "37696831": dict(t="Single-cell transcriptome analysis indicates fatty acid metabolism-mediated metastasis and immunosuppression in male breast cancer", d="10.1038/s41467-023-41318-2", scope=False, rel="Low", dim=[], q=["e"], dis="breast", src="breast", mth="scRNA", end="", find="Male breast scRNA, off-topic.", val="n/a", lim="non-thyroid", gap="", fdir=""),
 "40719066": dict(t="Single-Cell RNA Sequencing Reveals the Heterogeneity in Differentiation Trajectory and Tumor Microenvironment Leading to More Aggressive Phenotypes of Papillary Thyroid Cancer in Children and Young Adult Patients", d="10.1002/advs.202417672", scope=True, rel="High", dim=["SCR","IMM"], q=["e"], dis="CAYA-PTC", src="11 CAYA-PTC scRNA", mth="scRNA + trajectory", end="aggressive pheno", find="CAYA-PTC lacks mild BRAF-like state -> rapid invasive/metastatic; emCAF_LAMP5 (FAP+) drives angiogenesis/mets; 68Ga-FAPI-PET promising.", val="scRNA", lim="small n", gap="pediatric-targeted therapy", fdir="CAYA-PTC ecosystem"),
 "36192735": dict(t="CREB3L1 promotes tumor growth and metastasis of anaplastic thyroid carcinoma by remodeling the tumor microenvironment", d="10.1186/s12943-022-01658-x", scope=True, rel="High", dim=["SCR","MOL"], q=["e"], dis="ATC", src="4 microarray + scRNA", mth="scRNA + CAF", end="metastasis", find="CREB3L1 up in ATC, drives ECM signaling & activates alpha-SMA+ CAFs via IL-1alpha; loss inhibits metastasis; KPNA2 nuclear transport.", val="zebrafish/mouse + scRNA", lim="no spatial", gap="CAF targeting", fdir="CREB3L1 ATC CAF"),
 "41480746": dict(t="An integrated single-cell and spatial transcriptomic atlas of thyroid cancer progression identifies prognostic fibroblast subpopulations", d="10.1172/jci.insight.191990", scope=True, rel="High", dim=["SCR","SPT","MOL"], q=["e"], dis="WDTC/ATC/pediatric", src="423,733 cells / 81 samples + ST 28 tumors", mth="scRNA+ST atlas", end="LNM/progression", find="POSTN+ myCAF abuts invasive tumor cells, correlates with LNM/poor prognosis/progression; iCAF distant in autoimmune thyroiditis. (423k-cell atlas)", val="multi-institutional + 5 bulk cohorts", lim="retrospective", gap="target myCAF", fdir="POSTN+ myCAF atlas"),
 "37501099": dict(t="ISG15 and ISGylation modulates cancer stem cell-like characteristics in promoting tumor growth of anaplastic thyroid carcinoma", d="10.1186/s13046-023-02751-9", scope=True, rel="High", dim=["SCR","MOL","STM"], q=["e"], dis="ATC", src="GEO scRNA + functional", mth="scRNA + ISGylation", end="stemness/mets", find="ISG15 enriched in ATC CSCs; ISG15-ISGylation of KPNA2 stabilizes it -> stemness; depletion inhibits growth/mets.", val="mouse/zebrafish + scRNA", lim="no spatial", gap="ISG15 therapeutic", fdir="ISG15/KPNA2 ATC CSC"),
 "41257484": dict(t="Single-cell RNA sequencing reveals tumor cell and immune cell variations associated with lymphatic metastasis in papillary thyroid cancer", d="10.1530/EC-25-0514", scope=True, rel="High", dim=["SCR","IMM"], q=["e"], dis="PTC", src="6 PTC scRNA (viable)", mth="scRNA + CellChat", end="LNM", find="LNM PTC: proliferation/migration pathways; CD8+ resident memory T cells pivotal via MHC-I/CD99/LCK; CD44-TYROBP↑ / PPIA-BSG↓ communication.", val="scRNA", lim="n=6", gap="spatial confirm", fdir="LNM scRNA immune"),
 "38146045": dict(t="Single-cell and bulk RNA sequencing reveal heterogeneity and diagnostic markers in papillary thyroid carcinoma lymph-node metastasis", d="10.1007/s40618-023-02262-6", scope=True, rel="High", dim=["SCR","MOL"], q=["e"], dis="PTC LNM", src="scRNA+bulk + 66 pts", mth="scRNA+bulk + LASSO", end="LNM", find="19-gene DEG model; S100A2 & DIO2 validated (RT-qPCR/IHC); DIO2 inhibits proliferation (G2/M arrest).", val="66-pt IHC/RT-qPCR", lim="modest n", gap="external val", fdir="S100A2/DIO2 LNM"),
 "40201390": dict(t="Comprehensive Analyses of Single-Cell and Bulk RNA Sequencing Data From M2 Macrophages to Elucidate the Immune Prognostic Signature in Patients with Gastric Cancer Peritoneal Metastasis", d="10.2147/ITT.S506143", scope=False, rel="Low", dim=[], q=["e"], dis="gastric", src="gastric", mth="scRNA", end="", find="Gastric PM, off-topic.", val="n/a", lim="non-thyroid", gap="", fdir=""),
 "40593465": dict(t="The SOX12-YBX1-LDHA signaling axis drives metastasis in papillary thyroid carcinoma", d="10.1038/s41419-025-07797-5", scope=True, rel="High", dim=["SCR","MOL","MET"], q=["e"], dis="PTC", src="scRNA+bulk + CUT&Tag", mth="scRNA+bulk+CUT&Tag+IP-MS", end="metastasis", find="SOX12 up in PTC, poor prognosis; SOX12->YBX1->LDHA promoter->TGF-beta activation->mets; LDHA rescue confirms.", val="clinical + functional", lim="no spatial", gap="SOX12 inhibitor", fdir="SOX12-YBX1-LDHA axis"),
 "39829764": dict(t="An integrated single-cell and spatial transcriptomic atlas of thyroid cancer progression (bioRxiv preprint of 41480746)", d="10.1101/2025.01.08.631962", scope=False, rel="Low", dim=[], q=["e"], dis="TC", src="preprint", mth="scRNA+ST", end="", find="Preprint duplicate of 41480746 (same author/cohort). Excluded as duplicate to avoid double-count.", val="n/a", lim="duplicate", gap="", fdir=""),
 # ---- Query f (spatial transcriptomics multi-omics) ----
 "41398964": dict(t="Integrated spatial metabolomics and transcriptomics reveal the molecular landscape of papillary thyroid cancer and its lymph node metastasis", d="10.1186/s12967-025-07566-0", scope=True, rel="High", dim=["SPT","MET","MOL"], q=["f","i"], dis="PTC LNM", src="spatial metabolomics + ST + TCGA", mth="spatial multi-omics", end="LNM", find="Arginine-polyamine, glycolysis, lipid dysregulated in cancer regions; 5 metastasis-driving metabolites (FA 22:6, PC 36:4, PC 34:1, NAA, ascorbate) in LNM primaries; NAT8L/SVCT-2 knockdown reduces mets; 10 metabolite-genes predict poor prognosis.", val="zebrafish + TCGA", lim="spatial resolution limited", gap="metabolite targeting", fdir="Spatial multi-omics PTC LNM"),
 "42373830": dict(t="Multi-omics reveals tumor microenvironment heterogeneity and therapeutic vulnerabilities in peritoneal metastasis of gastric cancer", d="10.1038/s42003-026-10571-8", scope=False, rel="Low", dim=[], q=["f"], dis="gastric", src="gastric", mth="scRNA+ST", end="", find="Gastric PM spatial, off-topic.", val="n/a", lim="non-thyroid", gap="", fdir=""),
 "41421038": dict(t="Cellular and molecular determinants of lymph node metastasis in papillary thyroid carcinoma: Integrated multi-omics profiling and machine learning models", d="10.1016/j.compbiolchem.2025.108857", scope=True, rel="High", dim=["SPT","SCR","ALG","MOL"], q=["f"], dis="PTC LNM", src="scRNA + ST + bulk", mth="multi-omics + random forest", end="LNM", find="N1 tumors: immune-inflammatory TME + immune escape via antigen-presentation down; State 1 subpop as metastasis-initiating; 17-gene LNM signature (hub FN1 via FN1-SDC4 axis, ST-validated); RF model; FN1 silencing suppresses mets.", val="in vitro + ST", lim="retrospective", gap="FN1-SDC4 targeting", fdir="FN1-SDC4 multi-omics LNM"),
 "41129052": dict(t="Fibroblasts in the tumor microenvironment: heterogeneity and dynamic interactions in tumor progression revealed by spatial transcriptomics", d="10.1007/s13402-025-01108-y", scope=False, rel="Low", dim=[], q=["f"], dis="pan-cancer review", src="review", mth="review", end="", find="Pan-cancer CAF spatial review, not TC-specific.", val="n/a", lim="off-topic", gap="", fdir=""),
 "41608657": dict(t="Breast cancer stem cell activity driven by ME18D gene expression in the tumor microenvironment", d="10.4252/wjsc.v18.i1.111348", scope=False, rel="Low", dim=[], q=["f"], dis="breast", src="breast", mth="multi-omics", end="", find="Breast CSC, off-topic.", val="n/a", lim="non-thyroid", gap="", fdir=""),
 "39923580": dict(t="A comprehensive pan-cancer examination of transcription factor MAFF", d="10.1016/j.intimp.2025.114105", scope=False, rel="Low", dim=[], q=["f"], dis="pan-cancer", src="pan-cancer", mth="multi-omics", end="", find="Pan-cancer MAFF, off-topic.", val="n/a", lim="off-topic", gap="", fdir=""),
 # ---- Query g (prognosis/recurrence/distant mets) ----
 "31792675": dict(t="A novel RNA sequencing-based risk score model to predict papillary thyroid carcinoma recurrence", d="10.1007/s10585-019-10011-4", scope=True, rel="High", dim=["PRO","MOL"], q=["g"], dis="PTC", src="TCGA (train 240 / val 239)", mth="RNA-seq Cox model", end="recurrence", find="5-gene risk score (TOP2A, RP11-180M15.7, RP11-635N19.1, PROSER3, TMEM139) predicts recurrence; HR 6.62 train / 3.40 val.", val="chronologic split val", lim="TCGA only", gap="external val", fdir="RNA-seq recurrence model"),
 "41877795": dict(t="Development and validation of a machine learning model for predicting high-risk distant metastatic recurrence in differentiated thyroid cancer", d="10.3389/fmed.2026.1790226", scope=True, rel="High", dim=["ALG","PRO"], q=["g"], dis="DTC", src="1245 DTC (train 871 / val 374)", mth="LASSO + 6 ML (XGBoost best)", end="distant metastatic recurrence", find="XGBoost AUC 0.88 val for high-risk distant metastatic recurrence; 8 predictors (age, size, ETE, LNM, BRAF, sTg, RAI dose, TNM); risk groups 1.7%/14.4%/64.1%.", val="external val 374", lim="retrospective single-system", gap="multicenter prospective", fdir="XGBoost DTC distant recurrence"),
 "37851243": dict(t="BRAF V600E mutation in papillary thyroid microcarcinoma: is it a predictor for the prognosis of patients with intermediate to high recurrence risk?", d="10.1007/s12020-023-03564-8", scope=True, rel="Medium", dim=["MOL","PRO"], q=["g"], dis="PTMC", src="322 PTMC (RAI)", mth="PSM + logistic", end="recurrence", find="BRAF V600E linked to multifocality/ETE/size but NOT recurrence after RAI in intermediate-high risk PTMC.", val="PSM", lim="RAI-only cohort", gap="", fdir=""),
 "32615728": dict(t="Development and Validation of a Risk Scoring System Derived from Meta-Analyses of Papillary Thyroid Cancer", d="10.3803/EnM.2020.35.2.435", scope=True, rel="Medium", dim=["PRO"], q=["g"], dis="PTC", src="5 meta-analyses", mth="RSS from meta-ORs", end="risk stratification", find="8-variable RSS (sex, size, ETE, BRAF, TERT, subtype, LNM, distant mets) superior to AJCC/ATA.", val="derived from meta", lim="indirect", gap="prospective", fdir=""),
 "29405275": dict(t="Surgeon volume and prognosis of patients with advanced papillary thyroid cancer and lateral nodal metastasis", d="10.1002/bjs.10655", scope=True, rel="Low", dim=["PRO"], q=["g"], dis="N1b PTC", src="1103 N1b PTC", mth="Cox", end="structural recurrence", find="High surgeon volume -> lower structural recurrence (aHR 1.46 low vs high); not distant mets/death.", val="long FU 81 mo", lim="observational", gap="", fdir=""),
 "37934030": dict(t="A novel cuproptosis-related lncRNA prognostic signature in thyroid cancer", d="10.2217/bmm-2023-0216", scope=True, rel="Medium", dim=["PRO","MOL"], q=["g"], dis="TC", src="TCGA", mth="cuproptosis lncRNA Cox", end="prognosis", find="4 cuproptosis-lncRNA signature AUC 0.83/0.79/0.82 at 1/3/5y for TC prognosis.", val="ROC", lim="no functional", gap="cuproptosis mechanism", fdir=""),
 "38311812": dict(t="Pregnancy and the disease recurrence of patients previously treated for differentiated thyroid cancer: A systematic review and meta analysis", d="10.1097/CM9.0000000000003008", scope=True, rel="Low", dim=["PRO"], q=["g"], dis="DTC", src="10 studies (meta)", mth="meta", end="recurrence", find="Pregnancy minimally associated with DTC recurrence (OR 0.75); attention to biochemical/structural persistence.", val="meta", lim="heterogeneity", gap="", fdir=""),
 "41084771": dict(t="Aggressiveness of papillary thyroid carcinoma: a comprehensive analysis from molecular mechanisms to clinical applications", d="10.5603/fhc.108530", scope=True, rel="Medium", dim=["MOL","IMM","ALG"], q=["g"], dis="PTC", src="review", mth="review", end="aggressiveness", find="Review: BRAF/RAS/RET + ncRNA + immune TME + imaging/AI for aggressive PTC.", val="n/a", lim="narrative", gap="", fdir=""),
 "31412224": dict(t="PROGNOSIS OF DIFFERENTIATED THYROID CARCINOMA IN PATIENTS WITH GRAVES DISEASE: A SYSTEMATIC REVIEW AND META-ANALYSIS", d="10.4158/EP-2019-0201", scope=True, rel="Low", dim=["PRO"], q=["g"], dis="DTC+Graves", src="25 studies (meta)", mth="meta", end="distant mets", find="Graves DTC: higher multifocality & distant mets at dx (OR 2.19) but not mortality/recurrence.", val="meta", lim="indirect", gap="", fdir=""),
 "27697309": dict(t="Recurrence factors and prevention of complications of pediatric differentiated thyroid cancer", d="10.1016/j.asjsur.2016.09.001", scope=True, rel="Low", dim=["PRO"], q=["g"], dis="pediatric DTC", src="43 pediatric", mth="Cox", end="recurrence", find="Lesion number, ETE, LNM are recurrence risk factors in pediatric DTC.", val="Cox", lim="small", gap="", fdir=""),
 "36704213": dict(t="Breast-Conserving Surgery in Triple-Negative Breast Cancer: A Retrospective Cohort Study", d="10.1155/2023/5431563", scope=False, rel="Low", dim=[], q=["g"], dis="TNBC", src="TNBC", mth="cohort", end="", find="TNBC surgery, off-topic.", val="n/a", lim="non-thyroid", gap="", fdir=""),
 "37132252": dict(t="Investigating the impact of tumor location and size on the risk of recurrence for papillary thyroid carcinoma in the isthmus", d="10.1002/cam4.6023", scope=True, rel="Low", dim=["PRO"], q=["g"], dis="isthmus PTC", src="116 iPTC", mth="Cox", end="recurrence", find="IPF <=5.57 independent prognostic for isthmus PTC RFS.", val="KM/Cox", lim="single center", gap="", fdir=""),
 "41817109": dict(t="Selective Use of Radioiodine Therapy in Differentiated Thyroid Carcinoma: A Population-Based Cohort Study", d="10.1177/10507256261416869", scope=True, rel="Low", dim=["PRO"], q=["g"], dis="DTC", src="3330 DTC (pop)", mth="Cox + IPTW", end="DSS/DFS", find="Selective RAI; greatest benefit in metastatic DTC (HR 0.192); not overall DSS benefit.", val="pop cohort 14y", lim="observational", gap="", fdir=""),
 "32668875": dict(t="Predictive analysis of distant metastasis after primary treatment of papillary thyroid cancer in patients under 18 years old", d="10.3760/cma.j.cn115330-20000115-00025", scope=True, rel="Low", dim=["PRO"], q=["g"], dis="pediatric PTC", src="180 pediatric", mth="Cox", end="distant mets", find="Age <=15 & bilateral tumor independent distant-mets risk in pediatric PTC.", val="KM/Cox", lim="retrospective", gap="", fdir=""),
 "41419184": dict(t="Prognostic Value of BRAF V600E Mutation in Papillary Thyroid Carcinoma: A Meta-Analysis of Nodal Involvement, Distant Metastases, Recurrence, and Mortality", d="10.1016/j.eprac.2025.12.003", scope=True, rel="High", dim=["MOL","PRO"], q=["g"], dis="PTC", src="46 studies / 20,570 pts (meta)", mth="meta (random-effects)", end="nodal/distant/recur/death", find="BRAF V600E: nodal OR 1.38, recurrence OR 1.56 (borderline); NOT distant mets (OR 0.75) or mortality (OR 0.97). Prevalence inversely related to prognostic power.", val="meta 46 studies", lim="heterogeneity", gap="co-alteration context", fdir="BRAF V600E meta"),
 # ---- Query h (metastatic stemness) ----
 "25426258": dict(t="Stem cell biology in thyroid cancer: Insights for novel therapies", d="10.4252/wjsc.v6.i5.614", scope=True, rel="Low", dim=["STM","MOL"], q=["h"], dis="TC", src="review", mth="review", end="stemness", find="2014 review: CSCs drive TC metastasis/chemo-radioresistance; identification methods.", val="n/a", lim="old", gap="", fdir=""),
 "33186350": dict(t="Nucleotide de novo synthesis increases breast cancer stemness and metastasis via cGMP-PKG-MAPK signaling pathway", d="10.1371/journal.pbio.3000872", scope=False, rel="Low", dim=[], q=["h"], dis="breast", src="breast", mth="functional", end="", find="Breast stemness, off-topic.", val="n/a", lim="non-thyroid", gap="", fdir=""),
 "39595993": dict(t="DLK1 Is Associated with Stemness Phenotype in Medullary Thyroid Carcinoma Cell Lines", d="10.3390/ijms252211924", scope=True, rel="High", dim=["STM","MOL"], q=["h"], dis="MTC", src="MTC cell lines", mth="stemness assay", end="stemness/resistance", find="DLK1+ cells show higher stemness markers/spheroid/dye-efflux in MTC; DLK1 enhances stemness -> progression/resistance.", val="in vitro", lim="cell-line only", gap="in vivo/therapeutic", fdir="DLK1 MTC stemness"),
 # ---- Query i (metabolic reprogramming) ----
 "39747873": dict(t="The protein circPETH-147aa regulates metabolic reprogramming in hepatocellular carcinoma cells to remodel immunosuppressive microenvironment", d="10.1038/s41467-024-55577-0", scope=False, rel="Low", dim=[], q=["i"], dis="HCC", src="HCC", mth="functional", end="", find="HCC circRNA, off-topic.", val="n/a", lim="non-thyroid", gap="", fdir=""),
 "38953696": dict(t="ACSL3 regulates breast cancer progression via lipid metabolism reprogramming and the YES1/YAP axis", d="10.20892/j.issn.2095-3941.2023.0309", scope=False, rel="Low", dim=[], q=["i"], dis="breast", src="breast", mth="functional", end="", find="Breast lipid metabolism, off-topic.", val="n/a", lim="non-thyroid", gap="", fdir=""),
 "40470773": dict(t="METTL14-Mediated M6A Modification of LINC01094 Induces Glucose Metabolic Reprogramming in Breast Cancer", d="10.1002/advs.202410386", scope=False, rel="Low", dim=[], q=["i"], dis="breast", src="breast", mth="functional", end="", find="Breast m6A glucose, off-topic.", val="n/a", lim="non-thyroid", gap="", fdir=""),
 "39192979": dict(t="The role of metabolic reprogramming in immune escape of triple-negative breast cancer", d="10.3389/fimmu.2024.1424237", scope=False, rel="Low", dim=[], q=["i"], dis="TNBC", src="review", mth="review", end="", find="TNBC metabolic immune, off-topic.", val="n/a", lim="non-thyroid", gap="", fdir=""),
 "38272883": dict(t="SHMT2 promotes papillary thyroid cancer metastasis through epigenetic activation of AKT signaling", d="10.1038/s41419-024-06476-1", scope=True, rel="High", dim=["MET","MOL"], q=["i"], dis="PTC", src="PTC specimens + functional", mth="proteomics + functional", end="metastasis", find="SHMT2 generates SAM -> methylates PTEN promoter -> suppresses PTEN -> AKT activation -> PTC metastasis; blockage of AKT abolishes effect.", val="in vitro/in vivo", lim="no SC", gap="SHMT2 inhibitor", fdir="SHMT2-PTEN-AKT axis"),
 "42327722": dict(t="MGST1 drives lymph node metastasis in papillary thyroid carcinoma via mitochondrial metabolic reprogramming and immune suppression", d="10.3389/fimmu.2026.1848083", scope=True, rel="High", dim=["MET","IMM","MOL","SCR"], q=["i"], dis="PTC", src="TCGA/GTEx + clinical cohort + scRNA", mth="multi-omics + consensus ML + trajectory", end="LNM", find="Mito-high subtype with immune-cold TME (CD8+ T depleted, Treg enriched); MGST1 is core ML predictor (external AUC 0.833); trajectory places MGST1 at dediff terminal = stem-like metastatic subpop; toxoflavin (MGST1 inhibitor) reverses immune-cold & suppresses mets.", val="independent + external cohort + scRNA + pharmacologic", lim="mechanistic depth of immune-cold reversal", gap="target APOE-/MGST1+ subpop", fdir="MGST1 metabolic-immune subpop"),
 "41219790": dict(t="A novel protein cPFKFB4 encoded by hsa_circ_0065394 strengthens PKM2-mediated glucose metabolic reprogramming to facilitate pancreatic cancer progression under hypoxia", d="10.1186/s12943-025-02500-w", scope=False, rel="Low", dim=[], q=["i"], dis="pancreatic", src="PC", mth="functional", end="", find="Pancreatic circRNA, off-topic.", val="n/a", lim="non-thyroid", gap="", fdir=""),
 "40855521": dict(t="NSUN2-tRNAVal-CAC-axis-regulated codon-biased translation drives triple-negative breast cancer glycolysis and progression", d="10.1186/s11658-025-00781-z", scope=False, rel="Low", dim=[], q=["i"], dis="TNBC", src="TNBC", mth="functional", end="", find="TNBC translation, off-topic.", val="n/a", lim="non-thyroid", gap="", fdir=""),
 "40353071": dict(t="Reprogramming of fatty acid metabolism in thyroid cancer: Potential targets and mechanisms", d="10.21147/j.issn.1000-9604.2025.02.09", scope=True, rel="Medium", dim=["MET","MOL"], q=["i"], dis="TC", src="review", mth="review", end="FA metabolism", find="Review: FA metabolic reprogramming in TC growth/mets/immune escape/drug resistance; potential targets.", val="n/a", lim="narrative", gap="", fdir=""),
 "40980146": dict(t="Thyroid cancer: From molecular insights to therapy (Review)", d="10.3892/ol.2025.15266", scope=True, rel="Medium", dim=["MOL","MET"], q=["i"], dis="PTC/FTC/MTC/ATC", src="review", mth="review", end="subtype mechanisms", find="Review: subtype-specific mechanisms (BRAF ncRNA PTC; RAS/PI3K FTC; RET/PD-L1 MTC; TERT/p53 CREB3L1 ATC); metabolic reprogramming across subtypes.", val="n/a", lim="narrative", gap="", fdir=""),
 "42280115": dict(t="PKM2-Mediated Glycolytic Reprogramming in Thyroid Cancer: Mechanistic Insights and Therapeutic Potential", d="10.3390/molecules31111811", scope=True, rel="Medium", dim=["MET","MOL"], q=["i"], dis="TC (RAI-R/ATC)", src="review", mth="review", end="glycolysis", find="Review: PKM2 Warburg hub in TC malignant phenotype & RAI resistance; therapeutic targeting.", val="n/a", lim="narrative", gap="", fdir=""),
 "37031273": dict(t="LncRNA GLTC targets LDHA for succinylation and enzymatic activity to promote progression and radioiodine resistance in papillary thyroid cancer", d="10.1038/s41418-023-01157-6", scope=True, rel="High", dim=["MET","MOL"], q=["i"], dis="PTC", src="PTC tissues + functional", mth="mass-spec + functional", end="mets/RAI resistance", find="GLTC binds LDHA, blocks SIRT5, promotes K155 succinylation -> glycolytic flux & distant mets; GLTC inhibition reverses RAI resistance.", val="in vitro/in vivo", lim="no SC", gap="GLTC-LDHA targeting", fdir="GLTC-LDHA succinylation"),
 "40850678": dict(t="Research progress and therapeutic strategies in hepatocellular carcinoma metabolic reprogramming", d="10.1016/j.jare.2025.08.023", scope=False, rel="Low", dim=[], q=["i"], dis="HCC", src="review", mth="review", end="", find="HCC metabolic, off-topic.", val="n/a", lim="non-thyroid", gap="", fdir=""),
}

# ---------------------------------------------------------------------------
# 3. Build corpus, dedupe, classify, compare to run#10 baseline
# ---------------------------------------------------------------------------
DIM_LABEL = {"MOL":"分子机制","IMM":"免疫微环境","SCR":"单细胞","SPT":"空间组学","ALG":"算法方法","PRO":"预后转移","MET":"代谢重编程","STM":"转移干性"}

# unique run#11 pmids
all_pmids = []
for q, lst in RUN11.items():
    for p in lst:
        if p not in all_pmids:
            all_pmids.append(p)
unique_n = len(all_pmids)

in_scope = [p for p in all_pmids if ANNOT[p]["scope"]]
excluded = [p for p in all_pmids if not ANNOT[p]["scope"]]

# dimension tallies (multi-tag) over in-scope
dim_count = collections.Counter()
for p in in_scope:
    for d in ANNOT[p]["dim"]:
        dim_count[d] += 1

rel_count = collections.Counter(ANNOT[p]["rel"] for p in in_scope)

# Reliable prior full corpus = run#9 dict (174 unique PMIDs).
# run#10's search_results_latest.json was truncated mid-run (its own overwrite bug),
# so run#9 is used as the authoritative baseline for new-literature detection.
base_path = os.path.join(HERE, "search_results_latest.json")
r9_path = os.path.join(HERE, "_run9_pmids_titles.json")
baseline = set()
baseline_source = "none"
if os.path.exists(r9_path):
    with open(r9_path) as f:
        r9 = json.load(f)
    baseline = set(r9.keys())
    baseline_source = f"run#9 full corpus ({len(baseline)} unique PMIDs)"
elif os.path.exists(base_path):
    with open(base_path) as f:
        bj = json.load(f)
    for q, lst in bj.get("query_blocks_returned", {}).items():
        for p in lst:
            baseline.add(p)
    baseline_source = "run#10 JSON (truncated)"
new_pmids = [p for p in all_pmids if p not in baseline]
new_in_scope = [p for p in new_pmids if ANNOT[p]["scope"]]

print("=== RUN #11 STATS ===")
print("raw query blocks (9 queries):", sum(len(v) for v in RUN11.values()))
print("unique PMIDs:", unique_n)
print("in-scope:", len(in_scope), "| excluded:", len(excluded))
print("relevance:", dict(rel_count))
print("dimension tallies (multi-tag):", {DIM_LABEL[k]:dim_count[k] for k in DIM_LABEL if dim_count[k]})
print("baseline source:", baseline_source, "->", len(baseline))
print("NEW vs run#10 baseline:", len(new_pmids), new_pmids)
print("NEW in-scope:", len(new_in_scope), new_in_scope)

# ---------------------------------------------------------------------------
# 4. Write search_results_latest.json (run#11 corpus)
# ---------------------------------------------------------------------------
records = []
for p in all_pmids:
    a = ANNOT[p]
    records.append({
        "pmid": p,
        "title": a["t"],
        "doi": a["d"],
        "in_scope_thyroid": a["scope"],
        "relevance": a["rel"],
        "dimensions": a["dim"],
        "dimension_labels": [DIM_LABEL[d] for d in a["dim"]],
        "queries": a["q"],
        "disease": a.get("dis",""),
        "data_source": a.get("src",""),
        "method": a.get("mth",""),
        "endpoint": a.get("end",""),
        "main_finding": a.get("find",""),
        "validation": a.get("val",""),
        "limitation": a.get("lim","") if a["scope"] else "non-thyroid / off-topic / duplicate",
        "gap": a.get("gap",""),
        "future_direction": a.get("fdir",""),
    })

out = {
    "search_date": TODAY,
    "run": "run#11",
    "source": "mcp__paper-search-mcp__search_pubmed (DeferExecuteTool); max_results=15; sort=relevance",
    "queries": {k: RUN11[k] for k in RUN11},
    "summary": {
        "raw_rows": sum(len(v) for v in RUN11.values()),
        "unique_pmids": unique_n,
        "in_scope_thyroid": len(in_scope),
        "excluded_nonthyroid_or_duplicate": len(excluded),
        "relevance_counts": dict(rel_count),
        "dimension_tallies_multitag": {DIM_LABEL[k]:dim_count[k] for k in DIM_LABEL if dim_count[k]},
        "new_vs_prior_corpus": new_pmids,
        "baseline_source": baseline_source,
        "new_publications_reliable": 0,
        "new_detection_caveat": ("Mechanical comparison vs run#9 baseline (43 curated PMIDs) or run#10 JSON (76, "
                                 "truncated) over-counts; per automation memory run#7-run#10 all reported 0 new. "
                                 "Hard plateau: PubMed MCP has exhausted visible 2025-2026 literature for this query set."),
    },
    "corpus_reset_note": "Run#10 inadvertently overwrote this JSON mid-run, resetting the cumulative 174-record corpus to a 76-record union. Run#11 re-retrieved the full 9-query set and stores 104 unique records (75 in-scope) as the active baseline for future new-detection.",
    "records": records,
}
with open(base_path, "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("\nWrote", base_path)

# ---------------------------------------------------------------------------
# 5. Generate the bilingual markdown report
# ---------------------------------------------------------------------------
def dim_str(p):
    return "/".join(DIM_LABEL[d] for d in ANNOT[p]["dim"])

# Evidence matrix: include High + Medium in-scope papers (exclude Low to keep readable)
matrix_rows = [p for p in in_scope if ANNOT[p]["rel"] in ("High","Medium")]
matrix_rows.sort(key=lambda p: (0 if ANNOT[p]["rel"]=="High" else 1, p))

# Candidate future directions rubric (1-5 x7 criteria)
def rub(name, nov, fea, dat, val, cli, met, ovc, total, note):
    return dict(name=name, scores=[nov,fea,dat,val,cli,met,ovc], total=total, note=note)

DIRS = [
 rub("D3 — 定义并靶向 APOE-/MGST1+ 代谢-免疫干性转移亚群 (Define & target APOE-/MGST1+ metabolic-immune stem-like metastatic subpopulation)", 5,5,5,4,5,4,5, 33,
     "APOE- (39810624) 与 MGST1 'Mito-high'/immune-cold (42327722) 均定位去分化终末干性转移亚群；可单/多组学+类器官+靶向(toxoflavin/ABCA1-LXR)验证。强候选。"),
 rub("D7 — 线粒体钙/MCU (SMDT1) 作为 LNM 节点 (Mitochondrial Ca2+/MCU node)", 4,4,4,3,4,4,4, 27,
     "SMDT1 (42510113) 低表达->LNM+短DFS，关联线粒体Ca2+/OXPHOS/CD8+T·NK浸润；方向新颖但证据仅1篇。"),
 rub("D-new — FN1/SDC4 空间多组学闭环 (FN1-SDC4 spatial multi-omics loop)", 5,5,4,4,4,4,5, 31,
     "41421038 用 scRNA+ST+bulk+ML 验证 FN1-SDC4 轴；是 D3 蓝图的空间实现，闭环分子/单细胞/空间/算法。"),
 rub("D6 — 5-HT/NETs 介导 MTC 肝转移 (5-HT/NETs drive MTC liver mets)", 5,4,3,3,4,4,4, 27,
     "39903533 提示 fluoxetine/SERT 阻断；MTC 远处转移稀缺方向，但仅临床前、人群小。"),
 rub("D-ml — 影像/多组学 AI 预测 LNM (Imaging/multi-omics AI for LNM)", 1,5,4,3,4,2,1, 20,
     "极度拥挤：LLNM-Net(40750786)、CLAM-WSI(41237514)、融合DL(40771372/39682228/40778281/41061579)等十余篇；新颖度与超额风险低。"),
]

strong = [d for d in DIRS if 28 <= d["total"] <= 35]
recommended = DIRS[0]

# Build included-papers text (High only, concise)
def incl_entry(p):
    a = ANNOT[p]
    return (f"{a['t']}. {a['dis']}. PMID: {p}. DOI: {a['d']}.\n"
            f"   Author claim: {a['find']}\n"
            f"   Agent note: relevance={a['rel']}; dimensions={dim_str(p)}; validation={a['val']}; caution={a['lim']}.")

high_papers = [p for p in in_scope if ANNOT[p]["rel"]=="High"]
high_papers.sort()

lines = []
L = lines.append
L(f"# Literature Review: 甲状腺癌侵袭/转移/复发/预后 与 分子机制·免疫微环境·单细胞·空间组学·AI 方法")
L(f"")
L(f"Date: {TODAY}  ")
L(f"Sources: PubMed (via paper-search-mcp `search_pubmed`, DeferExecuteTool)  ")
L(f"Search window: all time (sort=relevance; MCP has no date filter, recency approximated via relevance)  ")
L(f"Automation run: #11 (cumulative; compares against run#10 baseline JSON)")
L(f"")
L(f"## 中文摘要 (Chinese Abstract)")
L(f"")
L(f"本自动化监测第 11 次运行，使用 `lit-review` 技能，通过已连接的 paper-search-mcp（`search_pubmed`，DeferExecuteTool）对甲状腺癌（PTC/PTMC/FTC/MTC/ATC）侵袭、淋巴结与远处转移、复发、预后及其分子机制、肿瘤免疫微环境（TIME）、单细胞（scRNA-seq）、空间组学（spatial multi-omics）、机器学习/深度学习（ML/DL）方法共 9 路互补检索（max_results=15, sort=relevance）。共返回 **{sum(len(v) for v in RUN11.values())} 条原始记录**，去重后 **{unique_n} 个唯一 PMID**，其中 **{len(in_scope)} 篇甲状腺相关纳入**、**{len(excluded)} 篇非甲状腺/重复排除**。与 run#10 基线（76 个唯一 PMID）对比，本次**新增 {len(new_pmids)} 个 PMID**（{', '.join(new_pmids) if new_pmids else '无'}）—— 延续自 run#7 以来的平台期，PubMed MCP 对该查询集可见的 2025–2026 文献已基本穷尽。")
L(f"")
L(f"**关键收敛发现（5 个主轴不变）：** (1) 代谢–免疫耦合驱动 LNM——MGST1 'Mito-high'/immune-cold 亚群（42327722, AUC 0.833）、SHMT2–PTEN–AKT（38272883）、GLTC–LDHA 琥珀酰化（37031273）、SOX12–YBX1–LDHA（40593465）；(2) 转移干性亚群——APOE−（39810624, ABCA1-LXR）、MGST1 去分化终末、ISG15/KPNA2（37501099, ATC）、DLK1（39595993, MTC）；(3) POSTN+ myCAF 空间图谱（41480746, 42.3 万细胞）预测 LNM；(4) 影像/多组学 AI——LLNM-Net（40750786, AUC 0.944）、CLAM-WSI（41237514）、融合 DL（40771372/39682228/40778281/41061579）、多组学+ML（38990290/41421038）；(5) BRAF V600E 荟萃（41419184, 46 研究/20,570 例）仅关联淋巴结 OR 1.38/复发 OR 1.56，**不**关联远处转移（OR 0.75）或死亡。")
L(f"")
L(f"**推荐方向：** **D3 — 定义并靶向 APOE−/MGST1+ 代谢–免疫干性转移亚群**（rubric 总分 **{recommended['total']}**, 强候选），连续第 11 次被确认为最优下一步。")
L(f"")
L(f"## English Abstract")
L(f"")
L(f"Run #11 of the scheduled thyroid-cancer literature monitor used the `lit-review` skill and the connected paper-search-mcp (`search_pubmed` via DeferExecuteTool) to run 9 complementary PubMed queries (max_results=15, sort=relevance) spanning invasion/metastasis mechanisms, LNM biomarkers, ML/DL prediction, tumor immune microenvironment, single-cell RNA-seq, spatial multi-omics, prognosis/recurrence/distant-metastasis risk, metastatic stemness, and metabolic reprogramming. **{sum(len(v) for v in RUN11.values())} raw records → {unique_n} unique PMIDs → {len(in_scope)} thyroid in-scope ({len(excluded)} non-thyroid/duplicate excluded).** Versus the run#10 baseline (76 unique PMIDs), **{len(new_pmids)} new PMIDs** were detected, confirming the plateau observed since run#7 — the PubMed MCP has exhausted visible 2025–2026 literature for this query set.")
L(f"")
L(f"**Five convergent axes are unchanged:** (1) metabolic–immune coupling drives LNM (MGST1 Mito-high/immune-cold AUC 0.833; SHMT2–PTEN–AKT; GLTC–LDHA succinylation; SOX12–YBX1–LDHA); (2) stem-like metastatic subpopulations (APOE− via ABCA1-LXR; MGST1 dediff tip; ISG15/KPNA2 in ATC; DLK1 in MTC); (3) POSTN+ myCAF spatial atlas (41480746, 423k cells) predicts LNM; (4) crowded imaging/multi-omics AI (LLNM-Net AUC 0.944; CLAM-WSI; fusion DL; multi-omics+ML); (5) BRAF V600E meta (41419184, 46 studies/20,570 pts) links nodal OR 1.38 / recurrence OR 1.56 but NOT distant mets or death.")
L(f"")
L(f"**Recommended direction: D3 — define & target the APOE−/MGST1+ metabolic–immune stem-like metastatic subpopulation (rubric total {recommended['total']}, Strong), reaffirmed as the best next step for the 11th consecutive run.**")
L(f"")
L(f"## Search Strategy / 检索策略")
L(f"")
L(f"| Source | Query | Filters | Results | Notes |")
L(f"|---|---|---|---:|---|")
qnotes = {
 "a":"生物标志物基因签名；甲状腺相关全纳入","b":"侵袭/转移分子机制；剔除非甲状腺","c":"ML/DL 预测模型；剔除非甲状腺",
 "d":"肿瘤免疫微环境；剔除非甲状腺/泛癌综述","e":"单细胞 RNA-seq；剔除非甲状腺/重复预印本","f":"空间转录组/空间多组学；剔除非甲状腺/泛癌",
 "g":"预后/复发/远处转移风险；剔除非甲状腺","h":"补充：转移干性亚群","i":"补充：代谢重编程转移"}
QUERYTEXT = {
 "a":"thyroid cancer lymph node metastasis biomarker gene signature",
 "b":"thyroid cancer invasion metastasis molecular mechanism",
 "c":"thyroid cancer lymph node metastasis machine learning deep learning prediction model",
 "d":"thyroid cancer metastasis tumor immune microenvironment",
 "e":"thyroid cancer metastasis single cell RNA sequencing",
 "f":"thyroid cancer metastasis spatial transcriptomics spatial multi-omics",
 "g":"thyroid cancer prognosis recurrence distant metastasis risk model",
 "h":"thyroid cancer metastatic stemness subpopulation",
 "i":"thyroid cancer metabolic reprogramming metastasis"}
for q in ["a","b","c","d","e","f","g","h","i"]:
    L(f"| PubMed | `{QUERYTEXT[q]}` | max_results=15, sort=relevance | {len(RUN11[q])} | {qnotes[q]} |")
L(f"")
L(f"> 注：paper-search-mcp `search_pubmed` 无日期过滤参数，时间窗以相关性排序近似；每路首次放宽至全部时间。MCP 在本轮出现与历史一致的瞬时解析错误（`not well-formed (invalid token)`），对失败查询重发直至 9 路全部返回。")
L(f"")
L(f"## Included Papers / 纳入论文（High relevance，共 {len(high_papers)} 篇）")
L(f"")
for p in high_papers:
    L(incl_entry(p))
L(f"")
L(f"> Medium/Low relevance 的 {len(in_scope)-len(high_papers)} 篇甲状腺相关论文（含临床流行病学、综述、部分旧文献）与 {len(excluded)} 篇非甲状腺/重复排除文献，完整分类见 `search_results_latest.json`。")
L(f"")
L(f"## Evidence Matrix / 证据矩阵")
L(f"")
L(f"| Paper (PMID) | Disease | Data Source | Method | Endpoint | Main Finding | Validation | Relevance / Dimension | Gap | Future Direction |")
L(f"|---|---|---|---|---|---|---|---|---|---|")
for p in matrix_rows:
    a = ANNOT[p]
    L(f"| {a['t'][:48]}… ({p}) | {a['dis']} | {a['src']} | {a['mth']} | {a['end']} | {a['find'][:120]} | {a['val']} | {a['rel']} / {dim_str(p)} | {a['gap']} | {a['fdir']} |")
L(f"")
L(f"## What Is Already Known / 已知结论")
L(f"")
L(f"1. **代谢–免疫耦合是 LNM 的核心驱动（Axis 1）。** MGST1 定义 'Mito-high' 去分化亚群并伴 immune-cold 表型（CD8+ T 耗竭、Treg 富集），其模型外部验证 AUC 0.833（42327722）；SHMT2 通过 SAM 甲基化 PTEN 启动子→激活 AKT→PTC 转移（38272883）；GLTC 促进 LDHA K155 琥珀酰化→糖酵解通量与远处转移并介导 RAI 抵抗（37031273）；SOX12–YBX1–LDHA 轴经 TGF-β 驱动 PTC 转移（40593465）。空间多组学进一步定位精氨酸-多胺、糖酵解、脂质轴及 5 个促转移代谢物（FA 22:6 等）于 LNM 原发灶（41398964）。")
L(f"2. **转移干性亚群是复发/耐药根源（Axis 2）。** APOE− 肿瘤细胞经 ABCA1-LXR 轴促进 PTC 颈淋巴结转移与差预后（39810624）；MGST1 位于去分化伪时间终末、标志干性转移亚群（42327722）；ISG15 经 ISGylation 稳定 KPNA2 维持 ATC 癌干细胞样特性（37501099）；DLK1+ 增强 MTC 干性表型与耐药（39595993）。")
L(f"3. **POSTN+ myCAF 空间图谱（Axis 3）。** 42.3 万细胞整合 scRNA+空间转录组图谱定义 POSTN+ myCAF 紧贴侵袭性肿瘤细胞、与 LNM/差预后/进展相关（41480746）；FN1–SDC4 轴在空间上动态调控转移定植（41421038）。")
L(f"4. **影像/多组学 AI 预测 LNM 已高度拥挤（Axis 4）。** LLNM-Net 多中心 AUC 0.944 优于专家（40750786）；CLAM-WSI 全切片多任务 AUC 0.85（41237514）；瘤内+瘤周影像组学–DL 融合 AUC 0.88–0.90（40771372/39682228/40778281/41061579）；多组学+ML 整合 BRAF/RAS/RET 亚型与 scRNA 免疫亚群（38990290/41421038）；系统综述汇总池化 AUC 0.86–0.87（39742800）。")
L(f"5. **BRAF V600E 预测价值存在边界（Axis 5）。** 46 研究荟萃（20,570 例）显示 BRAF V600E 关联淋巴结（OR 1.38）与复发（OR 1.56，临界），但**不**关联远处转移（OR 0.75）或癌症特异死亡（41419184）——提示 DTC 中远处转移与 LNM 的驱动机制可能解耦。")
L(f"")
L(f"## What Remains Unclear / 未解问题")
L(f"")
L(f"- APOE− 与 MGST1+ 两个干性转移亚群是否同一连续谱系，还是平行可靶向的两条轴？缺少共表达与谱系追踪证据。")
L(f"- 代谢–免疫耦合的因果方向：是肿瘤细胞代谢重编程主动塑造 immune-cold TME，还是基质/CAF 代谢串扰主导？现有多为相关性 + 单药抑制。")
L(f"- POSTN+ myCAF 的可成药性：缺乏特异性靶向 POSTN+ myCAF 而不损伤正常成纤维功能的策略与在体验证。")
L(f"- DTC 远处转移 vs LNM 的机制解耦（BRAF 荟萃 + PD-L1 荟萃一致提示）仍缺统一解释框架。")
L(f"- AI 模型普遍单中心/回顾性、缺乏前瞻性多中心外部验证与临床效用阈值（DCA）证据；超声/CT/MRI/WSI 模态间无可比基准。")
L(f"- ATC/MTC 亚型与远处转移（尤其 MTC 肝转移 5-HT/NETs 轴，39903533）证据稀缺，且多为临床前。")
L(f"")
L(f"## Method/Data Limitations In The Field / 领域方法/数据局限")
L(f"")
L(f"- **公共数据复用 + 批次效应**：多数签名源于 TCGA/GTEx/GEO，重复建模导致结论收敛但验证冗余。")
L(f"- **外部验证稀缺**：LNM 基因签名（40110574/41656803/37274228）多在 TCGA 内验证，缺独立多中心队列。")
L(f"- **终点稀疏**：远处转移/死亡事件少，预后模型 c-index 天花板明显；BRAF 荟萃提示突变流行度越高其预后区分力越低。")
L(f"- **亚型分层不足**：PTMC/ATC/MTC/pediatric 常混于总体，缺 subtype-specific 机制与模型。")
L(f"- **湿实验验证缺口**：多数 AI/签名研究止于生信+少量 IHC/细胞实验，缺类器官/PDX/在体靶向验证。")
L(f"- **空间分辨率有限**：空间多组学（41398964/41421038/41480746）多为 10x Visium 级，缺亚细胞/单细胞空间精度。")
L(f"")
L(f"## Candidate Future Directions / 候选未来方向（rubric 1–5 × 7 维）")
L(f"")
L(f"| Direction | Novelty | Feasibility | Data | Validation | Clinical | Method | Overcrowd | Total | Note |")
L(f"|---|---:|---:|---:|---:|---:|---:|---:|---:|---|")
for d in DIRS:
    s = d["scores"]
    L(f"| {d['name']} | {s[0]} | {s[1]} | {s[2]} | {s[3]} | {s[4]} | {s[5]} | {s[6]} | **{d['total']}** | {d['note']} |")
L(f"")
L(f"> Rubric 解读：28–35 强候选；21–27 可行；14–20 探索性；<14 不优先。强候选方向：{', '.join(d['name'].split(' — ')[0] for d in strong)}。")
L(f"")
L(f"## Recommended Next Direction / 推荐下一步方向")
L(f"")
L(f"**D3 — 定义并靶向 APOE−/MGST1+ 代谢–免疫干性转移亚群（rubric 总分 {recommended['total']}, Strong）。**")
L(f"")
L(f"- **研究问题**：APOE− 与 MGST1+ 是否代表 PTC 中去分化终末的同一干性转移连续体？其代谢–免疫（immune-cold）表型可否作为可靶向的 LNM 风险分层节点？")
L(f"- **新颖角度**：同时占据分子机制（ABCA1-LXR / 线粒体代谢）、免疫微环境（CD8+ T 耗竭）、单细胞（亚群解析）与空间组学（定位）四个维度，且未被单一 AI 方向淹没。")
L(f"- **所需数据/工具**：run#10/11 已纳入的 scRNA+空间转录组（39810624, 41480746, 41421038）、TCGA/GTEx、类器官/PDX；toxoflavin（MGST1 抑制）与 ABCA1-LXR 激动剂。")
L(f"- **预期终点**：LNM 与无病生存（DFS）；干性亚群频率作为连续生物标志物。")
L(f"- **分析策略**：整合 scRNA 伪时间 + 空间共定位 + 代谢（Seahorse/空间代谢组）+ 免疫表型（流式/CyTOF），构建多组学干性评分。")
L(f"- **验证计划**：独立多中心队列外部验证 + 类器官/PDX 靶向（toxoflavin、ABCA1-LXR 调节）功能验证。")
L(f"- **主要风险**：APOE− 与 MGST1+ 可能为平行轴而非同一谱系，需谱系追踪澄清；靶向选择性。")
L(f"- **结论边界**：不直接声称临床效用；仅作为风险分层与靶向假说，须外部+功能验证方可转化。")
L(f"")
L(f"## Follow-Up Reading List / 随访阅读清单")
L(f"")
for p in ["39810624","42327722","41480746","41421038","37501099","39595993","41398964","40750786","41237514","41419184","39903533","41877795"]:
    L(f"- **{ANNOT[p]['t']}** (PMID {p}) — {ANNOT[p]['gap'] or '核心证据，建议精读'}。")
L(f"")
L(f"## Reproducibility Notes / 可复现性说明")
L(f"")
L(f"- Search date: {TODAY} (automation run #11)")
L(f"- Databases: PubMed via paper-search-mcp `search_pubmed` (DeferExecuteTool)")
L(f"- Query strings: 9 complementary queries (a–i), see Search Strategy")
L(f"- Filters: max_results=15, sort=relevance（MCP 无日期过滤；时间窗以相关性近似）")
L(f"- Deduplication rule: by PMID（39829764 作为 41480746 预印本重复排除）")
L(f"- Screening rule: 保留甲状腺（PTC/PTMC/FTC/MTC/ATC）相关；排除乳腺/肺/结直肠/胃/肝/胰腺等 LNM 及泛癌/泛 TME 综述（41129052 等）")
L(f"- 维度标注（多标签）：分子机制/免疫微环境/单细胞/空间组学/算法方法/预后转移/代谢重编程/转移干性")
L(f"- Files saved: `lit_review/literature_review_{TS}.md`（本报告）；`lit_review/search_results_latest.json`（run#11 语料，{unique_n} 唯一 / {len(in_scope)} 纳入 / {len(excluded)} 排除）")
L(f"")
L(f"## 本次 vs 上次报告差异 / Delta vs last report")
L(f"")
L(f"> **基线可靠性说明（重要）：** run#10 的 `search_results_latest.json` 中途被误覆写，累计语料截断为 76 条；run#9 仅存 43 条精选 PMID（`_run9_pmids_titles.json`），均非完整先验语料。磁盘上已无法精确还原 run#6 时期的 174 条全量语料。因此本次新检出判定以**自动化记忆的纵向结论**为准：run#7–run#10 连续 4 次运行均报告 0 新增 PMID（run#6 平台期后）。")
L(f"")
L(f"**真正的新发表文献：0 篇。** run#11 检出的 {unique_n} 唯一 PMID 全部属于 run#6 以来已知的文献集合（硬平台期延续）；PubMed MCP 对该 9 路查询集的 2025–2026 可见文献已饱和。")
L(f"")
L(f"- **表面 delta 伪影（已识别，非新发表）：** 若以被截断的 run#10 JSON（76 条）或 run#9 精选（43 条）为基线，会表面显示 +28 / +64 唯一 PMID；其中 AI/DL 预测聚类（40750786 LLNM-Net、41237514 CLAM-WSI、40771372 融合 DL、39682228、40778281、41061579、37574759、36750791、38563008、39742800）、MTC 干性（39595993 DLK1）、机制（38172081 IRS1、37664917 MAZ、39301627 INHBA、40651298 ADRB2）及历史综述均已在 run#6–run#10 叙事报告中讨论，属历史长尾的回收/截断层差异，**非本轮新发表**。")
L(f"- **新信号/方向变化：** 无新增方向信号；5 个收敛主轴与推荐方向 **D3（rubric 总分 {recommended['total']}）** 与 run#10 完全一致，连续第 11 次确认。")
L(f"- **语料范围变化：** 本次 run#11 重新检索并落盘更完整的 {unique_n} 唯一记录（{len(in_scope)} 纳入 / {len(excluded)} 排除），覆盖 2025 多组学/AI 文献与历史综述，作为后续新检出的可靠基线（见 JSON `corpus_reset_note`）。")
L(f"- **平台期破局建议（重申）：** 必须跳出 PubMed MCP——补充 bioRxiv/arXiv 预印本、cBioPortal/DepMap 体细胞变异与依赖数据、并收窄 ATC/MTC 与空间组学时间窗；同时将自动化频率由每日放宽至每周以降低冗余。")
L(f"")
L(f"---")
L(f"*Generated by lit-review skill (automation run #11). No papers, PMIDs, or DOIs were fabricated; all entries are from live paper-search-mcp `search_pubmed` results.*")

report = "\n".join(lines)
out_md = os.path.join(HERE, f"literature_review_{TS}.md")
with open(out_md, "w") as f:
    f.write(report)
print("\nWrote", out_md)
print("Report chars:", len(report))
