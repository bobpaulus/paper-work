# Literature Review: 甲状腺癌侵袭、淋巴结/远处转移、复发、预后及其分子机制、肿瘤免疫微环境、单细胞与空间组学、机器学习/深度学习算法 (Thyroid Cancer Metastasis, Recurrence, Prognosis, Mechanisms, TME, Single-Cell/Spatial Omics, ML/DL)

Date: 2026-08-06 (run #15)
Sources: PubMed (via paper-search-mcp `search_pubmed`)
Search window: all time, relevance-ranked (近 30 天优先、首轮放宽至全部；MCP 无日期过滤器，以相关性排序近似近期性)

---

## 中文摘要 (Chinese Abstract)

本次为 lit-review 自动监测的第 15 次运行。run #14 出现 PubMed MCP **全量检索失败**（9 路查询全部超时报错），故本运行重新实时执行全部 9 路互补检索（a–i）。检索过程中 MCP 出现间歇性服务端 XML 解析故障（`not well-formed (invalid token)`），经「并行批次→单条重试」策略，最终 **9 路查询全部成功返回**（c 于第 2 轮返回，a/b/d/e/f/g/h/i 经单条重试返回；f、h 因故障返回截断集，分别仅 7、3 篇）。

本运行共去重得到 **106 篇唯一文献 / 78 篇甲状腺相关在域文献 / 28 篇非甲状腺排除文献**。关键发现：**本月新增 2 篇此前基线（run #14 之 104 篇语料）未收录的甲状腺在域文献**，打破了自 run #7（+2）以来连续 8 次「零新增」的平台期：

1. **32421354** — *Metastatic propagation of thyroid cancer; organ tropism and major modulators.*（甲状腺癌转移播散与器官趋向性综述，2020）——强化 Axis 1（代谢重编程 + ECM + EMT 耦合驱动转移）。
2. **36974361** — *Molecular Testing Predicts Incomplete Response to Initial Therapy in Differentiated Thyroid Carcinoma…*（分子检测预测 DTC 初始治疗不完全应答的回顾性队列，2023）——强化 Axis 4 的临床风险分层维度（术前分子检测补充 ATA RSS）。

领域五大收敛结论（代谢–免疫耦合驱动 LNM；APOE−/MGST1+ 干性转移亚群；POSTN+ myCAF 空间图谱；拥挤的影像/多组学 AI；BRAF V600E 与 PD-L1 荟萃均提示「远处转移 vs 淋巴结转移解耦」）保持不变。推荐方向仍为 **D3——界定并靶向 APOE−/MGST1+ 代谢–免疫干性转移亚群**（rubric 总分 **32**，Strong），已连续 15 次确认为强候选。run #14 关键文献 37031273（GLTC-LDHA 代谢）与 41419184（BRAF V600E 4.6 万例荟萃）本月因相关性截断跌出 top-15，但仍保留于追踪语料，未被删除。

## English Abstract

This is run #15 of the scheduled thyroid-cancer literature monitor. Run #14 suffered a **full PubMed MCP outage** (all 9 queries failed), so this run re-executed all 9 complementary queries (a–i) live. The MCP exhibited intermittent server-side XML parse faults (`not well-formed (invalid token)`); using a "parallel-batch → solo-retry" strategy, **all 9 queries returned successfully** (c in round 2; a/b/d/e/f/g/h/i via solo retry; f and h returned truncated sets of 7 and 3 papers respectively due to transient faults).

After de-duplication: **106 unique / 78 thyroid in-scope / 28 non-thyroid excluded**. Key finding: **2 genuinely new in-scope thyroid papers not present in the run #14 baseline (104-record corpus) surfaced**, breaking the 8-run zero-new plateau (run #7 +2 → runs #8–#14 all 0):

1. **32421354** — *Metastatic propagation of thyroid cancer; organ tropism and major modulators.* (2020 review) — reinforces Axis 1 (metabolic reprogramming + ECM + EMT coupling drives metastasis).
2. **36974361** — *Molecular Testing Predicts Incomplete Response to Initial Therapy in Differentiated Thyroid Carcinoma…* (2023 cohort) — reinforces the clinical risk-stratification dimension of Axis 4 (preoperative molecular testing augments ATA RSS).

The five convergent axes (metabolic–immune coupling drives LNM; APOE−/MGST1+ stem-like metastatic subpopulation; POSTN+ myCAF spatial atlas; crowded imaging/multi-omics AI; BRAF V600E & PD-L1 meta-analyses both show distant-met vs LNM decoupling) are unchanged. Recommended direction remains **D3 — define & target the APOE−/MGST1+ metabolic–immune stem-like metastatic subpopulation** (rubric total **32**, Strong), confirmed for the 15th consecutive run. Two run #14 key papers (37031273 GLTC-LDHA; 41419184 BRAF V600E 46k meta) fell off the relevance top-15 this run but remain in the tracked corpus (not deleted).

---

## 检索策略 (Search Strategy)

| Source | Query | Filters | Results (this run) | Notes |
|---|---|---|---:|---|
| PubMed | a) `thyroid cancer lymph node metastasis biomarker gene signature` | relevance, max=15 | 15 | 单条重试成功；全部在基线语料内 |
| PubMed | b) `thyroid cancer invasion metastasis molecular mechanism` | relevance, max=15 | 15 | 单条重试成功；含非甲状腺排除项（乳腺癌/胃癌 MR 等）|
| PubMed | c) `thyroid cancer lymph node metastasis machine learning deep learning prediction model` | relevance, max=15 | 15 | 第 2 轮返回；与基线一致 |
| PubMed | d) `thyroid cancer metastasis tumor immune microenvironment` | relevance, max=15 | 15 | 单条重试成功；**新增 41057823（外泌体代谢重编程，甲状腺）** |
| PubMed | e) `thyroid cancer metastasis single cell RNA sequencing` | relevance, max=15 | 15 | 单条重试成功；全部在基线内 |
| PubMed | f) `thyroid cancer metastasis spatial transcriptomics spatial multi-omics` | relevance, max=15 | 7 (截断) | 单条重试成功但仅回 7 篇；41398964/41421038 为关键空间组学文献 |
| PubMed | g) `thyroid cancer prognosis recurrence distant metastasis risk model` | relevance, max=15 | 15 | 单条重试成功；**新增 36974361（DTC 分子检测）** |
| PubMed | h) `metastatic stemness subpopulation thyroid cancer` | relevance, max=15 | 3 (截断) | 单条重试成功但仅回 3 篇；39595993（DLK1 MTC 干性）在基线内 |
| PubMed | i) `thyroid cancer metabolic reprogramming metastasis` | relevance, max=15 | 15 | 单条重试成功；**新增 32421354（转移播散综述）**；41057823 复现 |

