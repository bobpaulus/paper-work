# 甲状腺癌文献监测报告 / Thyroid Cancer Literature Surveillance Report

Date / 检索日期: 2026-09-11
Sources / 数据源: OpenAlex REST API（主源，直连稳定）; 对 12 条 High/关键 DOI 另发起了 Crossref 元数据 + Unpaywall OA 校验（补充源，异步执行，结果见 `search_results_20260911_enrich.json`）
Search window / 检索窗口: 主窗口 2026-08-12 → 2026-09-11（近 30 天，`from_publication_date`，相对 run #21 累积基线 113 条）；**代谢重编程（ME）维度近 30 天增量 = 0，按协议单独补跑 `--days 90`**（2026-06-13 → 2026-09-11），回补 5 条 ME 新增
Run index / 轮次: #22（相对 run #21 / 2026-09-04 基线，累积基线 113 → 149）
Primary retriever / 主检索器: `oa_search.py`（九路维度 a–i，`sort=publication_date:desc`）

---

## 中文摘要 (Chinese Abstract)

本轮以 OpenAlex 为主源，对甲状腺癌（PTC/PTMC/FTC/MTC/ATC）侵袭、淋巴结（LNM）与远处转移、复发、预后及其分子机制、肿瘤免疫微环境（TIME）、单细胞与空间组学、机器学习/深度学习算法方向执行增量监测。主窗口（近 30 天）去重后唯一记录 **88** 条、甲状腺在范围 **59** 条、相对 run #21 累积基线**新增 31 条**；**代谢重编程（ME）维度 30 天窗口增量 = 0**，按协议放宽至 90 天补跑，回补 **5 条** ME 新增（均为 2026-06-23–2026-07-17 区间、落在 30 天窗口之外、相对基线确为新）。**本轮去重后唯一新增共 36 条**（31 主窗口 + 5 ME 补跑）；在范围预印本按严格 `type` 判定为 **0**，但含 **2 条 Zenodo 仓库型存档**（含关键的 SPP1+ TAM AI 多组学论文）与 **2 条会议摘要**（JCO 增刊 SPP1+ 巨噬细胞、Endocrine Abstracts 免疫细胞因子），按 deposit/abstract 降档处理。

**本轮最强收敛信号：SPP1+ 肿瘤相关巨噬细胞（TAM）轴强势浮现**——同一窗口内出现两篇独立证据：①「AI-driven multi-omics and machine learning identify SPP1+ tumor-associated macrophages as a therapeutic target and predict lymph node metastasis in papillary thyroid cancer」（Zenodo 存档，High，覆盖 AL/PR/IM/SC/SP/ST 六维度，整合 scRNA + 空间转录组 + ML）；②「SPP1⁺ macrophage influence on differentiation of radioiodine-refractory thyroid cancer」（JCO 2026 增刊摘要，High，ME 维度）。两文共同将 **SPP1+ TAM** 定位为 PTC 淋巴结转移预测因子与 RAI 难治性去分化调节者，直接**强化 D9（SPP1–CD44 / SPP1+ TAM 轴，rubric 由 28 升 31）**。

**巨噬细胞/TAM 异质性成为本轮核心主题**：除 SPP1+ TAM 外，另有 UTMD 抑制 CSF-1 驱动巨噬细胞介导铁死亡（PTC）、巨噬细胞介导 Dabrafenib+Trametinib 耐药（ATC）、系统炎症/免疫谱预后（DTC）、免疫细胞因子提升侧颈 LNM 预测——共同把既往 D8（TREM2+ AHR–IDO1）的「髓系免疫抑制」主题拓宽为「TAM 亚群异质性」这一更宽的活跃前沿。

**IL1β/SMDT1-MAPK 轴在 PTC 中呈肿瘤抑制性**（Cancers, High）——SMDT1 正是 run #21 已点名的「代谢–免疫轴」线粒体基因，本轮证据提示其经 MAPK 发挥抑制功能，为 D3 代谢–免疫轴提供**反向/精细化**注脚（非反证，而是功能方向需复核）。

**持续跟踪重点方向状态**：APOE−/MGST1+ 代谢–免疫干性转移亚群（**D3**）——本轮**无变化**（无直接锚定 APOE/MGST1 癌细胞亚群的原发证据）；但 SMDT1 再获数据点，代谢–免疫轴在机制层持续累积。D8（TREM2+ AHR–IDO1）**维持并拓宽**（无 TREM2+ 直接再命中，但 TAM 异质性证据密集）；D11（乳酸化–EMT-TF）**无变化**（本轮无新乳酸化/ETV4/KLF6 论文）。

## English Abstract

This run uses OpenAlex as the primary source for incremental surveillance of thyroid cancer (PTC/PTMC/FTC/MTC/ATC) covering invasion, lymph-node (LNM) and distant metastasis, recurrence, prognosis, molecular mechanisms, tumor immune microenvironment (TIME), single-cell and spatial omics, and ML/DL methods. The 30-day primary window yielded **88 deduplicated records, 59 in thyroid scope, 31 new vs the run #21 cumulative baseline of 113**. The metabolic-reprogramming (**ME**) dimension returned **0 hits in 30 days**; per protocol it was widened to a **90-day supplement** (2026-06-13→2026-09-11) that recovered **5 ME records** (dated 2026-06-23–2026-07-17, outside the 30-day window, hence genuinely new). **36 unique new records this run** (31 + 5). Strict `type`-based preprints = **0**, but there are **2 Zenodo repository deposits** (incl. the key SPP1+ TAM AI multi-omics manuscript) and **2 conference abstracts** (JCO suppl. SPP1+ macrophage; Endocrine Abstracts immune cytokines), down-weighted as deposit/abstract.

**Strongest convergence signal: the SPP1+ tumor-associated macrophage (TAM) axis surges.** Two independent lines of evidence appear in the same window: (i) "AI-driven multi-omics and machine learning identify SPP1+ tumor-associated macrophages as a therapeutic target and predict lymph node metastasis in papillary thyroid cancer" (Zenodo deposit, High, spanning AL/PR/IM/SC/SP/ST, integrating scRNA + spatial + ML); (ii) "SPP1⁺ macrophage influence on differentiation of radioiodine-refractory thyroid cancer" (JCO 2026 suppl., High, ME). Together they position **SPP1+ TAM** as both a PTC LNM predictor and a regulator of RAI-refractory dedifferentiation, directly **strengthening D9 (SPP1–CD44 / SPP1+ TAM axis, rubric 28→31)**.

**Macrophage/TAM heterogeneity is the dominant theme this round**: beyond SPP1+ TAM, we also see UTMD suppressing CSF-1 to drive macrophage-mediated ferroptosis (PTC), macrophage-mediated Dabrafenib+Trametinib resistance (ATC), systemic inflammatory/immune prognostic profiles (DTC), and immune cytokines improving lateral-LNM prediction — collectively broadening the prior D8 (TREM2+ AHR–IDO1) "myeloid immunosuppression" theme into the wider, highly active frontier of **TAM subset heterogeneity**.

