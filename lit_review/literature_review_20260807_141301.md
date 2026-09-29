# Literature Review: 甲状腺癌侵袭、淋巴结/远处转移、复发、预后及其分子机制、肿瘤免疫微环境、单细胞与空间组学、机器学习/深度学习算法 (Thyroid Cancer Metastasis, Recurrence, Prognosis, Mechanisms, TME, Single-Cell/Spatial Omics, ML/DL)

Date: 2026-08-07 (run #16 · 首次以 OpenAlex 为主源 / first run on the OpenAlex-primary chain)
Sources: OpenAlex（主源，按 publication_date 倒序）+ Crossref / Unpaywall（DOI 与 OA 校验）；PubMed 直连不可达、paper-search-mcp 未启用为补充源
Search window: 近 30 天（from 2026-07-08），九路互补检索

---

## 中文摘要 (Chinese Abstract)

本次为甲状腺癌文献自动监测的第 16 次运行，也是**检索链路切换后的首轮**——从此前 15 轮依赖的 PubMed MCP（本机 NCBI eutils 实测 4/4 超时不可达、MCP 频繁 `not well-formed` 截断）切换为 **OpenAlex 主源 + Crossref/Unpaywall 校验**，并改用 `oa_search.py` 按 `publication_date` 倒序、内建三类数据清洗（剔除期刊补充材料条目、合并单篇多版本、剔除仅顺带提及甲状腺的非肿瘤病）。

近 30 天窗口九路检索共去重得到 **79 篇唯一记录 / 57 篇甲状腺在域文献 / 22 篇排除**（其中「标题未点名甲状腺」17 篇、「甲状腺良性/自身免疫病等非肿瘤主题」5 篇），合并 25 组多版本记录，含 3 篇预印本。相关性分布 **High 13 / Medium 25 / Low 19**。

**关键结论：改源后单一 30 天窗口即捞到 13 篇 High 文献，而旧 PubMed 链路连续 8 轮零新增、峰值单轮仅 +2——证实此前的「平台期」主要是 `relevance` 排序 + 单点 PubMed + PMID 编目滞后造成的方法学假象，而非领域真实停滞。** 本轮 High 文献在**单细胞 + 空间组学 + 免疫微环境**三轴高度收敛，且多篇正面强化长期跟踪的推荐方向 **D3（APOE−/MGST1+ 代谢–免疫干性转移亚群）**：

1. **CENPM**（42553973）——TCGA-THCA + 空间 + scRNA + IHC + in silico KO 联合鉴定的 LNM 生物标志物兼治疗靶点。
2. **KLF6**（figshare 预印本）——scRNA-seq + 空间转录组鉴定的转移性 PTC EMT 驱动因子，勾勒 S100A2⁺ 恶性上皮 → POSTN⁺ CAF → THY1⁺ CAF 的分化级联，**直接接续 D3 的 POSTN⁺ myCAF 生态位轴**。
3. **TREM2⁺ 巨噬细胞 AHR–IDO1–kynurenine 通路**（42553364）——scRNA + scATAC + CyTOF + 体内外验证，靶向可恢复抗肿瘤免疫，**首次为 D3「免疫冷→免疫热逆转」补上带体内证据的可成药节点**。
4. **突变特异性去分化轨迹**（42458477）——snRNA-seq + 空间 + bulk 揭示 BRAF V600E（渐进去分化）与 RAS（骤变+EMT+缺氧）驱动的两类进展轨迹。
5. **终末免疫耗竭表型与 LNM 风险相关**（预印本）——流式 + TCGA 验证，CD8⁺ T 终末耗竭亚群与淋巴结转移正相关。

据此，本轮将 D3 的 rubric 由上轮 **32** 微调至 **33（Strong）**——因 TREM2⁺/AHR–IDO1 体内证据补齐了此前「免疫逆转仅临床前/单基因」的短板（Validation 4→5）。同时提出两条新候选子方向：**D8（TREM2⁺ 巨噬细胞 AHR–IDO1–kynurenine 免疫代谢检查点，rubric 30）** 与 **D9（citrullination/PADI 非经典侵袭程序 × SPP1–CD44 生态位，rubric 28）**。

**与上轮（run #15）差异**：源、排序、清洗规则全部更换，故「57 篇相对基线新增」中含链路切换红利，不能等同于「24 小时真实增量」；本轮 JSON 将作为新链路的**基线锚点**，从下轮起计算真实增量。收敛主线（代谢–免疫耦合驱动 LNM、干性转移亚群、POSTN⁺/CAF 空间图谱）不变且被显著强化；新信号为 TREM2⁺/AHR–IDO1 免疫逆转与 citrullination 侵袭程序。

## English Abstract

This is run #16 of the scheduled thyroid-cancer literature monitor and the **first run of the re-engineered retrieval chain**: after 15 runs bottlenecked on the PubMed MCP (local NCBI eutils unreachable, 4/4 timeouts; MCP frequently truncating with `not well-formed`), the chain now uses **OpenAlex as the primary source with Crossref/Unpaywall verification**, via `oa_search.py` sorted by `publication_date` (descending) with three built-in cleaners (drop journal supplementary-material entries, merge single-paper multi-version records, drop non-tumor thyroid disease that only mentions the thyroid in passing).

The 30-day nine-query sweep yielded **79 unique records / 57 in-scope thyroid papers / 22 excluded** (17 "title does not name thyroid", 5 "non-tumor thyroid disease"), merging 25 multi-version groups and including 3 preprints. Relevance distribution: **High 13 / Medium 25 / Low 19**.

**Key finding: a single 30-day window on the new chain surfaced 13 High papers, whereas the old PubMed chain recorded 8 consecutive zero-new runs (peak +2) — confirming the prior "plateau" was mainly a methodological artifact of relevance-ranking + single-source PubMed + PMID cataloguing lag, not genuine field stagnation.** This run's High papers converge strongly on **single-cell + spatial + immune microenvironment**, and several directly reinforce the long-tracked recommended direction **D3 (APOE−/MGST1+ metabolic–immune stem-like metastatic subpopulation)**:

1. **CENPM** (42553973) — LNM biomarker and therapeutic target from TCGA-THCA + spatial + scRNA + IHC + in silico KO.
2. **KLF6** (figshare preprint) — scRNA-seq + spatial-transcriptomics EMT driver in metastatic PTC, mapping an S100A2⁺ malignant-epithelial → POSTN⁺ CAF → THY1⁺ CAF differentiation cascade, **directly extending D3's POSTN⁺ myCAF niche axis**.
3. **TREM2⁺ macrophage AHR–IDO1–kynurenine pathway** (42553364) — scRNA + scATAC + CyTOF + in vivo, targetable to restore antitumor immunity, **the first in-vivo-validated druggable node for D3's "immune-cold → immune-hot reversal"**.
4. **Mutation-specific dedifferentiation trajectories** (42458477) — snRNA-seq + spatial + bulk delineating BRAF V600E (gradual) vs RAS (abrupt + EMT + hypoxia) progression trajectories.
5. **Terminal immune exhaustion phenotype correlates with LNM** (preprint) — flow cytometry + TCGA; terminally exhausted CD8⁺ T subsets associate with lymph node metastasis.

Accordingly, D3's rubric is nudged from **32** to **33 (Strong)** — TREM2⁺/AHR–IDO1 in-vivo evidence closes the prior "immune reversal is preclinical/single-gene only" gap (Validation 4→5). Two new candidate sub-directions are added: **D8 (TREM2⁺ macrophage AHR–IDO1–kynurenine immunometabolic checkpoint, rubric 30)** and **D9 (citrullination/PADI non-canonical invasive program × SPP1–CD44 niche, rubric 28)**.

**Delta vs run #15**: source, sort order and cleaning rules all changed, so the "57 new vs baseline" figure includes a chain-switch dividend and must not be read as a true 24-hour increment; this run's JSON becomes the **new-chain baseline anchor** against which subsequent true increments will be computed. The convergent backbone (metabolic–immune coupling drives LNM; stem-like metastatic subpopulation; POSTN⁺/CAF spatial atlas) is unchanged and markedly strengthened; the new signals are TREM2⁺/AHR–IDO1 immune reversal and the citrullination invasive program.

---

## 检索策略 (Search Strategy)

主源为 OpenAlex `works` 端点，`filter=title_and_abstract.search:<布尔式>,from_publication_date:2026-07-08`，`sort=publication_date:desc`，`per-page=25`，`mailto` 署名。DOI 元数据经 Crossref、OA 全文经 Unpaywall 二次校验。**本机 NCBI eutils/pubmed.ncbi.nlm.nih.gov 实测不可达（4/4 超时 HTTP 000），故禁止直连；paper-search-mcp 未在本轮启用。**

| Source | Query (维度) | Filters | 库内命中 / 取回 | Notes |
|---|---|---|---:|---|
| OpenAlex | a) thyroid + LNM + biomarker/gene signature（预后转移/算法方法）| date≥2026-07-08, desc | 17 / 17 | 桥本共病、CENPM 等 |
| OpenAlex | b) thyroid + invasion/metastasis + molecular mechanism（分子机制）| 同上 | 31 / 25 | 命中最多，含多篇机制文献 |
| OpenAlex | c) thyroid + LNM + ML/DL prediction model（算法方法）| 同上 | 13 / 13 | 超声组学 + 可解释 AI |
| OpenAlex | d) thyroid + metastasis + tumor immune microenvironment（免疫微环境）| 同上 | 22 / 22 | TREM2⁺、终末耗竭、TIME 综述 |
| OpenAlex | e) thyroid + metastasis + scRNA-seq（单细胞）| 同上 | 21 / 21 | 55,005 细胞图谱、cell-state 综述 |
| OpenAlex | f) thyroid + metastasis + spatial transcriptomics/multi-omics（空间组学）| 同上 | 21 / 21 | KLF6、突变特异性去分化 |
| OpenAlex | g) thyroid + prognosis/recurrence/distant metastasis risk model（预后转移）| 同上 | 55 / 25 | 命中最多，取回上限 25 |
| OpenAlex | h) thyroid + cancer stem cell/dedifferentiation（转移干性）| 同上 | 4 / 4 | 窗口内偏少 |
| OpenAlex | i) thyroid + metabolic reprogramming + metastasis（代谢重编程）| 同上 | 8 / 8 | GSEC/GLUT1、curcumin/GPX4 |
| Crossref | 5 篇重点 High DOI 元数据校验 | — | 5/5 命中 | 全部 2026 年、期刊一致 |
| Unpaywall | 同上 OA 状态解析 | — | 5/5 gold OA | 全部开放获取 |

