# Literature Review: 甲状腺癌侵袭·转移·复发·预后 — 分子机制 / 免疫微环境 / 单细胞与空间组学 / 算法方法
# Thyroid Cancer Invasion, Metastasis, Recurrence & Prognosis — Molecular Mechanisms, TME, Single-Cell & Spatial Omics, ML/DL Methods

**Run #24**
Date / 检索日期: 2026-09-18
Search window / 检索窗口: OpenAlex 30 d (2026-08-19→2026-09-18) + OpenAlex 90 d (2026-06-20→2026-09-18) + Europe PMC 跨源补检 (2025-06→2026-09)
Sources / 数据源: OpenAlex（主源）, Europe PMC（补检与元数据核验）, Crossref, Unpaywall
Baseline / 基线: `search_results_latest.json` 171 条 → **245 条**

---

## 中文摘要 (Chinese Abstract)

本轮为第 24 次监测，距上一轮（Run #23，2026-09-17）仅 1 天。**主窗口 30 天仅得 7 条真新增**——这符合 1 天间隔的预期，**不是领域平台期**；本轮 74 条新增中的 67 条来自两处方法学回补：① 对 30 天窗口增量为 0 的免疫微环境 / 单细胞 / 空间组学 / 转移干性四个维度按协议放宽到 90 天（回补 44 条）；② **本轮新增启用了 Europe PMC 作为跨源交叉补检通道**，一次性暴露出 OpenAlex 查询矩阵的系统性盲区，补回 23 条高价值文献。

本轮最重要的发现是**持续跟踪 23 轮「无变化」的 D3 方向（APOE−/MGST1+ 代谢–免疫干性亚群）首次获得直接锚定证据，但证据方向与原始假设相反**：*Discover Oncology*（PMID 42217128）通过 scRNA-seq + 空间转录组识别出 **APOE 高表达的肿瘤细胞亚群（Trem/T01）**，其通过 **APOE（肿瘤细胞）–NCF1（CD8⁺ Tex 耗竭 T 细胞）** 轴形成空间共定位的免疫抑制生态位，并衍生出跨队列验证的预后签名。即：**APOE 在甲状腺癌中是"高表达促免疫逃逸"的肿瘤细胞标志，而非原假设中"APOE 阴性"的干性亚群**。D3 状态由「无变化」改为 **「重构（Reframed）」**。

第二强信号是 **SPP1⁺ TAM 轴获得直接机制证据**：*Organogenesis*（PMID 42153613）证明甲状腺癌来源外泌体 SPP1 经 **CD44/JAK2/STAT3** 驱动巨噬细胞 M2 极化并促转移（体外 + 异种移植），把 Run #22 以来的 SPP1⁺ 相关性证据升级为因果链，D9 由 31 → **32**。

第三是**去分化/ATC 转化轨迹成为本轮最密集的新证据簇**：复发 FTC 中的 **UBE2C⁺ ATC-like 细胞**（*Endocrinology*）、**ZFP57–PKM2–乳酸**轴驱动的 CAF 介导去分化与碘难治（*J Exp Clin Cancer Res*，10× Visium 空间验证 + 白藜芦醇逆转）、**C/EBPβ** 经 IL-6/JAK/STAT 驱动 ATC 去分化（预印本）、CD109 空间免疫荧光描绘 PTC→ATC 转化边界（*Sci Rep*）、ATC 单细胞图谱（p53 抑制 / E2F 激活 / CD8 耗竭 + Treg 双层抑制，*Cancer Medicine*）。据此提出新方向 **D15（rubric 30）**。

此外：*Cell Reports Medicine* 揭示 **RET→OPG（osteoprotegerin）** 驱动 MTC 成骨性骨转移的器官特异性机制（远处转移维度的本轮最高质量原发证据）；*Science Advances* 提供配对原发灶–淋巴结转移灶 scRNA + 多重 IHC 的高质量免疫决定因子图谱（IL7R 为保护性生物标志）；*Cell Reports Medicine* 另有晚期 DTC 蛋白基因组三分类（canonical/stromal/immunogenic）+ 机器学习分类器 + 单细胞/空间独立验证，是算法方法维度的**方法学范式级**工作。

算法方法维度本轮增量最大（25 条），但**绝大部分为单中心、仅内部验证的列线图/影像组学**，外部验证与前瞻性设计稀缺，方法学同质化严重。

---

## English Abstract

This is Run #24, executed only one day after Run #23 (2026-09-17). **The strict 30-day main window yielded only 7 genuinely new records** — consistent with a one-day interval and **not indicative of a field plateau**. Of the 74 new records, 67 came from two methodological backfills: (i) per protocol, the four dimensions with zero increment in the 30-day window (immune microenvironment, single-cell, spatial omics, stemness/dedifferentiation) were re-run at 90 days (+44); (ii) **Europe PMC was newly introduced as a cross-source verification channel** and immediately exposed systematic blind spots in the OpenAlex query matrix, recovering 23 high-value papers.

The most consequential finding: **D3 (the APOE−/MGST1+ metabolic–immune stemness subpopulation), tracked as "no change" for 23 consecutive runs, finally received direct anchoring evidence — but the evidence runs opposite to the original hypothesis.** *Discover Oncology* (PMID 42217128) combined scRNA-seq with spatial transcriptomics to identify an **APOE-high malignant thyrocyte subcluster (Trem/T01)** that forms a spatially co-localized immunosuppressive niche with CD8⁺ exhausted T cells via an **APOE (tumour) – NCF1 (CD8⁺ Tex)** axis, yielding a cross-cohort-validated prognostic signature. APOE therefore marks a **tumour-cell immune-evasion programme in thyroid cancer**, not the APOE-negative stemness state originally posited. D3 status changes from "unchanged" to **"Reframed"**.

Second, the **SPP1⁺ TAM axis gained direct mechanistic evidence**: *Organogenesis* (PMID 42153613) showed that thyroid-cancer-derived exosomal SPP1 drives macrophage M2 polarization via **CD44/JAK2/STAT3**, promoting proliferation/migration/invasion in vitro and in xenografts — upgrading SPP1⁺ from correlative to causal and raising D9 from 31 to **32**.

Third, **dedifferentiation / ATC transformation trajectories formed the densest new evidence cluster**: **UBE2C⁺ ATC-like cells** in relapsed FTC (*Endocrinology*); CAF-driven dedifferentiation and radioiodine refractoriness via the **ZFP57–PKM2–lactate** axis, spatially validated with 10× Visium and reversed by resveratrol (*J Exp Clin Cancer Res*); **C/EBPβ** driving ATC dedifferentiation through IL-6/JAK/STAT (preprint); a CD109-based spatial immunofluorescence assay delineating the PTC→ATC boundary (*Sci Rep*); and an ATC single-cell atlas showing p53 suppression, E2F activation, and dual-layered CD8 exhaustion plus Treg-mediated suppression (*Cancer Medicine*). New direction **D15 (rubric 30)** is proposed.

Also notable: *Cell Reports Medicine* uncovered a **RET→osteoprotegerin (OPG)** mechanism driving osteoblastic bone metastasis in MTC — the highest-quality primary evidence this run for the distant-metastasis dimension; *Science Advances* delivered a paired primary-tumour/metastatic-LN scRNA + multiplex-IHC atlas identifying IL7R as a favourable biomarker; and another *Cell Reports Medicine* study established a proteogenomic three-subtype classification of advanced DTC (canonical/stromal/immunogenic) with an ML classifier independently validated by single-cell and spatial transcriptomics — a methodological exemplar for the algorithms dimension.

The algorithms dimension contributed the largest increment (25 records) but is dominated by single-centre nomograms and radiomics models with internal validation only; external and prospective validation remain scarce and methodological homogenization is severe.

---

## 1. 检索策略 / Search Strategy

| Source / 数据源 | Query / 查询 | Filters / 过滤 | Results / 命中 | Notes / 说明 |
|---|---|---|---:|---|
| **OpenAlex** `a` 分子机制+预后转移 | `THYROID AND (metastasis OR metastatic OR "lymph node") AND (biomarker OR "gene signature" OR signature)` | ≥2026-08-19, sort=publication_date:desc, per-page 25 | 21 | 新条目 21 |
| **OpenAlex** `b` 分子机制 | `...AND (invasion OR metastasis) AND (mechanism OR pathway OR EMT OR "epithelial-mesenchymal")` | 同上 | 53（取 25） | 新条目 19 |
| **OpenAlex** `c` 算法方法+预后 | `...AND ("machine learning" OR "deep learning" OR radiomics OR nomogram OR "prediction model")` | 同上 | 19 | 新条目 13 |
| **OpenAlex** `d` 免疫微环境 | `...AND ("immune microenvironment" OR "tumor microenvironment" OR immune OR macrophage OR "T cell")` | 同上 | 27（取 25） | 新条目 11 |
| **OpenAlex** `e` 单细胞 | `...AND ("single-cell" OR scRNA-seq OR "single cell RNA")` | 同上 | 13 | 新条目 8 |
| **OpenAlex** `f` 空间组学 | `...AND ("spatial transcriptomic(s)" OR "spatial multi-omics" OR "spatial omics" OR Visium)` | 同上 | 10 | 新条目 2 |
| **OpenAlex** `g` 预后转移 | `...AND (prognosis OR recurrence OR "distant metastasis") AND ("risk model" OR "risk stratification" OR survival OR nomogram)` | 同上 | 53（取 25） | 新条目 15 |
| **OpenAlex** `h` 转移干性 | `...AND ("cancer stem cell" OR stemness OR dedifferentiation OR "tumor-initiating")` | 同上 | 9 | 新条目 3 |
| **OpenAlex** `i` 代谢重编程 | `...AND ("metabolic reprogramming" OR glycolysis OR "lipid metabolism" OR ferroptosis OR OXPHOS)` | 同上 | 6 | 新条目 4 |
| **OpenAlex 90 d 补跑** | 全部九路 | ≥2026-06-20, per-page 50 | 244 唯一 / 176 在范围 | 新条目 52 |
| **Europe PMC（本轮新增通道）** | `SC`: `TITLE:"thyroid" AND (TITLE:"single-cell" OR TITLE:"single cell" OR ABSTRACT:"scRNA-seq") AND PUB_YEAR:2026` | sort=P_PDATE_D desc, pageSize 50 | 50 | 39 条基线未收录，取 12 |
| **Europe PMC** | `SP`: `TITLE:"thyroid" AND (TITLE:"spatial" OR ABSTRACT:"spatial transcriptomics")` | 同上 | 33 | 21 条未收录，取 5 |
| **Europe PMC** | `IM`: `TITLE:"thyroid" AND (TITLE:"tumor microenvironment" OR TITLE:"macrophage")` | 同上 | 24 | 21 条未收录，取 6 |
| **Crossref** | DOI 元数据校验（10 条 High/重点） | — | 10/10 OK | 无失败 |
| **Unpaywall** | OA 状态与全文链接（同 10 条） | email=lit-review@local | 10/10 OK | 本轮 SSL 问题消失 |
| **NCBI eutils / PubMed** | — | — | **未调用** | 本机 HTTP 000 不可达，按环境事实禁止直连 |
| **paper-search-mcp** | — | — | **未调用** | 本会话该 MCP 未连接（仅 agent-mail 可用） |