**IL1β/SMDT1-MAPK is tumor-suppressive in PTC** (Cancers, High) — SMDT1 being the same mitochondrial gene flagged in run #21's metabolic–immune axis, here framed as MAPK-dependent suppression, a nuanced (not contradictory) refinement of D3.

**Tracked direction status**: APOE−/MGST1+ metabolic–immune stem-like metastatic subpopulation (**D3**) — **unchanged** (no direct primary evidence anchoring APOE/MGST1 cancer-cell subpopulations this run); SMDT1 adds another data point but with a suppressive framing. D8 (TREM2+ AHR–IDO1) — **maintained and broadened** (no direct TREM2+ re-hit, but dense TAM-heterogeneity evidence). D11 (lactylation–EMT-TF) — **unchanged** (no new lactylation/ETV4/KLF6 paper).

---

## 检索策略 (Search Strategy)

主源 OpenAlex（`api.openalex.org/works`），九路维度检索，过滤器 `title_and_abstract.search:<q>,from_publication_date:<date>`，`sort=publication_date:desc`，每路 `per-page=25`。维度代码：MO=分子机制 / IM=免疫微环境 / SC=单细胞 / SP=空间组学 / AL=算法方法 / PR=预后转移 / ST=转移干性 / ME=代谢重编程。

| 路 | 维度 | 窗口 | OpenAlex 命中 | 取回 | 新条目 | 状态 |
|---|---|---|---:|---:|---:|---|
| a | MO/PR | 30d | 20 | 20 | 19 | OK |
| b | MO | 30d | 42 | 25 | 17 | OK |
| c | AL/PR | 30d | 10 | 10 | 6 | OK |
| d | IM | 30d | 30 | 25 | 11 | OK |
| e | SC | 30d | 13 | 13 | 8 | OK |
| f | SP | 30d | 8 | 8 | 2 | OK |
| g | PR | 30d | 47 | 25 | 16 | OK |
| h | ST | 30d | 10 | 10 | 4 | OK |
| i | ME | 30d | 7 | 7 | **0** | **0→补跑 90d** |
| i | ME | **90d** | 19 | 19 | 5 | 维度 0 放宽补跑 |

补充源约定：`paper-search-mcp` 本轮**未调用**——本机 NCBI eutils / pubmed.ncbi.nlm.nih.gov 实测仍不可达（HTTP 000），MCP 频繁 `not well-formed` 截断，按"失败即跳过、绝不阻塞主流程"处理。对 12 条 High/关键 DOI 经 Crossref 校验元数据、Unpaywall 解析 OA 状态（补充源，异步执行；主 OA 状态以 OpenAlex 内建 `oa_status` 为准）。

窗口边沿处理：维度 i（代谢重编程）30 天增量 = 0 → 按协议单独补跑 `--days 90`（中间产物 `search_results_20260911_90day_supplement.json`，不覆盖基线）。补跑确认 ME 维度并非领域停滞，而是 **30 天严格窗口对低频高分维度的欠采样**——90 天窗口命中 19、在范围 5，且含 SPP1+ 巨噬细胞（JCO）、HIF-1α/ACSL 铁死亡抵抗（ATC）等机制文献。这与 run #20 空间组学、run #21 单细胞"30 天=0 → 90 天补跑"同构，再次印证**对稀疏高分维度应默认 90 天窗口**。

---

## 纳入论文 (Included Papers)

> 本轮 36 条相对 run #21 基线新增文献。标注：★ = 30 天主窗口新增（≥2026-08-12）；▲ = 代谢重编程 90 天补跑新增（2026-06-23–2026-07-17）；[deposit] = Zenodo 仓库型存档（非同行评议论著）；[abstract] = 会议摘要（初步证据）。

**30 天主窗口（31 条，★）**