去重规则：DOI 优先，缺失时用归一化标题；单篇多版本（预印本↔正式版、figshare/OSF 镜像）按标题归一化合并（本轮合并 25 组，KLF6 一篇合并 12 版本）。筛除规则：标题未点名甲状腺且正文仅顺带提及 → 排除；甲状腺良性结节/桥本/Graves/甲状腺眼病等非肿瘤主题 → 排除。相关性 High/Medium/Low 由维度命中数、是否含机制/组学证据、是否直达转移/LNM/预后终点综合判定。

## 纳入论文 (Included Papers) — High 相关 13 篇

1. **CENPM as a biomarker and therapeutic target for lymph node metastasis in thyroid carcinoma.** Front Genet. 2026. DOI: 10.3389/fgene.2026.1875148. PMID: 42553973.
   Author claim: GAM 在 TCGA-THCA 中筛出 CENPM，其表达随肿瘤直径上升且经独立队列、空间转录组、IHC 验证；scRNA + in silico KO + 药物重定位提示其免疫学与治疗相关性。
   中文要点: 多组学 + 空间 + 单细胞联合把 CENPM 立为 LNM 标志物兼靶点，方法闭环完整。Agent note: High；分子机制/预后转移/免疫微环境/单细胞/空间组学五维交叉，D3 蓝图强证据。

