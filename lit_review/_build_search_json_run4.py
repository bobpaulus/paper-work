# -*- coding: utf-8 -*-
"""Build search_results_latest.json for lit-review run #4 (2026-07-26).
Records screened from 9 complementary PubMed queries via paper-search-mcp search_pubmed.
Fields: pmid, title, doi, year, disease, queries, relevance, dimensions, in_scope, note.
Dimensions: molecular / immune / singlecell / spatial / algorithm / prognosis / metabolic / offtopic.
"""
import json, datetime

# tuples: pmid, title, doi, year, disease, queries, relevance, dimensions, in_scope, note
R = [
 # ---- query a: biomarker gene signature ----
 ("40110574","Identification of Novel Gene Signature Predicting Lymph Node Metastasis in Papillary Thyroid Cancer via Bioinformatics Analysis and in vitro Validation.","10.2147/IJGM.S502480",2025,"PTC",["a"],"High",["molecular","prognosis"],True,"6-gene LNM signature COL8A2/MET/FN1/MPZL2/PDLIM4/CLDN10 (TCGA+GEO+GSE60542)."),
 ("40171809","A nomogram based on the 3-gene signature and clinical characteristics for predicting lymph node metastasis in papillary thyroid cancer.","10.1177/18758592241311195",2025,"PTC",["a"],"Medium",["prognosis","algorithm"],True,"3-gene nomogram IQGAP2/BTBD11/MT1G AUC 0.802/0.718."),
 ("31711617","A novel gene panel for prediction of lymph-node metastasis and recurrence in patients with thyroid cancer.","10.1016/j.surg.2019.06.058",2020,"PTC",["a"],"High",["algorithm","prognosis"],True,"25-gene ML panel (TCGA) predicts N0/N1 + DFS, OR=8.06."),
 ("33656532","A 4 Gene-based Immune Signature Predicts Dedifferentiation and Immune Exhaustion in Thyroid Cancer.","10.1210/clinem/dgab132",2021,"TC",["a"],"Medium",["immune","prognosis"],True,"4 IRGs (PRKCQ/PLAUR/PSMD2/BMP7) predict dediff + immune exhaustion; linked LNM."),
 ("41368991","BRAF V600E in thyroid cancer: navigating prognostic uncertainty and therapeutic opportunity.","10.1530/ETJ-25-0225",2025,"PTC",["a"],"Medium",["molecular"],True,"Review: BRAF V600E prognostic controversy + targeted therapy."),
 ("35033555","A four-enhancer RNA-based prognostic signature for thyroid cancer.","10.1016/j.yexcr.2022.113023",2022,"TC",["a"],"Medium",["prognosis","algorithm"],True,"4-eRNA signature (AC141930.1/NBDY/MEG3/AP002358.1) predicts prognosis, linked N stage."),
 ("30942873","Transcriptome Analyses Identify a Metabolic Gene Signature Indicative of Dedifferentiation of Papillary Thyroid Cancer.","10.1210/jc.2018-02686",2019,"PTC",["a"],"Medium",["metabolic","prognosis"],True,"Metabolic gene signature (LPCAT2/ACOT7/HSD17B8/PDE8B/ST3GAL1) predicts DDTC + LNM."),
 ("34595349","A two-microRNA signature predicts the progression of male thyroid cancer.","10.1515/biol-2021-0099",2021,"TC",["a"],"Medium",["prognosis"],True,"miR-451a/miR-16-1-3p prognostic in male TC recurrence/LNM."),
 ("41701943","DNA Methylation-Based Risk Stratification and Classification of Pediatric Thyroid Carcinoma.","10.1158/1078-0432.CCR-25-2109",2026,"pediatric TC",["a"],"High",["algorithm","molecular"],True,"Methylation classifiers predict invasiveness/nodal mets + driver mutation in pediatric TC."),
 ("40741176","Development and validation of mRNA expression-based classifiers to predict low-risk thyroid tumors.","10.3389/fendo.2025.1600815",2025,"TC",["a"],"High",["algorithm"],True,"mRNA classifiers rule out invasion/LNM NPV 97.6-100% (Afirma cohort)."),
 ("39497824","Coagulation-related genes for thyroid cancer prognosis, immune infltration, staging, and drug sensitivity.","10.3389/fimmu.2024.1462755",2024,"THCA",["a"],"Medium",["prognosis","immune"],True,"D-dimer predicts lateral LNM; 8-gene coagulation prognostic model."),
 ("41656803","[A multi-molecular predictive model for lymph node metastasis in papillary thyroid carcinoma based on machine learning algorithms].","10.11817/j.issn.1672-7347.2025.250216",2025,"PTC",["a"],"High",["algorithm","molecular"],True,"11-gene ML LNM model (FN1/PI15/IL11/PLA2G5...) AUC 0.80/0.79 across 6 ML algos."),
 ("35255661","Transcriptomic Analysis of Papillary Thyroid Cancer: A Focus on Immune-Subtyping, Oncogenic Fusion, and Recurrence.","10.21053/ceo.2021.02215",2022,"PTC",["a"],"Medium",["immune","prognosis"],True,"HOXD9 recurrence marker; immune-escape signature in advanced PTC."),
 ("40977710","Multi-omics analysis and metastasis risk factor prediction in N1b stage PTMC: insights into immune infiltration and therapeutic implications.","10.3389/fimmu.2025.1620085",2025,"PTMC",["a"],"High",["algorithm","immune","singlecell"],True,"N1b PTMC: NLR model AUC 0.852; 4-gene classifier (ALDH1A3/CTXN1/MGAT3/TMEM163) AUC 0.857."),
 ("37274228","Identification of key immune genes related to lymphatic metastasis of papillary thyroid cancer via bioinformatics analysis and experimental validation.","10.3389/fonc.2023.1181325",2023,"PTC",["a"],"High",["immune","molecular"],True,"MET/ICAM1/PTGS2 immune-gene LNM signature (TCGA+WGCNA+LASSO/RF)."),

 # ---- query b: invasion/metastasis molecular mechanism ----
 ("39810624","Single-cell RNA-sequencing and spatial transcriptomic analysis reveal a distinct population of APOE- cells yielding pathological lymph node metastasis in papillary thyroid cancer.","10.1002/ctm2.70172",2025,"PTC",["b","e"],"High",["singlecell","spatial","molecular","algorithm"],True,"APOE- stem-like subpop via ABCA1-LXR; 13-gene ML LNM signature."),
 ("40456735","Neuro-immune crosstalk in cancer: mechanisms and therapeutic implications.","10.1038/s41392-025-02241-8",2025,"pan-cancer",["b","d"],"Low",["offtopic"],False,"Pan-cancer neuro-immune review, not thyroid-specific."),
 ("17133106","Molecular mechanisms involved in differentiated thyroid cancer invasion and metastasis.","10.1097/01.MD.0000287929.25749.6b",2007,"DTC",["b"],"Medium",["molecular"],True,"Review: RAS-RAF-ERK/PI3K-AKT, EMT, collective migration in thyroid invasion."),
 ("39719645","The role of MAPK pathway in gastric cancer: unveiling molecular crosstalk and therapeutic prospects.","10.1186/s12967-024-05998-8",2024,"gastric",["b"],"Low",["offtopic"],False,"Gastric cancer MAPK review, non-thyroid."),
 ("37835455","Thyroid Cancer: Focus on Invasion and Metastasis Mechanisms, Therapeutic Target and Drug Treatment.","10.3390/cancers15194762",2023,"TC",["b"],"Medium",["molecular"],True,"Review: invasion/metastasis mechanisms + therapeutics in TC."),
 ("38935111","The association between immune cells and breast cancer: insights from Mendelian randomization and meta-analysis.","10.1097/JS9.0000000000001840",2025,"breast",["b","d"],"Low",["offtopic"],False,"Breast cancer immune MR, non-thyroid."),
 ("35973989","DDX39B drives colorectal cancer progression by promoting the stability and nuclear translocation of PKM2.","10.1038/s41392-022-01096-7",2022,"CRC",["b"],"Low",["offtopic"],False,"Colorectal cancer, non-thyroid."),
 ("38172081","IRS1 promotes thyroid cancer metastasis through EMT and PI3K/AKT pathways.","10.1111/cen.15005",2024,"TC",["b"],"High",["molecular"],True,"IRS1 drives thyroid cancer distant mets via EMT/PI3K-AKT."),
 ("40651298","An integrative analysis reveals mechanisms of Prunella vulgaris in thyroid cancer metastasis.","10.1016/j.phymed.2025.157051",2025,"PTC",["b"],"Medium",["molecular","algorithm"],True,"ADRB2 hub gene for PTC LNM; beta-sitosterol anti-metastatic."),
 ("34916087","Molecular mechanisms of thyroid cancer: A competing endogenous RNA (ceRNA) point of view.","10.1016/j.biopha.2021.112251",2022,"TC",["b"],"Medium",["molecular"],True,"Review: ceRNA networks in TC metastasis/EMT/drug resistance."),
 ("29546880","Cell motility in cancer invasion and metastasis: insights from simple model organisms.","10.1038/nrc.2018.15",2018,"pan-cancer",["b"],"Low",["offtopic"],False,"General cell-motility review, not thyroid."),
 ("37664917","Myc-Associated Zinc Finger Protein Promotes Metastasis of Papillary Thyroid Cancer.","10.31083/j.fbl2808162",2023,"PTC",["b"],"High",["molecular"],True,"MAZ promotes PTC migration/invasion via FN1/EMT."),
 ("40855521","NSUN2-tRNAVal-CAC-axis-regulated codon-biased translation drives triple-negative breast cancer glycolysis and progression.","10.1186/s11658-025-00781-z",2025,"TNBC",["b","i"],"Low",["offtopic"],False,"Triple-negative breast cancer, non-thyroid."),
 ("39301627","Molecular mechanisms and clinicopathological characteristics of inhibin betaA in thyroid cancer metastasis.","10.3892/ijmm.2024.5423",2024,"TC",["b"],"Medium",["molecular"],True,"INHBA promotes TC metastasis via RhoA/LIMK/cofilin."),
 ("17940185","BRAF mutation in papillary thyroid cancer: pathogenic role, molecular bases, and clinical implications.","10.1016/j.amjmed.2007.08.037",2007,"PTC",["b"],"Medium",["molecular"],True,"Xing review: BRAF V600E drives PTC progression/recurrence."),

 # ---- query c (re-run): ML/DL prediction ----
 ("40750786","Explainable multimodal deep learning for predicting thyroid cancer lateral lymph node metastasis using ultrasound imaging.","10.1038/s41467-025-62042-z",2025,"PTC",["c"],"High",["algorithm"],True,"LLNM-Net multimodal US DL, 7-center, AUC 0.944 > experts."),
 ("39137488","Non-invasive prediction of axillary lymph node dissection exemption in breast cancer patients post-neoadjuvant therapy: A radiomics and deep learning analysis on longitudinal DCE-MRI data.","10.1016/j.breast.2024.103786",2024,"breast",["c"],"Low",["offtopic"],False,"Breast cancer, non-thyroid."),
 ("38990290","Artificial intelligence-based multi-modal multi-tasks analysis reveals tumor molecular heterogeneity, predicts preoperative lymph node metastasis and prognosis in papillary thyroid carcinoma: a retrospective study.","10.1097/JS9.0000000000001875",2025,"PTC",["c","d","e"],"High",["algorithm","singlecell","immune"],True,"Multimodal DL (pathogenomics+WSI) predicts LNM/DFS AUC 0.83-0.93; scRNA T-cell subsets."),
 ("37574759","Deep learning prediction model for central lymph node metastasis in papillary thyroid microcarcinoma based on cytology.","10.1111/cas.15930",2023,"PTMC",["c"],"High",["algorithm"],True,"FNA cytology DL predicts central LNM AUC 0.85."),
 ("40771372","Development and validation of a prediction model for lymph node metastasis in thyroid cancer: integrating deep learning and radiomics features from intra- and peri-tumoral regions.","10.21037/gs-2025-50",2025,"PTC",["c"],"High",["algorithm"],True,"US radiomics+DL fusion SVM CLNM AUC 0.897/0.881 external."),
 ("31746687","Lymph Node Metastasis Prediction from Primary Breast Cancer US Images Using Deep Learning.","10.1148/radiol.2019190372",2020,"breast",["c"],"Low",["offtopic"],False,"Breast cancer US DL, non-thyroid."),
 ("39421056","Radiomics and deep learning for large volume lymph node metastasis in papillary thyroid carcinoma.","10.21037/gs-24-308",2024,"PTC",["c"],"High",["algorithm"],True,"PTC LVLNM Thy-DL-Radiomics combined AUC 0.839/0.789 external."),
 ("36750791","Deep learning-based multifeature integration robustly predicts central lymph node metastasis in papillary thyroid cancer.","10.1186/s12885-023-10598-8",2023,"PTC",["c"],"High",["algorithm"],True,"CNN CLNM AUC 0.89 train / 0.78 test."),
 ("38563008","Predicting central cervical lymph node metastasis in papillary thyroid microcarcinoma using deep learning.","10.7717/peerj.16952",2024,"PTMC",["c"],"Medium",["algorithm"],True,"PTMC DL CLNM AUC ~0.65 (weak)."),
 ("39742800","Predicting lymph node metastasis in thyroid cancer: systematic review and meta-analysis on the CT/MRI-based radiomics and deep learning models.","10.1016/j.clinimag.2024.110392",2025,"TC",["c"],"Medium",["algorithm"],True,"SR/MA of 16 CT/MRI radiomics+DL LNM studies; pooled AUC 0.86-0.87."),
 ("39682228","Multimodal MRI Deep Learning for Predicting Central Lymph Node Metastasis in Papillary Thyroid Cancer.","10.3390/cancers16234042",2024,"PTC",["c"],"High",["algorithm"],True,"MRI+clinical DL (AMMCNet) CLNM AUC 0.891."),
 ("40778281","A novel deep learning model based on multimodal contrast-enhanced ultrasound dynamic video for predicting occult lymph node metastasis in papillary thyroid carcinoma.","10.3389/fendo.2025.1634875",2025,"PTC",["c"],"High",["algorithm"],True,"CEUS dynamic video DL OLNM AUC 0.734 test."),
 ("37178202","Artificial intelligence-based prediction of cervical lymph node metastasis in papillary thyroid cancer with CT.","10.1007/s00330-023-09700-2",2023,"PTC",["c"],"High",["algorithm"],True,"CT AI CLNM AUC 0.84/0.81 internal/external; boosts radiologist specificity."),
 ("41061579","SCLResNet and DSAF: A self-supervised contrastive learning and deep self-attention fusion-based multimodal network for predicting central lymph node metastasis in papillary thyroid carcinoma.","10.1016/j.artmed.2025.103280",2025,"PTC",["c"],"High",["algorithm"],True,"Self-supervised multimodal (US+PVAT CT) CLNM AUC 0.863/0.839."),
 ("41237514","A multi-task deep learning framework for intraoperative diagnosis of thyroid cancer metastasis using whole slide images.","10.1016/j.ijmedinf.2025.106176",2026,"PTC",["c"],"High",["algorithm"],True,"CLAM WSI multi-task (LNM/T-stage/localisation) AUC 0.85; 2-center."),

 # ---- query f: spatial transcriptomics / spatial multi-omics ----
 ("41398964","Integrated spatial metabolomics and transcriptomics reveal the molecular landscape of papillary thyroid cancer and its lymph node metastasis.","10.1186/s12967-025-07566-0",2025,"PTC",["f","i"],"High",["spatial","metabolic","molecular"],True,"Spatial multi-omics PTC LNM: arginine-polyamine/glycolysis; NAT8L/SVCT-2 validated."),
 ("42373830","Multi-omics reveals tumor microenvironment heterogeneity and therapeutic vulnerabilities in peritoneal metastasis of gastric cancer.","10.1038/s42003-026-10571-8",2026,"gastric",["f"],"Low",["offtopic"],False,"Gastric cancer peritoneal mets, non-thyroid."),
 ("41421038","Cellular and molecular determinants of lymph node metastasis in papillary thyroid carcinoma: Integrated multi-omics profiling and machine learning models.","10.1016/j.compbiolchem.2025.108857",2026,"PTC",["f"],"High",["singlecell","spatial","algorithm","molecular"],True,"scRNA+ST+bulk PTC LNM; FN1-SDC4 axis; 17-gene RF model."),
 ("41129052","Fibroblasts in the tumor microenvironment: heterogeneity and dynamic interactions in tumor progression revealed by spatial transcriptomics.","10.1007/s13402-025-01108-y",2025,"pan-cancer",["f"],"Low",["offtopic"],False,"Pan-cancer CAF spatial review (POSTN+ myCAF theme, not thyroid-specific)."),
 ("41608657","Breast cancer stem cell activity driven by ME18D gene expression in the tumor microenvironment.","10.4252/wjsc.v18.i1.111348",2026,"breast",["f"],"Low",["offtopic"],False,"Breast cancer stem cell, non-thyroid."),
 ("39923580","A comprehensive pan-cancer examination of transcription factor MAFF: Oncogenic potential, prognostic relevance, and immune landscape dynamics.","10.1016/j.intimp.2025.114105",2025,"pan-cancer",["f"],"Low",["offtopic"],False,"Pan-cancer MAFF TF, non-thyroid."),

 # ---- query e: single-cell RNA sequencing ----
 ("39540244","Spatial and Single-Cell Transcriptomics Unraveled Spatial Evolution of Papillary Thyroid Cancer.","10.1002/advs.202404491",2025,"PTC",["e"],"High",["singlecell","spatial"],True,"scRNA+SRT PTC evolution; ferroptosis resistance; malignant/metastatic footprints."),
 ("37696831","Single-cell transcriptome analysis indicates fatty acid metabolism-mediated metastasis and immunosuppression in male breast cancer.","10.1038/s41467-023-41318-2",2023,"breast",["e"],"Low",["offtopic"],False,"Male breast cancer, non-thyroid."),
 ("40719066","Single-Cell RNA Sequencing Reveals the Heterogeneity in Differentiation Trajectory and Tumor Microenvironment Leading to More Aggressive Phenotypes of Papillary Thyroid Cancer in Children and Young Adult Patients.","10.1002/advs.202417672",2025,"CAYA-PTC",["e"],"High",["singlecell","immune"],True,"CAYA-PTC scRNA: emCAF_LAMP5/FAP promotes angio+metastasis."),
 ("39221971","Tryptophan 2,3-dioxygenase-positive matrix fibroblasts fuel breast cancer lung metastasis via kynurenine-mediated ferroptosis resistance of metastatic cells and T cell dysfunction.","10.1002/cac2.12608",2024,"breast",["e","d"],"Low",["offtopic"],False,"Breast cancer lung mets CAF, non-thyroid."),
 ("36192735","CREB3L1 promotes tumor growth and metastasis of anaplastic thyroid carcinoma by remodeling the tumor microenvironment.","10.1186/s12943-022-01658-x",2022,"ATC",["e"],"High",["molecular","singlecell","immune"],True,"CREB3L1 drives ATC ECM/CAF niche via IL-1alpha + KPNA2."),
 ("41480746","An integrated single-cell and spatial transcriptomic atlas of thyroid cancer progression identifies prognostic fibroblast subpopulations.","10.1172/jci.insight.191990",2026,"TC",["e"],"High",["singlecell","spatial","immune"],True,"423,733-cell atlas; POSTN+ myCAF predicts LNM/progression (pediatric+adult)."),
 ("37501099","ISG15 and ISGylation modulates cancer stem cell-like characteristics in promoting tumor growth of anaplastic thyroid carcinoma.","10.1186/s13046-023-02751-9",2023,"ATC",["e"],"High",["singlecell","molecular"],True,"ISG15/KPNA2 maintains ATC stemness + mets (scRNA)."),
 ("41257484","Single-cell RNA sequencing reveals tumor cell and immune cell variations associated with lymphatic metastasis in papillary thyroid cancer.","10.1530/EC-25-0514",2025,"PTC",["e"],"High",["singlecell","immune"],True,"PTC LNM scRNA: CD8+ TRM (MHC-I/CD99/LCK) pivotal regulators."),
 ("38146045","Single-cell and bulk RNA sequencing reveal heterogeneity and diagnostic markers in papillary thyroid carcinoma lymph-node metastasis.","10.1007/s40618-023-02262-6",2024,"PTC",["e"],"High",["singlecell","molecular"],True,"PTC LNM scRNA+bulk: S100A2/DIO2 diagnostic model (66-pt validation)."),
 ("40201390","Comprehensive Analyses of Single-Cell and Bulk RNA Sequencing Data From M2 Macrophages to Elucidate the Immune Prognostic Signature in Patients with Gastric Cancer Peritoneal Metastasis.","10.2147/ITT.S506143",2025,"gastric",["e"],"Low",["offtopic"],False,"Gastric cancer peritoneal mets, non-thyroid."),
 ("40593465","The SOX12-YBX1-LDHA signaling axis drives metastasis in papillary thyroid carcinoma.","10.1038/s41419-025-07797-5",2025,"PTC",["e"],"High",["molecular","singlecell","metabolic"],True,"SOX12-YBX1-LDHA (TGF-beta) PTC metastasis; LDHA glycolytic."),
 ("40315321","Targeting HMGB2 acts as dual immunomodulator by bolstering CD8+ T cell function and inhibiting tumor growth in hepatocellular carcinoma.","10.1126/sciadv.ads8597",2025,"HCC",["e"],"Low",["offtopic"],False,"HCC HMGB2 CD8 T cell, non-thyroid."),
 ("39829764","An integrated single-cell and spatial transcriptomic atlas of thyroid cancer progression identifies prognostic fibroblast subpopulations.","10.1101/2025.01.08.631962",2025,"TC",["e"],"Low",["offtopic"],False,"Preprint duplicate of 41480746 (same Loberg atlas) - excluded as duplicate."),

 # ---- query d: immune microenvironment ----
 ("41057823","Exosome-mediated metabolic reprogramming: effects on thyroid cancer progression and tumor microenvironment remodeling.","10.1186/s12943-025-02470-z",2025,"TC",["d","i"],"Medium",["metabolic","immune"],True,"Review: exosomes drive TC metabolic reprogramming + immune escape."),
 ("38981044","Lactylated Apolipoprotein C-II Induces Immunotherapy Resistance by Promoting Extracellular Lipolysis.","10.1002/advs.202406333",2024,"NSCLC",["d"],"Low",["offtopic"],False,"NSCLC lactylation immunotherapy, non-thyroid."),
 ("39615165","Decoding tumor microenvironment: EMT modulation in breast cancer metastasis and therapeutic resistance, and implications of novel immune checkpoint blockers.","10.1016/j.biopha.2024.117714",2024,"breast",["d"],"Low",["offtopic"],False,"Breast cancer TME-EMT, non-thyroid."),
 ("32626535","Immune Microenvironment of Thyroid Cancer.","10.7150/jca.44506",2020,"TC",["d"],"Medium",["immune"],True,"Review: immune cells/checkpoints/escape in TC."),
 ("39903533","5-HT orchestrates histone serotonylation and citrullination to drive neutrophil extracellular traps and liver metastasis.","10.1172/JCI183544",2025,"MTC",["d"],"High",["immune","prognosis"],True,"5-HT/SERT/NETs drive MTC (and NE) liver mets; fluoxetine blocks."),
 ("40207795","SERPINE1 Facilitates Metastasis in Gastric Cancer Through Anoikis Resistance and Tumor Microenvironment Remodeling.","10.1002/smll.202500136",2025,"gastric",["d"],"Low",["offtopic"],False,"Gastric cancer SERPINE1, non-thyroid."),
 ("36975413","Tumor-Infiltrating Immune Cell Landscapes in the Lymph Node Metastasis of Papillary Thyroid Cancer.","10.3390/curroncol30030200",2023,"PTC",["d"],"High",["immune"],True,"PTC LNM immune landscape: M2 macrophage/NK/eosinophil shifts; TG/HRAS driver effects."),
 ("37173925","The Tumor Microenvironment and the Estrogen Loop in Thyroid Cancer.","10.3390/cancers15092458",2023,"TC",["d"],"Medium",["immune"],True,"Review: estrogen-TME crosstalk in TC."),
 ("37279258","Papillary thyroid cancer immune phenotypes via tumor-infiltrating lymphocyte spatial analysis.","10.1530/ERC-23-0110",2023,"PTC",["d"],"High",["immune","spatial"],True,"TIL spatial IPs: immune-desert/excluded/inflamed; BRAF V600E linked LNM."),
 ("33654093","RNA m6A methylation orchestrates cancer growth and metastasis via macrophage reprogramming.","10.1038/s41467-021-21514-8",2021,"pan-cancer",["d"],"Low",["offtopic"],False,"General m6A/METTL3 macrophage, non-thyroid."),
 ("40256431","Lipid metabolism involved in progression and drug resistance of breast cancer.","10.1016/j.gendis.2024.101376",2025,"breast",["d"],"Low",["offtopic"],False,"Breast cancer lipid metabolism, non-thyroid."),

 # ---- query i: metabolic reprogramming ----
 ("39747873","The protein circPETH-147aa regulates metabolic reprogramming in hepatocellular carcinoma cells to remodel immunosuppressive microenvironment.","10.1038/s41467-024-55577-0",2025,"HCC",["i"],"Low",["offtopic"],False,"HCC circRNA metabolism, non-thyroid."),
 ("37031273","LncRNA GLTC targets LDHA for succinylation and enzymatic activity to promote progression and radioiodine resistance in papillary thyroid cancer.","10.1038/s41418-023-01157-6",2023,"PTC",["i"],"High",["metabolic","molecular"],True,"GLTC-LDHA K155 succinylation drives PTC glycolysis + RAI resistance."),
 ("38953696","ACSL3 regulates breast cancer progression via lipid metabolism reprogramming and the YES1/YAP axis.","10.20892/j.issn.2095-3941.2023.0309",2024,"breast",["i"],"Low",["offtopic"],False,"Breast cancer lipid metabolism, non-thyroid."),
 ("40470773","METTL14-Mediated M6A Modification of LINC01094 Induces Glucose Metabolic Reprogramming in Breast Cancer by Recruiting the PKM2/JMJD5 Complex.","10.1002/advs.202410386",2025,"breast",["i"],"Low",["offtopic"],False,"Breast cancer m6A metabolism, non-thyroid."),
 ("39192979","The role of metabolic reprogramming in immune escape of triple-negative breast cancer.","10.3389/fimmu.2024.1424237",2024,"TNBC",["i"],"Low",["offtopic"],False,"TNBC metabolic immune escape, non-thyroid."),
 ("38272883","SHMT2 promotes papillary thyroid cancer metastasis through epigenetic activation of AKT signaling.","10.1038/s41419-024-06476-1",2024,"PTC",["i"],"High",["metabolic","molecular"],True,"SHMT2 serine metabolism -> SAM -> PTEN methylation -> AKT mets."),
 ("42327722","MGST1 drives lymph node metastasis in papillary thyroid carcinoma via mitochondrial metabolic reprogramming and immune suppression.","10.3389/fimmu.2026.1848083",2026,"PTC",["i"],"High",["metabolic","immune","algorithm","molecular"],True,"MGST1 'Mito-high' subtype; ML model AUC 0.833; Toxoflavin reverses immune-cold."),
 ("41219790","A novel protein cPFKFB4 encoded by hsa_circ_0065394 strengthens PKM2-mediated glucose metabolic reprogramming to facilitate pancreatic cancer progression under hypoxia.","10.1186/s12943-025-02500-w",2025,"pancreas",["i"],"Low",["offtopic"],False,"Pancreatic cancer circRNA, non-thyroid."),
 ("40353071","Reprogramming of fatty acid metabolism in thyroid cancer: Potential targets and mechanisms.","10.21147/j.issn.1000-9604.2025.02.09",2025,"TC",["i"],"Medium",["metabolic"],True,"Review: FA metabolic reprogramming in TC mets/immune escape."),
 ("40980146","Thyroid cancer: From molecular insights to therapy (Review).","10.3892/ol.2025.15266",2025,"TC",["i"],"Medium",["molecular"],True,"Review: 4 subtypes (PTC/FTC/MTC/ATC) molecular + metabolic + therapy."),
 ("42280115","PKM2-Mediated Glycolytic Reprogramming in Thyroid Cancer: Mechanistic Insights and Therapeutic Potential.","10.3390/molecules31111811",2026,"TC",["i"],"Medium",["metabolic"],True,"Review: PKM2 glycolytic reprogramming in TC."),
 ("40850678","Research progress and therapeutic strategies in hepatocellular carcinoma metabolic reprogramming.","10.1016/j.jare.2025.08.023",2026,"HCC",["i"],"Low",["offtopic"],False,"HCC metabolic review, non-thyroid."),

 # ---- query g: prognosis / recurrence / distant metastasis ----
 ("31792675","A novel RNA sequencing-based risk score model to predict papillary thyroid carcinoma recurrence.","10.1007/s10585-019-10011-4",2020,"PTC",["g"],"High",["algorithm","prognosis"],True,"5-gene RNA-seq recurrence risk score (TOP2A...) HR 6.62/3.40."),
 ("41877795","Development and validation of a machine learning model for predicting high-risk distant metastatic recurrence in differentiated thyroid cancer.","10.3389/fmed.2026.1790226",2026,"DTC",["g"],"High",["algorithm","prognosis"],True,"XGBoost DTC distant-met recurrence (1245 pts) AUC 0.88 external."),
 ("37851243","BRAF V600E mutation in papillary thyroid microcarcinoma: is it a predictor for the prognosis of patients with intermediate to high recurrence risk?","10.1007/s12020-023-03564-8",2024,"PTMC",["g"],"Medium",["prognosis","molecular"],True,"BRAF V600E PTMC: linked multifocality/ETE but NOT recurrence after RAI."),
 ("32615728","Development and Validation of a Risk Scoring System Derived from Meta-Analyses of Papillary Thyroid Cancer.","10.3803/EnM.2020.35.2.435",2020,"PTC",["g"],"Medium",["prognosis"],True,"RSS from 5 meta-analyses (8 vars) outperforms AJCC/ATA."),
 ("29405275","Surgeon volume and prognosis of patients with advanced papillary thyroid cancer and lateral nodal metastasis.","10.1002/bjs.10655",2018,"PTC",["g"],"Low",["offtopic"],False,"Pure clinical epidemiology (surgeon volume), not mechanism-focused."),
 ("37934030","A novel cuproptosis-related lncRNA prognostic signature in thyroid cancer.","10.2217/bmm-2023-0216",2023,"TC",["g"],"Medium",["prognosis","algorithm"],True,"4 cuproptosis-lncRNA prognostic model AUC 0.79-0.83."),
 ("38311812","Pregnancy and the disease recurrence of patients previously treated for differentiated thyroid cancer: A systematic review and meta analysis.","10.1097/CM9.0000000000003008",2024,"DTC",["g"],"Low",["offtopic"],False,"Pure clinical epidemiology (pregnancy recurrence), non-mechanism."),
 ("41084771","Aggressiveness of papillary thyroid carcinoma: a comprehensive analysis from molecular mechanisms to clinical applications.","10.5603/fhc.108530",2025,"PTC",["g"],"Medium",["molecular","immune"],True,"Review: PTC aggressiveness mechanisms + imaging/AI."),
 ("31412224","PROGNOSIS OF DIFFERENTIATED THYROID CARCINOMA IN PATIENTS WITH GRAVES DISEASE: A SYSTEMATIC REVIEW AND META-ANALYSIS.","10.4158/EP-2019-0201",2019,"DTC",["g"],"Low",["offtopic"],False,"Pure clinical epidemiology (Graves disease), non-mechanism."),
 ("27697309","Recurrence factors and prevention of complications of pediatric differentiated thyroid cancer.","10.1016/j.asjsur.2016.09.001",2017,"pediatric DTC",["g"],"Medium",["prognosis"],True,"Pediatric DTC recurrence: ETE + LNM risk factors."),
 ("36704213","Breast-Conserving Surgery in Triple-Negative Breast Cancer: A Retrospective Cohort Study.","10.1155/2023/5431563",2023,"TNBC",["g"],"Low",["offtopic"],False,"Triple-negative breast cancer, non-thyroid."),
 ("37132252","Investigating the impact of tumor location and size on the risk of recurrence for papillary thyroid carcinoma in the isthmus.","10.1002/cam4.6023",2023,"PTC",["g"],"Low",["offtopic"],False,"Pure radiology/clinical (isthmus CT geometry), non-mechanism."),
 ("41817109","Selective Use of Radioiodine Therapy in Differentiated Thyroid Carcinoma: A Population-Based Cohort Study.","10.1177/10507256261416869",2026,"DTC",["g"],"Low",["offtopic"],False,"Pure clinical epidemiology (RAI population), non-mechanism."),
 ("32668875","[Predictive analysis of distant metastasis after primary treatment of papillary thyroid cancer in patients under 18 years old].","10.3760/cma.j.cn115330-20000115-00025",2020,"pediatric PTC",["g"],"Medium",["prognosis"],True,"Pediatric PTC distant mets: age<=15 + bilateral independent risks."),
 ("41419184","Prognostic Value of BRAF V600E Mutation in Papillary Thyroid Carcinoma: A Meta-Analysis of Nodal Involvement, Distant Metastases, Recurrence, and Mortality.","10.1016/j.eprac.2025.12.003",2026,"PTC",["g"],"High",["prognosis","molecular"],True,"Meta (46k pts): BRAF V600E OR nodal 1.38 / recurrence 1.56, NOT distant/death."),

 # ---- query h: metastatic stemness subpopulation ----
 ("25426258","Stem cell biology in thyroid cancer: Insights for novel therapies.","10.4252/wjsc.v6.i5.614",2014,"TC",["h"],"Medium",["molecular"],True,"Review: CSCs/EMT in thyroid cancer, identification markers."),
 ("33186350","Nucleotide de novo synthesis increases breast cancer stemness and metastasis via cGMP-PKG-MAPK signaling pathway.","10.1371/journal.pbio.3000872",2020,"breast",["h"],"Low",["offtopic"],False,"Breast cancer stemness, non-thyroid."),
 ("39595993","DLK1 Is Associated with Stemness Phenotype in Medullary Thyroid Carcinoma Cell Lines.","10.3390/ijms252211924",2024,"MTC",["h"],"Medium",["molecular"],True,"DLK1+ enriches stemness in MTC (MZ-CRC-1 > TT)."),
]