### 去重与筛选规则 / Deduplication & Screening
- **主键**：DOI 小写优先；无 DOI 时用标题归一化（去标点、小写、截断 70 字符）。
- **多版本合并**：OpenAlex 的仓储副本/出版版本合并入主记录（本轮合并 29 组 30 d、68 组 90 d；PRECISE 数据存档 `10.1158/1078-0432.c.8568781` 并入正文 `10.1158/1078-0432.ccr-25-4488`）。
- **剔除**：`SUPPLEMENT` 正则丢弃期刊补充材料（`Table 1_...` 等）；标题未点名甲状腺（30 d 29 条 / 90 d 57 条）；非肿瘤主题（30 d 4 条 / 90 d 11 条）。
- **边界标注**：ICI 相关甲状腺 irAE（3 条 ECE 摘要）因 "Hypothyroidism/Thyroid dysfunction" 误匹配被纳入，标记为 **off-topic 边界**，不计入甲状腺癌机制证据。

### 本轮新增构成（重要，避免趋势误读）/ Composition of This Run's Increment
| 来源 | 条数 | 说明 |
|---|---:|---|
| 30 天主窗口真增量 | **7** | 距 Run #23 仅 1 天，7 条属正常日更量级 |
| 90 天补跑净增量 | **44** | IM/SC/SP/ST 四维度 30 d 为 0 → 协议要求放宽 |
| Europe PMC 跨源补检 | **23** | OpenAlex 查询矩阵系统性漏检 |
| **合计（去重后）** | **74** | 累积基线 171 → **245** |

> ⚠️ 方法学警示：**74 条不等于"近 30 天领域产出 74 篇"**。其中 67 条是历史窗口回补与跨源补检，反映的是**此前 23 轮的检索欠采样**，而非本轮窗口内的真实产出速率。趋势判断必须以 7 条为准。

---

## 2. 纳入论文 / Included Papers

> 完整 74 条见 `search_results_20260918_232000.json` 的 `new_records`。以下列出 18 条 **High** 相关性条目（OpenAlex 8 + Europe PMC 10），其余在证据矩阵 B 中压缩呈现。

### 2.1 High 相关性 — OpenAlex 主源 (8)

1. **Single-cell transcriptomic analysis reveals tumor-immune determinants of lymph node colonization and progression in thyroid cancer.** *Science Advances*. 2026-07-03. PMID: 42397917. DOI: 10.1126/sciadv.aea4727. OA: gold.
   - Author claim: 配对原发灶与转移淋巴结的 scRNA-seq + 多重 IHC 显示，定植淋巴结后甲状腺细胞与 TAM 下调 TNFRSF12A、CX3CR1 等炎症因子受体，并诱导 Treg 抑制 CTL；淋巴结内 **IL7R** 高表达与较好预后相关。
   - Agent note: 本轮**配对原发–LNM 设计质量最高**的原发证据，直接可用于 D8/D9 的空间与亚群验证。

2. **Spatially resolved immune niches in thyroid cancer: from hot–cold–excluded ecosystems to precision immunotherapy.** *Frontiers in Immunology*. 2026-07-01. PMID: 42459642. DOI: 10.3389/fimmu.2026.1863184. OA: gold.
   - Author claim: 综述指出甲状腺癌免疫微环境由 hot/cold/excluded 等空间生态位构成，PD-L1/TMB/常规转录组框架不足以解释免疫反应异质性；B 细胞与三级淋巴结构富集区常对应惰性行为。
   - Agent note: 综述级证据，仅作共识背景；**不构成 D3/D9 的原发支持**。

3. **RET-driven osteoprotegerin expression links medullary thyroid cancer to osteoblastic bone metastases.** *Cell Reports Medicine*. 2026-08-27. PMID: 42660113. DOI: 10.1016/j.xcrm.2026.103010. OA: gold.
   - Author claim: 患者来源 MTC 细胞（RET C634W / M918T）通过激活 RET 上调 **OPG**，抑制破骨分化，形成成骨性骨转移；RET 敲低或药物抑制可减轻骨病灶负荷，循环 OPG 具生物标志潜力。
   - Agent note: 本轮**远处转移维度最高质量原发证据**，是 MTC 器官特异性转移机制的重要补白。

4. **Integrated Bioinformatics and Experimental Validation Reveal the Diagnostic and Prognostic Value of SMDT1 in Thyroid Carcinoma.** *Diagnostics*. 2026-07-18. PMID: 42510113. DOI: 10.3390/diagnostics16142250. OA: gold.
   - Author claim: SMDT1（线粒体钙单向转运体调控因子）在甲状腺癌中显著下调，低表达与不良病理特征相关；50 对配对组织 + 体外过表达功能实验验证。
   - Agent note: **Run #22 已报道 SMDT1 的抑制性数据点，本轮为独立重复**；提示代谢–免疫基因方向呈肿瘤抑制性，D3 需调和。

5. **Developing an epithelial signature for prognosis of papillary thyroid carcinoma.** *Endocrine-Related Cancer*. 2026-07-01. PMID: 42447050. DOI: 10.1530/erc-25-0515. OA: closed.
   - Author claim: 整合正常甲状腺/原发 PTC/淋巴结转移 scRNA-seq 构建跨阶段细胞图谱，基于恶性上皮程序在 TCGA-THCA 建立 4 基因 Cox+LASSO 风险签名，并对 TMEM45A、STC1 做 siRNA 验证。
   - Agent note: 与 PRECISE（下述）高度同构，**互为独立重复**；非 OA。

6. **Integrated bulk and single-cell RNA sequencing reveals a prognostic neuro-mimicry signature in papillary thyroid carcinoma.** *Discover Oncology*. 2026-06-22. PMID: 42329337. DOI: 10.1007/s12672-026-05278-5. OA: gold.
   - Author claim: TCGA 521 例 PTC 构建 8 基因"神经模拟"签名（KCNN4/KCNN1/KCNT2/SNAP25/KCNK16/GABRG1/GABRG2/GABRB2），预测 LNM AUC 0.721；GSE184362（65,744 细胞）验证 **GABRB2** 特异富集于恶性甲状腺细胞（20.0% vs 免疫细胞 0.1%）。
   - Agent note: 离子通道/神经模拟是**较新颖的侵袭角度**，但 AUC 0.721 属中等，临床效用有限。

7. **Clinical significance of coexisting Hashimoto's thyroiditis in differentiated thyroid cancer: a retrospective cohort study.** *BMC Endocrine Disorders*. 2026-07-08. PMID: 42420994. DOI: 10.1186/s12902-026-02404-w. OA: gold.
   - Author claim: 198 例 DTC 队列中，合并桥本甲状腺炎与被膜侵犯/腺外侵犯等侵袭特征的相关性在多因素校正后仍需谨慎解读。
   - Agent note: 单中心小样本，与下述 myeloid landscape 构成**炎症背景影响 TME**的交叉议题。

8. **99mTc-FAPI-YQ3 SPECT/CT for characterizing FAPI uptake phenotypes and metabolic-stromal heterogeneity in advanced DTC.** *Frontiers in Immunology*. 2026-07-16. PMID: 42534915. DOI: 10.3389/fimmu.2026.1888899. OA: gold.
   - Author claim: 前瞻性单中心影像–影像组学研究，用新型 FAPI 示踪剂刻画晚期/RAIR-DTC 的基质–代谢异质性。
   - Agent note: 作者**明确声明**示踪剂摄取不能作为 FAP 表达的直接组织学证据，需 IHC/多组学验证；无正式样本量计算。属探索性。

### 2.2 High 相关性 — Europe PMC 跨源补检 (10)

9. **Spatially resolved single cell analysis suggests an APOE NCF1 associated immunosuppressive niche and its prognostic signature in thyroid cancer.** *Discover Oncology*. 2026-05-30. PMID: 42217128. DOI: 10.1007/s12672-026-05061-6. OA: gold.
   - Author claim: 整合 scRNA-seq + 空间转录组，识别出 **APOE 高表达的肿瘤细胞亚群 Trem/T01** 与 CD8⁺ 耗竭 T 细胞（Tex）亚群；计算与空间分析揭示 **APOE（Trem）–NCF1（CD8⁺ Tex）** 互作轴且两者在空间上显著邻近；由此衍生的预后基因签名在独立队列验证。
   - Agent note: ⭐ **本轮最重要发现**。24 轮以来**首个直接锚定 APOE 的甲状腺癌原发证据**，且带空间共定位 + 跨队列验证。但方向与原假设相反（APOE **高**表达的肿瘤细胞驱动免疫逃逸），D3 需重构。

10. **Thyroid cancer-derived exosomal SPP1 promotes tumor progression by driving macrophage M2 polarization through the CD44/JAK2/STAT3 signaling pathway.** *Organogenesis*. 2026-05-19. PMID: 42153613. DOI: 10.1080/15476278.2026.2670152. OA: gold.
    - Author claim: SPP1 在甲状腺癌组织与 TPC1 外泌体中富集；外泌体 SPP1 诱导 THP-1 来源 M0 巨噬细胞 M2 极化并促癌；SPP1 敲除消除该效应；机制上直接结合 **CD44** 并激活 **JAK2/STAT3**；异种移植验证。
    - Agent note: ⭐ 把 SPP1⁺ TAM 从相关性升级为**因果链**，直接强化 D9。

11. **Myeloid landscape of BRAF-mutant papillary thyroid cancer and thyroiditis.** *Endocrine-Related Cancer*. 2026-08-01. PMID: 42583701. DOI: 10.1530/erc-26-0088. OA: gold.
    - Author claim: 11 例 PTC-BRAF（4 例伴淋巴细胞性甲状腺炎 LT）scRNA-seq；无 LT 者**中性粒细胞为优势髓系群**，甲状腺细胞高表达中性粒细胞趋化因子 **ECRG4**，且中性粒细胞表达致癌基因、预后差；伴 LT 者甲状腺细胞 MHC-II 抗原提呈上调、甲状腺细胞与巨噬细胞富集 IFN-γ 应答。
    - Agent note: 首次把**中性粒细胞（非仅 TAM）**置于 BRAF-PTC 髓系全景中心；n=11 属小样本。

