# Literature Review: Thyroid Cancer Lymph Node Metastasis (LNM) — Biomarkers, Signatures & Prediction Models

Date: 2026-07-19
Sources: PubMed (via paper-search-mcp)
Search window: all time, sorted by relevance
Topic scope: papillary thyroid carcinoma (PTC) and thyroid carcinoma (THCA) lymph-node metastasis — molecular biomarkers, gene-expression signatures, machine-learning / deep-learning prediction models.

> Note on scope: 45 records were retrieved across 3 complementary queries. 41 are thyroid-relevant and form the evidence base below; 4 records were retrieved but are OUT OF SCOPE (lymph-node metastasis in non-thyroid cancers — lung adenocarcinoma PMID:36793937, breast cancer PMID:30950057 / PMID:39137488 / PMID:40620610) and are excluded from the evidence matrix.

---

## Search Strategy

| Source | Query | Filters | Results | Notes |
|---|---|---|---:|---|
| PubMed | `papillary thyroid carcinoma lymph node metastasis biomarker` | relevance, max 15 | 15 | Biomarker / mechanism / wet-lab angle |
| PubMed | `thyroid cancer lymph node metastasis gene expression signature TCGA` | relevance, max 15 | 15 | Transcriptomic signatures & public-data reuse |
| PubMed | `thyroid cancer lymph node metastasis machine learning prediction model` | relevance, max 15 | 15 | ML/DL radiogenomic & gene-classifier angle |
| — | cross-query dedup | — | 45 → 41 in-scope | 4 off-topic (non-thyroid LNM) removed |

---

## Included Papers (thyroid-relevant, n=41)

Key primary studies (claim + agent caution). Reviews/meta-analyses are flagged.

1. BRAF V600E & TERT in PTC LNM. *Soeratman et al.* APJCP 2024. PMID:38918666. DOI:10.31557/APJCP.2024.25.6.2043.
   Author claim: BRAF V600E strongly associated with LNM (OR 25.33); TERT+ with BRAF raises risk to OR 60. Agent note: small Indonesian cohort (n=42); cross-sectional; BRAF–LNM link is well established — low novelty, useful as clinical anchor.
2. Systematic review: miRNAs as LNM risk factor in PTC. *Laukiene et al.* Endokrynol Pol 2021. PMID:33970479. DOI:10.5603/EP.a2021.0010. (REVIEW)
   Author claim: miR-146B/-221/-222/-21/-204/-451/-199a-3p/-30a-3p dysregulated in ≥2 studies; prognostic value limited. Agent note: consensus weak; heterogeneity across studies.
3. 14-gene PTC metastasis risk set. *Zhang et al.* Front Endocrinol 2022. PMID:36465624. DOI:10.3389/fendo.2022.991906.
   Author claim: CLDN1/LRP4/LRRK2/TENM1 high; DIO1/HGD/SLC26A4/TPO low; core risk = iodine-metabolism genes. Agent note: GEO + RT-qPCR + IHC; no external cohort.
4. MGST1 drives LNM via mitochondrial reprogramming & immune suppression. *Wang et al.* Front Immunol 2026. PMID:42327722. DOI:10.3389/fimmu.2026.1848083.
   Author claim: MGST1 top ML predictor, AUC 0.833 external; Toxoflavin inhibits. Agent note: multi-omics + independent cohort + scRNA + pharmacology — one of the strongest recent mechanistic papers; 2026 date, verify journal status.
5. Hashimoto's thyroiditis protects against CLNM/LLNM. *Wang et al.* EJSO 2023. PMID:36404253. DOI:10.1016/j.ejso.2022.11.014.
   Author claim: HT protective for both central & lateral LNM in 4131 PTC. Agent note: large cohort; clinical confounder, not a molecular marker.
6. Multi-omics + ML multi-gene classifier for LATERAL LNM. *Yu et al.* Endocrine 2025. PMID:40517210. DOI:10.1007/s12020-025-04308-6.
   Author claim: WES+WTS (50 PTC); tumor-infiltrating neutrophils predictor; classifier AUC 0.98 train / 0.892 test. Agent note: small discovery set (50); strong but needs validation.
7. Targeted DNA/RNA seq + radiomics nomogram. *Zhang et al.* Cancer Imaging 2024. PMID:38886866. DOI:10.1186/s40644-024-00719-2.
   Author claim: ATM co-mutation+ LNM; radiomic+gene+clinical AUC 87% (vs 71.5%). Agent note: multi-modal integration; retrospective.