records = []
for (pmid,title,doi,year,disease,queries,relevance,dimensions,in_scope,note) in R:
    records.append({
        "pmid": pmid, "title": title, "doi": doi, "year": year,
        "disease": disease, "queries": queries, "relevance": relevance,
        "dimensions": dimensions, "in_scope": in_scope, "note": note
    })

unique = len(records)
in_scope = sum(1 for r in records if r["in_scope"])
excluded = unique - in_scope

out = {
    "search_date": "2026-07-26",
    "source": "PubMed via paper-search-mcp search_pubmed (DeferExecuteTool)",
    "queries": {
        "a": "thyroid cancer lymph node metastasis biomarker gene signature",
        "b": "thyroid cancer invasion metastasis molecular mechanism",
        "c": "thyroid cancer lymph node metastasis machine learning deep learning prediction model",
        "d": "thyroid cancer metastasis tumor immune microenvironment",
        "e": "thyroid cancer metastasis single cell RNA sequencing",
        "f": "thyroid cancer metastasis spatial transcriptomics spatial multi-omics",
        "g": "thyroid cancer prognosis recurrence distant metastasis risk model",
        "h": "thyroid cancer metastatic stemness subpopulation",
        "i": "thyroid cancer metabolic reprogramming metastasis",
    },
    "raw_count": unique,
    "unique_count": unique,
    "in_scope_count": in_scope,
    "excluded_count": excluded,
    "records": records,
}

with open(r"D:\paperwork\lit_review\search_results_latest.json","w",encoding="utf-8") as f:
    json.dump(out,f,ensure_ascii=False,indent=2)

print("records:",unique,"in_scope:",in_scope,"excluded:",excluded)
