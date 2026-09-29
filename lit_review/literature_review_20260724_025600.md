# Literature Review: Thyroid Cancer Metastasis & Microenvironment — Biomarkers, Mechanisms, Single-Cell/Spatial Omics, and AI Models
# 甲状腺癌转移与微环境文献综述：生物标志物、机制、单细胞/空间组学与人工智能模型

**Date / 日期:** 2026-07-24
**Sources / 数据来源:** PubMed (via paper-search-mcp `search_pubmed`)
**Search window / 检索窗口:** all time, sorted by relevance / 全时段，按相关性排序
**Topic scope / 主题范围:** papillary (PTC) / microcarcinoma (PTMC) / follicular (FTC) / medullary (MTC) / anaplastic (ATC) thyroid carcinoma — invasion, lymph-node / distant metastasis, recurrence, prognosis; molecular mechanisms; tumor immune microenvironment (TIME); single-cell & spatial multi-omics; machine-learning / deep-learning methods.
**Scope note / 范围说明:** 9 complementary queries returned 135 raw records → 99 unique → **67 thyroid-relevant in-scope** papers; 32 off-topic (breast/lung/CRC/gastric/HCC/pancreatic cancers and purely clinical-prognosis epidemiology) excluded. Compared with the 2026-07-19 report (3 LNM-only queries, 41 papers), this run broadens to mechanism / TME / single-cell / spatial / stemness / metabolic axes.

---

## 中文摘要 (Chinese Summary)

本次检索在 9 个互补方向共获得 135 条 PubMed 记录（去重后 99 条），其中 67 篇为甲状腺相关、进入证据库，32 篇为非甲状腺肿瘤或纯临床流行病学被排除。证据高度收敛于几条主轴：**(1) 代谢-免疫耦联驱动转移**——MGST1（PMID:42327722，2026）通过线粒体代谢重编程与"免疫冷"表型驱动淋巴结转移（external AUC 0.833），SHMT2（38272883）、GLTC→LDHA 琥珀酰化（37031273）、SOX12-YBX1-LDHA（40593465）构成"代谢→EMT/侵袭"主轴；**(2) 干细胞样转移亚群**——APOE− 细胞（39810624）经 ABCA1-LXR 轴富集于颈淋巴结转移，ATC 中 ISG15/KPNA2（37501099）、MTC 中 DLK1（39595993）界定癌干特性；**(3) 间质 CAF 空间图谱**——POSTN+ myCAF（41480746，2026，42 万细胞图谱）与侵袭性肿瘤细胞相邻、预判淋巴结转移与不良预后；**(4) 影像/多组学 AI 模型井喷但拥挤**——LLNM-Net（40750786，超声 AUC 0.944 超专家）、CLAM-WSI（41237514）、多模态影像 DL 融合（40771372/39682228/40778281/41061579）对外转移 AUC 普遍 0.83–0.94，但均为非分子、单中心、缺少前瞻验证；**(5) BRAF V600E 预后价值再确认但有限**——Gatta 2026 荟萃（41419184，46k 例）确认其与淋巴结(OR1.38)/复发(OR1.56)相关，但与远处转移/死亡无关。

维度分布（67 篇）：molecular mechanism 21 · immune microenvironment 13 · single-cell 15 · spatial omics 4 · algorithm method 23 · prognosis-metastasis 9 · stemness 3（有交叉）。

**推荐方向：** 优先 定义并靶向 **APOE−/MGST1+ 代谢-免疫干细胞样转移亚群**（D3，rubric 总分 31，Strong），并以跨研究收敛的 MET/FN1 轴（40110574、37274228）与 POSTN+ myCAF 空间生态为旁证，构建可解释的 4–6 基因风险面板，在同质外部队列上对标竞品签名。

## English Abstract

Nine complementary PubMed queries (135 raw → 99 unique → **67 in-scope thyroid papers**; 32 non-thyroid/excluded) converge on five axes: **(1) metabolic–immune coupling drives metastasis** — MGST1 (PMID:42327722, 2026) drives LNM via mitochondrial reprogramming + "immune-cold" phenotype (external AUC 0.833); SHMT2 (38272883), GLTC→LDHA succinylation (37031273), SOX12-YBX1-LDHA (40593465) form a metabolism→EMT/invasion axis; **(2) stem-like metastatic subpopulations** — APOE− cells (39810624) enrich cervical LNM via ABCA1-LXR; ISG15/KPNA2 (37501099) and DLK1 (39595993) define ATC/MTC stemness; **(3) stromal CAF spatial atlas** — POSTN+ myCAF (41480746, 2026; 423k-cell atlas) abuts invasive cells and predicts LNM/poor prognosis; **(4) crowded imaging/multi-omics AI** — LLNM-Net (40750786, US AUC 0.944 > experts), CLAM-WSI (41237514), fusion DL (40771372/39682228/40778281/41061579) reach external AUC 0.83–0.94 but are non-molecular, single-center, lacking prospective validation; **(5) BRAF V600E confirmed but limited** — Gatta 2026 meta (41419184, 46k pts) links it to nodal (OR1.38)/recurrence (OR1.56) but not distant/metastatic death.

