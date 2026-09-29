# 甲状腺癌文献监测报告 / Thyroid Cancer Literature Surveillance Report

Date / 检索日期: 2026-08-28
Sources / 数据源: OpenAlex REST API（主源，直连稳定）; Crossref + Unpaywall（DOI 元数据与 OA 校验，仅补充）
Search window / 检索窗口: 2026-07-29 → 2026-08-28（近 30 天，`from_publication_date`）
Run index / 轮次: #20（相对 run #19 / 2026-08-21 基线）
Primary retriever / 主检索器: `oa_search.py`（九路维度 a–i，`sort=publication_date:desc`）

---

## 中文摘要 (Chinese Abstract)

本轮以 OpenAlex 为主源、对甲状腺癌（PTC/PTMC/FTC/MTC/ATC）侵袭、淋巴结与远处转移、复发、预后及其分子机制、肿瘤免疫微环境、单细胞与空间组学、机器学习/深度学习算法方向执行近 30 天增量监测。去重后唯一记录 **88** 条，甲状腺在范围 **58** 条，剔除 **30** 条（26 条标题未点名甲状腺、4 条非肿瘤主题）；合并 **25** 组多版本记录。相对 run #19 基线**新增 19 条**（其中 5 篇发表于 run #19 窗口结束 2026-08-21 之后、确为本周新增；14 条为 run #19 单路 `per-page=25` 截断导致的窗口边沿回填，主要为 Gland Surgery 列线图批次，非领域新进展）。在范围预印本 **4** 条（本轮新增 1 条）。

本轮**无直接强化或削弱 D3（APOE−/MGST1+ 代谢–免疫干性转移亚群）的新证据**——D3 维持 Strong（rubric 33，连续第 20 轮确认）。真正新增的机制信号集中在：①plectin 作为 PTC 可成药靶点的 TCGA 整合亚型分析 + troglitazone（PPARγ）治疗潜力（High）；②MYH10/Myosin-10 经 FGF/FGFR1 轴促血管生成与恶性表型；③AGK::BRAF 融合激活 MAPK、促基因组不稳定并下调 NIS（解释儿童 PTC 肺转移 RAI 抵抗）；④RANKL 诱导 DNA 损伤经内质网应激/Hedgehog 驱动骨转移（preprint）。算法方向上 **LNM 预测模型持续拥挤**（本周新增 6 个列线图/radiomics 模型，全部单中心、非分子），再次确认 D-ml 不优先。空间组学维度 30 天增量为 0，经 90 天补跑确认属窗口边沿效应（6 篇空间文献均早于 2026-07-29）。

## English Abstract

This run uses OpenAlex as the primary source for a 30-day incremental surveillance of thyroid cancer (PTC/PTMC/FTC/MTC/ATC) covering invasion, lymph-node (LNM) and distant metastasis, recurrence, prognosis, molecular mechanisms, tumor immune microenvironment (TIME), single-cell and spatial omics, and ML/DL algorithmic methods. After deduplication, **88 unique records** were retrieved; **58 are in thyroid scope** and **30 excluded** (26 titles not naming thyroid, 4 non-oncologic thyroid topics); **25 multi-version record groups** were merged. **19 records are new vs the run #19 baseline** (5 published after run #19's 2026-08-21 cutoff = genuinely fresh this week; 14 are window-edge backfill from run #19's per-page=25 truncation, mainly the Gland Surgery nomogram batch, not new field progress). **4 in-scope preprints** (1 new this run).

No new evidence directly strengthens or weakens **D3 (APOE−/MGST1+ metabolic–immune stem-like metastatic subpopulation)** — D3 remains Strong (rubric 33, 20th consecutive confirmation). Genuinely fresh mechanism signals: (1) plectin as a druggable PTC target via TCGA integrative subtyping + troglitazone (PPARγ) therapeutic potential (High); (2) MYH10/Myosin-10 drives angiogenesis and malignant phenotypes through the FGF/FGFR1 axis; (3) AGK::BRAF fusion activates MAPK, promotes genomic instability and downregulates NIS (explaining RAI resistance in pediatric PTC with pulmonary mets); (4) RANKL-induced DNA damage drives bone metastasis via ER stress / Hedgehog (preprint). The algorithmic direction remains **crowded** (6 new LNM nomograms/radiomics models this week, all single-center, non-molecular), reconfirming D-ml as low priority. Spatial-omics had 0 new hits in 30 days; a 90-day supplement confirmed this is a window-edge effect (all 6 spatial papers predate 2026-07-29).

