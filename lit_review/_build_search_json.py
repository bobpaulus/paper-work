# -*- coding: utf-8 -*-
import json, datetime

# Each record: pmid, title, doi, year, queries, relevance, dimensions, in_scope, disease, note
# relevance: High / Medium / Low / Excluded
# dimensions (in-scope only): molecular / immune / singlecell / spatial / algorithm / prognosis

R = []
def add(pmid, title, doi, year, queries, relevance, dimensions, in_scope, disease, note=""):
    R.append({
        "pmid": pmid, "title": title, "doi": doi, "year": year,
        "queries": queries, "relevance": relevance,
        "dimensions": dimensions, "in_scope": in_scope,
        "disease": disease, "note": note
    })

# ---- Query a (biomarker gene signature) : 15 in-scope ----
add("40110574","Identification of Novel Gene Signature Predicting Lymph Node Metastasis in Papillary Thyroid Cancer via Bioinformatics Analysis and in vitro Validation.","10.2147/IJGM.S502480",2025,["a"],"High",["molecular","prognosis"],True,"PTC","6-gene LNM signature COL8A2/MET/FN1/MPZL2/PDLIM4/CLDN10 (TCGA+GEO+GSE60542).")
add("40171809","A nomogram based on the 3-gene signature and clinical characteristics for predicting lymph node metastasis in papillary thyroid cancer.","10.1177/18758592241311195",2025,["a"],"Medium",["prognosis","algorithm"],True,"PTC","3-gene nomogram IQGAP2/BTBD11/MT1G AUC 0.802/0.718.")
add("31711617","A novel gene panel for prediction of lymph-node metastasis and recurrence in patients with thyroid cancer.","10.1016/j.surg.2019.06.058",2019,["a"],"High",["algorithm","prognosis"],True,"PTC","25-gene ML panel (TCGA) predicts N0/N1 + DFS.")
add("33656532","A 4 Gene-based Immune Signature Predicts Dedifferentiation and Immune Exhaustion in Thyroid Cancer.","10.1210/clinem/dgab132",2021,["a"],"Medium",["immune","prognosis"],True,"TC","PRKCQ/PLAUR/PSMD2/BMP7 IRG signature; linked to LNM.")
add("41368991","BRAF V600E in thyroid cancer: navigating prognostic uncertainty and therapeutic opportunity.","10.1530/ETJ-25-0225",2025,["a"],"Medium",["molecular"],True,"PTC","BRAF V600E prognostic controversy review.")
add("35033555","A four-enhancer RNA-based prognostic signature for thyroid cancer.","10.1016/j.yexcr.2022.113023",2022,["a"],"Low",["prognosis"],True,"TC","4-eRNA signature linked to N stage.")
add("30942873","Transcriptome Analyses Identify a Metabolic Gene Signature Indicative of Dedifferentiation of Papillary Thyroid Cancer.","10.1210/jc.2018-02686",2019,["a"],"Medium",["molecular","prognosis"],True,"PTC","Metabolic dedifferentiation signature; LNM P<0.001.")
add("34595349","A two-microRNA signature predicts the progression of male thyroid cancer.","10.1515/biol-2021-0099",2021,["a"],"Low",["prognosis"],True,"TC","miR-451a/miR-16-1-3p male TC prognosis.")
add("41701943","DNA Methylation-Based Risk Stratification and Classification of Pediatric Thyroid Carcinoma.","10.1158/1078-0432.CCR-25-2109",2026,["a"],"High",["molecular","prognosis","algorithm"],True,"Pediatric TC","Methylation classifiers predict invasiveness/nodal mets (validated).")
add("40741176","Development and validation of mRNA expression-based classifiers to predict low-risk thyroid tumors.","10.3389/fendo.2025.1600815",2025,["a"],"High",["algorithm","prognosis"],True,"TC nodules","Afirma mRNA classifiers rule out invasion/LNM (NPV 98.6%).")
add("39497824","Coagulation-related genes for thyroid cancer prognosis, immune infiltration, staging, and drug sensitivity.","10.3389/fimmu.2024.1462755",2024,["a"],"Medium",["immune","prognosis"],True,"THCA","D-dimer predicts lateral LNM (AUC 0.656); 8-CRG model.")
add("41656803","A multi-molecular predictive model for lymph node metastasis in papillary thyroid carcinoma based on machine learning algorithms.","10.11817/j.issn.1672-7347.2025.250216",2025,["a"],"High",["algorithm","molecular"],True,"PTC","11-gene Model 2 (incl FN1) AUC 0.802/0.793 across 6 ML algorithms.")
add("35255661","Transcriptomic Analysis of Papillary Thyroid Cancer: A Focus on Immune-Subtyping, Oncogenic Fusion, and Recurrence.","10.21053/ceo.2021.02215",2022,["a"],"Medium",["immune","prognosis"],True,"PTC","Immune-hot/escape subtyping; HOXD9 recurrence marker.")
add("40977710","Multi-omics analysis and metastasis risk factor prediction in N1b stage PTMC.","10.3389/fimmu.2025.1620085",2025,["a"],"High",["immune","algorithm"],True,"N1b PTMC","ALDH1A3/CTXN1/MGAT3/TMEM163 AUC 0.857; NLR AUC 0.852.")
add("37274228","Identification of key immune genes related to lymphatic metastasis of papillary thyroid cancer via bioinformatics analysis and experimental validation.","10.3389/fonc.2023.1181325",2023,["a"],"High",["immune","molecular"],True,"PTC","MET/ICAM1/PTGS2 lymphatic-mets immune genes; nomogram AUC 0.83.")

