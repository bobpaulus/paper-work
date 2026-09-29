# Literature Review: 甲状腺癌侵袭·转移·复发·预后与分子机制 / 免疫微环境 / 单细胞与空间组学 / 机器学习方法
# Thyroid Cancer (PTC/PTMC/FTC/MTC/ATC): Invasion, LNM & Distant Metastasis, Recurrence, Prognosis — Molecular Mechanisms, Tumor Immune Microenvironment, Single-Cell & Spatial Omics, ML/DL Methods

Date: 2026-09-25
Run: #25（自动化文献监测 / automated surveillance run #25）
Sources: OpenAlex（主源 / primary）、Europe PMC（第二通道 / secondary, 6 路）、Crossref（DOI 元数据校验）、Unpaywall（OA 解析）、OpenAlex 定向基因深挖（第三通道 / third, 7 路）
Search window: 主窗口 30 d（2026-08-26 → 2026-09-25）；90 d 补检（2026-06-27 → 2026-09-25）；Europe PMC `PUB_YEAR:2026`；定向深挖 2026-01-01 起
基线对比 / Baseline: `search_results_latest.json`（Run #24，245 条）

---

## 中文摘要 / 摘要

**本轮（Run #25）三通道并行，去重后唯一新增 52 条**（OpenAlex 主检 18 + Europe PMC 补检 22 + 定向基因深挖 12），累积基线由 **245 → 297 条**。相关性分布 High 12 / Medium 24 / Low 16；本轮**严格预印本 0 条**（两条相关预印本经查已在基线中）。维度分布：预后转移 25、算法方法 15、代谢重编程 17、分子机制 13、免疫微环境 10、转移干性 4、单细胞 3、空间组学 1。

**最重要的变化是持续跟踪方向 D3 在连续 24 轮后首次出现第二次实质性重构。** 本轮通过定向基因深挖通道捕获两条直接锚定证据：①**MGST1 经线粒体代谢重编程 + 免疫抑制驱动 PTC 淋巴结转移**（*Front Immunol* 2026-06-04, PMID 42327722, gold；多组学 + 独立临床队列 + scRNA + 共识机器学习 + 基因/药理验证）——这是 24 轮监测以来 **MGST1 首次获得直接功能证据**，此前一直标注为"位置未检验"；②**APOE 经 PINK1/Parkin 线粒体自噬促进 PTC 进展**（*Transl Cancer Res* 2026-08-01, PMID 42724858, diamond）。两者合起来**推翻了原假设的互斥结构**：APOE 并非"阴性背景标志"而是促癌因子，MGST1 并非"APOE− 亚群的定义基因"而是独立的 LNM 驱动因子。因此 D3 由 D3′（APOE⁺–CD8⁺ Tex 生态位）进一步重构为 **D3″：APOE×MGST1 双代谢–免疫轴的共定位与功能解耦**，rubric 29 → **31**。

**第二条主线是代谢–免疫轴（ME × IM）成为本轮最密集的证据簇**（ME 17 条 + IM 10 条）。其中三条达到因果/准因果强度：**GPI–O-GlcNAc–THBS1 介导 ATC 髓系免疫抑制**（*Cancer Lett*, PMID 42248319）、**cGAS–STING 抑制驱动 ATC 免疫逃逸**（*Thyroid*, PMID 42644464，三模型 + scRNA）、**PHGDH 丝氨酸代谢重编程介导 dabrafenib 耐药**（*Cell Death Discov*, 10.1038/s41420-026-03293-7）。据此 **D9（SPP1⁺ TAM）提升至 33**（ATC scRNA 直接证据，10.1186/s12885-026-16648-1，gold）、**D12（铁死亡/新型程序性死亡）由 27 升至 29**（HIF-1α–ACSL4 轴使它由"泛癌共性"转为"甲状腺特异机制"）。

**第三条主线是算法方法（AL，15 条）出现罕见的"方法学自省"证据**：*Gland Surgery* 三中心研究正面检验了 B 超影像组学模型的**临床可移植性、校准漂移与本地更新**（PMID 42591955），把 D13 长期标注的最大风险（外部验证缺失）变成了领域公开讨论的对象，D13 26 → 27。

**通道方法学是本轮第二项重要产出**：Europe PMC 由 3 路扩至 6 路（新增 ME/AL/ST）贡献 22 条（42%）；新增的**定向基因深挖通道（7 路）贡献仅 12 条，却独占了本轮 3 条最重要的原发证据**（MGST1、APOE、SPP1⁺ ATC）。这直接证明 `oa_search.py` 的九路布尔矩阵对**"基因名锚定"型文献存在系统性漏检**——这类文献标题常不含 metastasis/progression 等检索词。建议自下轮起把定向基因查询固化为常规第三通道。

**空间组学（SP）本轮近乎空窗（仅 1 条综述）**，但结合基线中已有的 *Spatial Transcriptomics in Thyroid Cancer* PRISMA 系统综述（preprint, 10.20944/preprints202608.0302.v1）与 Run #23/#24 连续两轮 90 d 补检，判定为**前序轮次已充分吸收，而非领域停滞**。

---

## English Abstract

Run #25 executed a three-channel retrieval (OpenAlex primary 30 d/90 d, Europe PMC six-query cross-check, and a newly introduced targeted-gene deep-dive channel). After deduplication, **52 unique new records** were added (OpenAlex 18, Europe PMC 22, deep-dive 12), expanding the cumulative baseline from **245 to 297**. Relevance: High 12 / Medium 24 / Low 16. Strict preprints: 0 (two relevant preprints were already in the baseline). Dimension distribution: PR 25, AL 15, ME 17, MO 13, IM 10, ST 4, SC 3, SP 1.

The decisive event is the **second substantive reconstruction of tracking direction D3 after 24 consecutive rounds**. The targeted-gene channel captured two directly anchoring papers: **MGST1 drives PTC lymph-node metastasis via mitochondrial metabolic reprogramming and immune suppression** (*Front Immunol*, PMID 42327722, gold; TCGA/GTEx + independent clinical cohort + scRNA + consensus ML + genetic/pharmacological validation) — the **first direct functional evidence for MGST1 in 24 rounds** — and **APOE promotes PTC progression via PINK1/Parkin-mediated mitophagy** (*Transl Cancer Res*, PMID 42724858). Together they invalidate the original mutually-exclusive formulation: APOE is not a negative background marker but a tumour promoter, and MGST1 is not a defining gene of an "APOE−" subpopulation but an independent LNM driver. D3 is therefore reconstructed from D3′ into **D3″: co-localization and functional decoupling of the APOE × MGST1 dual metabolic–immune axis**, rubric 29 → **31**.

The second thread is that the **metabolic–immune axis is now the densest evidence cluster** (ME 17 + IM 10), with three near-causal additions: GPI–O-GlcNAc–THBS1 myeloid immunosuppression in ATC (*Cancer Lett*, PMID 42248319), suppressed cGAS–STING DNA sensing driving ATC immune evasion (*Thyroid*, PMID 42644464), and PHGDH-dependent serine metabolism underlying dabrafenib resistance (*Cell Death Discov*, 10.1038/s41420-026-03293-7). Consequently **D9 (SPP1⁺ TAM) rises to 33** on new ATC scRNA evidence (10.1186/s12885-026-16648-1, gold), and **D12 (ferroptosis/novel programmed cell death) rises 27 → 29** as the HIF-1α–ACSL4 axis converts it from a pan-cancer generic to a thyroid-specific mechanism.

The third thread is a rare piece of **methodological self-reflection in the ML/AL literature**: a three-centre *Gland Surgery* study explicitly tests clinical transportability, calibration drift, and local updating of a B-mode ultrasound radiomics model (PMID 42591955), converting D13's long-flagged risk into an openly discussed field problem; D13 26 → 27.

At the channel level, the new **targeted-gene deep-dive channel contributed only 12 records but captured all three of the round's most important primary papers**, demonstrating that the nine-query boolean matrix in `oa_search.py` systematically misses gene-anchored papers whose titles lack terms such as metastasis or progression. Spatial omics was nearly empty this round (1 review), judged to be saturation from prior 90-day and Europe PMC sweeps rather than a field plateau.

---

## 1. 检索策略 / Search Strategy

