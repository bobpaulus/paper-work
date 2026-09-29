# Literature Review: 甲状腺癌侵袭、淋巴结/远处转移、复发、预后及其分子机制 / 免疫微环境 / 单细胞·空间组学 / 机器学习算法

**Date / 日期:** 2026-07-26
**Sources / 来源:** PubMed via `paper-search-mcp` `search_pubmed` (真实检索，未编造 PMID/DOI)
**Search window / 检索时间窗:** 全部时间（all-time relevance 排序；本工具不支持按日期过滤）；监测目标为捕获相对 2026-07-25（run #3）的新信号。
**Automation / 自动化:** lit-review (run #4, 每日 03:00 触发)

---

## 中文摘要 / Chinese Abstract

本次为甲状腺癌文献定期监测第 4 次运行，沿用 `lit-review` 技能，通过已连接的 `paper-search-mcp` 真实执行 **9 路互补检索**（侵袭/转移分子机制、LNM 生物标志物、ML/DL 预测、肿瘤免疫微环境、单细胞 RNA-seq、空间多组学、预后/复发/远处转移、转移干性亚群、代谢重编程），max_results=15、relevance 排序。共获 **105 条唯一记录**，剔除非甲状腺（乳腺/肺/结直肠/胃/肝/胰腺等）与泛癌/泛 TME 综述及纯临床流行病学后，**70 篇甲状腺相关文献纳入**。

五大收敛发现保持稳定：(1) **代谢–免疫耦联**驱动 LNM——MGST1「Mito-high/immune-cold」亚型（AUC 0.833）、SHMT2（丝氨酸代谢→PTEN 甲基化→AKT）、GLTC-LDHA 琥珀酰化、SOX12-YBX1-LDHA、空间代谢组学；(2) **干性转移亚群**——APOE−（ABCA1-LXR）、MGST1 去分化顶端、ISG15/KPNA2（ATC）、DLK1（MTC）；(3) **POSTN+ myCAF 空间图谱**（423,733 细胞）预测 LNM，FN1-SDC4 / MET-FN1 ECM–黏附轴跨多项研究收敛；(4) **影像/多组学 AI** 拥挤但多为单中心、非分子（LLNM-Net AUC 0.944、CLAM-WSI、融合 DL、XGBoost 远处复发 AUC 0.88）；(5) **BRAF V600E 荟萃**（46k）仅关联淋巴结（OR 1.38）与复发（OR 1.56），不关联远处转移/死亡。

推荐方向：**D3——界定并靶向 APOE−/MGST1+ 代谢–免疫干性转移亚群**（rubric 总分 **31**，强候选），连续 4 次运行一致推荐。本次新信号：干性维度新增 **DLK1（MTC 干性，39595993）** 与干细胞生物学综述（25426258）；MTC 经 5-HT/SERT/NETs 肝转移（39903533）作为子方向 D6（rubric 26）。

## English Abstract

This is the 4th daily run of the thyroid-cancer literature surveillance automation, executed with the `lit-review` skill and the connected `paper-search-mcp` (`search_pubmed`, real retrieval — no fabricated PMIDs/DOIs). **Nine complementary queries** (invasion/metastasis mechanism; LNM biomarker; ML/DL prediction; tumor immune microenvironment; single-cell RNA-seq; spatial multi-omics; prognosis/recurrence/distant metastasis; metastatic stemness; metabolic reprogramming) were run at max_results=15, relevance sort. **105 unique records** were retrieved; after excluding non-thyroid, pan-cancer/pan-TME reviews, and pure clinical-epidemiology papers, **70 thyroid-focused papers were included**.

Five convergent axes are stable: (1) **metabolic–immune coupling** drives LNM (MGST1 "Mito-high/immune-cold" AUC 0.833; SHMT2; GLTC-LDHA succinylation; SOX12-YBX1-LDHA; spatial metabolomics); (2) **stem-like metastatic subpopulations** (APOE− via ABCA1-LXR; MGST1 dedifferentiation tip; ISG15/KPNA2 in ATC; DLK1 in MTC); (3) **POSTN+ myCAF spatial atlas** (423,733 cells) predicts LNM, with convergent FN1-SDC4 / MET-FN1 ECM–adhesion axis; (4) **imaging/multi-omics AI** is crowded but mostly single-center and non-molecular (LLNM-Net AUC 0.944; CLAM-WSI; fusion DL; XGBoost distant-recurrence AUC 0.88); (5) **BRAF V600E meta-analysis** (46k) associates with nodal (OR 1.38) and recurrence (OR 1.56) but not distant metastasis/death.

Recommended direction: **D3 — define and target the APOE−/MGST1+ metabolic–immune stem-like metastatic subpopulation** (rubric total **31**, Strong), reaffirmed for the 4th consecutive run. New signals vs run #3: stemness dimension gains **DLK1 (MTC stemness, 39595993)** and a stem-cell biology review (25426258); MTC liver metastasis via 5-HT/SERT/NETs (39903533) as sub-direction D6 (rubric 26).

---

## 检索策略 / Search Strategy

| Source | Query | Filters | Results (unique) | Notes |
|---|---|---|---:|---|
| PubMed | a) `thyroid cancer lymph node metastasis biomarker gene signature` | relevance, max 15 | 15 | 生物标志物/基因签名 |
| PubMed | b) `thyroid cancer invasion metastasis molecular mechanism` | relevance, max 15 | 15 | 侵袭/转移分子机制 |
| PubMed | c) `thyroid cancer lymph node metastasis machine learning deep learning prediction model` | relevance, max 15 | 15* | *首轮返回空间块，重跑后返回 ML/DL 影像簇 |
| PubMed | d) `thyroid cancer metastasis tumor immune microenvironment` | relevance, max 15 | 15 | 肿瘤免疫微环境 |
| PubMed | e) `thyroid cancer metastasis single cell RNA sequencing` | relevance, max 15 | 15 | 单细胞 RNA-seq |
| PubMed | f) `thyroid cancer metastasis spatial transcriptomics spatial multi-omics` | relevance, max 15 | 6 | 空间转录组/空间多组学 |
| PubMed | g) `thyroid cancer prognosis recurrence distant metastasis risk model` | relevance, max 15 | 15 | 预后/复发/远处转移 |
| PubMed | h) `thyroid cancer metastatic stemness subpopulation` | relevance, max 15 | 3 | 转移干性亚群（补充） |
| PubMed | i) `thyroid cancer metabolic reprogramming metastasis` | relevance, max 15 | 15 | 代谢重编程（补充） |