8. CXCL8 associated with PTC LNM. *Liu et al.* Sci Rep 2025. PMID:41290801. DOI:10.1038/s41598-025-25686-x.
   Author claim: CXCL8↑, +LNM, PI3K-Akt, dendritic-cell association. Agent note: bioinformatics + small validation.
9. Review: miRNAs & LNM in PTC. *Mutalib et al.* 2016. PMID:26838219. (REVIEW) — association still controversial.
10. Serum sEV-BST2 biomarker for PTMC LNM. *Cao et al.* Cancer Gene Ther 2025. PMID:39558134. DOI:10.1038/s41417-024-00854-9.
    Author claim: sEV-BST2 promotes proliferation/migration/lymphangiogenesis. Agent note: liquid-biopsy angle; n=29 small.
11. Ki-67 labeling index & CLNM/DFS. *Lei et al.* Cancer Control 2023. PMID:36744396. DOI:10.1177/10732748231155701.
    Author claim: Ki-67 >5% OR 3.85 for CLNM; validated in TCGA + GSE60542. Agent note: IHC marker, clinically actionable.
12. RET variation & nodal mets + immune microenvironment. *Huang et al.* BMC Endocr Disord 2024. PMID:38734621. DOI:10.1186/s12902-024-01586-5.
    Author claim: RET variation + nodal mets in 108 Chinese PTC; immune-cycle steps altered. Agent note: NGS, population-specific.
13. Nrf2 as diagnostic + LNM predictor. *Wang et al.* Eur J Histochem 2023. PMID:36951264. DOI:10.4081/ejh.2023.3622.
    Author claim: Nrf2 sens 96%/spec 88.6% for LNM (n=120). Agent note: small single-center.
14. Plasma exosomal miRNAs for LNM. *Chen et al.* Endocrine 2022. PMID:34854020. DOI:10.1007/s12020-021-02949-x.
    Author claim: miR-6774-3p + miR-6879-5p combo AUC 0.914. Agent note: liquid biopsy; stable to RNase.
15. scRNA + bulk DIO2/S100A2 diagnostic markers. *Lu et al.* J Endocrinol Invest 2024. PMID:38146045. DOI:10.1007/s40618-023-02262-6.
    Author claim: 19-gene model; DIO2 inhibits proliferation (G2/M arrest). Agent note: heterogeneity + wet-lab; good integration.
16. Spatial multi-omics of PTC + LNM. *Li et al.* J Transl Med 2025. PMID:41398964. DOI:10.1186/s12967-025-07566-0.
    Author claim: arginine-polyamine/glycolysis/lipid axes; NAT8L & SVCT-2 knockdown reduces metastasis; 10 pro-metastatic metabolite genes in TCGA. Agent note: emerging spatial niche; few public datasets.
17. Integrated miRNA+gene+TF in PTC LNM. *Ab Mutalib et al.* PeerJ 2016. PMID:27350898. DOI:10.7717/peerj.2119.
    Author claim: 181 DEG miRNAs; OxPhos downregulation central to LNM. Agent note: early TCGA reanalysis.
18. **COMPETITOR** 6-gene signature (COL8A2/MET/FN1/MPZL2/PDLIM4/CLDN10). *Li et al.* Int J Gen Med 2025. PMID:40110574. DOI:10.2147/IJGM.S502480.
    Author claim: 52 DEGs → 6 hub genes via WGCNA (TCGA+GEO+GSE60542), in-vitro validated. Agent note: direct competitor to a gene-signature proposal; MET & FN1 recur across multiple signatures (convergent evidence).
19. WGCNA co-expression modules & hub genes. *Zhai et al.* Endocrine 2019. PMID:31332712. DOI:10.1007/s12020-019-02021-9.
    Author claim: 11 hub genes (MET, FN1, ITGA3, RUNX1…); ECM/mitochondrial/cell-junction modules. Agent note: MET & FN1 converge again.
20. 3-gene nomogram (IQGAP2/BTBD11/MT1G) + clinical. *Yang et al.* 2025. PMID:40171809. DOI:10.1177/18758592241311195.
    Author claim: AUC 0.802 train / 0.718 val. Agent note: parsimonious; modest validation.