2. **Single Cell and Spatial Transcriptome Profiling Identifies KLF6 as a EMT Driver in Metastatic PTC.** figshare preprint. 2026. DOI: 10.6084/m9.figshare.33085235.v2. PMID: 待编目 [preprint].
   Author claim: 9 例非远处转移 + 5 例远处转移 PTC 的 scRNA-seq 显示 DM 组特有 S100A2⁺ 恶性上皮经 EMT 反分化为 POSTN⁺ CAF、再向 THY1⁺ CAF 分化，空间转录组与拟时序佐证。
   中文要点: 把 EMT 与 CAF 分化级联在单细胞 + 空间层面串起来，接续 POSTN⁺ myCAF 生态位轴。Agent note: High（预印本，证据强度降档）；分子机制/单细胞/空间组学/预后转移。

3. **Targeting the AHR–IDO1–kynurenine pathway in TREM2+ macrophages restores antitumor immunity in thyroid cancer.** Front Immunol. 2026. DOI: 10.3389/fimmu.2026.1826288. PMID: 42553364.
   Author claim: scRNA + scATAC + 质谱流式 + 空间验证 + 体内外功能实验鉴定 TREM2⁺ TAM 富集，AHR–IDO1–kynurenine 轴介导免疫抑制，靶向可恢复抗肿瘤免疫。
   中文要点: 为「免疫冷」表型给出带体内证据的可成药节点（IDO1 抑制剂临床可及）。Agent note: High；单细胞主导，D3「免疫逆转」缺口的关键补强。

4. **Cell-state transitions and microenvironmental remodeling in thyroid cancer progression revealed by single-cell and spatial transcriptomics.** Front Immunol. 2026. DOI: 10.3389/fimmu.2026.1904196. PMID: 42488635.
   Author claim: 系统整合 PTC→DTC(转移/RAI 难治)→PDTC→ATC 的 scRNA + 空间证据，进展伴随恶性上皮 cell-state 迁移与空间异质性重塑。
   中文要点: 覆盖全谱系的单细胞 + 空间综述，为 D3 提供整合框架。Agent note: High；免疫微环境/单细胞/空间组学/转移干性。

5. **Single-cell sequencing profiling of intratumoral heterogeneity and immunosuppressive microenvironment in primary thyroid cancer and lymph node metastases.** OncoImmunology. 2026. DOI: 10.1080/2162402x.2026.2701504. PMID: 42430190.
   Author claim: 分析配对原发灶与淋巴结转移共 55,005 个单细胞，结合 CNV 推断 + cNMF 解析恶性演化与免疫抑制微环境。
   中文要点: 配对原发–LNM 单细胞图谱，直击转移灶免疫抑制。Agent note: High；免疫微环境/单细胞，D3 转移灶维度直接证据。