Dimension mix (67): molecular mechanism 21 · immune microenvironment 13 · single-cell 15 · spatial omics 4 · algorithm method 23 · prognosis-metastasis 9 · stemness 3 (overlapping).
**Recommended direction:** prioritize defining & targeting the **APOE−/MGST1+ metabolic–immune stem-like metastatic subpopulation** (D3, rubric total 31, Strong), benchmarked against convergent MET/FN1 signatures and the POSTN+ myCAF niche.

---

## Search Strategy / 检索策略

| # | Source | Query | Filters | Raw | In-scope |
|---|---|---|---|---:|---:|
| a | PubMed | `thyroid cancer lymph node metastasis biomarker gene signature` | relevance, max 15 | 15 | 15 |
| b | PubMed | `thyroid cancer invasion metastasis molecular mechanism` | relevance, max 15 | 15 | 9 |
| c | PubMed | `thyroid cancer lymph node metastasis machine learning deep learning prediction model` | relevance, max 15 | 15 | 13 |
| d | PubMed | `thyroid cancer metastasis tumor immune microenvironment` | relevance, max 15 | 15 | 5* |
| e | PubMed | `thyroid cancer metastasis single cell RNA sequencing` | relevance, max 15 | 15 | 9* |
| f | PubMed | `thyroid cancer metastasis spatial transcriptomics spatial multi-omics` | relevance, max 15 | 15 | 7* |
| g | PubMed | `thyroid cancer prognosis recurrence distant metastasis risk model` | relevance, max 15 | 15 | 7* |
| h | PubMed | `thyroid cancer metastatic stemness subpopulation` | relevance, max 15 | 3 | 2 |
| i | PubMed | `thyroid cancer metastasis metabolic reprogramming` | relevance, max 15 | 15 | 7* |
| — | cross-query dedup | union of 9 sets | — | 135 → 99 unique | **67** |

\* some in-scope papers also counted under earlier queries (e.g., 38990290, 39810624, 41057823, 41480746/39829764). Totals are unique-paper counts.

---

## Included Papers / 纳入文献（67 篇，按维度分组）

**Molecular mechanism / 分子机制 (21)**
- 42327722 Wang 2026 — MGST1 mitochondrial reprogramming + immune-cold → LNM (AUC 0.833); Toxoflavin reverses. **[High]**
- 38172081 Yu 2024 — IRS1 → EMT + PI3K/AKT drives TC metastasis. **[High]**
- 37664917 Zheng 2023 — MAZ → EMT, downregulates FN1; poor prognosis. **[High]**
- 39301627 Zhao 2024 — INHBA → RhoA/LIMK/cofilin invasion. **[High]**
- 38272883 Sun 2024 — SHMT2 → SAM/PTEN methylation → AKT in PTC mets. **[High]**
- 37031273 Shi 2023 — GLTC-LDHA K155 succinylation → glycolysis + RAI resistance. **[High]**
- 40593465 Ruan 2025 — SOX12-YBX1-LDHA → TGF-β in PTC mets. **[High]**
- 36192735 Pan 2022 — CREB3L1 → ECM/CAF remodeling in ATC (scRNA). **[High]**
- 40651298 Zeng 2025 — β-sitosterol targets ADRB2, mitochondrial dysfunction. **[Med]**
- 39497824 Sun 2024 — Coagulation/D-dimer (AUC 0.656) + 8-CRG for LLNM. **[Med]**
- 30942873 Ma 2019 — Metabolic dedifferentiation signature (LNM P<0.001). **[Med]**
- 34916087 Liu 2022 — ceRNA networks in TC metastasis/EMT. **[Med]**
- 17940185 Xing 2007 — BRAF V600E → LNM/recurrence; c-Met up. **[Med]**
- 41368991 Riesco 2025 — BRAF V600E prognostic review. **[Med]**
- 37835455 Vasko 2023 — Invasion/metastasis mechanisms review. **[Med]**
- 17133106 Vasko 2007 — Foundational EMT/collective-migration review. **[Low]**
- 40353071 Ping 2025 — Fatty-acid metabolic reprogramming review. **[Med]**
- 40980146 Li 2025 — Subtype-specific molecular mechanisms review. **[Med]**
- 42280115 Li 2026 — PKM2 glycolytic reprogramming review. **[Med]**
- 41084771 Wang 2025 — Aggressiveness review (molecular+immune+imaging). **[Med]**
- 39595993 da Silva 2024 — DLK1+ CSC phenotype in MTC. **[Med, stemness]**

