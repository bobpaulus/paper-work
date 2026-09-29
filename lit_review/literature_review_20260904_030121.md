# 甲状腺癌文献监测报告 / Thyroid Cancer Literature Surveillance Report

Date / 检索日期: 2026-09-04
Sources / 数据源: OpenAlex REST API（主源，直连稳定）; Crossref + Unpaywall（High 条目 DOI 元数据与 OA 校验，仅补充）
Search window / 检索窗口: 主窗口 2026-08-28 → 2026-09-04（近 7 天，`from_publication_date`，严格对齐 run #20 基线日）；单细胞维度因 7 天窗口增量=0，按协议单独补跑 `--days 90`（2026-06-06 → 2026-09-04）
Run index / 轮次: #21（相对 run #20 / 2026-08-28 基线）
Primary retriever / 主检索器: `oa_search.py`（九路维度 a–i，`sort=publication_date:desc`）

---

## 中文摘要 (Chinese Abstract)

本轮以 OpenAlex 为主源，对甲状腺癌（PTC/PTMC/FTC/MTC/ATC）侵袭、淋巴结（LNM）与远处转移、复发、预后及其分子机制、肿瘤免疫微环境（TIME）、单细胞与空间组学、机器学习/深度学习算法方向执行增量监测。主窗口（7 天）去重后唯一记录 **24** 条，甲状腺在范围 **16** 条，相对 run #20 基线**全部为本周真实新增**（无截断回填，因本次 `--since` 精确对齐基线日）。单细胞维度 7 天窗口命中 0，按协议放宽至 90 天补跑，新增 **9** 条单细胞在范围记录（均为 2026-06-06→2026-08-28 区间、run #20 的 30 天窗口之外，故相对基线确为新）。**本轮去重后唯一记录 24（主窗口）+ 累积基线 88 = 113；本轮新增唯一记录共 25 条**（16 主窗口 + 9 单细胞补跑）。在范围预印本 **2** 条（1 条 Research Square 维生素 D 通路亚型 preprint；1 条 figshare KLF6 EMT 驱动 deposit）。

**本轮最强收敛信号**：90 天补跑回库的单细胞文献中包含**直接原发证据**——「Targeting the AHR–IDO1–kynurenine pathway in TREM2+ macrophages restores antitumor immunity in thyroid cancer」(Front Immunol, PMID 42553364) 以 scRNA + scATAC + mass cytometry + 空间验证 + 体内功能实验锁定 **TREM2+ 巨噬细胞**为甲状腺肿瘤免疫抑制的核心髓系亚群，并被 AHR–IDO1–犬尿氨酸轴驱动。这正是既往 run #20 标记为「本轮无新证据」的 **D8（TREM2+ AHR–IDO1 免疫代谢检查点）**——本轮**直接强化**该方向。同批补跑还回库 KLF6（EMT 驱动，转移 PTC 空间+单细胞）、CENPM（LNM 分子标志物，空间验证），均与 D3/D9 代谢–免疫–转移轴高度契合。

**持续跟踪重点方向状态**：APOE−/MGST1+ 代谢–免疫干性转移亚群（**D3**）——本轮**无变化**（无直接锚定 APOE/MGST1 癌细胞亚群的原发证据）；但其所属「代谢–免疫」轴在免疫侧（TREM2+ 髓系）获首次直接支撑，D8 由待补升级为强化。

## English Abstract