| Source / 通道 | Query / 查询 | Filters / 过滤 | Hits | Returned | Kept/New | Notes / 备注 |
|---|---|---|---:|---:|---:|---|
| **OpenAlex** `a` | `thyroid AND (metastasis OR metastatic OR "lymph node") AND (biomarker OR signature)` | 30 d, `sort=publication_date:desc`, per-page 25 | 23 | 23 | 23 | MO/PR |
| **OpenAlex** `b` | `thyroid AND (invasion OR metastasis) AND (mechanism OR pathway OR EMT)` | 30 d | 52 | 25 | 19 | MO（命中上限截断） |
| **OpenAlex** `c` | `thyroid AND (metastasis OR "lymph node") AND ("machine learning" OR "deep learning" OR radiomics OR nomogram)` | 30 d | 21 | 21 | 14 | AL/PR |
| **OpenAlex** `d` | `thyroid AND (metastasis OR metastatic) AND ("immune microenvironment" OR macrophage OR "T cell")` | 30 d | 24 | 24 | 9 | IM |
| **OpenAlex** `e` | `thyroid AND (metastasis OR metastatic OR heterogeneity) AND ("single-cell" OR scRNA-seq)` | 30 d | 10 | 10 | 5 | SC |
| **OpenAlex** `f` | `thyroid AND ("spatial transcriptomic" OR Visium OR "spatial omics")` | 30 d | 11 | 11 | 4 | SP |
| **OpenAlex** `g` | `thyroid AND (prognosis OR recurrence OR "distant metastasis") AND ("risk model" OR survival OR nomogram)` | 30 d | 52 | 25 | 17 | PR（命中上限截断） |
| **OpenAlex** `h` | `thyroid AND (metastasis OR metastatic) AND ("cancer stem cell" OR stemness OR dedifferentiation)` | 30 d | 8 | 8 | 3 | ST |
| **OpenAlex** `i` | `thyroid AND (metastasis OR metastatic OR progression) AND ("metabolic reprogramming" OR glycolysis OR ferroptosis OR OXPHOS)` | 30 d | 7 | 7 | 4 | ME |
| **OpenAlex 合计（30 d）** | 九路 | ≥2026-08-26 | **208** | **154** | 唯一 98 / 在范围 69 / 新增 15 | 合并多版本 29 组 |
| **OpenAlex 90 d 补检** | 同上九路 | ≥2026-06-27, per-page 50 | **610** | **364** | 唯一 240 / 在范围 171 / 新增 19 | 与 30 d 重叠 4 条 |
| **Europe PMC** SC | `TITLE:"thyroid" AND (TITLE:"single-cell"/"single cell" OR ABSTRACT:"scRNA-seq") AND PUB_YEAR:2026` | `sort=P_PDATE_D desc`, ps=50 | 50 | 50 | 候选 25 → 筛入 0 | 本路全部为基线已有或非甲状腺癌主题 |
| **Europe PMC** SP | `TITLE:"thyroid" AND (TITLE:"spatial" OR ABSTRACT:"spatial transcriptomics")` | 同上 | 35 | 35 | 候选 17 → 筛入 1 | 含 1 条撤回声明，已剔除 |
| **Europe PMC** IM | `TITLE:"thyroid" AND (TITLE:"tumor microenvironment"/"macrophage")` | 同上 | 24 | 24 | 候选 15 → 筛入 0 | 全部已在基线 |
| **Europe PMC** ME | `TITLE:"thyroid" AND (TITLE:"metabolic"/"metabolism"/"ferroptosis"/"glycolysis")` | 同上 | 160 | 50 | 候选 42 → 筛入 11 | **本轮贡献最大一路** |
| **Europe PMC** AL | `TITLE:"thyroid" AND (TITLE:"machine learning"/"deep learning"/"radiomics"/"nomogram")` | 同上 | 231 | 50 | 候选 35 → 筛入 9 | — |
| **Europe PMC** ST | `TITLE:"thyroid" AND (TITLE:"stemness"/"dedifferentiation"/"cancer stem cell")` | 同上 | 19 | 19 | 候选 12 → 筛入 1 | 1 条为 Correction，已剔除 |
| **Europe PMC 合计** | 六路 | PUB_YEAR:2026 | **519** | — | 候选 146 → **人工筛入 22** | 剔除 124（甲状腺激素/代谢病/甲状腺眼病/动物模型/良性结节/撤回与书信） |
| **定向深挖** D3-MGST1 | `thyroid AND MGST1` | 2026-01-01 起 | 1 | 1 | **1** ⭐ | 捕获本轮最重要证据 |
| **定向深挖** D3-APOE | `thyroid AND (APOE OR "apolipoprotein E")` | 同上 | 19 | 19 | 2 ⭐ | 含 APOE–PINK1/Parkin |
| **定向深挖** D3-lipid | `("thyroid cancer" OR "thyroid carcinoma") AND ("lipid metabolism"/"metabolic reprogramming")` | 同上 | 73 | 30 | 3 | figshare 补充材料批量剔除 |
| **定向深挖** D3-immunomet | `thyroid carcinoma AND ("immunometabolism"/"metabolic-immune")` | 同上 | 2 | 2 | 2 ⭐ | MGST1 + GPI |
| **定向深挖** SP-review | `thyroid AND ("spatial transcriptomics" OR "spatial omics")` | 同上 | 59 | 30 | 1 | — |
| **定向深挖** SC-atlas | `thyroid carcinoma AND ("single-cell"/"single nucleus"/scRNA-seq)` | 同上 | 159 | 30 | 3 ⭐ | SPP1⁺ TAM、cGAS–STING |
| **定向深挖** ME-ferro | `thyroid carcinoma/ATC AND (ferroptosis OR cuproptosis)` | 同上 | 85 | 30 | 4 | 含 figshare 补充材料，已剔除 |
| **定向深挖 合计** | 七路 | 2026-01-01 起 | **398** | — | **筛入 12** | 另 5 条已在基线 |
| **Crossref / Unpaywall** | 10 条 High 条目 DOI 元数据 + OA 解析 | — | — | — | **10/10 + 10/10 成功** | 通道健康 |
| **NCBI eutils / PubMed** | — | — | — | — | **未使用** | 本机网络不可达（HTTP 000），按 `RETRIEVAL_ENVIRONMENT.md` 禁止直连 |
| **paper-search-mcp** | — | — | — | — | **未调用** | 本会话未连接该 MCP |

**检索口径合计 / Grand total**：四通道累计命中 **1,735** 次（OpenAlex 818 + Europe PMC 519 + 定向深挖 398）→ 取回 518 → 去重后唯一记录 **338**（OpenAlex 窗口内）→ 在范围 **240** → **本轮去重后唯一新增 52**。

---

## 2. 纳入论文 / Included Papers

本轮新增 **52 条**。下面对 **High（12 条）** 逐条给出作者主张与本方判断；Medium/Low 以要点形式附后。

### 2.1 High 相关性（12 条）

**H1. MGST1 drives lymph node metastasis in papillary thyroid carcinoma via mitochondrial metabolic reprogramming and immune suppression**
*Frontiers in Immunology*, 2026-06-04. **PMID 42327722**. DOI **10.3389/fimmu.2026.1848083**. OA: gold. 维度 ME/IM/PR.
> Author claim: 整合 TCGA/GTEx 转录组、大规模独立临床队列与 scRNA-seq 构建多组学发现框架，用共识机器学习筛出核心驱动基因，并经基因操作与药理学实验验证；T 细胞耗竭伴随 Treg 富集，巨噬细胞区室同步重塑。
> Agent note: ⭐ **本轮最重要证据，也是 24 轮监测以来 MGST1 的首次直接功能锚定**。方法链完整（生物信息学 → 独立队列 → scRNA → 机器学习 → 湿实验验证）。但它**并未**在 APOE− 背景下定义亚群，也未做空间共定位——原 D3 假设的"APOE−/MGST1⁺"互斥结构在本文中无直接支持。

**H2. Apolipoprotein E promotes papillary thyroid carcinoma progression by activating PINK1/Parkin-mediated mitophagy**
*Translational Cancer Research*, 2026-08-01. **PMID 42724858**. DOI **10.21037/tcr-2026-0796**. OA: diamond. 维度 MO/ME.
> Author claim: APOE 在 PTC 中表达升高，经 TCGA/GEO 整合分析与 PTC 组织 IHC 验证；机制上通过激活 PINK1/Parkin 线粒体自噬促进肿瘤进展。
> Agent note: ⭐ 与 Run #24 的 APOE–NCF1 空间生态位证据**方向一致（APOE 促癌）**，进一步**否定**了原 D3 假设中"APOE 低表达 = 干性亚群标志"的设定。样本量与功能挽救实验强度需核对原文。

**H3. GPI promotes immunosuppression in anaplastic thyroid carcinoma via O-GlcNAcylated THBS1-mediated myeloid cell crosstalk**
*Cancer Letters*, 2026-06-05. **PMID 42248319**. DOI **10.1016/j.canlet.2026.218650**. OA: closed. 维度 ME/IM.
> Author claim: 糖酵解酶 GPI 通过 O-GlcNAc 修饰的 THBS1 介导髓系细胞间通讯，驱动 ATC 免疫抑制。
> Agent note: **代谢酶 → 翻译后修饰 → 髓系免疫抑制**的完整链路，是"代谢–免疫轴"在本轮机制上最完整的一条。OA 闭源，需机构访问获取全文核实实验细节。

**H4. Single-cell RNA-seq reveals SPP1+ tumor-associated macrophage population associated with collagen remodeling in anaplastic thyroid cancer**
*BMC Cancer*, 2026-08-01. DOI **10.1186/s12885-026-16648-1**. PMID 待编目. OA: gold. 维度 SC/IM.
> Author claim: 联合公共 scRNA-seq 与 bulk 转录组，发现 ATC 中显著髓系富集与间充质样恶性上皮态占主导，SPP1⁺ TAM 与胶原高表达程序相关；经小鼠成瘤模型与免疫荧光验证。
> Agent note: ⭐ **D9 的直接强化证据，且把 SPP1⁺ TAM 从 PTC/RAI 难治扩展到 ATC**，并新增"胶原重塑/ECM"这一此前未纳入的机制维度。

**H5. Suppressed cGAS–STING DNA Sensing Drives Immune Evasion in Anaplastic Thyroid Cancer**
*Thyroid*, 2026-08-26. **PMID 42644464**. DOI **10.1177/10507256261481666**. OA: closed. 维度 IM/SC.
> Author claim: 在三类互补模型（Thrb1/Trp53/Pten 三突变基因工程鼠 RU3、Trp53+Braf 突变原位模型、Ifnb1/Trp53 表达皮下模型）中均观察到 ATC 进展期 cGAS–STING 信号显著抑制，伴随抗肿瘤免疫受损；scRNA-seq 刻画免疫微环境改变。
> Agent note: **本轮方法学最严谨的免疫原发证据**。为 D8 增添"先天免疫感知"维度（此前集中于 TAM/T 细胞适应性层面）。OA 闭源。