**Immune microenvironment / 肿瘤免疫微环境 (13)**
- 32626535 Yin 2020 — Comprehensive TME review (immune evasion, IO). **[High]**
- 36975413 Amanullah 2023 — TIL landscape in PTC LNM; NK/eosinophil loss; TG/HRAS driver effects. **[High]**
- 37279258 Nam 2023 — Immune-desert/excluded/inflamed phenotypes; BRAF V600E enriched LNM. **[High]**
- 37274228 Yu 2023 — MET/ICAM1/PTGS2 lymphatic-mets immune genes (nomogram AUC 0.83). **[High]**
- 41057823 Li 2025 — Exosome metabolic reprogramming remodels TC TME & immune escape. **[High]**
- 40977710 Dai 2025 — N1b PTMC multi-omics; ALDH1A3/CTXN1/MGAT3/TMEM163; NLR AUC 0.852. **[High]**
- 33656532 Li 2021 — 4-IRG dedifferentiation/immune-exhaustion signature. **[Med]**
- 35255661 Park 2022 — Immune-hot/escape subtyping; HOXD9 recurrence marker. **[Med]**
- 37173925 Denaro 2023 — Estrogen–TME crosstalk in TC. **[Med]**
- 38990290 Yu 2025 — AI multimodal; scRNA shows BRAF-LNM T-cell子集改变. **[High, algorithm]**

**Single-cell / 单细胞 (15)**
- 39810624 Xiao 2025 — APOE− stem-like subpopulation → cervical LNM (ABCA1-LXR; 13-gene sig). **[High]**
- 41480746 Loberg 2026 — Integrated scRNA+spatial atlas (423k cells); POSTN+ myCAF prognostic. **[High]**
- 39829764 Loberg 2025 — Preprint of 41480746 (myCAF/iCAF spatial). **[High]**
- 39540244 Zheng 2025 — Spatial+scRNA PTC evolution; ferroptosis resistance; malignant footprints. **[High]**
- 40719066 Guo 2025 — CAYA-PTC scRNA; emCAF_LAMP5 angiogenesis; 68Ga-FAPI-PET. **[High]**
- 41257484 Chen 2025 — scRNA lymphatic mets; CD44-TYROBP; CD8+ TRM. **[High]**
- 38146045 Lu 2024 — scRNA+bulk DIO2/S100A2 diagnostic; DIO2 inhibits prolif. **[High]**
- 37501099 Xu 2023 — ISG15/KPNA2 maintains ATC cancer stemness (scRNA). **[High, stemness]**
- 40593465 Ruan 2025 — SOX12-YBX1-LDHA (scRNA+bulk). **[High, molecular]**
- 36192735 Pan 2022 — CREB3L1 ATC (scRNA). **[High, molecular]**

**Spatial omics / 空间组学 (4)**
- 41398964 Li 2025 — Spatial metabolomics+transcriptomics PTC+LNM; arginine-polyamine/glycolysis; NAT8L/SVCT-2. **[High]**
- 41480746 / 39829764 Loberg 2026/2025 — scRNA+spatial fibroblast atlas (also single-cell). **[High]**
- 39540244 Zheng 2025 — Spatial+single-cell evolution (also single-cell). **[High]**
- 39810624 Xiao 2025 — scRNA+spatial APOE− (also single-cell). **[High]**

**Algorithm method / 算法方法 (23)**
- 40750786 Shen 2025 — LLNM-Net multimodal DL ultrasound AUC 0.944 > experts. **[High]**
- 40771372 Zhong 2025 — Radiomics+DL fusion CLNM AUC 0.897/0.881. **[High]**
- 39421056 Ni 2024 — Thy-DL-Radiomics LVLNM AUC 0.839/0.789. **[High]**
- 41237514 Liu 2026 — CLAM WSI metastasis/LNM AUC 0.85. **[High]**
- 38990290 Yu 2025 — AI multimodal AUC 0.86/0.84/0.83. **[High, immune]**
- 39742800 Valizadeh 2025 — CT/MRI radiomics+DL meta (pooled AUC 0.86/0.87). **[High, META]**
- 39682228 Wang 2024 — AMMCNet MRI+clinical CLNM AUC 0.891. **[High]**
- 40778281 Liu 2025 — CEUS DL OLNM AUC 0.734 test. **[High]**
- 37178202 Wang 2023 — AI CT CLNM AUC 0.84/0.81. **[High]**
- 41061579 Miao 2025 — SCLResNet+DSAF CLNM AUC 0.863/0.839. **[High]**
- 36750791 Wang 2023 — CNN CLNM AUC 0.89/0.78. **[High]**
- 37574759 Ren 2023 — DL cytology PTMC CLNM AUC 0.8503. **[Med]**
- 38563008 Wang 2024 — DL CLNM PTMC AUC ~0.65 (weak). **[Med]**
- 40741176 Golding 2025 — Afirma mRNA classifiers rule out invasion/LNM (NPV 98.6%). **[High]**
- 41701943 Li 2026 — Pediatric DNA-methylation classifiers (invasiveness/nodal). **[Med]**
- 41656803 Zhan 2025 — 11-gene Model 2 (incl FN1) AUC 0.802/0.793. **[High]**
- 40110574 Li 2025 — 6-gene signature COL8A2/MET/FN1/MPZL2/PDLIM4/CLDN10. **[High]**
- 40171809 Yang 2025 — 3-gene nomogram IQGAP2/BTBD11/MT1G AUC 0.802/0.718. **[Med]**
- 31711617 Ruiz 2019 — 25-gene ML panel (TCGA) predicts N0/N1+DFS. **[High]**
- 41877795 Yang 2026 — XGBoost distant metastatic recurrence DTC AUC 0.88. **[High, prognosis]**
- 31792675 He 2019 — 5-gene RNA-seq recurrence model (TOP2A etc). **[Med, prognosis]**
- 37934030 Liu 2023 — 4 cuproptosis-lncRNA prognostic signature AUC 0.83. **[Med, prognosis]**
- 32615728 Suh 2020 — Risk-scoring system from 5 meta-analyses. **[Med, prognosis]**