检索状态说明：本运行起始并行批次（9 路同发）全部触发 `not well-formed (invalid token)` 瞬态错误（与 run #14 全量故障同源）；改为单条顺序重试后 9 路全部成功。f、h 因瞬态故障返回截断集（7、3 篇），但其关键甲状腺文献（41398964、41421038、39595993）均已在基线语料内，不影响结论。

---

## 纳入论文 (Included Papers)

> 标注 ★ 为本运行相对 run #14 基线的 **2 篇新增在域文献**；其余为基线语料中支撑五大收敛轴的代表文献。

★ **32421354**. *Metastatic propagation of thyroid cancer; organ tropism and major modulators.* Future Oncol. 2020. DOI: 10.2217/fon-2019-0780.
  Author claim: 甲状腺癌转移播散受信号通路、细胞周期调控、代谢重编程、ECM 重塑、EMT、表观遗传、缺氧与细胞因子共同调控。
  Agent note: Medium 相关性；综述，强化 Axis 1 机制框架；器官趋向性（骨/肺/脑）机制仍薄弱。

★ **36974361**. *Molecular Testing Predicts Incomplete Response to Initial Therapy in Differentiated Thyroid Carcinoma Without Lateral Neck or Distant Metastasis at Presentation.* Thyroid. 2023. DOI: 10.1089/thy.2023.0060.
  Author claim: 945 例 DTC 中，分子检测使复发预测 c-statistic 提升 27%，与 ATA RSS 相当；肿瘤大小是唯一传统术前预测因子。
  Agent note: Medium 相关性；补充 Axis 4 的临床风险分层维度（术前分子检测），与影像 AI 方向不同、不重叠。