**去重 / Deduplication:** 按 PMID 归一化（39829764 为 41480746 的预印本重复，剔除）。
**筛选 / Screening:** 剔除非甲状腺（乳腺/肺/结直肠/胃/肝/胰腺/HCC/TNBC/NSCLC 等）、泛癌/泛 TME 综述、纯临床流行病学（术者volume、妊娠复发、Graves 预后、峡部 CT 几何、RAI 人群）。
**结果 / Totals:** 原始唯一 **105** → 甲状腺相关纳入 **70** → 排除 **35**。（注：本工具 `search_pubmed` 仅支持 query/max_results/sort，无日期过滤参数，故「近 30 天优先」以相关性+后续与历史报告比对实现。）

---

## 纳入论文 / Included Papers

> 按维度分组；每条保留英文原题 + 一句话中文要点。完整 70 篇的 PMID/相关性/维度标注见 `search_results_latest.json`。

### 分子机制 / Molecular Mechanism
- **APOE− subpopulation drives PTC LNM** (39810624, PTC, scRNA+ST) — APOE− 干性亚群经 ABCA1-LXR 促侵袭，13 基因 ML 预测 LNM。
- **IRS1 promotes thyroid cancer metastasis via EMT/PI3K-AKT** (38172081, TC) — IRS1 与远处转移、晚期分期正相关。
- **MAZ promotes PTC metastasis via FN1/EMT** (37664917, PTC) — MAZ 高表达预后差，诱导 EMT。
- **INHBA promotes TC metastasis via RhoA/LIMK/cofilin** (39301627, TC) — INHBA 经 RhoA 轴增强迁移侵袭。
- **CREB3L1 remodels ATC TME via ECM/CAF** (36192735, ATC, scRNA) — CREB3L1→IL-1α→α-SMA+ CAF→侵袭。
- **SOX12-YBX1-LDHA axis drives PTC metastasis** (40593465, PTC, scRNA) — SOX12 上调 YBX1 招募 LDHA 启动 TGF-β 促转移。
- **SHMT2 promotes PTC metastasis via SAM/PTEN methylation/AKT** (38272883, PTC) — 丝氨酸代谢→SAM→PTEN 甲基化→AKT 激活。
- **GLTC-LDHA succinylation drives PTC glycolysis + RAI resistance** (37031273, PTC) — lncRNA GLTC 促 LDHA K155 琥珀酰化。
- **BRAF V600E meta-analysis** (41419184, PTC, 46k) — 淋巴结 OR 1.38、复发 OR 1.56，不关联远处/死亡。
- **MGST1 drives PTC LNM via mito-metabolism + immune suppression** (42327722, PTC) — 「Mito-high」亚型，ML 模型 AUC 0.833，Toxoflavin 逆转 immune-cold。