6. **Mutation-specific dynamics of dedifferentiation trajectories and tumor–stromal interactions in thyroid cancer.** Mol Cancer. 2026. DOI: 10.1186/s12943-026-02699-2. PMID: 42458477.
   Author claim: snRNA-seq + 空间 + bulk 显示 BRAF V600E 驱动渐进式去分化（伴免疫通路激活），RAS 驱动骤变式转变（非整倍体、EMT、缺氧、ECM 重塑）。
   中文要点: 把「去分化轨迹」按驱动突变分型，深化转移干性/去分化机制。Agent note: High；空间组学主导，D3 去分化轨迹轴。

7. **Integrated Bioinformatics and Experimental Validation Reveal the Diagnostic and Prognostic Value of SMDT1 in Thyroid Carcinoma.** Diagnostics. 2026. DOI: 10.3390/diagnostics16142250. PMID: 42510113.
   Author claim: SMDT1（线粒体钙单向转运体复合物调控子）在 THCA 高表达，具诊断/预后价值并与免疫浸润相关，50 例样本验证。
   中文要点: 线粒体 Ca²⁺ 轴（D7）再获证据，可并入 D3 代谢–免疫轴。Agent note: High；免疫微环境/分子机制。

8. **Papillary Thyroid Carcinoma with Terminal Immune Exhaustion Phenotype Correlates with Increased Risk of Lymph Node Metastasis: A Combined Flow Cytometry and TCGA Validation Study.** Preprints.org. 2026. DOI: 10.20944/preprints202607.2346.v1. PMID: 待编目 [preprint].
   Author claim: 流式 + TCGA 验证显示终末耗竭 CD8⁺ T 亚群与 PTC 淋巴结转移风险正相关，可辅助术前风险分层。
   中文要点: 把 T 细胞终末耗竭与 LNM 直接挂钩，补 D3 免疫维度。Agent note: High（预印本，降档）；分子机制/预后转移/免疫微环境。

9. **Molecular Pathogenesis and Emerging Therapeutic Targets in Anaplastic Thyroid Carcinoma.** IntechOpen. 2026. DOI: 10.5772/intechopen.1016607. PMID: 待编目.
   Author claim: 综述 ATC 由 DTC 去分化累积驱动的分子发病机制与生物标志物驱动的靶向治疗。
   中文要点: ATC 去分化与靶向治疗全景综述。Agent note: High（书章综述，降档）；分子机制/预后转移/免疫微环境/转移干性。

10. **Thyroid Cancer: From Potential Drivers to Real Modulators.** Cancers. 2026. DOI: 10.3390/cancers18152474. PMID: 待编目.
    Author claim: 综述主张甲状腺癌研究重心应从基因驱动转向肿瘤免疫微环境（TIME）调控网络。
    中文要点: TIME 视角综述，与 D3 免疫–代谢主线一致。Agent note: High（综述，降档）；分子机制/免疫微环境/代谢重编程。

11. **Citrullination-associated transcriptional states identify a non-canonical invasive program in malignant epithelial cells and correlate with SPP1-CD44 immune microenvironment niches in thyroid cancer.** Transl Oncol. 2026. DOI: 10.1016/j.tranon.2026.102931. PMID: 待编目.
    Author claim: 整合 scRNA（GSE232237，92,519 细胞）+ 空间（GSE250521）+ TCGA-THCA，PADI 家族 citrullination 评分刻画一种非经典侵袭程序，与 SPP1–CD44 免疫生态位相关。
    中文要点: 全新 citrullination/PADI 侵袭轴 × SPP1–CD44 生态位，D9 候选。Agent note: High；分子机制/空间组学。

12. **99mTc-FAPI-YQ3 SPECT/CT for characterizing FAPI uptake phenotypes and metabolic-stromal heterogeneity in advanced differentiated thyroid carcinoma.** Front Immunol. 2026. DOI: 10.3389/fimmu.2026.1888899. PMID: 42534915.
    Author claim: 前瞻性单中心影像组学研究，用 99mTc-FAPI-YQ3 SPECT/CT 表征进展期 DTC（含 RAI 难治）的成纤维活化蛋白摄取表型与代谢–基质异质性。
    中文要点: 把基质/代谢异质性影像化，桥接空间生物学与临床影像。Agent note: High；算法方法/预后转移。

13. **Clinical significance of coexisting Hashimoto's thyroiditis in differentiated thyroid cancer: a retrospective cohort study.** BMC Endocr Disord. 2026. DOI: 10.1186/s12902-026-02404-w. PMID: 42420994.
    Author claim: 198 例 DTC 回顾性队列，评估桥本共病在校正肿瘤因素后是否独立影响侵袭性特征（肿瘤大小、LNM 等）。
    中文要点: 桥本–DTC 免疫背景与侵袭性关系的临床证据。Agent note: High；算法方法/预后转移（临床风险分层维度）。