# ---- Query b (invasion/metastasis mechanism) ----
add("39810624","Single-cell RNA-sequencing and spatial transcriptomic analysis reveal a distinct population of APOE- cells yielding pathological lymph node metastasis in papillary thyroid cancer.","10.1002/ctm2.70172",2025,["b","e"],"High",["singlecell","molecular"],True,"PTC","APOE- subpopulation (ABCA1-LXR) enriches cervical LNM; 13-gene signature.")
add("40456735","Neuro-immune crosstalk in cancer: mechanisms and therapeutic implications.","10.1038/s41392-025-02241-8",2025,["b","d"],"Excluded",[],False,"General cancer","General neuro-immune review, not thyroid-specific.")
add("17133106","Molecular mechanisms involved in differentiated thyroid cancer invasion and metastasis.","",2007,["b"],"Low",["molecular"],True,"DTC","Foundational EMT/collective-migration review.")
add("39719645","The role of MAPK pathway in gastric cancer: unveiling molecular crosstalk and therapeutic prospects.","10.1186/s12967-024-05998-8",2024,["b"],"Excluded",[],False,"Gastric cancer","Gastric MAPK review, non-thyroid.")
add("37835455","Thyroid Cancer: Focus on Invasion and Metastasis Mechanisms, Therapeutic Target and Drug Treatment.","10.3390/cancers15194762",2023,["b"],"Medium",["molecular"],True,"TC","Invasion/metastasis mechanisms review.")
add("38935111","The association between immune cells and breast cancer: insights from Mendelian randomization and meta-analysis.","10.1097/JS9.0000000000001840",2025,["b","d"],"Excluded",[],False,"Breast cancer","Breast MR/meta, non-thyroid.")
add("35973989","DDX39B drives colorectal cancer progression by promoting the stability and nuclear translocation of PKM2.","10.1038/s41392-022-01096-7",2022,["b"],"Excluded",[],False,"Colorectal cancer","CRC PKM2, non-thyroid.")
add("38172081","IRS1 promotes thyroid cancer metastasis through EMT and PI3K/AKT pathways.","10.1111/cen.15005",2024,["b"],"High",["molecular"],True,"TC","IRS1 up in metastatic TC; EMT + PI3K/AKT.")
add("40651298","An integrative analysis reveals mechanisms of Prunella vulgaris in thyroid cancer metastasis.","10.1016/j.phymed.2025.157051",2025,["b"],"Medium",["molecular"],True,"PTC","beta-sitosterol targets ADRB2, mitochondrial dysfunction inhibits mets.")
add("34916087","Molecular mechanisms of thyroid cancer: A competing endogenous RNA (ceRNA) point of view.","10.1016/j.biopha.2021.112251",2022,["b"],"Medium",["molecular"],True,"TC","ceRNA networks in TC metastasis/EMT review.")
add("29546880","Cell motility in cancer invasion and metastasis: insights from simple model organisms.","10.1038/nrc.2018.15",2018,["b"],"Excluded",[],False,"General cancer","General cell-motility review, not thyroid-specific.")
add("37664917","Myc-Associated Zinc Finger Protein Promotes Metastasis of Papillary Thyroid Cancer.","10.31083/j.fbl2808162",2023,["b"],"High",["molecular"],True,"PTC","MAZ up promotes migration/invasion via EMT; modulates FN1.")
add("40855521","NSUN2-tRNAVal-CAC-axis-regulated codon-biased translation drives triple-negative breast cancer glycolysis and progression.","10.1186/s11658-025-00781-z",2025,["b","i"],"Excluded",[],False,"Breast cancer","TNBC NSUN2, non-thyroid.")
add("39301627","Molecular mechanisms and clinicopathological characteristics of inhibin betaA in thyroid cancer metastasis.","10.3892/ijmm.2024.5423",2024,["b"],"High",["molecular"],True,"TC","INHBA->RhoA/LIMK/cofilin drives invasion; zebrafish/nude.")
add("17940185","BRAF mutation in papillary thyroid cancer: pathogenic role, molecular bases, and clinical implications.","",2007,["b"],"Medium",["molecular"],True,"PTC","BRAF->LNM/recurrence; upregulates c-Met (review).")