### 免疫微环境 / Immune Microenvironment
- **POSTN+ myCAF spatial atlas predicts LNM** (41480746, TC, 423,733 cells) — POSTN+ myCAF 紧邻侵袭性肿瘤细胞，关联 LNM/进展。
- **5-HT/SERT/NETs drive MTC liver metastasis** (39903533, MTC) — 5-HT 诱导中性粒细胞胞外诱捕网，氟西汀/SERT 抑制。
- **PTC immune phenotypes via TIL spatial analysis** (37279258, PTC) — immune-desert/excluded/inflamed 三型；BRAF V600E 富集 immune-excluded 且 LNM 率高。
- **Immune landscape of PTC LNM** (36975413, PTC) — M2 巨噬/活化 NK/嗜酸粒变化；TG/HRAS 驱动基因影响浸润。
- **MET/ICAM1/PTGS2 immune-gene LNM signature** (37274228, PTC) — 免疫基因签名预测 LNM（LASSO+RF）。
- **CAYA-PTC scRNA: emCAF_LAMP5/FAP** (40719066, CAYA-PTC) — emCAF 促血管生成与转移，68Ga-FAPI-PET 潜力。
- **ISG15/KPNA2 maintains ATC stemness** (37501099, ATC, scRNA) — ISG15 ISGylation 稳定 KPNA2 维持干性。

### 单细胞 / Single-Cell
- **APOE− scRNA+ST** (39810624) — 见分子机制。
- **Spatial+single-cell PTC evolution** (39540244, PTC) — ferroptosis resistance；恶性/转移 footprint。
- **PTC LNM scRNA: CD8+ TRM** (41257484, PTC) — CD8+ 组织驻留记忆 T（MHC-I/CD99/LCK）为 LNM 关键调控。
- **PTC LNM scRNA+bulk: S100A2/DIO2** (38146045, PTC) — 19 基因诊断模型，DIO2 抑增殖。
- **Integrated multi-omics PTC LNM: FN1-SDC4** (41421038, PTC) — 17 基因 RF 模型；FN1-SDC4 空间验证。

### 空间组学 / Spatial Omics
- **Integrated spatial metabolomics+transcriptomics PTC LNM** (41398964, PTC) — 精氨酸-多胺/糖酵解空间异质；NAT8L/SVCT-2 验证。
- **POSTN+ myCAF atlas** (41480746) — 见免疫。
- **FN1-SDC4 multi-omics** (41421038) — 见单细胞。
- **PTC TIL spatial IPs** (37279258) — 见免疫。

### 算法方法 / Algorithmic (ML/DL)
- **LLNM-Net multimodal US DL** (40750786, PTC) — 7 中心 29,615 例，AUC 0.944，超专家。
- **CLAM WSI intraoperative metastasis** (41237514, PTC, 2026) — 多任务 WSI，LNM AUC 0.85，双中心。
- **Radiomics+DL fusion CLNM** (40771372 / 39682228 / 40778281 / 41061579, PTC) — 融合 SVM / AMMCNet / CEUS 视频 / 自监督多模态，AUC 0.88–0.90。
- **XGBoost DTC distant-met recurrence** (41877795, DTC, 2026) — 1,245 例，外部 AUC 0.88，分层风险 1.7%/14.4%/64.1%。
- **11-gene ML LNM (FN1…)** (41656803, PTC) — 跨 6 种 ML 算法稳定 AUC 0.78–0.81。
- **mRNA classifiers rule out invasion/LNM** (40741176, TC) — Afirma 队列 NPV 97.6–100%。
- **DNA-methylation pediatric classifier** (41701943, pediatric TC) — 预测侵袭性/驱动突变。
- **Multimodal AI PTC LNM/DFS** (38990290, PTC) — 病理+基因+免疫多模态 DL，AUC 0.83–0.93。

### 预后转移 / Prognosis & Metastasis
- **25-gene ML LNM+recurrence panel** (31711617, PTC) — TCGA，OR 8.06。
- **5-gene RNA-seq recurrence score** (31792675, PTC) — HR 6.62/3.40。
- **N1b PTMC multi-omics + immune** (40977710, PTMC) — NLR 模型 AUC 0.852；4 基因分类器 AUC 0.857。
- **Pediatric PTC distant metastasis** (32668875, pediatric PTC) — 年龄≤15 + 双侧为独立风险。
- **Cuproptosis-lncRNA prognostic signature** (37934030, TC) — AUC 0.79–0.83。
- **BRAF V600E meta** (41419184) — 见分子机制。