---

## 检索策略 (Search Strategy)

主源 OpenAlex（`api.openalex.org/works`），九路维度检索，过滤器 `title_and_abstract.search:<q>,from_publication_date:2026-07-29`，`sort=publication_date:desc`，每路 `per-page=25`。维度代码：MO=分子机制 / IM=免疫微环境 / SC=单细胞 / SP=空间组学 / AL=算法方法 / PR=预后转移 / ST=转移干性 / ME=代谢重编程。

| 路 | 维度 | OpenAlex 命中 | 取回 | 新条目 | 状态 |
|---|---|---:|---:|---:|---|
| a | MO/PR | 11 | 11 | 10 | OK |
| b | MO | 31 | 25 | 21 | OK |
| c | AL/PR | 15 | 15 | 14 | OK |
| d | IM | 20 | 20 | 9 | OK |
| e | SC | 8 | 8 | 5 | OK |
| f | SP | 6 | 6 | 1 | OK |
| g | PR | 36 | 25 | 18 | OK |
| h | ST | 6 | 6 | 2 | OK |
| i | ME | 13 | 13 | 8 | OK |

补充源约定：`paper-search-mcp` 本轮**未调用**——run #17/#18/#19 一致，主源 OpenAlex 已充分覆盖九路维度（且本机 NCBI 通道实测不可达、MCP 频繁 `not well-formed` 截断，按"失败即跳过、绝不阻塞主流程"处理）。High 相关新文献经 Crossref 校验 DOI 元数据、Unpaywall 解析 OA 状态（全部命中、标题一致、无幻影 DOI）。

窗口边沿处理：维度 f（空间组学）30 天增量 = 0 → 按协议单独补跑 `--days 90`（中间产物 `search_results_20260828_90day_supplement.json`，不覆盖基线），确认 6 篇空间文献均发表于 2026-05-30→2026-07-17，属更早窗口回填，非近 30 天真实新增。

---

## 纳入论文 (Included Papers)

> 本轮 19 条相对 run #19 基线新增文献。标注：★ = 确为本周新增（>2026-08-21）；△ = run #19 截断回填（2026-07-29–08-21）；[preprint] = 预印本。