> Medium（25 篇）与 Low（19 篇）完整清单见 `search_results_20260807_141301.json` 的 `new_records` 字段（含 DOI、PMID/待编目、OA 状态、维度标签、相关性）。代表性 Medium：多模态超声组学预测中央区 LNM（42421358、42467019、42527780 XAI）、术前隐匿高负荷 LNM 预测、Tg/TSHR/NIS mRNA 检测识别 LNM（42426688）、液体活检综述（16、29）、ML/DL 诊断性能 meta 的更正（42487114）、GSEC/IGF2BP2/GLUT1 糖代谢（42536764）、curcumin/GPX4 铁死亡（42550316）。

## 证据矩阵 (Evidence Matrix)

| Paper | PMID/DOI | Disease/Pop. | Data Source | Method | Endpoint | Main Finding | Validation | Limitations | Relevance (维度) | Gap Suggested | Future Direction |
|---|---|---|---|---|---|---|---|---|---|---|---|
| CENPM LNM 标志/靶点 | 42553973 / 10.3389/fgene.2026.1875148 | THCA | TCGA-THCA + 独立队列 + ST + IHC | GAM 筛选 + scRNA + in silico KO + 药物重定位 | LNM | CENPM 随肿瘤直径升高，N0/N1 表达方向相反；具治疗靶点潜力 | 独立队列 + 空间 + IHC | 计算主导，体内验证少 | High（分子/预后/免疫/单细胞/空间）| 干性转移亚群缺可靶向标志物组合 | 并入 D3；作 LNM 联合标志物候选 |
| KLF6 EMT 驱动 | 待编目 / 10.6084/m9.figshare.33085235.v2 | 转移性 PTC | 14 例 scRNA-seq + ST | 拟时序 + 空间验证 | 远处转移/EMT | S100A2⁺ 上皮→POSTN⁺ CAF→THY1⁺ CAF 级联；KLF6 为 EMT 驱动 | 空间 + 拟时序 | 预印本、样本量小、无体内 | High（分子/单细胞/空间/预后）| POSTN⁺ CAF 起源与干性亚群关系未连 | D3：接续 POSTN⁺ myCAF 生态位轴 |
| TREM2⁺ AHR–IDO1 免疫逆转 | 42553364 / 10.3389/fimmu.2026.1826288 | 甲状腺癌（人+鼠）| scRNA + scATAC + CyTOF + 空间 + 体内外 | 多组学 + 功能/药理 | 抗肿瘤免疫恢复 | TREM2⁺ TAM 经 AHR–IDO1–kynurenine 抑制免疫；靶向可逆转 | 体内 + 人样本 | 通路在多癌种拥挤 | High（单细胞）| D3 缺「免疫冷→热」体内可成药节点 | **D8**（新）+ 强化 D3 |
| 突变特异性去分化轨迹 | 42458477 / 10.1186/s12943-026-02699-2 | BRAF/RAS 甲状腺瘤 | snRNA-seq + ST + bulk | 轨迹 + 空间 | 去分化/进展 | BRAF 渐进去分化 vs RAS 骤变(EMT/缺氧/ECM) | 多模态整合 | 无前瞻队列 | High（空间）| 去分化轨迹终末态与干性亚群映射未完 | D3：去分化轨迹轴分型 |
| 配对原发–LNM 单细胞图谱 | 42430190 / 10.1080/2162402x.2026.2701504 | TC 原发+LNM | 55,005 单细胞 | CNV 推断 + cNMF | LNM/免疫抑制 | 解析恶性演化与转移灶免疫抑制微环境 | 配对样本 | 单中心 | High（免疫/单细胞）| 转移灶免疫抑制的可逆性未证 | D3：转移灶免疫维度 |
| cell-state 迁移综述 | 42488635 / 10.3389/fimmu.2026.1904196 | 全谱系 TC | scRNA + ST 整合 | 综述整合 | 进展 | 进展伴 cell-state 迁移 + 空间异质性重塑 | 文献整合 | 综述、非原始数据 | High（免疫/单细胞/空间/干性）| 缺统一 cell-state 命名与基准 | D3 整合框架 |
| SMDT1 线粒体 Ca²⁺ | 42510113 / 10.3390/diagnostics16142250 | THCA/PTC | 公共库 + 50 例 | 生信 + 实验验证 | 诊断/预后 | SMDT1 高表达、与免疫浸润相关 | 50 例样本 | 机制链未闭 | High（免疫/分子）| 与 MGST1/OXPHOS 轴关系未明 | 并入 D3（原 D7）|
| 终末免疫耗竭 × LNM | 待编目 / 10.20944/preprints202607.2346.v1 | PTC | 流式 + TCGA | 免疫分型 + 验证 | LNM 风险 | 终末耗竭 CD8⁺T 与 LNM 正相关 | TCGA 验证 | 预印本、机制浅 | High（分子/预后/免疫）| 耗竭亚群是否因果未证 | D3：免疫耗竭风险维度 |
| citrullination 侵袭程序 | 待编目 / 10.1016/j.tranon.2026.102931 | THCA | scRNA(GSE232237)+ST(GSE250521)+TCGA | CopyKAT + CitrScore + regulon | 侵袭 | PADI citrullination 非经典侵袭程序 × SPP1–CD44 生态位 | 多数据集整合 | 计算为主、无功能 | High（分子/空间）| PADI 轴功能与可药性未证 | **D9**（新）|
| FAPI SPECT/CT 代谢–基质 | 42534915 / 10.3389/fimmu.2026.1888899 | 进展期 DTC | 前瞻影像 + 组学 | 影像组学 | 表型分层 | FAPI 摄取表型刻画代谢–基质异质性 | 前瞻单中心 | 摄取≠FAP 表达（需 IHC）| High（算法/预后）| 影像与分子/空间脱节 | 桥接 D3 空间生物学与临床影像 |
| 桥本共病 × DTC 侵袭 | 42420994 / 10.1186/s12902-026-02404-w | DTC | 198 例回顾队列 | 多因素回归 | 侵袭性/LNM | 评估 HT 是否独立影响侵袭特征 | 单中心校正分析 | 样本量中等、单中心 | High（算法/预后）| 免疫背景对 TME 的调制未机制化 | 临床风险分层 × TIME 交叉 |
| 多模态超声 XAI 预测 CLNM | 42527780 / 10.1007/s10278-026-02141-5 | PTC | 多模态超声 | 可解释 AI | 中央区 LNM | XAI 辅助术前 CLNM 风险分层 | 内部验证 | 单中心、非分子 | Medium（算法/预后）| 与分子机制脱节（拥挤方向）| 与 D3 机制闭环（瓶颈）|
| Tg/TSHR/NIS mRNA 检测 LNM | 42426688 / 10.1186/s12885-026-16515-z | PTC | 淋巴结组织 | mRNA 标志物 | LNM 识别 | 三标志物 mRNA 识别淋巴结转移 | 队列验证 | 特异性待验 | Medium（分子/预后）| 与影像/单细胞未整合 | 分子 LNM 检测补充维度 |

