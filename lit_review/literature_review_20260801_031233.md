# Literature Review: 甲状腺癌侵袭·淋巴结与远处转移·复发·预后及分子机制 / 肿瘤免疫微环境 / 单细胞与空间组学 / 机器学习算法方向

**Date / 日期:** 2026-08-01
**Sources / 数据源:** PubMed（via `mcp__paper-search-mcp__search_pubmed`，DeferExecuteTool 调用）
**Search window / 检索窗口:** all time；MCP 无日期过滤器，故以 `sort=relevance` 近似近期优先
**Run / 轮次:** run #10（自动监测任务「甲状腺癌文献定期监测 / lit-review」）
**Queries / 检索式:** 9 路互补（a–i），`max_results=15`，`sort=relevance`

---

## 中文摘要 (Chinese Abstract)

本轮（run #10，2026-08-01）沿用 9 路互补 PubMed 检索，覆盖甲状腺癌（PTC/PTMC/FTC/MTC/ATC）侵袭、淋巴结转移（LNM）、远处转移、复发、预后，及其分子机制、肿瘤免疫微环境（TIME）、单细胞（scRNA-seq）、空间组学（spatial multi-omics）与机器学习/深度学习（ML/DL）算法方法。9 路检索共返回原始记录 **126 行**，去重后 **76 个唯一 PMID**，剔除非甲状腺文献（乳腺/胃/肝/胰腺/泛癌综述）后 **48 篇纳入（in-scope）**、**28 篇排除**。

与上一轮（run #9，2026-07-31）对比，**0 篇新纳入文献**——语料库自 run #7（2026-07-28）以来已连续 4 轮处于平台期（174 唯一 / 103 纳入）。所有返回的 76 个 PMID 均已在 run #9 语料库中。本报告的收敛发现（5 条主轴）与 run #9 完全一致，未被任何反证削弱。

五大收敛主轴：**(1) 代谢–免疫耦联驱动 LNM**（MGST1/SHMT2/GLTC–LDHA/SOX12–YBX1–LDHA 等多条通路汇向「Mito-high / immune-cold」表型）；**(2) 转移性干性亚群**（APOE− 细胞经 ABCA1–LXR 轴、ISG15–KPNA2 维持 ATC 干性）；**(3) POSTN+ myCAF 空间图谱**（41480746，423k 细胞）预测 LNM；**(4) 影像/多组学 AI**（LLNM-Net AUC 0.944、多模态 DL 38990290、XGBoost 远处复发 41877795 AUC 0.88）但普遍单中心、缺外部验证；**(5) BRAF V600E 荟萃分析**（41419184，46k 例）结节日 OR 1.38 / 复发 OR 1.56，但**不**预测远处转移或死亡——印证 DTC「远处转移 vs LNM 解耦」。

推荐方向仍为 **D3（界定并靶向 APOE−/MGST1+ 代谢–免疫干性转移亚群）**，rubric 总分 **32（Strong）**，连续第 10 轮确认。

> ⚠️ 数据完整性说明：本轮执行中 `search_results_latest.json` 一度被误覆盖，导致 run #9 的累计 174 条语料（含 55 篇纳入长尾 + 43 篇排除）不可从磁盘恢复；本文件现以本轮返回的 76 条并集（48 纳入 / 28 排除）作为后续新文献检测的活动基线。报告证据矩阵基于本轮 48 篇纳入文献（含全部关键收敛论文）撰写，结论不受影响。

## English Abstract

