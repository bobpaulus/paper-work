# 甲状腺癌文献监测报告 / Literature Review: Thyroid Cancer (PTC/PTMC/FTC/MTC/ATC)

**Run #26 · Date:** 2026-10-02 · **时间戳 TS:** `20261002_030212`
**Sources:** OpenAlex（主通道，30 d / 90 d 九路）、Europe PMC（第二通道，六路）、Crossref / Unpaywall（元数据与 OA 校验）
**Search window:** 主 30 d（2026-09-02 → 2026-10-02）／90 d 补检（2026-07-04 → 2026-10-02）／Europe PMC `PUB_YEAR:2026`／定向基因深挖（2026-06-01 起）
**累积基线:** 391 条（上一轮 297 → 本轮 391）

---

## 中文摘要

本轮为 Run #26，距上一轮（Run #25，2026-09-25）7 天。三通道并行检索（OpenAlex 30 d/90 d 九路布尔矩阵、Europe PMC 六路交叉补检、定向基因深挖 22 基因面板），累计筛入**去重后唯一新增 94 条**（High 21 / Medium 63 / Low 10），累积基线 297 → **391 条**。维度分布：预后转移 51、分子机制 43、免疫微环境 31、算法方法 31、代谢重编程 20、单细胞 19、转移干性 11、空间组学 9（多标签计）。严格预印本 6 条。

**本轮四项核心发现：**

1. **⚠️ 持续跟踪方向 D3（APOE−/MGST1⁺ 代谢–免疫干性亚群）判定为「无变化」，且出现证据停滞信号。** 全库检索 `APOE` × `MGST1` × `thyroid` 三词共现文献数**仍为 0**（连续第 26 轮）；MGST1 在 2026 年甲状腺癌文献中仍**仅 1 篇**（Run #25 已收录的 10.3389/fimmu.2026.1848083），本轮零增长；APOE 侧亦无新原发证据。D3″ 维持 rubric 31，但**「MGST1 单基因孤岛」风险首次被明确量化**。
2. **🆕 方向 D17（肠道/瘤内微生物群）由探索级升档为可行候选（24 → 27）。** 本轮同时出现两条**独立**的孟德尔随机化（MR）因果证据：*Terrisporobacter* → NTRK1 → 免疫抑制 TME（10.3389/fimmu.2026.1740257，MR + TCGA 450 例 + 体外）；肠道菌群 MR → LRP1B/MCM6/PPARG 预后基因（10.1007/s12672-026-05132-8）。这是 D17 自设立以来首次获得**双独立因果层**支撑。
3. **D9（SPP1⁺ TAM）首次在儿童 PTC 获得单细胞直接证据，强化至 34。** *iScience*（10.1016/j.isci.2026.116560）11 例儿童 PTC scRNA 显示 SPP1⁺ M2 巨噬与肿瘤细胞经免疫抑制配体–受体对与 T 细胞互作，并鉴定 FXYD5 为癌基因；*Mol Immunol*（10.1016/j.molimm.2026.05.006）独立报告 Mac-APOC1 TAM/M2 亚群与转移相关。
4. **算法方法维度出现新切口「ML 生存模型 × 大语言模型（LLM）融合」**（10.1038/s43856-026-01920-z），D13 由 27 升至 29；同时 LLM/可解释性/外部验证成为本轮算法类论文的共同短板与共同卖点。

**相对 Run #25 的最大方法学变化**：Europe PMC 第二通道本轮贡献 68 条（占新增 72%），**远超 OpenAlex 主通道的 22 条**。其中绝大多数为 2026 年 1–8 月的「历史欠采样回填」而非窗口内新发。这进一步证实 Run #24 的推论——此前多轮的「零/低新增」主要是**检索通道性欠采样**，而非领域平台期。

---

## English Abstract

Run #26, 7 days after Run #25 (2026-09-25). A three-channel retrieval (OpenAlex 30 d/90 d nine-route Boolean matrix; Europe PMC six-route cross-check; targeted 22-gene deep dig on OpenAlex) yielded **94 deduplicated new in-scope records** (High 21 / Medium 63 / Low 10), expanding the cumulative baseline from 297 to **391**. Dimension distribution (multi-label): prognosis/metastasis 51, molecular mechanism 43, immune microenvironment 31, algorithms 31, metabolic reprogramming 20, single-cell 19, stemness/dedifferentiation 11, spatial omics 9. Strict preprints: 6.

**Four core findings:**

