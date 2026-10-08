# Literature Review: 甲状腺癌侵袭、淋巴结与远处转移、复发、预后及其分子机制、肿瘤免疫微环境、单细胞与空间组学、机器学习/深度学习方法
# Thyroid Cancer (PTC/PTMC/FTC/MTC/ATC): Invasion, Nodal & Distant Metastasis, Recurrence, Prognosis, Molecular Mechanisms, Tumor Immune Microenvironment, Single-Cell & Spatial Omics, and ML/DL Methods

- **Date / 检索日期**: 2026-10-09
- **Run**: #28（连续监测第 28 轮）
- **Sources / 数据源**: OpenAlex（主通道）、Europe PMC（第二通道，12 路）、定向基因深挖（第三通道，34 基因面板）、Crossref（DOI 校验）、Unpaywall（OA 解析）
- **Search window / 检索窗口**: 主窗口 30 d = 2026-09-09 → 2026-10-09；补跑 90 d = 2026-07-11 → 2026-10-09；Europe PMC `PUB_YEAR:2026`；深挖 `from_publication_date:2026-06-01`
- **Baseline / 基线**: 457 条 → 本轮新增 70 条 → **527 条**

---

## 中文摘要

本轮（Run #28）三通道并行检索，累计命中 1,000+ 条，取回候选 383 条，**去重后唯一新增 70 条**（OpenAlex 15 / Europe PMC 50 / 定向深挖 5），其中 High 17、Medium 34、Low 19；严格预印本 2 条，PMID 待编目 15 条。

**本轮最强信号有三条：**

1. ⭐⭐⭐ **首次出现「碘代谢 → CD36⁺ 促炎巨噬细胞 → SPP1 → ZCCHC12⁺ 肿瘤细胞（PI3K-AKT）」的完整跨细胞轴**（*Cancer Immunology Research*, PMID 39178310）。这是 28 轮监测中第一篇把**碘（甲状腺癌最核心的环境/治疗因子）与 TAM 极化直接连通**的原发证据，且给出了"补碘可抑制 CD36⁺ 巨噬细胞发育"的可干预节点。SPP1 首次在 PTC 中被定位为**髓系来源的配体**而非仅肿瘤细胞标志物。
2. ⭐⭐ **「代谢重编程 → 铁死亡抵抗 → 免疫逃逸」三元耦合成为本轮最密集的机制簇**：ETV4→STAT6→SLC7A11/PD-L1（PMID 41759995，同一转录因子同时驱动铁死亡抵抗与免疫逃逸）、SPARCL1→SLC3A2 铁死亡（PMID 42160309）、IGF2BP2→m⁶A-PHGDH 丝氨酸代谢（PMID 42174614）、ATC 代谢-免疫抑制综述（PMID 41716397）。代谢维度（ME 20 条）与免疫维度（IM 10 条）合计占本轮 43%。
3. ⭐⭐ **算法维度出现明确的范式转移：从"造模型"转向"嵌流程、评人、评公平性"**：Human vs AI 的 RAI 决策头对头比较（PMID 42791092，100 例 × 4 个 LLM 平台 vs 医师 vs 共识估计）、LLM 增强的 SPECT 影像组学多模态融合（PMID 42420643，311 例）、Agentic no-code AI 自主建模（PMID 42808848）、AI 代表性路线图（PMID 41041822）。算法维度（AL 19 条）首次接近预后维度（PR 31 条）的一半。

**持续跟踪方向 D3″（APOE×MGST1 代谢–免疫干性亚群）本轮执行预注册的 M5 终判：阴性，正式归档。** 量化事实：OpenAlex 全库 `MGST1 × thyroid` = 1 篇（2026-06-04，PMID 42327722，连续第 3 轮零增长）；`APOE × MGST1 × thyroid` 三词共现 = **0**；Europe PMC 全时间 `MGST1` × `thyroid` = 1 篇。反观同年 APOE = 7 篇、APOC1 = 5 篇、CD36 = 2 篇。**结论：把 MGST1 当作该轴锚点本身是错误的先验**，残余价值（APOE 区室归属问题）整体并入 **D21 脂代谢–载脂蛋白轴**。

**推荐下一步**：D21″（rubric 29）——脂代谢重编程 × 免疫生态位 × 获得性耐药的跨区室整合，零湿实验起步；并行 D13-M（rubric 28）多模态 radiopathomics 作为可立即执行的第二赛道。

---

## English Abstract

Run #28 executed a three-channel surveillance (OpenAlex / Europe PMC 12 routes / targeted 34-gene deep dig). After deduplication, **70 unique new records** were added (OpenAlex 15, Europe PMC 50, deep dig 5): High 17, Medium 34, Low 19; 2 strict preprints; 15 records without PMID (PubMed indexing lag — DOI used as primary identifier, never fabricated).

**Three dominant signals:**

1. ⭐⭐⭐ **A complete iodine → CD36⁺ proinflammatory macrophage → SPP1 → ZCCHC12⁺ tumor cell (PI3K-AKT) axis** (*Cancer Immunol Res*, PMID 39178310). First primary evidence in 28 rounds directly linking **iodine — the single most thyroid-specific environmental/therapeutic variable — to TAM polarization**, with an actionable node (iodine supplementation impedes CD36⁺ macrophage development). SPP1 is repositioned as a **myeloid-derived ligand** rather than a tumor-intrinsic marker.
2. ⭐⭐ **Metabolic reprogramming → ferroptosis resistance → immune escape emerges as the densest mechanistic cluster**: ETV4→STAT6→SLC7A11/PD-L1 (PMID 41759995; one TF driving both ferroptosis resistance and immune evasion), SPARCL1→SLC3A2 (PMID 42160309), IGF2BP2→m⁶A-PHGDH serine metabolism (PMID 42174614), ATC metabolic-immunosuppressive TIME review (PMID 41716397). ME (20) + IM (10) = 43% of this round.
3. ⭐⭐ **The algorithm dimension shows a clear paradigm shift from "build a model" to "embed in workflow, benchmark against humans, audit fairness"**: human-vs-AI head-to-head on postoperative RAI decisions (PMID 42791092; 100 patients × 4 LLM platforms vs physician vs consensus estimate), LLM-enhanced SPECT radiomics multimodal fusion (PMID 42420643; n=311), agentic no-code model building (PMID 42808848), and a representativeness roadmap (PMID 41041822).

**Tracked direction D3″ (APOE × MGST1 metabolic–immune stemness axis): pre-registered terminal judgment executed — NEGATIVE, archived.** OpenAlex full-library `MGST1 × thyroid` = 1 paper (zero growth for 3 consecutive checks); `APOE × MGST1 × thyroid` co-occurrence = **0**; Europe PMC all-time = 1. By contrast, 2026 alone yields APOE = 7, APOC1 = 5, CD36 = 2. **Using MGST1 as the anchor of this axis was a false prior.** Residual value (the APOE compartment question) is folded into **D21 (lipid metabolism / apolipoprotein axis)**.

**Recommended next step**: D21″ (rubric 29) — cross-compartment integration of lipid metabolic reprogramming × immune niche × acquired resistance, starting with zero wet-lab work; in parallel D13-M (rubric 28) multimodal radiopathomics as an immediately executable second track.

---

## 一、检索策略 (Search Strategy)

| Source / 通道 | Query / 查询 | Filters / 过滤 | Results / 命中 | Notes / 说明 |
|---|---|---|---:|---|
| OpenAlex 九路（30 d） | `a` 分子机制+预后转移 / `b` 分子机制 / `c` 算法 / `d` 免疫微环境 / `e` 单细胞 / `f` 空间 / `g` 预后转移 / `h` 转移干性 / `i` 代谢重编程 | `from_publication_date:2026-09-09`，`sort=publication_date:desc`，`per-page=25` | 唯一 89 / 在范围 66 / 剔除 23 / 合并多版本 23 / **新增 15** | 主窗口；`oa_search.py` 内建三类清洗 |
| OpenAlex 九路（90 d） | 同上 | `from_publication_date:2026-07-11`，`per-page=50` | 唯一 222 / 在范围 161 / 剔除 61 / 合并多版本 48 / **新增 14** | 与 30 d 并集后 OpenAlex 净贡献 **15** |
| Europe PMC（12 路） | `SC`/`SP`/`IM`/`ME`/`AL`/`ST`/`MO`/`PR`/`MACRO2`/`SPATIAL_DS` + 本轮新增 `LIPID`/`AI` | `TITLE:"thyroid"`，`PUB_YEAR:2026`，`sort=P_PDATE_D desc`，`pageSize=50` | 候选 **162** → 人工纳入 **50** | ME 路按 Run #27 建议加 `TITLE:"carcinoma"/"cancer"` 约束，污染明显下降 |
| 定向基因深挖（OpenAlex） | 34 基因 × `title_and_abstract.search:thyroid` | `from_publication_date:2026-06-01`，`per-page=25` | 34 路 → 净新增 **5** | 面板 27→34（新增 APOA1/LPL/VLDLR/ACSL4/GPX4/SLC7A11/FN1） |
| Crossref / Unpaywall | 30 条 High/Medium DOI | — | 见 §10 | 元数据校验 + OA 全文解析 |
| NCBI eutils / PubMed / GEO / FTP | — | — | **未使用** | 本机 HTTP 000 不可达（实测 4/4），禁止直连重试 |
| paper-search-mcp | — | — | **未连接** | 本会话仅 agent-mail 可用 |