1. ★ **IL1β Functions as a Tumor Suppressor in Papillary Thyroid Carcinoma via the SMDT1-MAPK Signaling Axis.** *Cancers* 2026-09-09. DOI:10.3390/cancers18182918. 中文要点：IL1β 经 SMDT1–MAPK 轴在 PTC 中发挥肿瘤抑制功能（与既往"代谢–免疫促转移轴"形成功能方向性对照）。
2. ★ **A clinical nomogram for evaluating occult central lymph node metastasis in clinically low-risk, unifocal papillary thyroid microcarcinoma.** *Front Endocrinol* 2026-09-09. DOI:10.3389/fendo.2026.1853172. 中文要点：低危单发 PTMC 隐匿中央区 LNM 列线图（回顾性、内部验证）。
3. ★ **[¹⁸F] FDG PET/CT in Differentiating Nodal Follicular Helper T-cell Lymphoma … from Postoperative Metastatic Thyroid Carcinoma.** *Nucl Med Mol Imaging* 2026-09-09. DOI:10.1007/s13139-026-01066-9. 中文要点：FDG PET/CT 鉴别淋巴结滤泡辅助 T 细胞淋巴瘤与术后转移 TC（鉴别诊断价值）。
4. ★ **Network based approach identifies miR‑145‑3p as a central regulatory hub associated to the progression from localized to metastatic medullary thyroid carcinoma.** *J Pathol* 2026-09-09. PMID:42713718. DOI:10.1002/path.70116. 中文要点：网络分析锁定 miR-145-3p 为 MTC 局限→转移进展的核心调控枢纽（D6 部分支撑）。
5. ★ **TERT Reactivation in Thyroid Cancer: Mechanisms, Clinical Implications, and Therapeutic Opportunities.** *Eur Thyroid J* 2026-09-09. DOI:10.1530/etj-26-0068. 中文要点：TERT 启动子重激活机制与临床/治疗意义综述（TERT 为预后锚点共识）。
6. ★ **Contemporary management of differentiated thyroid cancer in Latin America: results from the CaTaLiNA prospective multicenter registry.** *Endocrine* 2026-09-09. DOI:10.1007/s12020-026-04760-y. 中文要点：拉美 DTC 真实世界管理登记（外推价值有限）。
7. ★ **Editorial Comment: Recurrence in Papillary Thyroid Carcinoma Based on Risk Stratification.** *Ann Surg Oncol* 2026-09-09. DOI:10.1245/s10434-026-20539-x. 中文要点：PTC 基于风险分层的复发述评（非实证）。
8. ★ **The TIF-1γ autoantigen in patients with dermatomyositis and thyroid cancer: from case series to preliminary mechanistic exploration.** *Front Immunol* 2026-09-08. DOI:10.3389/fimmu.2026.1817558. 中文要点：皮肌炎相关 TIF-1γ 自身抗原与 TC 关联（含孟德尔随机化探索）。
9. ★ **Identifying the therapeutic effects of talniflumate in metastatic papillary thyroid microcarcinoma through integrating multiple omics analysis.** *Naunyn-Schmiedeberg's Arch Pharmacol* 2026-09-08. PMID:42709185. DOI:10.1007/s00210-026-05854-0. 中文要点：多组学整合提示 talniflumate（抗炎药）对转移 PTMC 的治疗潜力。
10. ★ **Reproducibility archive for TLS-like spatial transcriptional organization in papillary thyroid carcinoma.** [deposit] *Zenodo* 2026-09-08. DOI:10.5281/zenodo.22661715. 中文要点：PTC 中 TLS（三级淋巴样结构）样空间转录组组织的可复现性存档（分析脚本+结果）。
11. ★ **Distinct molecular profiles of indeterminate and malignant thyroid nodules in patients under 21 years of age.** *Endocr Relat Cancer* 2026-09-07. PMID:42704707. DOI:10.1530/erc-26-0115. 中文要点：<21 岁患者不确定/恶性结节的差异化分子谱（Afirma GSC 大数据）。
12. ★ **Dickkopf-1 (DKK1) controls papillary and follicular thyroid cancer growth.** *Endocr Relat Cancer* 2026-09-07. PMID:42704709. DOI:10.1530/erc-26-0026. 中文要点：Wnt 拮抗物 DKK1 调控 PTC/FTC 生长（增殖机制）。
13. ★ **Thyroid Cancer in the Modern Era: From Molecular Landscape and Multimodal Diagnostics to Integrative Traditional Chinese Medicine—A Comprehensive Review.** *Cancer Manag Res* 2026-09-05. DOI:10.2147/cmar.s635801. 中文要点：TC 分子景观+多模态诊断+整合 TCM 综述（High 相关性但非原发）。
14. ★ **Prognostic significance of systemic inflammatory and peripheral immune profiles in differentiated thyroid carcinoma: a retrospective cohort study.** *BMC Cancer* 2026-09-04. DOI:10.1186/s12885-026-16883-6. 中文要点：系统炎症/外周免疫谱（NLR、淋巴细胞亚群等）对 DTC 预后的补充价值（High，免疫预后）。
15. ★ **Multiomics analyses identify diet-derived creatine and α-linolenic acid linking with metastatic thyroid cancer.** *Mol Cell Probes* 2026-09-04. PMID:42697284. DOI:10.1016/j.mcp.2026.102086. 中文要点：血清代谢组+肠道菌群多组学锁定饮食来源肌酸与 α-亚麻酸与 TC 转移关联（代谢–转移轴）。
16. ★ **AI-driven multi-omics and machine learning identify SPP1+ tumor-associated macrophages as a therapeutic target and predict lymph node metastasis in papillary thyroid cancer.** [deposit] *Zenodo* 2026-09-04. DOI:10.5281/zenodo.22290057. 中文要点：整合 scRNA + 空间转录组 + ML，鉴定 SPP1+ TAM 为 PTC LNM 预测因子与治疗靶点（★本轮最关键，D9 直接证据）。
17. ★ **Predicting unfavorable response to initial radioactive iodine therapy in differentiated thyroid cancer: an explainable machine learning and survival analysis approach.** *Front Endocrinol* 2026-09-04. DOI:10.3389/fendo.2026.1943597. 中文要点：可解释 ML 预测 DTC 初始 RAI 治疗不良应答（内部验证）。
18. ★ **The tumor immune microenvironment of thyroid cancer and colorectal cancer: cellular crosstalk and therapeutic implications.** *Front Immunol* 2026-09-04. DOI:10.3389/fimmu.2026.1916192. 中文要点：TC 与结直肠癌 TIME 细胞互作与治疗的跨癌种比较（High，SC/SP）。
19. ★ **68Ga-FAPI-04 PET/CT has high diagnostic efficacy in Tg-positive and Tg-negative differentiated thyroid cancer.** *PLoS ONE* 2026-09-03. PMID:42691023. DOI:10.1371/journal.pone.0355343. 中文要点：68Ga-FAPI-04 PET/CT 在 Tg 阳/阴性 DTC 复发转移诊断中的高效能。
20. ★ **SYTL5 drives malignant progression in differentiated thyroid carcinoma: unveiling its regulatory mechanisms.** *Front Oncol* 2026-09-03. DOI:10.3389/fonc.2026.1810543. 中文要点：SYTL5 经调控机制驱动 DTC 恶性进展（IHC+qPCR+WB）。
21. ★ **TWO-STAGE RECONSTRUCTION OF A FEMORAL METASTASIS FROM PAPILLARY THYROID CARCINOMA USING A CEMENT SPACER AND STRUCTURAL FIBULAR AUTOGRAFT: A CASE REPORT.** *World J Adv Res Rev* 2026-09-03. DOI:10.30574/wjarr.2026.31.3.2260. 中文要点：PTC 股骨干转移两步重建个案（骨转移外科）。
22. ★ **Papillary thyroid carcinoma under the WHO 2022 framework: subtype distribution, preoperative correlates and pathological associates of extrathyroidal extension and nodal metastasis.** *Diagn Pathol* 2026-09-03. DOI:10.1186/s13000-026-01851-2. 中文要点：南印 PTC 队列按 WHO 2022 重新分型，ETE/淋巴结转移病理关联。
23. ★ **Targeting MAPK Pathways in Skin, Thyroid, and Pancreatic Cancer: A Perspective on Synthetic Inhibitors and Natural Modulators.** *Adv Biol* 2026-09-01. PMID:42708305. DOI:10.1002/adbi.70156. 中文要点：MAPK 通路合成抑制剂与天然调节物综述（含甲状腺）。
24. ★ **UTMD Suppresses CSF‑1 to Drive Macrophage‑Mediated Ferroptosis in Papillary Thyroid Carcinoma.** *Cancer Med* 2026-08-27. PMID:42656085. DOI:10.1002/cam4.72220. 中文要点：超声靶向微泡破坏（UTMD）抑制 CSF-1，重编程 TAM 并诱导铁死亡（TAM+铁死亡轴）。
25. ★ **Macrophages as Drivers of Resistance to Dabrafenib Plus Trametinib Therapy in Anaplastic Thyroid Cancer.** *Int J Mol Sci* 2026-08-27. DOI:10.3390/ijms27177691. 中文要点：巨噬细胞（经 SPRY4）驱动 ATC 对 Dabrafenib+Trametinib 耐药（髓系–靶向耐药）。
26. ★ **Immune cytokines improve prediction of lateral lymph node metastasis in papillary thyroid cancer.** [abstract] *Endocrine Abstracts* 2026-08-27. DOI:10.1530/endoabs.119.ps2-09-07. 中文要点：免疫细胞因子提升 PTC 侧颈 LNM 预测（会议摘要，初步）。
27. ★ **Less is more? Evaluating the role of radioiodine therapy in pediatric differentiated thyroid cancer management.** *Ann Pediatr Endocrinol Metab* 2026-08-27. PMID:42655994. DOI:10.6065/apem.2652220.110. 中文要点：儿童 DTC RAI 治疗"少即是多"再评估（低危儿童获益有限）。
28. ★ **Clinical presentation, management and outcomes of differentiated thyroid cancer: a tertiary center experience.** *Egypt J Otolaryngol* 2026-08-27. DOI:10.1186/s43163-026-01202-4. 中文要点：三级中心 DTC 临床结局回顾（异质性高）。
29. ★ **Aberrant membranous localization of cleaved caspase-3 in anaplastic thyroid carcinoma: Implications for cell proliferation and stemness.** *Histochem Cell Biol* 2026-08-27. PMID:42658275. DOI:10.1007/s00418-026-02530-5. 中文要点：ATC 中切割 caspase-3 膜定位异常与增殖/干性（ST 维度）。
30. ★ **Diagnostic and management in a rare case of double primary carcinoma: metastatic papillary thyroid cancer coexisting with TTF-1/p40 co-expressing non-small cell lung cancer.** *Discov Oncol* 2026-08-26. DOI:10.1007/s12672-026-05830-3. 中文要点：转移性 PTC 合并 NSCLC 双原发罕见例（鉴别诊断）。
31. ★ **Development and validation of an ultrasound-based deep learning radiomics nomogram for risk assessment of lymph node metastasis in papillary thyroid microcarcinoma.** *Quant Imaging Med Surg* 2026-08-24. PMID:42701453. DOI:10.21037/qims-2026-1-0135. 中文要点：多中心超声 DL 影像组学列线图评估 PTMC LNM 风险（D-ml，仍单/多中心内部验证）。