21. GABRB2 oncogene in PTC LNM. *Jin et al.* Biochem Biophys Res Commun 2017. PMID:28859983. DOI:10.1016/j.bbrc.2017.08.114.
    Author claim: GABRB2↑, correlated LNM, TCGA-confirmed; knockdown reduces invasion. Agent note: older; under-followed.
22. Metabolic gene signature of dedifferentiation. *Ma et al.* J Clin Endocrinol Metab 2019. PMID:30942873. DOI:10.1210/jc.2018-02686.
    Author claim: LPCAT2/ACOT7/HSD17B8/PDE8B/ST3GAL1; associated with LNM. Agent note: links metabolism↔dedifferentiation↔LNM.
23. 4-eRNA signature (prognosis/N stage). *Liang et al.* Exp Cell Res 2022. PMID:35033555. DOI:10.1016/j.yexcr.2022.113023.
    Author claim: AC141930.1/NBDY/MEG3/AP002358.1 linked to N stage. Agent note: prognostic, not LNM-specific prediction.
24. lncRNA profile & LNM co-expressed genes. *Zhang et al.* Med Sci Monit 2019. PMID:31856144. DOI:10.12659/MSM.917845.
    Author claim: LINC01016/LHX1-DT/IGF2-AS/NDMIR1-1HG-AS1 related to LNM. Agent note: survival model primary.
25. 2-miRNA signature (male TC). *Liu et al.* 2021. PMID:34595349. DOI:10.1515/biol-2021-0099.
    Author claim: miR-451a / miR-16-1-3p independent DFS factors in male TC. Agent note: sex-stratified; niche.
26. miRNome of PTC primary + LNM. *Saiselet et al.* BMC Genomics 2015. PMID:26487287. DOI:10.1186/s12864-015-2082-3.
    Author claim: miR-146b-5p/-222-3p up; miR-7-5p/-30c-2-3p down; BRAF V600E drives aggressive profile. Agent note: foundational.
27. 12-gene nodal-metastasis signature. *Choi et al.* 2018. PMID:29562496. DOI:10.3233/CBM-170784.
    Author claim: 12 genes; TCGA training 158 / val 80. Agent note: preoperative FNAB potential.
28. Coagulation genes & D-dimer for LLNM. *Sun et al.* Front Immunol 2024. PMID:39497824. DOI:10.3389/fimmu.2024.1462755.
    Author claim: D-dimer AUC 0.656 for LLNM; 8-CRG prognostic model. Agent note: D-dimer weak standalone;凝血 axis underexplored.
29. LLNM-Net multimodal DL ultrasound. *Shen et al.* Nat Commun 2025. PMID:40750786. DOI:10.1038/s41467-025-62042-z.
    Author claim: 29,615 pts / 9836 surgical; AUC 0.944, acc 84.7%, beats experts (64.3%). Agent note: large multicenter; imaging not molecular.
30. scRNA + spatial: APOE− subpopulation → cervical mets. *Xiao et al.* Clin Transl Med 2025. PMID:39810624. DOI:10.1002/ctm2.70172.
    Author claim: APOE− cells via ABCA1-LXR; 13-gene ML signature. Agent note: stem-like metastatic subpopulation — novel, targetable.
31. AI multimodal multi-task (histopath+genomic+transcriptomic+immune). *Yu et al.* 2025. PMID:38990290. DOI:10.1097/JS9.0000000000001875.
    Author claim: 1011 PTC; AUC 0.86/0.84/0.83; DFS prediction. Agent note: broad integration; GradCAM interpretability.
32. ML dynamic prediction of LLNM (web tool). *Lai et al.* Front Endocrinol 2022. PMID:36299455. DOI:10.3389/fendo.2022.1019037.
    Author claim: random forest AUC 0.80, acc 0.74, 1135/1815 LLNM. Agent note: clinical-feature only; deployed web tool.
33. XGBoost for paratracheal LNM in cN0 PTC. *Chun et al.* Sci Rep 2024. PMID:39333646. DOI:10.1038/s41598-024-73837-3.
    Author claim: AUC 0.935/0.857/0.775 (train/val/test) + external 533. Agent note: interpretable SHAP; good external set.
34. GBM multimodal radiomics LLNM. *Feng et al.* Front Endocrinol 2025. PMID:40904800. DOI:10.3389/fendo.2025.1618902.
    Author claim: GBM AUC 0.973/0.803/0.975 (train/internal/external). Agent note: very high training AUC → leakage risk.