**剔除规则 / Exclusion rules**
1. 期刊补充材料被索引为独立条目（`Table 1_…` / `Data Sheet 1_…` / `Additional file …` / `Supplementary …`）→ 丢弃。
2. 撤稿/更正/视觉摘要（`Retraction notice to` / `Correction:` / `Erratum:` / `ASO Visual Abstract:`）→ 丢弃或降档。
3. 同一论文多版本 → 以标题归一化为主键合并，补齐 PMID/DOI。
4. 标题未点名甲状腺 **或** 整体非肿瘤主题 → 剔除。
5. 预印本保留但标注 `[preprint]` 并在证据强度上降档。

**EPMC 162 条候选的剔除构成**（规则化归因，人工复核）：非肿瘤甲状腺激素代谢/甲状腺–肝轴/肥胖/代谢综合征/妊娠/卒中/认知 28；甲状腺良性结节/消融/影像诊断（非癌机制）23；甲状腺眼病/Graves/自身免疫/irAE 18；撤稿/更正/补充材料 15；其他/重复/低相关 14；非人/兽医 6；文献计量/来信/评论 3；空间生态学/发病率地理分布 2；其他癌种 1；正常甲状腺/发育 1。

---

## 二、纳入论文 (Included Papers)

**计数汇总 / Counts**

| 指标 | 数值 |
|---|---:|
| 三通道累计命中（去重前） | ~1,000+ |
| 取回候选 | 383 |
| **去重后唯一新增** | **70** |
| — OpenAlex | 15 |
| — Europe PMC | 50 |
| — 定向基因深挖 | 5 |
| 相关性 High / Medium / Low | 17 / 34 / 19 |
| **严格预印本** | **2** |
| PMID 待编目（DOI 为主标识） | 15 |
| 维度分布 | PR 31 / AL 19 / ME 20 / MO 18 / IM 10 / SC 2 / SP 1 |
| OA 分布 | gold 28 / closed 32 / diamond 6 / hybrid 2 / green 2 |
| 发表月份 | 2026-10: 17；2026-09: 11；2026-08: 3；2026-07: 2；2026-06: 6；2026-05: 8；2026-04: 10；2026-03: 5；2026-02: 2；2026-01: 3；2025-12/10: 2；2024-11: 1 |

> **重要读数**：OpenAlex 贡献的 15 条**全部**落在 2026-09/10（真正的窗口内新发）；Europe PMC + 深挖贡献的 55 条中，仅 13 条为 2026-09/10，**42 条为 2024-11 ~ 2026-08 的历史欠采样回填**。

### 2.1 High 相关性（17 条，逐条要点）

1. **CD36⁺ Proinflammatory Macrophages Interact with ZCCHC12⁺ Tumor Cells in Papillary Thyroid Cancer Promoting Tumor Progression and Recurrence.** *Cancer Immunol Res* 2024-11-01. PMID **39178310**. DOI **10.1158/2326-6066.cir-23-1047**. [IM+SC] closed.
   - Author claim / 作者主张：多组学鉴定 PTC TME 中 CD36⁺ 促炎巨噬细胞亚群；其向癌前区域募集与不良预后相关，是复发风险因子；通过分泌 **SPP1** 激活 PI3K-AKT 促进 ZCCHC12⁺ 代谢活跃肿瘤细胞增殖；**碘代谢失调与巨噬细胞促炎表型获得密切相关，补碘可抑制促炎信号并阻碍 CD36⁺ 巨噬细胞发育**。
   - Agent note / 研判：本轮最强原发证据。至此 SPP1 在甲状腺癌中的来源首次被定位为**髓系 compartment**（此前 Run #22/#25/#26 的 SPP1 证据均未明确来源细胞），且引入碘这一甲状腺特异变量。⚠️ 为 2024 年论文，因补充材料条目被本轮深挖通道捞出——说明既往 27 轮存在该文的系统性漏检。
2. **TCF4-driven cathepsin S promotes papillary thyroid carcinoma via PI3K/AKT/mTOR.** *Endocr Relat Cancer* 2026-10-05. PMID **42831790**. DOI **10.1530/erc-25-0517**. [MO+PR] closed.
   - 作者主张：整合 GEO + TCGA-THCA + **eQTL 遗传工具**筛选，CTSS 为 PTC 驱动基因，TCF4 转录激活；gain/loss-of-function + 裸鼠成瘤验证；关联 LNM、RAI 抵抗与复发。
   - 研判：本轮唯一带**遗传工具变量（eQTL）**的分子机制论文，因果层次高于常规差异表达+细胞实验；但 OA closed，需机构通路。
3. **ETV4 transcriptionally activates STAT6 to inhibit ferroptosis and promote immune escape in thyroid cancer.** *Endocr Res* 2026-02-27. PMID **41759995**. DOI **10.1080/07435800.2026.2629919**. [ME+IM] closed.
   - 作者主张：ETV4→STAT6→SLC7A11/PD-L1；细胞活力、ROS、凋亡、MDA/GSH/Fe²⁺ 全套铁死亡表型 + 免疫逃逸标志。
   - 研判：**同一转录因子同时解释铁死亡抵抗与 PD-L1 介导免疫逃逸**，是 D12′（铁死亡–免疫逃逸耦合）最直接的双表型节点。ETV4 亦曾在 Run #21 的乳酸化–EMT 轴出现 → 该 TF 是多轴枢纽。
4. **IGF2BP2-driven serine metabolism promotes the progression of thyroid carcinoma via m⁶A-PHGDH.** *J Transl Med* 2026-05-22. PMID **42174614**. DOI **10.1186/s12967-026-08316-6**. [ME+MO] gold.
   - 作者主张：IGF2BP2 经 m⁶A 稳定 PHGDH 驱动丝氨酸代谢；LC-MS 代谢组 + RIP/m⁶A-RIP + RNA 稳定性；体内外功能验证。
   - 研判：PHGDH 第二次在甲状腺癌出现（Run #25 为 PHGDH–dabrafenib 耐药），本次补上 m⁶A 上游；**代谢–表观–耐药三元链条闭合度提升**。
5. **Lipid Metabolism-Related Genes Define Prognosis and Therapeutic Targets in Thyroid Cancer.** *Int J Genomics* 2026-05-17. PMID **42157886**. DOI **10.1155/ijog/9661210**. [ME+PR] gold.
   - 作者主张：**孟德尔随机化 + 转录组 + 单细胞**三层，鉴定脂代谢相关因子；9 基因签名分层预后；高危组脂通路激活、免疫格局不同、**BRAF 突变率更高**；ACBD7 敲减降低增殖/侵袭/迁移。
   - 研判：D21 的核心支柱。MR 提供因果层、scRNA 提供区室层、ACBD7 提供功能层——**三层齐备但分属不同子分析，未在同一批样本上贯通**。
6. **Alterations in gut microbiota and metabolic profiling are associated with papillary thyroid cancer and BRAF V600E mutation.** *Endocrine* 2026-04-27. PMID **42043696**. DOI **10.1007/s12020-026-04607-6**. [ME+IM] closed.
   - 作者主张：70 PTC vs 70 健康对照，16S rRNA + LC-MS/MS 粪便代谢组；PTC 组多样性/丰富度更高；19 个差异菌属（Collinsella/Carnobacterium/Moryella 富集；Lacticaseibacillus/Faecalibaculum 等耗竭）；随机森林 10 折交叉验证。
   - 研判：D17 新增**配对菌群+代谢组**数据层。⚠️ 与 Run #26 的 *Terrisporobacter*→NTRK1（促瘤）和 Run #27 的 *Ruminococcaceae*→RBM15（抑瘤/焦亡）方向再次不一致 → **菌株特异性结论进一步坐实，"肠道菌群与甲状腺癌"作为整体命题无意义**。
7. **Metabolic reprogramming orchestrates an immunosuppressive microenvironment in anaplastic thyroid cancer: mechanisms and clinical perspectives.** *Front Immunol* 2026-02-04. PMID **41716397**. DOI **10.3389/fimmu.2026.1699202**. [ME+IM] gold.
   - 作者主张：系统梳理 ATC 中糖酵解/脂代谢/氨基酸利用如何经营养竞争、免疫抑制代谢物累积、代谢调控免疫检查点表达三条路径塑造免疫抑制 TIME。
   - 研判：综述（不作一级原发证据），但为 D21/D12′ 提供 ATC 端的理论框架；且为 OA gold，可直接取全文。
8. **The secreted protein SPARCL1 suppresses tumor progression in papillary thyroid carcinoma via SLC3A2-mediated ferroptosis.** *Endocr Relat Cancer* 2026-06-08. PMID **42160309**. DOI **10.1530/erc-26-0018**. [ME] gold.
   - 作者主张：SPARCL1 过表达 + 上清蛋白回加 + 重组蛋白三路；皮下成瘤与多器官转移模型；经 SLC3A2 介导铁死亡抑制 PTC 侵袭转移。
   - 研判：**分泌蛋白 + 铁死亡 + 转移**三者合一，是可转化性最好的一条（重组蛋白即潜在治疗分子）。⚠️ SPARCL1 与 SPARC 家族在 Run #25 的 LGALS1/SPARC 链条同源，注意勿混淆。