**H6. PHGDH inhibition overcomes dabrafenib resistance through metabolic rewiring in BRAF V600E anaplastic thyroid carcinoma**
*Cell Death Discovery*, 2026-08-15. DOI **10.1038/s41420-026-03293-7**. PMID 待编目. OA: gold. 维度 ME/ST.
> Author claim: 建立 dabrafenib 耐药 ATC 细胞系 8505C-R，鉴定 EGFR 与 PHGDH 上调为耐药标志；PHGDH 抑制剂 NCT-503 重编程肿瘤可塑性、干细胞样表型与 EGFR–MAPK 轴，LRIG1 参与反馈环。
> Agent note: **丝氨酸代谢 → 靶向耐药 → 干性**三点闭环，把"代谢重编程"从描述性关联推进到可干预节点。仅细胞系证据，无体内/临床验证。

**H7. Loss of heterozygosity exposes germline mutations in complex I and drives Warburg metabolism in oncocytic carcinoma of the thyroid**
*Science Advances*, 2026-07-03. DOI **10.1126/sciadv.aee5417**. OA: gold. 维度 MO/ME.
> Author claim: 建立新型嗜酸细胞癌（OCT）细胞系 UT946，胞质杂交实验证明复合物 I 缺陷源自核编码亚基 NDUFS1 的功能丧失突变；该突变为**隐性胚系等位基因**，经肿瘤中 LOH 暴露；91 例 OCT 肿瘤基因组再分析显示"LOH 暴露隐性胚系复合物 I 突变"是复发性机制。
> Agent note: ⭐ **本轮机制最深刻的一条**——把胚系遗传、LOH、线粒体复合物 I 与 Warburg 代谢串成一条完整因果链，且直接解释了 OCT 的线粒体积累表型。
> ⚠️ **标识符冲突提示 / identifier discrepancy**：Europe PMC 报 PMID **42397919**，OpenAlex 报 PMID **41427350**，两者不一致；Crossref 校验标题/期刊/日期（2026-07-03）一致。**以 DOI 10.1126/sciadv.aee5417 为主标识，PMID 标注"待确认"**，未采用任一冲突值。

**H8. Clinical transportability, calibration drift, and local updating of a B-mode ultrasound radiomics-clinical prediction model for occult high-volume central lymph node metastasis in cN0 papillary thyroid carcinoma: development, temporal validation, and external validation**
*Gland Surgery*, 2026-07-01. **PMID 42591955**. DOI **10.21037/gs-2026-0217**. OA: diamond. 维度 AL/PR.
> Author claim: 三中心回顾性模型开发/验证/更新研究，源数据 957 例 cN0 PTC，终点为隐匿性高容量 CLNM（>5 枚转移中央区淋巴结）；系统评估跨中心可移植性、校准漂移、阈值后果与本地更新策略。
> Agent note: ⭐ **本轮算法维度最有价值的一条，且是罕见的"反拥挤"证据**——它不追求更高 AUC，而正面处理 D13 长期被本方标注的首要风险（外部验证与校准漂移）。

**H9. Noninvasive immune-inflammatory profiling by ultrasound radiomics for preoperative prediction of central lymph node metastasis in papillary thyroid carcinoma**
*Frontiers in Immunology*, 2026-09-18. DOI **10.3389/fimmu.2026.1912827**. PMID 待编目. OA: gold. 维度 MO/AL/PR/IM.
> Author claim: 1,000 例 cN0 PTC 回顾队列，整合 BRAF V600E 状态、6 项外周血免疫炎症指数与超声影像组学深度学习评分，构建四个渐进式 LightGBM 模型；跨尺度 Spearman 相关、BRAF 分层 Fisher z 检验 + TCGA-THCA 免疫反卷积；三尺度整合模型验证 AUC 0.824，DeLong 增量检验显著。
> Agent note: **"影像 + 外周血 + 分子"三尺度整合 + 免疫反卷积解释**是本轮 AL 维度设计最完整的范式，值得作为 D14 的方法学模板之一。

**H10. Ultrasound-Based Radiomics and Deep Learning for Prediction of Lateral and Central Lymph Node Metastasis and BRAF Gene Mutation in Papillary Thyroid Carcinoma**
*Technology in Cancer Research & Treatment*, 2026-08-01. **PMID 42771519**. DOI **10.1177/15330338261490262**. OA: gold. 维度 AL/PR.
> Author claim: 580 例双中心术后病理确诊 PTC，构建影像组学 + 深度学习 + 临床特征的 nomogram，同时预测 BRAF 突变、LLNM 与 CLNM；含训练集/内部验证/外部测试集。
> Agent note: 三终点联合预测 + 外部测试集是同类研究中的较优设计，但仍未报告决策曲线与临床效用。

**H11. Intratumor microbiota in thyroid cancer: emerging insights into tumorigenesis and therapeutic potential**
*Thyroid Research*, 2026-09-19. DOI **10.1186/s13044-026-00314-6**. PMID 待编目. OA: gold. 维度 SP（综述）.
> Author claim: 甲状腺肿瘤内存在独特微生物群落，可调控 TME、促进 DNA 损伤、改变致癌信号并重塑免疫应答；PTC 中已观察到跨组织学亚型、分期与性别的微生物组成差异。
> Agent note: **新方向候选 D17 的立论依据**。目前为综述，甲状腺癌组织内微生物群的**原发测序证据仍极其有限**（主要依赖 16S/宏基因组与泛癌推断），证据强度须显著降档。

**H12. A case report and diagnostic-therapeutic analysis of de novo bilateral papillary thyroid carcinoma complicated with stage I diffuse large B-cell lymphoma (ABC subtype, double-expressor)**
*Frontiers in Oncology*, 2026-09-21. DOI **10.3389/fonc.2026.1921091**. PMID 待编目. OA: gold. 维度 MO/IM.
> Author claim: 提出 PI3K/AKT/mTOR 与 NF-κB 轴组成性激活、免疫抑制性组织微环境重塑与 B 细胞克隆扩增是 PTC 与 ABC 型双表达 DLBCL 同步发生的共同分子免疫机制。
> Agent note: ⚠️ **相关性由脚本自动评为 High，本方人工降档为 Medium**：单例病例报告，机制论述为推演而非验证，不可计入机制证据，仅作"免疫微环境与淋巴瘤共病"线索保留。

### 2.2 Medium 相关性（24 条，要点）

| # | 文献（标题截断） | 来源 / 日期 | PMID / DOI | 维度 | OA |
|---|---|---|---|---|---|
| M1 | Timosaponin AIII-based liposomes loaded with Auranofin for ferroptosis induction in ATC | *J Cancer Res Clin Oncol* 2026-07-15 | 42455333 / 10.1007/s00432-026-06538-1 | ME/ST | gold |
| M2 | Serum 25(OH)D and HDL-C as site-specific metabolic markers of cervical LNM in PTC（n=1,003） | *World J Surg Oncol* 2026-07-06 | 42410598 / 10.1186/s12957-026-04483-4 | ME/PR | gold |
| M3 | Prognostic value of volume-based [¹⁸F]FDG PET/CT metabolic parameters in ATC（n=34） | *Eur J Nucl Med Mol Imaging* 2026-07-30 | 42530576 / 10.1007/s00259-026-08100-0 | PR/ME | hybrid |
| M4 | Integrated cytokine, metabolic and proliferative profiling in PTC cells | *Int J Mol Sci* 2026-07-09 | 42511477 / 10.3390/ijms27146131 | IM/ME | gold |
| M5 | SGLT2 and broad DPP inhibition modulate oxidative stress / metabolic burden in PTC | *Front Mol Biosci* 2026-07-29 | 42591312 / 10.3389/fmolb.2026.1875059 | ME | gold |
| M6 | LncRNA GSEC impedes glucose-metabolism reprogramming via IGF2BP2/GLUT1 axis in PTC | *Arch Endocrinol Metab* 2026 | 42536764 / 10.20945/2359-4292-2026-0083 | MO/ME | diamond |
| M7 | Gold-modified mesoporous carbon enables serum metabolic fingerprinting for PTC diagnosis（PTC 131 / BTN 79 / HC 71） | *Small Methods* 2026-09-16 | 42750355 / 10.1002/smtd.71048 | ME/AL | hybrid |
| M8 | Glucose-metabolism & somatostatin-receptor protein expression: primary vs distant metastasis in DTC | *Ann Nucl Med* 2026-07-21 | 42481909 / 10.1007/s12149-026-02252-7 | PR/ME | closed |
| M9 | Cuproptosis × mitochondrial energy metabolism in thyroid cancer: multi-omics subtyping & prognosis | *Mol Cell Biochem* 2026-06-19 | 42319714 / 10.1007/s11010-026-05604-z | ME | closed |
| M10 | Nomogram predicting extrathyroidal extension: dual-plane US radiomics + clinical（483 + 103 外部） | *Gland Surg* 2026-08-01 | 42724929 / 10.21037/gs-2026-0304 | AL/PR | diamond |
| M11 | Habitat imaging based on enhanced CT for occult CLNM in PTC | *Eur Radiol* 2026-09-19 | 42763332 / 10.1007/s00330-026-12806-y | AL/PR | closed |
| M12 | Deep learning framework for thyroid lesion malignancy in CEUS videos | *Artif Intell Med* 2026-07-26 | 42526280 / 10.1016/j.artmed.2026.103500 | AL | closed |
| M13 | Deep learning classification of NIFTP vs invasive encapsulated FVPTC from gross pathology images | *J Imaging Inform Med* 2026-08-26 | 42649337 / 10.1007/s10278-026-02236-z | AL | closed |
| M14 | Multimodal US decision support for Bethesda IV nodules: clinical + radiomics + DL + topological features | *J Imaging Inform Med* 2026-08-25 | 42642692 / 10.1007/s10278-026-02208-3 | AL | closed |
| M15 | Super-resolution US microvascular features for ML thyroid nodule classification（68 结节 / 63 例，5 算法 + SHAP） | *J Vis Exp* 2026-09-11 | 42730688 / 10.3791/72803 | AL | closed |
| M16 | ML hierarchical classification for early response to initial ¹³¹I therapy in PTC | *Ann Nucl Med* 2026-07-24 | 42496848 / 10.1007/s12149-026-02258-1 | AL/PR | closed |
| M17 | Nomogram for poorly differentiated thyroid cancer based on SEER（n=983） | *Nucl Med Commun* 2026 | 42011027 / 10.1097/mnm.0000000000002163 | PR/AL | closed |
| M18 | Tumor immune microenvironment markers (FOXP3/CD8/CD138) in PTC with vs without Hashimoto's thyroiditis（n=44） | *Baghdad Sci J* 2026-09-18 | 待编目 / 10.21123/2411-7986.5399 | IM | gold |
| M19 | Prognostic factors in thyroid cancer with lung-only metastasis: SEER | *Gland Surg* 2026-09-01 | 待编目 / 10.21037/gs-2026-0333 | PR | diamond |
| M20 | Raw-data-NPC2 as a potential biomarker for PTC（脂质代谢驱动因子 NPC2；Harvard Dataverse 数据集存档） | *Harvard Dataverse* 2026-09-21 | 待编目 / 10.7910/dvn/rj0nul | ME | green |
| M21 | Data from PRECISE: A Prognostic Thyrocyte-Derived Gene Signature for PTC（数据存档；主文见随访清单） | AACR 存档 2026-07-01 | 待编目 / 10.1158/1078-0432.c.8568781 | SC/PR | gold |
| M22 | TP53/p53 alterations in thyroid cancer: dedifferentiation, RAI refractoriness, risk stratification（综述） | *Crit Rev Oncol Hematol* 2026-09-01 | 42759586 / 10.1016/j.critrevonc.2026.105601 | ST/PR | closed |
| M23 | Synchronous medullary and papillary thyroid carcinoma with mixed-component lateral cervical LNM（病例） | *Gland Surg* 2026-09-01 | 待编目 / 10.21037/gs-2026-0288 | MO/PR | diamond |
| M24 | Treatment strategies for unilateral PTC with ipsilateral cervical LNM（叙述性综述） | *Gland Surg* 2026-09-01 | 待编目 / 10.21037/gs-2026-0281 | MO/PR | diamond |