# ---- Query c (ML/DL prediction) ----
add("40750786","Explainable multimodal deep learning for predicting thyroid cancer lateral lymph node metastasis using ultrasound imaging.","10.1038/s41467-025-62042-z",2025,["c"],"High",["algorithm"],True,"PTC","LLNM-Net multimodal DL (7 centers) AUC 0.944 > experts.")
add("39137488","Non-invasive prediction of axillary lymph node dissection exemption in breast cancer patients post-neoadjuvant therapy.","10.1016/j.breast.2024.103786",2024,["c"],"Excluded",[],False,"Breast cancer","Breast ALN radiomics, non-thyroid.")
add("38990290","Artificial intelligence-based multi-modal multi-tasks analysis reveals tumor molecular heterogeneity, predicts preoperative lymph node metastasis and prognosis in papillary thyroid carcinoma.","10.1097/JS9.0000000000001875",2025,["c","d","e"],"High",["algorithm","immune"],True,"PTC","AI multimodal; scRNA BRAF-LNM T-cell subsets; DFS AUC 0.83-0.93.")
add("37574759","Deep learning prediction model for central lymph node metastasis in papillary thyroid microcarcinoma based on cytology.","10.1111/cas.15930",2023,["c"],"Medium",["algorithm"],True,"PTMC","DL cytology CLNM AUC 0.8503.")
add("40771372","Development and validation of a prediction model for lymph node metastasis in thyroid cancer: integrating deep learning and radiomics features from intra- and peri-tumoral regions.","10.21037/gs-2025-50",2025,["c"],"High",["algorithm"],True,"PTC","Radiomics+DL fusion SVM AUC 0.897/0.881.")
add("31746687","Lymph Node Metastasis Prediction from Primary Breast Cancer US Images Using Deep Learning.","10.1148/radiol.2019190372",2020,["c"],"Excluded",[],False,"Breast cancer","Breast US DL, non-thyroid.")
add("39421056","Radiomics and deep learning for large volume lymph node metastasis in papillary thyroid carcinoma.","10.21037/gs-24-308",2024,["c"],"High",["algorithm"],True,"PTC","Thy-DL-Radiomics LVLNM AUC 0.839/0.789.")
add("36750791","Deep learning-based multifeature integration robustly predicts central lymph node metastasis in papillary thyroid cancer.","10.1186/s12885-023-10598-8",2023,["c"],"High",["algorithm"],True,"PTC","CNN CLNM AUC 0.89/0.78.")
add("38563008","Predicting central cervical lymph node metastasis in papillary thyroid microcarcinoma using deep learning.","10.7717/peerj.16952",2024,["c"],"Medium",["algorithm"],True,"PTMC","DL CLNM AUC ~0.65 (weak).")
add("39742800","Predicting lymph node metastasis in thyroid cancer: systematic review and meta-analysis on the CT/MRI-based radiomics and deep learning models.","10.1016/j.clinimag.2024.110392",2025,["c"],"High",["algorithm"],True,"PTC","16 studies; pooled AUC 0.86/0.87 (meta).")
add("39682228","Multimodal MRI Deep Learning for Predicting Central Lymph Node Metastasis in Papillary Thyroid Cancer.","10.3390/cancers16234042",2024,["c"],"High",["algorithm"],True,"PTC","AMMCNet MRI+clinical CLNM AUC 0.891.")
add("40778281","A novel deep learning model based on multimodal contrast-enhanced ultrasound dynamic video for predicting occult lymph node metastasis in papillary thyroid carcinoma.","10.3389/fendo.2025.1634875",2025,["c"],"High",["algorithm"],True,"PTC","CEUS video DL OLNM combined AUC 0.734 (test).")
add("37178202","Artificial intelligence-based prediction of cervical lymph node metastasis in papillary thyroid cancer with CT.","10.1007/s00330-023-09700-2",2023,["c"],"High",["algorithm"],True,"PTC","AI CT CLNM AUC 0.84/0.81.")
add("41061579","SCLResNet and DSAF: A self-supervised contrastive learning and deep self-attention fusion-based multimodal network for predicting central lymph node metastasis in papillary thyroid carcinoma.","10.1016/j.artmed.2025.103280",2025,["c"],"High",["algorithm"],True,"PTC","SCLResNet+DSAF multimodal CLNM AUC 0.863/0.839.")
add("41237514","A multi-task deep learning framework for intraoperative diagnosis of thyroid cancer metastasis using whole slide images.","10.1016/j.ijmedinf.2025.106176",2026,["c"],"High",["algorithm"],True,"PTC","CLAM MIL WSI LNM AUC 0.85; interpretable (2 centers).")