12. **TIM3 as a therapeutic target in anaplastic thyroid cancer: upregulation in M2-like macrophages induced by TME-derived TGFβ1.** *The Journal of Pathology*. 2026-08-05. PMID: 42557785. DOI: 10.1002/path.70104. OA: closed.
    - Author claim: ATC 细胞分泌 TGFβ1 上调单核细胞 **HAVCR2/TIM3**；PTC/ATC 组织 TIM3 高于腺瘤/正常；公共 scRNA-seq 显示 T 细胞 TIM3 升高；TIM3 上调定位于 M2-like 巨噬细胞并与 TGFB1/CD163 正相关，提示 **TGFβ–TIM3 轴**。
    - Agent note: 直接给出可成药检查点组合（TGFβ + TIM3），临床相关性高。

13. **Single-Cell Transcriptome of Anaplastic Thyroid Cancer Reveals Immunosuppressive Tumor Microenvironment Remodeling.** *Cancer Medicine*. 2026-09-01. PMID: 42702761. DOI: 10.1002/cam4.72261. OA: gold.
    - Author claim: 3 例 ATC + 3 例致死性 PTC scRNA-seq；ATC 肿瘤细胞炎症/免疫基因上调、MAPK 与 PI3K 共激活、**p53 通路受抑**、血管生成与免疫逃避程序激活；E2F1/7/8 激活（CDK-RB-E2F 轴失调）；CD8⁺ T 细胞耗竭 + Treg-CD8 互作增强（双层抑制）；另鉴定出抗原提呈型 CAF。
    - Agent note: n=3+3 极小样本，**结论为假设生成级**；但与 D15 轨迹方向高度契合。

14. **PRECISE: A Prognostic Thyrocyte-Derived Gene Signature for Papillary Thyroid Carcinoma.** *Clinical Cancer Research*. 2026-07-01. PMID: 42008746. DOI: 10.1158/1078-0432.ccr-25-4488（数据存档 10.1158/1078-0432.c.8568781）. OA: closed.
    - Author claim: 用 snRNA-seq（11 肿瘤 + 4 正常）整合既往 scRNA-seq 甲状腺细胞基因，构建 **41 个上皮基因**的 PRECISE 签名；发现队列 MDACC n=109（中位随访 14 年），验证于 VUMC n=65 与 TCGA n=370；高 PRECISE 与较短 PFS/DSS 相关。
    - Agent note: **细胞类型来源明确 + 三队列 + 14 年随访**，是本轮预后签名方法学质量标杆。

15. **Integrated multi-omics and single-cell analyses identify metabolic heterogeneity and therapeutic vulnerabilities in medullary thyroid cancer.** *British Journal of Cancer*. 2026-05-07. PMID: 42098434. DOI: 10.1038/s41416-026-03467-1. OA: closed.
    - Author claim: 101 例 MTC RNA-seq + 51 对配对非靶向代谢组；三代谢亚型，其中 **M3 型预后最差**，特征为糖胺聚糖（GAG）/硫酸软骨素合成上调与 **CHSY1** 高表达，伴 EMT 增强；多组学提示 CHSY1 经肌成纤维细胞互作促 EMT（IHC 47 例 + mIF 12 例 + scRNA 7 例验证）；8 代谢物 / 28 代谢基因分类器可分层复发风险。
    - Agent note: MTC 代谢异质性的**高质量多组学 + 多模态验证**；与本轮 RET–OPG 共同把 MTC 推为本轮活跃亚型。

16. **Mechanism of cancer-associated fibroblast-driven thyroid cancer dedifferentiation via the ZFP57-PKM2 axis-mediated lactate secretion and therapeutic intervention with resveratrol.** *Journal of Experimental & Clinical Cancer Research*. 2026-02-27. PMID: 41761234. DOI: 10.1186/s13046-026-03675-w. OA: gold.
    - Author claim: 3 例手术标本 10× Visium（14,191 spots，7 类细胞）；低分化区域 CAF 糖酵解增强，伴 ZFP57 上调与 PKM2 诱导；CAF 条件培养基促 PTC 增殖/侵袭/去分化并**降低摄碘**；ZFP57 过表达促生长并损害碘潴留，**白藜芦醇**抑制 ZFP57、恢复分化与碘亲和性；机制上 CAF 分泌乳酸激活 TGF-β 通路。
    - Agent note: ⭐ 空间组学 + 代谢 + 去分化 + 可干预（白藜芦醇）四维闭环，**直接强化 D11** 并衔接 D15。

17. **Proteogenomic characterization delineates clinically relevant subtypes of advanced differentiated thyroid cancer.** *Cell Reports Medicine*. 2026-03-06. PMID: 41794039. DOI: 10.1016/j.xcrm.2026.102661. OA: gold.
    - Author claim: 113 例晚期 DTC 蛋白基因组学 → **canonical / stromal / immunogenic** 三亚型，驱动突变、病理特征与结局各异；开发基于常规基因突变 + 数字病理的**机器学习分类器**；独立队列以 scRNA + 空间转录组验证；真实世界系统治疗队列提供初步临床证据。
    - Agent note: ⭐ 算法方法维度**方法学范式级**工作——ML 分类器的生物学有效性由单细胞/空间独立验证，是本轮同质化影像组学中的正面反例。

18. **Single-cell analysis identifies ATC-like cells driving progression in relapsed follicular thyroid carcinoma.** *Endocrinology*. 2026-02-01. PMID: 41631714. DOI: 10.1210/endocr/bqag012. OA: closed.
    - Author claim: 46,739 细胞（PTC / FVPTC / 复发 FTC / ATC）scRNA-seq 重建进展轨迹；PTC、FVPTC、FTC 去分化为 ATC 的路径不同但汇合，FVPTC 亦可进展为 FTC；复发 FTC 中存在具 ATC 分子特征的细胞群，主要经 **COL9A3–整合素 α1β1** 与内皮/成纤维细胞互作，具有高代谢与增殖潜能；**UBE2C** 为该群特异标志，体外体内验证。
    - Agent note: ⭐ 首次在复发 FTC 中定位"ATC-like"前体态并给出可操作标志 UBE2C，是 D15 的核心支点之一。

---

## 3. 证据矩阵 / Evidence Matrix

### 3.1 矩阵 A — High 相关性完整条目（18 行）/ Full Schema, High-Relevance Papers