**代谢重编程 90 天补跑（5 条，▲）**

32. ▲ **Associations between postoperative serum omics-derived proteins and aggressive clinicopathologic features in thyroid cancer.** *Sci Rep* 2026-07-17. DOI:10.1038/s41598-026-63023-y. 中文要点：术后血清蛋白组与 TC 侵袭性临床病理特征关联。
33. ▲ **Pin1 targets phosphorylated NCOA4 for K29/K48-linked ubiquitination to suppress ferritinophagy.** *Cell Death Dis* 2026-07-01. DOI:10.1038/s41419-026-09058-5. 中文要点：Pin1 经泛素化 NCOA4 抑制铁蛋白自噬（ferritinophagy），影响 TC（铁死亡上游）。
34. ▲ **MMRN1 suppresses thyroid cancer progression via activation of the Hippo signaling pathway.** *Endocrine* 2026-06-30. DOI:10.1080/07435800.2026.2694492. 中文要点：MMRN1 经激活 Hippo 信号抑制 TC 进展（增殖/转移）。
35. ▲ **HIF-1α enhances ferroptosis resistance in anaplastic thyroid carcinoma by suppressing ACSL.** *Cancer Cell Int* 2026-06-27. DOI:10.1186/s11658-026-00973-1. 中文要点：HIF-1α 抑制 ACSL 增强 ATC 铁死亡抵抗（铁死亡–ATC 轴，与 [24] 呼应）。
36. ▲ **SPP1⁺ macrophage influence on differentiation of radioiodine-refractory thyroid cancer.** [abstract] *J Clin Oncol* 2026 44(19) suppl. 2026-06-23. DOI:10.1200/jco.2026.44.19_suppl.239. 中文要点：SPP1+ 巨噬细胞影响 RAI 难治性 TC 的去分化（★D9 第二独立证据，JCO 增刊摘要）。

---

## 证据矩阵 (Evidence Matrix)

> 列：维度 / 相关性 / 预印本·存档 / OA / 疾病人群 / 数据源 / 方法 / 终点 / 主要发现 / 验证 / 局限 / 缺口 / 后续方向。相关性 High/Med/Low；OA: gold/diamond/hybrid/green/bronze/closed。