1. ★ **Myosin-10 promotes angiogenesis and malignant phenotypes in thyroid cancer through functional association with the FGF/FGFR1 signaling axis.** *Scientific Reports* 2026-08-26. DOI:10.1038/s41598-026-67897-w. 中文要点：MYH10 经 FGF/FGFR1 轴促 TC 血管生成、迁移与侵袭，提供抗血管生成联用切入点。
2. ★ **The role of plectin as a druggable target in papillary thyroid carcinoma: therapeutic potential of troglitazone.** *Frontiers in Immunology* 2026-08-26. DOI:10.3389/fimmu.2026.1789251. 中文要点：TCGA 整合亚型分析锁定 plectin 为可成药靶点，troglitazone（PPARγ 激动剂）显示治疗潜力（High）。
3. ★ **AGK::BRAF fusion activates MAPK signaling, promotes genomic instability, and reduces NIS expression in thyroid cancer cells.** *Endocrine Oncology* 2026-08-26. DOI:10.1530/eo-25-0096. 中文要点：儿童 PTC 复发融合 AGK::BRAF 激活 MAPK、促基因组不稳定并下调 NIS，解释肺转移 RAI 抵抗。
4. ★ **Anaplastic thyroid cancer: genomic landscape, molecular drivers and novel therapeutics.** *Nature Reviews Endocrinology* 2026-08-25. PMID:42642459. DOI:10.1038/s41574-026-01293-2. 中文要点：ATC 基因组全景综述（BRAF/TP53/RAS/TERT），梳理靶向+免疫联合新疗法。
5. ★ **Radioiodine in Low-risk Differentiated Thyroid Cancer.** *Clinical Nuclear Medicine* 2026-08-24. PMID:42640623. DOI:10.1097/rlu.0000000000006676. 中文要点：低危 DTC RAI 降级治疗述评，呼应 2015/2025 ATA 分层去过度治疗趋势。
6. ★ **RNF123 Inhibits the Proliferation, Migration, and Invasion of Thyroid Cancer by Inhibiting KAT5-Mediated PSPC1 Histone Acetylation.** *Molecular Carcinogenesis* 2026-08-23. PMID:42633698. DOI:10.1002/mc.70168. 中文要点：E3 连接酶 RNF123 经抑制 KAT5 介导的 PSPC1 组蛋白乙酰化抑制 TC 进展。
7. ★ **Mutations of the DICER1 gene among children and adolescents with thyroid cancer: a systematic review.** *Pediatric Research* 2026-08-21. PMID:42629387. DOI:10.1038/s41390-026-05334-4. 中文要点：儿童/青少年 TC 中 DICER1 突变系统综述，强化儿科/AYA 亚群基因型。
8. ★ **Correction to "Single-Cell RNA Sequencing Reveals the Heterogeneity in Differentiation Trajectory and Tumor Microenvironment Leading to More Aggressive Phenotypes of Papillary Thyroid Cancer in Children and Young Adult Patients".** *Advanced Science* 2026-08-21. PMID:42627634. DOI:10.1002/advs.77252. 中文要点：儿童/青年 PTC 单细胞图谱的勘误声明，非新数据。
9. ★ **Longitudinal relationships of malnutrition risk, sleep disturbance, and fear of cancer recurrence in thyroid cancer patients: a cross-lagged panel model.** *Frontiers in Nutrition* 2026-08-21. DOI:10.3389/fnut.2026.1882241. 中文要点：PTC 术后营养/睡眠/复发恐惧的交叉滞后模型，属生存质量方向。
10. ★ **Integrative computational evaluation of tazemetostat for ARID1A-deficient anaplastic thyroid cancer via predicted polypharmacology and epigenetic target engagement.** *Clinical Epigenetics* 2026-08-20. DOI:10.1186/s13148-026-02222-w. 中文要点：计算预测 EZH2 抑制剂 tazemetostat 对 ARID1A 缺失 ATC 的多药理疗效。
11. ★ **Receptor Activator of Nuclear Factor-κB Ligand (RANKL)-Induced DNA Damage Promotes Thyroid Cancer Bone Metastasis via Endoplasmic Reticulum Stress and Hedgehog Signaling.** [preprint] *Research Square* 2026-08-20. DOI:10.21203/rs.3.rs-10596464/v1. 中文要点：RANKL 诱导 DNA 损伤经 ER 应激/Hh 驱动 TC 骨转移（preprint，证据降档）。
12. ★ **TERT Promoter Variants, Older Age, and Prognosis in Papillary Thyroid Carcinoma.** *JAMA Otolaryngology–Head & Neck Surgery* 2026-08-20. PMID:42623041. DOI:10.1001/jamaoto.2026.2273. 中文要点：TERT 启动子变异叠加高龄预测 PTC 不良预后，巩固 TERT 作为预后锚点。
13. ★ **Development and validation of a preoperative nomogram for predicting contralateral occult carcinoma and central lymph node metastasis in T1b-T2 stage papillary thyroid carcinoma.** *Frontiers in Endocrinology* 2026-08-19. DOI:10.3389/fendo.2026.1891976. 中文要点：T1b-T2 PTC 对侧隐匿癌+中央区 LNM 术前列线图（High，算法拥挤再确认）。
14. ★ **Long-term TSH suppression in metabolically unhealthy survivors of differentiated thyroid cancer: a cardiovascular perspective.** *Frontiers in Cardiovascular Medicine* 2026-08-19. DOI:10.3389/fcvm.2026.1924477. 中文要点：代谢不健康 DTC 存活者长期 TSH 抑制的心血管风险视角。
15. △ **Influencing factors and prediction model of ultrasound-based false-negative central lymph node metastasis in localized papillary thyroid carcinoma.** *Gland Surgery* 2026-08-01. DOI:10.21037/gs-2026-1-0129. 中文要点：局灶 PTC 超声假阴性中央区 LNM 预测模型。
16. △ **Development and internal validation of a multimodal MRI-FNAC radiomics-pathomics model for predicting cervical lymph node metastasis in papillary thyroid carcinoma.** *Gland Surgery* 2026-08-01. DOI:10.21037/gs-2026-0241. 中文要点：MRI-FNAC 多模态 radiomics-pathomics 预测颈部 LNM。
17. △ **Risk factors and nomogram for predicting central lymph node metastasis in papillary thyroid carcinoma based on gasless transaxillary endoscopic thyroidectomy.** *Gland Surgery* 2026-08-01. DOI:10.21037/gs-2026-0228. 中文要点：经腋无气腔镜 PTC 中央区 LNM 列线图。
18. △ **A simple four-variable nomogram integrating age, ACR-TIRADS, BRAF V600E and Bethesda cytology for predicting occult central lymph node metastasis in papillary thyroid microcarcinoma.** *Gland Surgery* 2026-08-01. DOI:10.21037/gs-2026-0352. 中文要点：PTMC 四变量（年龄/ACR-TIRADS/BRAF V600E/Bethesda） occult 中央区 LNM 列线图。
19. △ **Development and validation of a multivariable prediction model for lateral lymph node metastasis in papillary thyroid carcinoma.** *Gland Surgery* 2026-08-01. DOI:10.21037/gs-2026-0236. 中文要点：PTC 侧颈 LNM 多变量预测模型。