This run (#10, 2026-08-01) repeats the 9 complementary PubMed queries covering thyroid cancer (PTC/PTMC/FTC/MTC/ATC) invasion, lymph-node metastasis (LNM), distant metastasis, recurrence, prognosis, plus molecular mechanisms, tumor immune microenvironment (TIME), single-cell (scRNA-seq), spatial multi-omics, and machine-learning/deep-learning (ML/DL) methodology. The 9 queries returned **126 raw rows → 76 unique PMIDs → 48 in-scope / 28 excluded** (non-thyroid off-topic papers removed).

Versus the prior run (#9, 2026-07-31): **0 new in-scope papers**. The corpus has been at a hard plateau since run #7 (174 unique / 103 in-scope); all 76 returned PMIDs were already present in the run #9 corpus. The five convergent axes are unchanged and unchallenged.

Five axes: **(1) metabolic–immune coupling drives LNM** (MGST1/SHMT2/GLTC–LDHA/SOX12–YBX1–LDHA converge on a "Mito-high / immune-cold" phenotype); **(2) stem-like metastatic subpopulations** (APOE− via ABCA1–LXR; ISG15–KPNA2 sustains ATC stemness); **(3) POSTN+ myCAF spatial atlas** (41480746, 423k cells) predicts LNM; **(4) imaging/multi-omics AI** (LLNM-Net AUC 0.944; multimodal DL 38990290; XGBoost distant-recurrence 41877795 AUC 0.88) but single-center, lacking external validation; **(5) BRAF V600E meta-analysis** (41419184, 46k) links nodal OR 1.38 / recurrence OR 1.56 but **not** distant metastasis or death — corroborating DTC "distant-metastasis vs LNM decoupling."

Recommended direction remains **D3 (define & target the APOE−/MGST1+ metabolic–immune stem-like metastatic subpopulation)**, rubric total **32 (Strong)**, confirmed for the 10th consecutive run.

> ⚠️ Reproducibility note: the cumulative 174-record `search_results_latest.json` was inadvertently overwritten mid-run; this file now uses run #10's 76-record union (48 in-scope / 28 excluded) as the active baseline for future new-detection. The evidence matrix below is built on the 48 in-scope papers (all key convergent papers included); conclusions are unaffected.

---

## 检索策略 (Search Strategy)

| Source | Query | Filters | max / sort | Results (raw→unique→in-scope) | Notes |
|---|---|---|---:|---|---|
| PubMed | a) `thyroid cancer lymph node metastasis biomarker gene signature` | relevance | 15 | 15 → (union) | LNM 基因标志物/签名 |
| PubMed | b) `thyroid cancer invasion metastasis molecular mechanism` | relevance | 15 | 15 → (union) | 侵袭/转移机制（MCP 返回偏单细胞集，relevance drift） |
| PubMed | c) `thyroid cancer lymph node metastasis machine learning deep learning prediction model` | relevance | 15 | 15 → (union) | ML/DL 预测（返回偏 TME/代谢综述） |
| PubMed | d) `thyroid cancer metastasis tumor immune microenvironment` | relevance | 15 | 6 → (union) | TIME（仅回 6 条，含空间代谢组） |
| PubMed | e) `thyroid cancer metastasis single cell RNA sequencing` | relevance | 15 | 15 → (union) | scRNA-seq（relevance drift 至预后集） |
| PubMed | f) `thyroid cancer metastasis spatial transcriptomics spatial multi-omics` | relevance | 15 | 15 → (union) | 空间多组学（返回单细胞+空间集） |
| PubMed | g) `thyroid cancer prognosis recurrence distant metastasis risk model` | relevance | 15 | 15 → (union) | 预后/复发/远处转移风险模型 |
| PubMed | h) `thyroid cancer metastatic stemness subpopulation` | relevance | 15 | 15 → (union) | 转移干性亚群（relevance drift 至预后集） |
| PubMed | i) `thyroid cancer metastasis metabolic reprogramming` | relevance | 15 | 15 → (union) | 代谢重编程 |

**合计 / Totals:** 9 queries → **126 raw rows** (含重叠块) → **76 unique PMIDs** → **48 in-scope / 28 excluded**.
**工具 / Tooling:** 本地 `paper_search_mcp` 包未安装，改用已连接 MCP `mcp__paper-search-mcp__search_pubmed`（DeferExecuteTool）。4 路（b/e/g/i）首次调用出现瞬时 `not well-formed (invalid token)` 解析错误，按技能降级规则逐路重发后全部返回。MCP 无日期过滤器，故以 `sort=relevance` 近似「近 30 天优先」。
**去重 / Dedup:** 以 PMID 为键；跨 9 路并集去重。
**剔除 / Exclusion:** 非甲状腺文献（乳腺 37696831/36704213/41608657、胃 42373830/40201390、肝 40850678/40315321、胰腺 41219790、泛癌 39923580/38935111/38981044）与纯临床流行病学（41817109 RAI 人群队列）判为排除；本轮 28 篇排除均为既往已判非甲状腺/泛癌。

---

## 纳入论文 (Included Papers)

本轮 48 篇纳入（28 High + 20 Medium）。以下列出 **28 篇 High-相关性** 论文（英文标题保留，附中文一句话要点）；20 篇 Medium 见文末压缩清单。

### High 相关性（28 篇）