| 论文 (Paper) | 维度 | 相关性 | 存档 | OA | 疾病/人群 | 数据源 | 方法 | 终点 | 主要发现 | 验证 | 局限 | 缺口 | 后续方向 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| IL1β/SMDT1-MAPK 抑制 PTC (10.3390/cancers18182918) | MO/PR | High | 否 | gold | PTC | 细胞+临床 | 功能+生存 | 抑制/进展 | IL1β 经 SMDT1–MAPK 抑制 PTC | 体外+临床 | 因果链浅 | 体内 LNM | SMDT1 功能方向复核 (D3) |
| 隐匿 CLNM 列线图 PTMC (10.3389/fendo.2026.1853172) | AL/PR | Med | 否 | gold | 低危 PTMC | 回顾队列 | 列线图 | CLNM | 低危 PTMC 隐匿 CLNM 风险模型 | 内部 | 单中心 | 外部 | 多中心 LNM 模型 |
| FDG PET 鉴别淋巴瘤/转移 TC (10.1007/s13139-026-01066-9) | IM | Low | 否 | closed | 淋巴结病变 | 影像 | PET/CT | 鉴别 | FDG 鉴别转移 TC 与淋巴瘤 | 影像 | 非机制 | — | 影像鉴别 |
| miR-145-3p MTC 转移枢纽 (10.1002/path.70116) | PR | Med | 否 | hybrid | MTC | 网络+临床 | 网络分析 | 局限→转移 | miR-145-3p 为 MTC 转移核心枢纽 | 生信+部分 | 机制浅 | 功能 | MTC 转移机制 (D6) |
| TERT 重激活综述 (10.1530/etj-26-0068) | PR | Med | 否 | hybrid | TC | 综述 | 综述 | 预后/治疗 | TERT 重激活机制与意义 | 综述 | 非原发 | — | TERT 靶向 |
| CaTaLiNA 拉美 DTC (10.1007/s12020-026-04760-y) | PR | Low | 否 | closed | DTC | 多中心登记 | 真实世界 | 管理 | 拉美 DTC 管理现状 | 登记 | 外推有限 | — | 真实世界 |
| PTC 复发述评 (10.1245/s10434-026-20539-x) | PR | Low | 否 | closed | PTC | 述评 | 述评 | 复发 | 风险分层复发述评 | 述评 | 非实证 | — | 复发模型 |
| TIF-1γ 皮肌炎+TC (10.3389/fimmu.2026.1817558) | MO | Med | 否 | gold | DM+TC | 病例+MR | 孟德尔随机 | 关联 | TIF-1γ 关联 DM 与 TC | 病例+MR | 机制初探 | 功能 | 自身抗原机制 |
| talniflumate 转移 PTMC 多组学 (10.1007/s00210-026-05854-0) | MO/IM/SC | Med | 否 | closed | PTMC | 多组学 | 整合 | 治疗 | talniflumate 治疗转移 PTMC 潜力 | 多组学 | 湿实缺 | 体内 | 抗炎药重定位 |
| TLS 样空间存档 PTC [deposit] (10.5281/zenodo.22661715) | SP | Med | 是 | green | PTC | scRNA+空间 | 存档 | 空间 | TLS 样空间转录组可复现存档 | 数据 | 非论著 | 功能 | TLS 空间生态位 |
| <21 岁结节分子谱 (10.1530/erc-26-0115) | MO/PR | Med | 否 | hybrid | <21y 结节 | Afirma GSC | 大数据 | 分子分型 | 年轻患者差异化分子谱 | 大样本 | 回顾 | 独立 | 年轻 TC 机制 |
| DKK1 调控 PTC/FTC (10.1530/erc-26-0026) | MO/PR | Med | 否 | closed | PTC/FTC | 细胞+动物 | Wnt | 生长 | DKK1 调控 PTC/FTC 生长 | 体外+体内 | 临床弱 | 队列 | Wnt 靶向 |
| TCM 整合综述 (10.2147/cmar.s635801) | MO/IM | Med | 否 | green | TC | 综述 | 综述 | 机制 | 分子+多模态+TCM 综述 | 综述 | 非原发 | 验证 | TCM 机制 |
| 系统炎症/免疫谱 DTC (10.1186/s12885-026-16883-6) | MO/PR/IM | High | 否 | gold | DTC | 回顾队列 | 免疫谱 | 预后 | 炎症/免疫谱补充 DTC 预后 | 队列 | 回顾 | 前瞻 | 免疫预后模型 |
| 饮食肌酸/α-亚麻酸 转移 (10.1016/j.mcp.2026.102086) | MO/ME | Med | 否 | closed | TC | 代谢组+菌群 | 多组学 | 转移 | 肌酸/α-亚麻酸关联 TC 转移 | 多组学 | 因果浅 | 机制 | 饮食-代谢-转移 (D9/ME) |
| SPP1+ TAM AI 多组学 [deposit] (10.5281/zenodo.22290057) | AL/PR/IM/SC/SP/ST | High | 是 | green | PTC | scRNA+空间+ML | 多组学+ML | LNM/靶点 | SPP1+ TAM 为 LNM 预测+治疗靶点 | 多组学 | 存档未评议 | 体内 | **D9 强化** |
| 可解释 ML RAI 不良应答 (10.3389/fendo.2026.1943597) | AL/PR | Med | 否 | gold | DTC | 临床+RAI | 可解释 ML | RAI 应答 | 预测 DTC RAI 不良应答 | 内部 | 单中心 | 外部 | RAI 应答模型 |
| TC vs 结直肠癌 TIME (10.3389/fimmu.2026.1916192) | SC/SP | High | 否 | gold | TC/CRC | 综述+比较 | 跨癌种 | 免疫 | TC 与 CRC TIME 互作比较 | 综述 | 非原发 | — | 跨癌种免疫 |
| 68Ga-FAPI-04 PET/CT DTC (10.1371/journal.pone.0355343) | MO/PR | Med | 否 | gold | DTC | 影像 | PET/CT | 复发/转移 | FAPI PET 高诊断效能（Tg 阴阳性） | 队列 | 单中心 | 多中心 | 影像诊断 |
| SYTL5 DTC 进展 (10.3389/fonc.2026.1810543) | MO | Med | 否 | gold | DTC | IHC+qPCR+WB | 机制 | 进展 | SYTL5 驱动 DTC 恶性进展 | 体外 | 体内弱 | 靶向 | SYTL5 机制 |
| 股骨干转移 PTC 重建 (10.30574/wjarr.2026.31.3.2260) | PR | Med | 否 | closed | PTC 骨转移 | 个案 | 外科 | 骨转移 | 两步重建个案 | 个案 | n=1 | 队列 | 骨转移外科 |
| WHO 2022 PTC 分型 (10.1186/s13000-026-01851-2) | PR | Med | 否 | gold | PTC | 队列 | 病理分型 | ETE/LNM | WHO 2022 亚型与 ETE/LNM 关联 | 队列 | 单中心 | 多中心 | 亚型预后 |
| MAPK 综述 (10.1002/adbi.70156) | MO | Low | 否 | bronze | 多癌 | 综述 | 综述 | 靶向 | MAPK 合成/天然抑制剂综述 | 综述 | 非原发 | — | MAPK 靶向 |
| UTMD-CSF1 铁死亡 PTC (10.1002/cam4.72220) | MO/IM | Med | 否 | gold | PTC | 转录组 | 物理+功能 | 铁死亡 | UTMD 抑 CSF-1 重编程 TAM 诱导铁死亡 | 体外+部分 | 体内浅 | 临床 | TAM 铁死亡 (D8/铁死亡) |
| 巨噬细胞驱动 DT 耐药 ATC (10.3390/ijms27177691) | MO/IM | Low | 否 | gold | ATC | 细胞+条件 | 耐药 | 靶向耐药 | 巨噬细胞经 SPRY4 驱动 DT 耐药 | 体外 | 临床弱 | 体内 | 髓系–靶向耐药 |
| 免疫细胞因子 侧颈 LNM [abstract] (10.1530/endoabs.119.ps2-09-07) | IM | Med | 是 | — | PTC | 摘要 | 队列 | LLNM | 免疫细胞因子提升侧颈 LNM 预测 | 摘要 | 初步 | 全文 | 免疫 LNM 模型 |
| 儿童 DTC RAI (10.6065/apem.2652220.110) | PR | Med | 否 | diamond | 儿童 DTC | 综述/登记 | 述评 | RAI | 低危儿童 RAI 获益有限 | 综述 | 非实证 | 前瞻 | 儿童 RAI 降级 |
| 三级中心 DTC 结局 (10.1186/s43163-026-01202-4) | PR | Med | 否 | diamond | DTC | 回顾 | 结局 | 生存 | DTC 临床结局回顾 | 回顾 | 异质 | 多中心 | 结局模型 |
| caspase-3 膜定位 ATC (10.1007/s00418-026-02530-5) | ST | Low | 否 | closed | ATC | 组织 | 免疫组化 | 干性 | 切割 caspase-3 膜定位异常关联增殖/干性 | 组织 | 机制浅 | 功能 | ATC 干性 |
| 双原发 PTC+NSCLC (10.1007/s12672-026-05830-3) | MO/PR | Low | 否 | hybrid | 双原发 | 个案 | 鉴别 | 诊断 | PTC 合并 NSCLC 双原发鉴别 | 个案 | n=1 | — | 鉴别诊断 |
| 超声 DL 影像组学 LNM (10.21037/qims-2026-1-0135) | AL/PR | Med | 否 | diamond | PTMC | 多中心超声 | DL 影像组学 | LNM | 超声 DL 影像组学 LNM 风险 | 多中心 | 内部验证 | 外部 | 影像 LNM (D-ml) |
| 术后血清蛋白组 侵袭 [▲] (10.1038/s41598-026-63023-y) | ME | Low | 否 | gold | TC | 血清蛋白组 | 蛋白组 | 侵袭 | 血清蛋白与侵袭特征关联 | 队列 | 因果浅 | 机制 | 血清蛋白标志物 |
| Pin1/NCOA4 铁蛋白自噬 [▲] (10.1038/s41419-026-09058-5) | ME | Low | 否 | gold | TC | 细胞 | 泛素化 | 铁死亡上游 | Pin1 抑 NCOA4 铁蛋白自噬 | 体外 | 体内弱 | 在体 | 铁死亡上游 |
| MMRN1 Hippo 抑制 TC [▲] (10.1080/07435800.2026.2694492) | ME | Low | 否 | hybrid | TC | 细胞+动物 | Hippo | 进展 | MMRN1 经 Hippo 抑 TC 进展 | 体外+体内 | 临床弱 | 队列 | Hippo 靶向 |
| HIF-1α/ACSL 铁死亡抵抗 ATC [▲] (10.1186/s11658-026-00973-1) | ME | Med | 否 | gold | ATC | 细胞 | 铁死亡 | 耐药 | HIF-1α 抑 ACSL 增强 ATC 铁死亡抵抗 | 体外 | 体内浅 | 在体 | 铁死亡–ATC (D12) |
| SPP1+ 巨噬细胞 RAI 难治 [▲][abstract] (10.1200/jco.2026.44.19_suppl.239) | ME/IM | High | 是 | — | RAI 难治 TC | 摘要 | 机制 | 去分化 | SPP1+ 巨噬细胞影响 RAI 难治去分化 | 摘要 | 初步 | 全文/体内 | **D9 第二证据** |