---

## 证据矩阵 (Evidence Matrix)

> 列：维度 / 相关性 / 预印本 / OA / 疾病人群 / 数据源 / 方法 / 终点 / 主要发现 / 验证 / 局限 / 提示缺口 / 后续方向。相关性 High=高、Med=中、Low=低；OA: gold/diamond/hybrid/green/closed。

| 论文 (Paper) | 维度 | 相关性 | 预印本 | OA | 疾病/人群 | 数据源 | 方法 | 终点 | 主要发现 | 验证 | 局限 | 缺口 | 后续方向 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Myosin-10/FGF-FGFR1 (10.1038/s41598-026-67897-w) | MO/SC | Med | 否 | gold | TC（PTC 细胞系+队列） | 细胞系+TCGA+IHC 队列 | 功能敲低/过表达、血管生成实验 | 血管生成、迁移/侵袭 | MYH10 经 FGF/FGFR1 轴促血管生成与恶性表型 | 体外+体内雏形 | 细胞系主导，因果未完全确立 | FGFR 抑制剂联用体内 LNM 模型 | FGFR 轴联合抗血管生成 |
| Plectin/troglitazone (10.3389/fimmu.2026.1789251) | MO/IM | **High** | 否 | gold | PTC | TCGA 整合（一致性聚类/CNV/突变） | 分子亚型+药物重定位 | 可成药靶点 | plectin 为 PTC 可成药靶点；troglitazone 显治疗潜力 | 计算+体外 | troglitazone 因肝毒已撤市，转化受限 | 用更安全 PPARγ 激动剂（pioglitazone）验证 | PPARγ 亚型靶向治疗 |
| AGK::BRAF 融合 (10.1530/eo-25-0096) | ST | Med | 否 | gold | 儿童 PTC（多灶+肺转移） | 甲状腺癌细胞系 | 融合表达/MAPK/基因组不稳定/NIS | MAPK 激活、NIS/RAI | 融合激活 MAPK、促基因组不稳定、下调 NIS | 细胞水平 | 儿童特异性、细胞系 | 与 RAI 反应临床关联 | NIS 丢失→RAI 抵抗标志物 |
| ATC 综述 (10.1038/s41574-026-01293-2) | MO/IM/ME | Low | 否 | closed | ATC | 文献综述 | 系统综述 | 驱动+疗法 | ATC 基因组全景与靶向/免疫联合 | 综述 | 非原始证据 | 组合策略前瞻验证 | BRAF+MEK+免疫三联 |
| RAI 低危 DTC (10.1097/rlu.0000000000006676) | PR | Low | 否 | closed | 低危 DTC | 述评 | 述评 | RAI 使用 | 低危 DTC RAI 降级去过度治疗 | 述评 | 非实证 | 前瞻性降级队列 | ATA 分层外推验证 |
| RNF123/KAT5-PSPC1 (10.1002/mc.70168) | MO | Low | 否 | closed | THCA | 配对瘤/癌旁 | E3 连接酶功能 | 增殖/迁移/侵袭 | RNF123 经抑制 PSPC1 乙酰化抑 TC | 体外+组织 | 机制单点 | 体内表型 | 表观调控靶点 |
| DICER1 儿童综述 (10.1038/s41390-026-05334-4) | MO | Low | 否 | hybrid | 儿童/青少年 TC | 系统综述 | 系统综述 | 基因型 | DICER1 突变谱汇总 | 综述 | 纳入异质 | 大型儿科队列 | 儿科/AYA 分子分层 |
| scRNA 勘误 (10.1002/advs.77252) | SC | Med | 否 | gold | 儿童/青年 PTC | 勘误 | 勘误声明 | — | 单细胞图谱勘误，非新数据 | — | 无新发现 | — | 引用原图需更新 |
| 营养/睡眠/恐惧 (10.3389/fnut.2026.1882241) | PR | Low | 否 | gold | PTC 术后 | 问卷面板 | 交叉滞后模型 | 生存质量 | 营养/睡眠/复发恐惧互作 | 面板模型 | 横断因果弱 | 干预研究 | 生存质量路径干预 |
| tazemetostat ARID1A ATC (10.1186/s13148-026-02222-w) | MO | Low | 否 | gold | ARID1A 缺失 ATC | 计算多药理 | 预测靶点结合 | 表观治疗 | EZH2 抑制剂对 ARID1A 缺失 ATC 多药理 | 计算 | 缺湿实验 | 体外/类器官验证 | SWI/SNF 缺陷表观治疗 |
| RANKL 骨转移 [preprint] (10.21203/rs.3.rs-10596464/v1) | MO | Low | **是** | green | TC 骨转移 | 细胞/动物 | RANKL/ER 应激/Hh | 骨转移 | RANKL 诱导 DNA 损伤经 ER 应激/Hh 驱动骨转移 | 临床前 | preprint，未同行评议 | 骨转移患者队列 | RANKL 抑制骨转移预防 |
| TERT+高龄预后 (10.1001/jamaoto.2026.2273) | PR | Med | 否 | green | PTC | 临床队列 | 预后建模 | OS/复发 | TERT 变异+高龄预测不良预后 | 独立队列 | 回顾性 | 外部多中心 | TERT 分层入组 |
| 对侧 occult 列线图 (10.3389/fendo.2026.1891976) | AL/PR | **High** | 否 | gold | T1b-T2 PTC | 单中心队列 | 列线图 | 对侧癌+CLNM | 术前预测对侧隐匿癌+中央区 LNM | 内部验证 | 单中心、非分子 | 外部验证 | 术式决策工具 |
| TSH 抑制 CV (10.3389/fcvm.2026.1924477) | PR | Med | 否 | gold | DTC 存活者 | 队列 | 心血管风险 | CV 事件 | 代谢不健康者长期 TSH 抑制 CV 风险 | 队列 | 混杂 | 前瞻性 | 代谢分层 TSH 目标 |
| US 假阴性 CLNM (10.21037/gs-2026-1-0129) | AL/PR | Med | 否 | diamond | 局灶 PTC | 单中心 | 预测模型 | 假阴性 CLNM | 超声假阴性 CLNM 影响因素模型 | 内部 | 单中心 | 多中心 | 超声+临床融合 |
| MRI-FNAC radiomics (10.21037/gs-2026-0241) | AL/PR | Med | 否 | diamond | PTC | 单中心 | 多模态 radiomics-pathomics | 颈部 LNM | MRI-FNAC 多模态预测颈部 LNM | 内部 | 单中心、非分子 | 外部 | 多模态融合 |
| 经腋腔镜 CLNM (10.21037/gs-2026-0228) | AL/PR | Med | 否 | diamond | PTC（经腋无气） | 单中心 | 列线图 | CLNM | 腔镜术式 CLNM 列线图 | 内部 | 术式偏倚 | 外部 | 术式适配模型 |
| PTMC 四变量 (10.21037/gs-2026-0352) | AL/PR | Med | 否 | diamond | PTMC | 单中心 | 列线图 | occult CLNM | 年龄/ACR-TIRADS/BRAF/Bethesda 预测 | 内部 | 单中心 | 外部 | 术前风险分层 |
| 侧颈 LNM (10.21037/gs-2026-0236) | AL/PR | Med | 否 | diamond | PTC | 单中心 | 多变量模型 | 侧颈 LNM | 侧颈 LNM 预测模型 | 内部 | 单中心 | 外部 | 侧颈决策 |