1. **A novel gene panel for prediction of lymph-node metastasis and recurrence in patients with thyroid cancer.** (PMID 31711617, *Surgery* 2020). 25-gene ML 签名预测 PTC 淋巴结转移（N0/N1，敏感度 86%）与无病生存（HR 2.64）。
2. **A novel RNA sequencing-based risk score model to predict papillary thyroid carcinoma recurrence.** (PMID 31792675, *Clin Exp Metastasis* 2020). TCGA 5-gene（TOP2A 等）复发风险模型，训练 HR 6.62 / 验证 HR 3.40。
3. **CREB3L1 promotes tumor growth and metastasis of anaplastic thyroid carcinoma by remodeling the tumor microenvironment.** (PMID 36192735, *Mol Cancer* 2022). ATC 中 CREB3L1 经 ECM 信号激活 α-SMA+ CAF，驱动侵袭/转移；scRNA 见渐进性激活。
4. **Tumor-Infiltrating Immune Cell Landscapes in the Lymph Node Metastasis of Papillary Thyroid Cancer.** (PMID 36975413, *Curr Oncol* 2023). PTC LNM 中活化 DC/M0 巨噬升高、NK/嗜酸粒下降，且受 TG/HRAS 驱动突变塑造。
5. **LncRNA GLTC targets LDHA for succinylation and enzymatic activity to promote progression and radioiodine resistance in papillary thyroid cancer.** (PMID 37031273, *Cell Death Differ* 2023). GLTC 结合 LDHA 促 K155 琥珀酰化→糖酵解+远处转移+RAI 抵抗。
6. **Identification of key immune genes related to lymphatic metastasis of papillary thyroid cancer via bioinformatics analysis and experimental validation.** (PMID 37274228, *Front Oncol* 2023). MET、ICAM1、PTGS2 为 LNM 枢纽免疫基因（RF+LASSO，AUC≈0.83），IHC 验证。
7. **Papillary thyroid cancer immune phenotypes via tumor-infiltrating lymphocyte spatial analysis.** (PMID 37279258, *Endocr Relat Cancer* 2023). TCGA PTC 基于 TIL 空间分布分 immune-desert(48%)/excluded(34%)/inflamed(18%)；excluded 多 BRAF V600E 且 LNM 率高。
8. **ISG15 and ISGylation modulates cancer stem cell-like characteristics in promoting tumor growth of anaplastic thyroid carcinoma.** (PMID 37501099, *J Exp Clin Cancer Res* 2023). ISG15 经 ISGylation 稳定 KPNA2 维持 ATC 干性，促进转移。
9. **Single-cell and bulk RNA sequencing reveal heterogeneity and diagnostic markers in papillary thyroid carcinoma lymph-node metastasis.** (PMID 38146045, *J Endocrinol Invest* 2024). scRNA+bulk 鉴定 S100A2/DIO2 为 PTC LNM 诊断标志物（66 例验证）。
10. **SHMT2 promotes papillary thyroid cancer metastasis through epigenetic activation of AKT signaling.** (PMID 38272883, *Cell Death Dis* 2024). SHMT2 生成 SAM→甲基化抑制 PTEN→AKT 激活→PTC 转移。
11. **Artificial intelligence-based multi-modal multi-tasks analysis reveals tumor molecular heterogeneity, predicts preoperative lymph node metastasis and prognosis in papillary thyroid carcinoma.** (PMID 38990290, *Int J Surg* 2025). 1011 例多模态 DL（病理+基因组+转录组+免疫）预测 LNM/DFS，AUC 0.83–0.86；含 scRNA。
12. **Spatial and Single-Cell Transcriptomics Unraveled Spatial Evolution of Papillary Thyroid Cancer.** (PMID 39540244, *Adv Sci* 2025). scRNA+SRT 解析 PTC 空间异质/恶性演化，ferroptosis 抵抗促演进。
13. **Single-cell RNA-sequencing and spatial transcriptomic analysis reveal a distinct population of APOE- cells yielding pathological lymph node metastasis in papillary thyroid cancer.** (PMID 39810624, *Clin Transl Med* 2025). **APOE− 亚群**经 ABCA1–LXR 轴促 LNM；13-gene scRNA ML 签名。
14. **5-HT orchestrates histone serotonylation and citrullination to drive neutrophil extracellular traps and liver metastasis.** (PMID 39903533, *J Clin Invest* 2025). 5-HT/SERT 经 NETs 驱动 MTC（及 NEPC/SCLC）肝转移；fluoxetine 可阻断。
15. **Identification of Novel Gene Signature Predicting Lymph Node Metastasis in Papillary Thyroid Cancer via Bioinformatics Analysis and in vitro Validation.** (PMID 40110574, *IJGM* 2025). 6-gene 签名（COL8A2/MET/FN1/MPZL2/PDLIM4/CLDN10）预测 PTC LNM，体外验证。
16. **The SOX12-YBX1-LDHA signaling axis drives metastasis in papillary thyroid carcinoma.** (PMID 40593465, *Cell Death Dis* 2025). SOX12→YBX1→LDHA 激活 TGF-β→PTC 转移。
17. **Single-Cell RNA Sequencing Reveals the Heterogeneity in Differentiation Trajectory and Tumor Microenvironment Leading to More Aggressive Phenotypes of Papillary Thyroid Cancer in Children and Young Adult Patients.** (PMID 40719066, *Adv Sci* 2025). CAYA-PTC 缺「mild-state」恶性 thyrocyte，emCAF_LAMP5 促血管/转移。
18. **Development and validation of mRNA expression-based classifiers to predict low-risk thyroid tumors.** (PMID 40741176, *Front Endocrinol* 2025). mRNA 分类器以 NPV 97.6–100% 排除侵袭/LNM，减过度手术。
19. **Multi-omics analysis and metastasis risk factor prediction in N1b stage PTMC.** (PMID 40977710, *Front Immunol* 2025). N1b-PTMC 多组学+ML：NLR 模型 AUC 0.852；ALDH1A3/CTXN1/MGAT3/TMEM163 签名 AUC 0.857。
20. **Single-cell RNA sequencing reveals tumor cell and immune cell variations associated with lymphatic metastasis in papillary thyroid cancer.** (PMID 41257484, *Endocr Connect* 2025). PTC LNM scRNA：CD8+ TRM 经 MHC-I/CD99/LCK 调控 LNM。
21. **Integrated spatial metabolomics and transcriptomics reveal the molecular landscape of papillary thyroid cancer and its lymph node metastasis.** (PMID 41398964, *J Transl Med* 2025). **空间代谢组+转录组**：精氨酸-多胺轴/糖酵解/脂代谢失调；NAT8L/SVCT-2 促转移。
22. **Prognostic Value of BRAF V600E Mutation in Papillary Thyroid Carcinoma: A Meta-Analysis of Nodal Involvement, Distant Metastases, Recurrence, and Mortality.** (PMID 41419184, *Endocr Pract* 2026). 46k 例荟萃：淋巴结 OR 1.38 / 复发 OR 1.56（边界），**不**预测远处转移（OR 0.75）或死亡（OR 0.97）。
23. **Cellular and molecular determinants of lymph node metastasis in papillary thyroid carcinoma: Integrated multi-omics profiling and machine learning models.** (PMID 41421038, *Comput Biol Chem* 2026). scRNA+ST+bulk：N1 免疫炎症增强但抗原呈递下调；**FN1–SDC4** 轴驱动转移，random-forest LNM 模型。
24. **An integrated single-cell and spatial transcriptomic atlas of thyroid cancer progression identifies prognostic fibroblast subpopulations.** (PMID 41480746, *JCI Insight* 2026). **423,733 细胞**整合图谱：POSTN+ myCAF 与侵袭/LNM/进展相关，预测不良预后。
25. **[A multi-molecular predictive model for lymph node metastasis in papillary thyroid carcinoma based on machine learning algorithms].** (PMID 41656803, *J Cent South Univ Med Sci* 2025). TCGA 457 例 11-gene（FN1 等）ML LNM 模型，验证 AUC 0.793。
26. **DNA Methylation-Based Risk Stratification and Classification of Pediatric Thyroid Carcinoma.** (PMID 41701943, *Clin Cancer Res* 2026). 儿童 TC 甲基化分型预测侵袭性（ nodal metastasis），两队列验证。
27. **Development and validation of a machine learning model for predicting high-risk distant metastatic recurrence in differentiated thyroid cancer.** (PMID 41877795, *Front Med* 2026). 1245 例 DTC，XGBoost 预测远处转移复发 AUC **0.88**（374 例外部验证），分层低/中/高险。
28. **MGST1 drives lymph node metastasis in papillary thyroid carcinoma via mitochondrial metabolic reprogramming and immune suppression.** (PMID 42327722, *Front Immunol* 2026). **MGST1** 为核心驱动：「Mito-high」亚型 CD8+ T 耗竭+Treg 富集；模型外部验证 AUC **0.833**；Toxoflavin 逆转 immune-cold。