35. RF for occult CLNM (OLNM) in cN0 PTC. *Wang et al.* J Clin Endocrinol Metab 2026. PMID:41378767. DOI:10.1210/clinem/dgaf636.
    Author claim: RET fusion & BRAF independent molecular risk factors; RF AUC 0.906/0.733. Agent note: first to flag RET fusion for OLNM; web calculator.
36. Radiomics+DL fusion for CLNM. *Zhong et al.* 2025. PMID:40771372. DOI:10.21037/gs-2025-50.
    Author claim: fusion SVM AUC 0.897 internal / 0.881 external. Agent note: peri-tumoral region adds value.
37. DL cytology for PTMC CLNM. *Ren et al.* Cancer Sci 2023. PMID:37574759. DOI:10.1111/cas.15930.
    Author claim: FNA liquid-based DL AUC 0.8503. Agent note: small (n=42 test); promising noninvasive.
38. ML 3-gene (RPS4Y1/PKHD1L1/CRABP1) multicenter. *Liu et al.* 2025. PMID:40265473. DOI:10.1097/JS9.0000000000002400.
    Author claim: RF AUC 0.992 train / 0.911–0.953 external (807 qRT-PCR). Agent note: very high AUC → possible leakage/overfit; needs scrutiny.
39. ML for MTC LLNM. *Zhang et al.* Cancer Med 2024. PMID:38808852. DOI:10.1002/cam4.7155.
    Author claim: AUC 0.92 test; 0.91 occult LLNM. Agent note: medullary subtype; distinct from PTC.
40. SVM for LLNM (ultrasound). *Huang et al.* 2023. PMID:36761483. DOI:10.21037/gs-22-741.
    Author claim: SVM AUC 0.91, acc 90.8%. Agent note: single-center 253.
41. **META-ANALYSIS** ML prediction models for LNM in thyroid cancer. *Liu et al.* 2024. PMID:39438906. DOI:10.1186/s12957-024-03566-4. (META)
    Author claim: 107 studies, 136,245 pts; c-index 0.762–0.829; logistic regression most common (81%); PROBAST bias concerns. Agent note: field-level synthesis; confirms crowding + methodology weakness.

---

## Evidence Matrix