---

## 已知结论 (What Is Already Known)

> 下列为跨多轮（run #16–#19）稳定收敛、且被本轮证据相容（未反证）的结论。本轮新文献均不与之冲突。

1. **代谢–免疫耦合驱动 LNM（核心轴 1）**：MGST1 "Mito-high"/免疫冷亚型（AUC 0.833）、SHMT2、GLTC-LDHA、SOX12-YBX1-LDHA、SMDT1（线粒体 Ca²⁺/MCU）共同指向"代谢重编程→免疫抑制→淋巴结转移"链条。本轮 MYH10/FGF-FGFR1（血管生成层面）、AGK::BRAF→NIS（RAI 抵抗层面）属该轴的邻近机制补充，但未触及 APOE/MGST1 具体节点。
2. **干性样转移亚群（核心轴 2）**：APOE−/MGST1+ 代谢–免疫干性亚群、ISG15/KPNA2（ATC）、DLK1（MTC）、DLEU2-ELAVL1-RCC2 等。本轮无新增直接证据，AGK::BRAF 融合的"基因组不稳定+去分化倾向"属干性/去分化上游驱动但非该亚群本身。
3. **POSTN+ myCAF 空间图谱（核心轴 3）**：POSTN+ 肌成纤维细胞 CAF 空间图谱预测 LNM（~423k 细胞）。本轮无新空间证据（空间维度 30 天 = 0）。
4. **影像/多组学 AI 拥挤（核心轴 4）**：LLNM-Net、CLAM-WSI、多模态 DL 等均为非分子、单中心。本轮**新增 6 个 LNM 预测模型**（1 个 Frontiers + 5 个 Gland Surgery），再次确认该方向过度拥挤、增量价值低。
5. **BRAF V600E 与 PD-L1 meta 远处 vs LNM 解耦（核心轴 5）**：BRAF V600E meta（46k）预测淋巴结 OR1.38/复发 OR1.56，但不预测远处转移/死亡；PD-L1 meta 镜像一致。本轮 TERT 启动子+高龄预后（JAMA）巩固"TERT 为预后锚点"共识，与轴 5 相容。