This run uses OpenAlex as the primary source for incremental surveillance of thyroid cancer (PTC/PTMC/FTC/MTC/ATC) covering invasion, lymph-node (LNM) and distant metastasis, recurrence, prognosis, molecular mechanisms, tumor immune microenvironment (TIME), single-cell and spatial omics, and ML/DL methods. The strict 7-day window (2026-08-28→2026-09-04, exactly aligned to the run #20 baseline date) yielded **24 deduplicated records, 16 in thyroid scope, all genuinely new this week** (no truncation backfill). The single-cell dimension returned 0 hits in 7 days; per protocol it was widened to a 90-day supplement (2026-06-06→2026-09-04) that added **9 in-scope single-cell records** (all dated before run #20's 30-day window, hence genuinely new vs baseline). **25 unique new records this run** (16 + 9). **2 in-scope preprints** (1 Research Square vitamin-D-pathway subtype preprint; 1 figshare KLF6 EMT-driver deposit).

**Strongest convergence signal**: the 90-day single-cell supplement surfaced **direct primary evidence** — "Targeting the AHR–IDO1–kynurenine pathway in TREM2+ macrophages restores antitumor immunity in thyroid cancer" (Front Immunol, PMID 42553364) uses scRNA + scATAC + mass cytometry + spatial + in vivo functional assays to pin **TREM2+ macrophages** as the core immunosuppressive myeloid subpopulation, driven by the AHR–IDO1–kynurenine axis. This directly **strengthens D8** (TREM2+ AHR–IDO1 immune-metabolic checkpoint), which run #20 had flagged as "no new evidence." The same supplement also recovered KLF6 (EMT driver in metastatic PTC, spatial + scRNA) and CENPM (LNM biomarker with spatial validation), both aligned with the D3/D9 metabolic–immune–metastatic axis.

**Tracked focus direction status**: APOE−/MGST1+ metabolic–immune stem-like metastatic subpopulation (**D3**) — **unchanged** (no direct primary evidence anchoring APOE/MGST1 cancer-cell subpopulations this run); however the immune arm of the same axis (TREM2+ myeloid) gains first direct support, upgrading D8 from pending to strengthened.

---

## 检索策略 (Search Strategy)

主源 OpenAlex（`api.openalex.org/works`），九路维度检索，过滤器 `title_and_abstract.search:<q>,from_publication_date:<date>`，`sort=publication_date:desc`，每路 `per-page=25`。维度代码：MO=分子机制 / IM=免疫微环境 / SC=单细胞 / SP=空间组学 / AL=算法方法 / PR=预后转移 / ST=转移干性 / ME=代谢重编程。

| 路 | 维度 | 窗口 | OpenAlex 命中 | 取回 | 新条目 | 状态 |
|---|---|---|---:|---:|---:|---|
| a | MO/PR | 7d | 7 | 7 | 7 | OK |
| b | MO | 7d | 8 | 8 | 5 | OK |
| c | AL/PR | 7d | 3 | 3 | 1 | OK |
| d | IM | 7d | 3 | 3 | 1 | OK |
| e | SC | 7d | 0 | 0 | 0 | **0→补跑** |
| f | SP | 7d | 1 | 1 | 1 | OK |
| g | PR | 7d | 11 | 11 | 7 | OK |
| h | ST | 7d | 1 | 1 | 1 | OK |
| i | ME | 7d | 1 | 1 | 1 | OK |
| e | SC | **90d** | 39 | 25 | 9 | 维度 0 放宽补跑 |

补充源约定：`paper-search-mcp` 本轮**未调用**——本机 NCBI eutils / pubmed.ncbi.nlm.nih.gov 实测仍不可达（HTTP 000），MCP 频繁 `not well-formed` 截断，按"失败即跳过、绝不阻塞主流程"处理。对 8 条 High 相关新文献经 Crossref 校验 DOI 元数据、Unpaywall 解析 OA 状态（全部命中、标题一致、无幻影 DOI；唯 KLF6 figshare deposit 不被 Crossref/Unpaywall 索引，标记为 [deposit]）。

窗口边沿处理：维度 e（单细胞）7 天增量 = 0 → 按协议单独补跑 `--days 90`（中间产物 `search_results_20260904_singlecell90.json`，不覆盖基线）。补跑确认单细胞维度并非领域停滞，而是 **7 天严格窗口对低频高分维度欠采样**——90 天窗口命中 39、在范围 14，且含 TREM2+/KLF6/CENPM 等最高价值机制文献。这与 run #20 空间组学"30 天=0 经 90 天补跑确认为窗口边沿"同构。

---

## 纳入论文 (Included Papers)

> 本轮 25 条相对 run #20 基线新增文献。标注：★ = 7 天主窗口新增（>2026-08-28）；▲ = 单细胞 90 天补跑新增（2026-06-06–2026-08-28）；[preprint] = 预印本 / [deposit] = 预印本式仓储。

**7 天主窗口（16 条）**

1. ★ **Subtype identification and prognostic signature construction of thyroid cancer based on vitamin D pathway genes.** [preprint] *Research Square* 2026-09-02. DOI:10.21203/rs.3.rs-10793784/v1. 中文要点：基于维生素 D 通路基因的 TC 亚型识别与预后特征，属代谢–免疫交叉亚型。
2. ★ **ETV4 coupled with p300-mediated histone lactylation drives thyroid cancer progression by activating autocrine TGFβ1 signaling.** *Genes & Diseases* 2026-09-01. DOI:10.1016/j.gendis.2026.102439. 中文要点：ETV4 经 p300 组蛋白乳酸化驱动 TC 进展，激活自分泌 TGFβ1——首见「乳酸化（lactylation）表观修饰→EMT→转移」轴进入 TC（ME/MO 维度）。
3. ★ **Multimodal multi-task deep learning for preoperative prediction of central and lateral lymph node metastasis in papillary thyroid carcinoma.** *Int J Med Inform* 2026-09-01. DOI:10.1016/j.ijmedinf.2026.106700. 中文要点：多模态多任务 DL 预测 PTC 中央区+侧颈 LNM，方法学较纯列线图升级（仍待外部验证）。
4. ★ **Prognostic Factors Affecting Survival in Thyroid Carcinoma: A Retrospective Single-center Study.** *Anatol J Gen Med Res* 2026-09-01. DOI:10.4274/anatoljmed.2026.70188. 中文要点：45 例单中心生存预后因素回顾，样本小、证据弱。
5. ★ **Patient Redistribution Across Risk Categories in Differentiated Thyroid Cancer Using the 2025 Versus 2015 American Thyroid Association Risk Stratification Systems.** *Endocrine Practice* 2026-09-01. PMID:42679997. DOI:10.1016/j.eprac.2026.08.019. 中文要点：2025 vs 2015 ATA 风险分层再分布，呼应去过度治疗趋势。
6. ★ **SMARCA4-deficient Anaplastic Thyroid Carcinoma: A Hitherto Unreported Case.** *Virchows Arch* 2026-09-01. PMID:42678420. DOI:10.1007/s00428-026-04689-7. 中文要点：SMARCA4 缺失 ATC 个案，呼应 SWI/SNF（ARID1A/SMARCA4）去分化主题。
7. ★ **How to manage medullary thyroid carcinoma: current treatment strategies.** *Drugs Context* 2026-08-31. DOI:10.7573/dic.2026-4-3. 中文要点：MTC 治疗策略综述（RET 驱动、降钙素监测、远处转移）。
8. ★ **Mechanistic and Clinical Perspectives on Traditional Chinese Medicine in Thyroid Cancer Management.** *Biomol Ther* 2026-08-31. PMID:42676033. DOI:10.4062/biomolther.2026.073. 中文要点：TCM 调控 BRAF/RAS/RET、MAPK/PI3K-Akt/mTOR/NF-κB 的综述（High，非原发）。
9. ★ **Postoperative Surveillance in Differentiated Thyroid Cancer: Response-Adapted De-Escalation in the 2025 ATA and 2026 KTA Guidelines.** *Endocrinol Metab* 2026-08-31. DOI:10.3803/enm.2026.3156. 中文要点：DTC 术后反应适应性降级随访指南述评。
10. ★ **High-grade follicular cell-derived thyroid carcinomas (PDTC/DHGTC): standardized histologic criteria and a practical diagnostic algorithm.** *Sib Sci Med J* 2026-08-30. DOI:10.18699/ssmj20260402. 中文要点：PDTC/DHGTC（WHO-2022 高分级）组织学标准与诊断流程。
11. ★ **Multi-omics, machine learning, and molecular simulation identify CD44 as a candidate target in endocrine-disrupting chemical–associated thyroid cancer progression.** *Molecular Diversity* 2026-08-30. PMID:42669107. DOI:10.1007/s11030-026-11721-0. 中文要点：多组学+ML+分子模拟锁定 CD44 为内分泌干扰物相关 TC 进展靶点——与 D9 SPP1–CD44 轴呼应。
12. ★ **Serum Lactate Dehydrogenase as a Potential Biomarker for Lateral Lymph Node Metastasis in Thyroid Cancer Patients After Total Thyroidectomy.** *J Current Surgery* 2026-08-29. DOI:10.14740/jcs1035. 中文要点：血清 LDH 作为侧颈 LNM 标志物（LDH=糖酵解 proxy，代谢–转移维度）。
13. ★ **Contribution to Diagnostic Accuracy and Prognostic Significance of MicroRNAs in Thyroid Cancer.** *J Current Surgery* 2026-08-29. DOI:10.14740/jcs1049. 中文要点：miRNA 在 TC 诊断/预后价值的综述（High，非原发）。
14. ★ **MODERN METHODS FOR THE INVESTIGATION OF THYROID DISEASES.** *Yassawi J Health Sci* 2026-08-28. DOI:10.47526/3080-8715.6486. 中文要点：2021–2026 甲状腺疾病现代研究方法学综述。
15. ★ **Thyroid Cancer Management in Contemporary Practice: A Systematic Review and Meta-Analysis of Diagnostic Pathways, Surgical Strategies, Airway Challenges, and Mediastinal Extension.** *Clin Ter* 2026-08-28. PMID:42664150. DOI:10.7417/ct.2026.2130. 中文要点：局晚 TC 气管/纵隔侵犯诊疗系统综述。
16. ★ **Afirma Xpression Atlas Alteration Status Is Associated with Malignancy Risk in Indeterminate Thyroid Nodules.** *Thyroid* 2026-08-28. PMID:42663592. DOI:10.1177/10507256261484715. 中文要点：Afirma XA 全转录组变异与 indeterminat 结节恶性风险关联。

**单细胞 90 天补跑（9 条，▲）**

17. ▲ **Construction and validation of a β-hydroxybutyrylation-related molecular model for predicting prognosis of papillary thyroid carcinoma.** *Transl Cancer Res* 2026-08-01. DOI:10.21037/tcr-2026-0917. 中文要点：β-羟基丁酰化（Kbhb，酮体/代谢衍生修饰）PTC 预后模型（TCGA）。
18. ▲ **Single-cell transcriptomic analysis identifies decreased CEBPB and PAX8 expression associated with immune landscape differences between medullary and papillary thyroid carcinoma.** *Transl Cancer Res* 2026-08-01. DOI:10.21037/tcr-2026-1098. 中文要点：MTC vs PTC 单细胞免疫景观差异（CEBPB/PAX8 下调）。
19. ▲ **Single Cell and Spatial Transcriptome Profiling Identifies KLF6 as a EMT Driver in Metastatic PTC.** [deposit] *Figshare* 2026-07-25. DOI:10.6084/m9.figshare.33085235.v1. 中文要点：转移 PTC 中 S100A2+ 恶性 EPC 经 EMT 转分化为 POSTN+→THY1+ CAF，KLF6 为 EMT 驱动（空间+单细胞）。
20. ▲ **The transcriptional landscape in thyroid cancer: current status of circulating biomarkers and liquid biopsy approaches.** *Expert Rev Anticancer Ther* 2026-07-23. PMID:42490163. DOI:10.1080/14737140.2026.2708770. 中文要点：TC 转录组与液体活检景观综述。
21. ▲ **CENPM as a biomarker and therapeutic target for lymph node metastasis in thyroid carcinoma.** *Front Genet* 2026-07-22. PMID:42553973. DOI:10.3389/fgene.2026.1875148. 中文要点：CENPM 经 TCGA 广义加性模型筛选 + 空间转录组 + IHC 验证为 LNM 分子标志物/靶点。
22. ▲ **Targeting the AHR–IDO1–kynurenine pathway in TREM2+ macrophages restores antitumor immunity in thyroid cancer.** *Front Immunol* 2026-07-21. PMID:42553364. DOI:10.3389/fimmu.2026.1826288. 中文要点：scRNA+scATAC+mass cytometry+空间+体内实验锁定 TREM2+ 巨噬细胞为免疫抑制髓系亚群，AHR–IDO1–犬尿氨酸轴驱动；靶向该轴恢复抗肿瘤免疫（★D8 直接证据）。
23. ▲ **Single-cell transcriptomics decodes the immunological landscape of thyroid cancer: Implications for immunotherapeutic targeting and precision oncology.** *Crit Rev Oncol Hematol* 2026-07-17. PMID:42463025. DOI:10.1016/j.critrevonc.2026.105490. 中文要点：TC 单细胞免疫景观综述。
24. ▲ **Single-cell sequencing profiling of intratumoral heterogeneity and immunosuppressive microenvironment in primary thyroid cancer and lymph node metastases.** *OncoImmunology* 2026-07-10. PMID:42430190. DOI:10.1080/2162402x.2026.2701504. 中文要点：55,005 单细胞原发–LNM 配对图谱，CNV 推断解析瘤内异质性与免疫抑制微环境。
25. ▲ **Cell-state transitions and microenvironmental remodeling in thyroid cancer progression revealed by single-cell and spatial transcriptomics.** *Front Immunol* 2026-07-08. PMID:42488635. DOI:10.3389/fimmu.2026.1904196. 中文要点：PTC→DTC(RAI-R)→PDTC→ATC 进展的细胞状态与空间异质综述。

---

## 证据矩阵 (Evidence Matrix)

> 列：维度 / 相关性 / 预印本 / OA / 疾病人群 / 数据源 / 方法 / 终点 / 主要发现 / 验证 / 局限 / 缺口 / 后续方向。相关性 High/Med/Low；OA: gold/diamond/hybrid/green/closed/bronze。

| 论文 (Paper) | 维度 | 相关性 | 预印本 | OA | 疾病/人群 | 数据源 | 方法 | 终点 | 主要发现 | 验证 | 局限 | 缺口 | 后续方向 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Vitamin D 通路亚型 [preprint] (10.21203/rs.3.rs-10793784/v1) | MO/PR/IM | Med | 是 | green | TC | 转录组+临床 | 亚型+预后特征 | 亚型/生存 | 维生素 D 通路基因定义 TC 亚型与预后 | 计算 | preprint，未评议 | 体外/独立队列 | 维 D 通路免疫调节 |
| ETV4+p300 lactylation→TGFβ1 (10.1016/j.gendis.2026.102439) | MO/ME | Med | 否 | gold | PTC | 细胞+组织 | 乳酸化 ChIP/功能 | EMT/进展 | ETV4+p300 乳酸化驱动 TGFβ1 自分泌促进展 | 体外 | 体内弱 | 乳酸化抑制剂 | 乳酸化–EMT 轴 (D11) |
| 多模态多任务 DL LNM (10.1016/j.ijmedinf.2026.106700) | AL/PR | Med | 否 | closed | PTC | 单中心影像+临床 | 多模态多任务 DL | CLNM/LLNM | 术前预测中央+侧颈 LNM | 内部 | 单中心、非分子 | 外部多中心 | 多模态融合决策 |
| 45 例预后因素 (10.4274/anatoljmed.2026.70188) | PR | Low | 否 | diamond | TC | 单中心 45 例 | 回顾预后 | OS | 临床病理预后因素 | 单中心 | n=45 小 | 大样本 | 预后模型 |
| 2025 vs 2015 ATA (10.1016/j.eprac.2026.08.019) | PR | Low | 否 | closed | DTC | 分层比较 | 指南比较 | 风险再分布 | 2025 ATA 风险再分层 | 指南 | 非实证 | 真实世界 | 分层外推 |
| SMARCA4 缺失 ATC (10.1007/s00428-026-04689-7) | ST | Low | 否 | closed | ATC | 个案 | 病理/分子 | 去分化 | SWI/SNF 缺失 ATC 罕见例 | 个案 | n=1 | 队列 | SWI/SNF 缺陷 |
| MTC 治疗综述 (10.7573/dic.2026-4-3) | MO/PR | Med | 否 | gold | MTC | 综述 | 综述 | 治疗 | RET/降钙素/MTC 管理 | 综述 | 非原发 | — | MTC 靶向 |
| TCM 综述 (10.4062/biomolther.2026.073) | MO/IM | **High** | 否 | hybrid | TC | 综述 | 综述 | 机制 | TCM 调控 BRAF/RAS/RET、MAPK/PI3K/NF-κB | 综述 | 非原发 | 机制验证 | TCM 免疫调节 |
| 术后降级随访 (10.3803/enm.2026.3156) | PR | Low | 否 | diamond | DTC | 指南 | 述评 | 随访 | 反应适应性降级 | 述评 | 非实证 | 前瞻 | 降级队列 |
| PDTC/DHGTC 标准 (10.18699/ssmj20260402) | MO/PR | Med | 否 | diamond | PDTC/DHGTC | 病理 | 标准 | 诊断 | WHO-2022 高分级组织标准 | 共识 | 单中心 | 多中心 | 诊断流程 |
| CD44 EDC 相关 TC (10.1007/s11030-026-11721-0) | PR/ME | Low | 否 | closed | TC | 多组学+ML | 模拟 | 靶点 | CD44 为 EDC 相关 TC 靶点 | 计算 | 湿实验缺 | 验证 | SPP1–CD44 (D9) |
| 血清 LDH 侧颈 LNM (10.14740/jcs1035) | MO/PR | Med | 否 | diamond | TC（2560 例） | 临床队列 | 标志物 | 侧颈 LNM | 血清 LDH 预测侧颈 LNM | 队列 | 回顾 | 外部 | LDH 代谢标志物 |
| miRNA 诊断/预后 (10.14740/jcs1049) | MO/PR | **High** | 否 | diamond | TC | 综述 | 综述 | 诊断/预后 | miRNA 诊断/预后价值 | 综述 | 非原发 | 临床验证 | miRNA panel |
| 现代方法综述 (10.47526/3080-8715.6486) | MO/PR | Med | 否 | bronze | 甲状腺疾病 | 综述 | 综述 | 方法 | 2021–26 研究方法 | 综述 | 非原发 | — | 方法学 |
| TC 管理 SR/MA (10.7417/ct.2026.2130) | MO | Low | 否 | closed | 局晚 TC | SR/MA | 系统综述 | 诊疗 | 气管/纵隔侵犯诊疗整合 | SR/MA | 异质 | 前瞻 | 局晚管理 |
| Afirma XA (10.1177/10507256261484715) | PR | Low | 否 | closed |  indeterminate 结节 | 回顾 | 分子诊断 | 恶性风险 | XA 变异关联恶性风险 | 回顾 | 单中心 | 多中心 | 分子诊断 |
| β-羟基丁酰化模型 (10.21037/tcr-2026-0917) | SC/ME | Med | 否 | diamond | PTC | TCGA | Kbhb 亚型/预后 | 生存 | Kbhb 相关预后模型 | TCGA | 仅生信 | 湿实 | 酮体/代谢修饰 |
| CEBPB/PAX8 MTC vs PTC (10.21037/tcr-2026-1098) | SC | **High** | 否 | diamond | MTC/PTC | scRNA | 单细胞分型 | 免疫景观 | CEBPB/PAX8 下调关联 MTC 差异免疫 | scRNA | 探索性 | 功能 | MTC 分化 |
| KLF6 EMT 驱动 [deposit] (10.6084/m9.figshare.33085235.v1) | SC/SP | **High** | 是 | green | 转移 PTC | scRNA+空间 | 空间+单细胞 | EMT/CAF/DM | KLF6 驱动 S100A2+ EPC→POSTN+/THY1+ CAF | 空间+单细胞 | deposit，未评议 | 体内靶向 | KLF6 EMT (D11) |
| 液体活检景观 (10.1080/14737140.2026.2708770) | SC | Med | 否 | closed | TC | 综述 | 综述 | 液体活检 | 转录组/液体活检景观 | 综述 | 非原发 | — | 液体活检 |
| CENPM LNM (10.3389/fgene.2026.1875148) | SC/PR | **High** | 否 | gold | THCA | TCGA+空间+IHC | 加性模型/空间 | LNM | CENPM 为 LNM 分子标志物/靶点 | 多队列+空间 | 机制浅 | 体内 | 分子 LNM 靶点 |
| TREM2+ AHR–IDO1 (10.3389/fimmu.2026.1826288) | SC/IM | **High** | 否 | gold | TC | scRNA+scATAC+CyTOF+空间+体内 | 多组学+功能 | 免疫抑制 | TREM2+ 巨噬细胞经 AHR–IDO1–犬尿氨酸致免疫抑制 | 多组学+体内 | 髓系为主 | 临床转化 | **D8 强化** |
| 单细胞免疫景观 (10.1016/j.critrevonc.2026.105490) | SC | Low | 否 | closed | TC | 综述 | 综述 | 免疫 | 单细胞免疫景观 | 综述 | 非原发 | — | 免疫靶点 |
| 瘤内异质+LNM (10.1080/2162402x.2026.2701504) | SC/IM | **High** | 否 | gold | 原发–LNM | 55,005 细胞 | scRNA+CNV | 异质/免疫 | 配对原发–LNM 高分辨图谱 | 单细胞 | 队列中 | 空间 | 转移演化 |
| 细胞状态转换 (10.3389/fimmu.2026.1904196) | SC/SP | **High** | 否 | gold | PTC→ATC | 综述 | 综述 | 进展 | 进展细胞状态/空间异质 | 综述 | 非原发 | — | 进展轨迹 |

---

## 已知结论 (What Is Already Known)

> 下列为跨 run #16–#20 稳定收敛、且被本轮证据相容（未反证）的结论；本轮新文献均不与之冲突。

1. **代谢–免疫耦合驱动 LNM（核心轴 1）**：MGST1 "Mito-high"/免疫冷亚型、SHMT2、GLTC-LDHA、SOX12-YBX1-LDHA、SMDT1 指向「代谢重编程→免疫抑制→淋巴结转移」。本轮 **ETV4+p300 乳酸化→TGFβ1**（原发表）、**血清 LDH 侧颈 LNM**（糖酵解 proxy）、**β-羟基丁酰化 PTC 模型**、**维生素 D 通路亚型** 四条独立线索共同强化「代谢修饰/代谢物→TC 进展与转移」链条，且从乳酸化、酮体衍生修饰、到维生素 D 通路多层面铺开。
2. **干性样转移亚群（核心轴 2 / D3）**：APOE−/MGST1+ 代谢–免疫干性亚群、ISG15/KPNA2（ATC）、DLK1（MTC）等。本轮**无直接锚定 APOE/MGST1 癌细胞亚群的原发证据**；但 KLF6 EMT（转移 PTC EPC→CAF 转分化）、CENPM LNM 属该轴邻近机制补充。
3. **POSTN+ myCAF 空间图谱（核心轴 3）**：POSTN+ CAF 空间图谱预测 LNM。本轮 KLF6 论文给出 S100A2+ EPC→POSTN+→THY1+ CAF 的 EMT 转分化序列，为 CAF 起源提供单细胞–空间证据闭环。
4. **影像/多组学 AI 拥挤（核心轴 4）**：本轮新增 1 个多模态多任务 DL（方法学较纯列线图升级，但仍单中心内部验证）+ 多位综述/系统综述；再次确认该方向增量价值低、外部泛化未解。
5. **BRAF V600E 与 PD-L1 meta 远处 vs LNM 解耦（核心轴 5）**：本轮 TCM 综述与 ATA 分层再分布文献相容「TERT/BRAF 为预后锚点」共识，无反证。
6. **★ 新确认（本轮直接证据）— TREM2+ 髓系免疫代谢检查点（D8）**：TREM2+ 巨噬细胞经 AHR–IDO1–犬尿氨酸轴驱动免疫抑制，首次在 TC 中以多组学+体内功能闭环证实。这是既往 run #20「D8 无新证据」缺口的本轮填补。

---

## 未解问题 (What Remains Unclear)

- **D3 癌细胞亚群的原代空间验证与体内靶向仍空缺**：APOE−/MGST1+ 代谢–免疫干性转移亚群虽多轮被推荐，仍缺原代组织空间验证 + 体内靶向干预证据（本轮未补）。TREM2+ 证据属**髓系免疫侧**，非癌细胞 APOE/MGST1 亚群本身。
- **TREM2+ 巨噬细胞的临床转化缺口**：AHR–IDO1–犬尿氨酸轴已被靶向恢复免疫，但缺TC 患者队列中 TREM2+ 丰度与 LNM/RAI 抵抗/生存的真实世界关联，以及 IDO1 抑制剂在 TC 的疗效证据。
- **乳酸化–EMT 轴的因果未闭合**：ETV4+p300 乳酸化→TGFβ1 为单篇体外证据，缺乳酸化写入 ETV4/KLF6 靶基因的直接 ChIP 与体内 LNM 模型。
- **KLF6 deposit 未同行评议**：figshare 仓储非期刊，证据强度降档，需正式发表版确认 S100A2+→CAF 序列。
- **CENPM 机制深度不足**：CENPM 作为 LNM 分子标志物已多队列+空间验证，但促转移机制（如细胞周期/中心体）未阐明。
- **算法模型外部泛化**：本轮多模态 DL 仍单中心内部验证，跨人群/跨设备漂移未评估。

---

## 领域方法/数据局限 (Method/Data Limitations In The Field)

- **7 天严格窗口对低频高分维度欠采样**：单细胞维度 7 天命中 0，但 90 天补跑命中 39、在范围 14 且含最高价值文献——证明**滚动短窗口会系统性漏掉低频高分维度**。建议对 SC/SP 等稀疏维度默认 90 天或对全部维度统一 90 天窗口、以 DOI 去重。
- ** PubMed 编目滞后**：本轮 25 篇中多数无 PMID（仅 6 篇有 PMID：42679997/42678420/42676033/42669107/42663592/42664150，以及单细胞补跑 42490163/42553973/42553364/42463025/42430190/42488635），以 DOI 为主标识，符合 skill 规范。
- **单细胞/空间组学稀疏但非停滞**：单细胞补跑显示该维度活跃（14 在范围），空间组学本轮仅 1 条（主窗口），ATC/MTC 亚型与远处转移空间证据仍薄。
- **预印本/仓储降档**：维生素 D preprint、KLF6 figshare deposit 按规范降档。
- **综述占比偏高**：本轮 High 条目中 TCM 综述、miRNA 综述、多份单细胞/方法学综述为非原发证据，应与原发机制论文区分权重。
- **伪新增消减验证**：因本次 `--since` 精确对齐 run #20 基线日，主窗口 16 条均为真实新增、无截断回填——run #20 抱怨的「滚动窗口伪新增」本轮已规避（基线已改为累积语料，见可复现性）。

---

## 候选未来方向 (Candidate Future Directions)

> 评分按 research-direction-rubric.md 七维（Novelty/Feasibility/Data/Validation/Clinical/Method/Overcrowding，各 1–5，满分 35）。28–35 = Strong。本轮更新：D8 由「待补」升级为「强化」；新增 D11。

| 方向 | 七维小计 | 评级 | 一句话依据 |
|---|---:|---|---|
| **D3** APOE−/MGST1+ 代谢–免疫干性转移亚群 | **33** | Strong | 连续 21 轮确认，本轮无反证；TREM2+ 免疫侧证据间接支撑同轴的免疫臂 |
| **D8** TREM2+ AHR–IDO1 免疫代谢检查点 | **32** | Strong（↑强化） | 本轮获 scRNA+scATAC+CyTOF+空间+体内直接原发证据（42553364） |
| **D11（新）** 乳酸化–EMT-TF（ETV4/KLF6）转移轴 | **30** | Strong | ETV4 乳酸化（原发）+ KLF6 EMT（deposit）共指乳酸/乳酸化→EMT-TF→转移，TC 中近乎空白 |
| **D9** citrullination/PADI 侵袭程序 | **28** | Strong | SPP1–CD44 轴机制清晰；本轮 CD44（EDC 相关）再补分子靶点线索 |
| **D6** MTC 5-HT/NETs 肝转移 | **27** | Feasible | MTC 治疗综述+CEBPB/PAX8 单细胞补强 MTC 分型，但未触及肝转移特异 |
| **D10** HT 自身免疫→LNM 保护自然对照 | **26** | Feasible | 「免疫热/LNM 冷」自然对照维度，本轮无新证据 |
| **D-ml** 算法/影像 LNM 预测 | **21** | Exploratory | 本轮+1 多模态多任务 DL（方法升级但仍单中心），仍拥挤 |

**D8 七维明细（本轮 32，由 30 升）**：Novelty 5（TREM2+ 髓系免疫代谢在 TC 首次多组学闭环）/ Feasibility 5（公开 scRNA/空间+已发表队列可用）/ Data 5（发现+验证队列可得）/ Validation 5（scRNA+scATAC+CyTOF+空间+体内多层级验证）/ Clinical 4（对应免疫抑制/LNM 终点，缺真实世界 IDO1 疗效）/ Method 5（清晰设计边界）/ Overcrowding 3（TC 内 TREM2+ 尚少，但泛癌 TREM2 热，需差异化）。

**D11 七维明细（新，30）**：Novelty 5（组蛋白乳酸化在 TC 转移近乎未探索；ETV4 乳酸化为首发）/ Feasibility 4（TCGA+GEO+本轮两文数据可用，需 ChIP/功能）/ Data 4（TCGA + ETV4/KLF6 数据）/ Validation 3（各 1 篇、KLF6 为 deposit）/ Clinical 4（LNM/远处转移终点）/ Method 4（需补体内 LNM 模型）/ Overcrowding 5（TC 乳酸化–EMT 轴明显空白）。

**D3 研究问题 / 下一步（维持）**：以 APOE−MGST1+ 双边界定义代谢–免疫干性转移亚群，TCGA+GEO 发现、独立 scRNA/空间队列验证，原代空间+类器官/PDX 体内靶向（PPARγ 激动剂或 IDO1 抑制）做功能闭环；主要风险为原代空间样本稀缺与靶向选择性，claim 边界限定「代谢–免疫耦合的 LNM 驱动亚群」。

---

## 推荐下一步方向 (Recommended Next Direction)

**首选维持 D3（APOE−/MGST1+ 代谢–免疫干性转移亚群，rubric 33，Strong）**，但本轮证据使**执行路径更清晰**：优先把本轮 TREM2+ 巨噬细胞（D8，42553364）作为 D3 的**免疫侧功能读出**——即在原代 PTC 空间验证中同时量化 APOE−/MGST1+ 癌细胞亚群与其邻近 TREM2+ 髓系生态位的共定位，检验「癌细胞代谢–免疫干性亚群 ↔ TREM2+ 免疫抑制生态位」是否空间偶联。这把 D3（癌细胞臂）与 D8（髓系臂）并入同一空间验证实验，一举补齐两边最大缺口。

具体下一步：
1. **空间共定位验证**（最高优先）：复用已发表 POSTN+ myCAF 空间图谱 + 配对原发–LNM 单细胞图谱（42430190），做 APOE/MGST1 × TREM2 多重免疫荧光/空间转录组共定位，验证 D3↔D8 空间偶联假说。
2. **D11 机制预研**：以 ETV4/KLF6 为起点，做乳酸化 ChIP-qPCR + 体内 LNM 模型，确认「乳酸→乳酸化→EMT-TF」因果；若成立，D11 可升格为独立强方向。
3. **D8 临床转化**：在 TC 队列中量化 TREM2+ 丰度与 LNM/RAI 抵抗/生存关联，并评估 IDO1 抑制剂联合免疫的可行性。
4. **检索基线已改为累积语料**（本轮 latest 含 113 条），并建议对 SC/SP 维度默认 90 天窗口以消减低频高分维度欠采样。

---

## 随访阅读清单 (Follow-Up Reading List)

- **TREM2+ AHR–IDO1 (10.3389/fimmu.2026.1826288, PMID 42553364)**：★本轮最关键，直接支撑 D8，建议作为 D3↔D8 空间验证的免疫侧锚点文献。
- **KLF6 EMT 驱动 (10.6084/m9.figshare.33085235.v1)**：转移 PTC EPC→CAF 转分化序列，待正式发表后纳入 D3/D11 EMT 机制基底。
- **CENPM LNM (10.3389/fgene.2026.1875148, PMID 42553373)**：分子 LNM 标志物+空间验证，优于拥挤的影像列线图方向。
- **ETV4+p300 乳酸化 (10.1016/j.gendis.2026.102439)**：TC 乳酸化–EMT 首发，D11 起点。
- **CEBPB/PAX8 MTC (10.21037/tcr-2026-1098)**：MTC vs PTC 单细胞免疫差异，补 D6 MTC 分型。
- **瘤内异质+LNM (10.1080/2162402x.2026.2701504, PMID 42430190)**：55,005 细胞配对图谱，D3 空间验证可复用。

---

## 可复现性说明 (Reproducibility Notes)

- 检索日期 / Search date: 2026-09-04
- 主数据库 / Primary DB: OpenAlex REST API（`api.openalex.org/works`）；补充 Crossref（`api.crossref.org`）+ Unpaywall（`api.unpaywall.org`）
- 查询串 / Queries: 九路 a–i（见检索策略表）；过滤器 `title_and_abstract.search:<q>,from_publication_date:<date>`；`sort=publication_date:desc`；`per-page=25`
- 去重规则 / Dedup: 标题归一化主键合并多版本；DOI/PMID/归一化标题三重判重；期刊补充材料（`Table 1_…`等）正则剔除
- 筛选规则 / Screening: 标题须点名甲状腺（PTC/PTMC/FTC/MTC/ATC/thyroid）且整体为肿瘤主题；顺带提及甲状腺的他病（乳腺/肺等 LNM、桥本、眼病）剔除
- 文件 / Files:
  - `literature_review_20260904_030121.md`（本报告）
  - `search_results_20260904_030121.json`（7 天主窗口带时间戳结果）
  - `search_results_20260904_singlecell90.json`（单细胞 90 天补跑中间产物，不覆盖基线）
  - `search_results_20260904_enrich.json`（8 条 High DOI 的 Crossref/Unpaywall 校验）
  - `search_results_latest.json`（**累积基线**：run #20 的 88 条 + 本轮 25 条新增 = 113 条，供下轮去重）
- 新增判定 / New-detection: 相对 `search_results_latest.json`（= run #20 输出）按 PMID/DOI/归一化标题比较；主窗口 16 条均为 >2026-08-28 真实新增（无截断回填）；单细胞 9 条为 2026-06-06–2026-08-28 区间、run #20 的 30 天窗口之外、故相对基线新。
- 通道状态 / Channel: 本机 NCBI eutils / pubmed.ncbi.nlm.nih.gov 不可达（HTTP 000），`paper-search-mcp` 不稳定（本轮未调用）；OpenAlex/Crossref/Unpaywall 直连稳定。
- 预印本 / Preprints: 本轮在范围预印本 2（维生素 D Research Square preprint；KLF6 figshare deposit），证据强度按规范降档。

---

## 与历史报告差异 (Delta vs Run #20 / 2026-08-28)

- **新增数**：run #20 = 19 条（其中 5 条真新增、14 条截断回填）；run #21 = **25 条真实新增**（16 主窗口 + 9 单细胞补跑），**零截断回填**——因本次 `--since` 精确对齐基线日，且基线已改为累积语料，彻底消除 run #20 抱怨的滚动窗口伪新增。
- **各维度分布对比**（在范围，run #20 → run #21 主窗口 16 条 + 补跑 9 条）：
  - 分子机制 MO：24 → 主窗口 9（+补跑含 MO 数条）
  - 预后转移 PR：33 → 主窗口 12
  - 免疫微环境 IM：7 → 主窗口 2 + **补跑 TREM2+ 强证据**
  - 算法方法 AL：13 → 1（多模态多任务 DL）
  - 转移干性 ST：4 → 1（SMARCA4 缺失 ATC）
  - 空间组学 SP：3 → 1（主窗口）；补跑 KLF6 含空间
  - 单细胞 SC：5 → **补跑 9（强反弹，7 天窗口 0 为欠采样假象）**
  - 代谢重编程 ME：9 → 主窗口 1（ETV4 乳酸化）+ 补跑 β-羟基丁酰化
- **新信号（vs run #20）**：
  1. **★ TREM2+ 巨噬细胞 AHR–IDO1–犬尿氨酸轴**（直接原发证据，42553364）——填补 run #20「D8 无新证据」缺口，**强化 D8**；
  2. **乳酸化–EMT 轴**：ETV4+p300 乳酸化→TGFβ1（原发）+ KLF6 EMT 驱动（deposit），共指「乳酸/乳酸化→EMT-TF→转移」，**新方向 D11**；
  3. **CENPM 分子 LNM 标志物**（空间验证）——优于影像列线图；
  4. **代谢标志物/代谢修饰群**：血清 LDH 侧颈 LNM、β-羟基丁酰化 PTC 模型、维生素 D 通路亚型——代谢轴从「基因亚型」扩展到「代谢物/修饰」层面；
  5. **SMARCA4 缺失 ATC**——SWI/SNF 去分化主题延续（呼应 run #20 ARID1A）。
- **D3 跟踪（APOE−/MGST1+ 代谢–免疫干性亚群）**：**无变化**——本轮无直接锚定 APOE/MGST1 癌细胞亚群的原发证据，D3 维持 Strong（rubric 33，连续第 21 轮确认）。但其所属「代谢–免疫」轴在**免疫侧（TREM2+ 髓系）获首次直接支撑**，D8 由待补升级为强化，整体轴证据增强。
- **平台期判定**：否——25 条真实新增、单细胞维度经 90 天补跑证伪「0=停滞」、代谢轴多线并发。唯一低活跃为算法方向（仍拥挤、价值低）。本次单细胞 7 天「0」经补跑确认属**短窗口低频高分维度欠采样**，非领域停滞（与 run #20 空间组学同构）。
- **建议（下一轮）**：①对 SC/SP 维度默认 90 天窗口（或全维度统一 90 天 + DOI 去重）以消减低频高分维度欠采样；②基线已为累积语料，继续沿用；③优先在 D3↔D8 空间共定位验证上投入，作为本轮最直接的可执行产出。