| # | Paper | PMID/DOI | 维度 Dim | 预印本 Preprint | OA | Disease/Population | Data Source | Method | Endpoint | Main Finding | Validation | Limitations | Relevance | Gap Suggested | Future Direction |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| A1 | Sci Adv LN colonization | 42397917 / 10.1126/sciadv.aea4727 | SC/IM/PR | 否 | gold | 甲状腺癌配对原发–LNM | 原发灶+配对转移 LN 原代样本 | scRNA-seq + 多重 IHC | LNM 定植、预后 | 定植后甲状腺细胞/TAM 下调 TNFRSF12A、CX3CR1；LN 内诱导 Treg 抑制 CTL；IL7R 高表达预后较好 | 配对设计 + mIHC 正交 | 样本量未在大样本外部队列复现；IL7R 截断值未定 | High | IL7R 因果性未知；TAM 亚群身份未细分 | D8/D9：在配对原发–LNM 空间图谱中细分 TAM 并检验 IL7R 因果 |
| A2 | Front Immunol 空间免疫生态位综述 | 42459642 / 10.3389/fimmu.2026.1863184 | SC/SP/IM | 否 | gold | 甲状腺癌（PTC/ATC） | 文献综述 | 综述 | 免疫分型 | hot/cold/excluded 空间生态位框架；B 细胞/TLS 区常对应惰性 | 无（综述） | 非原发证据；框架尚未标准化 | High | 缺乏可操作的空间分型阈值 | D14：建立可复现的空间生态位量化流程 |
| A3 | Cell Rep Med RET–OPG 骨转移 | 42660113 / 10.1016/j.xcrm.2026.103010 | MO/PR | 否 | gold | MTC 骨转移 | 患者来源 TT/MZCRC1 细胞 + 小鼠股骨模型 + 人血清 | 体外成骨表型 + RET 敲低/抑制 + 循环 OPG | 远处（骨）转移机制 | RET 激活→OPG↑→抑制破骨分化→成骨性骨转移；RET 抑制减轻负荷 | 体内模型 + 临床样本 OPG | 骨转移模型为股骨内注射；OPG 前瞻性阈值未验证 | High | OPG 作为筛查标志的敏感/特异未知 | D16：MTC 器官特异性转移机制与 OPG 液体活检 |
| A4 | Diagnostics SMDT1 | 42510113 / 10.3390/diagnostics16142250 | IM/MO | 否 | gold | THCA/PTC | 公共数据库 + 50 对配对组织 + PTC 细胞系 | 生信 + qRT-PCR/WB/CCK-8/克隆/划痕/Transwell | 诊断、预后、免疫浸润 | SMDT1 显著下调，低表达与不良特征相关；过表达抑制恶性表型 | 50 对组织 + 体外功能 | 单中心组织；免疫浸润为生信推断 | High | SMDT1 与免疫细胞因果互作未证 | D3′：检验 SMDT1 与 APOE⁺ 生态位关系 |
| A5 | Endocr Relat Cancer 上皮签名 | 42447050 / 10.1530/erc-25-0515 | SC/PR | 否 | closed | PTC（正常/原发/LNM） | 多套 scRNA-seq + TCGA-THCA | 跨阶段图谱 + Cox/LASSO + siRNA | 预后 | 4 基因风险签名；TMEM45A、STC1 敲低验证 | TCGA 内部 + 体外 siRNA | 无外部独立临床队列；非 OA | High | 签名与 TME 空间关系未测 | D14：把上皮签名映射回空间生态位 |
| A6 | Discov Oncol 神经模拟签名 | 42329337 / 10.1007/s12672-026-05278-5 | SC/PR/AL | 否 | gold | PTC | TCGA 521 + GSE184362（65,744 cells） | LASSO + scRNA 细胞来源验证 | LNM 预测 | 8 基因签名 AUC 0.721；GABRB2 富集于恶性甲状腺细胞 | 单细胞正交 + TCGA | AUC 中等；无外部验证 | High | 离子通道功能机制未做湿实验 | 备选：GABRB2 电生理/药理干预 |
| A7 | BMC Endocr Disord 桥本合并 DTC | 42420994 / 10.1186/s12902-026-02404-w | AL/PR | 否 | gold | DTC ± HT | 198 例单中心手术队列 | 多因素 logistic | 侵袭特征（被膜/腺外侵犯、LNM） | HT 与侵袭特征的独立关联需谨慎解读 | 无外部验证 | 单中心、样本小、回顾性 | High | 缺乏免疫细胞层面的机制解释 | 与 #11 联动：炎症背景 × 髓系全景 |
| A8 | Front Immunol FAPI SPECT/CT | 42534915 / 10.3389/fimmu.2026.1888899 | AL/PR/SP | 否 | gold | 晚期/RAIR-DTC | 单中心前瞻影像队列 | 新型 FAPI 示踪剂 + 影像组学 | 基质–代谢异质性表型 | FAPI 摄取表型可刻画异质性 | 无（探索性） | 无样本量计算；作者自述摄取≠FAP 组织学证据 | High | 缺乏 IHC/多组学配对验证 | D13：影像–病理配对验证范式 |
| A9 | **Discov Oncol APOE–NCF1 生态位** | 42217128 / 10.1007/s12672-026-05061-6 | SC/SP/IM/AL/PR | 否 | gold | 甲状腺癌 | scRNA-seq + 空间转录组 | 细胞通讯推断 + 空间共定位 + ML 预后建模 | 免疫逃逸、预后 | **APOE⁺ 肿瘤细胞亚群 Trem/T01 与 CD8⁺ Tex 经 APOE–NCF1 轴空间共定位**；签名跨队列验证 | 空间共定位 + 独立队列 | 互作为计算推断，无功能阻断实验；期刊层级中等 | High | APOE–NCF1 因果性、MGST1 位置未明 | **D3′（首选）** |
| A10 | **Organogenesis 外泌体 SPP1** | 42153613 / 10.1080/15476278.2026.2670152 | IM/MO | 否 | gold | 甲状腺癌 | TPC1 外泌体 + THP-1 巨噬 + 异种移植 | 外泌体分离、M2 标志、CD44 阻断、WB | M2 极化、增殖/迁移/侵袭 | 外泌体 SPP1→CD44→JAK2/STAT3→M2 极化→促癌 | 体外 + 异种移植 + 挽救实验 | 单一细胞系；人体组织 M2 空间定位未做 | High | 人组织中 SPP1⁺/TREM2⁺ 空间关系未知 | **D9（强化）** |
| A11 | Endocr Relat Cancer 髓系全景 | 42583701 / 10.1530/erc-26-0088 | SC/IM | 否 | gold | PTC-BRAF ± 淋巴细胞性甲状腺炎 | 11 例 10x Chromium scRNA-seq | QC/批次校正/降维/DEG | 髓系组成、LNM、腺外侵犯 | 无 LT 者中性粒细胞占优且表达致癌基因；伴 LT 者 MHC-II 提呈与 IFN-γ 应答上调 | 1 例公共样本复用 | n=11 小样本；鲜样与固定样混合 | High | 中性粒细胞功能验证缺失 | D8：髓系全景拓展（中性粒细胞 × TAM） |
| A12 | J Pathol TIM3 ATC | 42557785 / 10.1002/path.70104 | IM | 否 | closed | ATC/PTC | 人单核细胞 + 患者组织 + 公共 scRNA-seq | qPCR、IHC、生信 | 检查点表达、巨噬极化 | TGFβ1→TIM3↑（M2-like 巨噬）；与 TGFB1/CD163 正相关 | 体外 + 组织 + 公共数据集 | 无体内药效验证；非 OA | High | TIM3 阻断在 ATC 的疗效未测 | D8：TGFβ + TIM3 联合检查点 |
| A13 | Cancer Med ATC 单细胞 | 42702761 / 10.1002/cam4.72261 | SC/IM/ST | 否 | gold | ATC vs 致死性 PTC | 3 ATC + 3 PTC scRNA-seq | 转录网络、免疫图谱、细胞互作 | 去分化、免疫逃避 | p53 受抑 + E2F1/7/8 激活；CD8 耗竭 + Treg 双层抑制；抗原提呈型 CAF | 无（小样本） | n=3+3，假设生成级 | High | 需扩大 ATC 队列与时间轨迹 | **D15** |
| A14 | Clin Cancer Res PRECISE | 42008746 / 10.1158/1078-0432.ccr-25-4488 | SC/PR/AL | 否 | closed | PTC | MDACC n=109（snRNA 11+4）、VUMC n=65、TCGA n=370 | snRNA/scRNA 整合 + 秩和打分 + Cox | PFS、DSS | 41 上皮基因签名；高 PRECISE 与较短 PFS/DSS 相关 | 三队列 + 14 年随访 | 非 OA；评分依赖平台 | High | 与空间生态位映射未做 | D14：签名空间化 |
| A15 | Br J Cancer MTC 代谢异质性 | 42098434 / 10.1038/s41416-026-03467-1 | ME/SC/ST | 否 | closed | MTC | PRJCA008783（101 例 RNA + 51 对代谢组）、PRJCA021386 | 聚类 + IHC 47 + mIF 12 + scRNA 7 + DL 预后模型 | 复发风险、代谢亚型 | 三代谢亚型；M3（GAGs/CHSY1↑、EMT↑）预后最差 | IHC/mIF/scRNA 三模态 + 独立数据集 | 非 OA；CHSY1 机制为相关性推断 | High | CHSY1 因果与治疗靶点未验证 | D11/ME：GAGs–EMT 轴 |
| A16 | J Exp Clin Cancer Res ZFP57–PKM2 | 41761234 / 10.1186/s13046-026-03675-w | SP/ME/ST/IM | 否 | gold | PTC→PDTC/ATC 去分化 | 3 例 10× Visium（14,191 spots）+ 细胞系 + 异种移植 | 空间转录组、Seahorse、报告基因、挽救实验 | 去分化、摄碘、糖酵解 | CAF 糖酵解↑→乳酸→TGF-β；ZFP57–PKM2 驱动去分化与碘难治；白藜芦醇逆转 | 空间 + 体外 + 体内 + 药物挽救 | n=3 空间样本；白藜芦醇浓度生理性存疑 | High | 人组织中 CAF–乳酸生态位空间范围未量化 | **D11 强化 / D15** |
| A17 | Cell Rep Med 蛋白基因组 DTC | 41794039 / 10.1016/j.xcrm.2026.102661 | MO/SP/AL/IM | 否 | gold | 晚期 DTC | 113 例蛋白基因组 + 独立 scRNA/空间队列 + 真实世界治疗队列 | 蛋白质组聚类 + ML 分类器（突变 + 数字病理） | 分子亚型、治疗决策 | canonical/stromal/immunogenic 三亚型；ML 分类器可用常规数据预测 | 独立单细胞/空间队列 + 真实世界队列 | 真实世界部分为非随机；亚型治疗证据为初步 | High | 前瞻性亚型指导治疗未验证 | **D14：ML 亚型的组学验证范式** |
| A18 | Endocrinology ATC-like FTC | 41631714 / 10.1210/endocr/bqag012 | SC/ST | 否 | closed | PTC/FVPTC/复发 FTC/ATC | 46,739 细胞 scRNA-seq | 轨迹重建、CellChat、标志物筛选、体内外验证 | 复发、去分化 | 复发 FTC 中 UBE2C⁺ ATC-like 细胞群，经 COL9A3–整合素 α1β1 互作 | 体外 + 体内功能验证 | 非 OA；跨数据集整合批次风险 | High | ATC-like 态在术前样本中可否检出 | **D15** |

### 3.2 矩阵 B — Medium / Low 相关性（56 条，压缩）/ Condensed, Medium & Low Relevance

> 列：# | 标题（截断）| DOI | 维度 | 相关性 | 预印本 | OA | 核心发现（一句话）

**免疫微环境 / 肿瘤免疫 (IM)**
| # | Title | DOI | Dim | Rel | Pre | OA | Key finding |
|---|---|---|---|---|---|---|---|
| B1 | HOXC10-mediated CCL2 transcriptional activation inducing M2 polarization in TAMs and promoting thyroid cancer metastasis | 10.21203/rs.3.rs-10044394/v1 | IM | Medium* | ✔ | green | HOXC10 转录激活 CCL2 → TAM M2 极化 → 促转移（**预印本，降档**）|
| B2 | AD16 / EP87 / EP1651 — ICI 致肾上腺功能不全合并甲状腺功能障碍（3 篇 ECE 摘要）| 10.1093/ejendo/lvag128.014 等 | IM | Medium* | 否 | hybrid | **边界 off-topic**：非甲状腺癌机制，系 irAE 误匹配，不计入 TC 证据 |
| B3 | Macrophage-Derived Transcriptional Signatures Predict Prognosis and Drug Sensitivity in Thyroid Cancer: SMYD3 | 10.2147/itt.s565624 | IM/AL/PR | Medium | 否 | gold | scRNA hdWGCNA 定义肿瘤富集巨噬模块，117 种 ML 组合建模 + SMYD3 体外验证 |
| B4 | CD44 is associated with PTC metastasis via modulation of the immunosuppressive TME | 10.1007/s10238-026-02101-x | IM/PR | Medium | 否 | gold | 血清 CD44 在 CLNM 患者更高（782 vs 249 pg/mL）；关联 Treg/TGF-β/IL-10；3D 透明化全片成像 |
| B5 | EGR1+CD4+ T Cells tumor-promoting role in PTC | 10.1093/gpbjnl/qzag060 | SC/IM | Medium | 否 | closed | 新型 EGR1⁺CD4⁺ T 亚群产 IL-10/IFN-γ；CD96 或 CD96/TIGIT 共阻断恢复抗瘤免疫 |
| B6 | CREM marks TCR-driven T-cell activation, favorable prognosis in PTC | 10.3390/ijms27167387 | SC/IM/PR | Medium | 否 | gold | CREM 标记 TCR 驱动的即刻早期激活态（非 cAMP 程序），多因素 HR 0.56 |
| B7 | CDKN2A-mediated cuproptosis mechanisms driving TC progression | 10.1038/s41540-026-00663-w | ME/MO/IM | Medium | 否 | gold | CDKN2A 为唯一一致上调的铜死亡相关基因；GAS5/miR-128-3p/CDKN2A 轴经实验验证 |