---

## 未解问题 (What Remains Unclear)

- **D3 亚群的原代空间验证与体内靶向仍空缺**：APOE−/MGST1+ 代谢–免疫干性转移亚群虽在多轮被推荐，仍缺原代组织空间验证 + 体内靶向干预证据（本轮未补）。
- **RANKL/骨转移的机制闭环未闭合**：RANKL 骨转移 preprint 提供 DNA 损伤→ER 应激/Hh 机制，但缺临床骨转移队列与 RANKL 抑制的预防性证据。
- **plectin/PPARγ 转化可行性存疑**：troglitazone 因肝毒性已撤市，需换用更安全 PPARγ 激动剂（pioglitazone）并在体内验证。
- **AGK::BRAF 与 RAI 抵抗的临床因果**：NIS 下调在细胞水平证实，但缺"融合状态→RAI 反应"的真实世界关联。
- **算法模型外部泛化**：本轮 6 个 LNM 模型均单中心内部验证，跨人群/跨设备漂移未评估，临床效用存疑。

---

## 领域方法/数据局限 (Method/Data Limitations In The Field)

- **滚动窗口基线的"伪新增"**：run #19 以来各轮以单路 `per-page=25` + `sort=publication_date:desc` 检索，新文献在 30 天窗口富集、但更早文献被截断——导致早期文献在下一轮被重复标记为"新增"（本轮 14/19 属 run #19 截断回填）。建议将基线改为**累积语料**以避免重复计数。
- **PubMed 编目滞后**：近 30 天新文献多数无 PMID（本轮 19 篇中 12 篇 PMID 待编目），以 DOI 为主标识，符合 skill 规范。
- **单细胞/空间组学稀疏**：单细胞维度在范围仅 5、空间仅 3（本轮新 30 天空间 = 0），ATC/MTC 亚型与远处转移的空间证据尤其薄。
- **算法方向发表偏向单中心小样本**：本轮 LNM 预测模型集中发表于 Gland Surgery，均为单中心、回顾性、非分子，证据强度低。
- **预印本降档**：RANKL 骨转移等为 preprint，证据强度按规范降档。