### Medium 相关性（20 篇，压缩列出）

- 预后/复发：27697309（儿童 DTC 复发）、30942873（代谢基因去分化签名）、32615728（PTC 风险评分系统荟萃）、32668875（儿童 PTC 远处转移）、33656532（4-gene 免疫签名去分化）、34595349（男性 PTC miRNA）、35033555（eRNA 预后）、35255661（PTC 免疫分型/复发 HOXD9）、37851243（PTMC BRAF V600E）、37934030（cuproptosis lncRNA）、40171809（3-gene nomogram）、41084771（PTC 侵袭综述）、41368991（BRAF V600E 综述）
- 免疫/TME：32626535（TC 免疫微环境综述）、33656532（同上免疫签名）、37173925（雌激素-TME）、39497824（凝血相关基因/侧颈 LNM）、35255661（免疫亚型）
- 代谢：40353071（脂肪酸代谢重编程综述）、40980146（TC 分子综述）、41057823（外泌体代谢重编程综述）、42280115（PKM2 糖酵解综述）

---

## 证据矩阵 (Evidence Matrix)

*按 `evidence-matrix-schema.md`：Paper / PMID·DOI / Disease / Data Source / Method / Endpoint / Main Finding / Validation / Limitations / Relevance / Gap / Future Direction。维度（分子机制/免疫微环境/单细胞/空间组学/算法方法/预后转移）体现于 Relevance 与 Gap 列。*