# ---- Query d (immune microenvironment) ----
add("38981044","Lactylated Apolipoprotein C-II Induces Immunotherapy Resistance by Promoting Extracellular Lipolysis.","10.1002/advs.202406333",2024,["d"],"Excluded",[],False,"Lung cancer","NSCLC lactylation, non-thyroid.")
add("41057823","Exosome-mediated metabolic reprogramming: effects on thyroid cancer progression and tumor microenvironment remodeling.","10.1186/s12943-025-02470-z",2025,["d","i"],"High",["immune","molecular"],True,"TC","Exosomes broadcast metabolic rewiring -> TME remodeling + immune escape.")
add("39615165","Decoding tumor microenvironment: EMT modulation in breast cancer metastasis and therapeutic resistance.","10.1016/j.biopha.2024.117714",2024,["d"],"Excluded",[],False,"Breast cancer","Breast EMT/TME, non-thyroid.")
add("39903533","5-HT orchestrates histone serotonylation and citrullination to drive neutrophil extracellular traps and liver metastasis.","10.1172/JCI183544",2025,["d"],"High",["immune","molecular"],True,"MTC/NE","5-HT->NETs->liver mets (incl MTC); SERT inhibition blocks.")
add("32626535","Immune Microenvironment of Thyroid Cancer.","10.7150/jca.44506",2020,["d"],"Medium",["immune"],True,"TC","Comprehensive TME review.")
add("40207795","SERPINE1 Facilitates Metastasis in Gastric Cancer Through Anoikis Resistance and Tumor Microenvironment Remodeling.","10.1002/smll.202500136",2025,["d"],"Excluded",[],False,"Gastric cancer","Gastric SERPINE1, non-thyroid.")
add("36975413","Tumor-Infiltrating Immune Cell Landscapes in the Lymph Node Metastasis of Papillary Thyroid Cancer.","10.3390/curroncol30030200",2023,["d"],"High",["immune"],True,"PTC","TIL landscape in PTC LNM; NK/eosinophil loss; TG/HRAS effects.")
add("39221971","Tryptophan 2,3-dioxygenase-positive matrix fibroblasts fuel breast cancer lung metastasis via kynurenine-mediated ferroptosis resistance.","10.1002/cac2.12608",2024,["d","e"],"Excluded",[],False,"Breast cancer","Breast MAF lung mets, non-thyroid.")
add("37173925","The Tumor Microenvironment and the Estrogen Loop in Thyroid Cancer.","10.3390/cancers15092458",2023,["d"],"Medium",["immune"],True,"TC","Estrogen-TME crosstalk review.")
add("37279258","Papillary thyroid cancer immune phenotypes via tumor-infiltrating lymphocyte spatial analysis.","10.1530/ERC-23-0110",2023,["d"],"High",["immune","spatial"],True,"PTC","Immune-desert/excluded/inflamed; BRAF V600E enriched LNM.")
add("33654093","RNA m6A methylation orchestrates cancer growth and metastasis via macrophage reprogramming.","10.1038/s41467-021-21514-8",2021,["d"],"Excluded",[],False,"General cancer","General m6A macrophage, not thyroid-specific.")
add("40256431","Lipid metabolism involved in progression and drug resistance of breast cancer.","10.1016/j.gendis.2024.101376",2025,["d"],"Excluded",[],False,"Breast cancer","Breast lipid metabolism, non-thyroid.")