| Paper | PMID/DOI | Disease/Population | Data Source | Method | Endpoint | Main Finding | Validation | Limitations | Relevance | Gap Suggested | Future Direction |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Soeratman 2024 | 38918666 | PTC, Indonesia | Clinical cohort n=42 | PCR, χ² | LNM | BRAF V600E OR 25.3; +TERT OR 60 | None | Tiny cohort | Low | BRAF–LNM well known | Clinical risk model |
| Zhang 2022 | 36465624 | PTC | GEO + IHC | GEO2R, RT-qPCR | Metastasis risk | 14 DEGs; DIO1/HGD/SLC26A4/TPO core | IHC clinical | No external | Med | Iodine-metabolism link unvalidated molecularly | Wet-lab iodine axis |
| Wang 2026 | 42327722 | PTC | TCGA/GTEx + cohort + scRNA | Multi-omics ML | LNM | MGST1 AUC 0.833; Mito-high subtype | Independent cohort + pharm | 2026, verify | High | MGST1 therapeutically actionable? | Target MGST1 axis |
| Yu 2025 | 40517210 | PTC (lateral) | WES+WTS n=50 | ML classifier | Lateral LNM | AUC 0.98/0.892; neutrophils | Test set only | Small discovery | High | Neutrophil role mechanistic? | Immune-metabolic link |
| Zhang 2024 | 38886866 | PTC | Targeted seq + radio | Nomogram | LNM | ATM co-mut+; AUC 87% | Internal | Retrospective | Med | ATM mechanism in LNM | Gene+radio fusion |
| Liu 2025 | 41290801 | PTC | TCGA + TMA | Bioinformatics | LNM | CXCL8↑ +LNM, PI3K-Akt | qRT-PCR/IHC | Small | Med | CXCL8 immune crosstalk | Immune target |
| Cao 2025 | 39558134 | PTMC | Serum sEV proteomics | DIA | LNM | sEV-BST2 promotes mets | Knockdown/oe | n=29 | Med | Liquid biopsy generalizability | sEV panel |
| Lei 2023 | 36744396 | PTC | TCGA+GSE60542+clinical | IHC, regression | CLNM/DFS | Ki-67>5% OR 3.85 | TCGA+GSE60542 | Retro | Med | Ki-67 cutoff standardization | IHC+ molecular |
| Huang 2024 | 38734621 | Chinese PTC | NGS n=108 | Mutational + TIM | Nodal mets | RET variation+ mets | TCGA TIM | Population | Med | RET–immune mechanism | RET fusion stratification |
| Wang 2023 | 36951264 | PTC | n=120 | IHC | LNM | Nrf2 sens96/spec88.6 | None | Small | Low | Nrf2 mechanism | — |
| Lu 2024 | 38146045 | PTC | scRNA+bulk | 19-gene model | LNM | DIO2 inhibits prolif (G2/M) | RT-qPCR/IHC | Single | High | DIO2 therapeutically? | scRNA diagnostic |
| Li 2025 (spatial) | 41398964 | PTC | Spatial multi-omics | Metabolite mapping | LNM | Polyamine/glycolysis; NAT8L/SVCT-2 | Zebrafish, TCGA | Few public | High | Spatial niche causal? | Spatial metastasis niche |
| Ab Mutalib 2016 | 27350898 | PTC | TCGA | miRNA+TF | LNM/DFS | OxPhos downregulation central | None | Early | Med | OxPhos–LNM mechanism | Metabolic axis |
| Li 2025 (competitor) | 40110574 | PTC | TCGA+GEO+GSE60542 | WGCNA+LASSO | LNM | 6-gene: COL8A2/MET/FN1/MPZL2/PDLIM4/CLDN10 | In-vitro | Public-data reuse | High | Overlaps others? | Benchmark against |
| Zhai 2019 | 31332712 | PTC | TCGA | WGCNA | N stage/relapse | 11 hub (MET,FN1,ITGA3…) | None | No ext | Med | ECM module causal | ECM–MET axis |
| Yang 2025 | 40171809 | PTC | TCGA | LASSO nomogram | LNM | 3-gene IQGAP2/BTBD11/MT1G AUC 0.80 | Val 0.718 | Modest | Med | External validation | Parsimonious panel |
| Jin 2017 | 28859983 | PTC | TCGA+cohort | Reseq+functional | LNM | GABRB2↑, knockdown↓invasion | TCGA+fn | Older | Low | GABRB2 follow-up | — |
| Ma 2019 | 30942873 | PTC/DDTC | TCGA+GEO | Metabolic sig | LNM/dediff | 5 metabolic genes; LNM p<0.001 | 3 cohorts | Indirect | Med | Metabolic↔dediff↔LNM | Metabolic target |
| Liang 2022 | 35033555 | TC | GTEx+TCGA | eRNA Cox | N stage | 4 eRNA sig | None | Prognostic | Low | eRNA–LNM direct? | — |
| Zhang 2019 | 31856144 | TC | TCGA | lncRNA Cox | LNM (subset) | LINC01016 etc related LNM | None | Survival focus | Low | lncRNA mechanism | — |
| Liu 2021 | 34595349 | Male TC | TCGA | miRNA Cox | DFS | miR-451a/miR-16-1-3p | None | Sex-specific | Low | Male-specific LNM? | — |
| Saiselet 2015 | 26487287 | PTC+LNM | TCGA smallRNA | miRNome | LNM | miR-146b/-222 up; miR-7/-30c down | 14 pts qRT-PCR | Foundational | Med | Arm-ratio/LNM | — |
| Choi 2018 | 29562496 | PTC | TCGA | Clustering+logit | Nodal mets | 12-gene sig | Val 80 | FNAB potential | Med | Preop validation | FNAB panel |
| Sun 2024 | 39497824 | THCA | TCGA+clinical | ROC+LASSO | LLNM | D-dimer AUC 0.656; 8-CRG | qPCR | Weak D-dimer | Low | Coagulation–LNM | Coag axis |
| Shen 2025 | 40750786 | PTC | 7-center imaging | Multimodal DL | Lateral LNM | LLNM-Net AUC 0.944, acc 84.7% | Multicenter | Imaging | High | Non-molecular | Imaging+gene fuse |
| Xiao 2025 | 39810624 | PTC | scRNA+spatial | ML 13-gene | Cervical mets | APOE− subpop (ABCA1-LXR) | In-vivo | New | High | Stem-like targetable? | APOE− subpopulation |
| Yu 2025 (AI) | 38990290 | PTC | 1011 (real+TCGA) | Multimodal DL | LNM/DFS | AUC 0.86/0.84/0.83 | TCGA val | Broad | High | Integration complexity | Full multi-omics |
| Lai 2022 | 36299455 | PTC | n=1815 | RF | LLNM | AUC 0.80, acc 0.74 | Test 20% | Clinical only | Med | Molecular add-on | Web tool+genes |
| Chun 2024 | 39333646 | cN0 PTC | 3213+533 ext | XGBoost | Paratracheal LNM | AUC 0.935/0.857/0.775 | External 533 | Features | High | Molecular features? | Add RET/BRAF |
| Feng 2025 | 40904800 | PTC | 799+50 ext | GBM radiomics | Lateral LNM | AUC 0.973/0.803/0.975 | External 50 | Leakage risk | High | Very high train AUC | Imaging+gene |
| Wang 2026 | 41378767 | cN0 PTC | n=961 | RF | Occult CLNM | RET fusion/BRAF risk; AUC 0.906/0.733 | Subset≤1cm | Test lower | High | RET fusion mechanism | Molecular web tool |
| Zhong 2025 | 40771372 | PTC | 294+111 ext | Radio+DL fusion | CLNM | Fusion SVM AUC 0.897/0.881 | External | Peri-tumoral | High | Gene add-on | Radio+gene fuse |
| Ren 2023 | 37574759 | PTMC | n=208 FNA | DL cytology | CLNM | AUC 0.8503 | None | Small | Med | Larger FNA set | Cytology DL |
| Liu 2025 | 40265473 | PTC | 157+807 qRT-PCR | RF 3-gene | LNM | AUC 0.992/0.911–0.953 | Multicenter | Overfit risk | High | Very high AUC suspect | 3-gene validate |
| Zhang 2024 | 38808852 | MTC | n=218 | Logistic+ML | LLNM (occult) | AUC 0.92; 0.91 occult | 5-fold | Subtype | Med | MTC-specific | MTC model |
| Huang 2023 | 36761483 | PTC | n=253 | SVM | LLNM | AUC 0.91, acc 90.8% | Test 98 | Single-center | Med | External | Multi-center |
| Liu 2024 (meta) | 39438906 | PTC (field) | 107 studies | PROBAST meta | LNM/CLNM/LLNM | c-index 0.762–0.829; LR 81% | — | Bias common | High | Methodology improvement | Standardized models |