---

## 已知结论 (What Is Already Known)

> 下列为跨 run #16–#21 稳定收敛、且被本轮证据相容（未反证）的结论；本轮新文献均不与之冲突，并在若干处强化或精细化。

1. **代谢–免疫耦合驱动 LNM（核心轴 1）**：MGST1 "Mito-high"/免疫冷亚型、SHMT2、GLTC-LDHA、SOX12-YBX1-LDHA、SMDT1（run #21 点名）指向「代谢重编程→免疫抑制→淋巴结转移」。本轮 **IL1β/SMDT1-MAPK 肿瘤抑制性**（原发表，High）、**饮食肌酸/α-亚麻酸多组学转移关联**、**HIF-1α/ACSL 铁死亡抵抗（ATC）**、**Pin1/NCOA4 铁蛋白自噬**、**MMRN1 Hippo**、**术后血清蛋白组** 六线并发，将代谢轴从「基因亚型」推向「代谢物/修饰/铁死亡上游/营养」多层。
2. **干性样转移亚群（核心轴 2 / D3）**：APOE−/MGST1+ 代谢–免疫干性亚群、ISG15/KPNA2（ATC）、DLK1（MTC）。本轮**无直接锚定 APOE/MGST1 癌细胞亚群的原发证据**；但 SMDT1 再获数据点（功能方向为抑制性，需与既往"促转移"表述复核），轴在机制层持续累积。
3. **POSTN+ myCAF 空间图谱（核心轴 3）**：POSTN+ CAF 空间图谱预测 LNM（run #20 KLF6 给出 EPC→CAF 序列）。本轮 TLS 样空间存档（[deposit]）为 PTC 三级淋巴样结构空间生态位提供可复现数据基底。
4. **影像/多组学 AI 拥挤（核心轴 4）**：本轮新增 1 个超声 DL 影像组学列线图（多中心但仍内部验证）+ 2 个列线图/可解释 ML（RAI 应答、隐匿 CLNM）。再次确认该方向增量价值低、外部泛化未解。
5. **BRAF/TERT 预后锚点（核心轴 5）**：本轮 TERT 重激活综述、WHO 2022 分型、多份预后/管理文献相容「TERT/BRAF 为预后锚点」共识，无反证。
6. **★ 新确认（本轮强势浮现）— SPP1+ TAM 轴（D9）**：SPP1+ TAM 在 PTC 中被 AI 多组学+ML 鉴定为 LNM 预测因子与治疗靶点，并在 RAI 难治 TC 中被 SPP1+ 巨噬细胞调控去分化（JCO 摘要）。这是既往 run #21 仅以 CD44 间接关联的 **SPP1–CD44 轴的 direct 升级**，本轮**直接强化 D9**。
7. **巨噬细胞/TAM 异质性成为活跃前沿（D8 拓宽）**：UTMD-CSF1-铁死亡、DT 耐药（ATC）、系统炎症/免疫谱、免疫细胞因子 LNM 共同把「髓系免疫抑制」主题从 TREM2+ 单一亚群拓宽为 TAM 亚群异质性全景。

---

## 未解问题 (What Remains Unclear)

- **D3 癌细胞亚群的原代空间验证与体内靶向仍空缺**：APOE−/MGST1+ 代谢–免疫干性转移亚群虽多轮被推荐，仍缺原代组织空间验证 + 体内靶向干预证据（本轮未补）。IL1β/SMDT1-MAPK 的"抑制性"走向与既往"代谢–免疫促转移"表述需机制层调和，不可直接外推为同一方向。
- **SPP1+ TAM 的临床转化与机制缺口（本轮重点）**：两篇 SPP1+ TAM 证据中，Zenodo 项为**仓库存档（未同行评议）**、JCO 项为**会议摘要（初步）**——均属降档证据，需正式发表全文 + 独立队列验证 SPP1+ TAM 丰度与 LNM/RAI 抵抗/生存的真实关联，及其与 TREM2+ 亚群的层级关系。
- **铁死亡轴的因果未闭合**：UTMD-CSF1 铁死亡（PTC）、HIF-1α/ACSL 铁死亡抵抗（ATC）均为体外证据，缺体内 LNM/RAI 模型与铁死亡诱导剂的在体疗效。
- **代谢机制深度不足**：饮食肌酸/α-亚麻酸、Pin1/NCOA4、MMRN1 Hippo 多为关联/上游机制，促转移因果链未闭合。
- **算法模型外部泛化**：本轮 3 个 LNM/RAI 模型仍单/多中心内部验证，跨人群/跨设备漂移未评估。
- **TLS 空间生态位功能空白**：TLS 样空间存档仅提供可复现数据，TLS 与 LNM/免疫应答的功能因果未阐明。

---

## 领域方法/数据局限 (Method/Data Limitations In The Field)