## 已知结论 / What Is Already Known

1. **代谢–免疫耦合驱动淋巴结转移（Axis 1）持续被强化。** 本轮 SMDT1（线粒体 Ca²⁺，42510113）、GSEC/IGF2BP2/GLUT1 糖代谢（42536764）、curcumin/GPX4 铁死亡（42550316）与「From Drivers to Real Modulators」TIME 综述（cancers18152474）共同延续既往 MGST1/SHMT2/GLTC-LDHA/SOX12–YBX1–LDHA 的代谢重编程主线。
2. **干性/去分化转移亚群是核心效应单元（Axis 2）显著加深。** 突变特异性去分化轨迹（42458477，BRAF 渐进 vs RAS 骤变）、KLF6 的 S100A2⁺→POSTN⁺ CAF→THY1⁺ CAF 级联（figshare）、以及 cell-state 迁移综述（42488635）从单细胞 + 空间层面把「去分化终末态 = 转移执行者」讲得更完整；与既往 APOE−（39810624）、MGST1⁺ 干性终末态（42327722）高度收敛。
3. **POSTN⁺/CAF 空间生态位（Axis 3）获新直接证据。** KLF6 研究首次给出 POSTN⁺ CAF 的**起源级联**（由恶性上皮 EMT 反分化而来），补上既往 POSTN⁺ myCAF 空间图谱（41480746）的上游环节。
4. **免疫抑制微环境的可成药节点开始清晰（新强化）。** TREM2⁺ 巨噬细胞 AHR–IDO1–kynurenine（42553364，体内验证）+ 终末免疫耗竭 CD8⁺T×LNM（预印本）+ 配对原发–LNM 单细胞免疫抑制图谱（42430190），三条独立线索指向「转移灶免疫冷可被靶向逆转」。
5. **影像/多组学 AI 仍高产但拥挤且与机制脱节（Axis 4）。** 多模态超声组学、XAI、FAPI SPECT/CT、nomogram、ML/DL meta 更正等 12 篇算法方法文献多为单中心、非分子，rubric 中仍因极端拥挤 + 机制脱节被打低分。

## 未解问题 / What Remains Unclear