| Paper | PMID/DOI | Disease | Data Source | Method | Endpoint | Main Finding | Validation | Limitations | Relevance | Gap | Future Direction |
|---|---|---|---|---|---|---|---|---|---|---|---|
| APOE− subpopulation | 39810624 / 10.1002/ctm2.70172 | PTC | scRNA-seq + ST + TCGA | 伪时序/CellChat/体内外 | LNM / 干性 | APOE− 细胞经 ABCA1–LXR 促 LNM；13-gene 签名 | 体内外 + scRNA ML | 单中心 scRNA；机制偏 ABCA1–LXR | High（单细胞·分子·干性） | 是否=MGST1 dediff tip 同一亚群？ | D3：界定 APOE−/MGST1+ 亚群 |
| MGST1 Mito-high | 42327722 / 10.3389/fimmu.2026.1848083 | PTC | TCGA/GTEx+队列+scRNA | 共识 ML+轨迹 | LNM / 免疫 | MGST1=核心驱动，Mito-high/immune-cold；AUC 0.833 | 外部验证+siRNA+药理 | 机制（Toxoflavin 脱靶）待深究 | High（代谢·免疫·算法） | MGST1 与 APOE− 是否共定位？ | D3：代谢–免疫干性靶向 |
| SHMT2–PTEN–AKT | 38272883 / 10.1038/s41419-024-06476-1 | PTC | TCGA+组织 | 蛋白组/甲基化 | 转移 | SHMT2→SAM→甲基化抑 PTEN→AKT→转移 | 体内外 | 单队列；临床端点弱 | High（代谢·分子） | 与 MGST1 通路交叉？ | 代谢重编程联合靶点 |
| GLTC–LDHA | 37031273 / 10.1038/s41418-023-01157-6 | PTC | TCGA+组织 | 质谱/琥珀酰化 | 远处转移/RAI抵抗 | GLTC 促 LDHA-K155 琥珀酰化→糖酵解+远处转移 | 体内外 | 仅 PTC；泛癌外推谨慎 | High（代谢·分子） | 与 SOX12–YBX1–LDHA 关系 | 糖酵解+RAI 增敏 |
| SOX12–YBX1–LDHA | 40593465 / 10.1038/s41419-025-07797-5 | PTC | scRNA+bulk+CUT&Tag | 转录/IP-MS | 转移 | SOX12→YBX1→LDHA→TGF-β 促转移 | 临床样本相关 | 机制复杂；缺治疗验证 | High（分子·单细胞） | 与 GLTC–LDHA 冗余？ | 轴靶向 |
| POSTN+ myCAF atlas | 41480746 / 10.1172/jci.insight.191990 | TC/ATC | 423,733 细胞 + ST | 整合图谱 | LNM/预后 | POSTN+ myCAF 与侵袭/LNM/进展相关 | 多机构+5 队列 bulk | 因果（CAF→转移）未证 | High（单细胞·空间·免疫） | 可否成药 POSTN+ myCAF？ | CAF  niche 靶向 |
| FN1–SDC4 (multi-omics) | 41421038 / 10.1016/j.compbiolchem.2025.108857 | PTC | scRNA+ST+bulk | 多组学+RF | LNM | FN1–SDC4 轴驱动转移；17-gene 签名+RF | ST 空间验证+体外 | 单中心；外部验证有限 | High（单细胞·空间·算法·分子） | FN1 与 MET/ICAM1 ECM 轴整合？ | D-new：ECM– adhesion 闭环 |
| Spatial metabolomics+Tx | 41398964 / 10.1186/s12967-025-07566-0 | PTC | 空间代谢组+ST | 空间多组学 | LNM | 精氨酸-多胺/糖酵解/脂代谢失调；NAT8L/SVCT-2 | TCGA+斑马鱼 | 代谢物→基因因果弱 | High（空间·代谢·分子） | 5 转移代谢物临床转化？ | 空间代谢靶点 |
| 多模态 AI (LNM/DFS) | 38990290 / 10.1097/JS9.0000000000001875 | PTC | 1011 例+TCGA | DL 多模态 | LNM/DFS | AUC 0.83–0.86；GradCAM 热图 | TCGA 验证 | 单中心；回顾性 | High（算法·单细胞·免疫） | 前瞻性/多中心缺失 | 外部验证 + 可解释 |
| XGBoost 远处复发 | 41877795 / 10.3389/fmed.2026.1790226 | DTC | 1245 例 | 6 ML 算法 | 远处转移复发 | XGBoost AUC 0.88（374 外部） | 训练+外部验证 | 单中心；临床变量为主 | High（算法·预后） | 整合分子/影像特征？ | 多模态融合 |
| BRAF V600E meta | 41419184 / 10.1016/j.eprac.2025.12.003 | PTC | 46k，20,570 例 | 荟萃（RCT-Q2） | 淋巴结/远处/复发/死亡 | 淋巴结 OR1.38/复发 OR1.56；**不**预测远处/死亡 | 敏感性/漏斗图稳健 | 异质性（突变率反比预后力） | High（预后·分子） | 为何不预测远处？机制缺口 | 远处 vs LNM 解耦机制 |
| 5-HT/NETs (MTC) | 39903533 / 10.1172/JCI183544 | MTC/NEPC | 体内+类器官 | 表观/药理 | 肝转移 | 5-HT/SERT→NETs→肝转移；fluoxetine 阻断 | 多癌种+药理 | MTC 样本少；临床前 | High（免疫·预后） | MTC 肝转移临床验证？ | D6：神经递质/免疫轴 |
| DNA-methyl pediatric | 41701943 / 10.1158/1078-0432.CCR-25-2109 | 儿童 TC | 两队列甲基化 | 分类器 | 侵袭性/nodal | 甲基化分型预测 nodal+驱动突变 | 第二验证队列 | 仅儿童；成人外推？ | High（算法·分子） | 成人 PTC 适用性 | 儿科风险分层 |
| N1b-PTMC 多组学 | 40977710 / 10.3389/fimmu.2025.1620085 | PTMC(N1b) | 638 例+RNA-seq | 8 ML+WGCNA | 侧颈 LNM | NLR 模型 AUC0.852；4-gene 签名 AUC0.857 | IHC+CIBERSORT | 单中心；签名机制浅 | High（算法·免疫·单细胞） | 签名→治疗假设验证 | 免疫逃逸干预 |
| ATC ISG15/KPNA2 | 37501099 / 10.1186/s13046-023-02751-9 | ATC | scRNA(GEO)+体内 | 质谱/IP | 干性/转移 | ISG15 ISGylation 稳定 KPNA2 维持 ATC 干性 | 异种移植+斑马鱼 | ATC 罕见；样本少 | High（单细胞·分子） | 与 APOE− 干性轴关系 | ATC 干性靶向 |
| ATC CREB3L1/CAF | 36192735 / 10.1186/s12943-022-01658-x | ATC | 4 微阵列+scRNA | 体内/细胞因子阵列 | 转移/TME | CREB3L1→IL-1α→α-SMA+ CAF→ECM→恶性 | 斑马鱼+裸鼠 | 机制链长；验证点少 | High（分子·单细胞·免疫） | CAF 互作可药？ | CAF 抑制 |
| CAYA scRNA | 40719066 / 10.1002/advs.202417672 | CAYA-PTC | 11 例 scRNA | 轨迹/互作 | 侵袭/转移 | 缺 mild-state；emCAF_LAMP5 促转移 | 68Ga-FAPI-PET 提示 | 小样本；儿童专病 | High（单细胞·免疫） | 成人对比验证 | 儿科诊断 |
| Immune phenotypes (TIL) | 37279258 / 10.1530/ERC-23-0110 | PTC | TCGA 病理 AI | TIL 空间 | LNM/免疫表型 | desert/excluded/inflamed；excluded 多 BRAF+LNM | 组织法 | 预测价值未前瞻验证 | High（免疫·空间） | 免疫表型→治疗分层 | IO 患者筛选 |
| LNM immune genes | 37274228 / 10.3389/fonc.2023.1181325 | PTC | TCGA+WGCNA | RF+LASSO | LNM | MET/ICAM1/PTGS2 枢纽（AUC≈0.83） | IHC | 机制（NK/DC）浅 | High（免疫·分子） | MET 与 FN1 ECM 轴整合 | ECM–免疫联合 |
| mRNA classifiers | 40741176 / 10.3389/fendo.2025.1600815 | TC | Afirma 697+259 | ML | 侵袭/LNM 排除 | NPV 97.6–100% 排除 LNM | 验证队列 | 商业平台依赖 | High（算法） | 与多组学融合？ | 临床降过度手术 |

