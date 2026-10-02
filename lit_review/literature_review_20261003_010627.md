# 甲状腺癌文献监测报告 Run #27 / Literature Review: Thyroid Carcinoma — Invasion, LNM & Distant Metastasis, Recurrence, Prognosis, and Molecular / Immune-Microenvironment / Single-Cell / Spatial / ML Axes

**Date / 检索日期**: 2026-10-03
**Run ID**: #27　**Timestamp (TS)**: `20261003_010627`
**Sources / 检索源**: OpenAlex（主通道）, Europe PMC（第二通道，本轮扩至 10 路）, 定向基因深挖（第三通道，27 基因面板）, Crossref（元数据校验）, Unpaywall（OA 解析）
**Search window / 检索窗口**: 2026-09-03 起（30 d）/ 2026-07-05 起（90 d）/ Europe PMC `PUB_YEAR:2026` / 深挖 2026-06-01 起
**Baseline / 基线**: `search_results_latest.json` (Run #26, 391 条) → 本轮 **457 条**

---

## 中文摘要 / Executive Summary (ZH)

本轮为 Run #27，与上轮（Run #26，2026-10-02）仅相隔 1 天。四通道并行检索共取回并去重后获得 **66 条唯一新增文献**（OpenAlex 9 / Europe PMC 56 / 定向深挖 1），其中 **High 12 / Medium 39 / Low 15**，**严格预印本 0 条**。累积基线由 391 条增至 **457 条**。

**方法学要点**：本轮 Europe PMC 由 6 路扩至 **10 路**（新增 `MO` 分子机制、`PR` 预后转移、`MACRO2`、`SPATIAL_DS` 四路）。这一改动单轮即回补 56 条，占本轮新增的 85%，且绝大多数为 2026 年 1–8 月的**历史欠采样回填**，而非窗口内新发。这是**连续第三轮**证明：本监测序列此前的"低新增"主要是**通道性欠采样**，而非领域真实平台期。

**三个最强新信号**：

1. ⭐⭐⭐ **载脂蛋白家族（APOC1/APOA1/APOE）在 PTC 中形成三证据独立收敛的脂代谢–免疫轴**。APOC1 跨队列 VLDL 通路 signature（TCGA-THCA n=209 + 3 个 GEO 队列 + XGBoost-SHAP + 233 项代谢标志物孟德尔随机化，PMID 42742374）、APOC1 作为治疗靶点联合 cyclopamine（PMID 41289702）、H3K27ac 激活 APOC1 促 PTC 增殖（PMID 42597226）。**新立 D21（载脂蛋白–脂代谢–免疫轴，rubric 29）**。
2. ⭐⭐ **TAM 极化由四通路扩张为五通路**：HN1/CEBPB/CCL2 轴经 CCR2/PI3K/AKT 塑造 **VSIG4⁺ TAM**，CCL2 与 VSIG4 双阻断在小鼠体内协同抑瘤（PMID 42191099，ATC）。这是本轮机制链条最完整的原发证据。
3. ⭐⭐ **两条"红分化/耐药"机制达准因果**：NOX4 源性氧化 DNA 损伤经 OGG1/MSH2-MSH6/DNMT1 阻断 PAX8、NKX2.1 染色质结合而沉默 NIS（PMID 41694580）；CRISPR 双筛发现 TAZ/WWTR1 缺失与 BRAF 抑制剂合成致死，机制为抑制 UPR 并触发 ferroptosis（PMID 42035477）。

**持续跟踪方向 D3″（APOE×MGST1 双轴）状态：无变化，且"结构性空白"判定进一步坐实。** 量化事实：OpenAlex 全库 `APOE`×`MGST1`×`thyroid` 三词共现仍 **= 0**；MGST1 2026 年甲状腺癌文献仍**仅 1 篇**（10.3389/fimmu.2026.1848083），本轮零增长（连续第 27 轮）。同时 APOE 侧 2026 年文献已达 20 篇、APOC1 侧 5 篇 —— 载脂蛋白家族中真正可操作的节点是 **APOC1/APOA1 而非 MGST1**。建议按 Run #26 预设，将 D3″ 由「候选方向」降级，其价值并入 D21。

**首选下一步**：D21 × D9 合并 —— 以 APOC1/APOA1/APOE 载脂蛋白签名与 SPP1⁺/APOC1⁺/VSIG4⁺ TAM 做空间耦合分析，零湿实验起步。

---

## English Abstract

Run #27 executed 1 day after Run #26. Four parallel channels yielded **66 de-duplicated new records** (OpenAlex 9 / Europe PMC 56 / targeted gene deep-dig 1): **High 12 / Medium 39 / Low 15**, with **zero strict preprints**. The cumulative baseline grew from 391 to **457 records**.

**Methodological note.** Europe PMC was expanded from 6 to **10 query routes** (adding `MO` molecular mechanism, `PR` prognosis, `MACRO2`, `SPATIAL_DS`). This single change recovered 56 records — 85% of this run's yield — overwhelmingly as **backfill of previously under-sampled 2026 Jan–Aug literature**, not as new in-window output. This is the **third consecutive run** showing that prior "low-yield" rounds reflected **channel under-sampling**, not a genuine field plateau.

**Three strongest new signals.**

1. ⭐⭐⭐ **The apolipoprotein family (APOC1/APOA1/APOE) converges as a lipid–immune axis in PTC with three independent lines of evidence**: a cross-cohort APOC1/VLDL transcriptomic signature (TCGA-THCA n=209 + 3 GEO cohorts + XGBoost-SHAP + Mendelian randomization over 233 metabolic biomarkers; PMID 42742374); APOC1 as a druggable target sensitized by cyclopamine (PMID 41289702); H3K27ac-driven APOC1 promoting PTC proliferation (PMID 42597226). **New direction D21 (rubric 29).**
2. ⭐⭐ **TAM polarization expands from four to five signaling nodes**: the HN1/CEBPB/CCL2 axis shapes **VSIG4⁺ TAMs** via CCR2/PI3K/AKT, and combined CCL2 + VSIG4 blockade synergistically suppresses ATC tumor growth in vivo (PMID 42191099). The most complete causal chain in this run.
3. ⭐⭐ **Two redifferentiation/resistance mechanisms reach near-causal status**: NOX4-derived oxidative DNA damage silences NIS by blocking PAX8/NKX2.1 chromatin occupancy through OGG1/MSH2-MSH6/DNMT1 (PMID 41694580); parallel CRISPR KO/activation screens identify TAZ/WWTR1 loss as synthetically lethal with BRAF inhibition, acting by repressing the UPR and triggering ferroptosis (PMID 42035477).

**Standing tracked direction D3″ (APOE × MGST1 dual axis): unchanged, with the "structural gap" verdict now further consolidated.** OpenAlex full-corpus `APOE`×`MGST1`×`thyroid` co-occurrence remains **0**; MGST1 thyroid-cancer papers in 2026 remain **1** (10.3389/fimmu.2026.1848083), zero growth for the 27th consecutive run. Meanwhile APOE-side 2026 output has reached 20 papers and APOC1-side 5 — the actionable nodes in the apolipoprotein family are **APOC1/APOA1, not MGST1**. Per the Run #26 pre-set rule, D3″ should be demoted from "candidate direction" and its residual value folded into D21.

**Recommended next step.** Merge D21 × D9: spatially couple the APOC1/APOA1/APOE apolipoprotein signature with SPP1⁺/APOC1⁺/VSIG4⁺ TAM niches, starting with zero wet-lab work.

---

## 一、检索策略 / Search Strategy

| Source / 通道 | Query / 查询 | Filters / 过滤 | Results / 命中 | Notes / 说明 |
|---|---|---|---:|---|
| OpenAlex 九路 `a`–`i` | `oa_search.py` 内建布尔矩阵（分子机制 / 算法方法 / 免疫微环境 / 单细胞 / 空间组学 / 预后转移 / 转移干性 / 代谢重编程） | `from_publication_date:2026-09-03`，`per-page=25`，`sort=publication_date:desc` | 唯一 87 / 在范围 61 / 剔除 26 | 相对基线新增 **6** |
| OpenAlex 九路（90 d 补跑） | 同上 | `from_publication_date:2026-07-05`，`per-page=50` | 唯一 241 / 在范围 169 / 剔除 72 | 相对基线新增 **9**（含 30 d 部分） |
| Europe PMC（10 路） | `SC/SP/IM/ME/AL/ST` + **新增 `MO`/`PR`/`MACRO2`/`SPATIAL_DS`** | `PUB_YEAR:2026`，`sort=P_PDATE_D desc`，`pageSize=50` | 候选 139 → 人工筛入 **56** | 本轮主贡献通道 |
| 定向基因深挖（27 基因） | OpenAlex `title_and_abstract.search:{GENE}` × `thyroid` | `from_publication_date:2026-06-01`，`per-page=25` | 候选 11 → 筛入 **1** | 新增 VSIG4/APOC1/HN1/CCL2 |
| Crossref | `api.crossref.org/works/{doi}` | 22 条 High | **22/22 成功** | DOI 元数据校验 |
| Unpaywall | `api.unpaywall.org/v2/{doi}` | 22 条 High | **22/22 成功** | OA 状态权威源 |
| NCBI eutils / PubMed | — | — | 未使用 | **本机不可达（HTTP 000），禁止直连重试** |
| paper-search-mcp | — | — | 未调用 | 本会话未连接 |

**剔除规则 / Exclusion rules**：① 标题未点名甲状腺（30 d 剔除 23、90 d 剔除 61）；② 非肿瘤主题（甲状腺良性/自身免疫病，30 d 3 条、90 d 11 条）；③ `Retraction notice to` / `Correction:` / `Erratum:` / `ASO Visual Abstract:` / `Supplementary Table|Figure` 前缀自动降档（本轮剔除 6 条）；④ Graves 病 / 桥本甲状腺炎 / Thyroid Eye Disease（TED）中提及 SPP1⁺ 巨噬细胞或 APOC1 者列为**边界条目**，不计入 TC 机制证据（本轮 2 条：10.1016/j.clim.2026.110712、10.1016/j.molimm.2026.04.005，后者按 Low 保留为边界标记）。

**去重规则 / Deduplication**：DOI 主键（小写、剥离 `https://doi.org/`）→ 标题归一化（仅保留字母数字，截断 90 字符）→ 多版本合并（30 d 合并 30 组、90 d 合并 62 组）。

**通道健康度 / Channel health**：OpenAlex ✅、Europe PMC ✅、Crossref ✅、Unpaywall ✅（Run #22 的 SSL 握手超时本轮未复现）。

---

## 二、纳入论文（High 相关性，12 条）/ Included Papers — High Relevance

> 标题与摘要保留英文原文；每条附一句话中文要点。PMID 缺失者标注「待编目」，**不得编造**。

**1. HN1/CEBPB/CCL2 signaling shapes VSIG4⁺ tumor-associated macrophages in anaplastic thyroid carcinoma.**
*Biochim Biophys Acta Mol Basis Dis*, 2026-05-25. PMID: 42191099. DOI: 10.1016/j.bbadis.2026.168303. OA: closed.
- Author claim: CCL2 is highly expressed in ATC cells and promotes VSIG4⁺ macrophage differentiation; HN1 binds CEBPB to prevent its ubiquitination and degradation, driving CCL2 transcription; the axis acts through CCR2/PI3K/AKT; combined CCL2 + VSIG4 blockade synergistically slows subcutaneous tumor growth and remodels the immunosuppressive ATC microenvironment.
- 中文要点：HN1 稳定 CEBPB → 转录 CCL2 → CCR2/PI3K/AKT → VSIG4⁺ TAM 分化；双靶点阻断体内协同。
- Agent note: 本轮机制链条最完整的原发证据（细胞因子芯片筛选 + 共培养验证 + 中和抗体 + 敲低 + 体内成瘤）。局限：VSIG4⁺ TAM 的免疫抑制功能在人 ATC 组织层面仅有浸润描述，缺少空间共定位与临床结局关联。

**2. APOC1-Associated VLDL-Pathway Dysregulation in Papillary Thyroid Carcinoma: A Reproducible Cross-Cohort Transcriptomic Signature Associated With the Diagnostic-to-Treatment Interval.**
*Chem Biol Drug Des*, 2026-09-01. PMID: 42742374. DOI: 10.1111/cbdd.70403. OA: hybrid.
- Author claim: A 77-day DTI threshold optimally stratified complete response (91.5% for ≤77 d vs 79.0% for >77 d; p=0.035); 77 DTI-associated genes enriched in PPAR signaling, fat digestion and apolipoprotein particle dynamics; longer DTI associated with higher APOA1 and APOC1; XGBoost-SHAP ranked APOA1/APOC1 top; APOC1 and LPL consistently up, VLDLR down across GSE29265/GSE33630/GSE60542; two-sample MR over 233 metabolic biomarkers.
- 中文要点：诊断—治疗间隔 >77 天与完全缓解率下降相关，APOA1/APOC1 为最强预测特征，跨三队列可复现，并经 MR 支持因果方向。
- Agent note: 四阶段设计（TCGA 发现 → 3 个 GEO 验证 → XGBoost-SHAP → MR）是本月方法学最完整的生信研究之一。**重要限定**：此处 APOC1/APOA1 是 bulk 转录组层面，不区分细胞区室（髓系 vs 上皮），不可直接等同于 Run #26 iScience 的髓系 Macro2（SPP1+APOC1+APOE） signature。

**3. Apolipoprotein C1 functions as a target of thyroid carcinoma and synergistic effects with promising candidate-cyclopamine.**
*Transl Oncol*, 2025-11-24. PMID: 41289702. DOI: 10.1016/j.tranon.2025.102617. OA: gold.
- Author claim: APOC1 overexpressed in PTC and associated with poorer prognosis and immune-evasion signatures; promotes proliferation, colony survival, apoptosis resistance; CMap nominated cyclopamine; APOC1 depletion sensitizes cells to cyclopamine; cyclopamine suppresses tumor growth in a PTC mouse model.
- 中文要点：APOC1 驱动 PTC 进展与免疫逃逸，环巴明经 CMap 提名并在体外/体内验证。
- Agent note: 提供可药化切口（cyclopamine 为 Hedgehog/SMO 抑制剂，机制连接较间接，作者自述 "acts, at least in part, through APOC1-related signaling"）。

**4. NOX4-derived oxidative DNA damage impairs thyroid differentiation through an epigenetic mechanism in BRAF-mutated radioactive iodine refractory papillary thyroid cancer cells.**
*Int J Biol Sci*, 2026-01-15. PMID: 41694580. DOI: 10.7150/ijbs.123980. OA: gold.
- Author claim: NOX4-generated oxidative DNA damage recruits OGG1 and MSH2/MSH6 which, with DNMT1, convert lesions into transcription-blocking events, preventing PAX8/NKX2.1 from accessing chromatin and silencing NIS; combined MAPK + TGF-β1 inhibition restores PAX8/NKX2.1 occupancy.
- 中文要点：NOX4–ROS–OGG1/MSH2-MSH6–DNMT1 轴表观沉默 NIS；MAPK + TGF-β1 双抑制可逆转。
- Agent note: 为 RAI 难治的"红分化"策略提供了明确的表观机制与可检验的组合用药假设。局限：细胞系为主，人组织层面为免疫组化相关性。

**5. CRISPR-Based Gene Dependency Screens Reveal Mechanism of BRAF Inhibitor Resistance in Anaplastic Thyroid Cancer.**
*Mol Carcinog*, 2026-04-26. PMID: 42035477. DOI: 10.1002/mc.70122. OA: hybrid.
- Author claim: Parallel CRISPR/KO and CRISPR/activation screens identified TAZ (WWTR1) deficiency as synthetically lethal with BRAF inhibition in ATC; TAZ loss represses the UPR, reverses protein-synthesis inhibition, and increases ferroptotic cell death under dabrafenib.
- 中文要点：TAZ 缺失与 BRAF 抑制剂合成致死；机制为抑制 UPR 并转向 ferroptosis。
- Agent note: 双向 CRISPR 筛（KO + activation）设计严谨；把 Hippo/TAZ、UPR、ferroptosis 三条线接到一起，是 D12（铁死亡）在甲状腺特异层面迄今最硬的证据。

**6. Acquired Driver Fusions as a Mechanism of Resistance to Selective RET Inhibitors in Advanced Medullary Thyroid Carcinoma.**
*JCO Precis Oncol*, 2026-02-20. PMID: 41719512. DOI: 10.1200/po-24-00900. OA: closed.
- Author claim: Acquired driver fusions emerge as a resistance mechanism to selective RET inhibitors in advanced MTC.
- 中文要点：获得性驱动融合是选择性 RET 抑制剂耐药的新机制（MTC）。
- Agent note: 摘要正文在 EPMC 未返回，仅标题级信息，证据强度据此降档；但主题与 D16（MTC 远处转移/耐药）高度契合，值得全文追踪。

**7. Compartment-Specific Recurrence in Medullary Thyroid Cancer.**
*JAMA Otolaryngol Head Neck Surg*, 2026-09-03. PMID: 42690646. DOI: 10.1001/jamaoto.2026.2597. OA: green (repository).
- Author claim: Multicenter retrospective cohort of 235 adults with MTC undergoing thyroidectomy (1998–2021) across 4 academic referral centers; recurrence categorized as biochemical (calcitonin >2 pg/mL), ipsilateral/contralateral central and lateral neck, and distant; multivariable Cox for contralateral neck and overall recurrence.
- 中文要点：235 例 MTC 四中心队列，按解剖分区刻画复发模式，评估对侧预防性中央区清扫的价值。
- Agent note: 期刊级别与样本量在本轮预后类文献中最高；直接关系 MTC 手术范围决策（D16）。

**8. Prognostic Stratification of Brain Metastases from Nonanaplastic Follicular Cell-Derived Thyroid Carcinoma: Results of an International Multicenter Retrospective Study.**
*Thyroid*, 2026-08-03. PMID: 42545312. DOI: 10.1177/10507256261473771. OA: closed.
- Author claim: 189 adults across 19 tertiary centers; median PFS 7.0 mo, median OS 15.0 mo; independent predictors of shorter OS: age >75, ECOG ≥2, papillary histology, extracranial metastases, ≥4 BM; a disease-specific GPA stratified four groups with median OS 72.6 → 3.7 months; exploratory SEER assessment consistent.
- 中文要点：非 ATC 甲状腺癌脑转移首个疾病特异性 GPA 评分，国际 19 中心 189 例 + SEER 探索验证。
- Agent note: 远处转移（脑）领域稀缺的高质量证据；"papillary histology" 为不良因素反直觉，值得复核是否为混杂。

**9. Ruminococcaceae promotes the NLRP3/ASC/Caspase-1 axis-mediated pyroptotic signaling in papillary thyroid carcinoma by upregulating RBM15 to increase the N⁶-methyladenosine methylation modulation of NLRP3.**
*Naunyn-Schmiedeberg's Arch Pharmacol*, 2026-02-02. PMID: 41627386. DOI: 10.1007/s00210-026-05025-1. OA: closed.
- Author claim: Rum upregulates RBM15 in BCPAP and KTC-1 cells, decreases viability, promotes pyroptotic signaling, inhibits invasion/migration, reduces tumor volume/weight in vivo; downregulates MMP2/MMP9 and upregulates IFN-γ, IL-1β, IL-18, NLRP3/ASC/Caspase-1 and NLRP3 m6A; RBM15 knockdown reverses all effects.
- 中文要点：肠道菌 Ruminococcaceae → RBM15 → NLRP3 m6A 甲基化 → 焦亡，体外 + 体内双向验证。
- Agent note: **D17（肠道/瘤内微生物群）首次获得机制层（而非仅 MR 关联）证据**。注意方向与 Run #26 的 *Terrisporobacter*→NTRK1 免疫抑制相反 —— 本条为抑瘤方向，提示菌群效应具菌株特异性，不可一概而论。

**10. Characterizing risk groups in papillary thyroid carcinoma through T-Cell mediated tumor cell killing-related genes: a pathway to therapeutic predictions.**
*Eur Arch Otorhinolaryngol*, 2026-07-27. PMID: 42507215. DOI: 10.1007/s00405-026-10470-y. OA: closed.
- Author claim: Five TTK-related genes (B3GLCT, EPS15L1, FGFR4, P2RY11, PSORS1C1) form a prognostic model with robust ROC performance; PSORS1C1 knockdown represses malignant progression under PRDM10 transcriptional regulation (ChIP-qPCR verified); stratification independent of immune-infiltration abundance.
- 中文要点：基于"肿瘤细胞对 T 细胞杀伤的内在敏感性"基因建模，风险分层不依赖免疫浸润丰度。
- Agent note: 概念新颖（内在杀伤敏感性 vs 浸润丰度），但五基因模型无外部队列验证，且 FGFR4 的"敏感性基因"定位需谨慎。

**11. Development and Validation of a Picture Archiving and Communication System-Integrated Artificial Intelligence for Predicting Cervical Lymph Node Metastasis in Papillary Thyroid Carcinoma.**
*J Imaging Inform Med*, 2026-09-18. PMID: 42760456. DOI: 10.1007/s10278-026-02275-6. OA: hybrid.
- Author claim: CT from 710 patients (4942 LNs), two centers; 3D TransUNet partition + Swin UNETR segmentation + 3D U-Net classification integrated into PACS; partition precision 0.919–0.990 (internal) / 0.848–1.000 (external); segmentation DSC 0.674/0.633; classification AUC 0.948 internal / **0.943 external**; reader study (202 patients/202 LNs) showed the model outperformed and significantly improved junior radiologists (p<0.05).
- 中文要点：PACS 内嵌的三段式 3D 深度学习流水线，外部验证 AUC 0.943，并有真实阅片者研究。
- Agent note: 本轮算法维度方法学最完整者（多中心 + 外部验证 + reader study + 工程落地）。局限：分割 DSC 仅 0.63–0.67 是明显短板；回顾性设计。

**12. Association of TP53 Mutational Status and Survival in Anaplastic Thyroid Cancer Treated with Dabrafenib Plus Trametinib.**
*Eur Thyroid J*, 2026-10-01. PMID: 42820284. DOI: 10.1530/etj-26-0135. OA: gold.
- Author claim: 25 BRAF-positive ATC patients treated 2018–2026; TP53 mutations (10 patients) associated with significantly lower OS (6.5 vs 21 months; p<0.01), with trends to shorter PFS (7 vs 19 mo; p=0.09) and DoR (5.5 vs 9 mo; p=0.09); four BRAF^V600E^ cell lines provided mechanistic support (TP53-mutant cells less sensitive to DT).
- 中文要点：TP53 突变是 BRAF^V600E^ ATC 接受达拉非尼+曲美替尼的不良预后因素（OS 6.5 vs 21 月），并有细胞系佐证。
- Agent note: 本轮**最新**（2026-10-01）且临床决策相关度最高的文献。n=25 单中心，PFS/DoR 仅达趋势，需独立队列复核。

---

## 三、证据矩阵 / Evidence Matrix

> 维度（Dim）：MO 分子机制 / IM 免疫微环境 / SC 单细胞 / SP 空间组学 / AL 算法方法 / PR 预后转移 / ST 转移干性 / ME 代谢重编程
> 相关性（Rel）：High / Medium / Low　预印本（Pre）：本轮严格预印本 = 0，故全列为否（N）
> OA：gold / green / hybrid / closed（Unpaywall 为权威源；EPMC `isOpenAccess` 为辅）

| # | Paper | PMID / DOI | Dim | Rel | Pre | OA | Disease / Population | Data Source | Method | Endpoint | Main Finding | Validation | Limitations | Gap Suggested | Future Direction |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | HN1/CEBPB/CCL2→VSIG4⁺ TAM | 42191099 / 10.1016/j.bbadis.2026.168303 | IM, MO | High | N | closed | ATC | 细胞系 + 小鼠皮下成瘤 | 细胞因子芯片 + 共培养 + 中和抗体 + 敲低 | TAM 极化 / 成瘤 | HN1 稳定 CEBPB→CCL2→CCR2/PI3K/AKT→VSIG4⁺ TAM | 体内成瘤 +  rescue | 人组织无空间定位；无临床结局 | VSIG4⁺ TAM 在人 ATC 的空间生态位 | D9：VSIG4⁺ × SPP1⁺ 共定位 |
| 2 | APOC1 VLDL × DTI | 42742374 / 10.1111/cbdd.70403 | ME, IM | High | N | hybrid | PTC | TCGA-THCA n=209 + GSE29265/33630/60542 | 差异表达 + XGBoost-SHAP + 两样本 MR | 完全缓解 / DTI | 77 d 阈值分层 CR 91.5% vs 79.0%；APOA1/APOC1 为 SHAP 首特征 | 三独立 GEO 队列 + MR | bulk 层面，区室未分；DTI 为行政变量 | APOC1 的细胞来源（髓系 vs 上皮） | D21：区室解析的载脂蛋白轴 |
| 3 | APOC1 + cyclopamine | 41289702 / 10.1016/j.tranon.2025.102617 | ME, MO | High | N | gold | PTC | TCGA-THCA + 细胞系 + 小鼠 | CMap 提名 + 增殖/克隆/凋亡 + 异种移植 | 增殖 / 凋亡 / 成瘤 | APOC1 高表达预后差且与免疫逃逸签名相关；环巴明体内抑瘤 | 体内异种移植 | CMap 提名机制间接 | APOC1 上游调控与下游效应子 | D21：APOC1 干预组合筛选 |
| 4 | NOX4→NIS 表观沉默 | 41694580 / 10.7150/ijbs.123980 | MO, ST | High | N | gold | BRAF^V600E^ RAI 难治 PTC | 细胞系 + 人 RAI-R 肿瘤组织 | ROS/损伤修复 + ChIP + 报告基因 | NIS 表达 / 红分化 | NOX4–OGG1/MSH2-MSH6–DNMT1 阻断 PAX8/NKX2.1 结合 | MAPK+TGF-β1 双抑制逆转 | 以细胞系为主；人组织为相关性 | 临床红分化方案中的验证 | D18：红分化联合策略 |
| 5 | CRISPR TAZ/WWTR1 | 42035477 / 10.1002/mc.70122 | ME, MO | High | N | hybrid | ATC | CRISPR KO + CRISPRa 双筛 + 细胞系 | 合成致死筛 + UPR/蛋白合成/ferroptosis | BRAFi 耐药 | TAZ 缺失与 BRAFi 合成致死；抑制 UPR → ferroptosis | 双向 CRISPR 筛 + 基因必要性评分交叉 | 无体内与患者队列 | TAZ 抑制剂的体内可行性 | D12：Hippo–UPR–ferroptosis 三联 |
| 6 | RET 抑制剂获得性融合 | 41719512 / 10.1200/po-24-00900 | MO, PR | High | N | closed | 晚期 MTC | 临床队列 | 基因组测序 | 耐药机制 | 获得性驱动融合介导选择性 RET 抑制剂耐药 | 仅标题级可得 | 摘要缺失，证据降档 | 融合谱与后续治疗选择 | D16：MTC 耐药克隆演化 |
| 7 | MTC 分区复发 | 42690646 / 10.1001/jamaoto.2026.2597 | PR | High | N | green | MTC | 4 中心 235 例（1998–2021） | 多中心回顾 + Cox | 分区复发 / 生化复发 | 量化对侧中央区 pCND 与分区复发的关系 | 多中心大样本 | 回顾性；手术跨度 23 年 | 分子标志物叠加 | D16：MTC 手术范围 + 分子分层 |
| 8 | 非 ATC 脑转移 GPA | 42545312 / 10.1177/10507256261473771 | PR | High | N | closed | 非 ATC FCDTC 脑转移 | 国际 19 中心 189 例 + SEER | Cox + GPA 构建 | OS / PFS | 首个疾病特异性 GPA，四组 OS 72.6→3.7 月 | SEER 探索验证 | 回顾性；"乳头状组织学"为不良因素反直觉 | 分子分层纳入 GPA | D16 扩展：远处转移预后工具 |
| 9 | Ruminococcaceae→m6A→焦亡 | 41627386 / 10.1007/s00210-026-05025-1 | MO, ME | High | N | closed | PTC | BCPAP/KTC-1 + 小鼠 | 菌群干预 + m6A 检测 + 体内成瘤 | 焦亡 / 成瘤 | Rum→RBM15→NLRP3 m6A→焦亡，RBM15 敲低可逆转 | 体内 + rescue | 单一菌株；口服/定植方式未详 | 菌株特异性与临床可转化性 | D17：菌株级机制与队列验证 |
| 10 | GSTTK T 细胞杀伤基因 | 42507215 / 10.1007/s00405-026-10470-y | IM, AL | High | N | closed | PTC | TCGA + 细胞实验 | 回归建模 + ChIP-qPCR | 风险分层 | 五基因模型；PRDM10/PSORS1C1 轴经 ChIP 验证 | 细胞实验 | 无外部队列；FGFR4 定位存疑 | 与免疫浸润解耦的生物学含义 | D8 扩展：内在杀伤敏感性 |
| 11 | PACS-AI 宫颈 LNM | 42760456 / 10.1007/s10278-026-02275-6 | AL, PR | High | N | hybrid | PTC | 2 中心 710 例 / 4942 淋巴结 | 3D TransUNet + Swin UNETR + 3D U-Net | LNM 转移风险 | 外部 AUC 0.943；提升低年资医师诊断 | 外部测试集 + reader study | 分割 DSC 0.63–0.67；回顾性 | 前瞻性与多民族外推 | D13：可落地临床 AI 与校准漂移 |
| 12 | TP53 × 达拉+曲美（ATC） | 42820284 / 10.1530/etj-26-0135 | PR | High | N | gold | BRAF^V600E^ ATC | 25 例 + 4 株细胞系 | RECIST 1.1 + Cox + 体外 | OS / PFS / DoR | TP53 突变 OS 6.5 vs 21 月（p<0.01） | 细胞系机制佐证 | n=25 单中心；PFS 仅趋势 | 独立队列与联合策略 | D15：ATC 精准分层 |
| 13 | MYOF→PINK1/Parkin 线粒体自噬 | 42271528 / 10.1002/kjm2.70245 | ME, MO | Med | N | gold | PTC | 3 配对组织 + TPC-1/KTC-1 + 异种移植 | shRNA + 线粒体自噬流 + 体内 | 增殖/侵袭/成瘤 | MYOF 抑制线粒体自噬驱动 PTC；敲低激活 BNIP3/NIX | 异种移植 | 配对组织仅 3 例 | 与 APOE–PINK1 轴的关系 | D21：PINK1 节点交叉验证 |
| 14 | POSTN→mTOR/AKT | 42305478 / 10.21037/tcr-2025-aw-2452 | MO | Med | N | gold | PTC | TCGA + 30 例患者血清/组织 | ELISA/IHC/qPCR/WB + Transwell | 增殖/迁移 | POSTN 在 PTC 与血清中升高，晚期更高 | 患者样本验证 | 样本量小；无预后随访 | POSTN 与 CAF 亚群的关系 | D9 扩展：基质-免疫耦合 |
| 15 | TRMT6/TRMT61A m¹A→IRE1α | 41667948 / 10.1186/s11658-026-00863-6 | MO | Med | N | gold | ATC | m¹A-MAP-tRNA-seq + tRNA/RNA/Ribo-seq | 多组学 + 翻译/UPR 功能实验 | 增殖/转移 | m¹A 修饰增强氨酰化与全局翻译 → ER 应激 → IRE1α–XBP1s | 多层次功能实验 | 无患者队列与体内 | tRNA 修饰作为治疗靶点 | D15 扩展：翻译层驱动去分化 |
| 16 | ECM 硬度→Integrin α6β4/FAK | 41606295 / 10.1038/s41388-025-03674-9 | MO, ST | Med | N | closed | ATC | 可调刚度水凝胶 + 转录/蛋白组 + 小鼠 | 力学建模 + FAK 抑制 | 增殖/侵袭/肺转移 | 60 kPa 高刚度促恶性；FAK 抑制体内逆转 | 体内 + 药理干预 | 体外刚度模型简化 | 人 ATC 组织刚度图谱 | D22（新）：ECM 力学轴 |
| 17 | Cabozantinib 原代 ATC | 42588600 / 10.3390/cancers18152379 | IM, MO | Med | N | gold | ATC | 2 株细胞系 + 5 例原代患者细胞 | 活力/凋亡/划痕 + 细胞因子 | 活力 / CXCL10/CCL2 | 卡博替尼降低活力并减少 CXCL10、CCL2 分泌 | 原代细胞（5 例） | 无体内；n 小 | 与 VSIG4⁺ TAM 轴的联用 | D8/D9：TKI 免疫调节 |
| 18 | FTC 远处复发评分 | 42289343 / 10.1507/endocrj.ej26-0184 | PR | Med | N | gold | FTC | 597 例无远处转移初治 | AIC 逐步选择 + 加权评分 | 远处复发 | 年龄≥60、Ki-67>5%、V2 各 2 分，肿瘤>4 cm 与 V1 各 1 分 | 内部分层 | 单国队列，无外部验证 | 分子标志物加入 | D16 扩展：FTC 远处复发 |
| 19 | 儿童/青少年 PTC 淋巴结数 | 42525679 / 10.1097/rlu.0000000000006547 | PR | Med | N | closed | 学龄儿童与青少年 PTC | 中国 12 中心 486 例 | Cox | 持续性病灶 | N1b 中转移淋巴结数为独立危险因素（HR 1.06/枚） | 多中心 | 回顾性；终点为持续性疾病而非生存 | 与成人队列的对照 | D20：儿童 PTC 风险分层 |
| 20 | RAI 在 T3b DTC 无生存获益 | 42385380 / 10.1016/j.surg.2026.110382 | PR | Med | N | closed | T3b DTC | SEER 6638 例（2004–2022） | RSF + SHAP + Cox + PSM + Fine-Gray | 疾病特异生存 | RAI 变量重要性低，未改善 DSS | 多种敏感性分析 | SEER 无复发数据、无分子信息 | 分子分层下的 RAI 决策 | D18：RAI 去强化 |
| 21 | pN1b 结外侵犯范围 | 42289564 / 10.1007/s00405-026-10368-9 | PR | Med | N | closed | pN1b PTC | 3382 例（2000–2018） | KM + Cox | 疾病特异生存 | 5 年 DSS：无 ENE 99.8% / 微 99.5% / 宏 a 97.5% / 宏 b 82.2% | 大样本长随访 | ENE 定义不统一 | 病理判读标准化 | PR 方法学：ENE 分层 |
| 22 | N1b 清扫范围 | 42546578 / 10.1016/j.surg.2026.110442 | PR | Med | N | closed | N1b PTC | 5 中心 2695 例 | Cox + 限制性立方样条 | 持续/复发病灶 | 检出淋巴结数与结局呈非线性关联 | 多中心 | 回顾性，清扫范围受术者影响 | 前瞻性或工具变量设计 | PR 方法学 |
| 23 | Transformer 多模态 DL 诊断 | 42374243 / 10.1186/s12880-026-02530-w | AL | Med | N | gold | PTC vs 良性结节 | 2 中心 491 例 | 34 种架构对比 + 消融 + SHAP/Grad-CAM | 诊断效能 | Efficientnetv2scbamTrans 融合模型最优 | 外部测试集 | 样本量中等；可解释性指标自定义 | 外部多民族验证 | D13：架构选择与可解释性 |
| 24 | ViT 预测 cervical LNM | 41931576 / 10.1371/journal.pone.0345937 | AL, PR | Med | N | gold | PTC | 2 院 540 例 | ViT vs CNN vs 影像组学 vs 临床 | LNM | ViT 模型 AUC 优于对照模型 | 内部验证 | 缺少外部验证与阅片者研究 | 外部验证 | D13 |
| 25 | 跳跃转移多中心 | 41942301 / 10.1002/hed.70257 | PR | Med | N | closed | PTC 侧颈转移 | 3 中心 130 例 | 多因素 logistic + ROC | 跳跃转移 | 建立术前风险模型 | 多中心 | 样本较小 | 分子预测因子 | D13/PR |
| 26 | 对侧中央区 LNM | 41952435 / 10.1002/hed.70275 | PR | Med | N | closed | 单灶 PTC | 1437 例 | logistic + ROC | 对侧 CLNM | 独立预测因子与模型效能 | 大样本 | 单中心回顾 | 前瞻性验证 | PR 方法学 |
| 27 | LNM 部位与复发无关 | 42003162 / 10.1080/07853890.2026.2652661 | PR | Med | N | gold | PTC | 1378 例，长期随访 | PSM + Cox + 时间依赖 ROC | 无复发生存 | 孤立中央/侧颈/合并 LNM 间 RFS 无独立差异 | PSM + 长期随访 | 横断面设计表述 | 与 AJCC 分区的张力 | PR 方法学 |
| 28 | TKI 生存获益 meta | 42730470 / 10.14740/wjon2842 | PR | Med | N | gold | 晚期甲状腺癌 | 18 项 RCT（14 项定量） | 系统综述 + meta | OS / PFS | 整合 donafenib、nintedanib 与更新 SELECT/COSMIC-311 | RCT 级 | 安慰剂对照与剂量比较分开分析 | 头对头比较缺失 | D18 扩展 |
| 29 | GOLPH3→TGF-β | 42301509 / 10.1007/s00438-026-02471-7 | MO | Med | N | closed | PTC | 公共数据 + 细胞系 | qPCR/WB + KEGG + 功能实验 | 增殖/周期 | GOLPH3 经 TGF-β 通路促癌 | 细胞实验 | 无体内与队列 | 与 EMT 的交叉 | MO 常规 |
| 30 | 类器官 EDN1→Hippo-YAP | 41569405 / 10.1007/s40618-025-02755-6 | MO, SP | Med | N | closed | PTC | 类器官 + 异种移植 | 慢病毒敲低 + 类器官/成瘤 | 增殖/迁移 | EDN1 经 Hippo-YAP 驱动 PTC | 类器官 + 体内 | 与 TAZ 轴的冗余未澄清 | 与 TAZ/WWTR1 的关系 | D15 扩展 |
| 31 | circFN1→miR-29a/TRIB2 | 42724449 / 10.21037/tcr-2026-1-0061 | MO | Med | N | gold | PTC | 配对组织 + TPC-1 | IHC/qPCR/WB + 功能 | 侵袭 | circFN1 经 miR-29a/TRIB2 激活 PI3K/AKT | 配对组织 | 单细胞系 | 体内验证 | MO 常规 |
| 32 | FN1→失巢凋亡抵抗 | 42002564 / 10.1038/s41598-026-43495-8 | MO, ST | Med | N | gold | PTC | TCGA + 实验验证 | 生信 + 功能 | 失巢凋亡 | FN1 调控失巢凋亡抵抗促进展 | 实验验证 | 机制层较浅 | 与转移定植的关系 | ST |
| 33 | RAN-S100A10-EGFR | 41991927 / 10.1038/s41419-026-08649-6 | MO, SC | Med | N | gold | PTC | 公共 scRNA + 组织/细胞 + MS + Co-IP | 单细胞筛选 + 互作验证 | 转移/预后 | S100A10 经 RAN/EGFR 激活 PI3K/AKT | 质谱 + Co-IP | 无体内成瘤 | 单细胞来源亚群定位 | MO/SC |
| 34 | CHI3L1×TP53 | 42001899 / 10.1002/cnr2.70553 | MO | Med | N | gold | PTC | 公共数据 + 细胞 + 异种移植 | 转录组 + 功能 + 成瘤 | 增殖/侵袭 | CHI3L1 与 TP53 信号相关并促 PTC | 异种移植 | 机制偏描述 | TP53 状态分层 | MO/D15 |
| 35 | MBP 慢性暴露→ATC | 42652139 / 10.3390/biomedicines14081755 | MO, IM | Med | N | gold | ATC | CAL-62 慢性 3 月暴露 | 转录组 + 网络毒理 + 分子对接 + WB | 活力/通路 | 环境相关浓度 MBP 增强 ATC 恶性表型 | 体外慢性模型 | 单一细胞系、单一浓度 | 环境暴露与 TC 风险 | 环境-肿瘤交叉 |
| 36 | EZH2 启动子×MAPK | 42511745 / 10.3390/ijms27146402 | MO | Med | N | gold | ATC | 报告基因删除 + U0126 + TF 操控 | 启动子解析 | EZH2 转录 | 107 bp 最小启动子含 MAPK 调控 TF 结合位点 | 报告基因 + 药理 | 无体内 | EZH2 抑制剂的再定位 | D15 扩展 |
| 37 | MAPKi→NIS/ARF4（ATC） | 42236533 / 10.1038/s41598-026-54570-5 | MO | Med | N | gold | ATC | 细胞系 + 异种移植 + ¹⁸F-FDG PET | WB + 定位分析 | RAI 敏感性 | 三种 MAPK 抑制剂提升 NIS 表达与膜定位 | 异种移植 + PET | 与 NOX4 轴的层级未明 | 与 NOX4/TGF-β1 三联 | D18：红分化 |
| 38 | UBE2T→SOCS2/JAK-STAT3 | 41330207 / 10.1016/j.seminoncol.2025.152439 | MO | Med | N | closed | PTC | TCGA/GEO + 本院样本 | Co-IP + rescue + IF | 侵袭/LNM | UBE2T  destabilize SOCS2 解除对 STAT3 磷酸化的抑制 | 临床样本 + rescue | 无体内 | 与 UBE2C 的冗余 | MO 常规 |
| 39 | EN1 促 PTC 转移 | 41817283 / 10.1177/10849785261428404 | MO, ST | Med | N | closed | PTC | 376 配对 + 细胞 + 皮下/尾静脉模型 | IHC + 功能 + 双体内模型 | 转移 | EN1 高表达与淋巴血管侵犯相关；敲低抑制恶性 | 双体内模型 + 大队列 IHC | 单中心 IHC 队列 | 下游效应子 | ST |
| 40 | METTL3/CSDE1→Wnt | 42306981 / 10.5603/ep.111586 | MO | Med | N | closed | PTC | TCGA + 组织/细胞 | MeRIP-qPCR + 双荧光素酶 | 增殖/EMT | METTL3 经 m⁶A 调控 CSDE1，激活 Wnt/β-catenin | 机制实验 | 无体内 | m⁶A 与 m¹A 的交叉 | D23（新）：表观-转录后交叉 |
| 41 | HPGD→NK/JAK2-STAT3 | 42136233 / 10.2174/0115680096425628251130133650 | MO, IM | Med | N | closed | PTC | TCGA + TPC-1 + NK 共培养 | 功能 + 浸润评分 + 共培养 | 免疫逃逸 | HPGD 抑制 NK 活化并激活自噬/JAK2-STAT3 | NK 共培养 | 单一细胞系 | NK 轴的体内验证 | D8 扩展 |
| 42 | 双原发肺癌+甲状腺癌 scRNA | 41859004 / 10.1016/j.gendis.2025.101889 | SC, MO | Med | N | gold | 双原发肺癌 + 甲状腺癌 | scRNA-seq + 大 panel NGS | 单细胞 + 基因组 | 异质性/基因组特征 | 刻画双原发肿瘤的转录异质性与基因组特征 | 无外部验证 | 双原发情境特殊，外推有限 | 共同克隆起源判别 | SC 方法学 |
| 43 | H3K27ac→APOC1（PTC） | 42597226 / 10.62347/qhyg5969 | MO, ME | Med | N | (未解析) | PTC | 公共数据 + 实验 | 表观 + 功能 | 增殖 | H3K27ac 激活 APOC1 促进 PTC 增殖 | 实验验证 | 期刊/数据库层级较弱，需核验 | 上游增强子定位 | D21 |
| 44 | JPH3→顺铂耐药（ATC） | 41862190 / 10.1002/cam4.71750 | MO | Med | N | gold | ATC | 生信 + 体内外 | WB + 功能 + 耐药模型 | 顺铂耐药 | JPH3 高表达预后差，经 JAK-STAT 介导耐药 | 体内外 | 与他癌中"抑癌基因"定位相反，需谨慎 | 组织特异性双面性 | D18 |
| 45 | ProGRP 动力学（MTC） | 42340255 / 10.1515/cclm-2026-0757 | PR | Med | N | closed | 转移性 MTC | 23 例，中位随访 37 月 | 个体化对数线性回归 + KM | 结构进展/死亡 | ProGRP 与 CA19-9 作为 CT/CEA 的补充标志物 | 纵向队列 | n=23 极小 | 大队列验证 | D16 |
| 46 | Level VII LNM（MTC） | 42322801 / 10.1016/j.surg.2026.110328 | PR | Med | N | closed | MTC | SEER 1983 例 | 比较 AJCC8 与改良 N 分类 | 疾病特异生存 | 评估 level VII 由 N1b 改列 N1a 的预后含义 | 大样本 SEER | SEER 无分子与复发细节 | 与分区复发研究联动 | D16 |
| 47 | 多区域超声影像组学（habitat） | 10.1186/s12880-026-02791-5 | AL, PR | Med | N | gold | PTC | 多中心超声 | 全肿瘤 + habitat 亚区 + 瘤周特征 | 术前 LNM | 多区域特征融合提升术前预测 | (摘要未取) | 待全文核验 | 与 PACS-AI 的互补 | D13 |
| 48 | cN0 PTC 中央区 LNM 列线图 | 10.1186/s12902-026-02624-0 | AL, PR | Med | N | gold | cN0 PTC | 临床队列 | 列线图 | 中央区 LNM | 术前预测列线图 | (摘要未取) | 待全文核验 | 外部验证 | D13 |
| 49 | 多模态 ML：pathomics + radiomics | 42822363 / 10.1016/j.clinsp.2026.101120 | AL | Med | N | closed | PTC | 视角文章 | 综述/观点 | — | 讨论病理组学与影像组学的多模态融合路径 | — | 无原始数据（观点文章） | 融合策略的实证基准 | D13 |
| 50 | 低危 PTC 腺叶切除后补全切除 | 10.1177/00031348261494195 | PR | Med | N | closed | 低危 PTC | 手术队列 | 回顾 | 再手术/结局 | 评估"更少手术"的代价 | (摘要未取) | 待全文核验 | 主动监测 vs 手术的决策 | PR |
| 51 | APOC1 焦亡（桥本，边界） | 41996849 / 10.1016/j.molimm.2026.04.005 | MO | Low | N | closed | 桥本甲状腺炎 | 公共数据 + 实验 | 通路分析 | 焦亡 | APOC1 经 TLR10/MyD88/NF-κB 介导焦亡 | 实验 | **非肿瘤，边界条目** | 桥本→PTC 的转化 | 边界观察 |
| 52 | LIFU 仿生纳米颗粒（MTC） | 10.1177/15330338261492797 | IM | Low | N | gold | MTC | 体外 | 纳米颗粒 + LIFU | 治疗效应 | "三合一"治疗策略体外验证 | 仅体外 | 非本监测主轴 | — | 边界观察 |
| 53 | VSIG4 甲状腺癌×SLE 共享标志物 | 42348043 / 10.1007/s12672-026-05493-0 | IM, AL | Low | Y→N | gold | 甲状腺癌 + SLE | GEO | CIBERSORTx + PPI + hub 基因 | 共享机制 | 46 个共享 DEG，识别 hub 基因 | 无实验验证 | 纯生信，无湿实验 | 自身免疫-肿瘤共病 | 边界观察 |
| 54 | Acacetin 滤泡甲状腺细胞 | 10.21873/anticanres.18390 | MO | Med | N | closed | 滤泡甲状腺细胞 | 细胞 | 活力/迁移 | 细胞死亡/迁移 | 金合欢素促进细胞死亡、抑制迁移 | 仅体外 | 机制浅 | — | 边界观察 |
| 55 | 峡部切除 vs 腺叶/全切 | 42026285 / 10.1007/s00405-026-10203-1 | PR | Low | N | closed | PTC | PSM 队列 | 倾向评分匹配 | 生存 | 峡部切除生存结局比较 | PSM | 回顾性 | — | PR 方法学 |
| 56 | ZEB1 预后 IHC | 42700989 / 10.1016/j.cpsurg.2026.102085 | PR | Low | N | closed | PTC | 回顾 IHC | IHC | 预后 | ZEB1 作为预后标志物 | (摘要未取) | 单中心 IHC | — | MO/PR |
| 57 | TRIM35→PPAR | 42180910 / 10.21037/tcr-2025-1-2769 | MO | Low | N | gold | PTC | IHC + 细胞 | 功能实验 | 增殖/转移 | TRIM35 敲低抑制恶性表型 | 细胞实验 | 机制浅 | — | MO 常规 |
| 58 | miR-181a-5p→PTEN/AKT | 42234375 / 10.1007/s12033-026-01581-2 | MO | Low | N | gold | PTC | 组织/细胞 + TCGA | qPCR + WB + 功能 | 增殖/侵袭 | miR-181a-5p 抑制 PTEN、激活 AKT | 功能实验 | 无体内 | — | MO 常规 |
| 59 | Berberine→焦亡 | 41740544 / 10.1016/j.bbrc.2026.153440 | MO | Low | N | closed | PTC | 多基因型细胞系 | 焦亡检测 | 焦亡 | 小檗碱经 NLRP3/Caspase-1/GSDMD 诱导焦亡 | 体外 | 无体内 | — | MO 常规 |
| 60 | Puerarin→FOXO1/GABARAPL1 | 42753466 / 10.1016/j.tice.2026.103968 | MO | Low | N | closed | 甲状腺癌 | 细胞系 | 自噬检测 | 自噬/存活 | 葛根素上调 FOXO1→GABARAPL1 促自噬 | 体外 | 无体内 | — | MO 常规 |
| 61 | Dendrobine→JAK-STAT3（ATC） | 42311248 / 10.3389/fonc.2026.1842670 | MO | Low | N | gold | ATC | CAL-62/8505C + 异种移植 | 活力/凋亡/迁移 + IL-6/STAT3 干预 | 成瘤 | 石斛碱抑制 JAK-STAT3 并体内抑瘤 | 异种移植 | 天然产物，靶点特异性存疑 | — | MO 常规 |
| 62 | KIF23→Wnt（ATC） | 41675939 / 10.1155/ije/7664607 | MO | Low | N | gold | ATC | 细胞 | 功能 + erastin 诱导 | 活力/侵袭 | KIF23 过表达经 Wnt/β-catenin 促恶性 | 细胞实验 | 无体内 | — | MO 常规 |
| 63 | Gilteritinib+dabrafenib（ATC） | 42409582 / 10.3724/zdxbyxb-2025-0799 | MO | Low | N | (未解析) | ATC | 细胞 | 联合用药 | 抑制效应 | Gilteritinib 经抑制 AXL 增强达拉非尼 | 细胞实验 | 无体内 | — | MO 常规 |
| 64 | 妊娠滋养细胞肿瘤合并甲亢 | 10.32502/sm.v17i1.11561 | MO | Low | N | diamond | GTN + 甲亢 | 病例 | 病例报告 | — | 严重甲亢伴 β-hCG 显著升高 | 病例 | **非甲状腺癌** | — | 边界 |
| 65 | RAI 治疗后生活质量综述 | 10.5530/ajphs.2026.16.98 | PR | Low | N | closed | 甲状腺癌 | 叙述综述 | — | QoL | RAI 治疗后生活质量 | — | 综述，非原始证据 | — | 边界 |
| 66 | BRAF 突变 PTC LNM 预测模型 | (无 DOI) | AL, PR | Med | N | closed | BRAF 突变 PTC | 队列 | 预测模型 | LNM | 构建 LNM 预测模型 | (摘要未取) | **无 DOI，可复现性受限** | — | D13 |

> 注：#47–#50、#52、#64–#66 为 OpenAlex 30 d 窗口内新增但摘要未完整返回者，按标题与维度入表并标注「待全文核验」。#66 无 DOI。

---

## 四、已知结论 / What Is Already Known

1. **TAM 异质性已是甲状腺癌最活跃的前沿，且本轮由四条通路扩张为五条。** Run #22 确立 SPP1/CD44–JAK2–STAT3，Run #21 确立 TREM2/AHR–IDO1，Run #26 补充 RARγ/CFI 与 BGN/NR2F2；本轮新增 **HN1/CEBPB/CCL2 → CCR2/PI3K/AKT → VSIG4⁺ TAM**（PMID 42191099）。五条通路在 ATC 中最集中，提示 ATC 是 TAM 靶向的最佳适应证，但也意味着**单纯"再做一次 TAM 亚群描述"的边际价值正在快速下降**。

2. **载脂蛋白家族构成 PTC 中一条跨队列可复现的脂代谢轴。** APOC1 与 APOA1 在 TCGA-THCA 与三个独立 GEO 队列中一致上调、VLDLR 一致下调（PMID 42742374）；APOC1 高表达与更差预后和免疫逃逸签名相关并可被 cyclopamine 靶向（PMID 41289702）；H3K27ac 可激活 APOC1（PMID 42597226）。结合基线中的 *Lipid Metabolic Reprogramming in Thyroid Cancer*（10.20944/preprints202608.0708.v1）与 Run #25 的 APOE–PINK1/Parkin（PMID 42724858），**"载脂蛋白—线粒体自噬—免疫逃逸"已成为可检验的三元框架**。

3. **RAI 难治的去分化存在可药物干预的表观机制。** NOX4 源性氧化损伤经 OGG1/MSH2-MSH6/DNMT1 阻断 PAX8/NKX2.1 染色质结合而沉默 NIS；MAPK + TGF-β1 双抑制可恢复（PMID 41694580）。独立地，MAPK 抑制剂经 NIS/ARF4 提升 ATC 的 RAI 敏感性（PMID 42236533）。两条证据共同支持"**红分化需要同时压 MAPK 与 TGF-β/ROS 两条腿**"。

4. **BRAF 抑制剂耐药在 ATC 中可由 Hippo–UPR–ferroptosis 三联解释。** TAZ/WWTR1 缺失与 BRAF 抑制合成致死，机制为抑制 UPR 并转向 ferroptosis（PMID 42035477）。这与 EDN1→Hippo-YAP（PMID 41569405）、EZH2 启动子受 MAPK 调控（PMID 42511745）共同提示 **Hippo 通路是 ATC 中被低估的耐药节点**。

5. **MTC 的手术范围与远处转移监测正在被大样本重塑。** 四中心 235 例分区复发（PMID 42690646）与 SEER 1983 例 level VII 分级（PMID 42322801）同时指向"分区精细化"；ProGRP/CA19-9 作为 CT/CEA 的补充（PMID 42340255）提供了纵向监测新选项；获得性驱动融合则是 RET 抑制剂耐药的新机制（PMID 41719512）。

6. **远处转移预后工具在甲状腺癌中仍稀缺，本轮取得突破。** 非 ATC 滤泡细胞来源甲状腺癌脑转移的疾病特异性 GPA（19 中心 189 例 + SEER；PMID 42545312）与 FTC 远处复发加权评分（597 例；PMID 42289343）是两项可直接进入临床讨论的工具。

7. **PTC 淋巴结转移"数量优于部位"的证据在继续累积。** 转移淋巴结部位与复发无独立关联（1378 例 PSM；PMID 42003162），而 N1b 中转移淋巴结**数目**为独立危险因素（486 例儿童/青少年；PMID 42525679）；结外侵犯的**范围**而非有无决定预后（3382 例；PMID 42289564）。

8. **RAI 去强化的边界在扩大。** T3b DTC 中 RAI 未带来疾病特异生存获益（SEER 6638 例 + PSM + Fine-Gray；PMID 42385380），与低危 PTC 腺叶切除后补全切除的代价评估（10.1177/00031348261494195）形成呼应。

9. **临床可落地的甲状腺 AI 正在从"造模型"转向"嵌流程 + 评人"。** PACS 内嵌的三段式 3D 流水线带外部验证与 reader study（PMID 42760456）代表新范式；同时出现对 AI 训练质量本身的审视（PMID 42758456）与多模态融合路径讨论（PMID 42822363）。

---

## 五、未解问题 / What Remains Unclear

1. **APOC1/APOA1 的细胞区室来源未定。** PMID 42742374 为 bulk 转录组，Run #26 的 iScience 儿科研究把 SPP1/APOC1/APOE 放在髓系 Macro2，而 PMID 41289702 把 APOC1 当肿瘤细胞靶点。**同一基因在三个 compartment（髓系 / 基质 / 上皮）的功能可能完全不同甚至相反，现有证据无法区分** —— 这是 D21 最大的方法学障碍，也是必须优先解决的问题。

2. **VSIG4⁺ TAM 与已知四个 TAM 节点的关系未测。** HN1/CCL2/VSIG4 轴是否与 SPP1⁺、TREM2⁺ 亚群重叠或互斥？是否存在层级（CCL2 为上游招募信号，SPP1/TREM2 为下游极化状态）？本轮无任何文献同时测量 VSIG4 与 SPP1/TREM2。

3. **NOX4 轴与 MAPK/TGF-β 轴的层级关系不清。** PMID 41694580 主张 NOX4 受 TGF-β1 调控、MSH2/MSH6 与 DNMT1 受 MAPK 调控；PMID 42236533 则从 MAPK 抑制剂出发得到 NIS 恢复。两者是否同一通路的不同入口，需要并排实验而非各自表述。

4. **MGST1 仍是孤岛（连续第 27 轮）。** APOE×MGST1×thyroid 共现 = 0；MGST1 2026 年甲状腺癌文献 = 1。当前**无法判断这是真实的生物学无关，还是检索/索引层面的系统性不可见** —— 但连续 27 轮三通道检索（含定向深挖）均为 0，实证上应视为结构性空白。

5. **肠道菌群效应方向矛盾。** Run #26 的 *Terrisporobacter*→NTRK1 为免疫抑制（促瘤），本轮 Ruminococcaceae→m6A→焦亡为抑瘤（PMID 41627386）。**"肠道菌群与甲状腺癌"作为整体命题可能无意义**，必须下沉到菌株—代谢物—通路层级。

6. **TP53 在 ATC 中的作用情境依赖。** 本轮 TP53 突变预示达拉非尼+曲美替尼疗效较差（PMID 42820284），而 CHI3L1 研究将 CHI3L1 与 TP53 信号关联（PMID 42001899）。TP53 是预后标志还是预测标志、是否需按治疗方案分层，尚未解决。

7. **儿童/青少年与成人 PTC 的差异机制未明。** 中国 12 中心 486 例证实 N1b 中淋巴结数目为独立危险因素（PMID 42525679），但未回答为何儿童 PTC 呈现"高淋巴结负荷 + 低死亡率"的解耦。

8. **AI 模型的校准漂移与跨中心泛化仍缺系统评估。** 本轮三项影像 AI（PMID 42760456、42374243、41931576）均在多中心但同区域数据上验证，Run #25 已指出校准漂移问题（PMID 42591955），本轮未见针对该问题的新证据。

---

## 六、领域方法/数据局限 / Method and Data Limitations In The Field

| 局限类型 | 本轮具体表现 | 影响 |
|---|---|---|
| **区室归属缺失（bulk vs single-cell）** | APOC1/APOA1（PMID 42742374）、CHI3L1、HPGD 等均以 bulk 或全组织为单位 | 无法区分髓系/基质/上皮来源，机制结论易张冠李戴 |
| **外部验证稀少** | 本轮 12 条 High 中仅 3 条有外部独立队列（PMID 42742374、42760456、42545312） | 模型与签名的可推广性存疑 |
| **单中心小样本** | TP53/ATC n=25（PMID 42820284）；ProGRP n=23；MBP 单一细胞系单一浓度 | 效应量估计不稳定 |
| **回顾性与选择偏倚** | 外科类研究（PMID 42690646、42289564、42546578）均为回顾，手术跨度长达 23 年 | 术式演变与影像分期迁移构成时间混杂 |
| **公共数据复用与批次效应** | TCGA-THCA + GEO 复用普遍；跨队列验证多为差异方向一致性而非批次校正后的定量一致 | "可复现"可能仅指方向 |
| **无湿实验的纯生信** | VSIG4×SLE（PMID 42348043）、GSTTK 五基因模型（PMID 42507215） | 结论停留在关联层 |
| **天然产物/药物重定位研究靶点特异性不足** | Dendrobine、Puerarin、Berberine、Acacetin 等 | 多靶点，机制归因弱 |
| **NCBI 域在本机完全不可达** | GEO/FTP/eutils/PubMed 均 HTTP 000，论文中 GSE 编号只是"引用"不是"可下载" | 原始数据层复现须转 ENA / NGDC / 合作节点 |
| **撤稿/更正条目污染** | 本轮 EPMC 命中 6 条 `Retraction notice` / `Correction` / `ASO Visual Abstract` | 若不剔除会虚增文献计数 |

---

## 七、候选未来方向 / Candidate Future Directions

> **评分口径说明**：历史轮次（Run #21–#26）的方向总分为整体估计，校准偏宽。**本轮起改为按 research-direction-rubric 七维（Novelty / Feasibility / Data availability / Validation strength / Clinical relevance / Method rigor / Overcrowding risk，各 1–5 分，满分 35）逐项打分并求和**。下表同时给出历史值与重算值；**趋势以重算值序列为准**，后续轮次沿用此口径。
> 解释阈值：28–35 强候选；21–27 可行候选；14–20 探索级。

| ID | Direction / 方向 | 研究问题 | 新颖度 | 可行性 | 数据可得 | 验证强度 | 临床相关 | 方法严谨 | 反拥挤 | **重算总分** | 历史值 | 本轮状态 |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| **D21** 🆕 | 载脂蛋白–脂代谢–免疫轴（APOC1/APOA1/APOE）在 PTC 的区室解析与因果验证 | APOC1/APOA1 在髓系、基质、上皮三个 compartment 中分别由谁表达、功能是否解耦？ | 4 | 5 | 5 | 4 | 4 | 4 | 3 | **29** | — | 新立（强候选） |
| **D9** | SPP1⁺/APOC1⁺/VSIG4⁺ TAM 空间生态位与极化层级 | 五个 TAM 节点是否构成招募→极化的层级？空间上是否共定位？ | 5 | 4 | 5 | 4 | 4 | 4 | 3 | **29** | 34 | **强化**（证据增、反拥挤降） |
| **D12** | Hippo/TAZ–UPR–ferroptosis 三联与 BRAFi 耐药 | TAZ 抑制能否作为 BRAFi 增敏策略？ferroptosis 是共同终末通路吗？ | 5 | 4 | 4 | 4 | 5 | 4 | 4 | **30** | 30 | **强化**（获准因果链） |
| **D17** | 肠道/瘤内微生物群的**菌株级**机制 | 为何不同菌株效应方向相反？代谢物中介是什么？ | 5 | 4 | 4 | 3 | 3 | 4 | 4 | **27** | 27 | **强化**（首获机制层证据） |
| **D15** | 去分化/ATC 轨迹与红分化 | 表观（NOX4/DNMT1/EZH2）与翻译层（m¹A）如何协同锁定去分化状态？ | 4 | 4 | 4 | 4 | 5 | 4 | 3 | **28** | 30 | **强化**（两条新机制） |
| **D16** | MTC 远处转移、分区复发与耐药克隆演化 | 手术分区决策能否与分子分层合并？RET 抑制剂耐药的融合谱？ | 4 | 4 | 4 | 4 | 5 | 4 | 4 | **29** | 27 | **强化**（JAMA Oto + SEER + 融合耐药） |
| **D18** | 代谢–耐药轴（RAI 去强化与红分化） | 谁真正从 RAI 获益？红分化需同时压哪几条腿？ | 4 | 5 | 5 | 4 | 5 | 4 | 4 | **31** | 29 | **强化**（SEER 6638 + NOX4 + MAPKi） |
| **D13** | 可落地临床 AI：从建模到嵌流程、评校准 | 多中心部署后校准漂移多大？reader study 能否成为标配？ | 3 | 5 | 5 | 4 | 5 | 4 | 3 | **29** | 29 | **维持**（方法学范式升级） |
| **D8** | TAM 极化全景 | — | 3 | 5 | 5 | 4 | 4 | 4 | **2** | **27** | 32 | **维持但反拥挤风险显著升高** |
| **D11** | 乳酸化–EMT–TF 轴 | — | 4 | 4 | 4 | 4 | 3 | 4 | 3 | **26** | 32 | 无新证据 |
| **D14** | 细胞类型解析因果 + 空间多组学方法论 | — | 4 | 4 | 4 | 4 | 3 | 5 | 4 | **28** | 28 | 无新证据 |
| **D20** | 儿童/青少年 PTC | 为何高淋巴结负荷与低死亡率解耦？ | 4 | 4 | 4 | 3 | 4 | 4 | 4 | **27** | 24 | **强化**（中国 12 中心 486 例） |
| **D19** | 性别二态性 | — | 3 | 4 | 4 | 3 | 3 | 4 | 4 | **25** | 26 | 无新证据 |
| **D22** 🆕 | ECM 力学–Integrin α6β4/FAK 轴在 ATC | 人 ATC 组织刚度图谱如何？FAK 抑制剂能否增敏？ | 4 | 3 | 3 | 3 | 3 | 4 | 4 | **24** | — | 新立（探索级） |
| **D23** 🆕 | 表观–转录后修饰交叉（m⁶A / m¹A / H3K27ac / 乳酸化） | 多层修饰是否构成统一的"分化锁"？ | 3 | 4 | 4 | 3 | 3 | 3 | 3 | **23** | — | 新立（探索级） |
| **D3″** | ~~APOE×MGST1 双轴~~ | — | 5 | 4 | **2** | **2** | 2 | 3 | 5 | **23** | 31 | ⬇️ **降级→建议归档** |

### 重点方向详述 / Detail on Leading Directions

**D21（新立，29）载脂蛋白–脂代谢–免疫轴的区室解析与因果验证 / Compartment-resolved causal mapping of the apolipoprotein–lipid–immune axis in PTC**
- Research question：APOC1 与 APOA1 在 PTC 的髓系（Macro2：SPP1⁺/APOC1⁺/APOE⁺）、基质（APOE⁺ PVL）与上皮（APOE-high tumor）三个 compartment 中分别由谁表达？三者功能是协同、冗余还是解耦？
- Novelty angle：现有四条证据（PMID 42742374 / 41289702 / 42597226 / Run #26 iScience）分属三个 compartment 却共用同一基因名，**尚无一项研究在同一批样本中同时测量三者**。
- Required datasets：TCGA-THCA（bulk 发现）+ GSE193581（成人 PTC scRNA，跨队列桥梁）+ iScience 儿科 PTC（10.1016/j.isci.2026.116560，PMC13378368）+ GSE29265/GSE33630/GSE60542（跨队列验证）。
- Expected endpoint：三 compartment 的 APOC1/APOA1/APOE 表达矩阵 + 各 compartment 特异的预后/免疫逃逸关联。
- Analysis strategy：先做公开 scRNA 的区室拆分与 signature 打分，再用 cell2location/BayesSpace 去卷积到可得的空间底图（**注意：JCI Insight 个体级数据受 IRB 限制，不可作空间底图**，见 Run #26 续作）。
- Validation plan：TCGA-THCA 生存/免疫逃逸签名 → 三个 GEO 队列方向一致性 → 若有条件，多重免疫荧光在自有样本上共定位。
- Major risk：APOC1 抗体质量与脂滴/巨噬细胞泡沫化的形态学干扰；跨数据集的脂代谢基因批次效应显著。
- Claim boundary：**不得声称 APOC1 为"肿瘤细胞内在驱动因子"** —— 现有证据无法排除髓系来源；**不得把 APOC1 结论外推为 MGST1 结论**。

**D9（29，强化）SPP1⁺/APOC1⁺/VSIG4⁺ TAM 空间生态位与极化层级**
- Research question：CCL2–CCR2 是否位于 SPP1/TREM2/VSIG4 极化的**上游招募层**？五个节点在空间中是否形成"血管周招募 → 生态位内极化"的级联？
- Novelty angle：本轮 VSIG4⁺ 为第五个节点，但**无一文献同时测量 VSIG4 与 SPP1/TREM2**。
- Required datasets：同上 + ATC 单细胞图谱（ATC 是五节点最集中的亚型）。
- Expected endpoint：TAM 亚群的层级树（招募信号 vs 极化状态）+ 空间邻域富集矩阵。
- Validation plan：两算法（BayesSpace + cell2location）一致性 + TCGA-THCA 去卷积预后。
- Major risk：TAM 方向已高度拥挤（反拥挤分 2–3），必须靠"层级 + 空间"而非"再发现一个亚群"取胜。
- Claim boundary：**不得把小鼠 CCL2/VSIG4 阻断结果直接外推为人 ATC 治疗假设**。

**D18（31，强化）代谢–耐药轴：RAI 去强化与红分化**
- Research question：在分子分层（BRAF/TERT/TP53）下，T3b DTC 中哪一类患者仍能从 RAI 获益？红分化方案中 MAPK + TGF-β1/NOX4 双抑制是否优于单药？
- Novelty angle：SEER 6638 例阴性结果（PMID 42385380）与两条红分化机制（PMID 41694580、42236533）形成"减去强化 + 增强敏感"的双向切口。
- Required datasets：SEER（可经第三方镜像）、TCGA-THCA、RAI 难治队列的 NIS/PAX8/NKX2.1 表达。
- Expected endpoint：RAI 获益的分子分层规则；NIS 恢复的联合用药组合。
- Validation plan：SEER 内部 PSM + 独立机构队列；体内验证 NOX4 抑制 + MAPKi。
- Major risk：SEER 无复发与分子信息，阴性结果可能来自适应证混杂。
- Claim boundary：**不得据 SEER 阴性结果得出"T3b 一律不做 RAI"**。

---

## 八、推荐下一步方向 / Recommended Next Direction

**首选：D21 × D9 合并 —— 载脂蛋白签名与 TAM 空间生态位的耦合分析（零湿实验起步）。**

**为什么是它**：这是本轮唯一同时满足「三证据独立收敛」+「公开数据即可启动」+「存在明确的错误推论风险（区室混用）」的方向。当前领域正在把 APOC1、APOE、SPP1+APOC1+APOE Macro2 混为一谈，而三者分属不同 compartment —— **谁先把区室拆开，谁就掌握了这个轴的解释权**。同时它能吸收 D3″ 的残余价值（把 APOE 问题放进正确的框架），避免 27 轮跟踪空转。

**第一批具体动作（无需湿实验）**：

1. **M1 — 区室拆分基线（1–2 周）**：在 GSE193581（成人 PTC scRNA）与 iScience 儿科队列（PMC13378368）上，分别计算 APOC1 / APOA1 / APOE 在髓系、基质、上皮三 compartment 的表达占比与共表达结构，产出"三 compartment 载脂蛋白表达矩阵 v1"。
2. **M2 — 跨队列一致性检验**：在 GSE29265 / GSE33630 / GSE60542 上复现 PMID 42742374 的 APOC1↑ / LPL↑ / VLDLR↓ 方向，并检验该方向是否可被髓系比例解释（即做**细胞比例校正后**的再分析）。
3. **M3 — TAM 层级建模**：以 CCL2/CCR2 为候选上游，SPP1 / TREM2 / VSIG4 / APOC1 为候选下游，构建 TAM 极化层级的因果图（可用 Run #23 确立的细胞类型解析因果框架 + Run #24 的蛋白基因组 ML 范式），明确 VSIG4⁺ 是否可由 CCL2 信号强度预测。
4. **M4 — 空间耦合**：把 M1 的 signature 去卷积到可得的空间底图（**JCI Insight 个体级数据受 IRB 限制，仅作单细胞参考与方法学范本**；优先 KHDP SNUH-THYROID-NGS2 或通过 ENA 检索的替代空间数据集）。
5. **M5 — MGST1 终判**：对 MGST1 做**全 compartment、全通道**最后一次系统检索（OpenAlex + Europe PMC + 定向深挖 + ENA/NGDC 数据层）。**若仍为 0 共现，按 Run #26 预设将 D3″ 从「候选方向」移入「已检验假设（阴性）」归档区**。

**所需数据集**：TCGA-THCA、GSE193581、GSE29265/GSE33630/GSE60542、iScience 儿科 PTC（PMC13378368）、ENA/NGDC 检索所得空间数据集。

**必须避免的主张**：① 不得声称 APOC1 是肿瘤细胞内在驱动因子；② 不得把 APOC1 结论外推至 MGST1；③ 不得把 CCL2/VSIG4 小鼠阻断结果表述为人 ATC 治疗假设；④ 不得据 bulk 差异表达断言区室归属。

---

## 九、随访阅读清单 / Follow-Up Reading List

| 优先级 | 文献 | 为什么下一步读 |
|---|---|---|
| P0 | APOC1 VLDL × DTI（PMID 42742374, 10.1111/cbdd.70403） | D21 的方法学模板：四阶段设计 + XGBoost-SHAP + MR，可直接复用；需核对区室归属表述 |
| P0 | HN1/CEBPB/CCL2→VSIG4⁺ TAM（PMID 42191099） | D9 层级建模的直接输入；需提取 CCL2/CCR2 与 VSIG4 的定量关系 |
| P0 | NOX4→NIS 表观沉默（PMID 41694580, gold OA） | D18 红分化的机制主干；需确认 TGF-β1 与 MAPK 的实验剂量与组合顺序 |
| P1 | CRISPR TAZ/WWTR1（PMID 42035477, hybrid） | D12 最硬证据；需提取 CRISPR 筛的筛选条件与 hit 列表以设计增敏实验 |
| P1 | Ruminococcaceae→m6A→焦亡（PMID 41627386） | D17 首条机制级证据；需对照 Run #26 *Terrisporobacter* 的方向矛盾 |
| P1 | MTC 分区复发（PMID 42690646, JAMA Otolaryngol） | D16 最高级别证据；需提取对侧 pCND 的风险差与 Cox 结果 |
| P1 | PACS-AI（PMID 42760456） | D13 新范式；需提取分割 DSC 偏低的原因与 reader study 设计 |
| P2 | TP53 × 达拉+曲美（PMID 42820284） | ATC 精准分层；n=25 需独立队列复核 |
| P2 | 非 ATC 脑转移 GPA（PMID 42545312） | 远处转移预后工具；需核对"乳头状组织学"为不良因素是否为混杂 |
| P2 | MYOF→PINK1/Parkin（PMID 42271528, gold） | 与 Run #25 APOE–PINK1 的交叉节点，D21 的线粒体分支 |
| P2 | ECM 硬度→FAK（PMID 41606295） | D22 的立论基础；需评估刚度模型的生理相关性 |
| P3 | *Spatial Transcriptomics in Thyroid Cancer: A PRISMA-Guided Systematic Review*（基线 10.20944/preprints202608.0302.v1） | 空间底图选型的现成综述，M4 前置阅读 |
| P3 | *Lipid Metabolic Reprogramming in Thyroid Cancer*（基线 10.20944/preprints202608.0708.v1） | D21 的领域背景；预印本，需降档采信 |

---

## 十、可复现性说明 / Reproducibility Notes

- **Search date / 检索日期**：2026-10-03 01:06–01:35 (UTC+8)
- **Databases / 数据库**：OpenAlex（`api.openalex.org`）、Europe PMC（`www.ebi.ac.uk/europepmc/webservices/rest`）、Crossref（`api.crossref.org`）、Unpaywall（`api.unpaywall.org`）
- **Query strings / 查询式**：
  - OpenAlex：`oa_search.py` 九路 `a`–`i` 布尔矩阵（`title_and_abstract.search` 组合 + `from_publication_date` + `sort=publication_date:desc`）
  - Europe PMC（10 路）：`SC / SP / IM / ME / AL / ST / MO / PR / MACRO2 / SPATIAL_DS`，均带 `PUB_YEAR:2026` 与 `sort=P_PDATE_D desc`
  - 定向深挖：27 基因 `{APOE, MGST1, SPP1, TREM2, HAVCR2, PHGDH, GPI, NDUFS1, NCF1, NPC2, CD44, THBS1, LDHA, PKM2, UBE2C, ZFP57, ECT2, SMDT1, CENPM, KLF6, CTHRC1, LGALS1, SPARC, VSIG4, APOC1, HN1, CCL2}` × `thyroid`，`from_publication_date:2026-06-01`
- **Filters / 过滤**：发表日期窗（30 d / 90 d / PUB_YEAR）；标题须点名甲状腺；整体须为肿瘤主题；撤稿/更正/补充材料/视觉摘要自动降档
- **Deduplication rule / 去重规则**：DOI 主键（小写、剥离 `https://doi.org/`）→ 标题归一化（保留字母数字，截断 90 字符）→ 多版本合并（30 d 30 组、90 d 62 组）
- **Screening rule / 筛查规则**：三通道候选合并后人工判读，逐条标注维度 / 相关性 / 预印本状态 / OA 状态；Graves、桥本、TED、动物甲状腺激素代谢研究列为边界或剔除
- **Enrichment / 增强**：Crossref 22/22 成功；Unpaywall 22/22 成功
- **Files saved / 产出文件**：
  - `literature_review_20261003_010627.md`（本报告）
  - `search_results_20261003_010627.json`（累积基线 457 条）
  - `search_results_latest.json`（同累积基线）
  - `search_results_20261003_010627_30d.json`（OpenAlex 30 d 原始）
  - `search_results_20261003_90day.json`（OpenAlex 90 d 原始）
  - `search_results_20261003_epmc.json`（Europe PMC 10 路候选）
  - `search_results_20261003_deep.json`（27 基因深挖候选）
  - `search_results_20261003_keyabs.json` / `_keyabs_b.json`（关键摘要）
  - `search_results_20261003_010627_enrich.json`（Crossref + Unpaywall 校验结果）
- **Scripts / 脚本**：`_epmc_run27.py`、`_deep_run27.py`、`_keyabs_run27.py`、`_keyabs_run27b.py`、`_enrich_run27.py`、`_final_run27.py`（一次性脚本，按 `_build_*` 惯例不入库）
- **未使用通道**：NCBI eutils / PubMed / GEO / FTP（本机不可达，HTTP 000）；paper-search-mcp（本会话未连接）

---

## 十一、与历史报告的差异 / Delta vs Previous Run (Run #26, 2026-10-02)

| 指标 | Run #26 | Run #27 | 变化 |
|---|---:|---:|---|
| 累积基线 | 391 | **457** | +66 |
| 本轮去重后唯一新增 | 94 | **66** | −28 |
| High / Medium / Low | 21 / 63 / 10 | **12 / 39 / 15** | High 占比 22% → 18% |
| 严格预印本 | 6 | **0** | −6 |
| Europe PMC 路数 | 6 | **10** | +4（MO/PR/MACRO2/SPATIAL_DS） |
| 深挖基因面板 | 22 | **27** | +5（VSIG4/APOC1/HN1/CCL2） |

**新增文献的时间分布**（66 条）：2025-10 至 2025-11 共 3 条；2026-01 至 2026-08 共 **49 条**；2026-09 共 7 条；2026-10 共 5 条；无日期 2 条。

**关键判断：本轮 66 条新增中，只有 7 条发表于上轮（2026-09-25）之后，其余 59 条为历史欠采样回填。** 这不是领域平台期 —— 恰恰相反，它**连续第三轮**证明：本监测序列此前的"低新增"绝大多数来自**查询矩阵覆盖不足**，而非文献真的没产出。本轮把 Europe PMC 从 6 路扩到 10 路（补上此前完全缺失的分子机制 `MO` 与预后转移 `PR` 两路）就一次性回补 56 条，是这一判断最直接的证据。

**相对上轮的新信号 / 方向变化**：

1. 🆕 **载脂蛋白轴从"背景"升为"主轴"**。上轮 APOC1 仅作为 Macro2 signature 的一个成分被提及；本轮它获得三条独立的 PTC 级证据（跨队列 signature + 可药化靶点 + 表观激活），足以单独立为 D21。
2. 🆕 **TAM 从四节点到五节点**。VSIG4⁺（HN1/CEBPB/CCL2）是本轮唯一具备完整因果链 + 体内双靶点验证的新节点。
3. ⬆️ **"红分化"从概念变为可操作机制**。NOX4 轴（PMID 41694580）与 MAPKi/NIS/ARF4（PMID 42236533）提供了两个可检验的组合假设，D18 由 29 升至 31，成为本轮总分最高的方向。
4. ⬆️ **MTC 方向显著加强**。JAMA Otolaryngol 分区复发 + SEER level VII + ProGRP 动力学 + RET 融合耐药，四条独立证据使 D16 由 27 升至 29。
5. ⬇️ **D3″ 正式进入降级程序**。MGST1 零增长第 27 轮，APOE×MGST1 共现仍为 0；同时载脂蛋白家族的活跃度反向说明"MGST1 是这条轴的合适锚点"这一前提本身可能错误。按 Run #26 预设，M5 终判阴性后归档。
6. ⚠️ **D8 反拥挤风险持续升高**。TAM 极化通路已达 5 条，反拥挤分由 3 降至 2，总分 32 → 27（重算口径）。"再描述一个 TAM 亚群"的窗口已基本关闭。
7. 📐 **评分口径变更**。本轮起全部方向按七维明细重算（历史为整体估计、校准偏宽），这是 D8、D9、D11 等历史值出现较大幅度下调的主要原因，**不代表证据倒退**。

---

## 十二、持续跟踪：APOE×MGST1 双轴（D3″）状态 / Standing Tracked Direction Status

**判定：无变化，且"领域结构性空白"的判定进一步坐实 → 建议降级并启动归档程序。**

**量化事实（本轮实测，OpenAlex 全库）**：

| 检索式 | 本轮计数 | 上轮计数 | 变化 |
|---|---:|---:|---|
| `APOE` × `MGST1` × `thyroid` 三词共现 | **0** | 0 | 无变化（连续第 27 轮） |
| `MGST1` × `thyroid`，2026 年 | **1** | 1 | 零增长（10.3389/fimmu.2026.1848083） |
| `APOE` × `thyroid`，2026 年 | **20** | （未记） | 活跃 |
| `APOC1` × `thyroid`，2026 年 | **5** | （未记） | 本轮新增 4 条独立证据 |
| `VSIG4` × `thyroid` | **8** | （未记） | 本轮新增 ATC 因果链 |

**解读**：
- **APOE 侧**：2026 年 20 篇，其中与本方向相关者为 Run #24 的 APOE–NCF1 空间生态位（PMID 42217128）与 Run #25 的 APOE–PINK1/Parkin（PMID 42724858）。APOE 已被反复证实为**促癌**（与最初的"APOE 低表达为干性标志"假设相反）。
- **载脂蛋白家族侧**：APOC1 在本轮获得三条独立 PTC 证据（PMID 42742374 / 41289702 / 42597226）。**家族中真正可操作的节点是 APOC1/APOA1，不是 MGST1。**
- **MGST1 侧**：连续 27 轮、跨越三个通道（OpenAlex 布尔矩阵、Europe PMC、定向基因深挖）均为 0 共现、1 篇文献。

**结论**：原假设「APOE⁻/MGST1⁺ 代谢–免疫干性亚群」中的**互斥关系早已作废**（Run #25 已重构为 APOE×MGST1 双轴），而本轮证据表明**把 MGST1 作为这条轴的锚点本身就是错误前提**。D3″ 的残余价值（APOE 的区室问题）已完整并入 **D21**。

**行动**：按 Run #26 预设，在 D21 的 M5 阶段对 MGST1 做最后一次全通道系统检索；**若仍为 0 共现，将 D3″ 从「候选方向」移入「已检验假设（阴性）」归档区**，并在后续报告中仅在 D21 项下以脚注形式保留 MGST1 作为阴性对照词。

---

*报告结束 / End of report — Run #27, TS `20261003_010627`*