9. **Deciphering functional intra-tumoral heterogeneity in BRAF V600E-driven mouse thyroid cancer reveals EMT trajectory and metabolic remodeling.** *Br J Cancer* 2026-04-04. PMID **41935217**. DOI **10.1038/s41388-026-03742-8**. [MO+SC] closed.
   - 作者主张：成年自发 BRAF^V600E 小鼠 PTC 模型 scRNA-seq；恶性甲状腺滤泡细胞存在不同间充质转化程度的亚群；EMT 轨迹从中级向更间充质/恶性状态推进；**类器官培养验证各亚群 EMT 表型**；各亚群以亚群特异通路维持 EMT 状态。
   - 研判：本轮唯一带**类器官功能验证**的单细胞轨迹研究。为 D11（EMT）与 D15（去分化）提供小鼠端因果框架；⚠️ 小鼠模型，向人 PTC 外推需谨慎。
10. **The role of microbiota on thyroid cancer: from carcinogenicity, treatment and predictability.** *Front Immunol* 2026-10-05. PMID 待编目. DOI **10.3389/fimmu.2026.1912576**. [MO+IM] gold.
    - 作者主张：肠道菌群及其代谢物经肠–甲状腺轴调控免疫与甲状腺功能；**瘤内微生物群（ITM）**直接参与 TC 发生进展侵袭；菌群调节剂（益生菌/抗生素/FMT）影响化疗、放疗、免疫治疗。
    - 研判：本轮 D17 的最新综述，明确把 ITM 与 GM 并列；OA gold 可取全文。
11. **Level of interleukine-10 and -22 in the blood and tissues of patients with medullary and papillary thyroid carcinomas.** *Int J Endocrinol (Ukr)* 2026-10-02. PMID 待编目. DOI **10.22141/2224-0721.22.6.2026.1753**. [MO+PR+IM] diamond.
    - 作者主张：MTC 与 PTC 组织、癌旁、转移灶及血浆配对检测 IL-10/IL-22；对比转移与非转移患者。
    - 研判：**少见的 MTC + PTC 同批对照**；配对组织–血浆设计对"液体活检替代"问题有直接价值。⚠️ 单中心、样本量未在摘要中给出，属 Low-to-Medium 证据强度（脚本判 High 因命中三维度）。
12. **TURNING THE TIDE: BRAF-TARGETED THERAPY ENABLING SURGICAL DOWNSTAGING IN STAGE IVC ANAPLASTIC THYROID CANCER.** *Thyroid Res Pract* 2026-10-01. PMID 待编目. DOI **10.4103/trp.trp_50_26**. [MO+PR+IM] diamond.
    - 作者主张：68 岁女性 IVC 期 ATC，NGS 示 **BRAF V600E + TERT 启动子 + TP53「三打击」**（由 PTC 去分化而来）；dabrafenib-trametinib 降期后实现根治性手术。
    - 研判：个案（证据强度低），但"三打击"基因型 + 靶向降期 + 手术的路径对 D15/D18 有示范意义。
13. **Navigating multimodal machine learning in papillary thyroid carcinoma: perspectives on pathomics and radiomics integration in thyroidology.** *Clinics* 2026-10-01. PMID **42822363**. DOI **10.1016/j.clinsp.2026.101120**. [AL] closed.
    - 作者主张：PTC 中病理组学（pathomics）与影像组学（radiomics）多模态融合的视角与路线。
    - 研判：D13-M 的方法学纲领；⚠️ 摘要在 EPMC 为空，需取全文确认具体推荐方案。
14. **Human versus artificial intelligence decision-making for radioactive iodine use in differentiated thyroid cancer — A proof of concept.** *Surgery* 2026-09-02. PMID **42791092**. DOI **10.1016/j.surg.2026.110590**. [AL+PR] closed.
    - 作者主张：100 例 DTC 全甲状腺切除患者；按 ATA 风险分层建立"共识知情估计"基准；**4 个 AI 平台给出 RAI 推荐**，与医师处方、共识估计三方比较。
    - 研判：**本轮范式转移的标志性论文**——评测对象从"模型的 AUC"变为"AI 与人的决策一致性与合理性"。样本量小、单中心、无患者结局随访。
15. **LLM-Enhanced Multimodal Fusion of SPECT Radiomics and Clinical Data for Predicting ¹³¹I Therapeutic Response in Differentiated Thyroid Cancer.** *Mol Imaging Biol* 2026-07-08. PMID **42420643**. DOI **10.1007/s11307-026-02114-8**. [AL] closed.
    - 作者主张：311 例；1,688 个 SPECT 影像组学特征；30 个交叉组合模型；早融合/晚融合；**再用 LoRA 微调 LLM 优化融合表征**。
    - 研判：Run #26 曾记录"ML 生存 × LLM 融合"新切口，本条是该切口在**治疗反应预测**上的落地；⚠️ 无外部验证队列。
16. **A multimodal study on predicting extrathyroidal extension of papillary thyroid carcinoma based on radiopathomics.** *BMC Endocr Disord* 2026-05-08. PMID **42104301**. DOI **10.1186/s12902-026-02308-9**. [AL+PR] gold.
    - 作者主张：388 例 PTC（术前超声 + 400× 细胞学图像，5 中心）；Radiomics/Pathomics/融合三模型（XGBoost + LASSO）；融合模型 AUC 0.887/0.857（外部），SHAP 可解释；与放射科医师对比。
    - 研判：**本轮可执行性最高的算法论文**——多中心、外部验证、金标准（ETE 为病理终点）、OA gold。**影像 + 细胞病理双模态**正是 D13-M 的模板。
17. **Integrated Proteomics and Transcriptomics Identify a FN1-ANXA1-PTK2B Network Driving Lymph Node Metastasis.** *Research Square* 2026-06-16. DOI **10.21203/rs.3.rs-9688961/v1**. [MO+PR] **[preprint]** green.
    - 作者主张：蛋白质组 + 转录组整合鉴定 FN1–ANXA1–PTK2B 网络驱动 LNM。
    - 研判：**预印本，降档**。若成立，可与本轮 FN1/MET/KRT19/CLDN1（PMID 42798839）、ITGA7–FN1（PMID 42319496）构成 FN1 三证据簇；⚠️ 三者均为 bulk 相关分析，无空间/单细胞区室归属。

### 2.2 Medium 相关性（34 条，压缩列出）