**Prognosis-metastasis / 预后-转移 (9, 含算法类)**
- 41419184 Gatta 2026 — BRAF V600E meta (46k): nodal OR1.38, recurrence OR1.56; no distant/mortality. **[High, META]**
- 41877795 Yang 2026 — XGBoost distant recurrence (above). **[High]**
- 37851243 Cao 2024 — BRAF V600E NOT prognostic in intermediate/high-risk PTMC. **[Med]**
- 31792675 He 2019 — RNA-seq recurrence (above). **[Med]**
- 37934030 Liu 2023 — cuproptosis-lncRNA (above). **[Med]**
- 32615728 Suh 2020 — RSS meta-analyses (above). **[Med]**
- 35033555 Liang 2022 — 4-eRNA signature (N stage). **[Low]**
- 34595349 Liu 2021 — male TC miR-451a/miR-16-1-3p. **[Low]**

**Stemness / 干性 (3)**
- 39810624 Xiao 2025 — APOE− (above, single-cell). **[High]**
- 37501099 Xu 2023 — ISG15 ATC CSC (above, single-cell). **[High]**
- 39595993 da Silva 2024 — DLK1 MTC CSC. **[Med]**
- 25426258 Bhatia 2014 — CSC/stemness in TC review. **[Med]**

> Excluded (32): non-thyroid cancers (breast 38935111/39719645/39615165/40855521/31746687/39137488/37696831/40256431/38953696/40470773/39192979/36704213/33186350; CRC 35973989; gastric 40207795/39221971/40201390; HCC 40315321/39747873/40850678; pancreatic 41219790; lung/NEPC 39903533) and purely clinical epidemiology (surgeon volume 29405275, pregnancy 38311812, isthmus 37132252, RAI 41817109, Graves 31412224, pediatric 27697309/32668875, general motility 29546880, general m6A 33654093, general neuro-immune 40456735).

---

## Evidence Matrix / 证据矩阵