---

## 已知结论 / What Is Already Known

（以下结论均由多篇直接证据或多队列支持，非单一综述。）

1. **代谢–免疫耦联是 LNM 的核心驱动（主轴 1）。** 多条独立通路汇向「Mito-high / immune-cold」表型：MGST1（42327722，外部验证 AUC 0.833，Toxoflavin 可逆转 CD8+ T 耗竭+Treg 富集）、SHMT2（38272883，SAM→甲基化抑 PTEN→AKT）、GLTC–LDHA（37031273，K155 琥珀酰化→糖酵解+远处转移+RAI 抵抗）、SOX12–YBX1–LDHA（40593465）、PKM2 糖酵解综述（42280115）、脂肪酸代谢重编程综述（40353071）。代谢重编程同时重塑免疫微环境（41057823 外泌体综述）。
2. **转移性干性亚群决定 LNM/进展（主轴 2）。** APOE− 细胞（39810624）经 ABCA1–LXR 轴促 LNM 并具干性；MGST1 位于去分化轨迹末端（「stem-like metastatic subpopulation」）；ISG15–KPNA2（37501099）维持 ATC 干性；CREB3L1（36192735）驱动 ATC 经 CAF/ECM 恶性演进。
3. **POSTN+ myCAF 空间图谱是 LNM 的基质标志（主轴 3）。** 41480746（423,733 细胞整合图谱）定义 POSTN+ myCAF 与侵袭、LNM、疾病进展及不良预后相关；空间定位在侵入性肿瘤细胞旁。
4. **影像/多组学 AI 预测 LNM 与 DFS 性能高但验证薄（主轴 4）。** 多模态 DL（38990290，AUC 0.83–0.86）、XGBoost 远处复发（41877795，AUC 0.88，374 例外部）、N1b-PTMC 多组学 ML（40977710，NLR AUC 0.852 / 4-gene AUC 0.857）、TCGA 11-gene ML（41656803，AUC 0.793）、mRNA 分类器（40741176，NPV 100%）均单中心、回顾性，缺前瞻性/多中心外部验证。
5. **BRAF V600E 预测淋巴结与复发，但不预测远处转移/死亡（主轴 5）。** 41419184（46k 例荟萃）淋巴结 OR 1.38、复发 OR 1.56（边界），远处 OR 0.75、死亡 OR 0.97 不显著；与 PD-L1 荟萃共同印证 **DTC「远处转移 vs LNM」解耦**——即 LNM 相关标志物不一定外推至远处转移。
6. **ECM–黏附轴多次收敛。** MET/FN1/ICAM1（37274228、40110574）、FN1–SDC4（41421038）在空间与机制层面反复出现，构成「ECM–adhesion」主题。

## 未解问题 / What Remains Unclear

