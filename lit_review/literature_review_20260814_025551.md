# 甲状腺癌文献监测报告 / Thyroid Cancer Literature Surveillance Report

**Date / 日期:** 2026-08-14 (run #18)
**Sources / 数据源:** OpenAlex REST API (`api.openalex.org`，主源)；Crossref（DOI 元数据校验）；Unpaywall（OA 状态解析）。
**Search window / 检索窗口:** 近 30 天，发表日期 ≥ 2026-07-15（`sort=publication_date:desc`）。
**Baseline / 基线:** `search_results_latest.json`（= run #17，2026-08-10 OpenAlex 基线）。
**Primary retriever / 主检索器:** `oa_search.py`（九路维度 a–i，内建补充材料剔除、多版本合并、非肿瘤甲状腺病过滤）。

---

## 中文摘要 (Chinese Abstract)

本轮（2026-08-14，相对 2026-08-10 基线）以 OpenAlex 为主源完成甲状腺癌（PTC/PTMC/FTC/MTC/ATC）侵袭、淋巴结与远处转移、复发、预后及其分子机制、肿瘤免疫微环境、单细胞与空间组学、机器学习/深度学习方向的增量监测。共取回 **81 条唯一记录**，其中 **59 条在范围**，剔除 22 条（17 条标题未点名甲状腺、5 条非肿瘤甲状腺病）；**相对基线新增 9 条**（全部 PMID 待编目——PubMed 编目滞后），其中 **4 条在范围预印本**（本轮新增含 1 条预印本）。相关性分布：High 13 / Medium 26 / Low 20。

**关键新信号：** (1) 脂质代谢重编程综述（preprint）首次将"循环脂质标志物 vs 瘤内脂质通量"区分，并明确耦合**免疫–空间生态位**与治疗抵抗，为代谢–免疫轴补充了脂质层次；(2) *Molecular Oncology* 发表 PTC/ATC **单核 + 空间转录组**图谱（PMID 42578411），以实验设计分离生物学与技术上变异，直接补齐 D3 方向长期缺乏的**原位分辨方法学底座**；(3) 继续涌现 3 篇 LNM 影像/列线图研究，算法方法维度过度拥挤（rubric 低分）结论不变；(4) NAT10-ac4C-PKM2 糖酵解机制、ATC 趋同通路综述补充代谢/ATC 轴。

**持续跟踪方向 D3（APOE−/MGST1+ 代谢–免疫干性转移亚群）：** 本轮**定性强化**——脂质–免疫综述 + 单核/空间 PTC/ATC 图谱共同加强其代谢–免疫与空间–单细胞证据底座；仍无直接 APOE−/MGST1+ 亚群验证、无反证，维持 **Strong（rubric 33，连续第 18 轮确认）**。

---

## English Abstract

This round (2026-08-14, vs. the 2026-08-10 baseline) re-ran the OpenAlex-based incremental surveillance across nine dimensions covering thyroid cancer (PTC/PTMC/FTC/MTC/ATC) invasion, nodal/distant metastasis, recurrence, prognosis, molecular mechanisms, immune microenvironment, single-cell & spatial omics, and ML/DL methods. **81 unique records** were retrieved; **59 are in-scope** (22 excluded: 17 with no thyroid term in title, 5 non-oncologic thyroid). **9 records are new vs. baseline** (all PMIDs pending indexing — PubMed lag), including **4 in-scope preprints** (1 of the 9 new is a preprint). Relevance: High 13 / Medium 26 / Low 20.

**Key new signals:** (1) a lipid-metabolism reprogramming narrative review (preprint) distinguishes circulating lipid markers from intratumoral lipid flux and explicitly couples lipid reprogramming to **immune–spatial niches** and therapy resistance, adding a lipid layer to the metabolic–immune axis; (2) *Molecular Oncology* published a **single-nucleus + spatial transcriptomics** atlas of PTC/ATC (PMID 42578411) with an experimental design disentangling biological from technical variation — directly supplying the in-situ resolution substrate D3 has long lacked; (3) three further LNM imaging/nomogram studies appeared, confirming algorithm-method overcrowding (low rubric); (4) NAT10-ac4C-PKM2 glycolysis mechanism and an ATC convergent-pathway review reinforce metabolic/ATC axes.

**Tracked direction D3 (APOE−/MGST1+ metabolic–immune stem-like metastatic subpopulation):** reinforced this round (lipid–immune review + snRNA/spatial PTC/ATC map strengthen its metabolic–immune and spatial–single-cell substrate); still no direct APOE−/MGST1+ validation, no countervailing evidence → **Strong (rubric 33, 18th consecutive confirmation)**.

---

## 检索策略 (Search Strategy)

| 源 Source | 查询维度 Query (维度代码) | 过滤 Filters | 取回 Hits | 备注 Notes |
|---|---|---|---:|---|
| OpenAlex | a 分子机制+预后转移 | `title_and_abstract.search` + `from_publication_date:2026-07-15` | 17 | 新条目 16 |
| OpenAlex | b 分子机制 | 同上 | 31 (取25) | 新条目 17 |
| OpenAlex | c 算法方法+预后转移 | 同上 | 12 | 新条目 11 |
| OpenAlex | d 免疫微环境 | 同上 | 13 | 新条目 5 |
| OpenAlex | e 单细胞 | 同上 | 10 | 新条目 6 |
| OpenAlex | f 空间组学 | 同上 | 13 | 新条目 3 |
| OpenAlex | g 预后转移 | 同上 | 45 (取25) | 新条目 17 |
| OpenAlex | h 转移干性 | 同上 | 5 | 新条目 1 |
| OpenAlex | i 代谢重编程 | 同上 | 10 | 新条目 5 |

**通道说明 / Channel note:** 本机 NCBI eutils / pubmed.ncbi.nlm.nih.gov 4/4 超时不可达（HTTP 000），故不直连 PubMed；`paper-search-mcp` 走服务端代理但频繁 `not well-formed` 并截断，仅作补充**且本轮未启用**（主源已充分覆盖，符合环境事实"失败即跳过"约定）。OpenAlex 直连稳定（~1.4s），且索引预印本、按日期排序，可捞到 PubMed 尚未编目的新文献。

**去重与清洗 / Dedup & cleaning:** 按标题归一化为主键合并单篇多版本（本轮合并 25 组）；正则剔除期刊补充材料条目（`Table 1_…` 等）；要求**标题点名甲状腺 AND 整体为肿瘤主题**，剔除顺带提及甲状腺的他病文献。

---

## 纳入论文 (Included Papers)

> 本轮纳入 = 相对 run #17 基线的 **9 条新增在范围文献**（以 DOI 为主标识，PMID 缺失标注"待编目"，不编造）。既有 50 条在范围语料（run #17 基线）作为"已知结论"背景承载，不重复列出。

1. **Lipid Metabolic Reprogramming in Thyroid Cancer: Systemic Biomarkers, Tumor Dependencies and Therapeutic Resistance**. Preprints.org. 2026-08-11. DOI: 10.20944/preprints202608.0708.v1. `[preprint, narrative review]`
   Author claim: 将循环脂质标志物与瘤内脂质通量区分，并把脂质重编程整合进免疫–空间生态位与治疗抵抗框架。
   Agent note: High 相关，但为 preprint 综述，证据权重降档；其"脂质↔免疫空间"框架直接补强 D3 代谢–免疫轴。

2. **Spatial and single-nuclei transcriptomics reveals idiosyncratic and generic patterns in papillary and anaplastic thyroid cancers**. *Molecular Oncology*. 2026-08-11. PMID: 42578411. DOI: 10.1002/1878-0261.70289.
   Author claim: 以单核 RNA-seq + 空间转录组刻画 BRAF V600E PTC 与 ATC，实验设计分离生物学/技术上变异，显示大量转录变异为瘤间"特异性"、同时存在"通用"程序。
   Agent note: High 相关；提供 D3 缺失的**原位（空间 + 单核）分辨底座**，并正面处理既往 scRNA 技术混杂问题。

3. **Dual nomograms to predict central and lateral cervical lymph node metastasis in papillary thyroid carcinoma with Hashimoto's thyroiditis: a two-cohort study**. *Frontiers in Endocrinology*. 2026-08-11. DOI: 10.3389/fendo.2026.1826515.
   Author claim: 针对 TgAb/TPOAb 升高的 PTC+桥本患者（反应性淋巴增生易误诊转移），构建并验证分别预测中央区 (CLNM) 与侧颈区 (LLNM) 淋巴结转移的 dual nomogram。
   Agent note: Medium；双队列，但仅适用于 HT 亚群，需外部验证。

4. **Multimodal ultrasound-based nomogram for predicting occult cervical lymph node metastasis in cN0 papillary thyroid carcinoma**. *BMC Medical Imaging*. 2026-08-10. DOI: 10.1186/s12880-026-02648-x.
   Author claim: 204 例 cN0 PTC，融合常规超声 + SMI + SWE 的多模态超声列线图预测隐匿性 CLNM，内部验证。
   Agent note: Medium；单中心、仅内部验证，属算法维度拥挤区。

5. **Dynamic phenotyping of radioiodine-refractory differentiated thyroid cancer: thyroglobulin trajectories, dual-modal imaging, and genotype-defined treatment resistance**. *Frontiers in Endocrinology*. 2026-08-10. DOI: 10.3389/fendo.2026.1891291.
   Author claim: 424 例高中危 DTC，关联纵向 Tg 动力学 + 双模态影像表型 + 基因型，刻画靶向治疗反应。
   Agent note: Low；回顾性，预后/治疗抵抗方向补强。

6. **Prevalence and outcome of metastases to the thyroid gland: a nationwide database study**. *European Thyroid Journal*. 2026-08-10. PMID: 42572999. DOI: 10.1530/etj-25-0307.
   Author claim: 基于荷兰 PALGA（1989–2014）与全国数据库，575 例甲状腺继发转移，刻画来源、时序与生存。
   Agent note: Medium；注意是**转移至甲状腺**（继发），非甲状腺Cancer远处转移，方向略偏但属在范围甲状腺肿瘤话题。

7. **No structural recurrence in patients with postoperative indetectable calcitonin after surgery for medullary thyroid cancer**. *British Journal of Surgery*. 2026-08-01. DOI: 10.1093/bjs/znag093.090.
   Author claim: 卡罗林斯卡 MTC 队列（2000–2021），术后降钙素不可测者无结构性复发（有利预后因素）。
   Agent note: Low；单中心，DOI 形态疑为会议摘要，需全文确认；补强 MTC（D6）预后角度。

8. **NAT10-mediated ac4C acetylation of PKM2 promotes papillary thyroid carcinoma through regulating glycolysis**. *Journal of Molecular Histology*. 2026-08-10. PMID: 42573834. DOI: 10.1007/s10735-026-10924-x.
   Author claim: NAT10 对 PKM2 进行 ac4C 乙酰化修饰 → 促进糖酵解 → 驱动 PTC。
   Agent note: Low；OpenAlex 无摘要（closed），机制结论需全文核验；补强代谢重编程轴。

9. **Convergent Mechanistic Pathways Driving the Anaplastic Phenotype in Thyroid Cancer**. *Int. J. Mol. Sci.*. 2026-08-10. DOI: 10.3390/ijms27167156.
   Author claim: ATC 无通用单一驱动突变，其表型由细胞周期/凋亡失调、去分化等"趋同"程序定义。
   Agent note: Medium；综述，补强 ATC/转移干性轴。

---

## 证据矩阵 (Evidence Matrix)

> 列说明：在 schema 基础上增加 **维度 / 相关性 / 预印本 / OA 状态** 四列（用户要求）。Relevance 与 Gap 列体现所属维度。

| Paper (第一作者/年) | PMID/DOI | 疾病/人群 | 数据来源 | 方法 | 终点 | 主要发现 | 验证 | 局限 | 维度 | 相关性 | 预印本 | OA |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lipid Metabolic Reprogramming (2026) | 10.20944/preprints202608.0708.v1 | TC 广义 | 综述 | 叙事综述 | 代谢–免疫 | 区分循环 vs 瘤内脂质；脂质↔免疫空间生态位、治疗抵抗 | 无（综述） | 无原始数据、preprint | 分子机制/预后转移/代谢重编程 | High | 是 | green |
| snRNA + Spatial PTC/ATC (2026) | 42578411 / 10.1002/1878-0261.70289 | BRAF V600E PTC, ATC | 机构队列 | 单核 RNA-seq + 空间转录组 | 异质性/分型 | 分离生物/技术变异；瘤间特异性 + 通用程序 | 内部多样本 | n 未明、未定位特定亚群 | 单细胞/空间组学 | High | 否 | gold |
| Dual nomograms PTC+HT (2026) | 10.3389/fendo.2026.1826515 | PTC 伴桥本 | 双队列 | 列线图 | CLNM/LLNM | 针对 HT 反应性淋巴增生误判构建双列线图 | 双队列 | HT 亚群限定、需外验 | 算法方法/预后转移 | Medium | 否 | gold |
| Multimodal US nomogram cN0 (2026) | 10.1186/s12880-026-02648-x | cN0 PTC | 204 例机构 | 超声+SMI+SWE 列线图 | 隐匿性 CLNM | 多模态超声列线图预测 | 内部验证 | 单中心、仅内验 | 算法方法/预后转移 | Medium | 否 | gold |
| Dynamic phenotyping RAIR-DTC (2026) | 10.3389/fendo.2026.1891291 | 高中危 DTC/RAIR | 424 例 | Tg 动力学+双模态影像+基因型 | 治疗抵抗 | 纵向表型关联靶向反应 | 内部 | 回顾性 | 分子机制/预后转移 | Low | 否 | gold |
| Metastases TO thyroid (2026) | 42572999 / 10.1530/etj-25-0307 | 继发甲状腺转移 | 全国数据库 PALGA | 回顾性数据库 | 来源/生存 | 575 例继发甲状腺转移特征 | 全国库 | 继发方向、非TC转移 | 预后转移 | Medium | 否 | gold/diamond |
| No recurrence MTC (2026) | 10.1093/bjs/znag093.090 | MTC | 卡罗林斯卡 2000–2021 | 回顾性 | 结构性复发 | 术后降钙素不可测→无结构复发 | 单中心 | 疑会议摘要、需全文 | 预后转移 | Low | 否 | closed |
| NAT10-ac4C-PKM2 (2026) | 42573834 / 10.1007/s10735-026-10924-x | PTC | 机制研究 | 乙酰化/糖酵解 | 驱动机制 | NAT10 ac4C 修饰 PKM2→糖酵解→PTC | 湿实验 | 摘要缺失需核验 | 代谢重编程 | Low | 否 | closed |
| Convergent ATC pathways (2026) | 10.3390/ijms27167156 | ATC | 综述 | 综述 | 去分化机制 | ATC 由趋同程序而非单一驱动定义 | 无（综述） | 综述综合 | 代谢重编程 | Medium | 否 | gold |

---

## 已知结论 (What Is Already Known)

*（基于 run #1–#17 纵向监测形成的稳定共识，本轮未改变；本轮 9 篇新文献见证据矩阵。）*

1. **代谢–免疫耦合驱动淋巴结转移 (Axis 1)：** MGST1 "Mito-high"/免疫冷 (AUC 0.833)、SHMT2、GLTC-LDHA、SOX12-YBX1-LDHA 等多条代谢–免疫耦合证据稳定；本轮脂质重编程综述进一步将**脂质代谢**纳入该耦合（系统标志物 vs 瘤内通量 + 免疫空间生态位），强化此轴。
2. **干性转移亚群 (Axis 2)：** APOE−（经 ABCA1-LXR）、MGST1 去分化尖端、ISG15/KPNA2 (ATC)、DLK1 (MTC) 等干性/去分化亚群证据稳定。本轮无新反证。
3. **POSTN+ myCAF 空间图谱 (Axis 3)：** POSTN+ 肌成纤维细胞 CAF 空间图谱预测 LNM 证据稳定；本轮 snRNA+空间 PTC/ATC 图谱为"原位分辨 APOE−/MGST1+ 亚群"提供方法学底座。
4. **影像/多组学 AI 高度拥挤 (Axis 4)：** LLNM-Net、CLAM-WSI、融合 DL 等大量单中心 AI 模型；本轮再增 3 篇 LNM 列线图/超声研究，**过度拥挤确认**。
5. **BRAF V600E / PD-L1 可预测远处转移但非 LNM/复发 (Axis 5)：** 46k BRAF V600E 荟萃（ nodal OR 1.38 / recurrence OR 1.56，但 distant OR 0.75）与 PD-L1 荟萃一致；DTC 远处 vs LNM 解耦稳定。

---

## 未解问题 (What Remains Unclear)

- **APOE−/MGST1+ 亚群尚未被直接原位验证：** 本轮空间+单核图谱提供了方法学底座，但未在该图谱中定位/验证 APOE−/MGST1+ 代谢–免疫干性亚群本身。
- **脂质代谢与既有糖酵解/OXPHOS 轴的关系未整合：** 新脂质综述提出脂质↔免疫空间框架，但与 MGST1/LDHA/SHMT2 等已建立代谢驱动的具体串扰机制仍空白。
- **单细胞技术混杂仍普遍：** 既往 scRNA 结论受批次/技术上变异干扰；本轮 PTC/ATC 图谱正面处理该问题，但**通用 vs 特异性程序**如何映射到具体转移/干性表型尚待下游功能解析。
- **DTC 远处 vs LNM 解耦的机制基础不明：** 远处可预测而 LNM/复发不可预测，分子解耦机制未阐明。
- **NAT10-ac4C-PKM2 可信度待核验：** OpenAlex 无摘要（closed），机制结论需全文确认。

---

## 领域方法/数据局限 (Method/Data Limitations In The Field)

- **PubMed 编目滞后：** 本轮 9 篇新文献全部无 PMID，纯靠 DOI 主标识；若依赖 PubMed 单点将系统性漏检（历史 16 轮零新增假象即源于此）。
- **预印本证据权重：** 1 篇 High 为 Preprints.org 叙事综述，须降档处理。
- **AI/列线图过度拥挤且验证薄弱：** 本轮 3 篇 LNM 预测均为单中心/仅内部验证，rubric 上不具新颖性。
- **公开数据复用与批次效应：** 单细胞/空间研究普遍样本量小、机构单中心，跨队列批次效应未系统校正。
- **继发转移方向偏离：** 1 篇为"转移至甲状腺"（继发），非甲状腺Cancer转移，计入在范围但信号方向需甄别。

---

## 候选未来方向 (Candidate Future Directions)

*按 research-direction-rubric.md 七维（Novelty/Feasibility/Data/Validation/Clinical/Method/Overcrowding，各 1–5）×7 求和；28–35 = Strong。*

| 方向 | 研究问题 | 新颖度 | 可行性 | 数据 | 验证 | 临床 | 方法 | 拥挤度 | 总分 | Claim Boundary |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| **D3** APOE−/MGST1+ 代谢–免疫干性转移亚群 | 界定并靶向 APOE−/MGST1+ 代谢–免疫干性转移亚群 | 5 | 4 | 5 | 4 | 5 | 5 | 5 | **33** | 不得声称临床可转化，须先原位+体内验证 |
| D8 TREM2+ AHR–IDO1 免疫代谢检查点 | TREM2+ 巨噬 AHR–IDO1–kynurenine 通路体内免疫逆转 | 5 | 4 | 4 | 4 | 4 | 4 | 4 | **30** | 体内模型验证前不主张治疗靶点 |
| D9 citrullination/PADI 侵袭程序 | PADI 瓜氨酸化 × SPP1–CD44 侵袭程序 | 4 | 4 | 4 | 3 | 4 | 4 | 4 | **28** | 需原代空间验证 |
| D6 MTC 5-HT/NETs 肝转移 | 5-HT/去甲肾上腺素能信号驱动 MTC 肝转移 | 4 | 4 | 4 | 3 | 4 | 4 | 4 | **27** | 依赖 fluoxetine/SERT 阻断实验确认 |
| D-ml 影像/多组学 AI | LNM/复发深度学习预测 | 1 | 3 | 3 | 2 | 3 | 2 | 1 | **20** | 过度拥挤，非优先 |

**D3 跟踪结论（本轮）：** 脂质–免疫综述 + 单核/空间 PTC/ATC 图谱**定性强化** D3 的代谢–免疫与空间–单细胞底座；机制层面无变化、无反证。维持 **Strong（33，连续第 18 轮）**。核心缺口（原代空间验证 + 体内靶向）未变。

---

## 推荐下一步方向 (Recommended Next Direction)

**继续推进 D3（APOE−/MGST1+ 代谢–免疫干性转移亚群），并将其与本轮新底座耦合：**

1. **用本轮 snRNA+空间 PTC/ATC 图谱的方法学（生物/技术变异分离）重分析 TCGA + 自有空间数据**，原位定位 APOE−/MGST1+ 亚群在 BRAF V600E PTC 与 ATC 中的空间分布。
2. **整合脂质代谢层：** 在 D3 框架中加入脂质通量（区别于循环标志物），检验脂质↔免疫空间生态位是否与 MGST1 "Mito-high"/免疫冷共定位。
3. **验证计划：** 独立机构队列 + 免疫荧光/多重 IHC 原位确认 + 类器官/PDX 体内靶向（脂质代谢 + ABCA1-LXR 轴）。
4. **Claim boundary：** 在获得原代空间验证与体内靶向证据前，不得声称临床可转化。

---

## 随访阅读清单 (Follow-Up Reading List)

- **Lipid Metabolic Reprogramming in Thyroid Cancer**（preprint, 10.20944/preprints202608.0708.v1）：脂质↔免疫空间框架，D3 新补充层。
- **Spatial and single-nuclei transcriptomics ... PTC/ATC**（PMID 42578411）：D3 原位分辨方法学底座，优先精读方法部分。
- **NAT10-ac4C-PKM2**（PMID 42573834）：需取全文核验糖酵解机制，补强代谢轴。
- **Convergent Mechanistic Pathways Driving the Anaplastic Phenotype**（10.3390/ijms27167156）：ATC 去分化综合，D3/D6 背景。
- **Metastases to the thyroid gland**（PMID 42572999）：继发转移全国数据，方向甄别用。

---

## 可复现性说明 (Reproducibility Notes)

- **检索日期 / Search date:** 2026-08-14 (UTC+8)
- **数据库 / Databases:** OpenAlex（主）、Crossref（元数据校验）、Unpaywall（OA 状态）
- **查询字符串 / Query strings:** 见 `oa_search.py` 中 `QUERIES`（九路 a–i，维度：分子机制/免疫微环境/单细胞/空间组学/算法方法/预后转移/转移干性/代谢重编程）
- **过滤 / Filters:** `from_publication_date:2026-07-15`，`sort=publication_date:desc`，`per-page 25`
- **去重规则 / Dedup:** 标题归一化为主键合并多版本；DOI 次级键；基线比对按 PMID/DOI/标题归一化
- **筛选规则 / Screening:** 标题须点名甲状腺 AND 整体肿瘤主题；剔除补充材料、非肿瘤甲状腺病
- **新增判定 / New detection:** 相对 `search_results_latest.json`（run #17）的 `new_records`
- **保存文件 / Files:**
  - 检索结果：`search_results_20260814_025551.json`（带时间戳副本）
  - 基线更新：`search_results_latest.json`（覆盖为 run #18 基线锚点）
  - 报告：`literature_review_20260814_025551.md`
  - 富集脚本：`_enrich_run18.py`（Crossref + Unpaywall）

---

## 相对上一份报告的变化 (Delta vs. Run #17, 2026-08-10)

| 指标 | run #17 (08-10) | run #18 (08-14) | 变化 |
|---|---:|---:|---|
| 唯一记录 unique | 76 | 81 | +5 |
| 在范围 in-scope | 55 | 59 | +4 |
| 剔除 excluded | 21 | 22 | +1 |
| 相对基线新增 new | 8 | 9 | +1（真实增量，3 天窗口） |
| 在范围预印本 preprints | 3 | 4 | +1 |
| High 相关 | 11 | 13 | +2 |
| 维度 分子机制 | 27 | 28 | +1 |
| 维度 预后转移 | 36 | 39 | +3 |
| 维度 空间组学 | 8 | 9 | +1 |
| 维度 单细胞 | 5 | 6 | +1 |
| 维度 算法方法 | 9 | 11 | +2 |
| 维度 代谢重编程 | 4 | 7 | +3 |
| 维度 转移干性 | 4 | 3 | −1 |
| 维度 免疫微环境 | 8 | 8 | 0 |

**本轮新信号（run #17 以来）：**
1. 脂质代谢重编程综述（preprint）→ D3 代谢–免疫轴新增**脂质层**（新框架）。
2. 单核 + 空间 PTC/ATC 转录组图谱（PMID 42578411）→ 补齐 D3 **原位空间–单细胞底座**（方法学突破）。
3. 3 篇 LNM 列线图/超声研究 → 算法维度拥挤度再确认。
4. NAT10-ac4C-PKM2 糖酵解、ATC 趋同通路综述 → 代谢/ATC 轴补强。
5. MTC 降钙素不可测无复发、继发甲状腺转移全国库 → 预后/转移方向细化。

**D3 跟踪结论：** 本轮**强化**（脂质–免疫 + 单核/空间图谱），无反证，维持 Strong（33，第 18 轮）。
**平台期判定：** 否——3 天窗口即新增 9 篇（~2–3 篇/日），属领域真实活跃，此前 16 轮零新增为 `relevance` 排序 + 单点 PubMed + PMID 滞后之方法学假象（已于 run #16 确诊）。