### 代谢重编程 / Metabolic Reprogramming (cross-cutting)
- MGST1 (42327722)、SHMT2 (38272883)、GLTC-LDHA (37031273)、SOX12-YBX1-LDHA (40593465)、空间代谢组学 (41398964)、FA 代谢综述 (40353071)、PKM2 综述 (42280115)、exosome 代谢综述 (41057823)。

---

## 证据矩阵 / Evidence Matrix

> 列按 `evidence-matrix-schema.md`：Paper | PMID/DOI | Disease | Data Source | Method | Endpoint | Main Finding | Validation | Limitations | Relevance | Gap Suggested | Future Direction。此处列 High/Medium 代表（共 70 篇，余见 JSON）。

| Paper | PMID | Disease | Data Source | Method | Endpoint | Main Finding (EN) | Validation | Limitations | Relevance | Gap | Future Dir |
|---|---|---|---|---|---|---|---|---|---|---|---|
| APOE− scRNA+ST | 39810624 | PTC | scRNA+ST (in-house) | scRNA, pseudotime, CellChat, ML | LNM | APOE− subpop drives cervical LNM via ABCA1-LXR; 13-gene ML signature | in vitro/vivo | single-center scRNA | High | molecular/singlecell/algorithm | mechanism of immune-cold APOE− | D3 |
| MGST1 mito-immune LNM | 42327722 | PTC | TCGA/GTEx + cohort + scRNA | multi-omics, consensus ML | LNM | "Mito-high" subtype, MGST1 AUC 0.833, Toxoflavin reverses immune-cold | external cohort | mechanism partly inferred | High | metabolic/immune/algorithm | target APOE−/MGST1+ subpop | D3 |
| SHMT2 metastasis | 38272883 | PTC | TCGA + in vitro | molecular + omics | metastasis | serine metabolism→SAM→PTEN methylation→AKT | in vitro/vivo | no human trial | High | molecular/metabolic | combine with immune axis | D3 |
| GLTC-LDHA | 37031273 | PTC | TCGA + in vitro | lncRNA/biochemistry | glycolysis/RAI-R | GLTC succinylates LDHA K155 → glycolysis + RAI resistance | in vitro/vivo | RAI-R cohort small | High | molecular/metabolic | spatial validation | D-new3 |
| SOX12-YBX1-LDHA | 40593465 | PTC | scRNA+bulk | CUT&Tag, IP-MS | metastasis | SOX12→YBX1→LDHA→TGF-β | clinical IHC | mechanism focus | High | molecular/singlecell/metabolic | metabolic-immune link | D3 |
| POSTN+ myCAF atlas | 41480746 | TC (pediatric+adult) | 423,733 cells, 81 samples + ST 28 | scRNA+ST, bulk 5 cohorts | LNM/progression | POSTN+ myCAF abuts invasive cells, predicts LNM | multi-institutional | mostly WDTC/ATC | High | singlecell/spatial/immune | target myCAF niche | D-new |
| FN1-SDC4 multi-omics | 41421038 | PTC | scRNA+ST+bulk | pseudotime, RF | LNM | State-1 metastasis-initiating cluster; FN1-SDC4 axis | spatial + in vitro | in-house | High | singlecell/spatial/algorithm/molecular | druggable stromal axis | D-new |
| Spatial metabolomics PTC LNM | 41398964 | PTC | spatial metabolomics+transcriptomics | multi-omics | LNM | polyamine/glycolysis spatial heterogeneity; NAT8L/SVCT-2 | TCGA + zebrafish | metabolite panel small | High | spatial/metabolic/molecular | causal metabolite test | D-new3 |
| ISG15/KPNA2 ATC | 37501099 | ATC | scRNA (GEO) + in vitro | scRNA, IP-MS | stemness/mets | ISG15 ISGylation stabilizes KPNA2 → stemness | xenograft zebra/dish | ATC rare | High | singlecell/molecular | combine with MGST1 tip | D3 |
| DLK1 MTC stemness | 39595993 | MTC | cell lines | stemness assay | stemness | DLK1+ enriches stemness (MZ-CRC-1>TT) | spheroid/Hoechst | cell-line only | Medium | molecular | in vivo MTC validation | D3 |
| 5-HT/NETs MTC liver mets | 39903533 | MTC/NE | in vivo | histone serotonylation | liver mets | 5-HT→NETs→MTC liver mets; fluoxetine blocks | genetic + pharmacologic | MTC cohort small | High | immune/prognosis | SERT inhibitor trial | D6 |
| PTC TIL spatial IPs | 37279258 | PTC | TCGA WSI | AI TIL density | LNM | immune-excluded enriched in BRAF V600E, higher LNM | TCGA | no IO cohort | High | immune/spatial | predict IO response | D-new |
| PTC LNM immune landscape | 36975413 | PTC | TCGA + in-house | immune deconvolution | LNM | M2 mac ↑ / NK ↓ in LNM; TG/HRAS effects | survival | retrospective | High | immune | driver–immune causality | D-new |
| MET/ICAM1 LNM | 37274228 | PTC | TCGA + IHC | WGCNA, LASSO/RF | LNM | MET/ICAM1/PTGS2 immune-gene signature | IHC | internal only | High | immune/molecular | ECM–adhesion axis | D-new |
| IRS1 metastasis | 38172081 | TC | 131 tissues + RNA-seq | IHC, RNA-seq | distant mets | IRS1 ↑ in mets; EMT/PI3K-AKT | in vitro | cohort single | High | molecular | stratify high-risk | D-new |
| MAZ/FN1 EMT | 37664917 | PTC | TCGA + IHC | bioinformatics, functional | metastasis | MAZ→FN1→EMT | in vitro | FN1 inverse corr | High | molecular | converge w/ FN1 axis | D-new |
| INHBA RhoA | 39301627 | TC | GEO/TCGA + in vivo | molecular | metastasis | INHBA→RhoA/LIMK/cofilin | zebrafish/mouse | mechanism | Medium | molecular | stromal crosstalk | D-new |
| CREB3L1 ATC CAF | 36192735 | ATC | microarray + scRNA | scRNA, functional | invasion/mets | CREB3L1→IL-1α→α-SMA CAF | xenograft | ATC rare | High | molecular/singlecell/immune | CAF-targeted therapy | D-new |
| LLNM-Net | 40750786 | PTC | 7-center US (29,615) | multimodal DL (bidirectional attention) | lateral LNM | AUC 0.944 > experts 64.3% | multicenter | non-molecular | High | algorithm | molecular subtype stratify | DL-img |
| CLAM WSI | 41237514 | PTC | 2-center WSI (569) | MIL/CLAM | intraop LNM | AUC 0.85 LNM; interpretable | 2-center | frozen-section only | High | algorithm | pair w/ spatial ground truth | DL-img |
| Fusion DL CLNM | 40771372 | PTC | 2-center US (405) | radiomics+DL SVM | CLNM | intra+peri-tumoral fusion AUC 0.881 ext | external | single modality | High | algorithm | multicenter + molecular | DL-img |
| MRI DL CLNM | 39682228 | PTC | MRI (105) | AMMCNet DL | CLNM | AUC 0.891 | train/test | small n | High | algorithm | external multisite | DL-img |
| CEUS video DL | 40778281 | PTC | CEUS video (396) | DL video | occult LNM | combined AUC 0.734 test | test set | modest test | High | algorithm | larger test | DL-img |
| Self-sup multimodal | 41061579 | PTC | US+CT (PVAT) | SCLResNet+DSAF | CLNM | AUC 0.863/0.839 | external | PVAT label | High | algorithm | prospective | DL-img |
| XGBoost distant recur | 41877795 | DTC | 1,245 pts | XGBoost (LASSO select) | distant-met recur | AUC 0.88 ext; risk 1.7/14.4/64.1% | validation 374 | retrospective | High | algorithm/prognosis | prospective + RAI-R | DL-img |
| 11-gene ML LNM | 41656803 | PTC | TCGA (457) | 4 methods + 6 ML algos | LNM | FN1/PI15/IL11… AUC 0.80/0.79 | 6-algo CV | TCGA only | High | algorithm/molecular | external molecular | D-new |
| mRNA rule-out classifiers | 40741176 | TC | Afirma (697 dev) | ML classifiers | invasion/LNM | NPV 97.6–100% rule-out | 259 val | commercial cohort | High | algorithm | prospective | DL-img |
| Methylation pediatric | 41701943 | pediatric TC | 2 cohorts (184) | methylation classifiers | invasiveness | predicts nodal mets + driver mut | validation | pediatric only | High | algorithm/molecular | adult extension | D3 |
| Multimodal AI PTC | 38990290 | PTC | 1,011 pts + TCGA | DL (path+genomic+immune) | LNM/DFS | AUC 0.83–0.93; scRNA T-cell subsets | TCGA val | single-center real | High | algorithm/singlecell/immune | multicenter | DL-img |
| 25-gene panel | 31711617 | PTC | TCGA (495) | ML + Cox | LNM/DFS | OR 8.06 nodal; HR 2.64 DFS | KM | early-stage only | High | algorithm/prognosis | validation | D-new |
| 5-gene recurrence | 31792675 | PTC | TCGA (479) | Cox ML | recurrence | HR 6.62/3.40 | chronological split | no ext val | High | algorithm/prognosis | external | — |
| N1b PTMC multi-omics | 40977710 | PTMC | 638 + RNA-seq | WGCNA+ML, CIBERSORT | N1b mets | NLR AUC 0.852; 4-gene AUC 0.857 | IHC | single center | High | algorithm/immune/singlecell | multicenter | D-new |
| Cuproptosis signature | 37934030 | TC | TCGA | Cox lncRNA | prognosis | AUC 0.79–0.83 | ROC | no wet-lab | Medium | prognosis/algorithm | biology | — |
| Pediatric distant mets | 32668875 | pediatric PTC | 180 | Cox | distant mets | age≤15 + bilateral independent | KM | retrospective | Medium | prognosis | — | — |
| BRAF V600E meta | 41419184 | PTC | 46k (46 studies) | MA (random-effects) | nodal/recur/death | OR nodal 1.38, recur 1.56; not distant/death | sensitivity OK | heterogeneity | High | prognosis/molecular | subtype-stratified | D-new |