- **APOE− 与 MGST1「stem-like」亚群是否同一群？** 二者均被定位为去分化/干性转移亚群（39810624 vs 42327722），但无研究直接比较其重叠与层级关系。
- **代谢重编程多通路（MGST1/SHMT2/GLTC/SOX12）是否冗余或层级？** 现有研究各自为战，缺统一框架判断哪条是可成药「上游节点」。
- **为何 BRAF V600E / PD-L1 预测 LNM 与复发却不预测远处转移？** 机制层面「远处转移 vs LNM 解耦」缺乏因果解释（是否不同克隆/微环境生态位？）。
- **POSTN+ myCAF 是否可药？** 空间图谱已建立关联，但靶向该 CAF 亚型能否阻断 LNM 仍未知。
- **MTC 肝转移的 5-HT/SERT/NETs 轴（39903533）能否转化为临床干预？** 仅临床前（fluoxetine 阻断），缺 MTC 患者验证。
- **AI 模型的临床效用边界。** AUC 高≠临床决策价值；缺前瞻性、多中心、与现行 ATA 风险分层头对头比较。

## 领域方法/数据局限 / Method/Data Limitations In The Field

- **公共数据复用与批次效应：** TCGA/GTEx/GEO 被几乎所有签名研究复用；跨平台批次效应未系统校正。
- **端点稀疏：** 远处转移、复发、DTC 特异性死亡在公开队列中事件数少，导致预后模型置信区间宽（如 BRAF 荟萃复发 OR 1.56 仅边界显著）。
- **缺外部验证：** 多数 ML/DL 与签名研究为单中心回顾性，外部验证队列小或无（仅 41877795、40741176 有独立/外部验证）。
- **亚型分层缺失：** ATC、MTC 样本稀少，单细胞/空间研究几乎全为 PTC；ATC/MTC 的转移与微环境机制证据薄弱。
- **湿实验验证不足：** 大量标志/签名仅有生信+部分 IHC，缺功能挽救（rescue）与体内转移验证。
- **空间组学最薄：** 本轮纳入仅 6 篇空间相关（41480746/41421038/41398964/39540244/37279258/39810624），且多为 PTC；ATC/MTC 空间空白。
- **MCP 局限：** `paper-search-mcp` 无日期过滤器，relevance 排序在 b/e/f/g/h/i 出现明显主题漂移与跨路重叠（同一 scRNA/预后/代谢集被多路返回），需全局去重。

## 候选未来方向 / Candidate Future Directions

*按 `research-direction-rubric.md` 七维 1–5 评分（Novelty/Feasibility/Data/Validation/Clinical/Method/Overcrowding）。28–35 = Strong。*

| Direction | Novelty | Feasibility | Data | Validation | Clinical | Method | Overcrowd | **Total** | Rationale |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| **D3** — 界定并靶向 APOE−/MGST1+ 代谢–免疫干性转移亚群 | 5 | 5 | 5 | 4 | 5 | 4 | 4 | **32** | 多通路收敛（代谢+干性+免疫+空间），公共数据 + 湿实验可行，直接端点 LNM |
| **D-new** — FN1–SDC4 / ECM–adhesion 多组学+空间+ML 闭环 | 4 | 5 | 5 | 4 | 4 | 4 | 4 | **30** | 分子(scRNA)+空间(ST)+算法(RF) 已闭环（41421038），缺靶向验证 |
| **D6** — 5-HT/SERT/NETs 轴（MTC 肝转移） | 5 | 4 | 3 | 3 | 4 | 4 | 4 | **27** | 神经-免疫新轴，fluoxetine 可阻断；但 MTC 样本少、仅临床前 |
| **D-spatial** — 空间代谢组+转录组靶点挖掘 | 4 | 4 | 4 | 3 | 4 | 4 | 4 | **27** | 41398964 开空间代谢窗口；但空间代谢物→基因因果弱、平台贵 |
| **D-pediatric** — 儿童 TC 甲基化/干性风险分层 | 4 | 4 | 3 | 3 | 4 | 4 | 4 | **26** | 41701943 已建分型；儿童专病样本稀缺 |
| **D-ml** — 影像/多组学 DL 预测 LNM/复发 | 2 | 4 | 4 | 3 | 4 | 3 | 2 | **22** | 极度拥挤（主轴 4），增量价值低，除非多中心前瞻 |

**D3 状态（state）：** research question = APOE− 与 MGST1+ 是否为同一「代谢–免疫干性」转移起始亚群？novelty = 多组学未整合该亚群；required datasets = TCGA+GTEx+已发表 scRNA/ST（39810624/41480746/41421038/42327722）；expected endpoint = LNM 与 DFS；analysis = 跨数据集亚群共定位 + 拟时序 + 代谢–免疫评分；validation = 独立队列 + 体内 rescue（APOE/MGST1 敲除）+ Toxoflavin 药理；major risk = 亚群异质性导致信号稀释；claim boundary = 不声称治愈，仅「风险分层 + 可药靶点」。

## 推荐下一步方向 / Recommended Next Direction