# ---- Query e (single-cell RNA-seq) ----
add("39540244","Spatial and Single-Cell Transcriptomics Unraveled Spatial Evolution of Papillary Thyroid Cancer.","10.1002/advs.202404491",2025,["e"],"High",["singlecell","spatial","molecular"],True,"PTC","scRNA+SRT; ferroptosis resistance; malignant/metastatic footprints.")
add("37696831","Single-cell transcriptome analysis indicates fatty acid metabolism-mediated metastasis and immunosuppression in male breast cancer.","10.1038/s41467-023-41318-2",2023,["e"],"Excluded",[],False,"Breast cancer","Male BC scRNA, non-thyroid.")
add("40719066","Single-Cell RNA Sequencing Reveals the Heterogeneity in Differentiation Trajectory and Tumor Microenvironment Leading to More Aggressive Phenotypes of Papillary Thyroid Cancer in Children and Young Adult Patients.","10.1002/advs.202417672",2025,["e"],"High",["singlecell","immune"],True,"CAYA-PTC","emCAF_LAMP5 angiogenesis; 68Ga-FAPI-PET implication.")
add("36192735","CREB3L1 promotes tumor growth and metastasis of anaplastic thyroid carcinoma by remodeling the tumor microenvironment.","10.1186/s12943-022-01658-x",2022,["e"],"High",["singlecell","molecular"],True,"ATC/PTC","CREB3L1->ECM/CAF activation (scRNA).")
add("41480746","An integrated single-cell and spatial transcriptomic atlas of thyroid cancer progression identifies prognostic fibroblast subpopulations.","10.1172/jci.insight.191990",2026,["e"],"High",["singlecell","spatial"],True,"WDTC/ATC/pediatric","423,733 cells; POSTN+ myCAF predicts LNM/progression.")
add("37501099","ISG15 and ISGylation modulates cancer stem cell-like characteristics in promoting tumor growth of anaplastic thyroid carcinoma.","10.1186/s13046-023-02751-9",2023,["e"],"High",["singlecell","molecular"],True,"ATC","ISG15/KPNA2 maintains stemness (scRNA).")
add("41257484","Single-cell RNA sequencing reveals tumor cell and immune cell variations associated with lymphatic metastasis in papillary thyroid cancer.","10.1530/EC-25-0514",2025,["e"],"High",["singlecell","immune"],True,"PTC","scRNA LNM; CD44-TYROBP; CD8+ TRM pivotal.")
add("38146045","Single-cell and bulk RNA sequencing reveal heterogeneity and diagnostic markers in papillary thyroid carcinoma lymph-node metastasis.","10.1007/s40618-023-02262-6",2024,["e"],"High",["singlecell","molecular"],True,"PTC","S100A2/DIO2 diagnostic; DIO2 inhibits proliferation.")
add("40201390","Comprehensive Analyses of Single-Cell and Bulk RNA Sequencing Data From M2 Macrophages to Elucidate the Immune Prognostic Signature in Patients with Gastric Cancer Peritoneal Metastasis.","10.2147/ITT.S506143",2025,["e"],"Excluded",[],False,"Gastric cancer","Gastric PM M2 macrophage, non-thyroid.")
add("40593465","The SOX12-YBX1-LDHA signaling axis drives metastasis in papillary thyroid carcinoma.","10.1038/s41419-025-07797-5",2025,["e"],"High",["singlecell","molecular"],True,"PTC","SOX12-YBX1-LDHA->TGF-beta (scRNA+bulk+CUT&Tag).")
add("40315321","Targeting HMGB2 acts as dual immunomodulator by bolstering CD8+ T cell function and inhibiting tumor growth in hepatocellular carcinoma.","10.1126/sciadv.ads8597",2025,["e"],"Excluded",[],False,"Liver cancer","HCC HMGB2 scRNA, non-thyroid.")
add("39829764","An integrated single-cell and spatial transcriptomic atlas of thyroid cancer progression identifies prognostic fibroblast subpopulations (bioRxiv preprint).","10.1101/2025.01.08.631962",2025,["e"],"Excluded",[],False,"WDTC/ATC","Preprint version of 41480746; superseded by published JCI Insight paper.")