**42327722**. *MGST1 drives lymph node metastasis in papillary thyroid carcinoma via mitochondrial metabolic reprogramming and immune suppression.* Front Immunol. 2026. DOI: 10.3389/fimmu.2026.1848083.
  MGST1 被机器学习优先选为核心驱动，外部验证 AUC 0.833；单细胞轨迹定位至去分化终末「干性转移亚群」，药物抑制可逆转「免疫冷」表型。→ **支撑 Axis 1 + Axis 2（D3 蓝图核心）**。

**39810624**. *Single-cell RNA-sequencing and spatial transcriptomic analysis reveal a distinct population of APOE- cells yielding pathological lymph node metastasis in papillary thyroid cancer.* Clin Transl Med. 2025.
  APOE− 肿瘤细胞亚群与宫颈转移及不良预后强相关，经 ABCA1-LXR 轴抑制增殖/侵袭；建立 13-gene LNM 签名。→ **Axis 2（D3 核心）**。

**41480746 / 39829764**. *An integrated single-cell and spatial transcriptomic atlas of thyroid cancer progression identifies prognostic fibroblast subpopulations.* JCI Insight / bioRxiv. 2026.
  423,733 细胞 + 空间转录组，定义 POSTN+ myCAF 与 LNM、进展、预后相关。→ **Axis 3**。

**40750786**. *Explainable multimodal deep learning for predicting thyroid cancer lateral lymph node metastasis using ultrasound imaging.* Nat Commun. 2025.
  LLNM-Net 融合多模态，AUC 0.944，优于人类专家。→ **Axis 4（拥挤方向，rubric 低分）**。

**41877795**. *Development and validation of a machine learning model for predicting high-risk distant metastatic recurrence in differentiated thyroid cancer.* Front Med. 2026.
  XGBoost 预测 DTC 远处转移复发，验证集 AUC 0.88（374 例外部）。→ **Axis 4（临床可用的远处转移风险模型）**。

**41419184**. *BRAF V600E mutation in papillary thyroid cancer: …meta-analysis.* (46k 例荟萃) → 淋巴结 OR1.38 / 复发 OR1.56，但**不**预测远处转移/死亡。→ **Axis 5（远处 vs 淋巴结解耦）**。

**38272883**. *SHMT2 promotes papillary thyroid cancer metastasis through epigenetic activation of AKT signaling.* 2024 → 代谢–表观遗传耦合驱动 PTC 转移。
**40593465**. *The SOX12-YBX1-LDHA signaling axis drives metastasis in papillary thyroid carcinoma.* 2025 → 代谢（LDHA 糖酵解）+ TGF-β 驱动转移。
**37501099**. *ISG15 and ISGylation modulates cancer stem cell-like characteristics in promoting tumor growth of anaplastic thyroid carcinoma.* 2023 → ATC 干性（ISG15/KPNA2）。
**39595993**. *DLK1 Is Associated with Stemness Phenotype in Medullary Thyroid Carcinoma Cell Lines.* 2024 → MTC 干性（DLK1）。
**41398964**. *Integrated spatial metabolomics and transcriptomics reveal the molecular landscape of papillary thyroid cancer and its lymph node metastasis.* 2025 → 空间代谢+转录多组学，鉴定 5 个转移驱动代谢物。
**41421038**. *Cellular and molecular determinants of lymph node metastasis in papillary thyroid carcinoma: Integrated multi-omics profiling and machine learning models.* 2026 → FN1–SDC4 轴空间验证，多组学+ML 闭环（D3 蓝图）。
**39903533**. *5-HT orchestrates histone serotonylation and citrullination to drive NETs and liver metastasis.* 2025 → MTC 肝转移经 5-HT/NETs（fluoxetine/SERT 阻断）。→ 子方向 D6。

---

## 证据矩阵 (Evidence Matrix)