| # | 论文要点 | PMID/DOI | 维度 | 日期 | OA |
|---|---|---|---|---|---|
| M1 | 儿童 PTC：患病率/形态/分子细胞遗传/预后决定因素（RET/PTC、NTRK、ALK 融合为主，BRAF V600E 次要） | 42829473 / 10.1515/jpem-2026-0277 | MO+PR | 2026-10-04 | closed |
| M2 | IκBβ（NF-κB 抑制亚基）在 PTC、腺瘤、结节性甲状腺肿、转移灶及血浆中的表达比较 | 待编目 / 10.22141/2224-0721.22.6.2026.1754 | MO+PR+IM | 2026-10-02 | diamond |
| M3 | 超声影像组学 + 临床 Nomogram 预测 PTC 颈部 LNM（LASSO + 5 分类器比较） | 待编目 / 10.3389/fonc.2026.1811434 | AL+PR | 2026-10-07 | gold |
| M4 | 高容量颈部 LNM 可解释预测模型：Deyang 521 例建模 + Liaocheng 193 例**地理外部验证** | 待编目 / 10.3389/fonc.2026.1963925 | AL+PR | 2026-10-06 | gold |
| M5 | **Spatial Transcriptomics in Thyroid Cancer: PRISMA 系统综述**（平台/架构/临床应用） | 待编目 / 10.3390/jcm15197636 | SP | 2026-10-02 | gold |
| M6 | 晚期 PTC 复发模式与生存（ESES 新定义，33 例，EUROCRINE® 登记） | 待编目 / 10.1007/s13304-026-02875-5 | PR | 2026-10-06 | hybrid |
| M7 | 年轻成人甲状腺癌 TERT 启动子突变的临床与预后意义（文献综述） | 待编目 / 10.52532/3135-3940-2026-3-792 | PR | 2026-10-06 | hybrid |
| M8 | DNA-PKcs 抑制剂 KU-57788 直接结合并激活 DRP1 → 线粒体过度分裂 + NRF2/SLC7A11/GSH 保护性激活 → 与铁死亡诱导协同（ATC） | 42049705 / 10.1038/s41419-026-08595-3 | ME | 2026-04-28 | gold |
| M9 | TIMP1 与 DPP4 经乳酸代谢促进 PTC 进展（12 候选基因筛选 + siRNA） | 42073588 / 10.3390/cancers18081264 | ME | 2026-04-16 | gold |
| M10 | METTL7B 经 USP28/HIF-1α 轴促进 PTC 糖酵解与恶性进展（GEO+TCGA+组织芯片） | 42332350 / 10.3724/zdxbyxb-2025-0822 | ME+MO | 2026-06-01 | gold |
| M11 | TMED2 经 mTORC1 介导脂肪酸代谢促进甲状腺癌发生（scRNA + TCGA + BODIPY + 裸鼠） | 41581626 / 10.1016/j.bbagen.2026.130910 | ME | 2026-01-23 | closed |
| M12 | SENP1 经 HIF-1α 降低分化型甲状腺癌细胞铁死亡 | 42198970 / 10.12122/…2026.05.13 | ME | 2026-05-01 | closed |
| M13 | KRT15–KRT81 复合物上调 DGKB 介导脂代谢 → 甲状腺癌仑伐替尼耐药（体内外 + shRNA/药理抑制） | 41991644 / 10.1038/s41598-026-47994-6 | ME+PR | 2026-04-16 | gold |
| M14 | 酮体代谢在 ATC 中的初步研究（乙酰乙酸抑制增殖；生酮饮食异种移植） | 41973605 / 10.1530/etj-25-0305 | ME | 2026-04-24 | gold |
| M15 | ATP2C2–PLA2R1 轴经 VGIC 特征调控 PTC 脂代谢与侵袭（GEO+TCGA，LASSO-Cox 6 基因） | 41845134 / 10.1007/s12672-026-04861-0 | ME+MO | 2026-03-17 | gold |
| M16 | 外泌体 miR-145-5p 靶向 TPM3 失活 PI3K-Akt 抑制 PTC | 42828149 / 10.3892/ol.2026.15870 | MO | 2026-09-17 | gold |
| M17 | 整合生信 + 分子对接鉴定 PTC 关键基因与候选药物（GSE58545/3467/29265/60542，1615 种 FDA 药物） | 42749459 / 10.1016/j.jgeb.2026.100791 | MO+AL | 2026-08-08 | gold |
| M18 | 贝母素乙（verticinone）经 AKT 通路抑制 PTC 生长并诱导焦亡 | 41330019 / 10.1016/j.molimm.2025.11.014 | MO | 2025-12-02 | closed |
| M19 | MCP-1（CCL2）在 MTC 与 PTC 中的水平 | 待编目 / 10.21856/j-pep.2026.2.01 | IM | 2026-06-15 | diamond |
| M20 | FTC-Net：视觉-语言基础模型术前鉴别滤泡性肿瘤（14 机构 2421 例/6477 图；外部 AUC 0.836/0.841） | 41991963 / 10.1038/s41698-026-01430-0 | AL | 2026-04-16 | gold |
| M21 | VL-ThyNet：DINOv2 + ResNet 适配器 + VLM 结构化描述，C-TIRADS 4 结节恶性风险（准确率 84.8%） | 42691717 / 10.1016/j.talanta.2026.130540 | AL | 2026-08-31 | closed |
| M22 | MDT-TC：AI 多模态多任务超声特征分析预测甲状腺癌（6884 例训练 + 3 个独立外部队列） | 41967078 / 10.1093/jncics/pkag037 | AL | 2026-07-01 | gold |
| M23 | **LymphUs**：PTC 颈部淋巴结超声多中心开放数据库（338 例，分割掩码 + 16 项语义特征 + FNA 金标准） | 41940127 / 10.1016/j.dib.2026.112694 | AL+PR | 2026-03-17 | gold |
| M24 | Agentic no-code AI 自主开发甲状腺结节恶性分类器（Hugging Face ML-Intern；TN5000 训练 + 232 结节外部验证） | 42808848 / 10.1210/clinem/dgag351 | AL | 2026-09-29 | closed |
| M25 | **Roadmap for Representative AI Models for Thyroid Cancer**（代表性数据/情境变量/训练验证设计/部署后监测四阶段） | 41041822 / 10.1002/lary.70169 | AL | 2025-10-03 | gold |
| M26 | 集成机器学习 + 血清蛋白质组学（MALDI-TOF，414 例 vs 430 对照；SHAP/LIME）早期检测 | 41959894 / 10.3389/fonc.2026.1807894 | AL+PR | 2026-03-25 | gold |
| M27 | 嗜酸细胞性甲状腺癌（OCA）日本 137 例：10/15 年无远处复发生存 100%/92.7%，无癌死亡 | 42830500 / 10.1507/endocrj.ej26-0328 | PR | 2026-10-03 | closed |
| M28 | 热消融治疗 PTC 颈部 LNM 的安全性与有效性系统综述（29 项研究，LA/RFA/MWA） | 42783457 / 10.3390/medsci14050584 | PR | 2026-09-18 | gold |
| M29 | 超声引导热消融治疗 PTC 术后局部复发性颈部 LNM：多中心 101 例/128 枚淋巴结 | 42754433 / 10.1016/j.acra.2026.08.064 | PR | 2026-09-17 | closed |
| M30 | 热消融 vs 颈清扫治疗复发性低负荷 LNM：双中心 230 例（36 个月复发率无差异） | 41883104 / 10.1080/02656736.2025.2602514 | PR | 2026-03-26 | closed |
| M31 | 预测 cN0 PTC 右喉返神经后方 LNM：721 例风险模型（气管旁 + 喉前淋巴结） | 42643058 / 10.1177/14574969261440429 | PR+AL | 2026-04-22 | closed |
| M32 | 血小板/HDL-C 比值（PHR）经倾向评分匹配预测 PTC LNM（784 例） | 42184935 / 10.1016/j.jormas.2026.102854 | PR | 2026-05-25 | closed |
| M33 | FN1/MET/KRT19/CLDN1 为 PTC 关键失调基因（6 套 RNA-seq 数据集，131 个共同 DEG） | 42798839 / 10.3892/ol.2026.15854 | MO | 2026-09-11 | closed |
| M34 | ITGA7 与 FN1 互作抑制 PI3K/AKT 抑制甲状腺癌进展 | 42319496 / 10.1007/s00432-026-06531-8 | MO | 2026-06-19 | gold |

### 2.3 Low 相关性（19 条，仅列题录）

PD-1/PD-L1 经 TGF-β/Smad 影响甲状腺癌细胞恶性行为（10.3892/etm.2026.13317）· 家族性 DTC 的 RAI 疗效 **[preprint]**（10.21203/rs.3.rs-10716459/v1）· 晚期甲状腺恶性肿瘤上气道切除与重建（10.22141/…1765）· LINC01614 经 miR-4521/IGF2/PI3K-AKT 促进 PTC 铁死亡抵抗（10.3390/genes17101232）· 葡萄糖代谢重编程综述（10.1007/s11596-026-00206-8）· ATC Warburg 效应综述（10.3390/ijms27125472）· 免疫治疗与铁死亡调控综述（10.1016/j.critrevonc.2026.105292）· 铁死亡机制综述（10.1007/s10495-026-02322-1）· 代谢综合征与甲状腺癌发病风险 meta（10.17305/bb.2026.13977）· miR-451 经 PI3K 调控 TPC-1（10.1530/ec-25-0802）· The prediction paradox: AI、遗传学与隐匿转移（10.1210/clinem/dgag065，社论）· AI 辅助数字甲状腺 FNA 细胞学（10.1002/cncy.70149）· LOCUS-Diff 超声合成（10.1007/s10278-026-02246-x）· AI 在甲状腺癌诊断中的应用 2026 更新（10.1177/10507256251412316）· CT vs CT+US 诊断 LNM（10.1016/j.jtumed.2026.08.004）· US 与 SPECT/CT 比较的方法学问题（10.1002/jum.70246）· Bethesda III 核异型的预后意义（10.1111/cyt.70084）· PTC 额叶转移病例（10.2174/0115734056513901260818073555）· MTC 颅内转移拟似脑膜瘤（10.47391/jpma-7anos-abs-38）

---

## 三、证据矩阵 (Evidence Matrix)

### 3.1 High 相关性完整矩阵