---

## 已知结论 / What Is Already Known

1. **代谢–免疫耦联是 LNM 的核心驱动（最强收敛信号）。** MGST1 定义「Mito-high」亚型并伴随 CD8+ T 耗竭与 Treg 富集（42327722，外部 AUC 0.833）；SHMT2 经丝氨酸→SAM→PTEN 甲基化→AKT（38272883）；GLTC 促进 LDHA K155 琥珀酰化致糖酵解与 RAI 抵抗（37031273）；SOX12-YBX1-LDHA 经 TGF-β（40593465）；空间代谢组学证实精氨酸-多胺/糖酵解空间异质（41398964）。
2. **干性转移亚群跨亚型存在。** PTC 中 APOE− 经 ABCA1-LXR 促侵袭并呈 immune-cold（39810624，机器学习 13 基因签名）；MGST1 位于去分化轨迹顶端（42327722）；ATC 中 ISG15/KPNA2 维持癌干样（37501099）；MTC 中 DLK1+ 富集干性（39595993）。
3. **CAF 生态位（POSTN+ myCAF）与 ECM–黏附轴收敛。** 423,733 细胞图谱定位 POSTN+ myCAF 紧邻侵袭性肿瘤细胞并预测 LNM（41480746）；FN1-SDC4（41421038）、MET-FN1（40110574）、MET/ICAM1（37274228）、MAZ-FN1（37664917）共同指向 FN1/整合素/ECM–黏附为 LNM 枢纽。
4. **影像/多组学 AI 性能高但证据薄弱。** LLNM-Net（超声多模态 AUC 0.944，7 中心）与 CLAM-WSI（术中 LNM AUC 0.85，双中心）为代表；XGBoost 远处复发 AUC 0.88（41877795）。但均为回顾性、单/少中心、非分子，且预后 AUC 多在 0.78–0.89。
5. **BRAF V600E 预后价值有限。** 46k 荟萃确认其关联淋巴结（OR 1.38）与复发（OR 1.56），但不关联远处转移或死亡（41419184）——不支持作为独立远处转移预后标志。