**单细胞 / 空间组学 (SC / SP)**
| # | Title | DOI | Dim | Rel | Pre | OA | Key finding |
|---|---|---|---|---|---|---|---|
| B8 | Single-cell RNA sequencing: heterogeneity in papillary and anaplastic thyroid carcinoma (review) | 10.1530/etj-25-0141 | SC | Medium | 否 | diamond | 综述 PTC/ATC 单细胞异质性 |
| B9 | Single-cell RNA sequencing in thyroid cancer: methodological review + thyroid dissociation protocol | 10.1186/s13044-026-00306-6 | SC | Medium | 否 | closed | 评估 22 项原发样本 scRNA 研究的方法学报告缺口，给出优化解离方案 |
| B10 | Integrative Single-Cell and ML Analysis Identifies EMT-Associated Prognostic Signature for PTC | 10.1002/cam4.71766 | SC/AL/ST | Medium | 否 | gold | 101 种 ML 算法组合筛选 8 个 EMT 预后基因（含 TYRO3、E2F…）|
| B11 | JAG1 expression in PTC stem-like cells predicts poor prognosis / angiogenesis | 10.1007/s12672-026-04601-4 | SC/ST | Medium | 否 | gold | GSE191288 + GSE250521，CytoTRACE 定义 stemness^High；JAG1 为枢纽基因 |
| B12 | CXCL8/SDC1 axis mediates tumor stem cell interactions driving remote metastasis | 10.1016/j.jpha.2025.101354 | SC/SP/ST | Medium | 否 | gold | CXCL8⁺ 单核 × SDC1⁺ 肿瘤干细胞互作驱动远处转移；scRNA + 空间 + 体外 |
| B13 | CD109-based spatial immunofluorescence delineates PTC→ATC transformation | 10.1038/s41598-026-41927-z | SP/IM/ST | Medium | 否 | gold | PTC/ATC 交界处标记呈相反梯度；ATC-TME 富集 Iba-1⁺/S100⁺ 巨噬与独特 CAF（COL III/VI、TGFBI）|
| B14 | Spatial proteomics + ML for indeterminate thyroid nodules | 10.1007/s12020-026-04552-4 | SP/AL | Medium | 否 | closed | 空间蛋白质组 + ML 诊断签名，作者自述"promising yet preliminary" |
| B15 | Dying cells initiate DLL4–Notch signaling driving tumor repopulation after insufficient thermal ablation of PTC | 10.1186/s12964-026-03106-5 | SP/MO | Medium* | 否 | gold | 消融后死亡细胞经 DLL4–Notch 驱动肿瘤再增殖（**治疗后复发新角度**）|
| B16 | P403 — senescent-like low-differentiation population in BRAF^V600E FCDTC (ECE 摘要) | 10.1093/ejendo/lvag096.534 | SC/SP | Medium | 否 | hybrid | 衰老样低分化细胞群的空间异质性（会议摘要，降档）|

**算法方法 / 预测模型 (AL)**
| # | Title | DOI | Dim | Rel | Pre | OA | Key finding |
|---|---|---|---|---|---|---|---|
| B17 | Nomogram for LN-prRLN metastasis in PTC (n=320) | 10.3389/fendo.2026.1953516 | AL/PR | Medium | 否 | gold | 右喉返神经后淋巴结转移预测列线图，仅内部验证 |
| B18 | Prognostic factors + nomogram for SIR after RAI in intermediate-risk PTC | 10.1002/cnr2.70692 | AL/PR | High→Med* | 否 | gold | 按 2025 ATA 再分层，构建中危患者 SIR 列线图（PMID 42748966）|
| B19 | Multimodal US radiomics for CLNM in PTC (n=470) | 10.1002/jum.70363 | AL/PR | Medium | 否 | closed | 瘤内+瘤周多模态超声影像组学 |
| B20 | Multimodal deep fusion US + clinical for lateral CLNM | 10.1016/j.ultrasmedbio.2026.06.017 | AL/PR | Medium | 否 | closed | 超声图像与临床因素深度融合 |
| B21 | MRI-based radiomics for preoperative CLNM (n=97) | 10.21037/gs-2026-0259 | AL/PR | Medium | 否 | diamond | 前瞻入组 97 例，仅内部验证 |
| B22 | Occult high-volume CLNM in cN0 PTC: multimodal US + radiomics, temporal + external validation (n=814) | 10.4274/dir.2026.264048 | AL/PR | Medium | 否 | closed | **本轮少数含外部验证**的模型 |
| B23 | Nomogram for CLNM in aspect-ratio ≥1 PTC (US + calcitonin) | 10.21037/gs-2026-0193 | AL/PR | Medium | 否 | diamond | 针对超声敏感性仅 ~50% 的特定亚群 |
| B24 | Nomogram for ≥0.2 cm clinically significant LNM burden in pN1 PTC (L2 ridge) | 10.3389/fendo.2026.1848554 | AL/PR | Medium | 否 | gold | 从"有无"升级到"负荷大小"分层 |
| B25 | CLNM risk factors + nomogram, Anhui PTC (n=171, US + gene mutation) | 10.1097/md.0000000000049837 | AL/PR | Medium | 否 | gold | 超声特征 + 基因突变的联合模型 |
| B26 | Nomogram for initial RAI response in DTC with Hashimoto's (n=461) | 10.21037/gs-2026-0252 | AL/PR | Medium | 否 | diamond | 合并桥本者的 RAI 初始疗效预测 |
| B27 | ResTAC-Net: residual texture-attention CNN for thyroid nodule classification | 10.53365/nrfhh.774 | MO/AL | Medium | 否 | closed | 超声结节分类深度网络 |
| B28 | RAIR-Sim: compartmental simulator of RAI therapy response in metastatic TC | 10.5281/zenodo.21496198 | MO/PR/AL | Low* | 否 | — | Zenodo 软件存档型记录（降档）|
| B29 | Correction: ML/DL for thyroid cancer metastasis (systematic review & meta-analysis) | 10.1186/s12911-026-03708-6 | AL/PR | Medium | 否 | gold | 勘误；原文为 ML/DL 转移预测的系统综述与荟萃分析 |
| B30 | P428 — Clustering & response prediction in DTC, Hungarian register (n=833) | 10.1093/ejendo/lvag096.553 | AL/PR | Medium | 否 | hybrid | K-means 四聚类（会议摘要）|
| B31 | OC12.1 — lncRNA + ML for preoperative diagnosis of thyroid cancer | 10.1093/ejendo/lvag096.141 | AL | Low | 否 | hybrid | 会议摘要 |
| B32 | Predictive model for increased postoperative drainage in PTC | 10.21037/gs-2026-0358 | AL/PR | Low | 否 | diamond | 术后引流量预测，与肿瘤学终点弱相关 |
| B33 | Psychological distress prediction in DTC undergoing ¹³¹I | 10.3389/fendo.2026.1877295 | AL/PR | Medium | 否 | gold | 心理困扰风险模型，非肿瘤学终点 |
| B34 | Survival and Recurrence in Thyroid Cancer Brain Metastases | 10.21203/rs.3.rs-9988983/v1 | AL/PR | Medium* | ✔ | green | 脑转移预后因素（**预印本，降档**）|

**分子机制 / 预后转移 (MO / PR)**
| # | Title | DOI | Dim | Rel | Pre | OA | Key finding |
|---|---|---|---|---|---|---|---|
| B35 | NAT10-mediated ac4C acetylation of PPFIA4 mRNA drives PTC progression and LNM via focal adhesion | 10.1038/s41419-026-09251-6 | MO | Medium | 否 | gold | ATF2→NAT10→ac4C 修饰 PPFIA4 mRNA 增强稳定性→重编程黏着斑→LNM（**表观转录组新层**）|
| B36 | ITM2A promotes thyroid cancer differentiation via metabolic reprogramming and enhances PD-L1-dependent T-cell responses | 10.1007/s10238-026-02229-w | ME/IM | Medium | 否 | hybrid | 分化状态 + 代谢重编程 + PD-L1 依赖的 T 细胞应答三者耦合 |
| B37 | MYC-regulated lncRNA SNHG1 controls SKP2-mediated p21 stability under thyroid hormone receptor signaling | 10.1016/j.ijbiomac.2026.154498 | MO | Low | 否 | closed | MYC–SNHG1–SKP2–p21 轴 |
| B38 | CircGABRB2_006 drives malignant progression and EMT via miR-296-5p/FGFR1 | 10.1007/s10528-026-11436-9 | MO | Low | 否 | closed | 环状 RNA–miRNA–FGFR1 轴 |
| B39 | Modulation of TC cell migration/invasion using miRNA-enriched extracellular vesicles | 10.3389/fendo.2026.1884738 | MO | Low | 否 | gold | NThy-ORI 来源 EV 递送 miR-485-5p/miR-495-3p |
| B40 | Detection of thyroglobulin / TSHR / NIS mRNA for LN metastases in PTC (388 FFPE LNs) | 10.1186/s12885-026-16515-z | MO/PR | Medium | 否 | gold | 三基因 mRNA 检测辅助 LNM 判定 |
| B41 | HALP score for thyroid nodules (n=521) | 10.14744/nci.2026.79477 | MO/PR | Medium | 否 | diamond | 免疫营养指数与 LNM 关联 |
| B42 | ABO/Rh blood groups and clinicopathological features in thyroid malignancies | 10.1186/s12902-026-02433-5 | MO/PR | Low | 否 | gold | 血型关联分析，机制薄弱 |
| B43 | TR07 — calcitonin-to-CEA ratio predicts LNM in MTC | 10.1093/ejendo/lvag128.080 | MO/PR | Medium | 否 | hybrid | 术前降钙素/CEA 比值预测中央区与侧颈区 LNM（会议摘要）|
| B44 | OC1.6 — % mutated neoplastic cells predicts persistent/recurrent disease in BRAF-mutated PTC | 10.1093/ejendo/lvag096.082 | MO/PR | Low | 否 | hybrid | 突变细胞比例作为复发风险（会议摘要）|
| B45 | Metastatic colorectal carcinoma to the thyroid gland: case report + review | 10.3892/br.2026.2203 | PR | Medium | 否 | diamond | **转移至甲状腺**（他病来源），非甲状腺癌转移；边界相关 |
| B46 | Persistent calcium dependence after total thyroidectomy: bone hunger syndrome hypothesis | 10.3389/fendo.2026.1901308 | MO/PR | Low | 否 | gold | 术后钙依赖，与肿瘤机制弱相关 |
| B47 | Editorial: Molecular characterization of thyroid lesions, volume III | 10.3389/fendo.2026.1926803 | MO/PR/AL/IM | Medium | 否 | gold | 社论；强调 BRAF/TERT/TP53 应作生物网络节点而非孤立标志 |
| B48 | Liquid biopsy biomarkers in thyroid cancer: current evidence | 10.55640/ijmsdh-12-07-01 | MO/PR | Medium | 否 | diamond | 液体活检系统综述（2020–2026）|
| B49 | Comprehensive evaluation of angiogenesis-associated genes in PTC (bulk + sc) | 10.1007/s00405-026-10456-w | MO/SC | Low | 否 | closed | 41 个血管生成基因 → 6 标志 → qPCR 验证 3 个（CDH13、SPHK1、EMCN）|
| B50 | Comparison of 2015 vs 2025 ATA risk stratification（2 篇 Endocrine Abstracts）| 10.1530/endoabs.119.ps1-08-10 / ps3-04-05 | PR | Low | 否 | — | 会议摘要；2025 ATA 新分层系统的比较 |