### 2.3 Low 相关性（16 条，仅列题名与处置）

XPR1–NF-κB in thyroid carcinoma（10.24976/discov.med.202638212.232）· osimertinib + paclitaxel in ATC（PMID 42773810）· AYA PTC recurrence predictors, Kazakhstan（10.63946/onmt/19300，会议摘要）· BRAF/TERTp co-mutations in RAIR-DTC（10.63946/onmt/19289，会议摘要）· PTMC in the era of risk-adapted management（PMID 42767500）· Spatial-temporal thyroid cancer mortality in China（PMID 42755586，流行病学非空间组学）· Targeting sirtuins in thyroid cancer（PMID 42449637，综述）· Graves' disease & thyroid carcinoma risk biomarkers（PMID 42646315，meta）· Common biomarkers between non-obstructive azoospermia and PTC（PMID 42710154）· Radiomics/ML in Bethesda IV nodules（PMID 42536308）· MTC grading on FNA: manual vs DL（PMID 42532782）· TCGA + TCM compounds in PTC（PMID 42700077）· LLPS-related genes prognosis in thyroid carcinoma（10.36922/cp025320050）· Triphenyl phosphate exposure & thyroid cancer（PMID 42450283）· Programmed cell death evasion in BRAF V600E CNS tumors & thyroid cancer brain metastases（PMID 42769885）· Modern treatment of ATC（clinical case, 10.17650/2222-1468-2026-16-2-99-108）。

---

## 3. 证据矩阵 / Evidence Matrix

列依 `evidence-matrix-schema.md`；**维度 / Relevance / 预印本 / OA** 三列为 Run #25 增补要求。