| Paper | PMID/DOI | 维度 | Disease/Population | Data Source | Method | Endpoint | Main Finding | Validation | Limitations | Rel | Gap Suggested | Future Direction |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| CD36⁺ Mac × ZCCHC12⁺ | **39178310** / 10.1158/2326-6066.cir-23-1047 | IM+SC | PTC，含癌前区域与复发队列 | 多组学（自采 + 公共） | 多组学 + 配体-受体互作 + 功能实验 | 复发、增殖 | CD36⁺ 促炎 Mac 分泌 **SPP1** → PI3K-AKT → ZCCHC12⁺ 肿瘤细胞；**碘代谢失调驱动促炎表型，补碘可阻断** | 临床复发关联 + 体外/体内 | 未做空间共定位定量；碘干预仅临床前 | High | SPP1 的**区室归属**（髓系 vs 上皮）未在同一样本解耦 | D9″ 髓系 SPP1 空间共定位 |
| TCF4→CTSS | **42831790** / 10.1530/erc-25-0517 | MO+PR | PTC | GEO + TCGA-THCA + **eQTL** | eQTL 遗传工具 + IHC/qRT-PCR/WB + 裸鼠 | DFS、LNM、RAI 抵抗 | CTSS 为 TCF4 下游驱动基因，经 PI3K/AKT/mTOR 促癌 | 公共队列 + 体内外 | OA closed；eQTL 为血源 eQTL 可能性需核 | High | CTSS 在**免疫细胞 vs 肿瘤细胞**的贡献未拆分 | D21 区室化 eQTL |
| ETV4→STAT6 | **41759995** / 10.1080/07435800.2026.2629919 | ME+IM | THCA 细胞系 | 细胞系 + 公共 | qRT-PCR/WB + ROS/MDA/GSH/Fe²⁺ + 流式 | 铁死亡、免疫逃逸 | ETV4 转录激活 STAT6 → SLC7A11↑ + PD-L1↑ | 仅体外 | 无体内、无临床队列、无 scRNA | High | 未验证 STAT6 阻断能否恢复铁死亡敏感性 | **D12′** 铁死亡–免疫逃逸耦合 |
| IGF2BP2→m⁶A-PHGDH | **42174614** / 10.1186/s12967-026-08316-6 | ME+MO | TC（TPC-1/8505C） | 组织 + 细胞 + LC-MS | IHC + RNAi/慢病毒 + RIP/m⁶A-RIP + 转录组 | 增殖/侵袭/代谢 | m⁶A 稳定 PHGDH → 丝氨酸代谢重编程 | 体内外 + 代谢组 | 缺少独立临床队列预后验证 | High | PHGDH 抑制剂在甲状腺癌未测 | D18 代谢–耐药 |
| 脂代谢 9 基因签名 | **42157886** / 10.1155/ijog/9661210 | ME+PR | THCA | TCGA + GEO + MR + scRNA | MR + 共识签名 + Cox + 功能（ACBD7） | 预后、免疫格局 | 9 基因签名分层预后；高危组 BRAF 突变率更高；ACBD7 促侵袭 | MR 因果 + 多队列 + 功能 | **MR/scRNA/功能三层未在同一批样本贯通** | High | ACBD7 的区室与机制不明 | **D21″** 首选 |
| 菌群 + 代谢组（PTC/BRAF） | **42043696** / 10.1007/s12020-026-04607-6 | ME+IM | 70 PTC vs 70 HC | 粪便 16S + LC-MS/MS | 差异菌属 + 随机森林 10 折 | PTC 风险、BRAF V600E | 19 个差异菌属；RF 可判别 | 内部交叉验证 | **无外部验证、横断面、因果方向不明** | High | 与既往两轮菌群结论**方向相反** | D17 菌株特异 MR |
| ATC 代谢–免疫抑制 | **41716397** / 10.3389/fimmu.2026.1699202 | ME+IM | ATC | 文献 | 叙述性综述 | — | 营养竞争/抑制性代谢物/检查点代谢调控三条路径 | 无（综述） | 不作一级证据 | High | 缺少单细胞/空间层面的 ATC 代谢-免疫图谱 | D15 + D21 |
| SPARCL1→SLC3A2 | **42160309** / 10.1530/erc-26-0018 | ME | PTC | 细胞 + 裸鼠（皮下 + 多器官转移） | 过表达/上清回加/重组蛋白 + 转移模型 | 侵袭、转移 | 分泌型 SPARCL1 经 SLC3A2 诱导铁死亡抑制转移 | 体内外三路 | 未做临床队列相关性 | High | 重组 SPARCL1 的药代与免疫原性未测 | D12′ 转化支线 |
| BRAF^V600E 小鼠 ITH | **41935217** / 10.1038/s41388-026-03742-8 | MO+SC | 成年自发 BRAF^V600E 小鼠 PTC | 小鼠 scRNA-seq + **类器官** | 轨迹推断 + 亚群特异通路 + 类器官验证 | EMT 状态、恶性度 | 恶性细胞沿 EMT 轨迹推进，各亚群以特异通路维持 EMT | 类器官功能验证 | **小鼠模型**；人样本验证缺 | High | 人 PTC 中是否存在同构 EMT 亚群 | D11 + D15 |
| 微生物群与甲状腺癌 | 待编目 / 10.3389/fimmu.2026.1912576 | MO+IM | TC | 文献 | 综述（GM + ITM） | — | ITM 直接参与 TC 发生/进展/侵袭 | 无（综述） | 综述 | High | ITM 在甲状腺癌几乎无原发数据 | D17 |
| IL-10/IL-22（MTC+PTC） | 待编目 / 10.22141/…1753 | MO+PR+IM | MTC + PTC | 组织 + 转移灶 + 血浆 | ELISA 配对 | 转移状态 | 组织与血浆 IL-10/IL-22 差异 | 单中心配对 | 样本量未知、无随访 | High | 血浆能否替代组织未做诊断学评价 | D16 |
| BRAF 降期 IVC ATC | 待编目 / 10.4103/trp.trp_50_26 | MO+PR+IM | ATC IVC 期，1 例 | 个案 NGS | dabrafenib+trametinib 降期 + 手术 | 可切除性 | 「BRAF+TERT+TP53」三打击 ATC 可靶向降期后根治 | 个案 | **n=1** | High | 三打击基因型是否预示降期成功率 | D15/D18 |
| PTC 多模态 ML 视角 | **42822363** / 10.1016/j.clinsp.2026.101120 | AL | PTC | 文献 | 视角/方法学 | — | pathomics × radiomics 融合路线 | 无 | 摘要不可得，需全文 | High | 缺少可复现的融合基准 | D13-M |
| Human vs AI（RAI） | **42791092** / 10.1016/j.surg.2026.110590 | AL+PR | DTC，100 例 | 单中心回顾 | 4 个 LLM 平台 vs 医师 vs 共识估计 | RAI 决策一致性 | AI 推荐可与医师处方/共识基准比较 | 内部基准 | n=100、单中心、**无患者结局** | High | 未评估 AI 推荐对真实复发率的影响 | **D13 范式转移** |
| LLM 融合 SPECT 影像组学 | **42420643** / 10.1007/s11307-026-02114-8 | AL | DTC，311 例 | 单中心 SPECT | 1,688 特征 + 早/晚融合 + **LoRA 微调 LLM** | ¹³¹I 疗效 | LLM 增强融合提升预测性能 | 内部交叉验证 | **无外部验证** | High | LLM 增益的可解释性与稳定性 | D13 |
| Radiopathomics 预测 ETE | **42104301** / 10.1186/s12902-026-02308-9 | AL+PR | PTC，388 例/5 中心 | 超声 + 400× 细胞学图像 | LASSO + XGBoost + SHAP | 甲状腺外侵犯（病理金标准） | 融合模型外部 AUC **0.887/0.857**，优于/可比医师 | **多中心外部验证 + reader 比较** | 回顾性；细胞学图像质量依赖 | High | 未与分子标志物（BRAF/TERT）融合 | **D13-M 首选执行模板** |
| FN1–ANXA1–PTK2B（LNM） | 待编目 / 10.21203/rs.3.rs-9688961/v1 **[preprint]** | MO+PR | PTC LNM | 蛋白质组 + 转录组 | 整合组学 + 网络分析 | LNM | FN1–ANXA1–PTK2B 网络驱动 LNM | 无外部验证 | **预印本，降档** | High | 未做空间/单细胞区室归属 | D21 区室化 |

### 3.2 Medium 相关性压缩矩阵

| # | 论文（简称） | 维度 | 数据/人群 | 关键发现 | Relevance | Gap / 未解 |
|---|---|---|---|---|---|---|
| M1 | 儿童 PTC 综述 | MO+PR | 文献 | 融合型驱动为主，高转移率但高生存 | Medium | 儿童 vs 成人的 TME 差异无单细胞对照 |
| M4 | 高容量颈部 LNM 预测 | AL+PR | 521 + 193（**地理外部验证**） | Ridge 逻辑回归；分子变量增量价值在两队列不一致 | Medium | **分子变量的跨中心可迁移性差**——本轮最重要的算法方法学警示 |
| M5 | 空间转录组 PRISMA 综述 | SP | 文献 | 甲状腺癌空间组学的平台/架构/应用全谱 | Medium | 本轮**唯一**空间维度证据；反映该维度仍极稀疏 |
| M8 | KU-57788→DRP1→铁死亡 | ME | ATC 体内外 | DNA-PKcs 抑制剂直接激活 DRP1，NRF2/SLC7A11/GSH 为保护性反馈 | Medium | 保护性反馈的克服策略未临床化 |
| M10 | METTL7B→USP28/HIF-1α | ME+MO | GEO+TCGA+组织芯片 | 糖酵解与恶性进展 | Medium | USP28 去泛素化底物谱未做 |
| M11 | TMED2→mTORC1 脂肪酸 | ME | scRNA + TCGA + 裸鼠 | 脂滴累积、FA 合成酶上调 | Medium | 区室归属仅用公共 scRNA，未自建 |
| M13 | KRT15/KRT81→DGKB 脂代谢 | ME+PR | 体内外 + shRNA/药理 | 仑伐替尼耐药机制 | Medium | 未与临床耐药队列验证 |
| M14 | 酮体代谢 ATC | ME | 8505C/CAL-62 + 异种移植 | 乙酰乙酸抑制增殖；生酮饮食体内有效 | Medium | "初步研究"，机制层薄弱 |
| M15 | ATP2C2–PLA2R1（VGIC） | ME+MO | GEO+TCGA | 6 基因 VGIC 预后签名 | Medium | 离子通道基因与脂代谢的因果链未验证 |
| M16 | 外泌体 miR-145-5p→TPM3 | MO | 公共库 + 细胞 | 失活 PI3K-Akt 抑制 PTC | Medium | 外泌体递送效率与体内分布未测 |
| M20 | FTC-Net（VLM） | AL | 14 机构 2421 例 | 外部 AUC 0.836/0.841，优于 TI-RADS | Medium | 滤泡性肿瘤的**良恶性**仍是细胞学盲区，模型未解决 FTC vs FTA 的金标准偏倚 |
| M23 | LymphUs 开放数据库 | AL+PR | 338 例，2 中心 | 分割掩码 + 16 项语义特征 + FNA 金标准 | Medium | **数据资源**，非方法论文；可直接复用 |
| M24 | Agentic no-code AI | AL | TN5000 + 232 外部 | 自主代理完成审计/建模/校准 | Medium | 模型锁定后未做前瞻；可复现性依赖平台 |
| M25 | AI 代表性路线图 | AL | 方法学 | 四阶段：代表性数据/情境变量/训练验证/部署后监测 | Medium | 无配套基准数据集 |
| M27 | OCA 日本 137 例 | PR | 单中心 | 10/15 年无远处复发 100%/92.7% | Medium | 远处转移者均 ≥60 岁、肿瘤 >4 cm、合并血管/包膜侵犯 |
| M28–M30 | 热消融治疗 LNM（3 篇） | PR | 29 研究 SR + 101 例多中心 + 230 例双中心 | 与再手术 36 个月复发率无差异，并发症相当，成本更低 | Medium | **全部回顾性**；缺少前瞻随机与长期（>5 年）结局 |
| M31 | 右喉返神经后 LNM 预测 | PR+AL | 721 例 cN0 | 气管旁数目 + 喉前/气管旁合并转移为独立预测因子 | Medium | 单中心、无外部验证 |
| M33/M34 | FN1 轴（2 篇） | MO | 6 套 RNA-seq / 配对组织 | FN1 为枢纽；ITGA7–FN1 抑制 PI3K/AKT | Medium | bulk 相关，无空间区室 |