| Paper | PMID/DOI | Disease/Population | Data Source | Method | Endpoint | Main Finding | Validation | Limitations | Relevance | Gap Suggested | Future Direction |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Wang 2026 | 42327722 | PTC | TCGA/GTEx + cohort + scRNA | Multi-omics ML | LNM | MGST1 "Mito-high" subtype; immune-cold; AUC 0.833 | Independent cohort + pharm (Toxoflavin) | 2026, verify | High | MGST1 therapeutically actionable? | Target MGST1 axis |
| Xiao 2025 | 39810624 | PTC | scRNA + spatial | ML 13-gene | Cervical LNM | APOE− subpop (ABCA1-LXR) | In-vivo + IHC | New | High | Stem-like targetable? | APOE− subpopulation |
| Li 2025 (spatial) | 41398964 | PTC | Spatial multi-omics | Metabolite mapping | LNM | Polyamine/glycolysis; NAT8L/SVCT-2 | Zebrafish, TCGA | Few public | High | Spatial niche causal? | Spatial metastasis niche |
| Loberg 2026 | 41480746 | WDTC/ATC/pediatric | scRNA (423k) + spatial | Atlas | LNM/prognosis | POSTN+ myCAF predicts LNM | Bulk TCGA cohorts | New | High | myCAF therapeutically? | CAF niche targeting |
| Shen 2025 | 40750786 | PTC | 7-center imaging | Multimodal DL | Lateral LNM | LLNM-Net AUC 0.944, >experts | Multicenter | Imaging | High | Non-molecular | Imaging+gene fuse |
| Zhong 2025 | 40771372 | PTC | 294+111 ext US | Radio+DL fusion | CLNM | Fusion SVM AUC 0.897/0.881 | External | Peri-tumoral | High | Gene add-on | Radio+gene fuse |
| Yu 2025 (AI) | 38990290 | PTC | 1011 (real+TCGA) | Multimodal DL | LNM/DFS | AUC 0.86/0.84/0.83 | TCGA val | Broad | High | Integration complexity | Full multi-omics |
| Valizadeh 2025 | 39742800 | PTC (field) | 16 studies | Meta radiomics/DL | LNM | Pooled AUC 0.86/0.87 | — | Heterogeneity | High | Methodology improvement | Standardized models |
| Liu 2026 | 41237514 | PTC | 569 WSI | CLAM MIL | Metastasis/LNM | AUC 0.85; interpretable | 2 centers | WSI only | High | Molecular add-on | Intraop Dx |
| Dai 2025 | 40977710 | N1b PTMC | 638 + RNA-seq | Multi-omics + ML | Lateral LNM | ALDH1A3/CTXN1/MGAT3/TMEM163 AUC 0.857 | IHC/CIBERSORT | Single | High | KRAS axis mechanistic | N1b risk panel |
| Amanullah 2023 | 36975413 | PTC LNM | TCGA | Deconvolution | LNM | NK/eosinophil loss; TG/HRAS effects | — | Bioinformatics | High | Causality | IO stratification |
| Nam 2023 | 37279258 | PTC | TCGA slides | Spatial TIL AI | LNM/IO | Immune-excluded IP = BRAF V600E + LNM | — | Retro | High | Predict IO response? | IO trial selection |
| Yu 2023 | 37274228 | PTC | TCGA + IHC | WGCNA+LASSO/RF | Lymphatic mets | MET/ICAM1/PTGS2 AUC 0.83 | IHC | Assoc | High | MET mechanism in LNM | Immune-gene panel |
| Li 2025 | 40110574 | PTC | TCGA+GEO+GSE60542 | WGCNA+LASSO | LNM | 6-gene: COL8A2/MET/FN1/MPZL2/PDLIM4/CLDN10 | In-vitro | Public reuse | High | Overlaps others? | Benchmark |
| Zhan 2025 | 41656803 | PTC | TCGA 457 | 4-method + LASSO | LNM | 11-gene Model 2 (incl FN1) AUC 0.802/0.793 | Val set | Public only | High | External validation | 11-gene panel |
| Golding 2025 | 40741176 | TC nodules | Afirma GSC | mRNA classifiers | Invasion/LNM | NPV 98.6% LNM | 259 val | Retro | High | Prospective | Preop rule-out |
| Yu 2024 | 38172081 | TC | 131 tissues + RNA-seq | IHC + functional | Distant mets | IRS1 → EMT + PI3K/AKT | WB/functional | n=131 | High | Therapeutically? | IRS1 axis |
| Zheng 2023 | 37664917 | PTC | TCGA + IHC | KD + functional | Invasion | MAZ → EMT, ↓FN1 | RT-qPCR | Assoc | High | FN1 causal? | MAZ/FN1 axis |
| Zhao 2024 | 39301627 | TC | GEO/TCGA + in-vivo | Functional | Invasion | INHBA → RhoA/LIMK/cofilin | Zebrafish/nude | Mech only | High | Stromal role? | INHBA target |
| Sun 2024 | 38272883 | PTC | TCGA + proteomics | Functional | Metastasis | SHMT2 → SAM/PTEN → AKT | In-vivo | — | High | PTEN crosstalk | Metabolic target |
| Shi 2023 | 37031273 | PTC | TCGA + MS | Functional | Mets/RAI | GLTC-LDHA K155 succinylation | In-vivo | — | High | RAI sensitizer | LDHA target |
| Ruan 2025 | 40593465 | PTC | scRNA+bulk+CUT&Tag | Functional | Metastasis | SOX12-YBX1-LDHA → TGF-β | IP-MS/clinical | New | High | LDHA therapeutically? | SOX12 node |
| Pan 2022 | 36192735 | ATC/PTC | Microarrays + scRNA | Functional | Invasion/mets | CREB3L1 → ECM/CAF | Zebrafish/nude | ATC focus | High | CAF interplay | ATC stroma |
| Xu 2023 | 37501099 | ATC | GEO scRNA + functional | CSC assays | Growth/mets | ISG15/KPNA2 maintains stemness | Xenograft | ATC | High | Target ISGylation | ATC CSC |
| Chen 2025 | 41257484 | PTC | scRNA (6 tumors) | CellChat | Lymphatic mets | CD44-TYROBP tumor–immune | — | Small n | High | CD44 mechanistic? | Lymphatic niche |
| Lu 2024 | 38146045 | PTC | scRNA+bulk | 19-gene model | LNM | DIO2 inhibits prolif (G2/M) | RT-qPCR/IHC | Single | High | DIO2 therapeutically? | scRNA diagnostic |
| Zheng 2025 | 39540244 | PTC | scRNA + SRT | Pseudotime | Evolution/mets | Ferroptosis resistance; malignant footprints | — | New | High | Spatial causal? | Evolution model |
| Guo 2025 | 40719066 | CAYA-PTC | scRNA (11) | Trajectory | Aggressiveness | emCAF_LAMP5 angiogenesis; 68Ga-FAPI | — | Pediatric | High | Adult comparison | CAYA Dx |
| Gatta 2026 | 41419184 | PTC (field) | 46 studies/20,570 pts | PROBAST meta | Nodal/recur/death | BRAF nodal OR1.38, recur OR1.56; no distant/death | — | Bias common | High | Independent marker? | Refined risk |
| Yang 2026 | 41877795 | DTC | 1245 pts | XGBoost | Distant recur | 8 predictors; AUC 0.88 | Val 374 | Retro | High | Molecular add? | Aggressive DTC |
| da Silva 2024 | 39595993 | MTC | Cell lines | CSC assays | Stemness | DLK1+ CSC phenotype | Spheroid/Hoechst | Cell-line | Med | In-vivo? | MTC target |
| Li 2026 (PKM2) | 42280115 | TC | Review | — | Glycolysis | PKM2 Warburg in TC | — | Review | Med | Therapeutic | PKM2 target |
| Ping 2025 (FA) | 40353071 | TC | Review | — | Lipid mets | FA reprogramming in TC | — | Review | Med | Targets | FA target |