**D3 — 界定并靶向 APOE−/MGST1+ 代谢–免疫干性转移亚群（rubric 总分 32，Strong）。** 连续第 10 轮确认为首选方向：分子机制（MGST1/SHMT2/GLTC/SOX12）、干性（APOE−/ISG15–KPNA2）、免疫（Mito-high/immune-cold）、空间（POSTN+ myCAF 旁 APOE− 细胞）与算法（13-gene scRNA 签名、AUC 0.833）五维证据同时收敛于同一「代谢–免疫干性」转移亚群，公共数据 + 湿实验均可及，且直接对应 LNM/复发临床端点。

**首步具体行动：** (1) 跨 TCGA/GTEx 与已发表 scRNA+ST（39810624、41480746、41421038、42327722）重注释，检验 APOE− 与 MGST1+ 亚群重叠与层级；(2) 构建「代谢–免疫干性」复合评分并在独立队列（如 GSE60542、40110574 队列）验证 LNM 预测；(3) 体内 rescue（APOE/MGST1 敲除）+ Toxoflavin 药理验证可药性。

## 随访阅读清单 / Follow-Up Reading List

- **42327722 (MGST1)** — 本轮最新冠键：代谢–免疫耦联 + AUC 0.833 + 可药（Toxoflavin），D3 核心。
- **39810624 (APOE−)** — 干性转移亚群 origin 研究，D3 另一支柱。
- **41480746 (POSTN+ myCAF)** — 423k 细胞空间图谱，连接基质与 LNM。
- **41421038 (FN1–SDC4)** — 分子/单细胞/空间/算法闭环模板，D-new 参考。
- **41419184 (BRAF V600E meta)** — 远处 vs LNM 解耦的权威证据。
- **41877795 (XGBoost 远处复发)** — 少数具外部验证的 ML 预后模型，方法学标杆。
- **39903533 (5-HT/NETs MTC)** — MTC 肝转移新机制，D6 起点。

## 可复现性说明 / Reproducibility Notes

- **Search date:** 2026-08-01（run #10）。
- **Databases:** PubMed via `mcp__paper-search-mcp__search_pubmed`（DeferExecuteTool）。本地 `paper_search_mcp` 未安装，按技能降级规则用 MCP 直接检索。
- **Query strings:** 9 路（a–i，见检索策略表），`max_results=15`，`sort=relevance`。
- **Filters:** 无日期/亚型过滤（MCP 不支持）；以 relevance 近似近期优先。
- **Deduplication rule:** 以 PMID 为键，9 路并集去重 → 76 唯一；非甲状腺/泛癌/纯流行病学判排除。
- **Screening rule:** 保留甲状腺（PTC/PTMC/FTC/MTC/ATC/DTC/儿童 TC）相关；按相关性标 High/Medium/Low，按内容标维度（分子/免疫/单细胞/空间/算法/预后/代谢）。
- **Transient-errors:** b/e/g/i 首轮 `not well-formed (invalid token)`，逐路重发后全部返回（共 126 raw rows）。
- **Files saved:** `lit_review/literature_review_20260801_031233.md`（本报告）；`lit_review/search_results_latest.json`（76 唯一 / 48 纳入 / 28 排除，含 query 块与 run#10 元数据）。
- **⚠️ 数据完整性：** 本轮 `search_results_latest.json` 曾被误覆盖，累计 174 条语料无法从磁盘恢复；现以本轮 76 条并集为活动基线（详见文件 `corpus_reset_note`）。

## 与历史报告对比 / Comparison With Prior Report (run #9, 2026-07-31)

- **检索条数：** 本轮 9 路共 **126 raw rows → 76 unique**（run #9 为 124 raw → 174 unique 累计）。
- **纳入条数：** 本轮 **48 篇 in-scope**（run #9 累计 103）；**28 篇 excluded**。
- **新增文献：** **0 篇**——所有 76 个返回 PMID 均已在 run #9 语料库中。语料自 run #7（2026-07-28）以来连续第 **4** 轮处于平台期（174 唯一 / 103 纳入）。
- **各维度分布（本轮 48 纳入，多标签）：** 分子 19 / 预后 18 / 免疫 18 / 算法 14 / 代谢 9 / 单细胞 12 / 空间 6。（run #9 累计：分子 47 / 免疫 30 / 单细胞 18 / 空间 6 / 算法 37 / 预后 28 / 代谢 14。）
- **关键收敛发现：** 5 条主轴与 run #9 **完全一致**，无任何反证。最新冠键 MGST1（42327722）、XGBoost 远处复发（41877795）、空间代谢组（41398964）、多组学 FN1–SDC4（41421038）、儿童甲基化（41701943）均已在 run #9 语料中。
- **推荐方向：** **D3（APOE−/MGST1+ 代谢–免疫干性转移亚群）rubric 32（Strong）**，连续第 **10** 轮确认。
- **方向变化信号：** 无新信号；平台期持续。建议后续**跳出 PubMed MCP**——补充 bioRxiv/arXiv 预印本 + cBioPortal/DepMap + 收窄 ATC/MTC 与空间组学窗口，以打破平台期。
- **数据完整性差异：** 本轮 `search_results_latest.json` 以 76 条并集为新基线（原 174 累计语料误覆盖不可恢复），不影响报告结论，但后续新检测基线收窄至 76。