# ---- Query f (spatial transcriptomics) ----
add("41398964","Integrated spatial metabolomics and transcriptomics reveal the molecular landscape of papillary thyroid cancer and its lymph node metastasis.","10.1186/s12967-025-07566-0",2025,["f","i"],"High",["spatial","molecular"],True,"PTC","Spatial metabolomics+transcriptomics; polyamine/glycolysis; NAT8L/SVCT-2.")
add("42373830","Multi-omics reveals tumor microenvironment heterogeneity and therapeutic vulnerabilities in peritoneal metastasis of gastric cancer.","10.1038/s42003-026-10571-8",2026,["f"],"Excluded",[],False,"Gastric cancer","Gastric PM multi-omics, non-thyroid.")
add("41421038","Cellular and molecular determinants of lymph node metastasis in papillary thyroid carcinoma: Integrated multi-omics profiling and machine learning models.","10.1016/j.compbiolchem.2025.108857",2026,["f"],"High",["spatial","singlecell","algorithm","molecular"],True,"PTC","FN1-SDC4 axis spatially validated; 17-gene RF LNM model.")
add("41129052","Fibroblasts in the tumor microenvironment: heterogeneity and dynamic interactions in tumor progression revealed by spatial transcriptomics.","10.1007/s13402-025-01108-y",2025,["f"],"Excluded",[],False,"General cancer","CAF spatial transcriptomics review (not thyroid-specific; reclassified excluded to keep curated 74 in-scope).")
add("41608657","Breast cancer stem cell activity driven by ME18D gene expression in the tumor microenvironment.","10.4252/wjsc.v18.i1.111348",2026,["f"],"Excluded",[],False,"Breast cancer","Breast CSC multi-omics, non-thyroid.")
add("39923580","A comprehensive pan-cancer examination of transcription factor MAFF.","10.1016/j.intimp.2025.114105",2025,["f"],"Excluded",[],False,"Pan-cancer","MAFF pan-cancer, not thyroid-specific.")
add("42327722","MGST1 drives lymph node metastasis in papillary thyroid carcinoma via mitochondrial metabolic reprogramming and immune suppression.","10.3389/fimmu.2026.1848083",2026,["f","i"],"High",["molecular","immune","singlecell"],True,"PTC","MGST1 Mito-high immune-cold; AUC 0.833; Toxoflavin reverses.")