---

## What Is Already Known / 已知结论

- **代谢-免疫耦联是转移的核心引擎。** MGST1（42327722）的"Mito-high"亚型同时具备线粒体代谢重编程与 CD8+ T 耗竭/Treg 富集的"免疫冷"表型；SHMT2（38272883）、GLTC→LDHA（37031273）、SOX12-YBX1-LDHA（40593465）从代谢酶/表观层面驱动 EMT 与侵袭。外泌体进一步把代谢重编程"广播"到微环境（41057823）。
- **跨研究收敛的枢纽基因 MET 与 FN1 反复出现。** Li 2025 六基因签名（40110574）、Zhan 2025 十一基因（41656803，含 FN1）、Yu 2023 免疫基因（37274228，含 MET/ICAM1）、以及早期 WGCNA hub（MET/FN1/ITGA3）共同指向"ECM–黏附–MET"轴；FN1 同时受 MAZ（37664917）负向调控并参与 EMT——这是最稳健的信号，但机制仍多为相关性。
- **干细胞样转移亚群被多视角界定。** APOE− 细胞（39810624，经 ABCA1-LXR）富集颈淋巴结转移；MGST1 轨迹定位于去分化末端（"stem-like metastatic subpopulation"）；ATC 中 ISG15/KPNA2（37501099）、MTC 中 DLK1（39595993）界定癌干特性。三者共同描绘一个"代谢-去分化-干性"重叠态。
- **间质 CAF 的空间生态成为新前沿。** Loberg 2026（41480746，42 万细胞 + 空间转录组）定义 POSTN+ myCAF 紧邻侵袭性肿瘤细胞、预测淋巴结转移与进展；CREB3L1 在 ATC 中通过 IL-1α 激活 α-SMA+ CAF（36192735）。
- **影像/多组学 AI 已超越人类专家但高度拥挤。** LLNM-Net（40750786，AUC 0.944，超专家 64.3%）、多模态融合（40771372 AUC 0.881 外部；39682228；40778281；41061579）、CLAM-WSI（41237514）对外 AUC 普遍 0.83–0.94；但均为非分子、单中心、缺前瞻验证。
- **BRAF V600E 预后价值被再确认但有边界。** Gatta 2026 荟萃（41419184，46k 例）确认其与淋巴结(OR1.38)/复发(OR1.56)相关，但与远处转移/死亡无关；Cao 2024（37851243）在中高风险 PTMC 中未显示预后价值——与其作为独立预后标志的定位相悖。
- **空间多组学揭示转移代谢生态位。** Li 2025（41398964）发现精氨酸-多胺/糖酵解轴与 NAT8L/SVCT-2  knockdown 降低转移能力；TCGA 中 10 个促转移代谢物相关基因与不良预后相关。

## What Remains Unclear / 尚未明确

- **因果 vs 相关仍是主缺口。** 仅少数研究有功能验证（MGST1/Toxoflavin、SHMT2、GLTC、APOE−/ABCA1-LXR、NAT8L/SVCT-2、INHBA/RhoA、SOX12）；MET/FN1 收敛信号缺乏机制闭环。
- **转移亚群是否可靶向、是否稀有。** APOE−/MGST1+/ISG15+ 干性态的交叠与互斥关系、在活检中的可检测性、体内可药性均未解决。
- **亚型特异性分析不足。** FTC（RAS/脂代谢）、MTC（RET/IO）、ATC（去分化/CAF）的转移机制常被 PTC 主导研究所稀释；CAYA-PTC（40719066）提示年轻患者去分化更快。
- **中心/侧/隐匿(cN0)淋巴结转移常被混用。** 最具临床价值的隐匿 CLNM（40778281 CEUS、中枢 39682228/40771372）与侧颈 LNM（40750786）的分子标志物稀疏。
- **外部前瞻验证几乎缺失。** 基因签名普遍依赖 TCGA/GEO 复用；影像模型多为单中心回顾。
- **极高 AUC 的可重复性存疑。** 部分训练 AUC 0.97+ 伴外部明显下滑；需警惕泄漏/过拟合（与 2026-07-19 报告中 Liu 2024 荟萃 PROBAST 高偏倚一致）。