| Paper | PMID/DOI | Disease/Population | Data Source | Method | Endpoint | Main Finding | Validation | Limitations | Relevance | Gap Suggested | Future Direction |
|---|---|---|---|---|---|---|---|---|---|---|---|
| MGST1 drives LNM via mitochondrial reprogramming + immune suppression | 42327722 / 10.3389/fimmu.2026.1848083 | PTC | TCGA/GTEx + 独立临床队列 + scRNA-seq | 多组学 + 共识 ML + 功能/药理验证 | LNM / 免疫冷 | "Mito-high" 亚型 AUC 0.833；MGST1 定位于去分化终末干性亚群；Toxoflavin 抑制可促 IL-1β、抑 TGF-β1 | 独立外部验证 + 体内外 | 药理抑制剂尚处临床前 | High | 干性转移亚群缺乏可靶向标志物组合 | D3：界定 APOE−/MGST1+ 亚群并联合靶向 |
| APOE− subpopulation yields LNM | 39810624 / 10.1002/ctm2.70172 | 进展期 PTC | 手术标本 scRNA + 空间转录组 | 拟时序 + CellChat + 体内外 | 宫颈/LNM | APOE− 与进展期/转移相关，经 ABCA1-LXR 调控；13-gene LNM 签名 | 体内外功能验证 | 单中心、样本量受限 | High | APOE− 与 MGST1+ 是否同一连续谱系未明 | D3：联合 scRNA 界定代谢–免疫干性轴 |
| POSTN+ myCAF atlas | 41480746 / 10.1172/jci.insight.191990 | WDTC/ATC（含儿童/成人）| 423,733 细胞 + 空间转录组（28 瘤）| 整合 atlas + bulk 验证 | LNM / 进展 / 预后 | POSTN+ myCAF 紧邻侵袭性瘤细胞，与 LNM、预后相关 | 多中心、多组学 | 空间分辨率平台依赖 | High | myCAF 是否可直接成药未证 | 靶向 POSTN+ myCAF–瘤细胞互作 |
| LLNM-Net 多模态 DL | 40750786 / 10.1038/s41467-025-62042-z | PTC 侧颈 LNM | 29,615 患者 / 7 中心 | 双向注意力多模态 DL | 侧颈 LNM | AUC 0.944，优于专家 64.3% | 7 中心外部测试 | 非分子、纯影像、单中心偏多 | High | 与分子/单细胞机制脱节 | 与 D3 机制闭环（瓶颈）|
| XGBoost 远处转移复发 | 41877795 / 10.3389/fmed.2026.1790226 | DTC | 1,245 例（训练 871 / 验证 374）| LASSO + 6 种 ML | 远处转移复发 | AUC 0.88；低/中/高危复发率 1.7%/14.4%/64.1% | 外部验证集 | 回顾性、随访中位 72 月 | High | 仅临床/病理/分子变量，缺影像–组学融合 | 融合多组学提升远期远处转移预测 |
| BRAF V600E 荟萃 | 41419184 | PTC（46k 例）| 荟萃分析 | meta | 淋巴结/复发/远处 | 淋巴结 OR1.38、复发 OR1.56，**不**预测远处/死亡 | 大样本 | 异质性、回顾性为主 | High | 与远处转移解耦机制未明 | 分离 LNM 与远处转移驱动通路 |
| SHMT2 代谢–表观 | 38272883 / 10.1038/s41419-024-06476-1 | PTC | 组织 + 功能实验 | 代谢+表观验证 | 转移 | SHMT2 经 SAM 甲基化抑制 PTEN → 激活 AKT | 体内外 | 单一通路 | High | 与其他代谢驱动协同未明 | 代谢–表观联合干预 |
| SOX12-YBX1-LDHA | 40593465 / 10.1038/s41419-025-07797-5 | PTC | scRNA + bulk + CUT&Tag | 调控网络 | 转移 | SOX12→YBX1→LDHA 激活 TGF-β 驱动转移 | 临床样本验证 | 机制复杂 | High | 与 APOE−/MGST1 关系未连 | 并入 D3 代谢–免疫轴 |
| ISG15/KPNA2 ATC 干性 | 37501099 / 10.1186/s13046-023-02751-9 | ATC | scRNA + 功能实验 | 干性验证 | 生长/转移 | ISG15 ISGylation 稳定 KPNA2 维持干性 | 体内外 | ATC 罕见、样本少 | Medium | ATC 干性靶向难 | ATC 干性联合靶向 |
| DLK1 MTC 干性 | 39595993 / 10.3390/ijms252211924 | MTC 细胞系 | 细胞系 + 球体/外排 | 干性标志 | 进展/耐药 | DLK1+ 细胞干性标志更高 | 细胞实验 | 仅细胞系 | Medium | 体内验证缺 | MTC 干性靶向 |
| 空间代谢+转录多组学 | 41398964 / 10.1186/s12967-025-07566-0 | PTC + LNM | 空间代谢组 + 空间转录组 | 空间多组学 | LNM | 精氨酸–多胺轴、糖酵解、脂质代谢失调；5 个转移驱动代谢物 | TCGA + 斑马鱼 | 代谢物机制待深 | High | 转移驱动代谢物成药性未证 | 靶向 NAT8L/SVCT-2 等 |
| FN1–SDC4 多组学+ML | 41421038 / 10.1016/j.compbiolchem.2025.108857 | PTC LNM | scRNA + ST + bulk | 多组学 + RF | LNM | FN1–SDC4 轴空间验证；17-gene 签名 + RF 预测 | 空间验证 + 体外 | 单中心 | High | 与 APOE−/MGST1 整合缺 | D3 蓝图闭环 |
| 5-HT/NETs 肝转移 | 39903533 / 10.1172/JCI183544 | MTC/NEPC 肝转移 | 体内 + 药理 | 神经–免疫轴 | 肝转移 | 5-HT→NETs 促进肝转移；fluoxetine/SERT 阻断有效 | 体内 | 限 MTC/NE 亚型 | Medium | PTC 肝转移是否同轴未明 | D6：5-HT/NETs 轴靶向 |
| ★ 转移播散综述 | 32421354 / 10.2217/fon-2019-0780 | 甲状腺癌（综述）| 文献综述 | 叙述综述 | 转移播散/器官趋向 | 代谢重编程+ECM+EMT+表观+缺氧+细胞因子共控转移 | 无 | 非原发性 | Medium | 器官趋向机制薄弱 | 代谢–ECM–EMT 耦合靶向 |
| ★ DTC 分子检测 | 36974361 / 10.1089/thy.2023.0060 | DTC（无侧颈/远处转移）| 945 例回顾队列 | 逻辑回归 + c-stat | 不完全应答/复发 | 分子检测提升 c-stat 27%，≈ATA RSS | 内部 + 对标 RSS | 回顾性、随访短、MT 覆盖 46.6% | Medium | 术前分层算法未整合多组学 | 分子检测纳入术前分层 |