## 未解问题 / What Remains Unclear

- **干性亚群的因果与可靶向性**：APOE−/MGST1+ 是否为同一连续谱？缺少体内清除/过继转移实验证明其为「转移起始细胞」。
- **代谢–免疫耦联的方向性**：是代谢重编程导致 immune-cold，还是 immune-cold 选择代谢表型？MGST1 逆转实验（Toxoflavin）提示可靶向，但临床转化未启。
- **FN1/MET/ECM 轴的可药性**：FN1-SDC4、MET 多为 correlative + 体外敲低，缺少空间分辨的配体–受体阻断在体实验。
- **MTC 肝转移的神经–免疫轴**：5-HT/SERT/NETs 机制清晰（39903533），但氟西汀再定位的临床可行性未证。
- **AI 模型的泛化**：影像 DL 多单中心、缺乏分子分层与外部多中心验证；c-index 天花板 ~0.76–0.89。
- **亚型覆盖不均**：ATC/MTC 样本小、单细胞/空间研究集中于 PTC；pediatric/AYA 与 FTC 证据稀少。

## 领域方法/数据局限 / Method / Data Limitations In The Field

- **公共数据复用与批次效应**：TCGA/GTEx/GEO 被反复使用；scRNA+ST 多来自单中心小队列，跨平台批次未系统校正。
- **终点稀疏**：远处转移、复发、特异性死亡事件少，尤其 ATC/MTC；多数模型以 LNM 为终点。
- **外部验证缺失**：大量 LNM 基因签名仅在 TCGA 内或单中心验证；影像 DL 极少多中心。
- **亚型分层不足**：BRAF/RAS/RET 分子亚型与免疫/代谢表型联动分析刚起步。
- **湿实验验证弱**：许多「机制」论文止于体外敲低，缺少体内转移与药物敏感性闭环。
- **检索方差**：同一查询在不同轮次返回不同 top-15（本次 c 查询先后在空间块与 ML/DL 块间漂移），提示相关性排序不稳定。