---

## 候选未来方向 (Candidate Future Directions)

> 评分按 research-direction-rubric.md 七维（Novelty/Feasibility/Data/Validation/Clinical/Method/Overcrowding，各 1–5，满分 35）。28–35 = Strong。

| 方向 | 七维小计 | 评级 | 一句话依据 |
|---|---:|---|---|
| **D3** APOE−/MGST1+ 代谢–免疫干性转移亚群 | **33** | Strong | 连续 20 轮确认，无反证；APOE NCF1 免疫冷 niche（90d 回填 42217128）再补空间证据 |
| **D8** TREM2+ AHR–IDO1 免疫代谢检查点 | 30 | Strong | 体内免疫冷→热逆转缺口待补，本轮无新证据 |
| **D9** citrullination/PADI 侵袭程序 | 28 | Strong | SPP1–CD44 轴机制清晰，缺原代验证 |
| **D6** MTC 5-HT/NETs 肝转移 | 27 | Feasible | RANKL 骨转移 preprint 拓宽远处转移机制，但未触及 MTC 特异 |
| **D10** HT 自身免疫→LNM 保护自然对照 | 26 | Feasible | "免疫热/LNM 冷"自然对照维度，本轮无新证据 |
| **D-ml** 算法/影像 LNM 预测 | 20 | Exploratory | 本轮再+6 模型，严重拥挤，不优先 |

**D3 七维明细（维持 33）**：Novelty 5（代谢–免疫干性交叉界面仍未被定义）/ Feasibility 5（TCGA+GEO+已发表 scRNA 可用）/ Data 5（发现+验证队列可得）/ Validation 4（缺原代空间+体内靶向）/ Clinical 5（直接对应 LNM/RAI 抵抗终点）/ Method 5（清晰设计边界）/ Overcrowding 4（与 MGST1/APOE 单基因研究区分度好）。

**D3 研究问题 / 下一步**：以 APOE−MGST1+ 双阴性/阳性边界定义代谢–免疫干性转移亚群，用 TCGA+GEO 做发现、独立 scRNA/空间队列做验证，原代组织空间验证 + 类器官/PDX 体内靶向（如 PPARγ 激动剂或 IDO1 抑制）做功能闭环；主要风险为原代空间样本稀缺与靶向选择性，claim 边界须限定"代谢–免疫耦合的 LNM 驱动亚群"而非泛转移。

---

## 推荐下一步方向 (Recommended Next Direction)

**维持 D3（APOE−/MGST1+ 代谢–免疫干性转移亚群，rubric 33，Strong）作为首选方向**——本轮无反证，且 90 天补跑回库的 APOE NCF1 免疫冷 niche 论文（42217128）进一步支持"APOE 关联免疫抑制生态位"前提。

具体下一步（呼应本轮新信号）：
1. 将本轮 plectin/PPARγ 与 RANKL/骨转移两条 fresh 线索作为 D3 的**邻近机制候选**纳入讨论，但不升格为独立强方向（新颖度/验证不足）。
2. 优先补 D3 最核心缺口：**原代 PTC 组织空间验证 + 体内靶向**。可复用已发表的 POSTN+ myCAF 空间图谱（核心轴 3）与配对原发-LNM 单细胞图谱做 APOE−/MGST1+ 亚群共定位。
3. 修复检索基线为累积语料，避免滚动窗口重复计"新增"；并将 per-page 提至 50 以减截断回填噪声。

---

## 随访阅读清单 (Follow-Up Reading List)

- **AGK::BRAF fusion (10.1530/eo-25-0096)**：儿童 PTC 肺转移 RAI 抵抗的机制解释，值得结合 NIS 免疫组化做临床关联。
- **Plectin/troglitazone (10.3389/fimmu.2026.1789251)**：TCGA 亚型 + PPARγ 重定位，是 D3 邻近治疗线索，需跟踪 safer PPARγ 激动剂验证。
- **RANKL bone metastasis [preprint] (10.21203/rs.3.rs-10596464/v1)**：骨转移机制，待同行评议后纳入 D6 远处转移框架。
- **TERT+高龄预后 (10.1001/jamaoto.2026.2273)**：TERT 作为预后锚点的独立验证，巩固核心轴 5。
- **APOE NCF1 免疫冷 niche (10.1007/s12672-026-05061-6, 90d 回填)**：直接支撑 D3 的 APOE 关联免疫抑制生态位，建议纳入 D3 证据基底。