---

## What Is Already Known

- **BRAF V600E is a consistent, but non-specific, LNM-associated alteration**; its combination with TERT amplifies risk (Soeratman 2024). This is clinically established, not novel.
- **Convergent hub genes recur across independent signatures**: MET and FN1 appear in Li 2025 (6-gene), Zhai 2019 (11 hub), and the ECM/module analyses; CLDN-family genes (CLDN1, CLDN10) appear in Zhang 2022 and Li 2025. This cross-study convergence is the most robust signal in the field and suggests a core "ECM–adhesion–MET" axis.
- **Multi-gene ML classifiers reach high AUCs on public data** but almost universally drop on external validation (Li 2025 6-gene conceptually; Yang 2025 0.80→0.718; Wang 2026 0.906→0.733; Liu 2025 RF 0.992→0.911). The meta-analysis (Liu 2024) confirms a ceiling c-index ≈0.76–0.83.
- **Immune microenvironment is an emerging, under-integrated axis**: tumor-infiltrating neutrophils (Yu 2025, AUC 0.892 classifier), Treg/CD8 imbalance (Wang 2026 MGST1 "immune-cold"), and RET-associated immune-cycle steps (Huang 2024) point to an immune–metabolic coupling in LNM.
- **Imaging DL/radiomics is now superior to humans for lateral LNM** (LLNM-Net AUC 0.944, beats experts 64.3%; Feng 2025; Zhong 2025 fusion 0.881 external) — but these are non-molecular and rarely fused with gene panels.
- **Metabolic reprogramming is mechanistically implicated**: MGST1 mitochondrial axis (Wang 2026), polyamine/glycolysis spatial niches (Li 2025 spatial), OxPhos downregulation (Ab Mutalib 2016), dedifferentiation metabolic signature (Ma 2019).

## What Remains Unclear