---

## 候选未来方向 / Candidate Future Directions

评分按 `research-direction-rubric.md`（1–5 × 7 维；28–35 = 强候选）。

| # | Direction | Rationale | Feasibility | Required Data | Validation | Main Risk | Claim Boundary | Rubric |
|---|---|---|---|---|---|---|---|---|
| **D3** | 界定并靶向 **APOE−/MGST1+ 代谢–免疫干性转移亚群** | 跨 PTC/ATC 收敛的 stem-like + metabolic-immune 轴，缺因果与靶向证据 | 公共 scRNA+ST+TCGA 现成 | 41480746 图谱、39810624、42327722、37501099；补充 scRNA of MGST1-high | 体内清除/过继转移 + Toxoflavin 类药敏 | 亚群异质性大 | 不宣称「治愈」，仅「风险分层+可靶向亚群」 | **31 (Strong)** |
| **D-new** | 绘制 **POSTN+ myCAF / FN1-SDC4 / MET ECM–黏附轴** 的空间多组学图谱并靶向 LNM | FN1/MET/ECM 跨 5+ 研究收敛，缺空间分辨靶向 | 空间平台现成 | 41480746、41421038、40110574、37274228 | 空间阻断 + 类器官共培养 | 体内递送难 | 不宣称临床疗效 | **31 (Strong)** |
| **D-new3** | **代谢–免疫耦联治疗**（MGST1/SHMT2/GLTC-LDHA + immune-cold 逆转） | 多篇机制+1 个药物逆转雏形 | 代谢+免疫双人可 | 42327722、38272883、37031273、41398964 | 类药筛选 + 免疫表型 | 脱靶/毒性 | 仅临床前 | **30 (Strong)** |
| **D6** | **5-HT/SERT/NETs 轴** MTC 肝转移（氟西汀再定位） | 机制清晰、已有 FDA 药 | MTC PDX/斑马鱼 | 39903533；MTC 队列 | SERT 抑制剂体内 | MTC 罕见、样本小 | 仅 MTC 肝转移亚群 | **26 (Feasible)** |
| **DL-img** | 分子分层的**多中心影像/WSI DL**前瞻性验证 | 模型多但泛化弱 | 模型已有 | LLNM-Net/CLAM + TCGA 分子 | 多中心 + 空间组学金标准 | 泄漏/偏倚 | 不宣称替代病理 | **24 (Feasible)** |

## 推荐下一步方向 / Recommended Next Direction

**D3 — Define and target the APOE−/MGST1+ metabolic–immune stem-like metastatic subpopulation** (rubric **31**, Strong), 连续 4 次运行一致推荐。

- **Why:** 分子机制（APOE−/ABCA1-LXR、MGST1 去分化顶端）、免疫（immune-cold）、单细胞/空间（39810624、42327722、41480746）、算法（13 基因/ML 模型）五维证据闭合，且 MGST1 已有 Toxoflavin 逆转雏形，是直接「风险分层 + 可靶向亚群」。
- **First concrete steps:** (1) 在 41480746 的 423k 细胞图谱中联合定义 APOE−∩MGST1+ 状态并验证其 LNM 富集；(2) 用独立 TCGA + 机构 scRNA 做外部验证；(3) 体内过继转移 APOE−/MGST1+ 细胞证明转移起始能力；(4) 测试 Toxoflavin 类 MGST1 抑制联用免疫检查点阻断逆转 immune-cold。
- **Claim boundary:** 仅主张「可靶向的干性转移风险亚群」，不宣称治愈或独立预后标志。