---

## 四、已知结论 (What Is Already Known)

以下结论由**两条及以上独立证据**或**强数据集**支撑：

1. **SPP1 是甲状腺癌 TME 中跨亚型保守的髓系效应分子。** PTC 中 CD36⁺ 巨噬细胞分泌 SPP1 激活肿瘤细胞 PI3K-AKT（本轮，PMID 39178310）；ATC 中 SPP1⁺/APOC1⁺ TAM 获 scRNA 证据（Run #25/#26）；外泌体 SPP1→CD44/JAK2/STAT3→M2 极化（Run #24）。**三者分属 PTC/ATC/体外三套体系，但配体来源一致指向髓系。**
2. **铁死亡抵抗与免疫逃逸在甲状腺癌中由共享上游节点耦合，而非两条平行通路。** ETV4→STAT6→SLC7A11 + PD-L1（本轮）；SENP1→HIF-1α→铁死亡（本轮）；CD36⁺ 巨噬细胞的促炎表型同时受碘代谢调控（本轮）；ATC 代谢重编程→免疫抑制 TIME（本轮综述）；叠加 Run #26 的 TRIM47–FBP1 乳酸化正反馈与 Run #25 的 HIF-1α–ACSL4。
3. **脂代谢重编程是甲状腺癌预后与耐药的共同底层。** 9 基因脂代谢签名（MR + scRNA + 功能，本轮）；KRT15/KRT81–DGKB 脂代谢→仑伐替尼耐药（本轮）；TMED2–mTORC1 脂肪酸合成（本轮）；ATP2C2–PLA2R1–VGIC（本轮）；Run #27 的 APOC1–VLDL 轴；Run #25 的 GPI–O-GlcNAc–THBS1。
4. **EMT/去分化轨迹具有亚群特异性通路依赖，而非单一连续体。** BRAF^V600E 小鼠 scRNA + 类器官（本轮）显示各恶性亚群以不同通路维持 EMT 状态；与 Run #24 的 UBE2C⁺ ATC-like、Run #23 的突变特异性去分化 snRNA 图谱一致。
5. **甲状腺癌 AI 研究已越过"能否分类"阶段，进入"能否迁移、能否被信任、能否改变决策"阶段。** 本轮 5 条独立证据：地理外部验证失败风险（M4）、Human vs AI 头对头（PMID 42791092）、代表性路线图（PMID 41041822）、Agentic no-code 可复现（PMID 42808848）、多中心外部验证 + reader 比较（PMID 42104301）。
6. **复发性颈部淋巴结转移的微创热消融在肿瘤学结局上不劣于再手术。** 系统综述（29 研究）+ 多中心 101 例 + 双中心 230 例（36 个月复发率无差异，p=0.54）三条独立证据一致。
7. **肠道/瘤内菌群与甲状腺癌的关联是菌株特异的，整体命题不成立。** 本轮 Collinsella/Carnobacterium/Moryella 富集；Run #26 *Terrisporobacter*→NTRK1（促瘤）；Run #27 *Ruminococcaceae*→RBM15→NLRP3（抑瘤/焦亡）。三轮方向互不一致。

---

## 五、未解问题 (What Remains Unclear)

1. **区室归属（compartment assignment）是本轮最大的未解问题。** SPP1（髓系 vs 上皮）、APOE（髓系 Macro2 / 基质 APOE⁺ PVL / 上皮 APOE-high tumor）、CTSS（肿瘤 vs 免疫）、FN1（肿瘤 vs 基质）——**本轮没有任何一篇在同一批样本上同时测量并解耦这些分子的来源区室**。Run #27 已提出该问题，本轮未改善。
2. **碘代谢与 TAM 极化的因果方向未定。** CD36 论文显示"碘代谢失调与促炎表型获得密切相关"，但究竟是低碘驱动 M1 样极化，还是炎症继发碘处理障碍（NIS 下调），论文未给出时间序列或干预-逆转证据。
3. **ETV4 的多轴枢纽身份是真实生物学还是发表偏倚？** ETV4 同时出现在乳酸化–EMT（Run #21）与铁死亡–免疫逃逸（本轮）两条轴，但两篇均无体内模型，且均由同一类细胞系实验支撑。
4. **分子变量的跨中心可迁移性存在实证反例。** M4（高容量 LNM）明确报告高危共突变状态与突变计数的增量价值在 Deyang 与 Liaocheng 两队列间**不一致**。这直接威胁所有"临床 + 分子"混合模型的部署前提。
5. **脂代谢三层证据（MR 因果 / scRNA 区室 / 功能验证）分属不同样本集。** 9 基因签名论文的 MR、单细胞、ACBD7 功能实验未做同批次贯通，因此"遗传因果 → 细胞类型 → 功能"三段链条实际未闭合。
6. **菌群研究全部为横断面，** 无干预、无时间序列、无外部验证；且 16S 物种级分辨率无法支撑菌株特异结论。
7. **热消融证据全部回顾性，** 缺少前瞻随机对照与 >5 年结局；患者选择偏倚（拒绝/不耐受手术者）无法排除。
8. **空间组学维度本轮仅 1 条（且为综述）。** 单细胞 2 条。这既可能是真实低产，也可能是通道性欠采样——见 §6。

---

## 六、领域方法/数据局限 (Method/Data Limitations In The Field)