---

## 已知结论 (What Is Already Known)

1. **代谢–免疫耦合驱动淋巴结转移（Axis 1）。** 多条独立证据一致指向：MGST1（42327722「Mito-high」/免疫冷，外部 AUC 0.833）、SHMT2（38272883，代谢–表观激活 AKT）、GLTC-LDHA（37031273）、SOX12–YBX1–LDHA（40593465）以及空间多组学鉴定的转移驱动代谢物（41398964）共同刻画一个「代谢重编程 + 免疫抑制」的转移前表型。
2. **干性转移亚群是核心效应单元（Axis 2）。** APOE− 肿瘤细胞（39810624，经 ABCA1-LXR）与 MGST1 去分化终末「干性亚群」（42327722）高度收敛；ATC 中 ISG15/KPNA2（37501099）、MTC 中 DLK1（39595993）进一步支持「代谢–免疫干性」是转移的执行者。
3. **POSTN+ myCAF 空间图谱可预测 LNM（Axis 3）。** 423,733 细胞整合 atlas（41480746）明确 POSTN+ myCAF 紧邻侵袭性瘤细胞并与 LNM/预后相关。
4. **影像/多组学 AI 高度拥挤但临床可用（Axis 4）。** LLNM-Net（40750786，AUC 0.944）、CLAM-WSI（41237514）、多模态融合 DL（40771372/39682228/40778281/41061579）以及 XGBoost 远处转移复发模型（41877795，AUC 0.88）显示强大判别力，但多为单中心、非分子、缺外部验证。
5. **BRAF V600E 与 PD-L1 荟萃共同揭示「远处转移 vs 淋巴结转移解耦」（Axis 5）。** BRAF V600E 荟萃（41419184，4.6 万例）提示淋巴结 OR1.38 / 复发 OR1.56，但**不**预测远处转移/死亡；PD-L1 荟萃（41510756）镜像一致。即 LNM 与远处转移由不同机制驱动。

## 尚未明确 (What Remains Unclear)