| # | 维度 Dim | Paper | PMID/DOI | 疾病/人群 | 数据源 | 方法 | 终点 | 主要发现 | 验证 | 局限 | Relevance | 预印本 | OA | Gap / 未解 | 未来方向 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ME/IM/PR | MGST1 drives LNM in PTC (Front Immunol 2026) | 42327722 / 10.3389/fimmu.2026.1848083 | PTC ± LNM | TCGA/GTEx + 独立临床队列 + scRNA | 多组学 + 共识 ML + 基因/药理验证 | LNM | MGST1 经线粒体代谢重编程 + 免疫抑制驱动 LNM；T 细胞耗竭 + Treg 富集 | 独立临床队列 + 体外/体内功能验证 | 无空间共定位；未检验 APOE 背景 | **High** | 否 | gold | MGST1 与 APOE 是否同框？是否在空间上邻近 TAM？ | **D3″** |
| 2 | MO/ME | APOE promotes PTC via PINK1/Parkin mitophagy (Transl Cancer Res 2026) | 42724858 / 10.21037/tcr-2026-0796 | PTC | TCGA + GEO + 组织 IHC | 生物信息学 + IHC + 细胞实验 | 进展 | APOE 高表达促癌，经线粒体自噬 | IHC + 细胞系 | 缺乏挽救实验强度与独立队列 | **High** | 否 | diamond | APOE 促癌 vs Run#24 免疫抑制生态位，二者如何统一？ | **D3″** |
| 3 | ME/IM | GPI–O-GlcNAc–THBS1 myeloid crosstalk in ATC (Cancer Lett 2026) | 42248319 / 10.1016/j.canlet.2026.218650 | ATC | 细胞 + 髓系共培养 | 糖酵解酶功能 + 翻译后修饰 | 免疫抑制 | GPI→THBS1 O-GlcNAc→髓系抑制 | 体外 + 共培养 | 无体内与临床验证；OA 闭源 | **High** | 否 | closed | 代谢酶–免疫轴的体内必要性？ | **D18** |
| 4 | SC/IM | scRNA reveals SPP1⁺ TAM & collagen remodeling in ATC (BMC Cancer 2026) | 待编目 / 10.1186/s12885-026-16648-1 | ATC | 公共 scRNA + bulk | scRNA + 小鼠成瘤 + IF | TAM 亚群 / ECM | 髓系富集 + 间充质样恶性态；SPP1⁺ TAM 关联胶原高程序 | 体内成瘤 + IF | 无空间分辨率；无人类独立队列 | **High** | 否 | gold | SPP1⁺ 与 TREM2⁺ 是否共定位？胶原是否为其下游效应？ | **D9** |
| 5 | IM/SC | Suppressed cGAS–STING drives immune evasion in ATC (Thyroid 2026) | 42644464 / 10.1177/10507256261481666 | ATC | 3 类小鼠模型 + scRNA | GEMM/原位/皮下 + scRNA | 免疫逃逸 | ATC 进展期 cGAS–STING 被抑制，抗肿瘤免疫受损 | 三模型互证 + scRNA | 人类样本验证不足；OA 闭源 | **High** | 否 | closed | STING 激动剂在 ATC 是否可恢复免疫？ | **D8** |
| 6 | ME/ST | PHGDH inhibition overcomes dabrafenib resistance in ATC (Cell Death Discov 2026) | 待编目 / 10.1038/s41420-026-03293-7 | BRAF V600E ATC | 8505C-R 耐药细胞系 | RNA-seq + 药理抑制 | 耐药 / 干性 | PHGDH↑ + EGFR↑ 为耐药标志；NCT-503 重编程可塑性 | 细胞系 + 转录组 | 无体内/临床；单细胞系 | **High** | 否 | gold | 丝氨酸代谢是否可预测临床耐药？ | **D18 / D15** |
| 7 | MO/ME | LOH exposes germline complex I mutations → Warburg in OCT (Sci Adv 2026) | 待确认 / 10.1126/sciadv.aee5417 | 嗜酸细胞癌 OCT | 新细胞系 UT946 + 91 例肿瘤基因组 | 胞质杂交 + 基因组再分析 | 代谢表型 | NDUFS1 隐性胚系突变经 LOH 暴露 → 复合物 I 失功能 → Warburg | 胞质杂交 + 大样本基因组 | 单细胞系；胚系携带者前瞻风险未评估 | **High** | 否 | gold | 胚系携带者是否构成可筛查人群？ | **D18（新）** |
| 8 | AL/PR | Transportability/calibration drift/local updating of US radiomics CLNM model (Gland Surg 2026) | 42591955 / 10.21037/gs-2026-0217 | cN0 PTC（957 例） | 三中心回顾 | 放射组学 + 时间/外部验证 + 本地更新 | 隐匿高容量 CLNM | 跨中心迁移存在校准漂移，本地更新可缓解 | 时间 + 外部验证 | 回顾性；无前瞻影响研究 | **High** | 否 | diamond | 本地更新的最小样本量与更新频率？ | **D13** |
| 9 | MO/AL/PR/IM | US radiomics + blood immune-inflammatory + BRAF for CLNM (Front Immunol 2026) | 待编目 / 10.3389/fimmu.2026.1912827 | cN0 PTC（1,000 例） | 单中心队列 + TCGA-THCA | LightGBM + 跨尺度相关 + 免疫反卷积 | CLNM | 三尺度整合 AUC 0.824，DeLong 增量显著 | 内部验证 + TCGA 外部解释 | 单中心；无外部影像队列 | **High** | 否 | gold | 影像–血液–分子跨尺度关联是因果还是共变？ | **D14** |
| 10 | AL/PR | US radiomics + DL for LLNM/CLNM/BRAF in PTC (Technol Cancer Res Treat 2026) | 42771519 / 10.1177/15330338261490262 | PTC（580 例） | 双中心 | 放射组学 + DL + nomogram | LLNM/CLNM/BRAF | 三终点联合可预测，含外部测试集 | 外部测试集 | 无决策曲线；无临床效用 | **High** | 否 | gold | 预测结果是否改变手术决策？ | **D13** |
| 11 | SP | Intratumor microbiota in thyroid cancer (Thyroid Res 2026, review) | 待编目 / 10.1186/s13044-026-00314-6 | 甲状腺癌（以 PTC 为主） | 文献综述 | 叙述性综述 | 发生/治疗 | 瘤内微生物可调控 TME、DNA 损伤与免疫 | 无（综述） | 甲状腺原发测序证据极少 | **High**（综述降档） | 否 | gold | 甲状腺瘤内微生物是否为真实定植而非污染？ | **D17（新）** |
| 12 | MO/IM | Bilateral PTC + DLBCL case report (Front Oncol 2026) | 待编目 / 10.3389/fonc.2026.1921091 | PTC + DLBCL | 单例 | 病例报告 | 共病机制 | 提出 PI3K/AKT/mTOR + NF-κB 与免疫抑制微环境为共同机制 | 无 | 单例；机制为推演 | Medium（人工降档） | 否 | gold | 共病是因果还是偶发？ | 仅作线索 |
| 13 | ME/ST | TAIII + Auranofin liposomes → ferroptosis in ATC (J Cancer Res Clin Oncol 2026) | 42455333 / 10.1007/s00432-026-06538-1 | ATC（CAL-62 / 8505C） | 细胞 + 体内 | 脂质体递药 + 铁死亡读数 | 肿瘤生长 | T-AUF-LPs 诱导 ROS/铁/GSH-GPX4/ACSL4/NCOA4 相关铁死亡 | 体内成瘤 + 生物安全性 | 无临床；剂量生理性存疑 | Medium | 否 | gold | 铁死亡诱导能否与免疫治疗协同？ | **D12** |
| 14 | ME/PR | Serum 25(OH)D & HDL-C as site-specific LNM markers in PTC (World J Surg Oncol 2026) | 42410598 / 10.1186/s12957-026-04483-4 | PTC（1,003 例） | 回顾队列 | 血清生化 + 逻辑回归 | CLNM / LLNM | 25(OH)D 与 HDL-C 为部位特异性代谢相关因子 | 大样本内部 | LLNM 亚组小（3.79%）；回顾性 | Medium | 否 | gold | 代谢标志物是否独立于已知病理因素？ | **D3″** |
| 15 | PR/ME | Volumetric [¹⁸F]FDG PET/CT parameters in ATC (EJNM 2026) | 42530576 / 10.1007/s00259-026-08100-0 | ATC（34 例） | 单中心 2010–2024 | MTV/TLG/SUV + 生存分析 | OS | MTV 为独立预后因子（HR 1.44, p=0.009） | 内部 | n=34；中位 OS 仅 48 天 | Medium | 否 | hybrid | 代谢体积能否指导治疗强度？ | **D16** |
| 16 | IM/ME | Integrated cytokine/metabolic/proliferative profiling in PTC cells (IJMS 2026) | 42511477 / 10.3390/ijms27146131 | PTC 细胞系 vs 正常甲状腺 | 细胞模型 | 多因子 + 代谢 + Ki-67 | 分泌/代谢/增殖 | PTC 细胞系呈细胞系特异性细胞因子与代谢谱；药物干预反应分化 | 无 | 仅体外；细胞系间异质性大 | Medium | 否 | gold | 体外葡萄糖条件与体内差距？ | **D11** |
| 17 | ME | SGLT2 / broad DPP inhibition in PTC (Front Mol Biosci 2026) | 42591312 / 10.3389/fmolb.2026.1875059 | PTC 细胞模型 | 细胞 | ROS/MDA/TAC/XIAP + 代谢指数 | 氧化应激/代谢负荷 | SGLT2 抑制改变葡萄糖依赖代谢与 XIAP 分布 | 无 | 体外；剂量由 MTT 选定 | Medium | 否 | gold | SGLT2 抑制在甲状腺癌是促癌还是抑癌？ | **D18** |
| 18 | ME | Au-mesoporous carbon serum metabolic fingerprinting for PTC (Small Methods 2026) | 42750355 / 10.1002/smtd.71048 | PTC 131 / BTN 79 / HC 71 | 临床血清 + MS 平台 | 纳米基底 MS + 机器学习 | 诊断 | 血清代谢指纹可区分 PTC/BTN/HC | 三分组比较 | 单中心；无外部验证；BTN 鉴别的临床增益不明 | Medium | 否 | hybrid | 能否替代/补充 FNA 与分子检测？ | **D13** |
| 19 | ME | Cuproptosis × mitochondrial energy metabolism in TC (Mol Cell Biochem 2026) | 42319714 / 10.1007/s11010-026-05604-z | 甲状腺癌 | TCGA + 多组学 | 分子分型 + 预后模型 | 分型/预后 | 铜死亡与线粒体能量代谢交互，可分子分型 | TCGA 内部 | 无外部验证；无湿实验 | Medium | 否 | closed | 铜死亡在甲状腺癌是特异还是泛癌共性？ | **D12** |
| 20 | SC/PR | Data from PRECISE: thyrocyte-derived prognostic signature for PTC（数据存档） | 待编目 / 10.1158/1078-0432.c.8568781 | PTC（MDACC n=109，中位随访 14 年） | snRNA/scRNA + 队列 | 细胞类型来源签名 | 预后 | 甲状腺滤泡细胞来源签名具预后价值 | 跨队列（详见随访清单主文 PMID 42008746） | 存档本身非独立证据 | Medium（存档） | 否 | gold | 细胞类型来源签名能否推广到 LNM 终点？ | **D14** |

> 完整 52 条新增的机器可读字段见 `search_results_20260925_new.json`；累积 297 条见 `search_results_20260925_033500.json` 与 `search_results_latest.json`。

---

## 4. 已知结论 / What Is Already Known

1. **PTC 的淋巴结转移由"线粒体代谢重编程 + 免疫抑制"双轮驱动，且存在可操作的单基因节点。** MGST1（PMID 42327722）经多组学 + 独立队列 + scRNA + 共识 ML + 基因/药理验证被确立为 LNM 驱动因子，其免疫表型为 T 细胞耗竭 + Treg 富集。这与 Run #21 以来的 TREM2⁺/AHR–IDO1 轴（D8）在**免疫表型层面高度一致**，提示髓系/Treg 抑制是 PTC 转移的共同通路。
2. **APOE 在甲状腺癌中是促癌因子，而非保护性或"阴性背景"标志。** 两条独立证据同向：Run #24 的 APOE⁺ 肿瘤亚群–CD8⁺ Tex 空间生态位（PMID 42217128）与本轮 APOE–PINK1/Parkin 线粒体自噬（PMID 42724858）。**原 D3 假设中"APOE 低表达定义干性亚群"的设定已被证伪。**
3. **代谢–免疫耦合在 ATC 中已从相关性升级到准因果。** GPI–O-GlcNAc–THBS1–髓系抑制（PMID 42248319）与 cGAS–STING 抑制（PMID 42644464）分别从代谢酶–翻译后修饰和先天免疫感知两条路径提供机制；PHGDH–丝氨酸代谢则解释了 BRAF 抑制剂耐药（10.1038/s41420-026-03293-7）。
4. **SPP1⁺ TAM 是跨亚型（PTC/DTC-RAI 难治 → ATC）的保守免疫抑制亚群，且与 ECM/胶原重塑耦合。** 本轮 ATC scRNA（10.1186/s12885-026-16648-1）在 Run #22 外泌体 SPP1→CD44/JAK2/STAT3 因果链（PMID 42153613）基础上，新增"胶原高恶性上皮态"这一效应层。
5. **甲状腺癌的代谢异质性可由胚系遗传结构决定。** OCT 中 LOH 暴露隐性胚系 NDUFS1 突变 → 复合物 I 失功能 → Warburg（10.1126/sciadv.aee5417），91 例基因组再分析支持其为复发性机制。这是本轮唯一把"胚系变异—体细胞 LOH—代谢表型"串成闭环的证据。
6. **术前 LNM/ETE/BRAF 预测的影像–临床模型已高度饱和，但外部可移植性成为新的方法学瓶颈。** 本轮 15 条 AL 文献中，仅 H8（PMID 42591955）系统处理校准漂移与本地更新；其余仍以 AUC 为主指标。
7. **铁死亡/铜死亡在甲状腺癌中正从"泛癌共性"转向"亚型特异机制"。** HIF-1α–ACSL4 轴（基线，PMID 42365271）、本轮 TAIII+Auranofin 脂质体（PMID 42455333）、Sirtuins 综述（PMID 42449637）、TCBM 铁死亡增敏（PMID 42769885）共同构成一条可检验的链条。

---

## 5. 未解问题 / What Remains Unclear