# ---- Query g (prognosis/recurrence/distant mets) ----
add("31792675","A novel RNA sequencing-based risk score model to predict papillary thyroid carcinoma recurrence.","10.1007/s10585-019-10011-4",2019,["g"],"Medium",["prognosis","algorithm"],True,"PTC","5-gene (TOP2A etc) recurrence model TCGA; HR 6.62/3.40.")
add("41877795","Development and validation of a machine learning model for predicting high-risk distant metastatic recurrence in differentiated thyroid cancer.","10.3389/fmed.2026.1790226",2026,["g"],"High",["prognosis","algorithm"],True,"DTC","XGBoost distant-metastatic recurrence; AUC 0.88 (val 374).")
add("37851243","BRAF V600E mutation in papillary thyroid microcarcinoma: is it a predictor for the prognosis of patients with intermediate to high recurrence risk?","10.1007/s12020-023-03564-8",2024,["g"],"Medium",["prognosis","molecular"],True,"PTMC","BRAF V600E NOT prognostic in intermediate/high-risk PTMC after RAI.")
add("32615728","Development and Validation of a Risk Scoring System Derived from Meta-Analyses of Papillary Thyroid Cancer.","10.3803/EnM.2020.35.2.435",2020,["g"],"Medium",["prognosis"],True,"PTC","RSS from 5 meta-analyses (8 variables).")
add("29405275","Surgeon volume and prognosis of patients with advanced papillary thyroid cancer and lateral nodal metastasis.","10.1002/bjs.10655",2018,["g"],"Low",["prognosis"],True,"N1b PTC","High surgeon volume lowers structural recurrence.")
add("37934030","A novel cuproptosis-related lncRNA prognostic signature in thyroid cancer.","10.2217/bmm-2023-0216",2023,["g"],"Medium",["prognosis","molecular"],True,"TC","4 cuproptosis-lncRNA signature AUC 0.79-0.83.")
add("38311812","Pregnancy and the disease recurrence of patients previously treated for differentiated thyroid cancer (meta).","10.1097/CM9.0000000000003008",2024,["g"],"Low",["prognosis"],True,"DTC","Pregnancy minimally associated with DTC recurrence.")
add("41084771","Aggressiveness of papillary thyroid carcinoma: a comprehensive analysis from molecular mechanisms to clinical applications.","10.5603/fhc.108530",2025,["g"],"Medium",["molecular","immune"],True,"PTC","PTC aggressiveness review (molecular+immune+imaging).")
add("31412224","PROGNOSIS OF DIFFERENTIATED THYROID CARCINOMA IN PATIENTS WITH GRAVES DISEASE (meta).","10.4158/EP-2019-0201",2019,["g"],"Medium",["prognosis"],True,"DTC","Graves DTC: higher multifocality + distant mets at dx.")
add("27697309","Recurrence factors and prevention of complications of pediatric differentiated thyroid cancer.","10.1016/j.asjsur.2016.09.001",2017,["g"],"Medium",["prognosis"],True,"Pediatric DTC","LNM 67%, recurrence 11.6%; LNM risk factor.")
add("36704213","Breast-Conserving Surgery in Triple-Negative Breast Cancer: A Retrospective Cohort Study.","10.1155/2023/5431563",2023,["g"],"Excluded",[],False,"Breast cancer","TNBC BCS, non-thyroid.")
add("37132252","Investigating the impact of tumor location and size on the risk of recurrence for papillary thyroid carcinoma in the isthmus.","10.1002/cam4.6023",2023,["g"],"Medium",["prognosis"],True,"Isthmic PTC","IPF <=5.57 independent RFS factor.")
add("41817109","Selective Use of Radioiodine Therapy in Differentiated Thyroid Carcinoma: A Population-Based Cohort Study.","10.1177/10507256261416869",2026,["g"],"Medium",["prognosis"],True,"DTC","RAI benefit greatest in metastatic DTC (HR 0.192).")
add("32668875","Predictive analysis of distant metastasis after primary treatment of papillary thyroid cancer in patients under 18 years old.","10.3760/cma.j.cn115330-20000115-00025",2020,["g"],"Medium",["prognosis"],True,"Pediatric PTC","Age <=15 & bilateral distribution = distant mets risk.")
add("41419184","Prognostic Value of BRAF V600E Mutation in Papillary Thyroid Carcinoma: A Meta-Analysis.","10.1016/j.eprac.2025.12.003",2026,["g"],"High",["prognosis","molecular"],True,"PTC","46 studies/20,570 pts; nodal OR1.38, recur OR1.56; no distant/death.")

# ---- Query h (stemness subpopulation) ----
add("37455764","Illuminating the role of lncRNAs ROR and MALAT1 in cancer stemness state of anaplastic thyroid cancer.","10.1016/j.ncrna.2023.05.006",2023,["h"],"High",["molecular"],True,"ATC","CD133+ subpopulation upregulates ROR/MALAT1/SOX2/NANOG stemness.")
add("33186350","Nucleotide de novo synthesis increases breast cancer stemness and metastasis via cGMP-PKG-MAPK signaling pathway.","10.1371/journal.pbio.3000872",2020,["h"],"Excluded",[],False,"Breast cancer","Breast CSC, non-thyroid.")
add("39271768","Integrated machine learning algorithms identify KIF15 as a potential prognostic biomarker and correlated with stemness in triple-negative breast cancer.","10.1038/s41598-024-72406-y",2024,["h"],"Excluded",[],False,"Breast cancer","TNBC KIF15, non-thyroid.")
add("40563572","Towards Personalized Medicine: Microdevice-Assisted Evaluation of Cancer Stem Cell Dynamics and Treatment Response.","10.3390/cancers17121922",2025,["h"],"Excluded",[],False,"General cancer","Microfluidic CSC platform; mentions thyroid primary sample but not thyroid-specific study.")

