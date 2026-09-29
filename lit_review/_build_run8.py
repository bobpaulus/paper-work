#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build run #8 literature_review corpus delta + search_results_latest.json.

Loads run #7 search_results_latest.json, compares against this run's 9-query
results (sort=pub_date recency sweep), identifies genuinely NEW papers, and
rebuilds the cumulative corpus JSON with updated counts.
"""
import json, os, datetime

BASE = os.path.dirname(os.path.abspath(__file__))
EXISTING = os.path.join(BASE, "search_results_latest.json")

# ---- THIS RUN (run #8) raw results: all 9 queries, sort=pub_date ----
# fields: pmid, query(single letter), title, doi, year, disease,
#         in_scope(bool), relevance, dimensions(list), note
this_run = [
    # --- query a: biomarker gene signature ---
    ("41701943","a","DNA Methylation-Based Risk Stratification and Classification of Pediatric Thyroid Carcinoma.","10.1158/1078-0432.CCR-25-2109",2026,"pediatric TC","thyroid",True,"High",["algorithm","molecular"],"Methylation classifiers predict invasiveness/nodal mets + driver mutation in pediatric TC."),
    ("41368991","a","BRAF V600E in thyroid cancer: navigating prognostic uncertainty and therapeutic opportunity.","10.1530/ETJ-25-0225",2025,"PTC","thyroid",True,"Medium",["molecular"],"Review: BRAF V600E prognostic controversy + targeted therapy."),
    ("41656803","a","[A multi-molecular predictive model for lymph node metastasis in papillary thyroid carcinoma based on machine learning algorithms].","10.11817/j.issn.1672-7347.2025.250216",2025,"PTC","thyroid",True,"High",["algorithm","molecular"],"11-gene ML LNM model (FN1/PI15/IL11/PLA2G5...) AUC 0.80/0.79 across 6 ML algos."),
    ("40977710","a","Multi-omics analysis and metastasis risk factor prediction in N1b stage PTMC: insights into immune infiltration and therapeutic implications.","10.3389/fimmu.2025.1620085",2025,"PTMC","thyroid",True,"High",["algorithm","immune","single-cell"],"N1b PTMC: NLR model AUC 0.852; 4-gene classifier (ALDH1A3/CTXN1/MGAT3/TMEM163) AUC 0.857."),
    ("40741176","a","Development and validation of mRNA expression-based classifiers to predict low-risk thyroid tumors.","10.3389/fendo.2025.1600815",2025,"TC","thyroid",True,"High",["algorithm"],"mRNA classifiers rule out invasion/LNM NPV 97.6-100% (Afirma cohort)."),
    ("40025314","a","UBC9: a novel therapeutic target in papillary thyroid carcinoma.","10.1007/s40618-024-02523-y",2025,"PTC","thyroid",True,"Low",["molecular","immune"],"UBC9 knockdown inhibits PTC proliferation/migration; immune-linked."),
    ("40110574","a","Identification of Novel Gene Signature Predicting Lymph Node Metastasis in Papillary Thyroid Cancer via Bioinformatics Analysis and in vitro Validation.","10.2147/IJGM.S502480",2025,"PTC","thyroid",True,"High",["molecular","prognosis"],"6-gene LNM signature COL8A2/MET/FN1/MPZL2/PDLIM4/CLDN10 (TCGA+GEO+GSE60542)."),
    ("40001321","a","Comprehensive transcriptomic profiling reveals molecular characteristics and biomarkers associated with risk stratification in papillary thyroid carcinoma.","10.1002/2056-4538.70022",2025,"PTC","thyroid",True,"Medium",["molecular","prognosis"],"31-gene PTCrisk signature validated multi-cohort; linked LNM/BRAF."),
    ("40171809","a","A nomogram based on the 3-gene signature and clinical characteristics for predicting lymph node metastasis in papillary thyroid cancer.","10.1177/18758592241311195",2025,"PTC","thyroid",True,"Medium",["prognosis","algorithm"],"3-gene nomogram IQGAP2/BTBD11/MT1G AUC 0.802/0.718."),
    ("39497824","a","Coagulation-related genes for thyroid cancer prognosis, immune infiltration, staging, and drug sensitivity.","10.3389/fimmu.2024.1462755",2024,"THCA","thyroid",True,"Medium",["prognosis","immune"],"D-dimer predicts lateral LNM; 8-gene coagulation prognostic model."),
    ("38233939","a","TIPARP as a prognostic biomarker and potential immunotherapeutic target in male papillary thyroid carcinoma.","10.1186/s12935-024-03223-6",2024,"PTC","thyroid",True,"Medium",["immune","prognosis","molecular"],"11-gene male-PTC LNM signature; TIPARP validated by IHC."),
    ("37274228","a","Identification of key immune genes related to lymphatic metastasis of papillary thyroid cancer via bioinformatics analysis and experimental validation.","10.3389/fonc.2023.1181325",2023,"PTC","thyroid",True,"High",["immune","molecular"],"MET/ICAM1/PTGS2 immune-gene LNM signature (TCGA+WGCNA+LASSO/RF)."),
    ("35388548","a","Analysis of anti-apoptotic PVT1 oncogene and apoptosis-related proteins (p53, Bcl2, PD-1, and PD-L1) expression in thyroid carcinoma.","10.1002/jcla.24390",2022,"TC","thyroid",True,"Medium",["molecular","immune"],"PVT1 up; high PD-L1 linked mortality; PD-1 linked LNM."),
    ("35255661","a","Transcriptomic Analysis of Papillary Thyroid Cancer: A Focus on Immune-Subtyping, Oncogenic Fusion, and Recurrence.","10.21053/ceo.2021.02215",2022,"PTC","thyroid",True,"Medium",["immune","prognosis"],"HOXD9 recurrence marker; immune-escape signature in advanced PTC."),
    ("35033555","a","A four-enhancer RNA-based prognostic signature for thyroid cancer.","10.1016/j.yexcr.2022.113023",2022,"TC","thyroid",True,"Medium",["prognosis","algorithm"],"4-eRNA signature predicts prognosis, linked N stage."),

    # --- query b: invasion/metastasis mechanism ---
    ("42517063","b","miR-1911-3p Regulates Malignant Biological Behaviors and Glycolytic Activity of Triple-Negative Breast Cancer via FBLN5.","10.2147/BCTT.S615715",2026,"TNBC","offtopic",False,"Low",["offtopic"],"TNBC miR-1911-3p/FBLN5 glycolysis; non-thyroid."),
    ("42464297","b","The NLRP3 inflammasome in gastrointestinal malignancies: molecular mechanisms, regulatory networks, and therapeutic opportunities.","10.1186/s12967-026-08565-5",2026,"GI","offtopic",False,"Low",["offtopic"],"GI NLRP3 review; non-thyroid."),
    ("42409802","b","Intratumoral microbiota in tumorigenesis: A double-edged sword.","10.1097/CM9.0000000000004178",2026,"pan-cancer","offtopic",False,"Low",["offtopic"],"Pan-cancer intratumoral microbiota review; non-thyroid-specific."),
    ("42343437","b","FBXO5 regulates RPL23A to promote MDM2-mediated p53 degradation and facilitate malignant progression of breast cancer.","10.1186/s13058-026-02335-3",2026,"breast","offtopic",False,"Low",["offtopic"],"Breast cancer FBXO5/RPL23A/p53; non-thyroid."),
    ("42330341","b","Neuron-Derived MIF Engages VCAM1 to Fuel a Self-Amplifying CXCL8 Loop That Drives Perineural Invasion and Metastasis in Gastric Cancer.","10.1002/advs.76195",2026,"gastric","offtopic",False,"Low",["offtopic"],"Gastric PNI MIF-VCAM1-CXCL8; non-thyroid."),
    ("42301557","b","DLEU2 promotes the migration and invasion of papillary thyroid carcinoma cells through the ELAVL1/RCC2 axis.","10.1007/s10142-026-01936-7",2026,"PTC","thyroid",True,"High",["molecular"],"lncRNA DLEU2-ELAVL1-RCC2 drives PTC migration/invasion via Wnt5a/b-catenin/EMT."),
    ("42237330","b","TRIM71 suppresses cervical cancer progression by inhibiting Nectin4-mediated Wnt/beta-catenin signaling.","10.1186/s13062-026-00843-y",2026,"cervical","offtopic",False,"Low",["offtopic"],"Cervical cancer TRIM71/Nectin4; non-thyroid."),
    ("42305510","b","Identification and validation of tumor microenvironment remodeling markers associated with prognosis in differentiated thyroid cancer.","10.21037/tcr-2026-1-0208",2026,"DTC","thyroid",True,"High",["immune","prognosis","algorithm"],"TER 5-gene (CAMP/DDIT4L/LMX1B/NAT16/CALN1) prognostic model AUC 0.96-1.00; 101 ML algos."),
    ("42351648","b","FOXP Transcription Factors in Thyroid Cancer: From Molecular Expression to Clinical Significance.","10.3390/biomedicines14061222",2026,"TC","thyroid",True,"Medium",["molecular"],"Review: FOXP1-4 in TC; FOXP3/FOXP4 linked LNM/distant mets, radioiodine resistance."),
    ("42222424","b","Methylation-regulated miR-374a-5p and miR-374b-5p suppress glycolysis and malignant progression of head and neck squamous cell carcinoma by targeting DEPDC1.","10.3389/fonc.2026.1816226",2026,"HNSCC","offtopic",False,"Low",["offtopic"],"HNSCC miR-374/DEPDC1 glycolysis; non-thyroid."),
    ("41879411","b","Inhibitory effect of vemurafenib combined with panobinostat on human anaplastic thyroid cancer cells.","10.36721/PJPS.2026.39.5.REG.13646.1",2026,"ATC","thyroid",True,"Medium",["molecular","metabolic"],"Ve+Pa synergistically suppresses ATC growth/mets, promotes redifferentiation (GLUT1 down)."),
    ("42002564","b","The mechanism of fibronectin 1 promoting papillary thyroid cancer progression by regulating anoikis resistance.","10.1038/s41598-026-43495-8",2026,"PTC","thyroid",True,"High",["molecular","metabolic"],"FN1 promotes PTC progression via anoikis resistance (BCL2L1/BAD); linked poor prognosis."),
    ("41964784","b","Lipocalin 2 promotes papillary thyroid cancer progression through activation of glycolysis via Hippo/YAP1/HIF1alpha axis.","10.1007/s40618-026-02887-3",2026,"PTC","thyroid",True,"High",["molecular","metabolic"],"LCN2 drives PTC glycolysis/progression via Hippo/YAP1/HIF1alpha; linked LNM/ETE."),
    ("41759425","b","Saikosaponin D inhibits gastric cancer progression by targeting PKM2-mediated glycolysis and histone lactylation.","10.1016/j.phymed.2026.157993",2026,"gastric","offtopic",False,"Low",["offtopic"],"Gastric cancer PKM2/lactylation; non-thyroid."),
    ("41539369","b","circPTPRM can encode a functional polypeptide circPTPRM-187aa to promote papillary thyroid carcinoma progression.","10.1016/j.mce.2026.112734",2026,"PTC","thyroid",True,"High",["molecular"],"circPTPRM-187aa (translatable circRNA) promotes PTC prolif/migration/invasion via IQGAP1/TGF-b."),

    # --- query c: ML/DL prediction ---
    ("42185182","c","Prediction and Clinical Application of Central Lymph Node Metastasis in Papillary Thyroid Carcinoma Based on Multi-modal Ultrasound Feature Fusion: A Multi-center Study.","10.1016/j.ultrasmedbio.2026.04.024",2026,"PTC","thyroid",True,"High",["algorithm"],"Multi-modal US DL (EfficientNet-B4 fusion) CLNM AUC 0.929/0.843 external; 4-center."),
    ("42433575","c","Enhancing BRAF V600E mutation prediction in thyroid cancer through interpretable deep learning models combining clinical and ultrasound-based radiomics features.","10.21037/qims-2026-1-0299",2026,"PTC","thyroid",True,"High",["algorithm"],"Interpretable DL+radiomics BRAF V600E AUC 0.845; SHAP/Grad-CAM."),
    ("41997788","c","Diagnostic Accuracy of Ultrasound Radiomics for Cervical Lymph-Node Metastasis in Papillary Thyroid Carcinoma: Evidence Predominantly From Chinese Cohorts.","10.1016/j.ultrasmedbio.2026.01.017",2026,"PTC","thyroid",True,"High",["algorithm"],"SR/MA 60 studies (10,852 pts): radiomics AUC 0.83, +clinical 0.88; lateral 0.94."),
    ("42244944","c","Bilateral disease in the classic subtype of papillary thyroid carcinoma: clinical significance and development of an artificial intelligence-based multimodal prediction model.","10.3389/fendo.2026.1759451",2026,"PTC","thyroid",True,"High",["algorithm","prognosis"],"Bilateral PTC AI model AUC 0.970/0.932/0.848; recurrence HR 9.664."),
    ("42031943","c","Deep learning-based multimodal radiopathomics for preoperative prediction of lymph node metastasis in papillary thyroid carcinoma.","10.1038/s41598-026-48693-y",2026,"PTC","thyroid",True,"High",["algorithm"],"ResNet-101 US+cytology radiopathomics CLNM AUC 0.891/0.875 external."),
    ("41931576","c","Utilizing the transformer mechanism to predict cervical lymph node metastasis in patients with papillary thyroid carcinoma.","10.1371/journal.pone.0345937",2026,"PTC","thyroid",True,"Medium",["algorithm"],"ViT US model CLNM AUC 0.807-0.809; > CNN/clinical."),
    ("41686681","c","Dual-channel ultrasonic images empowered deep learning: significantly improving prediction of occult central lymph node metastases in solitary papillary thyroid microcarcinoma.","10.2478/raon-2026-0006",2026,"PTMC","thyroid",True,"Medium",["algorithm"],"Dual-channel DL PTMC occult CLNM AUC 0.765/0.726; +clinical 0.900/0.873."),
    ("41078274","c","A Comparison of Different Radiomics Methods Predicting Cervical Lymph Node Metastasis in Papillary Thyroid Carcinoma.","10.1002/jcu.70102",2026,"PTC","thyroid",True,"Medium",["algorithm"],"Handcrafted+DL radiomics CLNM combined AUC 0.790/0.761."),
    ("41664099","c","Prediction of malignancy and metastasis of thyroid cancer by combined feature sets through advanced machine learning.","10.1186/s12911-026-03372-w",2026,"TC","thyroid",True,"Medium",["algorithm"],"Transfer-learning US+clinical ML: TC AUC 0.82, LNM AUC 0.78."),
    ("41237514","c","A multi-task deep learning framework for intraoperative diagnosis of thyroid cancer metastasis using whole slide images.","10.1016/j.ijmedinf.2025.106176",2026,"PTC","thyroid",True,"High",["algorithm"],"CLAM WSI multi-task (LNM/T-stage/localisation) AUC 0.85; 2-center."),
    ("41061579","c","SCLResNet and DSAF: A self-supervised contrastive learning and deep self-attention fusion-based multimodal network for predicting central lymph node metastasis in papillary thyroid carcinoma.","10.1016/j.artmed.2025.103280",2025,"PTC","thyroid",True,"High",["algorithm"],"Self-supervised multimodal (US+PVAT CT) CLNM AUC 0.863/0.839."),
    ("41049154","c","Development and Validation of Machine Learning Models in Predicting Prognosis of Breast Cancer Patients with Lymph Nodes Metastasis Following Neoadjuvant Chemotherapy.","10.2147/BCTT.S534964",2025,"breast","offtopic",False,"Low",["offtopic"],"Breast cancer NAC LN ML; non-thyroid."),
    ("40750786","c","Explainable multimodal deep learning for predicting thyroid cancer lateral lymph node metastasis using ultrasound imaging.","10.1038/s41467-025-62042-z",2025,"PTC","thyroid",True,"High",["algorithm"],"LLNM-Net multimodal US DL, 7-center, AUC 0.944 > experts."),
    ("40771372","c","Development and validation of a prediction model for lymph node metastasis in thyroid cancer: integrating deep learning and radiomics features from intra- and peri-tumoral regions.","10.21037/gs-2025-50",2025,"PTC","thyroid",True,"High",["algorithm"],"US radiomics+DL fusion SVM CLNM AUC 0.897/0.881 external."),
    ("40778281","c","A novel deep learning model based on multimodal contrast-enhanced ultrasound dynamic video for predicting occult lymph node metastasis in papillary thyroid carcinoma.","10.3389/fendo.2025.1634875",2025,"PTC","thyroid",True,"High",["algorithm"],"CEUS dynamic video DL OLNM AUC 0.734 test."),

    # --- query d: immune microenvironment ---
    ("42430190","d","Single-cell sequencing profiling of intratumoral heterogeneity and immunosuppressive microenvironment in primary thyroid cancer and lymph node metastases.","10.1080/2162402X.2026.2701504",2026,"PTC/LNM","thyroid",True,"High",["single-cell","immune"],"55k-cell scRNA PTC primary+LNM; LAG3-LGALS3/TIGIT alt checkpoints; FOXP3 Treg/LAMP3 DC/M2."),
    ("42373805","d","DNA methylation-mediated silencing of STAT5A drives breast cancer metastasis via dual regulation of EMT and immunosuppressive microenvironment.","10.1038/s41388-026-03849-y",2026,"breast","offtopic",False,"Low",["offtopic"],"Breast cancer STAT5A methylation; non-thyroid."),
    ("42321032","d","Retraction notice to 'Decoding tumor microenvironment...' [Biomedicine & Pharmacotherapy 181 (2024) 117714].","10.1016/j.biopha.2026.119655",2026,"breast","offtopic",False,"Low",["offtopic"],"Retraction notice (breast); non-thyroid."),
    ("42510113","d","Integrated Bioinformatics and Experimental Validation Reveal the Diagnostic and Prognostic Value of SMDT1 in Thyroid Carcinoma.","10.3390/diagnostics16142250",2026,"PTC","thyroid",True,"High",["molecular","metabolic","immune"],"SMDT1 (MCU complex) tumor-suppressor; low expr -> LNM/short DFS; mitochondrial Ca/OXPHOS/CD8+ T/NK."),
    ("42500581","d","The Intratumoral Microbiota in Breast Cancer: Roles in Progression, Immunity, and Therapy.","10.32604/or.2026.079281",2026,"breast","offtopic",False,"Low",["offtopic"],"Breast microbiota review; non-thyroid."),
    ("42500577","d","Tumour-Derived sEVs Promote Triple-Negative Breast Cancer Progression Associated with HAVCR2 Upregulation in Macrophages.","10.32604/or.2026.079137",2026,"TNBC","offtopic",False,"Low",["offtopic"],"TNBC sEVs/HAVCR2 macrophages; non-thyroid."),
    ("42464297","d","The NLRP3 inflammasome in gastrointestinal malignancies: molecular mechanisms, regulatory networks, and therapeutic opportunities.","10.1186/s12967-026-08565-5",2026,"GI","offtopic",False,"Low",["offtopic"],"GI NLRP3 review; non-thyroid (dup of query b)."),
    ("42488653","d","Heterogeneity of immune checkpoint inhibitor-related inflammatory central nervous system adverse event reporting signals in primary and metastatic brain tumors.","10.3389/fimmu.2026.1866830",2026,"CNS/brain mets","offtopic",False,"Low",["offtopic"],"ICI CNS irAE pharmacovigilance; non-thyroid."),
    ("42409802","d","Intratumoral microbiota in tumorigenesis: A double-edged sword.","10.1097/CM9.0000000000004178",2026,"pan-cancer","offtopic",False,"Low",["offtopic"],"Pan-cancer microbiota review; non-thyroid (dup)."),
    ("42397917","d","Single-cell transcriptomic analysis reveals tumor-immune determinants of lymph node colonization and progression in thyroid cancer.","10.1126/sciadv.aea4727",2026,"PTC/LNM","thyroid",True,"High",["single-cell","immune"],"scRNA PTC primary+LNM; IL7R in LNM TILs predicts better outcome; TNFRSF12A/CX3CR1 down."),
    ("42134246","d","Transcriptomic sequencing analysis of the tumor microenvironment atlas and potential mechanisms of metastasis in papillary thyroid carcinoma.","10.1016/j.molimm.2026.05.006",2026,"PTC","thyroid",True,"High",["single-cell","immune","algorithm"],"scRNA T/PT/LN + bulk; RGS5+ myCAF in M; random-forest N-stage 0.98; lasso-Cox C>0.9."),
    ("42310731","d","Plasma proteome-metabolome signatures enable non-invasive early detection and lymph node risk stratification in breast cancer.","10.1186/s12943-026-02713-7",2026,"breast","offtopic",False,"Low",["offtopic"],"Breast plasma multi-omics; non-thyroid."),
    ("42327722","d","MGST1 drives lymph node metastasis in papillary thyroid carcinoma via mitochondrial metabolic reprogramming and immune suppression.","10.3389/fimmu.2026.1848083",2026,"PTC","thyroid",True,"High",["metabolic","immune","algorithm","molecular"],"MGST1 'Mito-high' subtype; ML model AUC 0.833; Toxoflavin reverses immune-cold."),
    ("41874611","d","Decoding the role of CXC chemokines in pulmonary metastasis of colorectal cancer using integrative computational approaches.","10.1007/s00210-026-05215-x",2026,"CRC","offtopic",False,"Low",["offtopic"],"CRC pulmonary metastasis CXC chemokines; non-thyroid."),
    ("42291329","d","The dialogue between breast cancer and microorganisms.","10.3389/fcimb.2026.1738739",2026,"breast","offtopic",False,"Low",["offtopic"],"Breast microbiota review; non-thyroid."),

    # --- query e: single-cell RNA-seq ---
    ("42430190","e","Single-cell sequencing profiling of intratumoral heterogeneity and immunosuppressive microenvironment in primary thyroid cancer and lymph node metastases.","10.1080/2162402X.2026.2701504",2026,"PTC/LNM","thyroid",True,"High",["single-cell","immune"],"55k-cell scRNA PTC primary+LNM (dup of query d)."),
    ("42067069","e","EWSR1-rearranged renal neoplasia: Clinicopathologic and molecular characterization of 39 cases from a single institution.","10.1016/j.humpath.2026.106135",2026,"renal","offtopic",False,"Low",["offtopic"],"Renal EWSR1 neoplasia; non-thyroid."),
    ("42500577","e","Tumour-Derived sEVs Promote Triple-Negative Breast Cancer Progression Associated with HAVCR2 Upregulation in Macrophages.","10.32604/or.2026.079137",2026,"TNBC","offtopic",False,"Low",["offtopic"],"TNBC sEVs; non-thyroid (dup)."),
    ("42436124","e","Single-cell multi-omics deciphers the myofibro-inflammatory program of cancer-associated fibroblasts in triple-negative breast cancer.","10.1038/s41420-026-03255-z",2026,"TNBC","offtopic",False,"Low",["offtopic"],"TNBC CAF scRNA multi-omics; non-thyroid."),
    ("42488653","e","Heterogeneity of immune checkpoint inhibitor-related inflammatory central nervous system adverse event reporting signals.","10.3389/fimmu.2026.1866830",2026,"CNS","offtopic",False,"Low",["offtopic"],"ICI CNS irAE; non-thyroid (dup)."),
    ("42397917","e","Single-cell transcriptomic analysis reveals tumor-immune determinants of lymph node colonization and progression in thyroid cancer.","10.1126/sciadv.aea4727",2026,"PTC/LNM","thyroid",True,"High",["single-cell","immune"],"scRNA PTC LNM (dup of query d)."),
    ("42134246","e","Transcriptomic sequencing analysis of the tumor microenvironment atlas and potential mechanisms of metastasis in papillary thyroid carcinoma.","10.1016/j.molimm.2026.05.006",2026,"PTC","thyroid",True,"High",["single-cell","immune","algorithm"],"scRNA PTC TME (dup of query d)."),
    ("42050078","e","Olfactomedin 4 orchestrates TGF-beta/CEACAM6 axis, promoting cell-autonomous epithelial to mesenchymal transition during gallbladder epithelium carcinogenesis.","10.1038/s41388-026-03808-7",2026,"gallbladder","offtopic",False,"Low",["offtopic"],"Gallbladder OLFM4/EMT; non-thyroid."),
    ("42008746","e","PRECISE: A Prognostic Thyrocyte-Derived Gene Signature for Papillary Thyroid Carcinoma.","10.1158/1078-0432.CCR-25-4488",2026,"PTC","thyroid",True,"High",["single-cell","prognosis","algorithm"],"41-gene thyrocyte signature (scRNA/snRNA); PFS/DSS independent prognostic; 3 cohorts."),
    ("40665712","e","Keratin 6A Overexpression in the Lymphovascular Invasion-Associated Tumor Subgroup Promotes Progression of Triple-Negative Breast Cancer.","10.4143/crt.2025.423",2026,"TNBC","offtopic",False,"Low",["offtopic"],"TNBC KRT6A/LVI; non-thyroid."),
    ("42373830","e","Multi-omics reveals tumor microenvironment heterogeneity and therapeutic vulnerabilities in peritoneal metastasis of gastric cancer.","10.1038/s42003-026-10571-8",2026,"gastric","offtopic",False,"Low",["offtopic"],"Gastric PM scRNA+spatial; non-thyroid (dup)."),
    ("42329337","e","Integrated bulk and single-cell RNA sequencing reveals a prognostic neuro-mimicry signature in papillary thyroid carcinoma.","10.1007/s12672-026-05278-5",2026,"PTC","thyroid",True,"High",["single-cell","molecular","immune"],"8-gene neural-mimicry signature (KCNN4/KCNN1/KCNT2/SNAP25/GABRG1/2/GABRB2...); LNM AUC 0.721; GABRB2 in malignant thyrocytes; immunosuppressive."),
    ("42271337","e","FGD3 as a prognostic and immunological biomarker: a pan-cancer analysis of its role in tumor progression and the immune landscape.","10.1186/s12935-026-04360-w",2026,"pan-cancer","offtopic",False,"Low",["offtopic"],"Pan-cancer FGD3; non-thyroid."),
    ("42327722","e","MGST1 drives lymph node metastasis in papillary thyroid carcinoma via mitochondrial metabolic reprogramming and immune suppression.","10.3389/fimmu.2026.1848083",2026,"PTC","thyroid",True,"High",["metabolic","immune","algorithm","molecular"],"MGST1 (dup)."),
    ("42131580","e","Tumor-Derived Exosomal PDLIM1 Promotes Angiogenesis and Tumor Progression in Papillary Thyroid Carcinoma: Insights From Integrated Single-Cell Transcriptomics and Exosomal Proteomics.","10.2147/CMAR.S589372",2026,"PTC","thyroid",True,"High",["single-cell","molecular"],"scRNA primary+metastatic PTC; exosomal PDLIM1 drives angiogenesis/lymphatic vessel density via VEGF."),

    # --- query f: spatial transcriptomics / multi-omics ---
    ("42373830","f","Multi-omics reveals tumor microenvironment heterogeneity and therapeutic vulnerabilities in peritoneal metastasis of gastric cancer.","10.1038/s42003-026-10571-8",2026,"gastric","offtopic",False,"Low",["offtopic"],"Gastric PM; non-thyroid (dup)."),
    ("41421038","f","Cellular and molecular determinants of lymph node metastasis in papillary thyroid carcinoma: Integrated multi-omics profiling and machine learning models.","10.1016/j.compbiolchem.2025.108857",2026,"PTC","thyroid",True,"High",["single-cell","spatial","algorithm","molecular"],"scRNA+ST+bulk PTC LNM; FN1-SDC4 axis; 17-gene RF model."),
    ("41608657","f","Breast cancer stem cell activity driven by ME18D gene expression in the tumor microenvironment.","10.4252/wjsc.v18.i1.111348",2026,"breast","offtopic",False,"Low",["offtopic"],"Breast CSC; non-thyroid."),
    ("41398964","f","Integrated spatial metabolomics and transcriptomics reveal the molecular landscape of papillary thyroid cancer and its lymph node metastasis.","10.1186/s12967-025-07566-0",2025,"PTC","thyroid",True,"High",["spatial","metabolic","molecular"],"Spatial multi-omics PTC LNM: arginine-polyamine/glycolysis; NAT8L/SVCT-2 validated."),
    ("41129052","f","Fibroblasts in the tumor microenvironment: heterogeneity and dynamic interactions in tumor progression revealed by spatial transcriptomics.","10.1007/s13402-025-01108-y",2025,"pan-cancer","offtopic",False,"Low",["offtopic"],"Pan-cancer CAF spatial review (POSTN+ myCAF theme); non-thyroid-specific."),
    ("39923580","f","A comprehensive pan-cancer examination of transcription factor MAFF: Oncogenic potential, prognostic relevance, and immune landscape dynamics.","10.1016/j.intimp.2025.114105",2025,"pan-cancer","offtopic",False,"Low",["offtopic"],"Pan-cancer MAFF; non-thyroid."),

    # --- query g: prognosis/recurrence/distant mets ---
    ("41510756","g","Programmed death-ligand 1 expression is associated with local invasion and distant metastases in differentiated thyroid cancer: Systematic review and meta-analysis.","10.1177/10815589261415900",2026,"DTC","thyroid",True,"High",["immune","prognosis"],"PD-L1 meta: distant OR 4.6 / LVI OR 4.2, NOT LNM/recurrence."),
    ("41759361","g","Clinicopathological predictors of distant recurrence in breast cancer patients achieving pathological complete response after neoadjuvant chemotherapy.","10.1016/j.ejso.2026.111508",2026,"breast","offtopic",False,"Low",["offtopic"],"Breast pCR distant recurrence; non-thyroid."),
    ("41877795","g","Development and validation of a machine learning model for predicting high-risk distant metastatic recurrence in differentiated thyroid cancer.","10.3389/fmed.2026.1790226",2026,"DTC","thyroid",True,"High",["algorithm","prognosis"],"XGBoost DTC distant-met recurrence (1245 pts) AUC 0.88 external."),
    ("41817109","g","Selective Use of Radioiodine Therapy in Differentiated Thyroid Carcinoma: A Population-Based Cohort Study.","10.1177/10507256261416869",2026,"DTC","offtopic",False,"Low",["offtopic"],"Pure clinical epidemiology (RAI population); non-mechanism."),
    ("41419184","g","Prognostic Value of BRAF V600E Mutation in Papillary Thyroid Carcinoma: A Meta-Analysis of Nodal Involvement, Distant Metastases, Recurrence, and Mortality.","10.1016/j.eprac.2025.12.003",2026,"PTC","thyroid",True,"High",["prognosis","molecular"],"Meta (46k pts): BRAF V600E OR nodal 1.38 / recurrence 1.56, NOT distant/death."),
    ("41815549","g","Prognostic prediction model for triple-negative breast cancer using artificial intelligence and ultrasound radiomics.","10.3389/fonc.2026.1654953",2026,"TNBC","offtopic",False,"Low",["offtopic"],"TNBC AI radiomics; non-thyroid."),
    ("41488288","g","Organ-Specific Clinicopathological Features That Are Associated With Post-Relapse Survival of Metastatic Breast Cancer in Japanese Women.","10.14740/wjon2662",2026,"breast","offtopic",False,"Low",["offtopic"],"Breast MBC organ-specific; non-thyroid."),
    ("41514331","g","The dual oncogenic and protective roles of hashimoto's thyroiditis in papillary thyroid carcinoma: a cohort-based meta-analysis.","10.1186/s12957-025-04184-4",2026,"PTC","thyroid",True,"Medium",["prognosis","immune"],"HT-PTC meta (67,901 pts): HT linked lower CLNM/distant mets/recurrence; higher multifocality."),
    ("39749465","g","A Comparison of the Predictive Value of International Medullary Thyroid Carcinoma Grading System (IMTCGS) With That of Other Risk Factors in a Chinese Medullary Thyroid Carcinoma Cohort.","10.1111/cen.15195",2025,"MTC","thyroid",True,"Medium",["prognosis"],"IMTCGS predicts MTC DSS (AUC 0.81); post-op calcitonin predicts recurrence."),
    ("39213698","g","The U-shaped association between age at diagnosis and recurrence in patients with papillary thyroid carcinoma: A retrospective single-institution cohort study.","10.1016/j.ejso.2024.108626",2024,"PTC","thyroid",True,"Low",["prognosis"],"13,758-pt PTC: age-recurrence U-shape (<=30 & >=55 high)."),
    ("41084771","g","Aggressiveness of papillary thyroid carcinoma: a comprehensive analysis from molecular mechanisms to clinical applications.","10.5603/fhc.108530",2025,"PTC","thyroid",True,"Medium",["molecular","immune"],"Review: PTC aggressiveness mechanisms + imaging/AI."),
    ("39296076","g","Machine learning based androgen receptor regulatory gene-related random forest survival model for precise treatment decision in prostate cancer.","10.1016/j.heliyon.2024.e37256",2024,"prostate","offtopic",False,"Low",["offtopic"],"Prostate AR ML; non-thyroid."),
    ("38218916","g","Surgical margins and prognosis of borderline and malignant phyllodes tumors.","10.1007/s12094-023-03377-1",2024,"phyllodes","offtopic",False,"Low",["offtopic"],"Phyllodes tumors; non-thyroid."),
    ("37851243","g","BRAF V600E mutation in papillary thyroid microcarcinoma: is it a predictor for the prognosis of patients with intermediate to high recurrence risk?","10.1007/s12020-023-03564-8",2024,"PTMC","thyroid",True,"Medium",["prognosis","molecular"],"BRAF V600E PTMC: linked multifocality/ETE but NOT recurrence after RAI."),
    ("38311812","g","Pregnancy and the disease recurrence of patients previously treated for differentiated thyroid cancer: A systematic review and meta analysis.","10.1097/CM9.0000000000003008",2024,"DTC","offtopic",False,"Low",["offtopic"],"Pure clinical epidemiology (pregnancy recurrence); non-mechanism."),
    ("32668875","g","[Predictive analysis of distant metastasis after primary treatment of papillary thyroid cancer in patients under 18 years old].","10.3760/cma.j.cn115330-20000115-00025",2020,"pediatric PTC","thyroid",True,"Medium",["prognosis"],"Pediatric PTC distant mets: age<=15 + bilateral independent risks."),

    # --- query h: metastatic stemness ---
    ("39595993","h","DLK1 Is Associated with Stemness Phenotype in Medullary Thyroid Carcinoma Cell Lines.","10.3390/ijms252211924",2024,"MTC","thyroid",True,"Medium",["molecular"],"DLK1+ enriches stemness in MTC (MZ-CRC-1 > TT)."),
    ("33186350","h","Nucleotide de novo synthesis increases breast cancer stemness and metastasis via cGMP-PKG-MAPK signaling pathway.","10.1371/journal.pbio.3000872",2020,"breast","offtopic",False,"Low",["offtopic"],"Breast CSC metabolism; non-thyroid."),
    ("25426258","h","Stem cell biology in thyroid cancer: Insights for novel therapies.","10.4252/wjsc.v6.i5.614",2014,"TC","thyroid",True,"Medium",["molecular"],"Review: CSCs/EMT in thyroid cancer, identification markers."),

    # --- query i: metabolic reprogramming ---
    ("42500581","i","The Intratumoral Microbiota in Breast Cancer: Roles in Progression, Immunity, and Therapy.","10.32604/or.2026.079281",2026,"breast","offtopic",False,"Low",["offtopic"],"Breast microbiota; non-thyroid (dup)."),
    ("42409802","i","Intratumoral microbiota in tumorigenesis: A double-edged sword.","10.1097/CM9.0000000000004178",2026,"pan-cancer","offtopic",False,"Low",["offtopic"],"Pan-cancer microbiota; non-thyroid (dup)."),
    ("42332350","i","[Methyltransferase-like protein 7B promotes glycolysis and malignant progression in papillary thyroid carcinoma cells via the USP28/HIF-1alpha axis].","10.3724/zdxbyxb-2025-0822",2026,"PTC","thyroid",True,"High",["metabolic","molecular"],"METTL7B stabilizes HIF-1alpha (USP28) -> glycolysis/LNM in PTC."),
    ("42353188","i","Targeting the Warburg Effect in Anaplastic Thyroid Carcinoma: Metabolic Vulnerabilities and Therapeutic Opportunities.","10.3390/ijms27125472",2026,"ATC","thyroid",True,"Medium",["metabolic","molecular"],"Review: Warburg effect/ATC; BRAF/RAS/TP53/PI3K/mTOR/HIF-1alpha converge on glycolysis."),
    ("42327722","i","MGST1 drives lymph node metastasis in papillary thyroid carcinoma via mitochondrial metabolic reprogramming and immune suppression.","10.3389/fimmu.2026.1848083",2026,"PTC","thyroid",True,"High",["metabolic","immune","algorithm","molecular"],"MGST1 (dup)."),
    ("41855762","i","Pseudoginsenoside F11 enhances YBX1-mediated transcriptional repression of PRPS2 to inhibit the stemness and pulmonary metastasis of triple-negative breast cancer.","10.1016/j.phymed.2026.158064",2026,"TNBC","offtopic",False,"Low",["offtopic"],"TNBC PRPS2/YBX1; non-thyroid."),
    ("42280115","i","PKM2-Mediated Glycolytic Reprogramming in Thyroid Cancer: Mechanistic Insights and Therapeutic Potential.","10.3390/molecules31111811",2026,"TC","thyroid",True,"Medium",["metabolic"],"Review: PKM2 glycolytic reprogramming in TC."),
    ("42199418","i","Cancer metabolism: from the Warburg effect to precision therapy.","10.3389/fimmu.2026.1793553",2026,"pan-cancer","offtopic",False,"Low",["offtopic"],"Pan-cancer metabolism review; non-thyroid."),
    ("40850678","i","Research progress and therapeutic strategies in hepatocellular carcinoma metabolic reprogramming.","10.1016/j.jare.2025.08.023",2026,"HCC","offtopic",False,"Low",["offtopic"],"HCC metabolic review; non-thyroid."),
    ("41974658","i","Oncoprotein CYB561, acting in IRE1-XBP1-SREBF1 and FAK-ERK pathway, promotes breast cancer lipogenesis and progression.","10.1038/s41420-026-03101-2",2026,"breast","offtopic",False,"Low",["offtopic"],"Breast CYB561 lipogenesis; non-thyroid."),
    ("41679436","i","Augmenting cuproptosis and anti-metastatic immunity in breast cancer by copper-based nanoplatform for synergistic immunotherapy via lactate metabolic reprogramming and hypoxia alleviation.","10.1016/j.jconrel.2026.114716",2026,"breast","offtopic",False,"Low",["offtopic"],"Breast cuproptosis nanoplatform; non-thyroid."),
    ("41759425","i","Saikosaponin D inhibits gastric cancer progression by targeting PKM2-mediated glycolysis and histone lactylation.","10.1016/j.phymed.2026.157993",2026,"gastric","offtopic",False,"Low",["offtopic"],"Gastric PKM2; non-thyroid (dup)."),
    ("41690034","i","Curcumol targets the ATG4B-PKM2-lactate signaling axis to reverse EMT and inhibit colorectal cancer liver metastasis.","10.1016/j.phymed.2026.157933",2026,"CRC","offtopic",False,"Low",["offtopic"],"CRC Curcumol/PKM2; non-thyroid."),
    ("41814323","i","PKM2 phosphorylation by c-SRC activates glycolysis and metastasis with the stimulation of tumor-associated macrophages.","10.1186/s12964-026-02766-7",2026,"colon","offtopic",False,"Low",["offtopic"],"Colon PKM2 c-SRC/TAM; non-thyroid."),
    ("41435694","i","HNRNPC lactylation promotes pancreatic cancer progression through mediating the alternative splicing of PAK6.","10.1016/j.canlet.2025.218230",2026,"pancreas","offtopic",False,"Low",["offtopic"],"Pancreatic HNRNPC lactylation; non-thyroid."),
]

# ---- load existing run #7 corpus ----
with open(EXISTING, "r", encoding="utf-8") as f:
    existing = json.load(f)

existing_pmids = set()
for r in existing["records"]:
    pid = r.get("pmid") or r.get("paper_id")
    if pid:
        existing_pmids.add(str(pid))

# dedupe this_run by pmid, keep first occurrence, accumulate query tags
seen = {}
for (pmid, q, title, doi, year, disease, _cat, scope, rel, dims, note) in this_run:
    pmid = str(pmid)
    if pmid in seen:
        if q not in seen[pmid]["queries"]:
            seen[pmid]["queries"].append(q)
        continue
    seen[pmid] = {
        "pmid": pmid, "query": q, "title": title, "doi": doi, "year": year,
        "disease": disease, "in_scope": scope, "relevance": rel,
        "dimensions": dims, "note": note, "queries": [q],
    }

this_run_pmids = set(seen.keys())
new_pmids = this_run_pmids - existing_pmids
print("RUN #7 corpus unique:", len(existing_pmids))
print("THIS RUN unique (9 queries):", len(this_run_pmids))
print("NEW pmids not in run#7 corpus:", len(new_pmids))
for p in sorted(new_pmids):
    rec = seen[p]
    tag = "IN-SCOPE(thyroid)" if rec["in_scope"] else "EXCLUDED(off-topic)"
    print(f"  {p}  {tag}  [{rec['relevance']}]  q={','.join(rec['queries'])}  {rec['title'][:70]}")

# classify new
new_in_scope = [seen[p] for p in new_pmids if seen[p]["in_scope"]]
new_excluded = [seen[p] for p in new_pmids if not seen[p]["in_scope"]]
print("\nNew IN-SCOPE:", len(new_in_scope))
print("New EXCLUDED:", len(new_excluded))

# ---- rebuild cumulative JSON ----
records = list(existing["records"])
for rec in new_in_scope:
    records.append({
        "pmid": rec["pmid"], "title": rec["title"], "doi": rec["doi"],
        "year": rec["year"], "disease": rec["disease"], "queries": rec["queries"],
        "relevance": rec["relevance"], "dimensions": rec["dimensions"],
        "in_scope": True, "note": rec["note"],
    })
for rec in new_excluded:
    records.append({
        "pmid": rec["pmid"], "title": rec["title"], "doi": rec["doi"],
        "year": rec["year"], "disease": rec["disease"], "queries": rec["queries"],
        "relevance": rec["relevance"], "dimensions": rec["dimensions"],
        "in_scope": False, "note": rec["note"],
    })

# recompute counts
unique_count = len(records)
in_scope = [r for r in records if r.get("in_scope")]
excluded = [r for r in records if not r.get("in_scope")]
dim_dist = {}
for r in in_scope:
    for d in r.get("dimensions", []):
        if d == "offtopic":
            continue
        dim_dist[d] = dim_dist.get(d, 0) + 1

today = datetime.date.today().isoformat()
out = {
    "search_date": today,
    "run": "run#8",
    "source": "mcp__paper-search-mcp__search_pubmed (DeferExecuteTool); max_results=15; sort=pub_date (recency sweep)",
    "queries": existing["queries"],
    "raw_count": len(this_run_pmids),
    "unique_count": unique_count,
    "in_scope_count": len(in_scope),
    "excluded_count": len(excluded),
    "dimension_distribution_in_scope": dim_dist,
    "corpus_delta_vs_run7": {
        "new_in_scope_count": len(new_in_scope),
        "new_in_scope_pmids": [r["pmid"] for r in new_in_scope],
        "new_excluded_offtopic_count": len(new_excluded),
        "new_excluded_offtopic_pmids": [r["pmid"] for r in new_excluded],
        "baseline_run7_unique": len(existing_pmids),
        "baseline_run7_in_scope": sum(1 for r in existing["records"] if r.get("in_scope")),
        "cumulative_unique": unique_count,
        "cumulative_in_scope": len(in_scope),
        "note": f"Run#8 (2026-07-30) re-ran the same 9 queries with sort=pub_date. {len(new_pmids)} PMIDs absent from run#7 corpus: {len(new_in_scope)} thyroid in-scope + {len(new_excluded)} off-topic excluded.",
    },
    "records": records,
}

out_path = os.path.join(BASE, "search_results_latest.json")
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=1)

print("\n=== WROTE", out_path, "===")
print("cumulative unique:", unique_count, "| in_scope:", len(in_scope), "| excluded:", len(excluded))
print("dimension dist (in-scope):", dim_dist)