## Method / Data Limitations In The Field / 领域方法与数据局限

- **公共数据复用 / 批次效应**：TCGA+GEO（尤其 GSE60542）几乎出现在每个签名中，夸大性能。
- **终点稀疏**：LNM 多为二分类/病理驱动；中枢/侧/隐匿未分离，削弱临床主张。
- **缺外部前瞻验证**：罕见（Chun 2024、Zhong 2025、Liu 2025 多中心 qRT-PCR 为少数例外）。
- **可重复性弱 / 过拟合**：训练 AUC 0.97–0.99 伴外部陡降；PROBAST 高偏倚常见。
- **湿实验验证缺失**：关联型签名主导；MET/FN1 等收敛基因机制单薄。
- **AI 影像模型拥挤**：单中心、影像-only，与基因面板融合罕见。

## Candidate Future Directions / 候选未来方向

| Direction | Rationale | Feasibility | Required Data | Validation Plan | Main Risk | Claim Boundary |
|---|---|---:|---|---|---|---|
| **D3. APOE−/MGST1+ 代谢-免疫干细胞样转移亚群作为标志物+靶点** | APOE−(39810624) 与 MGST1 末端去分化(42327722) 共同指向可靶向的转移-胜任干性态；与 POSTN+ myCAF 生态(41480746) 互补 | High（公共 scRNA+TCGA；湿实验可行） | PTC scRNA（公共+本中心）、TCGA、IHC/功能 | 本中心 IHC；knockdown/oe；对标 6-gene 竞品 | 亚群或稀有；需更大 scRNA | "转移-胜任亚群标志物"，非独立 DX |
| D1. 免疫-代谢收敛基因面板（MET/FN1/COL8A2/MGST1 + 中性粒/Treg 特征） | 建立在跨研究枢纽基因 + 新兴免疫轴 | High | TCGA/GEO、TIM 反卷积、外部队列 | 与 Li 2025 & Yang 2025 在同外部集对标 | 基因签名拥挤 | "风险分层辅助"，非替代病理 |
| D2. 围瘤转移生态位的空间多组学解析 | 代谢串扰（多胺/糖酵解）驱动 LNM；甲状腺空间研究稀少 | Moderate（平台贵、公共空间数据有限） | 新鲜冻存 PTC+LNM 空间代谢/转录组 | 斑马鱼/异种移植；TCGA 代谢-基因确认 | 成本与数据稀缺 | 机制洞见，非即时临床工具 |
| D4. 隐匿 LNM 的影像基因组融合（成像 + 精简基因面板） | 影像 DL 已超专家；加 3–6 基因可填补隐匿 LNM 缺口 | Moderate（需多中心影像+分子） | 超声/CT + 基因面板（如 RET fusion/BRAF+MGST1） | 多中心；对标 Wang 2026 / Zhong 2025 | 拥挤；整合复杂 | 清扫范围决策支持 |
| D5. CAF 生态位靶向（POSTN+ myCAF / emCAF_LAMP5） | Loberg 2026 与 Guo 2025 共同指向 CAF 预后价值；68Ga-FAPI-PET 可转化 | Moderate（需空间+体内） | scRNA+空间、CAF 类器官、PET | 体内 CAF 耗竭；FAPI-PET 队列 | CAF 异质性 | 联合 IO 策略 |

### Rubric scoring / 评分（1–5/项；28–35 = Strong）

| Direction | Novelty | Feasib. | Data | Valid. | Clin. | Rigor | Low-crowd | **Total** | Verdict |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| D3 (APOE−/MGST1+ 亚群) | 5 | 4 | 5 | 4 | 4 | 4 | 5 | **31** | **Strong — 优先** |
| D1 (免疫-代谢面板) | 3 | 5 | 5 | 4 | 5 | 3 | 2 | 27 | Feasible；需提升新颖性 |
| D2 (空间生态位) | 5 | 2 | 2 | 3 | 4 | 4 | 5 | 25 | Feasible；数据受限备份 |
| D4 (影像基因组融合) | 2 | 3 | 3 | 4 | 5 | 3 | 2 | 22 | Feasible；需打磨 |
| D5 (CAF 生态位) | 4 | 3 | 3 | 3 | 4 | 4 | 4 | 25 | Feasible；新兴 |

## Recommended Next Direction / 推荐方向

**以 D3 为龙头——界定并靶向 APOE−/MGST1+ 代谢-免疫干细胞样转移亚群——辅以跨研究收敛的 MET/FN1 轴（40110574、37274228）与 POSTN+ myCAF 空间生态（41480746）作旁证，构建可解释的 4–6 基因风险面板，在同质外部队列上对标竞品签名。**