**代谢重编程 (ME)**
| # | Title | DOI | Dim | Rel | Pre | OA | Key finding |
|---|---|---|---|---|---|---|---|
| B51 | Metabolic reprogramming in DTC progression: tumor metabolomics analysis | 10.1016/j.surg.2026.110658 | ME | Low | 否 | closed | 肿瘤代谢组学分析（摘要缺失，仅题录）|
| B52 | C/EBPβ drives ATC dedifferentiation and radioiodine resistance via IL-6/JAK/STAT and EMT | 10.21203/rs.3.rs-9248842/v1 | SC/SP/ST/ME | Medium* | ✔ | — | 43,866 细胞 + 空间转录组；C/EBPβ 为去分化主调控因子，抑制 NIS 致碘难治（**预印本**）|

> \* 标记为 Agent 调整后的相关性判断（脚本相关性为关键词启发式，可能与实际议题重要性偏离）。

---

## 4. 已知结论 / What Is Already Known

以下结论有**多篇或强数据集支撑**，采用谨慎表述：

1. **甲状腺癌的免疫微环境是空间结构化的生态位集合，而非均质背景。** 至少有 *Front Immunol*（PMID 42459642）综述共识、*Discov Oncol*（PMID 42217128）的 APOE–NCF1 生态位、*Endocr Relat Cancer*（PMID 42583701）的 BRAF-PTC 髓系全景三项独立工作支持。hot/cold/excluded 框架已成为领域通用语言，但**尚未有统一的可操作量化阈值**。

2. **TAM / 髓系区室是甲状腺癌免疫逃逸的核心执行者，且机制链条正在闭合。** 本轮形成两条独立的因果链：外泌体 **SPP1→CD44→JAK2/STAT3→M2**（PMID 42153613，体外 + 异种移植）与 **TGFβ1→TIM3↑（M2-like 巨噬）**（PMID 42557785）。结合 Run #21 的 TREM2⁺ AHR–IDO1–犬尿氨酸轴与 Run #22 的 SPP1⁺ 关联证据，SPP1⁺/TREM2⁺/TIM3⁺ 三个 TAM 状态已构成可检验的亚群谱系。

3. **淋巴结定植伴随免疫受体下调与 Treg 介导的抑制增强。** *Science Advances*（PMID 42397917）用配对原发–转移 LN 设计证明甲状腺细胞与 TAM 下调 TNFRSF12A、CX3CR1，LN 内诱导 Treg 抑制 CTL，且 **IL7R 高表达提示较好预后**。这与 Run #23 的配对原发–LNM scRNA 资源（10.1080/2162402x.2026.2701504）方向一致。

4. **去分化（PTC→PDTC/ATC）是 CAF 与代谢重编程共同驱动、且可被空间解析的过程。** 三条独立证据：CAF **ZFP57–PKM2–乳酸→TGF-β** 轴驱动去分化与碘难治（PMID 41761234，Visium 空间 + 白藜芦醇逆转）；复发 FTC 中 **UBE2C⁺ ATC-like 细胞**经 COL9A3–整合素 α1β1 与基质互作（PMID 41631714）；ATC 显示 **p53 受抑 + E2F1/7/8 激活 + CD8 耗竭 + Treg 双层抑制**（PMID 42702761）。另有 C/EBPβ 经 IL-6/JAK/STAT 驱动去分化（预印本）。

5. **MTC 是远处转移与代谢异质性机制的高价值亚型。** 本轮两篇高质量工作：RET→OPG 驱动的成骨性骨转移（PMID 42660113，*Cell Rep Med*）与 CHSY1/GAGs 相关的 M3 代谢亚型（PMID 42098434，*Br J Cancer*，多模态验证）。

6. **细胞类型来源明确的预后签名显著优于 bulk 衍生签名。** PRECISE（41 个甲状腺细胞来源基因，MDACC/VUMC/TCGA 三队列，14 年随访，PMID 42008746）与 *Endocr Relat Cancer* 的四基因上皮签名（PMID 42447050）互为独立重复，均显示从 sc/snRNA 定义细胞程序再回映 bulk 的路线可行。

7. **表观转录组（ac4C）是 PTC 淋巴转移的新调控层。** NAT10 经 ATF2 上调，ac4C 修饰 PPFIA4 mRNA 增强稳定性并重编程黏着斑信号（10.1038/s41419-026-09251-6）。此前该层在甲状腺癌中证据稀少。

8. **术前 LNM 风险预测模型已严重饱和。** 本轮 25 条算法方法条目中绝大多数为单中心列线图/影像组学，终点高度同质（CLNM 有无），仅 1 条（10.4274/dir.2026.264048）含外部验证。

---

## 5. 未解问题 / What Remains Unclear

1. **APOE 在甲状腺癌中的方向与功能未知（本轮最关键的开放问题）。** 原跟踪假设是"APOE 阴性/MGST1 阳性的代谢–免疫干性亚群"；本轮唯一直接证据（PMID 42217128）却指向 **APOE 高表达的肿瘤细胞通过 APOE–NCF1 轴驱动 CD8⁺ T 细胞耗竭**。两者不可直接调和，需要明确：APOE 究竟是**免疫抑制配体**、**代谢重编程标记**，还是**随分化状态切换的双功能分子**？**MGST1 在该生态位中的位置完全未被检验。**

2. **APOE–NCF1 与 SPP1–CD44 两条轴是否在同一空间生态位内共存或互斥？** 目前两条链各自独立（前者 scRNA+空间共定位，后者体外+异种移植），**没有任何一项工作同时测量 APOE、SPP1、TREM2、TIM3 的空间分布**。

3. **TAM 亚群的身份界定尚未统一。** SPP1⁺、TREM2⁺、TIM3⁺、M2-like（CD163⁺）四种命名来自不同技术路径，缺乏统一的甲状腺癌 TAM 参考图谱与命名映射。

4. **中性粒细胞在甲状腺癌中的角色几乎空白。** 仅 *Endocr Relat Cancer*（PMID 42583701）提示无淋巴细胞性甲状腺炎的 BRAF-PTC 以中性粒细胞为优势髓系群且表达致癌基因，但**无功能验证、无空间定位、无预后独立性检验**。

5. **去分化的"时间点"与可逆性窗口不明。** ZFP57–PKM2 轴提示白藜芦醇可逆转，但**在体内人组织中的有效浓度与治疗窗口未定**；ATC-like 细胞（UBE2C⁺）是否可在术前/复发早期被检出仍未知。

6. **影像/列线图类预测模型的临床效用未被证明。** 本轮 20+ 模型仅 1 条含外部验证；AUC 提升能否改变手术范围或 RAI 决策，无前瞻性或决策曲线证据。作者本人亦在 FAPI 研究中声明摄取≠组织学证据。

7. **MTC 骨转移机制的临床转化路径不清。** RET–OPG 轴虽清晰，但循环 OPG 作为筛查或疗效监测标志的敏感性/特异性、以及与现有降钙素/CEA 的增量价值未评估。

8. **液体活检与组织空间证据之间缺乏桥接。** 液体活检综述（10.55640/ijmsdh-12-07-01）与空间生态位研究分处两端，**没有研究把 ctDNA/外泌体信号映射回具体空间生态位**。

---

## 6. 领域方法/数据局限 / Method/Data Limitations In The Field

| 局限 | 本轮表现 | 影响 |
|---|---|---|
| **单中心、仅内部验证** | 25 条算法方法中约 20 条；仅 1 条含外部验证 | 模型泛化性不可评估，AUC 不可外推 |
| **小样本单细胞/空间队列** | ATC scRNA n=3+3；髓系全景 n=11；Visium n=3 | 亚群发现为假设生成级，易受批次与取样偏差影响 |
| **计算推断的互作缺乏功能阻断** | APOE–NCF1、COL9A3–整合素、CXCL8–SDC1 均为 CellChat/共定位推断 | 因果性未证，不能直接作为靶点依据 |
| **公共数据复用与批次效应** | 多研究跨 GEO/TCGA/PRJCA 整合，鲜样与固定样混合 | 亚群比例与差异表达可能被技术变异驱动 |
| **终点稀疏与替代终点** | 多数签名以 PFS/LNM 为终点，DSS 事件数少；部分以"初始疗效/引流量/心理困扰"为终点 | 与临床决策的关联弱 |
| **缺乏亚型分层** | 多数模型未按 BRAF/RAS/RET/TERT 或组织学亚型分层 | 效应可能被混合人群稀释 |
| **预印本与存档型记录混入** | 本轮 3 条预印本（HOXC10–CCL2、C/EBPβ、脑转移）+ Zenodo 软件存档 + 9 条会议摘要 | 证据强度需降档；会议摘要无同行评审全文 |
| **检索通道本身的系统性盲区** | OpenAlex 九路查询漏检 23 条 Europe PMC 可检出的高相关文献，含本轮最重要的 APOE 论文 | **单一通道监测会系统性低估领域进展并产生"假平台期"** |
| **他病/irAE 误匹配** | 3 条 ICI 甲状腺 irAE 摘要、1 条结直肠癌甲状腺转移 | 需人工边界标注，不可计入机制证据 |

---

## 7. 候选未来方向 / Candidate Future Directions

评分依据 `research-direction-rubric.md` 七维 1–5 分，28–35 为强候选。