| 局限 | 本轮实证 | 影响 |
|---|---|---|
| **公共数据复用 + 队列同质** | 至少 8 篇仅用 TCGA + GEO 差异表达 + 生存，无自建队列 | 结论不可外推；同一批数据被反复"再发现" |
| **外部验证缺失** | 19 条算法论文中仅 5 条有真正外部验证（M4、M20、M22、M24、M16-radiopathomics） | AUC 虚高，临床可用性存疑 |
| **终点稀疏/替代终点** | 铁死亡/代谢类论文终点多为细胞活力、ROS、MDA/GSH，极少以复发/生存为终点 | 无法推断临床效用 |
| **单细胞/空间维度产出极低** | 本轮 SC=2、SP=1 | 区室归属问题（§5.1）无法解决 |
| **撤稿/更正污染** | EPMC 候选池中 15 条（9.3%）为撤稿/更正/补充材料 | 若不剔除将污染证据矩阵 |
| **NCBI 全域不可达** | 本轮未使用（HTTP 000 实测）；GEO 数据须转 ENA | 论文中的 GSE 编号是"引用"而非"可下载" |
| **预印本与低质期刊混杂** | 本轮 2 条预印本 + 数篇低影响力期刊（如 10.22141/*、10.52532/*） | 需逐条降档，不可等权纳入 |
| **模型部署后监测缺位** | 仅 Roadmap（M25）提出四阶段框架，无实证 | 校准漂移问题（Run #25 已记录）仍未解决 |

---

## 七、候选未来方向 (Candidate Future Directions)

按 `research-direction-rubric.md` 七维评分（各维 1–5，总分 7–35；**28–35 为强候选**）。**评分口径：Run #27 起改为七维明细逐项求和**，跨轮比较请以重算值序列为准。

| 方向 | N 新颖 | F 可行 | D 数据 | V 验证 | C 临床 | M 严谨 | O 反拥挤 | **总分** | 状态 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| **D21″ 脂代谢重编程 × 免疫生态位 × 获得性耐药（跨区室整合）** | 4 | 5 | 5 | 4 | 4 | 4 | 3 | **29** | ⭐ 首选，本轮强化 |
| **D13 算法：从"造模型"到"嵌流程 / 评人 / 评公平"** | 4 | 5 | 5 | 4 | 5 | 4 | 2 | **29** | ⭐ 并列首选，本轮范式升级 |
| **D13-M 多模态 radiopathomics（影像 × 细胞病理）** | 4 | 5 | 4 | 4 | 4 | 4 | 3 | **28** | 本轮新立（D13 的具体执行形态） |
| **D18 代谢–耐药轴** | 4 | 4 | 4 | 4 | 5 | 4 | 3 | **28** | 本轮强化（仑伐替尼耐药 + BRAF 降期） |
| **D12′ 铁死亡–免疫逃逸耦合**（由 D12 升级） | 4 | 4 | 4 | 4 | 4 | 4 | 4 | **28** | 本轮升级：ETV4 提供双表型节点 |
| **D9″ SPP1 髓系来源的空间共定位与区室解耦** | 4 | 4 | 4 | 4 | 4 | 4 | 2 | **26** | 本轮强化（CD36 提供来源）但反拥挤分低 |
| **D11 EMT / 去分化轨迹的亚群特异通路** | 4 | 4 | 4 | 3 | 3 | 4 | 4 | **26** | 维持（小鼠类器官新证据） |
| **D15 去分化 / ATC** | 3 | 4 | 4 | 3 | 5 | 4 | 3 | **26** | 维持 |
| **D16 MTC 远处转移** | 3 | 4 | 3 | 3 | 4 | 4 | 4 | **25** | 本轮弱化（仅 IL-10/22、MCP-1、1 例颅内转移） |
| **D8 TAM 极化全景** | 3 | 4 | 4 | 3 | 4 | 4 | 2 | **24** | 维持但**反拥挤分降至 2**（CD36 为第 6 条通路） |
| **D17 肠道/瘤内微生物群** | 4 | 4 | 4 | 3 | 3 | 3 | 3 | **24** | 本轮强化，但**方向矛盾未解** |
| **D24 复发性颈部 LNM 的微创局部治疗分层** | 3 | 3 | 4 | 3 | 5 | 3 | 2 | **23** | 本轮新立（3 篇独立证据） |
| **D20 儿童/AYA PTC** | 3 | 4 | 3 | 3 | 4 | 4 | 4 | **25** | 维持 |
| **D3″ APOE × MGST1 代谢–免疫干性亚群** | — | — | — | — | — | — | — | **归档** | ❌ 终判阴性，见 §11 |

### 方向要点（Top 3）

**D21″ 脂代谢重编程 × 免疫生态位 × 获得性耐药（跨区室整合）— 29**
- Research question：在甲状腺癌中，脂代谢重编程的**因果层（MR）**、**细胞层（scRNA 区室）**与**功能层（耐药表型）**能否在同一批样本上贯通？特别是 APOE/SPP1 的髓系 vs 上皮来源如何改变结论方向。
- Novelty angle：现有文献三层分离；无人做同批次贯通。
- Required datasets：TCGA-THCA（bulk + 生存）、GSE193581（成人 PTC scRNA，跨队列桥梁）、iScience 儿童 PTC（PMC13378368，Macro2 = SPP1+APOC1+APOE）、公开空间底图（JCI Insight 个体级受 IRB 限制 → 需另寻 ENA/合作节点）。
- Expected endpoint：无复发生存 + 仑伐替尼/RAI 耐药。
- Analysis strategy：① 用 9 基因脂代谢签名在 scRNA 上按 compartment 拆分（上皮/髓系/基质/成纤维）；② 检验签名评分在髓系 compartment 是否由 APOE/SPP1/CD36 主导；③ 与 KRT15/KRT81–DGKB、TMED2–mTORC1 两套耐药机制做通路收敛分析。
- Validation plan：TCGA-THCA 为发现队列 → GSE193581 + 儿童队列跨年龄验证 → 独立 IHC 队列（若有）。
- Major risk：公开空间底图不可得（NCBI GEO 不可达）；APOE 三 compartment 混用是最大错误来源。
- Claim boundary：**不可声称"脂代谢基因 X 驱动甲状腺癌进展"**——只能声称"在 Y compartment 中，该基因的评分与 Z 终点相关，且 MR 支持其因果方向"。

**D13 算法：嵌流程 / 评人 / 评公平 — 29**
- Research question：甲状腺癌 AI 模型在**跨中心迁移、人机决策一致性、部署后校准漂移**三个环节上各自失败于何处？
- Novelty angle：绝大多数 AI 论文只报 AUC；本轮 5 篇已转向评测 AI 本身。
- Required datasets：LymphUs（338 例淋巴结超声，gold OA，本轮即可下载）、TN5000（agentic 论文所用开源集）、自建多中心超声 + 细胞学配对（参照 radiopathomics 论文的 5 中心设计）。
- Expected endpoint：模型在**地理外部队列**的性能衰减幅度；AI 推荐 vs 医师处方 vs 指南共识的三方一致率。
- Analysis strategy：① 用 LymphUs 做跨中心域偏移基线；② 复现 radiopathomics 的 US+ cytology 双模态融合（XGBoost + SHAP）；③ 加入分子变量后测量跨中心性能衰减（直接检验 M4 的迁移性失败）。
- Validation plan：中心 1 训练 → 中心 2/3 地理外部验证 → reader study（≥3 名不同年资医师）。
- Major risk：甲状腺超声 AI 已高度拥挤（O=2）；必须靠"评模型"而非"造模型"建立差异。
- Claim boundary：**不可声称 AI 优于医师**——只能声称"在 X 队列上，AI 与医师的一致率为 Y，且在 Z 亚组中不一致集中在……"。

**D13-M 多模态 radiopathomics — 28**（D13 的具体执行形态，见 §8）

---

## 八、推荐下一步方向 (Recommended Next Direction)

### 首选：D21″ 脂代谢重编程 × 免疫生态位 × 获得性耐药的跨区室整合（rubric 29）

**理由**：本轮机制簇最密集（ME 20 + IM 10 = 43%），且三层证据（MR 因果 / scRNA 区室 / 功能耐药）**同时到齐但彼此分离**——这正是最容易被一篇整合性研究闭合的缺口。零湿实验即可启动 M1。

**首批具体步骤（无需湿实验）**：
- **M1 区室拆分基线**：把本轮 9 基因脂代谢签名（PMID 42157886）投影到 GSE193581 成人 PTC scRNA，按 epithelial / myeloid / stromal / fibroblast 四个 compartment 分别打分，输出"签名评分由哪个 compartment 贡献"的量化表。
- **M2 CD36/SPP1 锚定检验**：以本轮 CD36⁺ 巨噬细胞特征（PMID 39178310）为查询集，检验其在髓系 compartment 与脂代谢签名的共表达；同步检验 APOE 在髓系（Macro2）/基质（APOE⁺ PVL）/上皮三个 compartment 的分布是否互斥。
- **M3 耐药通路收敛**：把 KRT15/KRT81–DGKB（仑伐替尼耐药）、TMED2–mTORC1（FA 合成）、METTL7B–USP28/HIF-1α（糖酵解）三条本轮新通路做 GSEA 收敛分析，找出共同下游节点。
- **M4 空间锚定（条件性）**：优先 ENA / NGDC GSA-human 检索公开甲状腺 Visium/GeoMx 数据集；JCI Insight 个体级数据受 IRB 限制，**仅作单细胞参考与方法学范本**，不作空间底图。
- **M5（可选）MGST1 终判已在本轮完成 → 阴性，不再投入。**

**所需数据集**：TCGA-THCA、GSE193581、iScience PMC13378368、ENA（替代 GEO）。
**验证要求**：至少一个独立 scRNA 队列 + TCGA 生存层；若有可能，IHC 双色染色验证髓系 vs 上皮来源。
**应避免的主张**：不得声称"MGST1 与 APOE 互斥"（已证伪）；不得把不同 compartment 的 APOE 信号合并报告。

### 并行第二赛道：D13-M 多模态 radiopathomics（rubric 28）

直接复用本轮 PMID 42104301 的模板（388 例 / 5 中心 / 超声 + 400× 细胞学 / XGBoost + SHAP / 外部 AUC 0.887）+ LymphUs 开放数据库（PMID 41940127，gold OA，338 例带分割掩码）+ M4 报告的"分子变量跨中心迁移失败"作为**待解决的具体问题**。这条赛道**数据立即可得、方法明确、终点为病理金标准**，是本轮可执行性最高的方向。

---

## 九、随访阅读清单 (Follow-Up Reading List)

| 优先级 | 论文 | 为什么下一步读 |
|---|---|---|
| 1 | CD36⁺ Mac × ZCCHC12⁺（PMID 39178310） | 本轮唯一给出"碘 → TAM → SPP1"完整链条的论文；决定 D9″/D21″ 的区室设计 |
| 2 | 脂代谢 9 基因签名 + ACBD7（PMID 42157886） | D21″ 的核心支柱；MR + scRNA + 功能三层，需逐层核对样本是否同源 |
| 3 | ETV4→STAT6→SLC7A11/PD-L1（PMID 41759995） | D12′ 的双表型节点；决定铁死亡–免疫逃逸耦合是否成立 |
| 4 | Radiopathomics 预测 ETE（PMID 42104301） | D13-M 的执行模板；多中心 + 外部验证 + SHAP + reader 比较齐全 |
| 5 | Human vs AI（RAI 决策）（PMID 42791092） | D13 范式转移的标志；学习其"共识知情估计"基准构建法 |
| 6 | 高容量颈部 LNM 跨中心验证（10.3389/fonc.2026.1963925） | **负结果价值**：分子变量跨中心迁移失败的直接证据 |
| 7 | BRAF^V600E 小鼠 ITH + 类器官（PMID 41935217） | D11/D15 的体内轨迹框架；类器官验证方式可复用 |
| 8 | Spatial Transcriptomics in Thyroid Cancer PRISMA 综述（10.3390/jcm15197636） | 本轮唯一空间证据；用于确定可用平台与已发表的空间数据集清单 |
| 9 | ATC 代谢–免疫抑制综述（PMID 41716397） | D21 在 ATC 端的理论框架；OA gold 可取全文 |
| 10 | IGF2BP2→m⁶A-PHGDH（PMID 42174614） | D18 的代谢–表观–耐药三元链条；PHGDH 第二次出现 |
| 11 | Roadmap for Representative AI Models（PMID 41041822） | D13 的公平性/部署监测框架 |
| 12 | LymphUs 数据库（PMID 41940127） | D13-M 的现成数据；gold OA |

---

## 十、可复现性说明 (Reproducibility Notes)

- **Search date / 检索日期**：2026-10-09 03:02–03:30 (UTC+8)
- **Databases / 数据库**：OpenAlex `api.openalex.org`；Europe PMC `www.ebi.ac.uk/europepmc/webservices/rest`；Crossref `api.crossref.org`；Unpaywall `api.unpaywall.org`
- **Query strings / 查询式**：见 §1；完整脚本见 `_epmc_run28.py`、`_deep_run28.py`、`_keyabs_run28.py`、`_enrich_run28.py`、`_final_run28.py`、`_d3check_run28.py`
- **Filters / 过滤**：OpenAlex `from_publication_date` + `sort=publication_date:desc`；Europe PMC `TITLE:"thyroid"` + `PUB_YEAR:2026` + `sort=P_PDATE_D desc`；深挖 `from_publication_date:2026-06-01`
- **Deduplication rule / 去重规则**：DOI（小写、去 `https://doi.org/` 前缀）优先；缺失时以标题归一化（仅保留字母数字，截断 90 字符）为键；与 457 条累积基线比对
- **Screening rule / 筛选规则**：标题须点名甲状腺（thyr*/PTC/FTC/MTC/ATC 等）**且**整体为肿瘤主题；撤稿/更正/补充材料剔除；预印本降档
- **通道可用性**：OpenAlex ✅；Europe PMC ✅；Crossref ✅（本轮部分请求超时）；Unpaywall ⚠️（本轮部分请求超时）；**NCBI 全域 ❌ 不可达（HTTP 000）**；paper-search-mcp 本会话未连接
- **Files saved / 产出文件**：
  - `literature_review_20261009_030249.md`（本报告）
  - `search_results_20261009_030249.json` / `search_results_latest.json`（累积基线 **527**）
  - `search_results_20261009_030249_new.json`（本轮 70 条新增）
  - `search_results_20261009_030249_30d.json`、`_90day.json`、`_epmc.json`、`_deep.json`、`_keyabs.json`、`_030249_enrich.json`
  - `search_results_latest_backup_run27.json`（Run #27 基线备份）
  - 脚本：`_epmc_run28.py`、`_deep_run28.py`、`_keyabs_run28.py`、`_enrich_run28.py`、`_final_run28.py`、`_d3check_run28.py`