- APOE− 与 MGST1+ 是否为同一连续去分化谱系的两个状态，还是平行亚群——二者在单细胞层面的整合尚未完成。
- 「代谢–免疫干性」亚群的可靶向标志物组合（而非单基因）仍缺；MGST1 抑制（Toxoflavin）仅临床前。
- 远处转移（Axle 5 解耦）的真实驱动通路 vs LNM 驱动通路尚未被同一队列同时剖析。
- 器官趋向性（骨/肺/脑）机制（32421354 强调）仍是最薄弱一环；MTC 肝转移 5-HT/NETs 轴（39903533）是否适用于 PTC 未证。
- 空间多组学（41398964、41421038、41480746）虽提供图谱，但「图谱→可成药靶点」的闭环仅 FN1–SDC4（41421038）迈出一步。

## 领域方法/数据局限 (Method/Data Limitations In The Field)

- **公共数据复用与批次效应**：TCGA/GTEx/GEO 被几乎所有基因签名与 ML 研究复用；scRNA/空间平台（10x Visium、Slide-seq、Stereo-seq）异质导致跨研究不可比。
- **外部验证稀缺**：Axis 4 的 DL 模型多为单中心，外部测试集小；rubric 中 D-ml 因极端拥挤被打低分。
- **亚型分层缺失**：PTC/FTC/MTC/ATC 常被合并分析，干性与代谢驱动在 ATC/MTC 中证据最弱（样本少）。
- **终点稀疏**：远处转移与复发为稀疏终点，多数预后模型依赖 LNM 这一替代终点。
- **湿实验验证不足**：大量计算发现的靶点（MGST1、SHMT2、SOX12 轴）仅少数进入体内外功能验证，临床前→临床鸿沟大。
- **MCP 检索可靠性**：本自动监测依赖的 `search_pubmed` MCP 在近两轮（#13 部分、#14 全量、#15 间歇性）频繁出现瞬态 XML 故障，需改为「单条重试」并考虑接入 bioRxiv/arXiv + cBioPortal/DepMap 以突破平台期。

## 候选未来方向 (Candidate Future Directions)

| Direction | Rationale | Feasibility | Required Data | Validation Plan | Main Risk | Claim Boundary |
|---|---|---:|---|---|---|---|
| **D3 — APOE−/MGST1+ 代谢–免疫干性转移亚群** | APOE−(39810624) 与 MGST1+(42327722) 双独立证据收敛于「干性+代谢+免疫冷」；FN1–SDC4(41421038) 提供空间闭环蓝图 | 高（公共 scRNA/空间数据 + 已有细胞系）| TCGA THCA + 41480746/39810624/41398964 的 scRNA&ST；可选 cBioPortal/DepMap | 独立队列验证亚群标志物；体内外功能 + 药理（Toxoflavin 类）| 亚群异质性导致标志物泛化难 | 仅定义与靶向「代谢–免疫干性」转移前体，非治愈性 |
| D-new — 空间代谢驱动转移（41398964 延伸）| 空间多组学鉴定 5 个转移驱动代谢物，机制新颖 | 中（需空间代谢平台）| 空间代谢+转录配对队列 | 代谢物 knockdown + 斑马鱼 | 代谢物成药性未证 | 机制探索，非临床终点 |
| D6 — 5-HT/NETs 轴（MTC 肝转移）| 39903533 显示 fluoxetine/SERT 可阻断，临床转化直接 | 中 | MTC + 限肝转移队列 | 前瞻药理验证 | 仅 MTC/NE 亚型，PTC 适用性未证 | 限 MTC/神经内分泌亚型肝转移 |
| D7 — 线粒体 Ca2+/MCU（SMDT1 42510113）| 线粒体钙调控 OXPHOS 与 CD8+T/NK 浸润 | 中 | PTC 配对 scRNA+代谢 | 功能 + 免疫浸润验证 | 与 MGST1 轴关系未明 | 已并入 D3，不单独 |
| D-ml — 影像/多组学 AI | 判别式强（AUC 0.88–0.944）| 高 | 多中心影像+组学 | 外部验证 | **极端拥挤**，增量价值低 | 仅风险分层，非机制 |

**Rubric 七维评分（D3）**：Novelty 5 / Feasibility 5 / Data availability 5 / Validation strength 4 / Clinical relevance 5 / Method rigor 4 / Overcrowding risk 4 → **总分 32（Strong，连续 15 次确认）**。

## 推荐下一步方向 (Recommended Next Direction)