| ID | Direction / 方向 | Rationale / 依据 | Rubric | Required Data / 所需数据 | Validation Plan / 验证 | Main Risk / 主要风险 | Claim Boundary / 声明边界 |
|---|---|---|---:|---|---|---|---|
| **D3′** | **APOE⁺ 肿瘤细胞–CD8⁺ Tex 免疫抑制生态位的空间解析与功能验证**（原 D3 重构）| 首次直接锚定 APOE 的原发证据（PMID 42217128），带空间共定位与跨队列签名；但方向与原假设相反，必须重构 | **29** | 配对原发–LNM scRNA（10.1080/2162402x.2026.2701504）、JCI Insight 空间图谱（10.1172/jci.insight.191990）、TCGA-THCA、自有 mIF 队列 | ①独立空间队列复现 APOE⁺/Tex 共定位；②APOE 阻断或 NCF1 敲低的体外共培养；③签名在外部队列的 C-index | APOE 可能为双向功能分子；共定位≠互作 | 只能声称"生态位关联与空间共定位"，**不得声称 APOE 为治疗靶点**直至功能阻断完成 |
| **D9** | **SPP1⁺ × TREM2⁺（× TIM3⁺）TAM 生态位共定位与统一命名** | 外泌体 SPP1→CD44→JAK2/STAT3 提供因果链（PMID 42153613）；与 Run #21 TREM2⁺ 轴、本轮 TIM3 轴交汇 | **32** | 同上空间图谱 + 配对原发–LNM scRNA + 自有多重免疫荧光 | 多重免疫荧光四色共定位；体外 SPP1 敲除 × TREM2 阻断的正交验证；外部队列预后增量 | TAM 命名混乱；SPP1 方向拥挤度上升 | 声称"亚群共定位与功能互作"，**不声称单一亚群主导** |
| **D15** | **去分化轨迹的细胞态解析：ATC-like 前体态、CAF–乳酸生态位与可逆性窗口** | 三路独立证据汇聚（UBE2C⁺ ATC-like；ZFP57–PKM2–乳酸 + 白藜芦醇逆转；p53/E2F 轴）；C/EBPβ 预印本补充 | **30** | 跨阶段 scRNA（PTC/FVPTC/FTC/ATC）、10× Visium 或 GeoMx、配对原发–复发样本 | UBE2C/ZFP57 在独立复发队列的 IHC 验证；类器官或 PDX 的乳酸/白藜芦醇剂量–效应；NIS 摄碘功能读数 | 去分化样本稀缺；白藜芦醇浓度生理性存疑 | **不声称"逆转去分化"的临床可行性**，仅限体外/体内概念验证 |
| **D8** | **甲状腺癌髓系全景：TAM × 中性粒细胞 × 甲状腺炎背景** | 本轮首次把中性粒细胞与淋巴细胞性甲状腺炎纳入髓系框架（PMID 42583701），并获 TIM3 可成药节点 | **32** | BRAF-PTC ± LT 队列 scRNA、多重免疫荧光、公共 scRNA 荟萃 | 中性粒细胞耗竭/趋化阻断的体内验证；ECRG4 功能验证；跨队列髓系比例复核 | 中性粒细胞在甲状腺癌中研究极少，抗体重现性问题 | 区分"髓系组成关联"与"髓系因果驱动" |
| **D11** | **乳酸/代谢–EMT–去分化轴的代谢流解析** | ZFP57–PKM2–乳酸（PMID 41761234）+ CHSY1/GAGs（PMID 42098434）+ ITM2A/PD-L1（10.1007/s10238-026-02229-w） | **31** | 空间代谢组（MALDI/AFDESI）+ 配对转录组、Seahorse、稳定同位素示踪 | 乳酸流同位素示踪 + CAF-肿瘤共培养梯度；EMT 标志空间梯度量化 | 代谢组空间分辨率限制；体外糖酵解条件与体内差异 | 不将代谢物浓度直接等同于通路活性 |
| **D14** | **细胞类型解析 + 空间多组学的因果与方法学框架**（含 ML 亚型的组学验证范式）| *Cell Rep Med* 蛋白基因组 ML 分类器由 scRNA/空间独立验证（PMID 41794039）树立范式；Run #23 已立方向，本轮获范式级支撑 | **28** | TCGA/CPTAC、GEO 空间数据集、孟德尔随机化汇总数据 | 分类器在独立空间队列复现；因果推断的阴性对照与敏感性分析 | 蛋白基因组数据获取门槛；MR 假设可检验性 | 声明"统计学支持的细胞类型特异关联"，**不声称个体水平因果** |
| **D16** | **MTC 器官特异性远处转移机制：RET–OPG 骨转移轴 + 液体活检** | 本轮最高质量远处转移原发证据（PMID 42660113）| **27** | MTC 骨转移组织、配对血清 OPG/降钙素/CEA、RET 抑制剂治疗队列 | OPG 在独立 MTC 血清队列的 ROC；与降钙素/CEA 的净重分类改善（NRI）| MTC 发病率低，样本获取难；OPG 受骨代谢混杂 | 不声称 OPG 可替代现有标志，仅评估增量价值 |
| **D13** | **术前 LNM 预测模型（影像/临床）** | 本轮增量最大（25 条）但同质化严重 | **26** | 多中心超声/MRI/CT、术后病理金标准 | 外部多中心验证 + 决策曲线分析 + 前瞻性影响研究 | 方向拥挤；缺乏改变临床行为的证据 | 仅声称"判别性能"，**不声称临床效用** |
| **D12** | 铁死亡/铜死亡等新型程序性死亡 | CDKN2A 铜死亡（10.1038/s41540-026-00663-w）等持续有产出但缺乏甲状腺特异机制 | **27** | TCGA、DepMap、体外铁/铜死亡诱导 | 特异性诱导剂在甲状腺细胞系的剂量验证 | 可能存在泛癌共性而非甲状腺特异 | 不声称亚型特异性 |

---

## 8. 推荐下一步方向 / Recommended Next Direction

### ⭐ 首选：**以 APOE⁺ 肿瘤细胞–CD8⁺ Tex 生态位为锚、联合 SPP1⁺/TREM2⁺/TIM3⁺ TAM 的甲状腺癌免疫抑制空间生态位图谱（D3′ + D9 合并推进）**

**为什么是它：**
1. **时机唯一**：持续跟踪 23 轮的 D3 方向首次拿到直接锚定证据，且该证据**推翻了原假设的方向**。这是 24 轮以来跟踪方向上第一次出现"实质性变化"——不立即跟进，就会把一个已经可操作的线索重新放回未知。
2. **可行性高**：所需数据**现已公开可用** —— 配对原发–LNM scRNA 图谱（10.1080/2162402x.2026.2701504，gold OA）、JCI Insight 整合单细胞 + 空间图谱（10.1172/jci.insight.191990，gold）、*Science Advances* 配对原发–LN 数据集（PMID 42397917，gold）、TCGA-THCA。
3. **可发表性强**：APOE–NCF1 与 SPP1–CD44 两条轴**从未被放在同一空间框架内检验**，这是一个明确的、可一次性回答的空白。
4. **rubric 综合最优**：D9 = 32、D3′ = 29，合并推进可同时满足新颖性、可验证性与临床相关性。

**第一批具体步骤（4 周内）：**
1. 在 JCI Insight 空间图谱与配对原发–LNM scRNA 中，**重新计算** APOE、NCF1、SPP1、TREM2、HAVCR2、CD163、CD8A 的共表达与空间邻近度，输出生态位评分（而非仅差异表达）。
2. 把 *Science Advances* 配对原发–LN 数据作为**第一批独立验证集**，检验 APOE⁺ 亚群在 LN 定植后是否扩张。
3. 用 **CellChat / NicheNet** 显式检验 APOE–NCF1 与 SPP1–CD44 两条配体–受体轴，并加入 Run #21 的 AHR–IDO1 轴作为对照。
4. 设计**四色多重免疫荧光**（APOE / SPP1 / CD163 / CD8）在 10–15 例自有配对原发–LNM 蜡块上的验证方案（此为湿实验门槛，明确标注为下一步）。
5. **必须避免的声明**：不得声称 APOE 为治疗靶点，不得声称单一 TAM 亚群主导免疫逃逸，不得把共定位等同于功能互作。

**次选（并行启动，不占用主资源）：** D15 去分化轨迹预研 —— 复用 Run #23 已产出的 `D3_D9_spatial_anchor_preresearch.md` 数据集清单，把 UBE2C 与 ZFP57 加入待检验标志物面板。

---

## 9. 随访阅读清单 / Follow-Up Reading List

**优先级 1（立即精读，直接决定下一步）**
- **APOE–NCF1 生态位**（PMID 42217128, 10.1007/s12672-026-05061-6, gold）：本轮最重要的方向性证据，需逐字核对 Trem/T01 亚群定义、空间共定位统计方法与签名构成基因。
- **外泌体 SPP1–CD44–JAK2/STAT3**（PMID 42153613, 10.1080/15476278.2026.2670152, gold）：D9 的因果链原文，需核对 CD44 阻断的剂量与特异性。
- **配对原发–LNM scRNA**（PMID 42397917, 10.1126/sciadv.aea4727, gold）：本轮设计最严谨的免疫图谱，是 D3′/D9 的第一验证集。
- **ZFP57–PKM2–乳酸–白藜芦醇**（PMID 41761234, 10.1186/s13046-026-03675-w, gold）：空间 + 代谢 + 去分化 + 干预四维闭环，D11/D15 的方法学模板。

**优先级 2（方法学与数据集）**
- **PRECISE**（PMID 42008746, 10.1158/1078-0432.ccr-25-4488）：细胞类型来源签名的质量标杆，14 年随访。
- **晚期 DTC 蛋白基因组三亚型 + ML 分类器**（PMID 41794039, 10.1016/j.xcrm.2026.102661, gold）：ML 分类器的组学验证范式，D14 的模板。
- **ATC-like 细胞 / UBE2C**（PMID 41631714, 10.1210/endocr/bqag012）：复发 FTC 去分化的可操作标志。
- **髓系全景 BRAF-PTC ± 甲状腺炎**（PMID 42583701, 10.1530/erc-26-0088, gold）：中性粒细胞视角的开创性工作。

**优先级 3（背景与补充）**
- TIM3 ATC（PMID 42557785）、ATC 单细胞（PMID 42702761）、MTC 代谢亚型（PMID 42098434）、RET–OPG 骨转移（PMID 42660113）、NAT10/ac4C–PPFIA4（10.1038/s41419-026-09251-6）。
- 甲状腺 scRNA 方法学综述 + 解离方案（PMID 42363265）：若启动自有单细胞实验，必读。

**降级处理（预印本/会议摘要，仅作线索跟踪）**
- HOXC10–CCL2–M2（10.21203/rs.3.rs-10044394/v1）、C/EBPβ（10.21203/rs.3.rs-9248842/v1）、脑转移预后（10.21203/rs.3.rs-9988983/v1）、ECE 2026 摘要 9 篇。