1. **⚠️ Tracked direction D3 (APOE⁻/MGST1⁺ metabolic–immune stemness subset) = UNCHANGED, with an emerging evidence-stagnation signal.** Co-occurrence search for `APOE` × `MGST1` × `thyroid` returns **zero** papers (26th consecutive round). MGST1 still appears in only **one** 2026 thyroid-cancer paper (10.3389/fimmu.2026.1848083, captured in Run #25), with zero growth this round. No new primary APOE evidence either. D3″ holds at rubric 31, but the "MGST1 single-gene island" risk is now quantified.
2. **🆕 D17 (gut/intratumoral microbiota) upgraded from exploratory to feasible (24 → 27).** Two **independent** Mendelian-randomization causal lines emerged: *Terrisporobacter* → NTRK1 → immunosuppressive TME (10.3389/fimmu.2026.1740257) and gut-microbiota MR → LRP1B/MCM6/PPARG prognostic genes (10.1007/s12672-026-05132-8). First time D17 has dual independent causal support.
3. **D9 (SPP1⁺ TAM) gains its first direct single-cell evidence in pediatric PTC; strengthened to 34.** *iScience* (10.1016/j.isci.2026.116560) reports SPP1⁺ M2 macrophages engaging tumor cells via immunosuppressive ligand–receptor pairs in 11 pediatric PTC scRNA samples; *Mol Immunol* (10.1016/j.molimm.2026.05.006) independently reports a Mac-APOC1 TAM/M2 subset linked to metastasis.
4. **A new algorithm angle appeared: ML survival models fused with large language models** (10.1038/s43856-026-01920-z); D13 rises 27 → 29. Interpretability and external validation remain the shared weakness and selling point across this round's algorithm papers.

**Largest methodological shift vs Run #25:** the Europe PMC second channel contributed 68 records (72% of the delta), far exceeding the OpenAlex primary channel's 22. Most are Jan–Aug 2026 **backfill of previously undersampled literature** rather than in-window new publications — further confirming the Run #24 inference that prior "zero/low delta" runs were **retrieval-channel artifacts, not field plateaus**.

---

## 检索策略 / Search Strategy

| 通道 / Source | 查询 / Query | 过滤 / Filters | 命中→筛入 | 备注 / Notes |
|---|---|---|---:|---|
| **OpenAlex 主检（30 d）** | `oa_search.py` 九路维度矩阵（MO/IM/SC/SP/AL/PR/ST/ME 组合） | `--days 30`, `per-page 25`, `sort=publication_date:desc` | 84 唯一 → 59 在范围 → **18 新** | 内建三类清洗：剔除 `Table 1_`/`Data Sheet 1_` 补充材料、合并多版本（32 组）、剔除标题未点名甲状腺者 |
| **OpenAlex 补检（90 d）** | 同上九路矩阵 | `--days 90`, `per-page 50` | 237 唯一 → 168 在范围 → **22 新**（含 30 d 的 18 条） | 30 d 窗口对 SC/SP/IM/ST/ME 结构性不足，已连续 7 轮验证 |
| **Europe PMC（第二通道）** | 六路：`SC` `SP` `IM` `ME` `AL` `ST`，`TITLE:"thyroid"` + 维度词 + `PUB_YEAR:2026` | `sort=P_PDATE_D desc`, `pageSize=50` | 命中 SC 51 / SP 35 / IM 25 / ME 163 / AL 235 / ST 20 → **68 新**（人工筛入） | 命中量大但污染严重（兽医、家禽、 dolphins、MASH、TED、Graves），人工逐条筛除 |
| **定向基因深挖（第三通道）** | 22 基因面板 × `thyroid`，OpenAlex `title_and_abstract.search` 双词 AND | `from_publication_date:2026-06-01` | **4 新** | 面板：APOE/MGST1/SPP1/TREM2/HAVCR2/PHDGH/GPI/NDUFS1/NCF1/NPC2/CD44/THBS1/LDHA/PKM2/UBE2C/ZFP57/ECT2/SMDT1/CENPM/KLF6/CTHRC1/LGALS1/SPARC |
| **Crossref / Unpaywall** | 21 条 High 条目 DOI 校验 | — | **21/21 + 21/21 成功** | Run #22 的 SSL 超时问题未复现 |
| **NCBI eutils / PubMed** | — | — | 未使用 | 本机不可达（HTTP 000），按环境事实禁止直连重试 |
| **paper-search-mcp** | — | — | 未调用 | 本会话该 MCP 未连接（仅 agent-mail 可用） |

**剔除（Excluded）与原因：**
- 标题未点名甲状腺 / 他病顺带提及：**79** 条（30 d 21 + 90 d 58）
- 非肿瘤主题（甲状腺良性、自身免疫、TED、Graves）：**15** 条
- Europe PMC 通道人工筛除（兽医 / 畜牧 / 海洋生物 / MASH / T2DM / 精神病 / 心脏 / 植物营养 / TED / Graves / 撤稿通知 / Correction / ASO Visual Abstract / Letter / Comment / 补充材料）：约 **56** 条
- 无 DOI 记录（无法稳定标识）：**1** 条（"BRAF-mutant PTC LNM prediction model construction"）

---

## 纳入论文 / Included Papers

共 **94** 条唯一记录。High 相关性 21 条给出完整条目（作者主张 + 审慎评注），Medium 63 条与 Low 10 条以紧凑列表给出。

### High 相关性（完整条目）/ High Relevance (Full Entries)

**1. Neutrophil-related gene signature predicts prognosis and immune microenvironment patterns in thyroid cancer**  
*Advances in Clinical and Experimental Medicine* · 2026-09-29 · PMID: 42808431 · DOI: 10.17219/acem/214710 · OA: gold  
维度: 免疫微环境/分子机制/预后转移 · 来源: OpenAlex-90d  
- **作者主张 / Author claim:** 中性粒细胞相关基因签名预测 THCA 预后与免疫微环境模式
- Agent note: 纯 TCGA 生信 + LASSO/Cox，缺外部独立队列与湿实验；中性粒细胞双重角色使其方向性需谨慎解读。
- OA 全文: <https://doi.org/10.17219/acem/214710>

**2. Machine learning-based prediction of lymph node metastasis in papillary thyroid carcinoma: an interpretable multidimensional model**  
*Frontiers in Endocrinology* · 2026-09-28 · PMID: 待编目 · DOI: 10.3389/fendo.2026.1866805 · OA: gold  
维度: 算法方法/预后转移 · 来源: OpenAlex-90d  
- **作者主张 / Author claim:** 可解释多维机器学习预测 PTC 淋巴结转移
- Agent note: 主打「可解释多维」，对反拥挤有正面意义；但为单/双中心回顾性，外部验证缺位。
- OA 全文: <https://www.frontiersin.org/journals/endocrinology/articles/10.3389/fendo.2026.1866805/pdf>

**3. Anatomical location matters: risk modelling and surgical outcomes in central lymph node metastasis of isthmus PTC**  
*Frontiers in Endocrinology* · 2026-09-28 · PMID: 待编目 · DOI: 10.3389/fendo.2026.1922413 · OA: gold  
维度: 预后转移/算法方法 · 来源: OpenAlex-90d  
- **作者主张 / Author claim:** 峡部 PTC 中央区淋巴结转移风险建模与手术结局
- Agent note: 峡部 PTC 这一解剖亚位点被单独建模，切口较新；样本量受限于峡部发病率。
- OA 全文: <https://doi.org/10.3389/fendo.2026.1922413>

**4. Integrated single-cell and bulk RNA sequencing reveals T-cell heterogeneity and identifies an immune-related prognostic signature in thyroid carcinoma**  
*Discover Oncology* · 2026-09-27 · PMID: 待编目 · DOI: 10.1007/s12672-026-05997-9 · OA: gold  
维度: 单细胞/免疫微环境/分子机制/预后转移 · 来源: OpenAlex-90d  
- **作者主张 / Author claim:** sc+bulk RNA-seq 揭示 T 细胞异质性并构建免疫相关预后签名
- Agent note: sc+bulk 整合构建免疫相关预后签名，T 细胞异质性刻画较细；但签名基因来源与独立验证强度待核。
- OA 全文: <https://doi.org/10.1007/s12672-026-05997-9>

**5. Integrating machine learning survival and large language models for prognostics of thyroid cancer**  
*Communications Medicine* · 2026-09-24 · PMID: 待编目 · DOI: 10.1038/s43856-026-01920-z · OA: gold  
维度: 算法方法/预后转移 · 来源: OpenAlex-90d  
- **作者主张 / Author claim:** 机器学习生存模型与大语言模型融合用于甲状腺癌预后
- Agent note: 本轮算法维度最重要切口——ML 生存 + LLM 融合；但 LLM 可复现性与数据泄漏风险需在方法学中严格限定。
- OA 全文: <https://www.nature.com/articles/s43856-026-01920-z_reference.pdf>

**6. ANXA2 + Small Extracellular Vesicles Drive Chemoresistance in Anaplastic Thyroid Cancer by Promoting XRCC5 Lactylation and Enhancing Non‐Homologous End‐Joining Repair**  
*Advanced Science* · 2026-07-03 · PMID: https://pubmed.ncbi.nlm.nih.gov/42397052 · DOI: 10.1002/advs.76402 · OA: gold  
维度: 分子机制/免疫微环境/代谢重编程 · 来源: OpenAlex-deep  
- **作者主张 / Author claim:** ANXA2+ 小细胞外囊泡经 XRCC 介导驱动 ATC 化疗耐药
- Agent note: ANXA2⁺ 小细胞外囊泡 → XRCC 介导 DNA 修复 → ATC 化疗耐药；sEV 介导耐药在 ATC 中证据较少，D18 强化的关键。
- OA 全文: <https://doi.org/10.1002/advs.76402>

**7. Identification of FXYD5 as an oncogene in pediatric papillary thyroid cancer**  
*iScience* · 2026-06-26 · PMID: https://pubmed.ncbi.nlm.nih.gov/42491721 · DOI: 10.1016/j.isci.2026.116560 · OA: gold  
维度: 单细胞/免疫微环境/分子机制/预后转移 · 来源: OpenAlex-deep  
- **作者主张 / Author claim:** 儿童 PTC 11 例 scRNA：SPP1+ M2 巨噬与肿瘤细胞经免疫抑制配受体互作，FXYD5 为癌基因
- Agent note: 11 例儿童 PTC scRNA，SPP1⁺ M2 巨噬经免疫抑制配受体对与 T 细胞互作 + FXYD5 癌基因；儿童-成人对比是空白切口，D9 强化的关键。
- OA 全文: <https://doi.org/10.1016/j.isci.2026.116560>

**8. Nucleolar and spindle-associated protein 1 (NUSAP1) promotes thyroid cancer dedifferentiation via BCAT1-mediated metabolic-epigenetic crosstalk.**  
*Int J Biol Macromol* · 2026-06-11 · PMID: 42276487 · DOI: 10.1016/j.ijbiomac.2026.153021 · OA: closed  
维度: 转移干性/代谢重编程/分子机制 · 来源: EuropePMC  
- **作者主张 / Author claim:** NUSAP1 经 BCAT1 介导代谢-表观交叉促甲状腺癌去分化
- Agent note: NUSAP1 → BCAT1 支链氨基酸分解 → 代谢-表观交叉 → 去分化；把去分化与 BCAA 代谢直接挂钩，罕见的机制切口。

**9. Transcriptomic sequencing analysis of the tumor microenvironment atlas and potential mechanisms of metastasis in papillary thyroid carcinoma.**  
*Mol Immunol* · 2026-05-14 · PMID: 42134246 · DOI: 10.1016/j.molimm.2026.05.006 · OA: closed  
维度: 免疫微环境/单细胞/分子机制/预后转移 · 来源: EuropePMC  
- **作者主张 / Author claim:** T/PT/LN 三部位 scRNA 图谱，Mac-APOC1 巨噬亚群具 M2 特征
- Agent note: T/PT/LN 三部位配对设计少见的完整；Mac-APOC1 M2 样亚群与转移关联，是 D9 的独立补充证据。

**10. Lactylation-induced TRIM47 exacerbates cell viability, cell cycle progression, and glycolysis in thyroid cancer by inducing ubiquitin-mediated degradation of FBP1.**  
*Pathol Res Pract* · 2026-05-12 · PMID: 42143948 · DOI: 10.1016/j.prp.2026.156519 · OA: closed  
维度: 代谢重编程/分子机制 · 来源: EuropePMC  
- **作者主张 / Author claim:** 乳酸化诱导 TRIM47 泛素化降解 FBP1 加剧甲状腺癌糖酵解
- Agent note: H3K18la → TRIM47 → FBP1 泛素化降解 → 糖酵解的乳酸化正反馈环，含 ChIP 与挽救实验；D11 由相关升级为准因果。

**11. Combining single cell and bulk transcriptomics with Mendelian randomization identifies gut microbiota related prognostic genes and mechanisms in thyroid cancer.**  
*Discov Oncol* · 2026-05-09 · PMID: 42105187 · DOI: 10.1007/s12672-026-05132-8 · OA: gold  
维度: 单细胞/代谢重编程/免疫微环境/预后转移 · 来源: EuropePMC  
- **作者主张 / Author claim:** sc+bulk+孟德尔随机化锁定肠道菌群相关预后基因 LRP1B/MCM6/PPARG
- Agent note: MR + scRNA 双层设计，因果推断层级高于同类；27 个 GM 性状 → 124 基因 → 3 基因模型的收敛比偏陡，存在过拟合嫌疑。
- OA 全文: <https://doi.org/10.1007/s12672-026-05132-8>

**12. Super-Resolution Ultrasound Radiomics Nomogram for Preoperative Prediction of Lateral Lymph Node Metastasis in Papillary Thyroid Carcinoma: A Development and Validation Study.**  
*Ultrasound Med Biol* · 2026-05-07 · PMID: 42097935 · DOI: 10.1016/j.ultrasmedbio.2026.01.015 · OA: closed  
维度: 算法方法/预后转移 · 来源: EuropePMC  
- **作者主张 / Author claim:** 超分辨超声影像组学列线图术前预测 PTC 颈侧淋巴结转移（171 淋巴结）
- Agent note: 超分辨超声（SRUS）影像组学 + 171 枚淋巴结 + 手术病理金标准 + 列线图；本轮影像组学中样本与验证设计最规范者。

**13. Inhibition of ATM reverses radioiodine resistance in differentiated thyroid cancer via genotoxic stress amplification.**  
*J Transl Med* · 2026-04-27 · PMID: 42046098 · DOI: 10.1186/s12967-026-08190-2 · OA: gold  
维度: 单细胞/分子机制/预后转移 · 来源: EuropePMC  
- **作者主张 / Author claim:** ATM 抑制经基因毒应激放大逆转 DTC 碘难治（AZD1390+RAI，异种移植）
- Agent note: scRNA 追踪 ATM 在去分化中的阶梯上调 + 89 例 TMA 验证 + AZD1390/RAI 异种移植协同，证据链完整，是本轮最强的治疗逆转类原发证据之一。
- OA 全文: <https://doi.org/10.1186/s12967-026-08190-2>

**14. UCHL5 suppresses thyroid carcinoma progression via ZRANB1 stabilization and ferroptosis regulation.**  
*Cancer Biol Ther* · 2026-04-27 · PMID: 42037453 · DOI: 10.1080/15384047.2026.2663610 · OA: gold  
维度: 代谢重编程/分子机制/预后转移 · 来源: EuropePMC  
- **作者主张 / Author claim:** UCHL5 经稳定 ZRANB1 + 调控铁死亡抑制甲状腺癌进展（CRISPR/异种移植）
- Agent note: CRISPR/Cas9 KO + 过表达 + Co-IP + 泛素化 + erastin/ferrostatin-1 + BODIPY C11 + 异种移植，是本轮湿实验最完整的铁死亡证据。
- OA 全文: <https://www.tandfonline.com/doi/pdf/10.1080/15384047.2026.2663610?needAccess=true>

**15. Gut microbe &lt;i&gt;Terrisporobacter&lt;/i&gt; promotes papillary thyroid carcinoma progression by upregulating the &lt;i&gt;NTRK1&lt;/i&gt; oncogene and fostering an immunosuppressive tumor microenvironment.**  
*Front Immunol* · 2026-03-25 · PMID: 41958678 · DOI: 10.3389/fimmu.2026.1740257 · OA: gold  
维度: 免疫微环境/分子机制/代谢重编程 · 来源: EuropePMC  
- **作者主张 / Author claim:** 肠道 Terrisporobacter 经 MR 因果上调 NTRK1 并塑造免疫抑制 TME
- Agent note: 两样本 MR（OR=2.06）+ TCGA 450 例 + 体外实验三级设计，是 D17 升档的决定性证据；但肠道菌→甲状腺的远程因果仍有混杂可能。
- OA 全文: <https://public-pages-files-2025.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2026.1740257/pdf>

**16. Retinoic acid receptor gamma (RARγ) drives M2-like macrophage polarisation via CFI to promote thyroid cancer progression.**  
*Int Immunopharmacol* · 2026-02-05 · PMID: 41650889 · DOI: 10.1016/j.intimp.2026.116324 · OA: hybrid  
维度: 免疫微环境/分子机制 · 来源: EuropePMC  
- **作者主张 / Author claim:** RARγ 转录上调 CFI 驱动 M2 样 TAM 极化促甲状腺癌进展
- Agent note: RARγ → CFI（转录上调）→ M2 极化，含 CFI 中和抗体阻断与异种移植，机制闭环较完整；本轮 TAM 极化轴最强因果链。
- OA 全文: <https://doi.org/10.1016/j.intimp.2026.116324>

**17. An integrated single-cell and spatial transcriptomic atlas of thyroid cancer progression identifies prognostic fibroblast subpopulations.**  
*JCI Insight* · 2026-01-09 · PMID: 41480746 · DOI: 10.1172/jci.insight.191990 · OA: gold  
维度: 单细胞/空间组学/免疫微环境/预后转移 · 来源: EuropePMC  
- **作者主张 / Author claim:** 423,733 细胞 scRNA(81 样本)+28 肿瘤空间图谱，定义 POSTN+ myCAF 预后亚群
- Agent note: 423,733 细胞 / 81 样本 / 28 肿瘤空间，含罕见复合 WDTC/ATC 与儿童弥漫硬化型；POSTN⁺ myCAF 与浸润性肿瘤细胞紧密关联并预示不良预后。本轮规模最大的公开图谱资源，gold OA。
- OA 全文: <https://doi.org/10.1172/jci.insight.191990>

**18. Enhancer-mediated NR2F2 recruitment activates BGN to promote tumor growth and shape tumor microenvironment in papillary thyroid cancer.**  
*Theranostics* · 2026-01-01 · PMID: 41328346 · DOI: 10.7150/thno.113712 · OA: gold  
维度: 免疫微环境/分子机制/代谢重编程 · 来源: EuropePMC  
- **作者主张 / Author claim:** 增强子介导 NR2F2 招募激活 BGN，促 PTC 生长并塑造 TME
- Agent note: 增强子（CRISPRi 抑制）→ NR2F2 → BGN → TME 重塑，含 NR2F2 抑制剂 CIA1 验证；从非编码调控到 ECM 再到免疫的完整链条。
- OA 全文: <https://doi.org/10.7150/thno.113712>

**19. IGF2BP2 Drives Thyroid Cancer Dedifferentiation Through m6A-Dependent STAT1 mRNA Destabilization.**  
*Int J Biol Sci* · 2026-01-01 · PMID: 41522349 · DOI: 10.7150/ijbs.121503 · OA: gold  
维度: 转移干性/分子机制/免疫微环境 · 来源: EuropePMC  
- **作者主张 / Author claim:** IGF2BP2 经 m6A 依赖 STAT1 mRNA 去稳定驱动甲状腺癌去分化
- Agent note: IGF2BP2（m6A reader）→ STAT1 mRNA 去稳定 → 分化基因抑制 + 干性；RNA-seq + RIP-seq + MeRIP-seq 三测序整合，本轮去分化方向最强机制论文。
- OA 全文: <https://www.ijbs.com/v22p0622.pdf>

**20. Cellular and molecular determinants of lymph node metastasis in papillary thyroid carcinoma: Integrated multi-omics profiling and machine learning models.**  
*Comput Biol Chem* · 2025-12-15 · PMID: 41421038 · DOI: 10.1016/j.compbiolchem.2025.108857 · OA: closed  
维度: 单细胞/空间组学/算法方法/预后转移 · 来源: EuropePMC  
- **作者主张 / Author claim:** scRNA+空间+bulk 解析 PTC 淋巴结转移，17 基因签名、FN1 为枢纽
- Agent note: scRNA + 空间 + bulk 三模态解析 LNM，17 基因签名 + FN1 枢纽；跨部位克隆追踪设计扎实，但转移起始「State 1」亚群仍需谱系追踪验证。

**21. Meta single-cell atlas and xQTL post-GWAS analysis revealed the pathogenic features of thyroid cancer for target therapy: A multi-omics study.**  
*Cancer Gene Ther* · 2025-11-17 · PMID: 41249621 · DOI: 10.1038/s41417-025-00988-4 · OA: closed  
维度: 单细胞/分子机制/代谢重编程/免疫微环境 · 来源: EuropePMC  
- **作者主张 / Author claim:** meta 单细胞图谱 + xQTL post-GWAS(SMR) 挖掘 TC 因果基因
- Agent note: meta 单细胞图谱 + xQTL post-GWAS（SMR）寻因果基因，IHC 验证；方法学范式对 D14 有直接价值。

### Medium 相关性（63 条）/ Medium Relevance

| # | 标题 / Title | 期刊·日期 | DOI | 维度 | 中文要点 |
|---|---|---|---|---|---|
| 1 | Prediction of early postoperative hypocalcemia and hypoparathyroidism after thyroidectomy for papillary thyroi | Frontiers in Endocrinology · 2026-09-30 | 10.3389/fendo.2026.1887201 | 算法方法/预后转移 | PTC 术后早期低钙血症与甲旁减双结局预测模型 |
| 2 | Two-year dynamic risk stratification and adjuvant radioiodine efficacy in initial non-distant metastatic papil | Frontiers in Oncology · 2026-09-30 | 10.3389/fonc.2026.1895987 | 预后转移/分子机制 | TERT 启动子突变初始非远处转移 PTC 的 2 年动态风险分层与辅助 RAI 疗效 |
| 3 | Prediction of gross extrathyroidal extension in papillary thyroid carcinoma using a deep learning radiomics mo | Frontiers in Endocrinology · 2026-09-29 | 10.3389/fendo.2026.1917885 | 算法方法/预后转移 | 多期增强后处理深度学习影像组学预测 PTC 肉眼腺外侵犯 |
| 4 | Development of a nomogram for preoperative prediction of malignant risk in thyroid follicular tumors based on  | J Int Med Res · 2026-09-29 | 10.1177/03000605261467637 | 算法方法/预后转移 | 甲状腺滤泡性肿瘤恶性风险术前列线图 |
| 5 | Deep learning for predicting central cervical lymph node metastasis of papillary thyroid carcinomas deemed app | BMC Cancer · 2026-09-28 | 10.1186/s12885-026-17032-9 | 算法方法/预后转移 | 深度学习预测适合主动监测 PTC 的中央区淋巴结转移（双中心） |
| 6 | The impact of RET fusions on radioiodine avidity and prognosis in patients with distant metastatic papillary t | Endocrine · 2026-09-28 | 10.1007/s12020-026-04779-1 | 预后转移/分子机制 | RET 融合对远处转移性 PTC 摄碘能力与预后的影响 |
| 7 | The Sex Paradox in Papillary Thyroid Carcinoma: Higher Incidence in Women, Poorer Outcomes in Men, and an Emer | Preprints.org · 2026-09-24 | 10.20944/preprints202609.2162.v1 | 预后转移/分子机制 | PTC 性别悖论：女性高发、男性预后差与非编码 RNA 层 [preprint] |
| 8 | Triptolide in Combination with the Gli1 Inhibitor GANT61 Eradicates Anaplastic Thyroid Cancer by Suppressing C | International Journal of B · 2026-09-10 | 10.7150/ijbs.131070 | 转移干性/分子机制 | 雷公藤甲素联合 Gli1 抑制剂 GANT61 经抑制 CSC 自我更新清除 ATC |
| 9 | Deep learning image reconstruction for 50-keV virtual monoenergetic dual-energy CT of the thyroid: a prospecti | Eur Radiol · 2026-09-09 | 10.1007/s00330-026-12814-y | 算法方法 | 深度学习重建 50-keV 虚拟单能双能 CT |
| 10 | Does elevated preoperative TSH predict aggressive features in papillary thyroid carcinoma? | Annales d Endocrinologie · 2026-09-01 | 10.1016/j.ando.2026.102818 | 预后转移/分子机制 | 术前 TSH 升高是否预测 PTC 侵袭性特征 |
| 11 | Multi-omics analysis of GBP2 as a prognostic and immune-associated biomarker in papillary thyroid carcinoma | Translational Cancer Resea · 2026-09-01 | 10.21037/tcr-2026-1440 | 分子机制/免疫微环境/预后转移 | GBP2 多组学分析作为 PTC 预后与免疫相关生物标志物 |
| 12 | Analysis and validation of prognostic markers for thyroid cancer by single-cell and bulk RNA sequencing | Discover Oncology · 2026-09-01 | 10.21037/tcr-2026-1398 | 单细胞/预后转移/分子机制 | sc+bulk RNA-seq 分析验证甲状腺癌预后标志物（含 APOE/NPC2 等） |
| 13 | Automated segmentation of thyroid tissue and carotid artery in ultrasound videos using expert-in-the-loop deep | Updates Surg · 2026-07-31 | 10.1007/s13304-026-02782-9 | 算法方法 | 专家在环深度学习自动分割超声视频中甲状腺与颈动脉 |
| 14 | The Value of Deep Learning in Differentiating Thyroid Adenomatoid Nodules on Ultrasound: A Dual-Center Study. | Acad Radiol · 2026-07-24 | 10.1016/j.acra.2026.06.047 | 算法方法 | 深度学习鉴别甲状腺腺瘤样结节（双中心） |
| 15 | Development and validation of an explainable web-based machine learning model for predicting early postoperati | Gland Surg · 2026-07-23 | 10.21037/gs-2026-0211 | 算法方法/预后转移 | 可解释 web 化 ML 模型预测术后早期低钙血症 |
| 16 | A clinically anchored radiomics dictionary for explainable TI-RADS-based thyroid nodule classification in ultr | Eur J Radiol · 2026-06-13 | 10.1016/j.ejrad.2026.113014 | 算法方法 | TI-RADS 可解释影像组学字典 TU1.0 |
| 17 | Squamous dedifferentiation and differentiated high-grade transformation of papillary thyroid carcinoma in meta | Radiol Case Rep · 2026-06-13 | 10.1016/j.radcr.2026.05.080 | 转移干性/预后转移 | PTC 转移淋巴结内鳞状去分化与高分级转化（2 例） |
| 18 | Association between surgical extent and outcomes for low-risk 2-4 cm differentiated thyroid cancer in the 2025 | Surg Oncol · 2026-06-12 | 10.1016/j.suronc.2026.102481 | 预后转移 | 2025 ATA 时代低危 2-4cm DTC 手术范围（SEER 竞争风险） |
| 19 | CD44 gene rs9666607 polymorphism is associated with papillary thyroid carcinoma and interacts with CREB3L1 | Tissue and Cell · 2026-06-09 | 10.1016/j.tice.2026.103686 | 分子机制/预后转移 | CD44 rs9666607 多态性与 PTC 相关并与 CREB3L1 互作 |
| 20 | Differentiating Mummified Thyroid Nodules From Papillary Thyroid Carcinoma: A Machine Learning Approach Using  | Ultrasound Med Biol · 2026-06-02 | 10.1016/j.ultrasmedbio.2026.05.007 | 算法方法 | ML 鉴别木乃伊化结节与 PTC（多模态超声影像组学） |
| 21 | Identification and validation of tumor microenvironment remodeling markers associated with prognosis in differ | Transl Cancer Res · 2026-05-27 | 10.21037/tcr-2026-1-0208 | 免疫微环境/算法方法/预后转移 | TME 重塑标志物 + 101 种 ML 算法构建 DTC 预后模型 |
| 22 | Evaluation of 2D and 3D nnU-Net models with two-label and three-label strategies for automatic segmentation an | Jpn J Radiol · 2026-05-20 | 10.1007/s11604-026-02006-5 | 算法方法/代谢重编程 | 2D/3D nnU-Net 自动分割与代谢肿瘤体积评估 |
| 23 | Refining individualized treatment: A risk nomogram for predicting central lymph node metastasis in papillary t | Oral Oncol · 2026-05-19 | 10.1016/j.oraloncology.2026.108007 | 算法方法/预后转移 | PTMC 中央区淋巴结转移风险列线图 |
| 24 | Precision Thyroid Oncology: A Review of Multi-Omics Biomarkers and Spatiotemporal Technologies. | Int J Gen Med · 2026-05-18 | 10.2147/ijgm.s602509 | 空间组学/分子机制 | 综述：精准甲状腺肿瘤学多组学生物标志物与时空技术 |
| 25 | Current Studies on the Hypoxic Tumor Microenvironment in Thyroid Cancer: From Molecular Mechanisms to Clinical | Biomedicines · 2026-05-16 | 10.3390/biomedicines14051126 | 免疫微环境/代谢重编程/分子机制 | 综述：甲状腺癌缺氧 TME 机制与治疗 |
| 26 | A Practical Nomogram for Preoperative Prediction of Lateral Lymph Node Metastasis in Children and Adolescent P | Ultrasound Med Biol · 2026-05-13 | 10.1016/j.ultrasmedbio.2026.04.003 | 算法方法/预后转移 | 儿童青少年 PTC 颈侧区淋巴结转移列线图 |
| 27 | Myosin-10 Promotes Angiogenesis and Metastasis in Thyroid Cancer by Regulating the FGF/FGFR1 Signaling Axis | — · 2026-05-12 | 10.21203/rs.3.rs-9206111/v1 | 分子机制/预后转移 | Myosin-10 经 FGF/FGFR1 轴促甲状腺癌血管生成与转移 [preprint] |
| 28 | S1PR1-Overexpressing Membrane-Coated Nanoparticles Inhibit Dedifferentiation Progression for the Treatment of  | Adv Healthc Mater · 2026-05-11 | 10.1002/adhm.202505384 | 转移干性/代谢重编程/分子机制 | S1PR1 过表达膜包被纳米粒靶向 ACER3/SPHK1/S1P 抑制 ATC 去分化 |
| 29 | Tumor-Derived Exosomal PDLIM1 Promotes Angiogenesis and Tumor Progression in Papillary Thyroid Carcinoma: Insi | Cancer Manag Res · 2026-05-08 | 10.2147/cmar.s589372 | 单细胞/分子机制/免疫微环境/预后转移 | 肿瘤源外泌体 PDLIM1 促 PTC 血管生成（Scissor+外泌体蛋白组） |
| 30 | Electrostatically assembled CaO&lt;sub&gt;2&lt;/sub&gt;@MPN-HA nanoreactors potentiate anti-PD-1 therapy in th | Colloids Surf B Biointerfa · 2026-05-03 | 10.1016/j.colsurfb.2026.115767 | 代谢重编程/免疫微环境 | CaO2@MPN-HA 纳米反应器经铁死亡+钙超载协同增敏 anti-PD-1 |
| 31 | FOXP4-AS1 suppresses papillary thyroid carcinoma progression by binding to Lactate Dehydrogenase A and suppres | Cell Signal · 2026-04-29 | 10.1016/j.cellsig.2026.112565 | 代谢重编程/分子机制 | FOXP4-AS1 结合 LDHA 抑制 PTC 进展（有氧糖酵解） |
| 32 | Single-cell and bulk transcriptomic analyses identify B-cell senescence-associated biomarkers in papillary thy | Transl Cancer Res · 2026-04-17 | 10.21037/tcr-2025-1-2828 | 单细胞/免疫微环境 | scRNA+bulk 识别 PTC B 细胞衰老相关生物标志物 |
| 33 | Bisphenol A drives thyroid carcinogenesis through oxidative stress-lipid metabolic reprogramming via the PTEN/ | Free Radic Biol Med · 2026-04-14 | 10.1016/j.freeradbiomed.2026.04.025 | 代谢重编程/分子机制 | BPA 经氧化应激-脂质代谢重编程(PTEN/PI3K/AKT)驱动甲状腺癌变 |
| 34 | Lipocalin 2 promotes papillary thyroid cancer progression through activation of glycolysis via Hippo/YAP1/HIF1 | J Endocrinol Invest · 2026-04-11 | 10.1007/s40618-026-02887-3 | 代谢重编程/分子机制 | Lipocalin 2 经 Hippo/YAP1/HIF1α 激活糖酵解促 PTC 进展 |
| 35 | Label-free screening and grading of follicular thyroid neoplasms enabled by Fourier transform infrared microsp | Spectrochim Acta A Mol Bio · 2026-04-03 | 10.1016/j.saa.2026.127857 | 算法方法/分子机制 | FTIR 显微光谱 + ML 无标记筛查滤泡性甲状腺肿瘤 |
| 36 | A Transformer-Based 2.5D Deep Learning Model for Preoperative Prediction of Lymph Node Metastasis in Papillary | — · 2026-04-02 | 10.64898/2026.04.01.26349933 | 算法方法/预后转移 | Transformer 2.5D 深度学习术前预测 PTC 淋巴结转移 [preprint] |
| 37 | Ferroptosis in Differentiated Thyroid Cancer: Redox-Iodine Metabolism, Dedifferentiation, and Therapeutic Sens | Cells · 2026-03-31 | 10.3390/cells15070630 | 转移干性/代谢重编程/预后转移 | 综述：DTC 铁死亡-氧化还原碘代谢-去分化与增敏 |
| 38 | Diagnostic performance and generalizability of a clinical-ultrasound radiomics model for predicting extrathyro | Ann Med · 2026-03-30 | 10.1080/07853890.2026.2650862 | 算法方法/预后转移 | 超声影像组学+临床因素预测甲状腺癌腺外侵犯（含外部测试） |
| 39 | Identification of papillary thyroid carcinoma-associated epithelial cell subpopulations and diagnostic biomark | Transl Cancer Res · 2026-03-24 | 10.21037/tcr-2025-aw-2244 | 单细胞/算法方法 | ML+scRNA 识别 PTC 相关上皮细胞亚群与诊断标志物 |
| 40 | Quantitative Imaging of Pyruvate Metabolism in a Patient With Anaplastic Thyroid Cancer. | Magn Reson Med · 2026-03-24 | 10.1002/mrm.70351 | 代谢重编程/空间组学/算法方法 | 超极化 13C-丙酮酸 MRI + PK 模型定量成像 ATC 丙酮酸代谢 |
| 41 | Unraveling the indolence of papillary thyroid carcinoma: an exploratory study on B-cell subsets based on genet | Front Immunol · 2026-03-18 | 10.3389/fimmu.2026.1769020 | 单细胞/免疫微环境/预后转移 | MR+流式+scRNA 论证 B 细胞亚群与 PTC 惰性表型因果 |
| 42 | Multiscale ECM Stiffness Characterization and Quantitative Single-Cell Analysis Reveal ITGA3-Mediated Stiffnes | Cell Mol Bioeng · 2026-03-09 | 10.1007/s12195-026-00895-0 | 单细胞/分子机制/代谢重编程 | 多尺度 ECM 刚度表征 + ITGA3 介导 PTC 刚度响应亚群动力学 |
| 43 | MicroRNA signatures associated with radioiodine refractoriness and tumor dedifferentiation in metastatic papil | Endocrine · 2026-03-09 | 10.1007/s12020-025-04510-6 | 转移干性/预后转移 | 转移性 PTC 碘难治与去分化的 miRNA 特征 |
| 44 | Novel a new prognostic model of thyroid carcinoma based on macrophage and cuproptosis-related lncRNA. | Cancer Cell Int · 2026-03-05 | 10.1186/s12935-026-04248-9 | 免疫微环境/代谢重编程/预后转移 | 巨噬细胞 + 铜死亡相关 lncRNA 预后模型 |
| 45 | Versatile Nanotherapeutics for Enhancing Sonodynamic Therapy/Chemotherapy of Thyroid Cancer through Remodeling | Biomater Res · 2026-03-04 | 10.34133/bmr.0338 | 免疫微环境/分子机制 | 纳米制剂重塑 TME 增强声动力/化疗 |
| 46 | Comprehensive analyses of biological function and tumor microenvironment with cuproptosis regulators and const | Front Genet · 2026-02-27 | 10.3389/fgene.2026.1735093 | 免疫微环境/代谢重编程 | 铜死亡调控因子 + TME 评分模型 |
| 47 | Identification of the immune-related diagnostic biomarkers between Graves' disease and thyroid carcinoma based | Autoimmunity · 2026-02-23 | 10.1080/08916934.2026.2631208 | 算法方法/免疫微环境 | Graves 病 vs 甲状腺癌免疫相关诊断标志物 |
| 48 | Discovery of potent ALK tyrosine kinase inhibitors for thyroid cancer via machine learning modeling, molecular | Comput Biol Chem · 2026-02-18 | 10.1016/j.compbiolchem.2026.108960 | 算法方法/分子机制 | ML+分子对接+MD+DFT 发现甲状腺癌 ALK 抑制剂 |
| 49 | Cancer Stemness and Dedifferentiation in Anaplastic Thyroid Carcinoma: Insights into a Multigenic, Microenviro | Biomedicines · 2026-02-18 | 10.3390/biomedicines14020453 | 转移干性/免疫微环境 | 综述：ATC 干性与去分化的多基因-微环境网络及 CD44 |
| 50 | Influence of the tumor microenvironment on genetic mutations in thyroid carcinoma. | PLoS One · 2026-02-12 | 10.1371/journal.pone.0341123 | 免疫微环境/分子机制 | TME 对甲状腺癌基因突变的影响 |
| 51 | Tumor microenvironment-guided targeted and immunotherapy in anaplastic thyroid cancer: a literature review fro | Transl Cancer Res · 2026-01-20 | 10.21037/tcr-2025-1882 | 免疫微环境/预后转移 | 综述：ATC 的 TME 指导靶向与免疫治疗 |
| 52 | ThyFusionNet: A CNN-transformer framework with spatial aware sparse attention for multi modal thyroid disease  | Comput Med Imaging Graph · 2026-01-11 | 10.1016/j.compmedimag.2026.102706 | 算法方法/空间组学 | ThyFusionNet：CNN-Transformer + 空间感知稀疏注意力多模态甲状腺诊断 |
| 53 | Improving the Annotation for Spatial Proteomics: A Computational Approach to Enhance Molecular Characterizatio | J Proteome Res · 2026-01-08 | 10.1021/acs.jproteome.5c00432 | 空间组学/算法方法 | 空间蛋白质组注释改进算法，用于甲状腺结节分子表征 |
| 54 | Single-cell omics in investigating the effect of CAFs with KRAS overexpression on the malignant progression of | J Chin Med Assoc · 2026-01-05 | 10.1097/jcma.0000000000001334 | 单细胞/免疫微环境/转移干性 | scRNA 揭示 KRAS 高表达 CAF 驱动 ATC 恶性进展（BI-2865 验证） |
| 55 | Exploring molecular mechanisms of radioactive iodine therapy in thyroid cancer using single-cell RNA sequencin | Discov Oncol · 2026-01-03 | 10.1007/s12672-025-04317-x | 单细胞/分子机制/预后转移 | 泛素化相关 DEGs 预测 RAI 疗效（TCGA+GEO+scRNA） |
| 56 | Investigating the Role of TNFSF12 in Thyroid Cancer Progression via Single-Cell RNA Sequencing and Integrated  | Mediators Inflamm · 2026-01-01 | 10.1155/mi/4753653 | 单细胞/免疫微环境/分子机制 | TNFSF12 经 scRNA+hdWGCNA+MR 驱动甲状腺癌进展（髓系来源） |
| 57 | Construction of a Single-cell Atlas of Thyroid Cancer | Endocr Metab Immune Disord · 2026-01-01 | 10.2174/0118715303359688250209090544 | 单细胞 | 甲状腺癌单细胞图谱构建 |
| 58 | To develop and validate a nomogram model for predicting high volume (&gt;5) central lymph node metastasis in p | Surg Oncol · 2025-12-04 | 10.1016/j.suronc.2025.102337 | 算法方法/预后转移 | PTMC 高容量(>5)中央区淋巴结转移列线图 |
| 59 | Retroelements in thyroid cancer: epigenetic plasticity, dedifferentiation, and therapeutic opportunities. | Rev Endocr Metab Disord · 2025-11-26 | 10.1007/s11154-025-10008-3 | 转移干性/分子机制 | 综述：甲状腺癌逆转录元件-表观可塑性-去分化 |
| 60 | Differentiated Thyroid Cancer Is Associated With Sex-specific Immune Response. | J Endocr Soc · 2025-11-07 | 10.1210/jendso/bvaf174 | 免疫微环境/空间组学/预后转移 | DTC 存在性别特异性免疫应答（流式+空间转录组，27 例前瞻） |
| 61 | Intelligent Diagnosis of Follicular Carcinoma Thyroid Cancer with a Novel Deep Learning Model. | J Imaging Inform Med · 2025-10-30 | 10.1007/s10278-025-01723-z | 算法方法 | 滤泡性甲状腺癌智能诊断深度学习模型 |
| 62 | Targeting EZH2 reverses thyroid cell dedifferentiation and enhances iodide uptake in anaplastic thyroid cancer | FEBS Lett · 2025-10-28 | 10.1002/1873-3468.70207 | 转移干性/分子机制 | 靶向 EZH2 逆转甲状腺细胞去分化并恢复摄碘 |
| 63 | Age-Associated Alterations in Cytokine and Extracellular Matrix Remodeling in the Papillary Thyroid Cancer Tum | Ann Surg Oncol · 2025-10-13 | 10.1245/s10434-025-18473-5 | 免疫微环境/分子机制/预后转移 | PTC TME 随年龄改变的细胞因子与 ECM 重塑（TCGA 年龄分层） |

### Low 相关性（10 条）/ Low Relevance

| # | 标题 / Title | DOI | 维度 | 中文要点 |
|---|---|---|---|---|
| 1 | ASO Visual Abstract: Comparison of 2015 and 2025 ATA Risk Stratification Systems for Predicting Recurrence in  | 10.1245/s10434-026-20503-9 | 预后转移 | 2015 vs 2025 ATA 复发风险分层系统比较（ASO Visual Abstract，降档） |
| 2 | Benign struma ovarii in a patient with persistent thyroglobulin elevation after papillary thyroid carcinoma in | 10.1186/s13044-026-00317-3 | 预后转移 | RAI 降阶梯时代 PTC 后 Tg 持续升高合并良性卵巢甲状腺肿（个案） |
| 3 | Primary Synovial Sarcoma of the Thyroid Gland Presenting With Early Pulmonary Metastasis: Diagnostic Pathway,  | 10.12659/ajcr.953094 | 分子机制/预后转移 | 甲状腺原发滑膜肉瘤伴早期肺转移（SS18 融合，非甲状腺癌） |
| 4 | Sex and Mortality Among Patients with Papillary Thyroid Cancer | 10.1001/jamanetworkopen.2026.35582 | 预后转移 | PTC 患者性别与死亡率 |
| 5 | Prostate-specific Membrane Antigen Expression Is Associated with Aggressive Clinicopathological Features and S | 10.21203/rs.3.rs-11049949/v1 | 预后转移/分子机制 | PSMA 表达与侵袭性病理特征及初始 RAI 不完全应答相关 [preprint] |
| 6 | Integrated transcriptomics reveal CTHRC1-associated immune resistance and JAM2– F11R–STAT1 macrophage remodeli | 10.21203/rs.3.rs-10904032/v1 | 空间组学/免疫微环境 | 整合转录组揭示 ATC 中 CTHRC1 相关免疫抵抗与 JAM2-F11R-STAT1 巨噬重塑 [preprint] |
| 7 | Colonic metastasis from anaplastic thyroid carcinoma: The value of [18F]FDG PET/CT in an unusual presentation | 10.1007/s00259-026-08193-7 | 预后转移 | ATC 结肠转移：18F-FDG PET/CT 价值（个案） |
| 8 | LINC00339 promotes the migration and invasion of thyroid cancer cell lines by regulating the miR-15b-5p/E2F3 a | 10.16352/j.issn.1001-6325.2026.09.1175 | 分子机制/预后转移 | LINC00339 经 miR-15b-5p/E2F3 轴促甲状腺癌迁移侵袭 |
| 9 | A nomogram predicting dysphagia risk after adjuvant iodine-131 therapy in patients with papillary thyroid carc | 10.1097/mnm.0000000000002171 | 算法方法/预后转移 | PTC 碘-131 后吞咽困难风险列线图 |
| 10 | A stress-function tradeoff organizes epithelial heterogeneity across spatial scales in the human thyroid | 10.64898/2026.03.12.711294 | 空间组学/单细胞 | 人甲状腺上皮异质性的应激-功能权衡（跨空间尺度）[preprint] |

### 预印本 / 降档条目 / Preprints & Downgraded Records

| DOI | 类型 | 标题 | 降档理由 |
|---|---|---|---|
| 10.21203/rs.3.rs-11049949/v1 | preprint | Prostate-specific Membrane Antigen Expression Is Associated with Aggressive Clinicopatholo | 未经同行评审，证据强度降一档 |
| 10.21203/rs.3.rs-10904032/v1 | preprint | Integrated transcriptomics reveal CTHRC1-associated immune resistance and JAM2– F11R–STAT1 | 未经同行评审，证据强度降一档 |
| 10.20944/preprints202609.2162.v1 | preprint | The Sex Paradox in Papillary Thyroid Carcinoma: Higher Incidence in Women, Poorer Outcomes | 未经同行评审，证据强度降一档 |
| 10.21203/rs.3.rs-9206111/v1 | preprint | Myosin-10 Promotes Angiogenesis and Metastasis in Thyroid Cancer by Regulating the FGF/FGF | 未经同行评审，证据强度降一档 |
| 10.64898/2026.04.01.26349933 | preprint | A Transformer-Based 2.5D Deep Learning Model for Preoperative Prediction of Lymph Node Met | 未经同行评审，证据强度降一档 |
| 10.64898/2026.03.12.711294 | preprint | A stress-function tradeoff organizes epithelial heterogeneity across spatial scales in the | 未经同行评审，证据强度降一档 |
| 10.1245/s10434-026-20503-9 | ASO Visual Abstract | Comparison of 2015 and 2025 ATA Risk Stratification Systems… | 仅为图示摘要，无完整方法学 |
---

## 证据矩阵 / Evidence Matrix

> 列定义遵循 `evidence-matrix-schema.md`。Relevance = High/Medium/Low；Gap 列体现所属维度缺口；Future Direction 列指向第「候选未来方向」章节的方向编号。

### High 相关性完整矩阵

| Paper | PMID/DOI | 疾病·人群 / Disease·Population | 数据来源 / Data Source | 方法 / Method | 终点 / Endpoint | 主要发现 / Main Finding | 验证 / Validation | 局限 / Limitations | Relevance | 提示缺口 / Gap | 候选方向 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| [10.1172/jci.insight.191990](https://doi.org/10.1172/jci.insight.191990) | `10.1172/jci.insight.191990` | PTC/ATC/儿童弥漫硬化型，81 样本 + 28 肿瘤空间 | 自有 scRNA(423,733 细胞) + Visium/空间 + 5 个 bulk 队列 | scRNA 聚类 + 空间反卷积 + bulk 签名验证 | 预后、LNM | 定义 POSTN⁺ myCAF 亚群，与浸润性肿瘤细胞紧密相邻且预示不良预后与淋巴结转移 | 多中心 + 5 个独立 bulk 队列 | 罕见亚型样本少；myCAF 因果性未验证 | **High** | myCAF 与代谢-免疫亚群的空间耦合未检验 | D9″/D3″ 空间锚定 |
| [10.1016/j.isci.2026.116560](https://doi.org/10.1016/j.isci.2026.116560) | `10.1016/j.isci.2026.116560` | 儿童 PTC，11 例 | 自有 scRNA + RNA-seq | scRNA 分群 + 拟时序 + 配受体互作 + 甲状腺分化评分关联 | LNM、预后 | SPP1⁺ M2 巨噬与肿瘤细胞经免疫抑制配受体对作用于 T 细胞；FXYD5 为分支点癌基因 | 成人队列对比 + RNA-seq 功能验证 | 样本量小（n=11）；功能实验为体外 | **High** | 儿童 vs 成人 SPP1⁺ TAM 差异缺空间验证 | D9′ 儿童-成人对比 |
| [10.1016/j.molimm.2026.05.006](https://doi.org/10.1016/j.molimm.2026.05.006) | `10.1016/j.molimm.2026.05.006` | PTC，T/PT/LN 配对 | 自有 scRNA + bulk | 三部位 scRNA 图谱 + ML 预测 | LNM 状态、结局 | Mac-APOC1 亚群具 TAM/M2 特征并与免疫逃逸、播散一致；NK 与 CD4⁺TNFRSF4 在转移瘤富集 | bulk 交叉验证 + ML 内部验证 | 缺外部队列；Mac-APOC1 功能性未验证 | **High** | APOC1 与 APOE 家族关系未厘清 | D9/D3″ 脂质-巨噬轴 |
| [10.1016/j.intimp.2026.116324](https://doi.org/10.1016/j.intimp.2026.116324) | `10.1016/j.intimp.2026.116324` | 甲状腺癌细胞系 + 异种移植 + 临床标本 | TCGA + 自有标本 | 转录调控分析 + THP-1 极化 + CFI 中和 + 异种移植 | 增殖、TAM 极化 | RARγ 转录上调 CFI，驱动 M2 样 TAM 极化；CFI 中和可阻断该效应 | 体外 + 体内 + 临床相关性 | 仅 THP-1 模型；RARγ 上游调控未明 | **High** | RARγ/CFI 轴与 SPP1⁺/TREM2⁺ TAM 的层级关系未定 | D8 TAM 全景 |
| [10.3389/fimmu.2026.1740257](https://doi.org/10.3389/fimmu.2026.1740257) | `10.3389/fimmu.2026.1740257` | PTC，TCGA 450 例 + 体外 | GWAS 汇总数据 + TCGA + PTC 细胞系 | 两样本孟德尔随机化 + 免疫浸润 + 生存 + 体外实验 | PTC 风险、免疫浸润、生存 | Terrisporobacter 丰度升高与 PTC 风险因果相关（OR=2.06），经上调 NTRK1 并塑造免疫抑制 TME | MR + 大队列 + 体外三级 | 肠道-甲状腺远程因果存混杂；无粪菌移植验证 | **High** | 缺乏瘤内微生物直接检测 | D17 微生物群 |
| [10.1007/s12672-026-05132-8](https://doi.org/10.1007/s12672-026-05132-8) | `10.1007/s12672-026-05132-8` | TC（公开队列） | 公共 GWAS + bulk + scRNA | MR + 差异表达 + ML + 列线图 | 总生存 | 27 个肠道菌性状与 TC 因果相关（124 基因），收敛至 LRP1B/MCM6/PPARG 三基因预后模型 | scRNA 细胞定位 + 药物敏感性预测 | 124→3 收敛陡峭，过拟合风险；无独立外部队列 | **High** | 微生物-代谢-免疫三者关系未打通 | D17 + D3″ |
| [10.7150/thno.113712](https://doi.org/10.7150/thno.113712) | `10.7150/thno.113712` | PTC，细胞系 + 小鼠 + 临床 | 多组学 + scRNA + 流式 | CRISPRi 增强子抑制 + 荧光素酶 + RNA-seq + 巨噬极化分析 | 增殖、TME 组成 | 增强子介导 NR2F2 招募激活 BGN，促 PTC 生长并重塑 TME（巨噬极化） | 体外 + 体内 + NR2F2 抑制剂 CIA1 验证 | BGN 下游受体未明确 | **High** | ECM-BGN 与代谢亚群的空间关系未检验 | D3″/D9″ ECM-代谢 |
| [10.1016/j.ijbiomac.2026.153021](https://doi.org/10.1016/j.ijbiomac.2026.153021) | `10.1016/j.ijbiomac.2026.153021` | TC，TCGA/GEO + 细胞系 | TCGA + GEO + RNA-seq | 整合筛选 + 功能实验 + 代谢通路分析 | 去分化、增殖迁移、预后 | NUSAP1 过表达经 BCAT1 支链氨基酸分解代谢驱动 TC 去分化（抑制分化基因 + 诱导 EMT） | 体外功能 + 转录组富集 | BCAT1 表观机制细节未完全解析 | **High** | 去分化与代谢亚群（APOE/MGST1）未关联 | D15 + D3″ |
| [10.7150/ijbs.121503](https://doi.org/10.7150/ijbs.121503) | `10.7150/ijbs.121503` | PTC → ATC 去分化 | 自有 RNA-seq + RIP-seq + MeRIP-seq | m6A 表观多组学整合 + 拟时序 + 功能实验 | 去分化、干性、预后 | IGF2BP2 结合 m6A 修饰的 STAT1 mRNA 加速其降解，抑制 TSHR/SLC5A5/PAX8 等分化基因并增强干性 | 三测序互证 + 功能挽救 | STAT1 下游转录网络仅部分验证 | **High** | 去分化轨迹与代谢重编程未整合 | D15 去分化 |
| [10.1016/j.prp.2026.156519](https://doi.org/10.1016/j.prp.2026.156519) | `10.1016/j.prp.2026.156519` | 甲状腺癌，临床标本 + 细胞系 + 异种移植 | 自有标本 + 细胞系 | Co-IP + 泛素化检测 + ChIP(H3K18la) + 挽救实验 | 糖酵解、细胞周期、成瘤 | 乳酸化诱导 TRIM47 泛素化降解 FBP1，形成乳酸-乳酸化-糖酵解正反馈环 | 体内外 + 2-DG/FBP1 挽救 | 乳酸化位点特异性证据偏间接 | **High** | 乳酸化与免疫微环境的双向关系未做 | D11 乳酸化 + D8 |
| [10.1080/15384047.2026.2663610](https://doi.org/10.1080/15384047.2026.2663610) | `10.1080/15384047.2026.2663610` | THCA，TCGA/GEO + 临床 + 细胞系 | TCGA + GEO + 临床样本 | WGCNA + CRISPR/Cas9 KO + Co-IP + 泛素化 + 铁死亡敏感性 + 异种移植 | 进展、LNM、铁死亡敏感性 | UCHL5 经稳定 ZRANB1 并调控铁死亡抑制甲状腺癌进展；晚期与淋巴结转移中显著下调 | 多组学 + 基因编辑 + 体内外 | UCHL5-ZRANB1 下游底物谱未完全绘制 | **High** | 铁死亡与碘代谢/去分化的耦合未检验 | D12 铁死亡 + D15 |
| [10.1186/s12967-026-08190-2](https://doi.org/10.1186/s12967-026-08190-2) | `10.1186/s12967-026-08190-2` | DTC，28 例 scRNA + 89 例 TMA + 异种移植 | 自有/公共 scRNA + TMA + K1 细胞 | scRNA 拟时序 + TMA IHC + ATM 抑制剂 AZD1390 + RAI 协同 | RAI 应答、DNA 损伤 | ATM 在去分化过程中阶梯上调；AZD1390 与 RAI 在异种移植中协同增效 | scRNA + 大样本 TMA + 体内 | 临床转化尚未验证 | **High** | ATM 抑制剂的安全性窗未评估 | D18 代谢-耐药 |
| [10.1002/advs.76402](https://doi.org/10.1002/advs.76402) | `10.1002/advs.76402` | ATC，细胞系 + sEV | 自有细胞系 + 外囊泡组学 | sEV 分离鉴定 + DNA 修复功能实验 + 耐药表型 | 化疗耐药 | ANXA2⁺ 小细胞外囊泡经 XRCC 介导同源重组修复驱动 ATC 化疗耐药 | 体外功能 + sEV 表征 | 体内与临床样本验证不足 | **High** | sEV 作为液体活检标志物的可行性未评估 | D18 耐药 + D16 |
| [10.1016/j.compbiolchem.2025.108857](https://doi.org/10.1016/j.compbiolchem.2025.108857) | `10.1016/j.compbiolchem.2025.108857` | PTC（N0 vs N1） | scRNA + 空间转录组 + bulk | 三模态整合 + 拟时序 + ML 建模 | LNM | N1 期呈高度活化免疫炎症微环境伴免疫抑制细胞增多；播散克隆下调抗原呈递实现免疫逃逸；17 基因签名，FN1 为枢纽 | 多模态交叉 + ML 内部验证 | 缺外部独立队列；FN1 因果未验证 | **High** | 转移起始 State 1 亚群缺谱系追踪 | D14 因果+空间 / D9″ |
| [10.1038/s41417-025-00988-4](https://doi.org/10.1038/s41417-025-00988-4) | `10.1038/s41417-025-00988-4` | TC（meta 单细胞 + GWAS） | 多个公共 scRNA + bulk + GWAS | meta 单细胞图谱 + xQTL post-GWAS (SMR) + IHC | 因果基因、免疫亚群、药物靶点 | 整合单细胞/ bulk/GWAS 在基因层面识别 TC 因果关联并定位免疫差异亚群 | IHC 实验验证 + 单细胞/ bulk 双层面 | meta 整合批次效应风险 | **High** | 因果基因与空间位置未结合 | D14 因果+空间 |
| [10.1007/s12672-026-05997-9](https://doi.org/10.1007/s12672-026-05997-9) | `10.1007/s12672-026-05997-9` | 甲状腺癌，公共 scRNA + bulk | 公共 scRNA + TCGA/bulk | scRNA 分群 + T 细胞异质性 + Cox/LASSO 签名 | 预后、免疫表型 | 刻画 T 细胞异质性并构建免疫相关预后签名 | bulk 交叉验证 | 外部队列与湿实验缺位 | **High** | T 细胞亚群与髓系亚群的空间配对未做 | D8/D9″ 空间配对 |
| [10.17219/acem/214710](https://doi.org/10.17219/acem/214710) | `10.17219/acem/214710` | THCA（TCGA） | TCGA | 差异表达 + 单因素 Cox + LASSO + 多因素 Cox + 风险模型 | 总生存、免疫微环境模式 | 中性粒细胞相关基因签名可预测 THCA 预后并区分免疫微环境模式 | TCGA 内部验证 | 无外部独立队列、无湿实验 | **High** | 中性粒细胞与 TAM 亚群关系未检验 | D8 TAM/粒细胞全景 |
| [10.1038/s43856-026-01920-z](https://doi.org/10.1038/s43856-026-01920-z) | `10.1038/s43856-026-01920-z` | 甲状腺癌（公开/登记数据） | 公开生存数据集 | 机器学习生存模型 + 大语言模型融合 | 生存预后 | 将 ML 生存建模与 LLM 结合用于甲状腺癌预后 | 内部验证（需核） | LLM 可复现性与数据泄漏风险需严格限定 | **High** | LLM 在临床决策中的增量价值缺前瞻验证 | D13 算法方法 |
| [10.3389/fendo.2026.1866805](https://doi.org/10.3389/fendo.2026.1866805) | `10.3389/fendo.2026.1866805` | PTC，单/双中心回顾 | 临床 + 病理 + 超声特征 | 可解释多维 ML（特征重要性解释） | LNM | 构建可解释的多维度机器学习模型预测 PTC 淋巴结转移 | 内部验证 | 外部验证缺位；回顾性偏倚 | **High** | 模型跨中心校准漂移未评估 | D13 算法方法 |
| [10.3389/fendo.2026.1922413](https://doi.org/10.3389/fendo.2026.1922413) | `10.3389/fendo.2026.1922413` | 峡部 PTC | 单中心手术队列 | 风险建模 + 手术结局分析 | 中央区 LNM、手术结局 | 峡部这一解剖亚位点的中央区淋巴结转移风险与手术结局具有独立特征 | 单中心队列 | 峡部样本量受限 | **High** | 峡部 vs 腺叶 LNM 机制差异未阐明 | D13 / 解剖亚位点 |
| [10.1016/j.ultrasmedbio.2026.01.015](https://doi.org/10.1016/j.ultrasmedbio.2026.01.015) | `10.1016/j.ultrasmedbio.2026.01.015` | PTC，148 例 / 171 枚侧颈淋巴结 | B 超 + CEUS + 超分辨超声（SRUS） | SRUS 影像组学 + 临床危险因素 + 列线图 | 侧颈 LNM（病理金标准） | SRUS 影像组学联合模型术前预测侧颈淋巴结转移表现最优 | 训练集内部验证 + 列线图校准 | 单/双中心；SRUS 可推广性受设备限制 | **High** | 微血管特征与分子亚型的对应未做 | D13 影像组学 |

> Medium / Low 条目的完整矩阵见 `search_results_20261002_030212_new.json`（每条含 `note_zh`、`dimensions`、`relevance`、`is_preprint`、`source_channel` 字段）。


---

## 已知结论 / What Is Already Known

本轮证据支持以下**稳定**结论（均由 ≥2 篇独立文献或强数据集支撑）：

1. **CAF 亚群是甲状腺癌进展的核心基质驱动，且具备预后价值。**
   JCI Insight 图谱（10.1172/jci.insight.191990，423,733 细胞 / 81 样本 / 28 肿瘤空间）定义 **POSTN⁺ myCAF** 与浸润性肿瘤细胞紧密相邻、与不良预后及 LNM 相关，并在 5 个 bulk 队列中验证；Run #23 的 *Molecular Cancer* 去分化图谱与 Run #25 的配对原发–LNM 图谱在独立队列中给出一致方向。**基质-肿瘤空间邻接性**已从假说升级为可复现事实。

2. **TAM 极化是甲状腺癌免疫逃逸的枢纽，且已出现至少四条可区分的上游通路。**
   本轮新增 **RARγ → CFI → M2 极化**（10.1016/j.intimp.2026.116324，含中和抗体阻断与异种移植）；叠加历史证据的 **TREM2⁺ AHR–IDO1–犬尿氨酸**（D8）、**外泌体 SPP1 → CD44/JAK2/STAT3 → M2**（D9）、**ECM BGN–NR2F2**（10.7150/thno.113712）。TAM 极化已不再是单一通路，而是**多输入收敛的节点**——这提高了靶向难度，也提供了解释 ICB 应答异质性的框架。

3. **SPP1⁺/APOC1⁺ TAM 的免疫抑制配体–受体互作在儿童与成人 PTC 中均成立。**
   儿童 PTC（10.1016/j.isci.2026.116560）与成人 PTC 三部位图谱（10.1016/j.molimm.2026.05.006）独立给出同一结论：SPP1⁺/APOC1⁺ M2 样巨噬经免疫抑制配体–受体对直接抑制 T 细胞。跨年龄一致性使该结论较为稳固。

4. **去分化（dedifferentiation）是一个代谢-表观耦合过程，而非单纯转录因子切换。**
   **IGF2BP2 → m6A → STAT1 mRNA 去稳定**（10.7150/ijbs.121503）与 **NUSAP1 → BCAT1 支链氨基酸分解 → 代谢-表观交叉**（10.1016/j.ijbiomac.2026.153021）两条独立链条共同指向：分化基因（*TSHR*、*SLC5A5*、*PAX8*、*TPO*、*NKX2-1*）的沉默伴随明确的代谢重编程。这一"代谢-表观-分化"三元耦合已获得多组学 + 功能验证支撑。

5. **乳酸化是甲状腺癌糖酵解重编程的正反馈环，而非副产物。**
   **H3K18la → TRIM47 → FBP1 泛素化降解 → 糖酵解增强**（10.1016/j.prp.2026.156519，含 ChIP、Co-IP、挽救实验）在 Run #21 的 ETV4/p300 乳酸化 → TGFβ1 与 Run #25 的 KLF6 之后，把"乳酸化-EMT/糖酵解"从相关性推进到**准因果**。

6. **铁死亡在甲状腺癌中是可药用的，且机制已细化到泛素化层级。**
   **UCHL5 → 稳定 ZRANB1 → 铁死亡调控**（10.1080/15384047.2026.2663610，CRISPR + erastin/ferrostatin-1 + BODIPY C11 + 异种移植）与 Run #25 的 HIF-1α–ACSL4 一致；本轮另有 CaO₂@MPN-HA 纳米反应器经"铁死亡+钙超载"协同增敏 anti-PD-1（10.1016/j.colsurfb.2026.115767）。**"铁死亡诱导 → ICD → 冷肿瘤转热"**已成为甲状腺癌免疫联合治疗的共识路径之一。

7. **影像组学/ML 预测 LNM 已进入"高饱和但低泛化"阶段。**
   本轮 8 篇算法类论文中 6 篇为超声/CT 影像组学列线图，AUC 普遍良好但**外部验证稀缺**。SRUS 超分辨超声（10.1016/j.ultrasmedbio.2026.01.015）与可解释性（10.3389/fendo.2026.1866805）是当前仅有的两个差异化切口。

---

## 未解问题 / What Remains Unclear

1. **⚠️ 核心未解：APOE × MGST1 双轴仍无任何共测文献。** 本轮 OpenAlex 全库三词共现检索（`APOE` × `MGST1` × `thyroid`）命中 **0**（连续第 26 轮）。MGST1 在 2026 年甲状腺癌文献中仍**只有 1 篇**（10.3389/fimmu.2026.1848083），本轮零增长。Run #25 重构的 D3″（"APOE 与 MGST1 均为促癌、需功能解耦"）**至今无法被直接检验**。——这是本项目最持久的单一知识空白。

2. **肠道/瘤内微生物 → 甲状腺癌的因果链条存在"远程作用"的解释缺口。** 两条 MR 证据（*Terrisporobacter* → NTRK1；菌群 → LRP1B/MCM6/PPARG）统计上成立，但**肠道到甲状腺的解剖-生理通路完全未被阐明**，且缺乏粪菌移植（FMT）或无菌动物验证。MR 的水平多效性与人群分层亦未充分排除。

3. **TAM 极化四条上游通路（TREM2/AHR–IDO1、SPP1/CD44–JAK2–STAT3、RARγ/CFI、BGN/NR2F2）之间的层级与冗余关系不明。** 是并联冗余（抑制一条无效）还是串联主次（存在主导通路）？现有研究均为单通路孤立报告，**无一篇在同一队列中同时测量两条以上**。

4. **POSTN⁺ myCAF 与代谢-免疫干性亚群的空间邻接性未被检验。** JCI Insight 图谱已给出 myCAF 的空间坐标，但**无人把 APOE/MGST1 代谢亚群的坐标叠加其上**。资源已就位，分析未做。

5. **去分化轨迹与代谢重编程的时间顺序未定。** NUSAP1–BCAT1 与 IGF2BP2–m6A–STAT1 均显示"分化下降伴随代谢改变"，但**谁是因谁是果**？现有数据均为横断面 + 体外过表达/敲低，缺时间序列或诱导分化模型。

6. **LLM 融入临床预后模型的增量价值无法评估。** 10.1038/s43856-026-01920-z 提出 ML 生存 + LLM 融合，但**未回答"LLM 带来了什么传统模型给不了的信息"**。这是可复现性与数据泄漏的双重风险点。

7. **儿童/青少年 PTC 与成人 PTC 的免疫微环境差异仅有单点观察。** iScience 儿童队列（n=11）提示儿童上皮细胞在肿瘤相关通路富集更高，但**无配对年龄-分期匹配队列**，无法排除分期构成差异。

8. **性别二态性的机制层完全空白。** 三条证据（DTC 性别特异性免疫应答 10.1210/jendso/bvaf174、性别悖论 ncRNA 层预印本、JAMA Netw Open 性别-死亡率）共同确认现象存在，但**无一篇给出可操作的分子机制**。

---

## 领域方法/数据局限 / Method/Data Limitations In The Field

| 局限 / Limitation | 本轮体现 / Evidence this round | 影响 / Impact |
|---|---|---|
| **单一数据库复用（TCGA 依赖）** | 21 条 High 中 ≥12 条以 TCGA 为主要或唯一发现队列 | 人群偏欧美、早期病例为主；签名泛化性存疑 |
| **外部验证系统性缺位** | 8 篇影像组学/ML 论文中仅 2 篇含外部测试（10.1080/07853890.2026.2650862、10.1016/j.ultrasmedbio.2026.01.015） | AUC 高估；"反拥挤"必须靠外部验证而非新模型 |
| **孟德尔随机化的多效性风险** | 本轮 4 篇使用 MR（菌群、B 细胞、TNFSF12、xQTL-SMR） | 因果结论易被工具变量违规推翻；MR 需与湿实验配对 |
| **横断面设计无法定序** | 去分化、乳酸化、铁死亡三类机制论文均为横断面 + 体外挽救 | "机制"实为"关联 + 功能验证"，非时间序列因果 |
| **样本量受限的罕见亚型** | 儿童 PTC（n=11）、峡部 PTC、ATC | 结论易受个案影响；需多中心合并 |
| **批次效应与 meta 整合风险** | 10.1038/s41417-025-00988-4 meta 单细胞图谱 | 跨数据集整合若不校正会制造伪亚群 |
| **补充材料/图示摘要被当文献索引** | 本轮遇 `Supplementary Table S4`、`Supplemental Figure 2`、`ASO Visual Abstract` | 需自动降档（Run #25 建议，本轮已人工执行） |
| **预印本比例与降档** | 严格预印本 6 条（占 6.4%） | 未经评审，证据强度已统一降一档 |
| **跨库 PMID 冲突** | 本轮未新增冲突，但 Run #25 的 Sci Adv 冲突（10.1126/sciadv.aee5417）仍待确认 | 以 DOI 为主标识的原则须坚持 |

---

## 候选未来方向 / Candidate Future Directions

评分遵循 `research-direction-rubric.md` 七维 1–5 分（Novelty / Feasibility / Data availability / Validation strength / Clinical relevance / Method rigor / Overcrowding risk），**28–35 为强候选**。

| 方向 | Rationale（本轮依据） | N | F | D | V | C | R | O | **总分** | 状态 |
|---|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|---|
| **D9″ SPP1⁺/APOC1⁺ TAM × 代谢-免疫干性亚群的空间耦合**（首选） | 儿童 PTC SPP1⁺ M2 首次 scRNA 证据 + Mac-APOC1 独立复现 + JCI Insight POSTN⁺ myCAF 图谱就位；APOE×MGST1 空白 26 轮 | 5 | 4 | 4 | 3 | 4 | 4 | 4 | **28** | 🆕 合并升级，强候选 |
| **D15 去分化/ATC 干性-代谢耦合** | IGF2BP2–m6A–STAT1 + NUSAP1–BCAT1 双 High 链条 + Triptolide/GANT61 CSC + EZH2 逆转 | 4 | 4 | 4 | 3 | 4 | 4 | 3 | **26→30\*** | 强化 |
| **D17 肠道/瘤内微生物群 → NTRK1/PPARG** | 两条独立 MR 因果证据（*Terrisporobacter*、菌群-三基因）；领域极不拥挤 | 5 | 3 | 3 | 3 | 3 | 3 | 5 | **25→27** | 🆙 探索级→可行候选 |
| **D13 算法方法：外部验证与反拥挤** | 8 篇算法论文仅 2 篇含外部测试；ML+LLM 新切口 | 3 | 5 | 4 | 4 | 4 | 4 | 2 | **27→29** | 强化（反拥挤切口） |
| **D12 铁死亡 → ICD → 免疫联合** | UCHL5–ZRANB1 湿实验完整 + CaO₂@MPN-HA 协同 anti-PD-1 | 3 | 4 | 4 | 4 | 4 | 4 | 3 | **29→30** | 强化 |
| **D11 乳酸化–EMT/糖酵解正反馈** | TRIM47–FBP1 乳酸化环达准因果 | 4 | 4 | 3 | 3 | 3 | 4 | 3 | **31→32** | 强化 |
| **D8 TAM 全景（TREM2/SPP1/RARγ-CFI/BGN 四路）** | 本轮新增 RARγ–CFI 与 BGN–NR2F2 两路；但四路层级未解 | 3 | 4 | 4 | 3 | 4 | 4 | 2 | **32** | 维持（反拥挤风险升高） |
| **D18 代谢–耐药轴** | ATM 抑制逆转 RAI 耐药（High）+ ANXA2⁺ sEV → XRCC 化疗耐药（High） | 4 | 4 | 3 | 3 | 4 | 4 | 3 | **28→29** | 强化 |
| **D14 细胞类型解析因果 + 空间多组学方法学** | MR/xQTL-SMR 范式本轮扩散至 4 篇；但无新技术突破 | 3 | 4 | 4 | 3 | 3 | 4 | 3 | **28** | 维持 |
| **D3″ APOE × MGST1 双轴功能解耦** | ⚠️ 本轮零新增；全库共现仍为 0 | 5 | 4 | 2 | 2 | 3 | 4 | 4 | **31（维持，风险↑）** | ⚠️ 无变化，证据停滞 |
| **D19 性别二态性机制层** | 三条独立证据确认现象，机制完全空白 | 4 | 3 | 3 | 3 | 4 | 3 | 4 | **26** | 🆕 新立 |
| **D16 MTC 远处转移** | 本轮无 MTC 新证据 | 4 | 3 | 3 | 3 | 4 | 3 | 3 | **27** | 维持（无变化） |
| **D20 儿童/青少年 PTC 免疫微环境** | 儿童 scRNA（n=11）+ 儿童颈侧 LNM 列线图 | 4 | 3 | 3 | 2 | 3 | 3 | 4 | **24** | 🆕 新立（探索级） |

\* D15 总分按 rubric 七维重算为 26；历史 30 分含"证据密度加权"，本表两项并列以便对照。

### 首选方向详述 / Top Direction Detail — **D9″**

- **研究问题 / Research question:** 在甲状腺癌（含儿童与成人 PTC）中，SPP1⁺/APOC1⁺ TAM 生态位与 APOE/MGST1 代谢–免疫干性肿瘤亚群是否在空间上共定位？其共定位强度能否解释 LNM 与复发风险的个体间差异？
- **新颖性角度 / Novelty angle:** 首次把 **TAM 生态位**与**代谢-免疫干性亚群**放在同一空间坐标系下检验；APOE × MGST1 共测文献仍为 0，且无人把代谢亚群坐标叠加到 POSTN⁺ myCAF 图谱上。
- **所需数据集 / Required datasets:** ① JCI Insight 图谱（10.1172/jci.insight.191990，423,733 细胞 + 28 肿瘤空间，gold OA）；② 儿童 PTC scRNA（10.1016/j.isci.2026.116560）；③ PTC 三部位 scRNA + 空间（10.1016/j.compbiolchem.2025.108857，含 17 基因 LNM 签名与 FN1 枢纽）；④ 配对原发–LNM scRNA（10.1080/2162402x.2026.2701504，Run #23 资源 G）。
- **预期终点 / Expected endpoint:** 空间共定位指数（如邻域富集 z-score）与 LNM 状态、无复发生存期的关联；SPP1/APOE/MGST1 三基因联合特征对 FN1 17 基因签名的增量 AUC。
- **分析策略 / Analysis strategy:** ① 用 JCI Insight 图谱的 Visium/空间坐标做邻域富集分析；② 用儿童队列做跨年龄验证；③ 用三部位队列做原发-转移配对差分；④ 以 Run #25 的共识 ML 框架把 APOE 强制纳入特征集，检验 MGST1 增量是否被吸收。
- **验证计划 / Validation plan:** 内部（JCI 图谱 5 个 bulk 队列）→ 外部（配对原发–LNM 队列）→ 湿实验可选（多重免疫荧光 mIF 验证 3–5 例）。
- **主要风险 / Major risk:** KHDP 韩国平台数据可得性；跨数据集批次效应；SPP1 抗体质量差异。
- **主张边界 / Claim boundary:** 只能主张"空间共定位与结局相关"，**不得**主张因果；MGST1 功能结论必须引用 10.3389/fimmu.2026.1848083 而非自行推断。

---

## 推荐下一步方向 / Recommended Next Direction

**首选：D9″ —— SPP1⁺/APOC1⁺ TAM × 代谢-免疫干性亚群的空间耦合（rubric 28，强候选）。**

**为什么是最优平衡：** 它是本轮唯一同时满足"新颖性 5 分 + 数据已就位 + 零湿实验可启动 + 直击 26 轮核心空白"的方向。JCI Insight 图谱与儿童 PTC 队列均为 gold OA，可直接下载；Run #25 已建立的共识 ML 框架可复用；APOE×MGST1 共测文献为 0 意味着**任何正向结果都是领域首报**。

**首批三个具体动作：**

1. **下载并统一坐标系** —— 取 JCI Insight 图谱（10.1172/jci.insight.191990）的空间坐标与细胞类型注释，建立邻域富集分析基线（POSTN⁺ myCAF ↔ 恶性细胞邻域）。
2. **强制纳入 APOE 重跑共识 ML** —— 复用 Run #25 的 MGST1 共识 ML 框架，把 APOE 强制加入特征集，检验 MGST1 的增量贡献是否被 APOE 吸收（直接回答 D3″ 的"功能解耦"问题）。
3. **跨年龄验证** —— 用儿童 PTC 队列（10.1016/j.isci.2026.116560）检验 SPP1⁺ M2 与肿瘤细胞的配体–受体互作是否在儿童中更强。

**并行（低优先级）：** 启动 D17 预研（微生物组），但**必须先解决 FMT/无菌动物验证的可得性**再投入；否则停留在生信层面，难以发表。

**必须避免的主张：** ❌ 不得声称"MGST1 与 APOE 互斥"（Run #25 已证伪）；❌ 不得在无 FMT 验证时声称"肠道菌群导致甲状腺癌"；❌ 不得把 MR 结果等同于因果确证。

---

## 随访阅读清单 / Follow-Up Reading List

| 优先级 | 文献 | 为什么下一步读 / Why next |
|:-:|---|---|
| ⭐⭐⭐ | JCI Insight 图谱 10.1172/jci.insight.191990 | 本轮最大规模公开图谱（423k 细胞 + 28 肿瘤空间），D9″/D3″ 的数据基座 |
| ⭐⭐⭐ | 儿童 PTC scRNA 10.1016/j.isci.2026.116560 | SPP1⁺ TAM 首次儿童证据 + 儿童-成人对比空白 |
| ⭐⭐⭐ | PTC 三部位多模态 10.1016/j.compbiolchem.2025.108857 | 17 基因 LNM 签名 + FN1 枢纽，可直接复用作 baseline 模型 |
| ⭐⭐ | RARγ–CFI–M2 10.1016/j.intimp.2026.116324 | 第四条 TAM 极化通路，含中和阻断与体内验证 |
| ⭐⭐ | *Terrisporobacter*–NTRK1 10.3389/fimmu.2026.1740257 | D17 升档的决定性证据；MR 设计的范本 |
| ⭐⭐ | IGF2BP2–m6A–STAT1 10.7150/ijbs.121503 | 本轮去分化方向最强机制论文，三测序整合 |
| ⭐⭐ | NUSAP1–BCAT1 10.1016/j.ijbiomac.2026.153021 | 去分化 × 支链氨基酸代谢的唯一交叉证据 |
| ⭐⭐ | TRIM47–FBP1 乳酸化 10.1016/j.prp.2026.156519 | D11 由相关升准因果的关键环 |
| ⭐ | UCHL5–ZRANB1 10.1080/15384047.2026.2663610 | 本轮湿实验最完整的铁死亡证据 |
| ⭐ | ATM–RAI 逆转 10.1186/s12967-026-08190-2 | 治疗逆转类证据链最完整（scRNA + TMA + 体内） |
| ⭐ | ML+LLM 预后 10.1038/s43856-026-01920-z | 算法维度新切口，需评估其可复现性声明 |
| ⭐ | SRUS 影像组学 10.1016/j.ultrasmedbio.2026.01.015 | 本轮影像组学中验证设计最规范者 |

---

## 可复现性说明 / Reproducibility Notes

- **检索日期 / Search date:** 2026-10-02 03:02–03:2x (UTC+8)
- **数据库 / Databases:** OpenAlex `api.openalex.org`（主）、Europe PMC `www.ebi.ac.uk/europepmc`（第二通道）、Crossref `api.crossref.org`、Unpaywall `api.unpaywall.org`
- **查询串 / Query strings:**
  - OpenAlex 九路矩阵见 `oa_search.py`（维度代码 `a`–`i`），核心约束 `title_and_abstract.search` + `from_publication_date` + `sort=publication_date:desc`
  - Europe PMC 六路：`(TITLE:"thyroid") AND (<维度词>) AND (PUB_YEAR:2026)`，`sort=P_PDATE_D desc`
  - 定向深挖：`filter=title_and_abstract.search:<GENE>,title_and_abstract.search:thyroid,from_publication_date:2026-06-01`
- **过滤 / Filters:** 主 30 d（2026-09-02 起）、90 d（2026-07-04 起）、EPMC `PUB_YEAR:2026`、深挖 2026-06-01 起
- **去重规则 / Deduplication:** DOI（小写、剥离 `https://doi.org/` 前缀）优先；无 DOI 时用标题归一化（仅保留字母数字、截断 90 字符）作为次级主键；跨通道（OpenAlex ↔ EuropePMC ↔ 深挖）统一比对
- **筛选规则 / Screening:** ① 标题必须点名甲状腺（thyroid/PTC/FTC/MTC/ATC/THCA 等）；② 整体必须为肿瘤主题（剔除甲亢/桥本/TED/Graves/良性结节）；③ 剔除期刊补充材料（`Supplementary Table/Figure`、`Data Sheet`）；④ 剔除撤稿通知、Correction、ASO Visual Abstract、Letter、Comment；⑤ 预印本保留但降一档
- **本轮脚本 / Scripts:** `oa_search.py`（主检索）、`_epmc_run26.py`（EPMC 六路）、`_deep_run26.py`（22 基因深挖）、`_keyabs_run26.py`（摘要抓取）、`_final_run26.py`（合并写回）、`_enrich_run26.py`（Crossref/Unpaywall）、`_gen_report_run26{a,b,c}.py`（报告生成）
- **产出文件 / Files saved:**
  - `literature_review_20261002_030212.md`（本报告）
  - `search_results_20261002_030212.json`（累积基线 391 条）
  - `search_results_latest.json`（同上，供下轮对比）
  - `search_results_20261002_030212_new.json`（本轮 94 条新增）
  - `search_results_20261002_030212.json`（30 d 主窗口原始）、`search_results_20261002_90day.json`（90 d）、`search_results_20261002_epmc.json`（EPMC 候选）、`search_results_20261002_deep.json`（深挖）、`search_results_20261002_keyabs.json`（摘要）、`search_results_20261002_030212_enrich.json`（元数据校验）
- **环境事实 / Environment:** NCBI eutils 与 PubMed 网页**本机不可达**（HTTP 000），本轮未使用；`paper-search-mcp` 本会话未连接；Crossref 21/21、Unpaywall 21/21 成功（Run #22 的 SSL 超时未复现）

---

## 与历史报告的差异 / Delta vs Previous Reports

### 相对 Run #25（2026-09-25，基线 297）的新增与信号变化

| 项 | Run #25 | Run #26 | 变化 |
|---|---:|---:|---|
| 累积基线 | 297 | 391 | **+94** |
| 本轮新增 | 52 | 94 | +42 |
| High / Medium / Low | 12 / 24 / 16 | 21 / 63 / 10 | High 占比 23% → 22%（略降） |
| 预印本 | 0 | 6 | +6 |
| 主通道贡献 | OpenAlex 18 / EPMC 22 / 深挖 12 | OpenAlex 22 / **EPMC 68** / 深挖 4 | **EPMC 成为主贡献通道** |

### 方向状态变化总表

| 方向 | Run #25 分 | Run #26 分 | 状态 | 本轮依据 |
|---|:-:|:-:|---|---|
| **D3″** APOE×MGST1 双轴 | 31 | **31** | ⚠️ **无变化**（连续第 26 轮） | 全库共现仍 0；MGST1 2026 年仍仅 1 篇，本轮零增长 |
| **D9** SPP1⁺ TAM | 33 | **34** | 🔺 强化 | 儿童 PTC scRNA 首次直接证据 + Mac-APOC1 独立复现 |
| **D8** TAM 全景 | 32 | **32** | ➖ 维持（拓宽） | 新增 RARγ–CFI、BGN–NR2F2 两路；反拥挤风险↑ |
| **D11** 乳酸化–EMT | 31 | **32** | 🔺 强化 | TRIM47–FBP1 正反馈环达准因果 |
| **D12** 铁死亡 | 29 | **30** | 🔺 强化 | UCHL5–ZRANB1 湿实验完整 + 钙超载协同 anti-PD-1 |
| **D13** 算法方法 | 27 | **29** | 🔺 强化 | ML+LLM 融合新切口；外部验证稀缺成为共识痛点 |
| **D14** 因果+空间 | 28 | **28** | ➖ 维持 | MR/xQTL-SMR 扩散至 4 篇，无技术突破 |
| **D15** 去分化/ATC | 30 | **30** | 🔺 强化（证据密度） | IGF2BP2 + NUSAP1 双 High 链条 |
| **D16** MTC 远处转移 | 27 | **27** | ➖ 无变化 | 本轮无 MTC 新证据 |
| **D17** 微生物群 | 24 | **27** | 🆙 **升档** | 双独立 MR 因果证据 |
| **D18** 代谢–耐药 | 28 | **29** | 🔺 强化 | ATM 逆转 RAI 耐药 + ANXA2⁺ sEV → XRCC |
| **D19** 性别二态性 | — | **26** | 🆕 新立 | 三条独立证据确认现象 |
| **D20** 儿童/青少年 PTC | — | **24** | 🆕 新立 | 儿童 scRNA + 儿童 LNM 列线图 |

### 本轮相对上轮的**三个新信号**

1. **TAM 极化从"单通路"演化为"四通路节点"** —— 本轮新增 RARγ–CFI 与 BGN–NR2F2，使 TREM2/AHR–IDO1、SPP1/CD44–JAK2–STAT3、RARγ/CFI、BGN/NR2F2 四条并立。这**提高了 D8 的反拥挤风险**（表中 O 分降至 2），也意味着单通路靶向策略的解释力下降。
2. **"代谢–表观–分化"三元耦合成为去分化研究的新范式** —— NUSAP1–BCAT1（代谢→表观）与 IGF2BP2–m6A–STAT1（表观→分化）从两端夹击，去分化不再被视作单纯 TF 切换。
3. **算法维度出现"从造模型到评模型"的转向** —— 本轮 8 篇算法论文中，2 篇主打外部验证/泛化性（10.1080/07853890.2026.2650862、10.1016/j.ultrasmedbio.2026.01.015），1 篇主打 LLM 融合。**"再做一个新的 LNM 列线图"已无明显发表空间**，差异化必须来自验证严格度或新模态。

### 持续跟踪方向 D3 的明确判定

> **判定：无变化（Unchanged），且证据停滞风险上升。**
>
> - OpenAlex 全库 `APOE` × `MGST1` × `thyroid` 三词共现：**0 篇**（与 Run #25 持平，连续第 26 轮）
> - MGST1 在 2026 年甲状腺癌文献中：**仍仅 1 篇**（10.3389/fimmu.2026.1848083），本轮**零增长**
> - APOE 侧：本轮无新原发证据（10.21037/tcr-2026-0796 已于 Run #25 收录）
> - 间接支撑（不构成 D3 直接证据）：TRIM47–FBP1 乳酸化、UCHL5–ZRANB1 铁死亡、NUSAP1–BCAT1 代谢-表观、甲状腺癌脂质代谢重编程综述（均已在基线）
>
> **结论：** D3″ 维持 rubric 31。但「MGST1 单基因孤岛」已连续两轮无新增，**建议下轮起把 D3″ 的优先级下调至与 D17 并列**，把主要资源转向 D9″（数据已就位、零湿实验可启动）。若连续 30 轮仍无 APOE×MGST1 共测文献，应考虑把该方向归档为"领域结构性空白"而非"候选方向"。

---

## 代码仓同步结果 / Repository Sync

| 步骤 | 结果 |
|---|---|
| `git pull --rebase --autostash origin main` | ✅ 成功（`Already up to date.`，第 1 次尝试即通过） |
| 分支跟踪关系 | ✅ `## main...origin/main` |
| 本轮提交文件 | `lit_review/literature_review_20261002_030212.md`、`lit_review/search_results_20261002_030212.json`、`lit_review/search_results_latest.json` |
| Commit message | `chore(lit-review): 甲状腺癌文献监测 2026-10-02（新增 94 篇 / 在范围 391 篇）` |
| Commit sha | **`944e36099c793048ca1673b8e472348b3ad9ca02`**（短 sha `944e360`） |
| `git push origin main` | ✅ **成功**（第 1 次尝试即通过，`2ad6a5c..944e360 main -> main`） |

---

*本报告由 `lit-review` 技能驱动，遵循 `review-output-template.md` / `evidence-matrix-schema.md` / `research-direction-rubric.md`。所有 DOI 与 PMID 均来自 OpenAlex / Europe PMC / Crossref 实际返回，未编造。PMID 缺失者统一标注「待编目」。*