1. **APOE 与 MGST1 的关系完全未检验。** 二者在本轮被独立确立，但**没有任何文献同时测量两者**，更无空间共定位。APOE 促癌（线粒体自噬）与 MGST1 驱动 LNM（线粒体代谢重编程 + 免疫抑制）在"线粒体"层面可能收敛，也可能完全独立。**这是本轮最大的可操作空白。**
2. **APOE 可能是双向功能分子。** Run #24 的免疫抑制生态位证据与本轮的线粒体自噬促癌证据，在不同背景下指向不同机制；是否存在剂量/亚型依赖的功能切换，尚无数据。
3. **SPP1⁺ 与 TREM2⁺ 是否同一亚群、是否共定位，仍无直接答案。** 两条轴分别被独立确立（Run #21 TREM2⁺ AHR–IDO1；Run #22/25 SPP1⁺），但从未在同一空间框架内被同时测量。
4. **代谢标志物的独立增量价值不明。** 血清 25(OH)D/HDL-C（PMID 42410598）、血清代谢指纹（PMID 42750355）都未报告在已知临床病理因素之上的净重分类改善（NRI）或决策曲线。
5. **cGAS–STING 抑制在人类 ATC 中的普遍性与可逆性未知。** 三模型互证很强，但缺少人类组织验证与 STING 激动剂的干预数据。
6. **PHGDH–耐药轴缺乏体内与临床验证。** 单一耐药细胞系 + 转录组，无法判断其临床可转化性。
7. **甲状腺瘤内微生物群仍停留在"是否存在"阶段。** 无甲状腺特异的原发测序 + 空间定位 + 污染对照研究。
8. **影像模型的可移植性缺乏量化标准。** H8 提出本地更新，但未给出最小更新样本量、更新频率与漂移阈值的通用规则。
9. **Sci Adv OCT 论文的 PMID 存在跨库冲突**（42397919 vs 41427350），反映 OpenAlex 与 Europe PMC 在 AAAS 期刊编目上的不同步；在 PMID 确认前，任何引用应以 DOI 为准。
10. **肺-only 转移、脑转移、骨转移的器官特异性机制证据依然稀薄**，本轮仅有 SEER 回顾（10.21037/gs-2026-0333）与一篇脑转移综述（PMID 42769885），无原发机制研究。

---

## 6. 领域方法/数据局限 / Method/Data Limitations In The Field

| 局限类别 | 本轮具体表现 | 影响 |
|---|---|---|
| **检索矩阵对基因锚定文献系统性漏检** | MGST1、APOE–PINK1、GPI–THBS1 三条本轮最重要证据**全部**未被 `oa_search.py` 九路查询命中，仅由定向基因深挖通道捕获 | 单一布尔矩阵会把高质量机制研究误判为"无新增" |
| **高频维度饱和、低频维度欠采样并存** | SP 本轮仅 1 条（且为综述）；AL 15 条几乎全是同质化 nomogram | 维度计数不能反映领域真实热度 |
| **单细胞研究的空间分辨率缺口** | SPP1⁺ TAM ATC（10.1186/s12885-026-16648-1）与 PRECISE 均无空间维度 | 亚群"共定位"只能靠推断 |
| **外部验证与校准漂移仍非标配** | 15 条 AL 中仅 1 条（PMID 42591955）系统处理可移植性 | 模型 AUC 与临床效用脱节 |
| **体外糖酵解条件与体内不符** | M4/M5/M16 三篇 PTC 细胞代谢研究均在标准高糖培养基下完成 | 代谢表型外推风险高 |
| **稀有亚型样本量天花板** | ATC PET 研究 n=34、中位 OS 48 天（PMID 42530576）；MTC/PDTC 依赖 SEER 回顾 | 统计效能与混杂控制受限 |
| **存档/补充材料污染** | figshare "Additional file 1–9 of HIF-1α…" 出现双版本（.v1 与非 v1），Harvard Dataverse/Zenodo 数据集与正式论文分离索引 | 需按标题归一化合并，否则虚增计数 |
| **会议摘要与书信错配** | 2 条 `onmt` 会议摘要、1 条 Editorial/Letter 被脚本纳入 | 证据强度须人工降档 |
| **标识符不同步** | Sci Adv 论文 PMID 跨库冲突；近 30 天文献大量"待编目" | 必须以 DOI 为主标识 |

---

## 7. 候选未来方向 / Candidate Future Directions

评分依据 `research-direction-rubric.md` 七维 1–5 分（Novelty / Feasibility / Data availability / Validation strength / Clinical relevance / Method rigor / Overcrowding risk），28–35 为强候选。

| ID | Direction / 方向 | Rationale / 依据 | Rubric（Δ vs Run#24） | Required Data / 所需数据 | Validation Plan / 验证 | Main Risk / 主要风险 | Claim Boundary / 声明边界 |
|---|---|---|---:|---|---|---|---|
| **D9** | **SPP1⁺ × TREM2⁺（× TIM3⁺）TAM 生态位共定位与统一命名** | 本轮 ATC scRNA 直接证据（10.1186/s12885-026-16648-1）+ 胶原/ECM 效应层；Run #22 外泌体 SPP1→CD44/JAK2/STAT3 因果链 | **33**（32 → 33 ⬆） | JCI Insight 空间图谱（10.1172/jci.insight.191990）、配对原发–LNM scRNA（10.1080/2162402x.2026.2701504）、ATC scRNA（本轮）、自有 mIF | 四色 mIF 共定位；SPP1 敲除 × TREM2 阻断正交；外部队列预后增量 | TAM 命名混乱；拥挤度上升 | 声称"亚群共定位与功能互作"，**不声称单一亚群主导** |
| **D3″** | **APOE × MGST1 双代谢–免疫轴的空间共定位与功能解耦**（D3′ 二次重构） | ⭐ MGST1 首次直接功能证据（PMID 42327722）+ APOE 促癌机制（PMID 42724858）+ GPI 代谢–免疫（PMID 42248319）；原互斥假设已被证伪，需重构为双轴模型 | **31**（29 → 31 ⬆） | TCGA/GTEx、配对原发–LNM scRNA、JCI Insight 空间图谱、自有配对原发–LNM 蜡块 | ①APOE/MGST1 双 IHC/mIF 在独立队列共定位；②MGST1 敲低 × APOE 阻断的体外正交；③签名外部 C-index | APOE 双向功能；MGST1 与 APOE 可能完全独立；共定位≠互作 | 只能声称"双轴关联与空间共定位"，**不得声称 APOE 或 MGST1 为治疗靶点**直至功能阻断完成 |
| **D8** | **甲状腺癌髓系全景 + 先天免疫感知：TAM × 中性粒细胞 × cGAS–STING** | 本轮新增 cGAS–STING 三模型证据（PMID 42644464），把 D8 从适应性/髓系组成拓宽到先天感知层 | **32**（维持） | BRAF-PTC ± LT scRNA、ATC GEMM 模型、多重免疫荧光 | STING 激动剂体内挽救；中性粒细胞耗竭；跨队列髓系比例复核 | 中性粒细胞研究极少；STING 激动剂临床失败史 | 区分"髓系组成关联"与"髓系因果驱动" |
| **D15** | **去分化轨迹的细胞态解析：ATC-like 前体态、CAF–乳酸生态位与可逆性窗口** | 本轮 TP53/p53–去分化综述（PMID 42759586）+ PHGDH 干性–耐药（10.1038/s41420-026-03293-7）补强；基线已有微环境可塑性综述（PMID 42653308） | **30**（维持） | 跨阶段 scRNA、Visium/GeoMx、配对原发–复发 | UBE2C/ZFP57 IHC 验证；类器官乳酸/剂量–效应；NIS 摄碘读数 | 去分化样本稀缺 | **不声称"逆转去分化"的临床可行性** |
| **D12** | **铁死亡/铜死亡在甲状腺癌的亚型特异机制** | HIF-1α–ACSL4（基线 PMID 42365271）+ 本轮 TAIII/Auranofin（PMID 42455333）+ Sirtuins–ferroptosis 综述（PMID 42449637）+ 铜死亡分型（PMID 42319714） | **29**（27 → 29 ⬆） | TCGA、DepMap、ATC/PTC 细胞系、铁/铜死亡诱导剂 | HIF-1α–ACSL4 轴的剂量–效应与挽救；亚型间敏感性比较 | 可能仍为泛癌共性 | 不声称亚型特异性，除非完成亚型间对照 |
| **D14** | **细胞类型解析 + 空间多组学的因果与方法学框架** | 本轮 Front Immunol 三尺度整合 + TCGA 反卷积（10.3389/fimmu.2026.1912827）提供新范式；PRECISE 数据集（PMID 42008746）为签名标杆 | **28**（维持） | TCGA/CPTAC、GEO 空间数据集、MR 汇总数据 | 分类器在独立空间队列复现；MR 阴性对照与敏感性分析 | 蛋白基因组门槛；MR 假设可检验性 | 声明"统计学支持的细胞类型特异关联"，**不声称个体水平因果** |
| **D18（新）** | **代谢–靶向耐药轴：PHGDH/丝氨酸代谢 × GPI–糖酵解 × 胚系复合物 I 的耐药与易感分层** | 本轮三篇独立论文（PHGDH–dabrafenib、GPI–THBS1、NDUFS1–LOH–Warburg）+ SGLT2/DPP 药理干预，共同指向"代谢状态决定治疗反应" | **28**（新立） | TCGA/GTEx、耐药细胞系配对转录组、DepMap 依赖性、OCT 基因组 | PHGDH 抑制剂在耐药模型的体内验证；NDUFS1 胚系携带者回顾性风险；代谢抑制剂与靶向药联用矩阵 | 三者可能互不相关，需避免强行统一；OCT 样本稀缺 | 仅声称"代谢状态与治疗反应的关联"，**不声称代谢抑制剂可临床逆转耐药** |
| **D13** | **术前 LNM/ETE 预测模型的可移植性工程（而非新模型）** | 本轮 15 条 AL 同质化严重，但 H8（PMID 42591955）开辟"校准漂移 + 本地更新"这一反拥挤切口 | **27**（26 → 27 ⬆） | 多中心超声/CT、术后病理金标准、已有公开模型的源工作簿 | 跨中心漂移量化；本地更新最小样本量；决策曲线与前瞻影响研究 | 方向整体拥挤；需以方法学而非性能取胜 | 仅声称"判别性能与可移植性"，**不声称临床效用** |
| **D16** | **MTC 器官特异性远处转移机制：RET–OPG 骨转移轴 + 液体活检** | 本轮无新 MTC 机制证据（仅 MTC FNA 分级 DL 与同步性病例） | **27**（维持） | MTC 骨转移组织、配对血清 OPG/降钙素/CEA | OPG 独立血清队列 ROC + NRI | 样本获取难 | 不声称 OPG 可替代现有标志 |
| **D11** | **乳酸/代谢–EMT–去分化轴的代谢流解析** | 本轮无直接新证据，经 M4/M5/M16 体外代谢数据间接支撑 | **31**（维持） | 空间代谢组 + 配对转录组、Seahorse、同位素示踪 | 乳酸同位素示踪 + CAF-肿瘤共培养梯度 | 空间代谢分辨率限制 | 不将代谢物浓度等同于通路活性 |
| **D17（新）** | **甲状腺癌瘤内微生物群：从"是否存在"到空间定位** | 本轮综述（10.1186/s13044-026-00314-6）+ 基线肠道菌群–PTC（PMID 41958678） | **24**（新立，探索级） | 甲状腺癌新鲜冷冻组织的 16S/宏基因组 + 空间转录组配对 + 污染对照 | 阴性对照（试剂/环境）与独立队列复现；FISH 空间定位 | 极低生物量样本的污染风险极高；可能全是假阳性 | **不得声称存在功能性瘤内微生物组**，除非完成污染对照与空间定位 |