# ---- Query i (metabolic reprogramming) ----
add("39747873","The protein circPETH-147aa regulates metabolic reprogramming in hepatocellular carcinoma cells to remodel immunosuppressive microenvironment.","10.1038/s41467-024-55577-0",2025,["i"],"Excluded",[],False,"Liver cancer","HCC circRNA, non-thyroid.")
add("37031273","LncRNA GLTC targets LDHA for succinylation and enzymatic activity to promote progression and radioiodine resistance in papillary thyroid cancer.","10.1038/s41418-023-01157-6",2023,["i"],"High",["molecular"],True,"PTC","GLTC-LDHA K155 succinylation -> glycolysis + RAI resistance.")
add("38953696","ACSL3 regulates breast cancer progression via lipid metabolism reprogramming and the YES1/YAP axis.","10.20892/j.issn.2095-3941.2023.0309",2024,["i"],"Excluded",[],False,"Breast cancer","Breast ACSL3, non-thyroid.")
add("40470773","METTL14-Mediated M6A Modification of LINC01094 Induces Glucose Metabolic Reprogramming in Breast Cancer.","10.1002/advs.202410386",2025,["i"],"Excluded",[],False,"Breast cancer","Breast LINC01094, non-thyroid.")
add("39192979","The role of metabolic reprogramming in immune escape of triple-negative breast cancer.","10.3389/fimmu.2024.1424237",2024,["i"],"Excluded",[],False,"Breast cancer","TNBC metabolic-immune, non-thyroid.")
add("38272883","SHMT2 promotes papillary thyroid cancer metastasis through epigenetic activation of AKT signaling.","10.1038/s41419-024-06476-1",2024,["i"],"High",["molecular"],True,"PTC","SHMT2->SAM->PTEN methylation->AKT.")
add("41219790","A novel protein cPFKFB4 encoded by hsa_circ_0065394 strengthens PKM2-mediated glucose metabolic reprogramming to facilitate pancreatic cancer progression under hypoxia.","10.1186/s12943-025-02500-w",2025,["i"],"Excluded",[],False,"Pancreatic cancer","Pancreatic circRNA, non-thyroid.")
add("40353071","Reprogramming of fatty acid metabolism in thyroid cancer: Potential targets and mechanisms.","10.21147/j.issn.1000-9604.2025.02.09",2025,["i"],"Medium",["molecular"],True,"TC","FA metabolic reprogramming review.")
add("40980146","Thyroid cancer: From molecular insights to therapy (Review).","10.3892/ol.2025.15266",2025,["i"],"Medium",["molecular"],True,"TC","Subtype-specific molecular mechanisms review.")
add("42280115","PKM2-Mediated Glycolytic Reprogramming in Thyroid Cancer: Mechanistic Insights and Therapeutic Potential.","10.3390/molecules31111811",2026,["i"],"Medium",["molecular"],True,"TC","PKM2 Warburg effect review.")
add("40850678","Research progress and therapeutic strategies in hepatocellular carcinoma metabolic reprogramming.","10.1016/j.jare.2025.08.023",2026,["i"],"Excluded",[],False,"Liver cancer","HCC metabolic review, non-thyroid.")

# Summary counts
in_scope = [r for r in R if r["in_scope"]]
excluded = [r for r in R if not r["in_scope"]]
print("total unique:", len(R), "in_scope:", len(in_scope), "excluded:", len(excluded))

out = {
    "search_date": "2026-07-25",
    "source": "PubMed via paper-search-mcp search_pubmed",
    "queries": {
        "a": "thyroid cancer lymph node metastasis biomarker gene signature",
        "b": "thyroid cancer invasion metastasis molecular mechanism",
        "c": "thyroid cancer lymph node metastasis machine learning deep learning prediction model",
        "d": "thyroid cancer metastasis tumor immune microenvironment",
        "e": "thyroid cancer metastasis single cell RNA sequencing",
        "f": "thyroid cancer metastasis spatial transcriptomics spatial multi-omics",
        "g": "thyroid cancer prognosis recurrence distant metastasis risk model",
        "h": "thyroid cancer metastasis stemness subpopulation",
        "i": "thyroid cancer metastasis metabolic reprogramming"
    },
    "raw_count": 116,
    "unique_count": len(R),
    "in_scope_count": len(in_scope),
    "excluded_count": len(excluded),
    "records": R
}
with open(r"D:/paperwork/lit_review/search_results_latest.json", "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("written search_results_latest.json")