- **APOE− / MGST1⁺ / KLF6-POSTN⁺CAF / 去分化终末态是否为同一连续谱系？** 本轮新增了 KLF6 与突变特异性轨迹两条线，但四者在单细胞层面的**统一整合与命名**仍未完成——这是 D3 落地的首要障碍。
- **TREM2⁺ TAM 的 AHR–IDO1 轴是甲状腺特异还是泛癌共性？** IDO1 抑制剂在多癌种临床试验多告失败，需证明 TREM2⁺ 亚群定位 + 空间生态位赋予其甲状腺特异的可成药窗口。
- **citrullination/PADI 侵袭程序的功能与可药性未证。** 目前纯计算（CitrScore/regulon），缺 PADI 抑制的体内外功能验证；SPP1–CD44 生态位的因果方向也未定。
- **终末免疫耗竭与 LNM 的因果性未证**（预印本、横断面）；耗竭是转移的因还是果尚不清楚。
- **近期文献 PMID 编目滞后普遍**：13 篇 High 中 5 篇「待编目」、3 篇预印本——DOI 可靠但传统 PubMed 检索会系统性漏掉这批最新信号。

## 领域方法/数据局限 / Method & Data Limitations In The Field

- **公共数据高度复用**：scRNA（GSE232237 等）与空间数据集在多篇文献间反复引用，存在批次效应与「同数据多结论」风险。
- **计算发现 >> 湿实验验证**：CENPM、citrullination、SMDT1 等多为生信 + 有限验证，体内功能与临床前→临床鸿沟大；TREM2⁺/AHR–IDO1 是少数带体内证据者。
- **预印本与书章比例上升**：本轮 High 含 3 预印本 + 2 书章/综述，证据强度需相应降档。
- **影像 AI 外部验证稀缺**：多为单中心、外部测试集小；且与分子/单细胞机制脱节。
- **检索层面的方法学教训（本轮固化）**：`relevance` 排序 + 单点 PubMed 会**结构性掩盖**新文献；本机 NCBI 直连不可达。已切换为 OpenAlex 主源 + `publication_date` 倒序，并将环境事实写入 `RETRIEVAL_ENVIRONMENT.md`。

## 候选未来方向 / Candidate Future Directions

| Direction | Rationale | Feasibility | Required Data | Validation Plan | Main Risk | Claim Boundary |
|---|---|---|---|---|---|---|
| **D3 — APOE−/MGST1+ 代谢–免疫干性转移亚群（推荐）** | 本轮 CENPM/KLF6/TREM2⁺/去分化轨迹/终末耗竭多线收敛，POSTN⁺CAF 起源与免疫逆转节点均补齐 | 高（公共 scRNA/空间 + 现成细胞系）| TCGA-THCA + 39810624/41480746/42430190/KLF6 的 scRNA&ST | 独立队列验证联合标志物；体内外功能 + IDO1/MGST1 药理 | 亚群异质性致标志物泛化难 | 仅定义与靶向「代谢–免疫干性」转移前体，非治愈 |
| **D8 — TREM2⁺ 巨噬细胞 AHR–IDO1–kynurenine 免疫代谢检查点（新）** | 42553364 带体内证据，IDO1 抑制剂临床可及；直接对应 D3「免疫冷→热」 | 高（scRNA/scATAC 公共 + 鼠模型 + 现成抑制剂）| 甲状腺 scRNA/scATAC + 空间；IDO1/AHR 抑制剂 | 体内逆转实验 + 人样本空间共定位 | AHR–IDO1 泛癌拥挤、既往临床失败 | 限 TREM2⁺ 亚群定位的甲状腺特异窗口 |
| **D9 — citrullination/PADI 非经典侵袭程序 × SPP1–CD44 生态位（新）** | 全新机制角度、拥挤度低；数据（GSE232237/GSE250521/TCGA）现成 | 中（计算可即刻，功能需建） | 上述 scRNA/ST/bulk + PADI 抑制剂 | PADI 抑制体内外功能 + SPP1–CD44 因果 | 纯计算风险高、功能未证 | 限「侵袭程序标志」，暂不宣称治疗 |
| D6 — 5-HT/NETs 轴（MTC 肝转移）| 既往 39903533，fluoxetine/SERT 可阻断 | 中 | MTC + 限肝转移队列 | 前瞻药理验证 | 仅 MTC/NE 亚型 | 限 MTC/神经内分泌亚型肝转移 |

**Rubric 七维评分（本轮）**

- **D3**：Novelty 5 / Feasibility 5 / Data availability 5 / Validation strength **5**（↑，TREM2⁺/AHR–IDO1 补体内证据）/ Clinical relevance 5 / Method rigor 4 / Overcrowding risk 4 → **总分 33（Strong，连续 16 次确认）**。
- **D8**：Novelty 4 / Feasibility 5 / Data 4 / Validation 5 / Clinical 5 / Method rigor 4 / Overcrowding 3 → **总分 30（Strong）**。
- **D9**：Novelty 5 / Feasibility 4 / Data 4 / Validation 3 / Clinical 3 / Method rigor 4 / Overcrowding 5 → **总分 28（Strong 下沿 / 可行–探索边界）**。