- **Causality vs correlation**: most signatures are associational; only a handful (MGST1/Toxoflavin, GABRB2, DIO2, APOE−/ABCA1-LXR, NAT8L/SVCT-2) have functional validation. The field lacks mechanism for the convergent MET/FN1 signal.
- **Subtype specificity is under-analyzed**: follicular-variant, tall-cell, and extent-of-BRAF-mutation effects on LNM are rarely stratified; male-specific signals (Liu 2021) need confirmation.
- **Central vs lateral vs occult (cN0) are often conflated**: the most clinically actionable gaps are occult CLNM (Wang 2026) and lateral LNM (Shen 2025) — but molecular markers for these specific endpoints are sparse.
- **External prospective validation is almost absent**: nearly every gene signature relies on TCGA/GEO reuse; the few with external cohorts (Chun 2024, Liu 2025, Zhong 2025) still retrovalidate.
- **Reproducibility of very-high AUCs is suspect**: Liu 2025 (0.992 train) and Feng 2025 (0.973 train) show classic leakage/overfit patterns; the meta-analysis flags PROBAST high-risk of bias in the majority.
- **Liquid biopsy (sEV, exosomal miRNA) promise remains unvalidated at scale** (Cao 2025 n=29; Chen 2022 combo 0.914 but small).

## Method/Data Limitations In The Field

- **Public-data reuse / batch effects**: TCGA+GEO (esp. GSE60542) appear in nearly every signature (Li 2025, Zhai 2019, Choi 2018, Lei 2023), inflating apparent performance.
- **Endpoint sparsity**: LNM is binary/pathology-driven; lateral vs central vs occult often not separated, weakening clinical claims.
- **Lack of external prospective validation**: rare (Chun 2024, Zhong 2025, Liu 2025 multicenter qRT-PCR are the exceptions).
- **Weak reproducibility / overfitting**: very high training AUCs (0.97–0.99) with sharp external drop; PROBAST bias common (Liu 2024 meta).
- **Missing wet-lab validation**: associational signatures dominate; functional mechanism for convergent genes (MET/FN1) thin.
- **Overcrowding of ML/DL imaging models**: 107 ML studies (Liu 2024) — incremental, single-center, imaging-only.

## Candidate Future Directions

| Direction | Rationale | Feasibility | Required Data | Validation Plan | Main Risk | Claim Boundary |
|---|---|---:|---|---|---|---|
| **D3. scRNA-defined stem-like (APOE−/MGST1+) metastatic subpopulation as biomarker + target** | APOE− (Xiao 2025) and MGST1 "terminal dediff" (Wang 2026) both mark a metastatic stem-like state — underexplored, mechanistically targetable (ABCA1-LXR, Toxoflavin) | High (public scRNA + TCGA; wet-lab feasible) | PTC scRNA-seq (public + in-house), TCGA, IHC/functional | In-house cohort IHC; knockdown/oe; compare to competitor 6-gene | Subpopulation may be rare; needs larger scRNA | "Markers of a metastatic-competent subpopulation," not standalone DX |
| D1. Immune-metabolic convergent gene panel (MET/FN1/COL8A2/MGST1 + neutrophil/Treg features) | Builds on cross-study convergent hub genes + emerging immune axis | High | TCGA/GEO, TIM deconvolution, external cohort | Benchmark vs Li 2025 & Yang 2025 on same external set | Crowded gene-signature space | "Risk stratification aid," not replacement for pathology |
| D2. Spatial multi-omics dissection of the peri-tumoral metastatic niche | Metabolic crosstalk (polyamine/glycolysis) drives LNM; few spatial studies in thyroid | Moderate (expensive platforms, limited public spatial data) | Fresh frozen PTC+LNM spatial metabolomics/transcriptomics | Zebrafish/xenograft; TCGA metabolite-gene confirmation | Cost & data scarcity | Mechanistic insight, not immediate clinical tool |
| D4. Radiogenomic fusion for occult LNM (imaging + parsimonious gene panel) | Imaging DL already beats experts; adding 3–6 genes could close the occult-LNM gap | Moderate (needs multicenter imaging + molecular) | Ultrasound/CT + gene panel (e.g., RET fusion/BRAF + MGST1) | Multicenter; compare to Wang 2026 / Zhong 2025 | Crowded; integration complexity | Decision-support for dissection extent |

### Rubric scoring (1–5 per criterion; 28–35 = strong)