---

## 8. 推荐下一步方向 / Recommended Next Direction

### ⭐ 首选：**D9 + D3″ 合并推进 —— 以 ATC/PTC 配对样本解析「APOE × MGST1 双代谢轴」与「SPP1⁺/TREM2⁺ TAM」的空间耦合（rubric 综合 D9 33 / D3″ 31）**

**为什么是它：**

1. **D3 出现了 24 轮以来的第二次实质变化，且这次是"可操作化"而非"证伪"。** Run #24 的 D3′ 拿到 APOE 首次锚定但方向反转；本轮 MGST1 首次获得直接功能证据（PMID 42327722，多组学 + 独立队列 + scRNA + ML + 湿实验），**且方向与假设一致**。这意味着"代谢–免疫干性亚群"第一次同时拥有**两个可操作的分子锚点**。
2. **空白是明确且可一次性回答的。** 检索确认：**目前没有任何文献同时测量 APOE 与 MGST1**，也没有任何研究把 APOE/MGST1 与 SPP1⁺/TREM2⁺ TAM 放在同一空间框架内。这不是"需要更多研究"，而是"有一个具体的、今天就能做的联合分析"。
3. **数据全部现成且公开。** 配对原发–LNM scRNA（10.1080/2162402x.2026.2701504，gold）、JCI Insight 整合单细胞 + 空间图谱（10.1172/jci.insight.191990，gold）、本轮新增 ATC scRNA（10.1186/s12885-026-16648-1，gold）、TCGA/GTEx、MGST1 论文所用独立临床队列（PMID 42327722，gold）。
4. **rubric 最优且互不冲突。** D9 = 33、D3″ = 31；两者共享同一批空间/scRNA 数据，合并推进的边际成本极低。

**第一批具体步骤（4 周内）：**

1. **重新计算双轴评分**：在 JCI Insight 空间图谱与配对原发–LNM scRNA 中，计算 APOE、MGST1、SPP1、TREM2、HAVCR2、CD163、CD8A 的**生态位共定位评分**（非仅差异表达），输出 APOE×MGST1 双阳性肿瘤细胞比例与象限分布。
2. **显式检验配体–受体轴**：用 CellChat / NicheNet 检验 APOE–NCF1（Run #24）、SPP1–CD44（Run #22）与本轮新提出的 THBS1–髓系轴（PMID 42248319），以 AHR–IDO1 轴作对照。
3. **第一验证集**：用本轮 ATC scRNA（10.1186/s12885-026-16648-1）检验 MGST1⁺/APOE⁺ 肿瘤细胞是否与 SPP1⁺ TAM 及胶原高恶性态共变——这是 D3″ 与 D9 的交汇点，也是本轮独有的机会（此前 ATC 从未进入该框架）。
4. **MGST1 功能层的直接延伸**：以 PMID 42327722 的共识 ML 框架为基线，把 APOE 强制纳入特征集，检验 MGST1 的 LNM 预测增量是否被 APOE 吸收（即二者是否冗余）——这是判断"双轴"还是"同一轴"的关键判别实验，**纯计算、零湿实验成本**。
5. **湿实验门槛（明确标注为第二阶段）**：10–15 例自有配对原发–LNM 蜡块做四色 mIF（APOE / MGST1 / SPP1 / CD8）。

**必须避免的声明：**
- 不得声称 APOE 或 MGST1 为治疗靶点（二者均仅有功能关联，无靶向验证）；
- 不得声称"APOE−/MGST1⁺"亚群存在（该结构已被本轮证据证伪）；
- 不得把共定位等同于功能互作；
- 不得声称单一 TAM 亚群主导免疫逃逸。

**次选（并行、低资源占用）：** **D18 代谢–耐药轴预研** —— 复用现有 TCGA/DepMap 数据，先做 PHGDH/GPI/NDUFS1 三基因的泛癌—甲状腺特异依赖性对比（DepMap），判断 D18 是否值得升为正式方向。此路径**完全基于公开数据，与主方向零冲突**。

---

## 9. 随访阅读清单 / Follow-Up Reading List

**优先级 1（立即精读，直接决定下一步）**
- **MGST1 驱动 PTC LNM**（PMID 42327722, 10.3389/fimmu.2026.1848083, gold）：本轮最重要证据。需逐字核对：线粒体代谢签名的基因构成、共识 ML 的具体算法与特征泄漏防护、Treg/巨噬细胞部分的 scRNA 证据强度、**是否曾测量 APOE**。
- **APOE–PINK1/Parkin 线粒体自噬**（PMID 42724858, 10.21037/tcr-2026-0796, diamond）：核对 IHC 样本量、功能挽救实验设计与 PINK1/Parkin 是否必要。
- **SPP1⁺ TAM 在 ATC 的 scRNA**（10.1186/s12885-026-16648-1, gold）：核对髓系亚群命名与胶原高恶性态的判定标准，作为 D9 的第三独立队列。
- **GPI–O-GlcNAc–THBS1 髓系轴**（PMID 42248319, 10.1016/j.canlet.2026.218650, closed）：OA 闭源，需机构访问；核对 O-GlcNAc 位点与 THBS1 受体验证。

**优先级 2（方法学与数据集）**
- **影像组学可移植性/校准漂移**（PMID 42591955, 10.21037/gs-2026-0217, diamond）：D13 的方法学模板，需提取其本地更新策略与阈值后果分析方法。
- **三尺度整合 US radiomics + 血液免疫 + BRAF**（10.3389/fimmu.2026.1912827, gold）：D14 的跨尺度整合范式，需核对免疫反卷积工具与 BRAF 分层检验。
- **LOH 暴露胚系复合物 I 突变（OCT）**（10.1126/sciadv.aee5417, gold，PMID 待确认）：本轮机制最深论文，需核对 91 例基因组再分析的统计方法与 UT946 表征数据。
- **PHGDH–dabrafenib 耐药**（10.1038/s41420-026-03293-7, gold）：D18 的起点，核对 8505C-R 建立流程与 NCT-503 剂量。

**优先级 3（背景与补充）**
- PRECISE 主文（PMID 42008746, 10.1158/1078-0432.ccr-25-4488）：细胞类型来源签名标杆，14 年随访；**注意本轮新入库的是其数据存档（10.1158/1078-0432.c.8568781），须合并引用**。
- 基线已有的关键资源（本轮复查确认已在库中，供主方向直接复用）：HIF-1α–ACSL4 铁死亡（PMID 42365271）、微环境可塑性与 RAI 抵抗（PMID 42653308）、脂质代谢重编程综述（preprint 10.20944/preprints202608.0708.v1）、甲状腺癌空间转录组 PRISMA 系统综述（preprint 10.20944/preprints202608.0302.v1）。
- TP53/p53–去分化综述（PMID 42759586）、cGAS–STING ATC（PMID 42644464，closed）、铜死亡–线粒体（PMID 42319714）。

**降级处理（存档/综述/会议摘要，仅作线索）**
- Raw-data-NPC2（10.7910/dvn/rj0nul，Dataverse 数据集存档）：脂质代谢候选，主文未见，跟踪即可。
- 2 条 `onmt` 会议摘要（AYA 复发、BRAF/TERTp RAIR-DTC）：无全文方法细节。
- "Modern methods of treatment of ATC (clinical case)"：单例临床病例。
- 瘤内微生物群综述（10.1186/s13044-026-00314-6）：立论性综述，无原发数据。

---

## 10. 可复现性说明 / Reproducibility Notes