---

## 10. 可复现性说明 / Reproducibility Notes

- **检索日期 / Search date**: 2026-09-18 23:02–23:20 (GMT+8)
- **数据库 / Databases**: OpenAlex（`api.openalex.org`，主源）、Europe PMC（`www.ebi.ac.uk/europepmc`，本轮新增交叉补检）、Crossref（DOI 元数据）、Unpaywall（OA 解析）
- **未使用 / Not used**: NCBI eutils / PubMed（本机 HTTP 000 不可达，按 `RETRIEVAL_ENVIRONMENT.md` 禁止直连）；paper-search-mcp（本会话未连接）
- **查询串 / Query strings**: 见第 1 节表格；OpenAlex 九路 `title_and_abstract.search`，`sort=publication_date:desc`；Europe PMC 三路 `TITLE:"thyroid"` 约束 + `sort=P_PDATE_D desc`
- **过滤 / Filters**: 发表日期窗口（30 d / 90 d）；每路 per-page 25（30 d）与 50（90 d）；Europe PMC pageSize 50
- **去重规则 / Deduplication**: DOI 小写主键优先 → 标题归一化（去标点、小写、截 70 字符）兜底；OpenAlex 多版本（仓储副本/出版版本）按标题合并；PRECISE 数据存档并入正文
- **筛选规则 / Screening**: 标题必须点名甲状腺 **且** 整体为肿瘤主题；`SUPPLEMENT` 正则剔除期刊补充材料；非肿瘤甲状腺主题（良性/自身免疫）剔除；ICI 相关 irAE 与他病甲状腺转移标记为边界 off-topic
- **通道健康 / Channel health**: 本轮 OpenAlex / Europe PMC / Crossref / Unpaywall **全部可用**；Crossref 10/10、Unpaywall 10/10 成功（Run #22 的 SSL 握手超时问题本轮消失）
- **脚本 / Scripts**: `oa_search.py`（主检索 + 清洗）、`_run24_merged.json`（两窗口合并）、`_epmc_run24.py` / `_epmc_detail.py` / `_epmc_detail2.py` / `_epmc_pack.py`（跨源补检）、`_enrich_run24.py`（DOI/OA 校验）、`_merge_run24.py`（基线回写）
- **产出文件 / Artifacts**:
  - `literature_review_20260918_232000.md`（本报告）
  - `search_results_20260918_230300.json`（OpenAlex 30 d 主窗口）
  - `search_results_20260918_90day.json`（OpenAlex 90 d 补跑）
  - `search_results_20260918_epmc.json` + `_epmc_detail_run24.json` + `_epmc_detail2_run24.json`（Europe PMC 补检）
  - `search_results_20260918_enrich.json`（Crossref/Unpaywall 校验，10/10 成功）
  - `search_results_20260918_232000.json`（**累积基线 245 条**，含 `new_records` 74 条）
  - `search_results_latest.json`（同上，已回写）
- **标识符政策 / Identifier policy**: 近 30 天新文献多数尚无 PMID，一律以 DOI 为主标识，PMID 缺失标注「待编目」；**未编造任何 PMID 或 DOI**。预印本单独标注并降档。

---

## 11. 与历史报告的差异 / Delta vs. Previous Reports

### 11.1 数量差异 / Quantitative Delta

| 指标 | Run #23 (2026-09-17) | **Run #24 (2026-09-18)** | 变化 |
|---|---:|---:|---|
| 累积基线 | 171 | **245** | **+74** |
| 主窗口新增 | 22（15 主 + 6 ST 90 d + 1 溢出）| **74**（7 主窗口 + 44 90 d 净增 + 23 跨源）| +52 |
| High 相关性 | 2 | **18** | +16 |
| 预印本 | 1（+3 降档存档）| **3** | +2 |
| 涉及维度数 | 8 | **8**（全维度）| 持平 |

### 11.2 本轮相对上轮的新信号 / New Signals

| 信号 | Run #23 状态 | **Run #24 状态** | 性质 |
|---|---|---|---|
| **D3（APOE−/MGST1+ 代谢–免疫干性亚群）** | 连续 23 轮无直接锚定证据，维持 33「无变化」| **首次获直接证据（APOE–NCF1 生态位，PMID 42217128），但方向与原假设相反 → 重构为 D3′，rubric 33→29** | ⚠️ **实质性变化（重构）** |
| **D9（SPP1⁺ TAM）** | Run #22 强化后 Run #23 暂停（31）| **获直接因果链（外泌体 SPP1→CD44→JAK2/STAT3，PMID 42153613）→ 31→32** | ✅ **强化** |
| **D11（乳酸–EMT–去分化）** | 维持 30 | **ZFP57–PKM2–乳酸 + 白藜芦醇逆转（空间验证）；CHSY1/GAGs；C/EBPβ 预印本 → 31** | ✅ **强化** |
| **D8（TREM2⁺ AHR–IDO1）** | 维持 32（拓宽）| **维持 32，新增中性粒细胞维度（ECRG4）与可成药节点 TIM3** | ➖ 维持 + 拓宽 |
| **去分化/ATC 轨迹** | 作为 D11/ST 的组成部分 | **独立成簇（5 篇）→ 新立 D15（rubric 30）** | 🆕 **新方向** |
| **MTC 远处转移机制** | 未单列 | **RET–OPG 成骨性骨转移（Cell Rep Med）→ 新立 D16（rubric 27）** | 🆕 **新方向** |
| **D14（细胞类型解析因果 + 空间方法）** | 28（新立）| **获范式级支撑：蛋白基因组 ML 分类器由 sc/空间独立验证 → 维持 28，可执行性提升** | ➖ 维持 + 强化可执行性 |
| **D13（临床 LNM 预测模型）** | 26（新立）| 维持 26，**增量最大（25 条）但同质化更严重**，仅 1 条含外部验证 | ➖ 维持（拥挤度上升）|
| **D12（铁死亡/铜死亡）** | 27 | 维持 27（CDKN2A 铜死亡新数据点）| ➖ 维持 |

### 11.3 方法学差异（本轮最重要的方法论发现）

**本轮引入 Europe PMC 作为跨源交叉补检通道，一次性暴露了 OpenAlex 九路查询矩阵的系统性盲区：**
- Europe PMC 三路查询共命中 107 条，其中 **81 条未出现在 171 条累积基线中**；经人工筛选纳入 23 条高相关文献。
- 漏检的**不是边缘文献**：包括本轮最重要的 APOE–NCF1 生态位论文（PMID 42217128）、SPP1 外泌体机制（PMID 42153613）、PRECISE 正文（PMID 42008746）、MTC 代谢亚型（PMID 42098434）、蛋白基因组三亚型（PMID 41794039）等 10 条 **High** 相关性工作。
- **根因**：OpenAlex 查询要求甲状腺词与"转移/侵袭/预后"等词在 `title_and_abstract.search` 中共同出现，而一批高质量工作把机制写在标题、把"thyroid"只放在标题但摘要用 "THCA/PTC" 缩写，或反之，导致布尔条件失配。
- **结论**：**前 23 轮的"零新增/低新增"至少有相当部分属于通道性欠采样，而非领域平台期。** 建议自下一轮起把 Europe PMC 纳入常规双通道（与 OpenAlex 并行），而不是临时补检。

### 11.4 关于「平台期 vs 通道问题」的明确回答

**本轮不是领域平台期，也不是检索窗口问题，而是"基线补全 + 通道扩展"的一次性回补。**
- 30 天主窗口的 **7 条**真增量对应 1 天间隔（Run #23 于 2026-09-17 执行），属于**正常的日更量级**，领域活跃度正常。
- 90 天补跑的 44 条净增，来自 IM/SC/SP/ST 四个维度在 30 天窗口内的结构性欠采样——这与 Run #21（单细胞）、Run #22（代谢）、Run #23（转移干性）观察到的现象**完全一致**，已连续四轮验证：**30 天窗口对低频高分维度系统性不足**。
- Europe PMC 的 23 条则纯粹是**跨源补漏**，与窗口无关。

**下一轮调整建议（三项，均有本轮证据支撑）：**
1. **把 Europe PMC 固化为常规第二通道**，与 OpenAlex 并行执行，至少覆盖 SC / SP / IM / ST 四个高频漏检维度。（本轮最强建议）
2. **对 SC / SP / IM / ST / ME 五个维度默认使用 90 天窗口**，MO / PR / AL 保留 30 天；或统一 90 天 + DOI 去重。连续四轮证据表明 30 天窗口在这五个维度上不可靠。
3. **在查询式中显式加入缩写同义词**（`THCA`、`PTC`、`FTC`、`MTC`、`ATC`、`DTC`、`FCDTC`），并把"thyroid"约束从 `title_and_abstract.search` 拆成 `title.search` 与 `abstract.search` 的并集，降低布尔失配率。

### 11.5 持续跟踪方向状态总表 / Longitudinal Tracking Status

| 方向 | 连续轮次 | 本轮证据 | 状态 | Rubric |
|---|---:|---|---|---:|
| **D3 → D3′（APOE 代谢–免疫生态位）** | 24 | **首次直接锚定（方向相反）** | ⚠️ **重构 Reframed** | 33 → **29** |
| D8（TREM2⁺/TAM 全景） | 5 | 中性粒细胞维度 + TIM3 节点 | 维持 + 拓宽 | 32 |
| D9（SPP1⁺ TAM） | 3 | **直接因果链** | ✅ 强化 | 31 → **32** |
| D11（乳酸–EMT–去分化） | 4 | ZFP57–PKM2 + CHSY1 + C/EBPβ | ✅ 强化 | 30 → **31** |
| **D15（去分化/ATC-like 轨迹）** | 1（新） | 5 篇独立证据簇 | 🆕 新立 | **30** |
| D14（细胞类型因果 + 空间方法） | 2 | 蛋白基因组 ML 范式 | 维持 + 可执行性↑ | 28 |
| D12（铁死亡/铜死亡） | 3 | CDKN2A 铜死亡 | 维持 | 27 |
| **D16（MTC 远处转移机制）** | 1（新） | RET–OPG 骨转移 | 🆕 新立 | **27** |
| D13（临床 LNM 预测模型） | 2 | 25 条增量，同质化↑ | 维持（拥挤度↑）| 26 |

---

*报告生成：2026-09-18 23:20 (GMT+8) · Run #24 · 基线 245 条 · 本轮新增 74 条（OpenAlex 51 + Europe PMC 23）*