| Direction | Novelty | Feasib. | Data | Valid. | Clin. | Rigor | Low-crowd | **Total** | Verdict |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| D3 (APOE−/MGST1+ subpopulation) | 5 | 4 | 5 | 4 | 4 | 4 | 4 | **30** | **Strong — prioritize** |
| D1 (immune-metabolic panel) | 3 | 5 | 5 | 4 | 5 | 3 | 2 | 27 | Feasible; sharpen novelty |
| D2 (spatial niche) | 5 | 2 | 2 | 3 | 4 | 4 | 5 | 25 | Feasible; data-limited backup |
| D4 (radiogenomic fusion) | 2 | 3 | 3 | 4 | 5 | 3 | 2 | 22 | Feasible; sharpen |

## Recommended Next Direction

**Lead with D3 — define and therapeutically target the APOE−/MGST1+ stem-like metastatic subpopulation — supported by a convergent immune-metabolic gene panel (D1) benchmarked against existing competitor signatures.**

Why this balances novelty, feasibility, and publishability:
- **Novelty (5):** APOE− (Xiao 2025) and MGST1 "terminal dedifferentiation" (Wang 2026) independently point to a metastatic-competent stem-like state that is essentially unexplored as a *combined* axis; it is distinct from the crowded pure gene-signature and pure-imaging lanes.
- **Feasibility (4):** Public PTC scRNA-seq and TCGA are available now; functional validation (knockdown/oe, IHC on in-house cohort) is standard.
- **Clinical relevance (4):** Directly addresses metastatic risk and offers a therapeutic angle (ABCA1-LXR activation, MGST1/Toxoflavin inhibition) — stronger than a statistical signature alone.
- **Claim boundary:** Position as "identification and targeting of a metastatic-competent subpopulation," not a standalone diagnostic; benchmark any gene panel against Li 2025 (6-gene) and Yang 2025 (3-gene) on a shared external cohort to prove added value.

First concrete next steps:
1. Re-analyze public PTC scRNA (incl. Xiao 2025 data) to co-localize APOE− and MGST1-high malignant cells and define a minimal marker set.
2. Deconvolve TCGA THCA immune landscape stratified by this subpopulation signature; test neutrophil/Treg enrichment (links to Yu 2025, Wang 2026).
3. Validate marker expression on an in-house IHC/RNA cohort with pathology-confirmed LNM (central/lateral/occult separated).
4. Functional assay (knockdown/oe + Transwell) for the MGST1–APOE axis; compare invasion phenotypes.
5. Benchmark a 4–6 gene panel (MGST1, APOE-surrogate, MET, FN1, COL8A2) vs competitor signatures on GSE60542 + in-house.

## Follow-Up Reading List

- **Wang 2026 (MGST1, PMID:42327722)** — strongest recent mechanistic + multi-omics LNM paper; anchor for the metabolic-immune axis.
- **Xiao 2025 (APOE−, PMID:39810624)** — defines the stem-like metastatic subpopulation; core to D3.
- **Li 2025 (6-gene competitor, PMID:40110574)** — direct benchmark target; shows MET/FN1 convergence.
- **Liu 2024 meta-analysis (PMID:39438906)** — field-level methodology reality check (PROBAST, c-index ceiling).
- **Shen 2025 (LLNM-Net, PMID:40750786)** — best-in-class imaging DL; model for radiogenomic fusion (D4).

## Reproducibility Notes

- Search date: 2026-07-19
- Databases: PubMed (paper-search-mcp `search_pubmed`)
- Query strings:
  1. `papillary thyroid carcinoma lymph node metastasis biomarker`
  2. `thyroid cancer lymph node metastasis gene expression signature TCGA`
  3. `thyroid cancer lymph node metastasis machine learning prediction model`
- Filters: `sort=relevance`, `max_results=15` per query
- Deduplication rule: union of 3 result sets; removed exact-PMID duplicates; removed 4 non-thyroid LNM records (PMID:36793937, 30950057, 39137488, 40620610) as out-of-scope.
- Screening rule: thyroid-relevant primary research + reviews + 1 meta-analysis included; off-topic cancers excluded.
- Files saved:
  - `literature_review_20260719_211838.md` (this report)
  - `search_results_latest.json` (raw 45-record payload from the 3 queries)
- Caveats: PMID:42327722 and PMID:41378767 carry 2026 publication dates — verify final journal status before citation. AUCs >0.97 in training (Liu 2025, Feng 2025) should be treated as overfit until externally reproduced.
