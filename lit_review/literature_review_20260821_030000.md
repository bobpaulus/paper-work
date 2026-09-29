# 甲状腺癌文献监测报告 / Thyroid Cancer Literature Surveillance Report

**Date / 日期:** 2026-08-21 (run #19)
**Sources / 数据来源:** OpenAlex REST API（主源）; Crossref + Unpaywall（元数据与 OA 校验）; paper-search-mcp（未启用——主源已充分覆盖）
**Search window / 检索窗口:** `from_publication_date:2026-07-22`（近 30 天）；零增量维度 h 单独补跑 `--days 90`
**Primary retriever / 主检索器:** `lit_review/oa_search.py`（九路维度 a–i，`sort=publication_date:desc`，内建三类清洗与去重）
**Baseline / 基线:** `search_results_latest.json`（run #18, 2026-08-14, 81 条记录）

---

## 中文摘要 / Chinese Abstract

本轮（run #19，2026-08-21）以 OpenAlex 为主源完成甲状腺癌（PTC/PTMC/FTC/MTC/ATC）侵袭、淋巴结与远处转移、复发、预后及其分子机制、肿瘤免疫微环境、单细胞与空间组学、机器学习/深度学习方向的增量监测。近 30 天窗口（≥2026-07-22）共取回 **81 条唯一记录 / 54 篇在范围 / 剔除 27 篇**，**相对 run #18 基线真实新增 15 篇**（全部为正式发表论著，PMID 多「待编目」反映 PubMed 编目滞后）。三大收敛信号：(1) **桥本甲状腺炎（Hashimoto's thyroiditis, HT）自身免疫微环境降低 LNM 风险**——本轮出现一篇 High 级 scRNA-seq + 瘤内 16S 微生物组研究（iScience）与一篇剂量-效应 Frontiers 研究，从「上皮状态重塑 + 菌微生态偏移 + 先天免疫信号富集」层面为 HT–LNM 负关联提供机制解释，构成全新的「免疫热/LNM 冷」自然对照维度；(2) **微环境对去分化与放射性碘（RAI）抵抗的可塑性调控**（IJMS High 综述）明确指出去分化并非单纯细胞自主遗传事件，而由肿瘤–基质互作维持——直接验证 D3（APOE−/MGST1+ 代谢–免疫干性转移亚群）的核心前提；(3) **算法维度持续拥挤**——新增 SAM3 自动分割 DL 影像组学 CLNM 模型、ATA 风险列线图、AI 临床验证综述，进一步确认 D-ml 方向过度拥挤。推荐方向 **D3（rubric 总分 33，Strong，连续第 19 轮确认）**——本轮为**定性强化**（微环境可塑性综述 + HT 免疫冷/热对比 + 免疫逃逸 scRNA 标志物），无反证。

## English Abstract

Run #19 (2026-08-21) performs incremental surveillance of thyroid cancer (PTC/PTMC/FTC/MTC/ATC) covering invasion, lymph-node (LNM) and distant metastasis, recurrence, prognosis, molecular mechanisms, tumor immune microenvironment, single-cell and spatial omics, and machine/deep-learning methods. Using OpenAlex as the primary source over a 30-day window (≥2026-07-22), we retrieved **81 unique records / 54 in-scope / 27 excluded**, with **15 genuinely new papers versus the run #18 baseline** (all formal articles; most PMIDs "pending cataloging" reflecting PubMed lag). Three convergent signals: (1) **Hashimoto's thyroiditis (HT) autoimmune microenvironment reduces LNM risk** — a High-scoring scRNA-seq + intratumoral 16S microbiome study (iScience) plus a dose–response Frontiers study mechanistically explain the HT–LNM negative association via epithelial-state remodeling, microbial shift, and innate-immune enrichment, opening a new "immune-hot / LNM-cold" natural-comparator axis; (2) **microenvironmental control of dedifferentiation and radioiodine (RAI) resistance** (IJMS High review) asserts dedifferentiation is maintained by reciprocal tumor–stroma interactions, directly validating the premise of D3 (APOE−/MGST1+ metabolic–immune stem-like metastatic subpopulation); (3) **the algorithm dimension remains overcrowded** — a SAM3-segmentation deep-learning radiomics CLNM model, an ATA-risk nomogram, and an AI clinical-validation review further confirm D-ml is saturated. Recommended direction **D3 (rubric total 33, Strong, 19th consecutive confirmation)** — qualitatively strengthened this run (microenvironment-plasticity review + HT immune-cold/hot contrast + immune-escape scRNA signature), with no countervailing evidence.

---

## 检索策略 / Search Strategy

主检索器 `oa_search.py` 覆盖九路维度（a–i），`sort=publication_date:desc`，每路上限 25 条；维度 h（转移干性）30 天窗口增量为 0，按协议单独补跑 `--days 90`（中间产物 `search_results_20260821_90day_supplement.json`，不覆盖基线）。所有取回记录经三类清洗：剔除期刊补充材料条目（`Table_/Data Sheet_...`）、合并同篇多版本（本轮合并 27 组）、剔除仅顺带提及甲状腺的他病/良性病文献（标题须点名甲状腺且整体为肿瘤主题）。

| 路 | 维度代码 | OpenAlex Filter（节选） | Hits | 新条目 | 状态 |
|---|---|---|---:|---:|---|
| a | 分子机制/预后转移 | `thyroid … AND (metastasis/lymph node) AND (biomarker/signature)` | 17 | 15 | OK |
| b | 分子机制 | `thyroid … AND (invasion/metastasis) AND (mechanism/EMT)` | 30 | 19 | OK |
| c | 算法方法/预后转移 | `thyroid … AND (lymph node) AND (machine/deep learning/radiomics/nomogram)` | 10 | 10 | OK |
| d | 免疫微环境 | `thyroid … AND (metastatic) AND (immune microenvironment/macrophage/T cell)` | 15 | 5 | OK |
| e | 单细胞 | `thyroid … AND (metastatic/heterogeneity) AND (single-cell/scRNA-seq)` | 11 | 6 | OK |
| f | 空间组学 | `thyroid … AND (spatial transcriptomic/multi-omics/Visium)` | 11 | 2 | OK |
| g | 预后转移 | `thyroid … AND (prognosis/recurrence/distant metastasis) AND (risk model/survival/nomogram)` | 37 | 17 | OK |
| h | 转移干性 | `thyroid … AND (metastatic) AND (cancer stem cell/stemness/dedifferentiation)` | 5 | 0 | OK* |
| i | 代谢重编程 | `thyroid … AND (progression) AND (metabolic reprogramming/glycolysis/lipid/ferroptosis/OXPHOS)` | 12 | 7 | OK |

\* h 路 30 天窗口增量为 0 → 按协议补跑 `--days 90`（详见「零增量维度分析」）。

---

## 纳入论文 / Included Papers（本轮 15 篇新增）

> 英文标题与摘要为原文；括注一句话中文要点。相关性：High / Medium / Low。

**1. [High] Hashimoto's thyroiditis influences tumor cell states and intratumoral microbiota in papillary thyroid carcinoma.**
*iScience*, 2026-08-13. DOI: `10.1016/j.isci.2026.117167`. PMID: 待编目. OA: gold.
- Author claim: HT 相关 PTC 淋巴结转移更少，肿瘤内恶性上皮富集先天免疫信号程序且瘤内微生物多样性升高。
- Agent note: scRNA-seq + 16S 首次把「HT–LNM 负关联」推到上皮状态 + 微生物组层面，是本论题全新机制入口（见 D10）。

**2. [High] Microenvironmental Control of Thyroid Cancer Plasticity and Radioiodine Resistance.**
*Int. J. Mol. Sci.*, 2026-08-16. DOI: `10.3390/ijms27167305`. PMID: 待编目. OA: gold.
- Author claim: 去分化与 RAI 抵抗由恶性细胞与免疫/基质微环境的互作维持，而非单纯细胞内基因事件。
- Agent note: 直接验证 D3 前提（干性/可塑性是微环境维持的），机制层面强化 APOE−/MGST1+ 亚群假设。

**3. [Medium] Development of an immune escape-related gene prognostic signature using integrated single-cell and bulk RNA sequencing for immune microenvironment profiling in thyroid cancer.**
*Korean J. Physiol. Pharmacol.*, 2026-08-12. DOI: `10.4196/kjpp.25.445`. PMID: 42581622. OA: gold (Unpaywall).
- Author claim: 整合 scRNA + bulk 以 AUCell 量化免疫逃逸活性并构建预后基因标签，经 KM 与时间依赖 ROC 验证。
- Agent note: 单细胞 + 免疫逃逸标志，补充 D3 免疫组分与 D8（TREM2/AHR–IDO1）证据。

**4. [Medium] Serum and Tumor PD-L1 Expression and Aggressive Clinicopathologic Features in Papillary Thyroid Carcinoma.**
*JAMA Otolaryngol.–Head Neck Surg.*, 2026-08-13. DOI: `10.1001/jamaoto.2026.2200`. PMID: 42593786. OA: green (PMC).
- Author claim: 血清与瘤内 PD-L1 均与 PTC 侵袭性临床病理特征相关。
- Agent note: 延续 PD-L1（远处转移 vs LNM 解耦）元分析主题；补充血清 PD-L1 可及性维度。

**5. [Medium] Prediction of Central Lymph Node Metastasis in Papillary Thyroid Microcarcinoma Using a Deep Learning Radiomics Model Based on SAM3 Automatic Segmentation of Ultrasound Images: A Multicenter Cohort Study.**
*Acad. Radiol.*, 2026-08-01. DOI: `10.1016/j.acra.2026.07.064`. PMID: 42586895. OA: hybrid.
- Author claim: SAM3 自动分割 + DL 影像组学在 4 中心 1859 例 PTMC 中无创预测中央区 LNM。
- Agent note: 算法维度拥挤再确认（D-ml 过度拥挤）；多中心设计是少数亮点。

**6. [Medium] Genetic Mutations in Recurrent/Metastatic Papillary Thyroid Carcinoma.**
*Laryngoscope*, 2026-08-17. DOI: `10.1002/lary.70842`. PMID: 42605721. OA: hybrid.
- Author claim: 日本 C-CAT 348 例复发/转移 PTC 经 NGS 揭示 top-10 突变谱及其预后含义。
- Agent note: 复发/转移 PTC 真实世界突变锚点，补充 DTC 远处转移 vs LNM 解耦讨论。

**7. [Medium] A preoperative nomogram for predicting ATA risk stratification in papillary thyroid carcinoma: development and internal validation.**
*BMC Med. Imaging*, 2026-08-18. DOI: `10.1186/s12880-026-02702-8`. PMID: 待编目. OA: gold.
- Author claim: 基于 404 例术前临床指标构建并内部验证 ATA 中/高危分层列线图。
- Agent note: 列线图方向再添一篇（拥挤）；仅内部验证，外部验证缺失。

**8. [Low] ATF4 and FGFR4 cooperatively support thyroid cancer progression and CAF-associated tumor-promoting features.**
*Endocrine*, 2026-08-15. DOI: `10.1007/s12020-026-04756-8`. PMID: 42603241. OA: hybrid.
- Author claim: ATF4 与 FGFR4 在甲状腺癌细胞中协同促进展，并在 CAF 条件下持续。
- Agent note: 补强 CAF 促瘤生态位（D5）；机制层面呼应代谢–基质耦合。

**9. [Low] Lower invasiveness of papillary thyroid carcinoma associated with Hashimoto's thyroiditis: evidence from AJCC 8th-edition stratification and a dose–response relationship with autoantibody titers.**
*Front. Endocrinol.*, 2026-08-14. DOI: `10.3389/fendo.2026.1897756`. PMID: 待编目. OA: gold.
- Author claim: 266 例 PTC 中 HT 共存者外侵（ETE）更轻，且与自身抗体滴度呈剂量–效应。
- Agent note: 与 #1 互证 HT–LNM/外侵负关联；剂量–效应提升因果暗示强度。

**10. [Low] Artificial Intelligence in Thyroid Nodules and Cancer: Clinical Validation and Real-World Performance.**
*Endocr. Connect.*, 2026-08-13. DOI: `10.1530/ec-26-0415`. PMID: 42593783. OA: gold.
- Author claim: 受邀综述综合 AI 在甲状腺结节风险分层中的临床部署与真实世界验证证据。
- Agent note: 算法拥挤的旁证；提示领域需从「新模型」转向「外部验证/校准」。

**11. [Low] Long-term outcomes of hemithyroidectomy in unexpected hereditary medullary thyroid cancer: a nationwide observational study.**
*BMC Cancer*, 2026-08-18. DOI: `10.1186/s12885-026-16770-0`. PMID: 待编目. OA: gold.
- Author claim: 全国多中心 hMTC 初始半身切除队列长期预后不劣于全切（特定亚群）。
- Agent note: MTC 外科决策证据；与 D6（MTC 5-HT/NETs 肝转移）弱相关。

**12. [Low] CircRNA PVT1 promotes migration, invasion and glucose metabolism of thyroid cancer cells through modulating the miR-195-5p-PDK4 axis.**
*Cytotechnology*, 2026-08-12. DOI: `10.1007/s10616-026-00960-6`. PMID: 42597312. OA: green.
- Author claim: circPVT1 经 miR-195-5p–PDK4 轴促迁移/侵袭与葡萄糖代谢。
- Agent note: 非编码 RNA → 糖代谢–侵袭轴；呼应 D3 代谢支柱（间接）。

**13. [Low] Heme oxygenase−1 in thyroid cancer: a context-dependent regulator.**
*J. Endocrinol. Invest.*, 2026-08-17. DOI: `10.1007/s40618-026-03025-9`. PMID: 42606811. OA: closed.
- Author claim: HO-1 在甲状腺癌中依 context 呈促/抗瘤双向调控（氧化/铁死亡轴）。
- Agent note: 综述；补充代谢重编程（铁死亡/氧化应激）维度。

**14. [Low] ANAPLASTIC THYROID CARCINOMA 10 YEARS FOLLOWING PAPILLARY THYROID CARCINOMA: A CASE REPORT OF MIXED HISTOMORPHOLOGY AND DIAGNOSTIC CHALLENGE.**
*World J. Biol. Pharm. Health Sci.*, 2026-08-13. DOI: `10.30574/wjbphs.2026.27.2.0424`. PMID: 待编目. OA: hybrid.
- Author claim: PTC 经去分化演变为 ATC 的混合组织形态个案（诊断挑战）。
- Agent note: 个案；支持 PTC→ATC 去分化轨迹主题（D3 机制背景）。

**15. [Low] Thyroid Nodules of Uncertain Malignant Potential Non-Conforming to World Health Organization Diagnostic Criteria - Clinicopathologic and Molecular Characterization of 39 Cases.**
*Hum. Pathol.*, 2026-08-01. DOI: `10.1016/j.humpath.2026.106239`. PMID: 待编目. OA: closed.
- Author claim: 39 例不符合 WHO 诊断标准的「不确定恶性潜能结节」临床病理与分子特征。
- Agent note: 边界结节分型；与预后/诊断方向弱相关。

---

## 证据矩阵 / Evidence Matrix（本轮新增 15 篇）

> 列：维度 | 相关性 | 预印本 | OA | 主要发现 | 验证 | 局限 | Gap / 未来方向。PMID 缺失标注「待编目」。

| Paper (first author / year) | PMID/DOI | 维度 | 相关性 | 预印本 | OA | 主要发现 | 验证 | 局限 | Gap / 未来方向 |
|---|---|---|---|---|---|---|---|---|---|
| HT–scRNA–microbiota (2026) | 待编目 / 10.1016/j.isci.2026.117167 | 免疫微环境/单细胞 | High | 否 | gold | HT-PTC 上皮先天免疫富集、瘤内菌多样性↑、LNM↓ | scRNA+16S，无独立队列 | 机制因果未证（观察） | D10：以 HT 为「免疫热/LNM 冷」自然对照 dissect 代谢–免疫转移开关 |
| Microenv. Plasticity & RAI-R (2026) | 待编目 / 10.3390/ijms27167305 | 分子/免疫/干性/代谢 | High | 否 | gold | 去分化/RAI 抵抗由肿瘤–基质互作维持 | 综述（整合多原发） | 非新实验 | 直接验证 D3 前提；需原代空间验证 |
| Immune-escape scRNA sig. (2026) | 42581622 / 10.4196/kjpp.25.445 | 单细胞 | Medium | 否 | gold | AUCell 免疫逃逸活性 + 预后标签 | KM + tROC | 单中心 bulk 验证弱 | D3 免疫组分 / D8 |
| Serum/Tumor PD-L1 (2026) | 42593786 / 10.1001/jamaoto.2026.2200 | 分子/预后 | Medium | 否 | green | 血清+瘤内 PD-L1 关联侵袭特征 | 回顾队列 | 未分层远处/LNM | 延续 PD-L1 元分析（远处 vs LNM 解耦） |
| SAM3 DLR CLNM (2026) | 42586895 / 10.1016/j.acra.2026.07.064 | 算法/预后 | Medium | 否 | hybrid | SAM3 分割 + DL 影像组学预测 PTMC 中央 LNM | 4 中心 1859 例 | 仍单国多中心 | D-ml 拥挤；缺外部国别验证 |
| Recur/Met PTC mut. (2026) | 42605721 / 10.1002/lary.70842 | 预后 | Medium | 否 | hybrid | 348 例复发/转移 PTC NGS top-10 突变 | 日本 C-CAT | 亚洲单族 | DTC 远处 vs LNM 解耦锚点 |
| ATA-risk nomogram (2026) | 待编目 / 10.1186/s12880-026-02702-8 | 预后 | Medium | 否 | gold | 404 例术前 ATA 中/高危列线图 | 仅内部验证 | 无外部验证 | 列线图拥挤 |
| ATF4+FGFR4/CAF (2026) | 42603241 / 10.1007/s12020-026-04756-8 | 分子 | Low | 否 | hybrid | ATF4–FGFR4 协同促进展（CAF 背景） | 敲低 + 异种移植 | 细胞系单一 | D5 CAF 生态位 |
| HT–invasiveness dose–resp. (2026) | 待编目 / 10.3389/fendo.2026.1897756 | 分子/预后 | Low | 否 | gold | HT 共存 PTC 外侵更轻，抗体滴度剂量–效应 | 266 例 | 回顾、单中心 | 与 #1 互证 HT–LNM 负关联 |
| AI clinical validation rev. (2026) | 42593783 / 10.1530/ec-26-0415 | 算法/预后 | Low | 否 | gold | AI 甲状腺结节风险分层临床验证综述 | 综述 | 无新数据 | D-ml 需转向校准/外部验证 |
| hMTC hemithyroidectomy (2026) | 待编目 / 10.1186/s12885-026-16770-0 | 预后 | Low | 否 | gold | hMTC 初始半身切除长期预后（全国） | 多中心观察 | 非随机 | MTC 外科决策 |
| circPVT1–miR195–PDK4 (2026) | 42597312 / 10.1007/s10616-026-00960-6 | 分子 | Low | 否 | green | circPVT1 经 miR-195-5p–PDK4 促糖代谢/侵袭 | 体外 | 缺体内/临床 | D3 代谢支柱（间接） |
| HO-1 context-dep. (2026) | 42606811 / 10.1007/s40618-026-03025-9 | 代谢 | Low | 否 | closed | HO-1 双向调控（铁死亡/氧化） | 综述 | 无新实验 | 代谢重编程 |
| PTC→ATC mixed case (2026) | 待编目 / 10.30574/wjbphs.2026.27.2.0424 | 分子 | Low | 否 | hybrid | PTC 去分化 ATC 混合个案 | 个案 | n=1 | D3 去分化轨迹背景 |
| Nodule uncertain (2026) | 待编目 / 10.1016/j.humpath.2026.106239 | 预后 | Low | 否 | closed | 39 例边界结节分子特征 | 39 例 | 小样本 | 诊断/分型 |

**在范围语料预印本情况：** 本轮 54 篇在范围中合 **3 篇预印本**（均来自历史基线，非本轮新增）；本轮 15 篇新增**全部为正式发表论著，0 预印本**。

---

## 已知结论 / What Is Already Known（稳定收敛，多源支撑）

1. **代谢–免疫耦合驱动 LNM（Axis 1）**：MGST1「Mito-high / 免疫冷」表型（AUC 0.833）、SHMT2、GLTC–LDHA、SOX12–YBX1–LDHA、SMDT1（线粒体 Ca²⁺/MCU）等多条证据一致指向「代谢重编程→免疫微环境冷化→淋巴结转移」轴。本轮 HT-scRNA 研究给出其**表型镜像**——自身免疫（HT）微环境使上皮呈「免疫热」并伴随 LNM↓，进一步坐实「免疫微环境构成决定转移倾向」。
2. **干性/去分化转移亚群（Axis 2）**：APOE−（ABCA1–LXR）、MGST1 去分化尖端、ISG15/KPNA2（ATC）、DLK1（MTC）等指向干样转移亚群；本轮 IJMS 综述明确「去分化由肿瘤–基质互作维持」，强化 APOE−/MGST1+ 亚群的非细胞自主维持机制。
3. **POSTN⁺ myCAF 空间图谱（Axis 3）**：POSTN⁺ 肌成纤维细胞生态位预测 LNM（~423k 细胞图谱）；本轮 ATF4–FGFR4–CAF 研究补充 CAF 促瘤信号。
4. **拥挤的影像/多组学 AI（Axis 4）**：LLNM-Net、CLAM-WSI、融合 DL 等；本轮再添 SAM3-DLR、ATA 列线图、AI 验证综述——**拥挤度持续升高**。
5. **BRAF V600E / PD-L1 元分析（Axis 5）**：BRAF V600E 关联 nodal OR 1.38 / recurrence OR 1.56 但**不**关联远处转移或死亡；PD-L1 元分析镜像一致；本轮血清/瘤内 PD-L1 关联侵袭特征延续该主题。

---

## 未解问题 / What Remains Unclear

- **远处转移 vs LNM 的解耦机制**仍缺直接实验解释（BRAF/PD-L1 均预测远处而非 LNM/复发）。
- **HT「免疫热/LNM 冷」是否因果**：本轮 scRNA+16S 为观察性，菌微生态偏移是驱动还是伴随未明；需菌群移植/体外共培养验证。
- **APOE−/MGST1+ 亚群的原代空间验证与体内靶向**仍为核心缺口（连续多轮未补）。
- **去分化轨迹的定向演化**：PTC→ATC 混合个案与「微环境维持去分化」综述并存，但「何时、何种微环境信号触发不可逆去分化」仍不明。
- **单细胞/空间组学样本偏向 PTC**：ATC、MTC、FTC 亚型与远处转移灶的单细胞/空间覆盖仍薄。

---

## 方法/数据局限 / Method/Data Limitations In The Field

- **公开数据复用 + 批次效应**：单细胞/空间研究多复用 TCGA/GEO，缺独立湿实验验证；商业化空间平台（Visium）分辨率限制细胞类型解析。
- **算法方向外部验证稀缺**：本轮 SAM3-DLR、ATA 列线图均仅内部/单国多中心验证，缺跨国别、跨设备外部验证与校准分析。
- **端点稀疏**：远处转移、复发仍以小样本或短随访为主；LNM 预测模型泛滥但临床净收益（decision curve）少见。
- **检索通道局限**：本机 NCBI eutils/PubMed 不可达，OpenAlex 为主源；预印本（bioRxiv/arXiv）未被主动补检（仅 OpenAlex 自带索引），可能漏检极新预印本。
- **PMID 编目滞后**：近 30 天文献多数「待编目」，以 DOI 为主标识（符合 lit-review 规范，不编造）。

---

## 候选未来方向 / Candidate Future Directions（rubric 1–5 × 7 维，28–35 为 Strong）

| 方向 | 研究问题 | 新颖度 | 可行性 | 数据 | 验证强度 | 临床相关 | 方法严谨 | 拥挤度 | 总分 | 主张边界 |
|---|---|---:|---:|---|---|---|---|---|---:|---|
| **D3** APOE−/MGST1+ 代谢–免疫干性转移亚群 | 定义并靶向该亚群 | 5 | 5 | 5 | 4 | 5 | 4 | 5 | **33** | 强；需原代空间+体内靶向验证 |
| **D8** TREM2⁺ AHR–IDO1 免疫代谢检查点 | 体内逆转免疫冷→热 | 4 | 4 | 4 | 4 | 4 | 4 | 5 | **30** | 强；体内实验已初步 |
| **D9** citrullination/PADI 侵袭程序（SPP1–CD44） | 蛋白citrullination驱动侵袭 | 4 | 4 | 4 | 3 | 4 | 3 | 4 | **28** | 强；需机制+临床锚定 |
| **D6** MTC 5-HT/NETs 肝转移 | 5-HT/NETs 驱动 MTC 肝转移 | 4 | 4 | 3 | 3 | 4 | 3 | 4 | **27** | 可行；fluoxetine/SERT 阻断已提示 |
| — | — | — | — | — | — | — | — | — | — | — |
| **D10（新）** HT 自身免疫微环境作为「LNM 冷」自然对照 | 借 HT-PTC 解析免疫–代谢转移开关 | 4 | 4 | 4 | 3 | 4 | 3 | 4 | **26** | 可行；需因果验证 |
| **D-ml** 算法/影像组学 | — | 1 | 3 | 3 | 2 | 3 | 2 | 1 | **20** | 过度拥挤，不优先 |

> D3 连续第 19 轮确认为 Strong（rubric 33）；D8/D9/D6 维持历史评分。D10 为本轮新增候选（源自 HT-scRNA 新信号）。

---

## 推荐下一步方向 / Recommended Next Direction

**D3 — 定义并靶向 APOE−/MGST1+ 代谢–免疫干性转移亚群（rubric 33, Strong）。**
- **为何**：本轮 IJMS 综述直接论证「去分化/RAI 抵抗由肿瘤–基质互作维持」、HT-scRNA 研究给出其表型镜像（免疫热→LNM 冷），与 MGST1「免疫冷→LNM」构成完整对比，机制与微环境证据链进一步闭合，且无任何反证。
- **所需数据**：TCGA THCA + 机构配对原发–LNM scRNA/空间转录组；MGST1/APOE 蛋白多重免疫荧光；ATC/MTC 远处转移灶样本。
- **首批具体步骤**：① 在已有配对单细胞图谱中分选 APOE−/MGST1+ 亚群并注释代谢–免疫程序；② 多重 IF 在原代组织验证空间共定位；③ 体内（PDX/类器官）靶向该亚群代谢节点（如 LDHA/MGST1）观察 LNM 抑制。
- **验证计划**：独立机构队列 + 体外侵袭/类器官 + 体内转移负荷。
- **主张边界**：在获得原代空间验证与体内靶向证据前，不得宣称「该亚群是 LNM 的充分驱动」。

---

## 随访阅读清单 / Follow-Up Reading List

1. **HT–scRNA–microbiota (iScience, 10.1016/j.isci.2026.117167)** — 开启「HT 免疫热/LNM 冷」机制研究，直接支撑 D10。
2. **Microenvironmental Control of Plasticity & RAI-R (IJMS, 10.3390/ijms27167305)** — D3 机制总纲，必读。
3. **Immune-escape scRNA signature (KJPP, 10.4196/kjpp.25.445)** — D3 免疫组分组装素材。
4. **Serum/Tumor PD-L1 (JAMA Otolaryngol, 10.1001/jamaoto.2026.2200)** — 延续远处 vs LNM 解耦主题。
5. 历史锚点：**MGST1 42327722**、**POSTN⁺ myCAF 41480746**、**BRAF V600E meta 41419184**、**TREM2⁺ AHR–IDO1 42553364**、**citrullination/PADI tranon.2026.102931**。

---

## 零增量维度分析 / Zero-Increment Dimension Analysis

- **维度 h（转移干性）**：30 天窗口增量 **0**（5 条命中均为历史基线已跟踪文献，run #18 亦为 4 篇）。按协议补跑 `--days 90`（中间产物 `search_results_20260821_90day_supplement.json`，189 唯一/141 在范围）：在 2026-05-24~2026-07-21 区间内发现 8 篇带 h 标签文献（含 MGST1 42327722、鳞状去分化、模拟去分化过程等），**均早于本轮 30 天窗口**。
- **结论**：h=0 属**窗口边界效应，非真实缺失**——该维度语料稳定且由 MGST1 等锚点持续支撑；与 run #17/#18 判定一致。不视为平台期。

---

## 本轮 vs 上轮（run #18, 2026-08-14）差异 / Delta vs Run #18

| 指标 | run #18 | run #19 | 变化解读 |
|---|---:|---:|---|
| 唯一记录 | 81 | 81 | 持平（rolling 窗口不同起点） |
| 在范围 | 59 | 54 | −5：Jul15–21 文献随滚动窗口出界（非丢失） |
| 剔除 | 22 | 27 | +5（21 标题未点名 + 6 非肿瘤） |
| **真实新增** | 9 | **15** | **↑活跃度回升**，领域真实活跃（non-plateau） |
| 预印本（在范围） | 4 | 3 | −1（1 篇预印本出界/重分类） |
| High / Med / Low | 13 / 26 / 20 | 11 / 24 / 19 | High −2（窗口老化带出部分 High） |
| 维度 分子机制 | 28 | 28 | 持平 |
| 维度 预后转移 | 39 | 34 | −5（窗口老化） |
| 维度 转移干性 | 3 | 4 | +1 |
| 维度 免疫微环境 | 8 | 7 | −1（窗口老化） |
| 维度 空间组学 | 9 | 7 | −2（窗口老化） |
| 维度 单细胞 | 6 | 6 | 持平 |
| 维度 代谢重编程 | 7 | 8 | +1 |
| 维度 算法方法 | 11 | 9 | −2（窗口老化） |

**新信号/方向变化：**
- **新增最大亮点**：HT 自身免疫微环境→LNM 保护的 scRNA+微生物组机制（#1, High）+ 剂量–效应 Frontiers（#9）——这是 run #1–#18 从未系统出现的**全新角度**，建议升格为候选方向 D10。
- **D3 机制强化**：IJMS 微环境可塑性综述（#2, High）直接验证「干性/去分化由微环境维持」，D3 由「机制假设」迈向「微环境维持」的更稳支撑。
- **算法拥挤再确认**：SAM3-DLR、ATA 列线图、AI 验证综述三连，D-ml（20）维持不优先。
- **Plateau 判定**：否——15 篇真实新增、领域活跃；此前 16 轮零新增已确证为方法学假象（run #16 起）。

---

## 重点方向持续跟踪 / Persistent Direction Tracking — D3 (APOE−/MGST1+)

- **本轮证据对 D3 的影响：定性强化（strengthened）**。
  - 机制层面：IJMS 综述明示去分化/RAI 抵抗由肿瘤–基质互作维持 → 与 APOE−/MGST1+「微环境维持的干性转移亚群」假设一致。
  - 表型层面：HT-scRNA 研究给出「免疫热/LNM 冷」镜像，与 MGST1「免疫冷/LNM 热」构成对比，强化「免疫微环境构成决定转移倾向」这一 D3 上游逻辑。
  - 免疫层面：immune-escape scRNA 标志（#3）补充 D3 免疫组分。
- **机制层面无变化**（仍缺原代空间验证 + 体内靶向）。
- **无反证**。维持 **Strong（rubric 33，连续第 19 轮确认）**。

---

## 可复现性说明 / Reproducibility Notes

- **检索日期 / Search date:** 2026-08-21 (UTC+8)
- **数据库 / Databases:** OpenAlex（主源，直连稳定 ~1.4s）；Crossref + Unpaywall（High/Medium 新文献元数据与 OA 校验，标题/日期全部匹配，无幻影 DOI）
- **查询字符串 / Query strings:** 见上「检索策略」九路 a–i；`filter=title_and_abstract.search:<q>,from_publication_date:2026-07-22`；`sort=publication_date:desc`
- **过滤器 / Filters:** 标题须点名 thyroid/PTC/PTMC/FTC/MTC/ATC 且整体为肿瘤主题；剔除补充材料、同篇多版本、他病/良性甲状腺文献
- **去重规则 / Deduplication:** 标题归一化主键合并（27 组多版本合并）；DOI/PMID 辅助
- **筛选规则 / Screening:** 在范围 = 标题点名甲状腺 ∧ 肿瘤主题
- **零增量补跑:** 维度 h `--days 90`（中间产物 `search_results_20260821_90day_supplement.json`，不覆盖基线）
- **保存文件 / Files saved:**
  - 报告：`lit_review/literature_review_20260821_030000.md`（本文件）
  - 检索结果（带时间戳）：`lit_review/search_results_20260821_030000.json`
  - 基线更新：`lit_review/search_results_latest.json`（已覆盖为 run #19 语料，作下轮锚点）
  - 90 天补跑中间产物：`lit_review/search_results_20260821_90day_supplement.json`
- **环境事实:** 本机 NCBI eutils/PubMed 不可达（HTTP 000），故未直连重试；paper-search-mcp 本轮未启用（主源已充分覆盖，符合「失败即跳过」约定）。