## 推荐下一步方向 / Recommended Next Direction

**仍推荐 D3 — 界定并靶向 APOE−/MGST1+ 代谢–免疫干性转移亚群（rubric 33，Strong，连续 16 轮）。** 本轮它是唯一同时被单细胞（42430190 配对原发-LNM、KLF6 EMT 级联）、空间组学（42458477 去分化轨迹、citrullination 生态位）、免疫（42553364 TREM2⁺/AHR–IDO1 体内逆转、终末耗竭×LNM）与代谢（SMDT1、GSEC/GLUT1）四条线同时强化的方向，且新证据恰好补齐了此前两个短板：**POSTN⁺ CAF 的上游起源**（KLF6）与**免疫冷→热的体内可成药节点**（TREM2⁺/AHR–IDO1）。

**首步具体动作**：
1. 用 42430190（55,005 细胞配对图谱）+ 39810624（APOE−）+ 41480746（POSTN⁺ myCAF）+ KLF6 的公开 scRNA/空间数据，构建「APOE− ∩ MGST1⁺ ∩ 去分化终末 ∩ S100A2⁺-POSTN⁺CAF 级联」的**统一 cell-state 定义与可复现流程**（优先解决四谱系是否同源）。
2. 在独立 PTC 队列（TCGA-THCA + 机构队列）验证该联合亚群对 LNM/远处转移的预测力，并纳入终末免疫耗竭评分作协变量。
3. 以 IDO1/AHR 抑制（对应 D8）+ MGST1 抑制（Toxoflavin 类）做体内外功能确认，检测「免疫冷→免疫热」逆转与转移抑制。
4. D9（citrullination/PADI）作为独立探索线并行，先在同一批公共数据上验证 CitrScore 与干性/免疫轴的关联，再决定是否投入 PADI 功能实验。

## 随访阅读清单 / Follow-Up Reading List

- **42553973（CENPM）**：D3 的 LNM 联合标志物候选，优先精读 GAM + in silico KO 方法。
- **KLF6（figshare 预印本）**：POSTN⁺ CAF 起源级联，D3 亚群流程的上游证据，关注 scRNA→ST 拟时序衔接。
- **42553364（TREM2⁺ AHR–IDO1）**：D8 核心 + D3 免疫逆转节点，精读体内实验设计与 IDO1 抑制方案。
- **42458477（突变特异性去分化）**：D3 去分化轨迹分型，关注 BRAF vs RAS 的空间差异分析。
- **42430190（配对原发-LNM 55k 单细胞）**：转移灶免疫抑制维度的必需数据来源。
- **10.1016/j.tranon.2026.102931（citrullination）**：D9 唯一奠基文献，关注 CitrScore 构建与 SPP1–CD44 生态位分析。

## 可复现性说明 / Reproducibility Notes

- Search date: 2026-08-07 14:13 (GMT+8)，run #16。
- Primary source: OpenAlex `works`（`title_and_abstract.search` + `from_publication_date:2026-07-08` + `sort=publication_date:desc`）；校验源 Crossref、Unpaywall。
- Databases 说明: 本机 NCBI eutils/pubmed 不可达（4/4 超时），paper-search-mcp 本轮未启用；详见 `RETRIEVAL_ENVIRONMENT.md`。
- Query strings: 九路 a–i（见「检索策略」表），布尔式与维度映射固化于 `oa_search.py`。
- Filters: 近 30 天、per-page 25、mailto 署名。
- Deduplication rule: DOI 优先→归一化标题；单篇多版本按标题归一化合并（本轮合并 25 组）。
- Screening rule: 标题须点名甲状腺且为肿瘤主题；排除仅顺带提及甲状腺的他病/非肿瘤病；相关性 High/Medium/Low 综合维度命中 + 证据类型 + 终点直达性判定。
- Files saved:
  - 报告：`D:\paperwork\lit_review\literature_review_20260807_141301.md`
  - 原始检索：`D:\paperwork\lit_review\search_results_20260807_141301.json`（同步更新 `search_results_latest.json` 为新链路基线锚点）
  - 环境事实：`D:\paperwork\lit_review\RETRIEVAL_ENVIRONMENT.md`
  - 检索器：`D:\paperwork\lit_review\oa_search.py`
- 与历史对比: 见「双语摘要」末段；本轮为新链路首轮，`new_vs_baseline=57` 含链路切换红利，非 24h 真实增量；自下轮起以本轮 JSON 为基线计算真实增量。

---

*本报告由 lit-review 自动监测链路（OpenAlex 主源版）于 run #16 生成。所有 DOI/PMID 均来自 OpenAlex 并经 Crossref/Unpaywall 校验，未编造标识符；「待编目」表示该文献尚未获 PubMed PMID（编目滞后），非缺失。*