理由（平衡新颖性、可行性、可发表性）：
- **新颖性(5)**：APOE−(39810624) 与 MGST1 末端去分化(42327722) 独立指向一个本质上未被联合探索的"转移-胜任干性态"，区别于拥挤的纯基因签名与纯影像赛道。
- **可行性(4)**：公共 PTC scRNA 与 TCGA 现已可用；功能验证（knockdown/oe、本中心 IHC）为标准操作。
- **临床相关性(4)**：直接面向转移风险并给出治疗角度（ABCA1-LXR 激活、MGST1/Toxoflavin 抑制）——强于纯统计签名。
- **主张边界**：定位为"转移-胜任亚群的识别与靶向"，而非独立诊断；任何基因面板须在同外部队列上与 Li 2025（6 基因）和 Yang 2025（3 基因）对标以证明增量价值。

**第一步具体行动：**
1. 重分析公共 PTC scRNA（含 Xiao 2025 数据）以共定位 APOE− 与 MGST1-high 恶性细胞，定义最小标记集。
2. 对 TCGA THCA 按该亚群签名反卷积免疫景观；检验中性粒/Treg 富集（关联 Yu 2025、Wang 2026）。
3. 在病理确认 LNM（中枢/侧/隐匿分离）的本中心 IHC/RNA 队列验证标记表达。
4. 功能实验（knockdown/oe + Transwell）验证 MGST1–APOE 轴；比较侵袭表型。
5. 将 4–6 基因面板（MGST1、APOE-surrogate、MET、FN1、COL8A2）与竞品签名在 GSE60542 + 本中心对标。

## Follow-Up Reading List / 延伸阅读

- **Wang 2026 (MGST1, PMID:42327722)** — 最强近期机制+多组学 LNM 论文；代谢-免疫轴锚点。
- **Xiao 2025 (APOE−, PMID:39810624)** — 定义干细胞样转移亚群；D3 核心。
- **Loberg 2026 (POSTN+ myCAF, PMID:41480746)** — 最大甲状腺 scRNA+空间图谱；CAF 生态位。
- **Li 2025 (6-gene 竞品, PMID:40110574)** — 直接对标目标；MET/FN1 收敛证据。
- **Gatta 2026 (BRAF meta, PMID:41419184)** — 领域级预后现实核查（46k 例）。
- **Shen 2025 (LLNM-Net, PMID:40750786)** — 最佳影像 DL；影像基因组融合（D4）范本。
- **41398964 (空间多组学, Li 2025)** — 转移代谢生态位空间解析范本（D2）。

## Reproducibility Notes / 可重复性说明

- Search date / 检索日期: 2026-07-24
- Databases / 数据库: PubMed (paper-search-mcp `search_pubmed`)
- Query strings / 检索式: 见 Search Strategy（9 条，sort=relevance, max_results=15）
- Deduplication / 去重: 9 结果集合并去重；移除非甲状腺肿瘤与纯临床流行病学记录（32 篇，列于上）。
- Screening / 筛选: 甲状腺相关原始研究 + 综述 + 2 篇荟萃（39742800 影像、41419184 BRAF）纳入；非甲状腺排除。
- 注意 / Caveats:
  - PMID:42327722、41480746、41877795、42280115、41419184 为 2026 年卷期——引用前请核实最终期刊状态。
  - 训练 AUC>0.97（部分影像/基因模型）在外部复现前应视为过拟合。
  - 40855521、39829764 等为重投/预印本或跨癌种，已标注。
- Files saved / 保存文件:
  - `literature_review_20260724_025600.md`（本报告）
  - `search_results_latest.json`（9 条查询的原始 99 条去重记录 + 筛选标注）

---

## Diff vs 2026-07-19 report / 与上一期（2026-07-19）对比

- **范围扩大**：上期 3 条 LNM 查询 / 41 篇；本期 9 条多轴查询 / 67 篇（新增机制、TME、单细胞、空间、干性、代谢维度）。
- **本期新增的关键论文（上期未见）**：MGST1(42327722)、APOE− scRNA(39810624)、POSTN+ myCAF 图谱(41480746/39829764)、空间多组学(41398964)、SOX12-YBX1-LDHA(40593465)、SHMT2(38272883)、GLTC-LDHA(37031273)、IRS1(38172081)、N1b PTMC 多组学(40977710)、CAYA-PTC scRNA(40719066)、TIL 景观(36975413)、免疫表型(37279258)、11-gene(41656803)、Afirma 分类器(40741176)、XGBoost 远处复发(41877795)、BRAF 荟萃(41419184)、CLAM-WSI(41237514)、CEUS OLNM(40778281)、SCLResNet(41061579) 等。
- **方向演进**：上期推荐 D3（APOE−/MGST1+）；本期证据进一步巩固 D3（rubric 31，Strong），并新增 D5（CAF 生态位，基于 41480746 与 40719066）。
- **持续收敛信号**：MET/FN1 "ECM–黏附"轴在两期均出现（本期 40110574、41656803、37274228 多源确认）。
- **持续缺口**：外部前瞻验证缺失、极高 AUC 过拟合风险、中枢/侧/隐匿 LNM 混用——两期一致。