- **30 天严格窗口对低频高分维度欠采样（再次证实）**：代谢重编程维度 30 天命中 0，但 90 天补跑命中 19、在范围 5 且含 SPP1+ 巨噬细胞（JCO）、HIF-1α/ACSL 铁死亡（ATC）等最高价值文献——**滚动短窗口系统性漏掉稀疏高分维度**。强烈建议对 ME/SC/SP 等稀疏维度默认 90 天窗口（或全维度统一 90 天 + DOI 去重）。这与 run #20 空间组学、run #21 单细胞同构。
- **PubMed 编目滞后**：本轮 36 篇中多数无 PMID（仅 9 篇有 PMID：42713718/42704707/42704709/42697284/42691023/42709185/42708305/42656085/42655994/42658275/42701453——实为 11 篇），以 DOI 为主标识，符合 skill 规范。
- **单细胞/空间组学稀疏但非停滞**：本轮 SC 新 3、SP 新 3（主窗口），ATC/MTC 亚型与远处转移空间证据仍薄；TLS 存档与 SPP1+ TAM 多组学为空间/SC 注入新料。
- **预印本/仓库/摘要降档**：2 条 Zenodo 仓库型存档（含关键 SPP1+ TAM 论文，`type=dataset`）、2 条会议摘要（JCO SPP1+、Endocrine Abstracts 免疫细胞因子）按规范降档，证据强度受限。
- **综述占比偏高**：本轮 High/Med 条目中 TCM 综述、TERT 综述、TC vs CRC TIME 综述、MAPK 综述、复发述评为非原发证据，应与原发机制论文区分权重。
- **伪新增消减验证**：基线已为累积语料（113→149），本轮 36 条均为相对累积基线真实新增、无截断回填（延续 run #21 已规避的滚动窗口伪新增问题）。

---

## 候选未来方向 (Candidate Future Directions)

> 评分按 research-direction-rubric.md 七维（Novelty/Feasibility/Data/Validation/Clinical/Method/Overcrowding，各 1–5，满分 35）。28–35 = Strong。本轮更新：D9 由 28 升 **31**（SPP1+ TAM 双证据）；新增 D12 铁死亡（探索级 ~27）。

| 方向 | 七维小计 | 评级 | 一句话依据 |
|---|---:|---|---|
| **D3** APOE−/MGST1+ 代谢–免疫干性转移亚群 | **33** | Strong | 连续 22 轮确认，本轮无反证；SMDT1 再获数据点（抑制性走向需调和） |
| **D8** TREM2+ AHR–IDO1 免疫代谢检查点 | **32** | Strong（维持并拓宽） | 无 TREM2+ 直接再命中，但 TAM 异质性证据密集（SPP1+/CSF1/铁死亡/耐药） |
| **D9（↑）** SPP1–CD44 / SPP1+ TAM 轴 | **31** | Strong（由 28 升） | 本轮两独立证据：AI 多组学 Zenodo + JCO 摘要 RAI 难治去分化 |
| **D11** 乳酸化–EMT-TF（ETV4/KLF6）转移轴 | **30** | Strong | 本轮无新乳酸化论文，维持（待 KLF6 正式发表） |
| **D12（新·探索）** 铁死亡–ATC/PTC 轴 | **27** | Feasible | HIF-1α/ACSL 抵抗 + UTMD-CSF1 铁死亡 + Pin1/NCOA4 上游，ATC 铁死亡几乎空白 |
| **D6** MTC 5-HT/NETs 肝转移 | **27** | Feasible | miR-145-3p 补 MTC 转移机制，但未触及肝转移特异 |
| **D10** HT 自身免疫→LNM 保护自然对照 | **26** | Feasible | 本轮无新直接证据 |
| **D-ml** 算法/影像 LNM 预测 | **21** | Exploratory | 本轮+3 模型（方法升级但仍内部验证），仍拥挤 |

**D9 七维明细（本轮 31，由 28 升）**：Novelty 5（SPP1+ TAM 在 TC 中首次被 AI 多组学+ML 系统鉴定为 LNM 靶点，TC 内几乎空白）/ Feasibility 5（scRNA/空间+已发表队列+Zenodo 数据可用）/ Data 5（发现+验证队列可得）/ Validation 4（多组学+ML，但 Zenodo 为存档、JCO 为摘要，需正式发表验证）/ Clinical 5（LNM/RAI 难治终点直接）/ Method 4（需补体内 LNM 模型）/ Overcrowding 4（泛癌 SPP1+ TAM 热，但 TC 特异证据少，需差异化）。

**D12 七维明细（新，27）**：Novelty 4（铁死亡在 TC 新兴，ATC 特异性抵抗研究少）/ Feasibility 4（TCGA+本轮 HIF-1α/ACSL、UTMD 数据可用，需铁死亡试剂）/ Data 4（TCGA + 细胞模型）/ Validation 3（各 1 篇、多为体外）/ Clinical 4（RAI 难治/ATC 极差预后终点）/ Method 4（需补体内 RAI 模型）/ Overcrowding 4（铁死亡泛癌热，但 TC 细分空白）。

**D3 研究问题 / 下一步（维持）**：以 APOE−MGST1+ 双边界定义代谢–免疫干性转移亚群，TCGA+GEO 发现、独立 scRNA/空间队列验证，原代空间+类器官/PDX 体内靶向做功能闭环；注意 IL1β/SMDT1-MAPK 抑制性走向提示该轴可能含双向调节，claim 边界限定「代谢–免疫耦合的 LNM 驱动亚群」。

---

## 推荐下一步方向 (Recommended Next Direction)

**首选将 SPP1+ TAM 空间与功能验证作为本轮最直接的可执行产出（即推进 D9，并作为 D8 的 TAM 异质性补充）**。理由：本轮两篇独立证据（AI 多组学 Zenodo 存档 + JCO 摘要）使 SPP1+ TAM 成为相较 TREM2+ 更易立即落地的 TAM 亚群——其 LNM 预测与 RAI 难治去分化的双终点均已初步建立，且数据（scRNA+空间+Zenodo 存档）公开可得。

具体下一步：
1. **SPP1+ × TREM2+ 空间共定位验证（最高优先）**：复用已发表 POSTN+ myCAF 空间图谱 + 配对原发–LNM 单细胞图谱（run #21 引用 42430190），做 SPP1 × TREM2 多重免疫荧光/空间转录组共定位，检验「SPP1+ 与 TREM2+ 是否为同一/不同 TAM 生态位」，一举厘清 D8↔D9 关系。
2. **SPP1+ TAM 体内功能闭环**：在 PTC 类器官/PDX 中敲低/过表达 SPP1+ TAM 信号，评估 LNM 与 RAI 难治去分化，验证 JCO 摘要的去分化假说。
3. **D12 铁死亡预研**：以 HIF-1α/ACSL、UTMD-CSF1 为起点，做铁死亡诱导剂（如 RSL3/erastin）在 ATC/PTC 体内 LNM/RAI 模型的疗效，确认「铁死亡抵抗→转移/RAI 难治」因果。
4. **检索配置升级**：对 ME/SC/SP 维度默认 90 天窗口（或全维度统一 90 天 + DOI 去重），消减低频高分维度欠采样；基线继续为累积语料（本轮 latest 含 149 条）。

---

## 随访阅读清单 (Follow-Up Reading List)