## 随访阅读清单 / Follow-Up Reading List

- **39810624** (APOE− PTC LNM) — D3 的机制与 ML 基石。
- **42327722** (MGST1 Mito-high/immune-cold) — D3 的代谢–免疫耦联核心 + 药物逆转。
- **41480746** (POSTN+ myCAF 423k 图谱) — D-new 空间 CAF 生态位金标准。
- **41421038** (FN1-SDC4 多组学) — D-new ECM–黏附轴闭环。
- **39903533** (5-HT/NETs MTC 肝转移) — D6 神经–免疫轴。
- **40750786 / 41237514** (LLNM-Net / CLAM) — DL-img 标杆，需分子分层验证。
- **41419184** (BRAF V600E 46k 荟萃) — 校正「BRAF=远处转移预后」误区。

## 可复现性说明 / Reproducibility Notes

- **Search date / 检索日期:** 2026-07-26
- **Databases / 数据库:** PubMed（via `paper-search-mcp` `search_pubmed`）
- **Query strings / 检索式:** 见「检索策略」表 a–i（9 路）
- **Filters / 过滤:** max_results=15, sort=relevance；按 PMID 去重；剔除非甲状腺/泛癌综述/纯临床流行病学
- **Deduplication rule / 去重规则:** PMID 归一化（39829764≡41480746 预印本重复剔除）
- **Screening rule / 筛选规则:** 甲状腺相关（PTC/FTC/MTC/ATC/PTMC/DTC/pediatric）+ 侵袭/LNM/远处转移/复发/预后/分子机制/免疫/单细胞/空间/ML 维度；非甲状腺及泛癌综述排除
- **Tooling note / 工具说明:** `search_pubmed` 仅支持 query/max_results/sort，无日期过滤；本轮 c 查询首次返回空间块、重跑返回 ML/DL 影像簇（相关性排序方差，已通过重跑修复）
- **Files saved / 生成文件:**
  - `D:\paperwork\lit_review\literature_review_20260726_025520.md`（本报告）
  - `D:\paperwork\lit_review\search_results_latest.json`（105 条记录，含 relevance + dimensions + query 标签）
  - `D:\paperwork\lit_review\_build_search_json_run4.py`（生成脚本）

---

## 与历史报告对比 / Comparison With Prior Run (2026-07-25, run #3)

| 指标 | run #3 (2026-07-25) | run #4 (本次) | 变化 |
|---|---:|---:|---|
| 原始唯一记录 | 106 | 105 | −1 |
| 甲状腺相关纳入 | 74 | 70 | −4 |
| 排除 | 32 | 35 | +3 |
| 新信号（vs 上次） | 10 新 + 7 再纳入 | **2 新**（25426258, 39595993） | 收敛 |
| 推荐方向 | D3 (rubric 32) | **D3 (rubric 31)** | 一致 |

**本次新增文献（vs run #3）：** 25426258（甲状腺癌干细胞生物学综述）、39595993（DLK1 与 MTC 干性表型）——均属**转移干性**维度，强化「MTC 干性」子主题（与 ATC 的 ISG15/KPNA2 37501099 形成跨亚型呼应）。

**相对上次的方向变化：**
1. **干性查询漂移：** run #3 的干性查询返回 37455764（lncRNA ROR/MALAT1 CD133+ ATC 干性）、39271768、40563572，本次未重检索到（检索相关性方差）；但新增 DLK1（MTC）与干细胞综述，MTC 干性维持为活跃子方向。
2. **ML/DL 影像簇稳定回归：** LLNM-Net（40750786）、CLAM-WSI（41237514）、融合 DL（40771372/39682228/40778281/41061559）、XGBoost 远处复发（41877795）全部重检索到，AI 维度证据稳定。
3. **五大收敛轴不变：** 代谢–免疫耦联（MGST1/SHMT2/GLTC-LDHA/SOX12）、干性亚群（APOE−/MGST1/ISG15/DLK1）、POSTN+ myCAF + FN1/MET ECM 轴、影像 AI、BRAF V600E 荟萃结论均延续。
4. **总体判断：** 甲状腺癌转移研究领域处于「证据巩固期」——每周新增以机制细节补全为主，未出现颠覆性新方向；D3（APOE−/MGST1+ 代谢–免疫干性亚群）连续 4 次运行被推荐，且获得代谢（SHMT2/GLTC/MGST1）、空间（41480746/41421038）、单细胞（39810624/37501099）三维支撑，是最成熟的下一步切入点。