**D3 — 界定并靶向 APOE−/MGST1+ 代谢–免疫干性转移亚群。** 它是唯一同时被单细胞（39810624 APOE−）、空间多组学（42327722 MGST1+ 干性终末态、41480746 POSTN+ myCAF 生态位）、代谢（38272883/40593465）与空间闭环（41421038 FN1–SDC4）共同支撑的方向，且 rubric 持续 32 分（Strong）。

**首步具体动作**：① 用 41480746 + 39810624 + 41398964 的公开 scRNA/空间数据，构建「APOE− ∩ MGST1+ ∩ 去分化轨迹终末」联合标志物的可复现流程；② 在独立 PTC 队列（TCGA THCA + 机构队列）验证该亚群对 LNM/远处转移的预测力；③ 以 Toxoflavin 类 MGST1 抑制剂做体内外功能确认，并检测「免疫冷→免疫热」逆转。

## 随访阅读清单 (Follow-Up Reading List)

- **32421354**（★新增）：甲状腺癌转移播散与器官趋向性总览——补强机制框架的起点。
- **36974361**（★新增）：DTC 术前分子检测风险分层——连接 Axis 4 临床转化。
- **42327722**：MGST1 线粒体代谢–免疫抑制轴心，D3 核心文献，优先精读方法。
- **39810624 + 41480746**：APOE− 与 POSTN+ myCAF 单细胞/空间基准，构建 D3 亚群流程的必需数据来源。
- **41421038**：FN1–SDC4 多组学+ML 空间闭环，D3 蓝图的「机制→靶点→模型」示范。
- **39903533**：MTC 5-HT/NETs 肝转移，D6 子方向，若拓展 MTC 必读。
- **41510756**（PD-L1 荟萃）：与 41419184 共证「远处 vs 淋巴结解耦」，理解 Axis 5 必需。

## 可复现性说明 (Reproducibility Notes)

- Search date: 2026-08-06（run #15）。
- Databases: PubMed（paper-search-mcp `search_pubmed`）。
- Query strings: a–i 九路（见检索策略表）。
- Filters: `max_results=15`, `sort=relevance`；MCP 无日期过滤器，近期性以相关性排序近似。
- Deduplication rule: 按 PMID 去重；同一文献跨多路命中仅计一次。
- Screening rule: 剔除非甲状腺肿瘤（乳腺癌/TNBC/胃癌/结直肠癌/泛癌/HCC/胰腺癌等）与纯临床流行病学（如 41817109 RAI 人群研究、36704213 TNBC）；保留 PTC/FTC/MTC/ATC 及甲状腺机制/免疫/单细胞/空间/算法/干性/代谢文献。
- Files saved: `lit_review/literature_review_20260806_030247.md`（本报告）；`lit_review/search_results_latest.json`（106 唯一 / 78 在域 / 28 排除，含 `new_vs_run14=[32421354,36974361]` 与 `retrieval_status`）；`lit_review/_build_run15.py`（构建脚本）。
- MCP 可靠性注记：本运行起始并行批次全失败，单条重试后 9 路全成功；f、h 因瞬态故障返回截断集。建议后续接入 bioRxiv/arXiv 预印本与 cBioPortal/DepMap，并将日级频率降至周级以突破平台期。

---

## 与 run #14 的差异（本月信号变化）(Delta vs run #14)

- **新增在域文献（突破 8 轮零新增平台期）**：2 篇 —— 32421354（转移播散综述，MO+PR）、36974361（DTC 分子检测预后，PR+MO）。
- **语料规模**：104 → **106 唯一 / 78 在域 / 28 排除**（run #14 为 104/76/28）。
- **维度分布变化**（在域，多标签）：分子机制 38→**40**、预后转移 31→**33**、算法方法 18、代谢重编程 11、免疫微环境 14、单细胞 12、空间组学 7、转移干性 5（后六项不变）。
- **相关性**：High 37 / Medium 29→**31** / Low 10。
- **关键文献跌出 top-15（截断，仍保留语料）**：37031273（GLTC-LDHA 代谢）、41419184（BRAF V600E 4.6 万例荟萃）——因本月对应查询（b/i/g）相关性重排，非丢失。
- **收敛结论**：五大轴与本推荐方向 D3（rubric 32）均**不变**，连续 15 次确认。
- **方法学提示**：`search_pubmed` MCP 在 #13–#15 持续不稳定（瞬态 XML 故障），强烈建议扩展数据源（预印本 + cBioPortal/DepMap）并降低监测频率至周级。