- **SPP1+ TAM AI 多组学 (10.5281/zenodo.22290057)**：★本轮最关键，D9 起点；待正式发表后纳入 SPP1+ TAM 机制基底（当前为 Zenodo 存档，降档）。
- **SPP1+ 巨噬细胞 RAI 难治 (10.1200/jco.2026.44.19_suppl.239)**：JCO 增刊摘要，D9 第二独立证据，需追踪正式全文。
- **IL1β/SMDT1-MAPK (10.3390/cancers18182918)**：SMDT1 代谢–免疫基因的功能方向精细化，D3 轴需调和。
- **UTMD-CSF1 铁死亡 (10.1002/cam4.72220)** + **HIF-1α/ACSL (10.1186/s11658-026-00973-1)**：铁死亡–TAM/ATC 轴双件，D12 起点。
- **TLS 样空间存档 (10.5281/zenodo.22661715)**：PTC 空间生态位可复现数据，D3↔D8 空间验证可复用。
- **miR-145-3p MTC (10.1002/path.70116, PMID 42713718)**：MTC 局限→转移枢纽，补 D6。

---

## 可复现性说明 (Reproducibility Notes)

- 检索日期 / Search date: 2026-09-11
- 主数据库 / Primary DB: OpenAlex REST API（`api.openalex.org/works`）；补充 Crossref（`api.crossref.org`）+ Unpaywall（`api.unpaywall.org`，对 12 条 High/关键 DOI 异步校验，结果 `search_results_20260911_enrich.json`）
- 查询串 / Queries: 九路 a–i（见检索策略表）；过滤器 `title_and_abstract.search:<q>,from_publication_date:<date>`；`sort=publication_date:desc`；`per-page=25`
- 去重规则 / Dedup: 标题归一化主键合并多版本；DOI/PMID/归一化标题三重判重；期刊补充材料（`Table 1_…`等）正则剔除
- 筛选规则 / Screening: 标题须点名甲状腺（PTC/PTMC/FTC/MTC/ATC/thyroid）且整体为肿瘤主题；顺带提及甲状腺的他病（乳腺/肺等 LNM、桥本、眼病）剔除
- 文件 / Files:
  - `literature_review_20260911_030027.md`（本报告）
  - `search_results_20260911_030027.json`（30 天主窗口带时间戳结果）
  - `search_results_20260911_90day_supplement.json`（代谢重编程 90 天补跑中间产物，不覆盖基线）
  - `search_results_20260911_enrich.json`（12 条 High/关键 DOI 的 Crossref/Unpaywall 校验，异步）
  - `search_results_latest.json`（**累积基线**：run #21 的 113 条 + 本轮 36 条新增 = **149 条**，供下轮去重）
- 新增判定 / New-detection: 相对 `search_results_latest.json`（= run #21 输出，113 条）按 PMID/DOI/归一化标题比较；主窗口 31 条均为 ≥2026-08-12 真实新增；ME 90 天补跑 5 条为 2026-06-23–2026-07-17 区间、30 天窗口之外、故相对基线新。
- 通道状态 / Channel: 本机 NCBI eutils / pubmed.ncbi.nlm.nih.gov 不可达（HTTP 000），`paper-search-mcp` 不稳定（本轮未调用）；OpenAlex/Crossref/Unpaywall 直连稳定。
- 预印本/存档 / Preprints & deposits: 本轮严格 `type=preprint` 计数为 0；含 2 条 Zenodo `type=dataset` 仓库存档（SPP1+ TAM AI 多组学、TLS 空间存档）与 2 条会议摘要（JCO SPP1+、Endocrine Abstracts 免疫细胞因子），均按 deposit/abstract 降档，证据强度受限，绝不编造 PMID/DOI。

---

## 与历史报告差异 (Delta vs Run #21 / 2026-09-04)

- **新增数**：run #21 = 25 条真实新增（16 主窗口 + 9 单细胞补跑）；run #22 = **36 条真实新增**（31 主窗口 + 5 ME 90 天补跑），**零截断回填**——基线为累积语料（113→149），彻底消除滚动窗口伪新增。
- **各维度分布对比**（在范围新增，run #21 → run #22）：
  - 分子机制 MO：9(+补跑) → **14**
  - 预后转移 PR：12(+补跑) → **18**
  - 免疫微环境 IM：2(+补跑 TREM2+) → **6**（巨噬细胞/TAM 主题爆发）
  - 算法方法 AL：1 → **4**（3 个 LNM/RAI 模型）
  - 转移干性 ST：1 → **3**
  - 空间组学 SP：1(+补跑 KLF6) → **3**（主窗口，含 TLS 存档）
  - 单细胞 SC：9(补跑) → **3**（主窗口；本轮单窗口已非零，无需补跑）
  - 代谢重编程 ME：1(+补跑 β-羟基丁酰化) → **0(30d) + 5(90d 补跑)**（30 天窗口 0 经 90 天证伪为欠采样）
- **新信号（vs run #21）**：
  1. **★ SPP1+ TAM 轴强势浮现**（两独立证据：Zenodo AI 多组学 + JCO 摘要 RAI 难治去分化）——直接**强化 D9（28→31）**，并作为 D8 TREM2+ 的 TAM 异质性补充；
  2. **巨噬细胞/TAM 异质性成为活跃前沿**：UTMD-CSF1 铁死亡、DT 耐药（ATC）、系统炎症/免疫谱、免疫细胞因子 LNM——把 D8 从单亚群拓宽为 TAM 全景；
  3. **IL1β/SMDT1-MAPK 肿瘤抑制性**（High）——SMDT1 代谢–免疫基因获功能方向精细化，D3 轴需调和；
  4. **铁死亡–ATC/PTC 轴浮现**：HIF-1α/ACSL 抵抗 + UTMD-CSF1 诱导——新方向 **D12（~27）**；
  5. **代谢多层扩展**：饮食肌酸/α-亚麻酸、Pin1/NCOA4 铁蛋白自噬、MMRN1 Hippo、术后血清蛋白组；
  6. **MTC miR-145-3p 转移枢纽**——补 D6；**TLS 样空间存档**——补空间生态位数据。
- **D3 跟踪（APOE−/MGST1+ 代谢–免疫干性亚群）**：**无变化**——本轮无直接锚定 APOE/MGST1 癌细胞亚群的原发证据，D3 维持 Strong（rubric 33，连续第 22 轮确认）。但 SMDT1 再获数据点（抑制性走向），代谢–免疫轴在机制层持续累积且 TAM 侧（SPP1+/TREM2+）证据密集。
- **平台期判定**：否——36 条真实新增、代谢维度经 90 天补跑证伪「0=停滞」、SPP1+ TAM 与铁死亡双线并发。唯一低活跃为算法方向（仍拥挤、价值低）。本次代谢 30 天「0」经补跑确认属**短窗口低频高分维度欠采样**，非领域停滞（与 run #20 空间组学、run #21 单细胞同构）。
- **建议（下一轮）**：①对 ME/SC/SP 维度默认 90 天窗口（或全维度统一 90 天 + DOI 去重）以消减低频高分维度欠采样；②基线已为累积语料（149 条），继续沿用；③优先在 SPP1+ × TREM2+ 空间共定位验证上投入，作为本轮最直接的可执行产出，并并行启动 D12 铁死亡预研。