- **检索日期 / Search date**: 2026-09-25 03:02–03:35 (GMT+8)
- **数据库 / Databases**: OpenAlex（`api.openalex.org`，主源，30 d + 90 d 九路）、Europe PMC（`www.ebi.ac.uk/europepmc/webservices/rest`，**本轮扩至 6 路**）、**OpenAlex 定向基因深挖（本轮新增第三通道，7 路）**、Crossref（DOI 元数据校验）、Unpaywall（OA 解析）
- **未使用 / Not used**: NCBI eutils / PubMed（本机 HTTP 000 不可达，按 `RETRIEVAL_ENVIRONMENT.md` 禁止直连，未重试）；paper-search-mcp（本会话未连接，仅有 agent-mail）
- **查询串 / Query strings**: 见第 1 节表格。OpenAlex `filter=title_and_abstract.search:<bool>,from_publication_date:<date>`，`sort=publication_date:desc`；Europe PMC `TITLE:"thyroid"` 约束 + `sort=P_PDATE_D desc`，pageSize 50；定向深挖同 OpenAlex 语法，无日期下限约束（`from_publication_date:2026-01-01`）
- **过滤 / Filters**: 30 d（≥2026-08-26）/ 90 d（≥2026-06-27）；per-page 25（30 d）与 50（90 d/深挖）
- **去重规则 / Deduplication**: DOI 小写优先 → 标题归一化（NFKD、去标点、小写、截 90 字符）兜底；OpenAlex 多版本（仓储副本/出版版本/figshare .v1 与非 v1）按标题合并；Dataverse/Zenodo 数据集存档与正式论文分离索引，按标题归一化合并且标注存档类型；与基线 245 条做三重比对（PMID / DOI / 归一化标题）
- **筛选规则 / Screening**: 标题必须点名甲状腺 **且** 整体为肿瘤主题；`SUPPLEMENT` 正则剔除期刊补充材料与 figshare "Additional file N of …"；会议摘要、书信、Correction、Retraction notice 单独标注并降档；他病甲状腺转移与 ICI 相关 irAE 标记边界 off-topic
- **通道健康 / Channel health**: OpenAlex ✅；Europe PMC ✅；Crossref **10/10 成功**；Unpaywall **10/10 成功**；NCBI ❌（未尝试）
- **脚本 / Scripts**: `oa_search.py`（主检索 + 清洗）、`_merge_run25.py`（双窗口合并）、`_epmc_run25.py`（6 路补检）、`_epmc_detail_run25.py`（OpenAlex 回填摘要/元数据）、`_d3_deep_run25.py`（7 路定向深挖 + 基线查重）、`_keyabs_run25.py`（关键证据摘要抽取）、`_enrich_run25.py`（Crossref/Unpaywall 校验 + D3 复查 + PRECISE 定位）、`_final_run25.py`（三通道合并 + 基线回写）
- **产出文件 / Artifacts**:
  - `literature_review_20260925_033500.md`（本报告）
  - `search_results_20260925_030100.json`（OpenAlex 30 d 主窗口：唯一 98 / 在范围 69 / 新增 15）
  - `search_results_20260925_90day.json`（OpenAlex 90 d 补检：唯一 240 / 在范围 171 / 新增 19）
  - `search_results_20260925_epmc.json` + `search_results_20260925_epmc_detail.json`（Europe PMC 6 路 + 元数据回填）
  - `search_results_20260925_d3check.json` + `search_results_20260925_d3deep.json`（定向深挖 7 路 + 基线查重）
  - `search_results_20260925_keyabs.json`（关键证据摘要）
  - `search_results_20260925_enrich.json`（Crossref/Unpaywall 校验，10/10 成功）
  - `search_results_20260925_new.json`（本轮 52 条新增）
  - `search_results_20260925_033500.json` / `search_results_latest.json`（**累积基线 297 条**，已回写）
- **标识符政策 / Identifier policy**: 近 30 天新文献多数尚无 PMID，一律以 DOI 为主标识，PMID 缺失标注「待编目」；**未编造任何 PMID 或 DOI**。对存在跨库冲突的 Sci Adv 论文（10.1126/sciadv.aee5417）标注"PMID 待确认"并列出两个冲突来源值，均不采用。预印本单独标注并降档（本轮 0 条）。

---

## 11. 与历史报告的差异 / Delta vs. Previous Reports

### 11.1 数量差异 / Quantitative Delta

| 指标 | Run #24 (2026-09-18) | **Run #25 (2026-09-25)** | 变化 |
|---|---:|---:|---|
| 去重后唯一新增 | 74 | **52** | −22（距上轮仅 7 天，正常日更量） |
| 通道数 | 2（OpenAlex + Europe PMC 3 路） | **3（OpenAlex + Europe PMC 6 路 + 定向深挖 7 路）** | +1 通道 |
| High / Medium / Low | 18 / 41 / 15 | **12 / 24 / 16** | High 占比 16% → 23%（筛入更严） |
| 严格预印本 | 3 | **0** | 两条相关预印本已在基线 |
| 累积基线 | 245 | **297** | +52 |
| 维度最大项 | 算法方法 25 | **预后转移 25 / 代谢重编程 17 / 算法方法 15** | ME 跃升为第二密集维度 |
| 空间组学 SP | 有 90 d 溢出 High | **1（仅综述）** | 近乎空窗 |

### 11.2 方向评分变化 / Direction Rubric Delta

| ID | Run #24 | **Run #25** | 判定 |
|---|---:|---:|---|
| D3 → D3′ → **D3″** | 29 | **31** | ⬆ **强化 + 二次重构** |
| D9（SPP1⁺ TAM） | 32 | **33** | ⬆ 强化（ATC scRNA） |
| D12（铁死亡/新型死亡） | 27 | **29** | ⬆ 强化（HIF-1α–ACSL4 + 药物诱导） |
| D13（术前 LNM 预测） | 26 | **27** | ⬆ 微升（可移植性方法学） |
| D8（髓系全景） | 32 | 32 | 维持（+cGAS–STING 拓宽） |
| D11（乳酸–EMT） | 31 | 31 | 维持 |
| D15（去分化轨迹） | 30 | 30 | 维持 |
| D14（因果 + 空间框架） | 28 | 28 | 维持 |
| D16（MTC 远处转移） | 27 | 27 | 维持（无新机制证据） |
| **D18（代谢–耐药轴）** | — | **28（新立）** | 新 |
| **D17（瘤内微生物群）** | — | **24（新立，探索）** | 新 |

### 11.3 持续跟踪方向状态 / Tracking Status of Standing Directions

> **重点跟踪对象：APOE−/MGST1⁺ 代谢–免疫干性亚群（D3 系列，已连续跟踪 25 轮）**

- **状态：强化 ⬆ —— 且需二次重构，由 D3′ 变更为 D3″。**
- **强化证据**：MGST1 首次获得直接功能锚定（PMID 42327722），方法链完整（TCGA/GTEx + 独立临床队列 + scRNA + 共识 ML + 基因/药理验证），LNM 表型与原假设一致。
- **重构证据**：APOE 被独立证明为**促癌**因子（PMID 42724858，PINK1/Parkin 线粒体自噬），与 Run #24 的 APOE⁺ 肿瘤亚群–CD8⁺ Tex 生态位同向。**"APOE 低表达定义干性亚群"这一原始设定正式作废。**
- **新表述（D3″）**：不再假定 APOE/MGST1 互斥，改为检验 **APOE × MGST1 双代谢轴的独立性与空间共定位**，并把两者与 SPP1⁺/TREM2⁺ TAM 放在同一空间框架内。
- **未变部分**：**仍无任何文献同时测量 APOE 与 MGST1** —— 这正是首选方向的核心空白。

其他方向：D9 强化（ATC 扩展）· D12 强化（机制特异化）· D8 维持并拓宽（先天免疫）· D11/D14/D15/D16 维持（无直接新证据或仅间接支撑）· D13 微升。

### 11.4 本轮新信号与新方向 / New Signals

1. **⭐ 代谢–免疫轴（ME × IM）正式成为甲状腺癌最活跃的机制前沿** —— 本轮 27/52 条（52%）落在 ME 或 IM 维度，其中 3 条达准因果强度。这是 25 轮以来该轴证据密度最高的一轮。
2. **⭐ 定向基因深挖通道被证明不可省略** —— 仅 12 条产出却独占本轮 3 条最重要原发证据。`oa_search.py` 的九路布尔矩阵对基因锚定文献存在结构性漏检。
3. **新方向 D18（代谢–耐药轴 28）**：PHGDH/丝氨酸代谢、GPI–糖酵解、胚系复合物 I 三条独立线索共同指向"代谢状态决定治疗反应"。
4. **新方向 D17（瘤内微生物群 24，探索级）**：目前仅有综述，污染风险极高，暂不建议投入资源。
5. **空间组学空窗**：本轮 SP 仅 1 条综述。结合 Run #23/#24 连续 90 d 补检与基线中已有的空间转录组 PRISMA 系统综述，判定为**前序轮次已充分吸收**，非领域停滞。

### 11.5 下一轮调整建议 / Adjustments For Next Run

1. **将定向基因深挖固化为常规第三通道**，并把基因面板从 {APOE, MGST1} 扩展到 {SPP1, TREM2, HAVCR2, PHGDH, GPI, NDUFS1, NCF1, NPC2, CD44, THBS1, LDHA, PKM2, UBE2C, ZFP57, ECT2, SMDT1}，每轮固定扫描。
2. **Europe PMC 维持 6 路**，并新增"代谢酶/耐药"专项查询。
3. **SP/ME 维度默认 90 天窗口**（已连续 5 轮验证 30 天窗口对低频高分维度不足）。
4. **在 `oa_search.py` 的清理规则中增加**：`Retraction notice to` / `Correction:` / `Erratum:` / `Publisher Correction:` / `ASO Visual Abstract:` 前缀条目自动降档或剔除（本轮已在人工层处理，应脚本化）。
5. **建立 PMID 冲突处理规则**：当 OpenAlex 与 Europe PMC 的 PMID 不一致时，一律标注"待确认"并以 DOI 为主标识（本轮 Sci Adv 案例）。