---

## 十一、与历史报告的差异 (Delta vs Previous Runs)

### 11.1 本轮新增 vs Run #27（基线 457 → 527）

| 项 | Run #27 | Run #28 | 变化 |
|---|---:|---:|---|
| 新增唯一记录 | 66 | **70** | +4 |
| OpenAlex 贡献 | 9 | **15** | +6（30 d 窗口真新增回归正常） |
| Europe PMC 贡献 | 56 | **50** | −6 |
| 深挖贡献 | 1 | **5** | +4（面板扩至 34 起效） |
| High / Medium / Low | 12 / 39 / 15 | **17 / 34 / 19** | High 占比 19% → 24% |
| 严格预印本 | 0 | **2** | +2 |
| 累积基线 | 457 | **527** | +70 |

### 11.2 相对上次的新信号 / 方向变化

1. **🔴 新增：碘–TAM–SPP1 轴（本轮最大增量）。** 既往 27 轮的 TAM 研究（TREM2/AHR-IDO1、SPP1/CD44-JAK2-STAT3、RARγ/CFI、BGN/NR2F2、CCL2-VSIG4）**从未涉及碘**。本轮 CD36 论文把甲状腺最特异的变量接入 TAM 极化，开辟了全新的干预维度（补碘/限碘）。
2. **🔴 方向升级：D12 铁死亡 → D12′ 铁死亡–免疫逃逸耦合。** ETV4→STAT6 同时调控 SLC7A11（铁死亡）与 PD-L1（免疫逃逸），使"铁死亡"从单一死亡方式研究升级为"代谢–免疫"接口研究。
3. **🔴 范式升级：D13 算法。** 由 Run #26 的"ML × LLM 融合"、Run #27 的"嵌流程 + reader study"，升级为本轮的**三条并行评测线**：人机决策头对头、模型代表性/公平性路线图、Agentic 自主建模可复现性。
4. **🟡 结构性缺口暴露：分子变量的跨中心不可迁移。** M4 首次在甲状腺癌中给出"分子变量增量价值随队列变化"的负结果，与 Run #25 的"校准漂移/本地更新"呼应 → 这是 D13 的最佳切口。
5. **🟡 空间/单细胞维度继续稀疏（SP=1、SC=2）。** 已连续 8 轮验证 30 d 窗口对 SC/SP/IM/ST/ME 结构性不足；本轮虽已固化 90 d + 三通道，空间维度仍仅 1 条（综述）。见 §11.4。
6. **🟢 新立方向：D13-M（多模态 radiopathomics，28）、D24（复发性 LNM 微创分层，23）。**

### 11.3 持续跟踪方向状态：D3″（APOE−/MGST1+ 代谢–免疫干性亚群）

> **本轮判定：终判阴性 → 正式归档（Archived as tested-negative hypothesis）**

| 检验项 | 结果（2026-10-09 实测） | 判定 |
|---|---|---|
| OpenAlex 全库 `MGST1 × thyroid` | **1** 篇（10.3389/fimmu.2026.1848083，PMID 42327722） | 连续第 3 轮零增长 |
| Europe PMC 全时间 `MGST1` × `thyroid` | **1** 篇（同上） | 同上 |
| OpenAlex 全库 `APOE × MGST1 × thyroid` 三词共现 | **0** | 孤岛未破 |
| 同期对照：APOE × thyroid（2026） | **7** 篇 | 反差悬殊 |
| 同期对照：APOC1 / CD36（2026） | 5 / 2 篇 | 反差悬殊 |

**结论**：Run #24 首次提出"APOE 高表达肿瘤亚群"、Run #25 首次锚定 MGST1、Run #27 因"APOE 被证为促癌"重构为 D3″ 双轴假设——但**连续 4 轮（#25–#28）MGST1 文献数恒为 1，三词共现恒为 0**。按 Run #27 预注册的 M5 终判规则，**D3″ 归入「已检验假设（阴性）」，不再作为候选方向投入**。

**残余价值处理**：D3″ 唯一有生命力的部分——"APOE 在髓系 Macro2 / 基质 APOE⁺ PVL / 上皮 APOE-high tumor 三个 compartment 必须分开报告"——**整体并入 D21″**（§8）。本轮 CD36 论文首次提供髓系 compartment 的脂处理巨噬细胞锚点，使该问题有了可检验的载体。

### 11.4 关于"低新增"的判定

本轮 OpenAlex 30 d 窗口新增 15 条（2026-09/10 真实新发），属**正常日更量**（距 Run #27 已 6 天）。Europe PMC + 深挖的 55 条中有 **42 条为 2024-11 ~ 2026-08 的历史欠采样回填**，说明即便三通道固化后，历史轮次仍存在可观漏检——**再次确认：历史"低新增"主要是查询矩阵覆盖不足，而非领域平台期。**

但需注意一个**真实信号**：空间组学维度本轮仅 1 条且为综述。在 SC/SP 已用 90 d 窗口 + 三通道 + `SPATIAL_DS`/`MACRO2`/`LIPID` 三路专项查询的条件下仍极低产，**这更可能是甲状腺癌空间组学真实的低产出状态**（受制于样本获取与平台成本），而非检索问题。建议下轮对该维度做一次**不限年份的全库普查**以最终确认。

---

## 十二、代码仓同步结果 (Repository Sync)

| 步骤 | 结果 |
|---|---|
| `git pull --rebase --autostash origin main` | ✅ 成功（第 1 次尝试，Already up to date） |
| `git status -sb` | ✅ `## main...origin/main`，跟踪关系正常 |
| 本轮提交文件 | `lit_review/literature_review_20261009_030249.md`；`lit_review/search_results_20261009_030249.json`；`lit_review/search_results_latest.json` |
| commit sha | 见下方最终回复 |
| `git push origin main` | 见下方最终回复 |

---

*报告生成：2026-10-09 · Run #28 · 三通道（OpenAlex / Europe PMC / 定向基因深挖）· 累积基线 527 条*