---

## 可复现性说明 (Reproducibility Notes)

- 检索日期 / Search date: 2026-08-28
- 主数据库 / Primary DB: OpenAlex REST API（`api.openalex.org/works`）；补充 Crossref（`api.crossref.org`）+ Unpaywall（`api.unpaywall.org`）
- 查询串 / Queries: 九路 a–i（见检索策略表）；过滤器 `title_and_abstract.search:<q>,from_publication_date:2026-07-29`；`sort=publication_date:desc`；`per-page=25`
- 去重规则 / Dedup: 标题归一化主键合并多版本；DOI/PMID/归一化标题三重判重；期刊补充材料（`Table 1_…`等）正则剔除
- 筛选规则 / Screening: 标题须点名甲状腺（PTC/PTMC/FTC/MTC/ATC/thyroid）且整体为肿瘤主题；顺带提及甲状腺的他病（乳腺/肺等 LNM、桥本、眼病）剔除
- 文件 / Files:
  - `literature_review_20260828_030000.md`（本报告）
  - `search_results_20260828_030000.json`（本轮带时间戳结果，已覆盖为 `search_results_latest.json` 作下轮基线）
  - `search_results_20260828_90day_supplement.json`（空间维度 90 天补跑中间产物，不覆盖基线）
- 新增判定 / New-detection: 相对 `search_results_latest.json`（= run #19 输出）按 PMID/DOI/归一化标题比较；**19 条新增中 5 条确为本周新增（>2026-08-21），14 条为 run #19 截断回填**。
- 通道状态 / Channel: 本机 NCBI eutils / pubmed.ncbi.nlm.nih.gov 不可达（HTTP 000），`paper-search-mcp` 不稳定（本轮未调用）；OpenAlex/Crossref/Unpaywall 直连稳定。
- 预印本 / Preprints: 本轮在范围预印本 4（新增 1：RANKL 骨转移），证据强度按规范降档。

---

## 与历史报告差异 (Delta vs Run #19 / 2026-08-21)

- **新增数**：run #19 = 15 条；run #20 = 19 条（相对 run #19 基线）。其中**确为本周新增 5 条**，其余 14 条为 run #19 单路 `per-page=25` 截断回填（主要为 Gland Surgery 列线图批次 + 若干预后/机制论著），非领域新进展——属 run #17/#19 已记录的"窗口漂移"现象。
- **各维度分布对比**（在范围，run #19 → run #20）：分子机制 28→24、预后转移 34→33、转移干性 4→4、免疫微环境 7→7、空间组学 7→3、单细胞 6→5、代谢重编程 8→9、算法方法 9→13。算法方法回升（+4，列线图批量回填）、空间组学回落（−4，30 天无新增）、单细胞略降（−1，窗口边沿）。
- **新信号（vs run #19）**：①plectin/PPARγ troglitazone PTC 亚型靶向（fresh High）；②MYH10/FGF-FGFR1 血管生成；③AGK::BRAF 融合→NIS/RAI 抵抗；④RANKL 骨转移 preprint；⑤5 个 Gland Surgery LNM 列线图（拥挤再确认）。
- **D3 跟踪**：**无变化**——本轮无直接强化/削弱 APOE−/MGST1+ 证据；90 天补跑回库的 APOE NCF1 免疫冷 niche（42217128）属更早文献回填，进一步支持 D3 前提但非本周新证据。D3 维持 Strong（rubric 33，连续第 20 轮确认）。
- **平台期判定**：否——5 条确为本周新增、领域真实活跃；此前 run #8–#16 连续零新增已确证为 PubMed 链路方法学假象（run #16 确诊）。本轮唯一"0 增量"为空间组学维度，经 90 天补跑确认属窗口边沿效应，非领域停滞。
- **建议**：将检索基线改为累积语料、per-page 提至 50，以消减滚动窗口"伪新增"并减少截断回填；空间组学与 ATC/MTC 亚型仍需拓宽预印本/专项源以突破稀疏。
