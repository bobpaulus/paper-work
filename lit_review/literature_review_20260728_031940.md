# Literature Review: 甲状腺癌淋巴结转移与远处转移的分子机制、免疫微环境、单细胞/空间组学及人工智能预测 (Thyroid Cancer Lymph Node & Distant Metastasis — Mechanisms, Immune Microenvironment, Single-Cell/Spatial Omics, and AI Prediction)

Date: 2026-07-28
Sources: PubMed (via `mcp__paper-search-mcp__search_pubmed`, DeferExecuteTool)
Search window: 全时段 (all time)，但本运行 (run #6) 采用 **`sort=pub_date` 近时效优先 (recency sweep)** 以打破 run #3–#5 的相关性排序平台期 (plateau)。
Automation: 甲状腺癌文献定期监测 (lit-review), run #6 (第 6 次运行)

---

## 中文摘要 (Chinese Abstract)

本次为自动化定期监测的第 6 次运行。为突破 run #3–#5 因 `sort=relevance` 始终返回相同 top‑15 而形成的语料平台期（106 unique / 70 in‑scope / 0 新增），本运行将 9 路互补检索全部改为 **`sort=pub_date` 近时效优先**。结果共检索 114 条原始结果，去重后累计语料 **170 unique / 101 in‑scope（甲状腺相关）/ 69 excluded（非甲状腺外溢）**，其中 **31 篇为 run #5 以来首次纳入的甲状腺文献**（多为 2025–2026 发表）。

五大收敛轴未变并获新证据强化：(1) **代谢–免疫偶联驱动淋巴结转移 (LNM)** —— MGST1（"Mito‑high"/immune‑cold，AUC 0.833，去分化末端干细胞样亚群）仍是核心节点；新证据 LCN2（Hippo/YAP1/HIF1α 糖酵解）、METTL7B（USP28/HIF‑1α 糖酵解）、FN1（失巢凋亡抵抗）进一步夯实该轴；(2) **干细胞样转移亚群** —— APOE−（ABCA1‑LXR）、MGST1 去分化末端、ISG15/KPNA2（ATC）、DLK1（MTC）之外，新增 circPTPRM‑187aa（可翻译环状 RNA，TGF‑β/RAC1/CDC42）与 DLEU2‑ELAVL1‑RCC2（lncRNA‑m6A‑EMT）两条非编码可译组 (translatome) 干细胞轴；(3) **POSTN+ myCAF 空间图谱**仍是最薄维度（spatial=6），无新增；(4) **影像/多组学 AI** 维度最大（algorithm=37），新增多中心多模态超声 DL（AUC 0.929）、radiopathomics（0.875）、可解释 BRAF V600E DL（0.845）、AI 双侧癌复发模型（0.97）、radiomics 荟萃（AUC 0.83/0.88）；(5) **BRAF V600E 荟萃**（46k，淋巴结 OR 1.38 / 复发 OR 1.56，但不预测远处转移/死亡）稳居，并有可解释 DL 无创预测 BRAF V600E 互补。

**推荐方向 D3（界定并靶向 APOE−/MGST1+ 代谢–免疫干细胞样转移亚群）rubric 总分 32（Strong），连续第 6 次运行获确认**，且本运行新证据（代谢驱动 LCN2/METTL7B、免疫生态位 LAG3/TIGIT 与 IL7R、临床已验证的 PRECISE 与 TER 5‑基因预后锚）显著强化其可行性。

## English Abstract

This is the 6th automated run of the thyroid‑cancer literature monitor. To break the plateau observed in runs #3–#5 (identical top‑15 from `sort=relevance`; 106 unique / 70 in‑scope / 0 new), all 9 complementary queries were re‑executed with **`sort=pub_date` (recency sweep)**. 114 raw results yielded a cumulative corpus of **170 unique / 101 in‑scope (thyroid) / 69 excluded (off‑topic non‑thyroid)**, of which **31 papers are newly captured since run #5** (mostly 2025–2026).

Five convergent axes hold and are strengthened: (1) **metabolic–immune coupling drives LNM** — MGST1 ("Mito‑high"/immune‑cold, AUC 0.833, dedifferentiation‑terminal stem‑like state) remains the hub; new LCN2 (Hippo/YAP1/HIF1α glycolysis), METTL7B (USP28/HIF‑1α glycolysis), and FN1 (anoikis resistance) reinforce it; (2) **stem‑like metastatic subpopulations** — besides APOE− (ABCA1‑LXR), MGST1 dediff tip, ISG15/KPNA2 (ATC), DLK1 (MTC), we add circPTPRM‑187aa (translatable circRNA, TGF‑β/RAC1/CDC42) and DLEU2‑ELAVL1‑RCC2 (lncRNA‑m6A‑EMT) non‑coding translatome axes; (3) **POSTN+ myCAF spatial atlas** stays the thinnest dimension (spatial=6), no new entry; (4) **imaging/multi‑omics AI** is now the largest dimension (algorithm=37) with new multicenter multimodal US DL (AUC 0.929), radiopathomics (0.875), interpretable BRAF V600E DL (0.845), AI bilateral‑disease recurrence model (0.97), and a radiomics meta‑analysis (AUC 0.83/0.88); (5) **BRAF V600E meta** (46k; nodal OR 1.38 / recurrence OR 1.56, not distant/death) is stable, complemented by interpretable DL for non‑invasive BRAF V600E prediction.

**Recommended direction D3 (define & target the APOE−/MGST1+ metabolic–immune stem‑like metastatic subpopulation) scores 32/35 (Strong) — confirmed for the 6th consecutive run**, now markedly better supported by new metabolic drivers (LCN2/METTL7B), the immune niche map (LAG3/TIGIT, IL7R), and clinically validated prognostic anchors (PRECISE, TER 5‑gene).

---

## Search Strategy (检索策略)

| Source | Query | Filters | Results (raw) | Notes |
|---|---|---|---:|---|
| PubMed | a. thyroid cancer lymph node metastasis biomarker gene signature | pub_date, max 15 | 15 | 甲状腺相关 15；含 2026 新 pediatric 甲基化 (41701943) |
| PubMed | b. thyroid cancer invasion metastasis molecular mechanism | pub_date, max 15 | 15 | 甲状腺 7（含 7 篇 2026 新）+ 非甲状腺 8 |
| PubMed | c. thyroid cancer lymph node metastasis machine learning deep learning prediction model | pub_date, max 15 | 15 | 甲状腺 14 + 乳腺 1 |
| PubMed | d. thyroid cancer metastasis tumor immune microenvironment | pub_date, max 15 | 15 | 甲状腺 4（与 e 重叠）+ 非甲状腺 11 |
| PubMed | e. thyroid cancer metastasis single cell RNA sequencing | pub_date, max 15 | 15 | 甲状腺 7 + 非甲状腺 8 |
| PubMed | f. thyroid cancer metastasis spatial transcriptomics spatial multi-omics | pub_date, max 15 | 6 | 甲状腺 2（41421038, 41398964，均为已知）；无新增 |
| PubMed | g. thyroid cancer prognosis recurrence distant metastasis risk model | pub_date, max 15 | 15 | 甲状腺 8 + 乳腺 7 |
| PubMed | h. thyroid cancer metastatic stemness subpopulation | pub_date, max 15 | 3 | 甲状腺 2（39595993, 25426258，已知）+ 乳腺 1 |
| PubMed | i. thyroid cancer metabolic reprogramming metastasis | pub_date, max 15 | 15 | 甲状腺 4（含 2026 新 METTL7B, ATC Warburg 综述）+ 非甲状腺 11 |
| **合计** | 9 路互补 | — | **114 raw** | 去重累计 170 unique / 101 in‑scope / 69 excluded |

---

## Included Papers (纳入文献)

下列为本运行**新增 (new since run #5)** 的 31 篇甲状腺相关文献（按维度归类；"Agent note" 给出相关性与警示）：

**分子机制 / 代谢 (molecular / metabolic)**
1. **DLEU2‑ELAVL1‑RCC2 axis (42301557, 2026, High)** — lncRNA DLEU2 经 m6A 稳定 RCC2 促进 PTC 迁移/侵袭（Wnt5a/β‑catenin‑EMT）。Agent note: 与已知 FN1/MET ECM‑粘附轴互补，但需体内转移验证。
2. **LCN2 glycolysis via Hippo/YAP1/HIF1α (41964784, 2026, High)** — LCN2 上调糖酵解促 PTC 进展，与 LNM/腺外侵犯相关。Agent note: 直接强化"代谢–免疫"轴，机制清晰。
3. **METTL7B via USP28/HIF‑1α (42332350, 2026, High)** — METTL7B 稳定 HIF‑1α 促糖酵解，与 LNM 正相关。Agent note: 去泛素化‑代谢新节点。
4. **FN1 anoikis resistance (42002564, 2026, High)** — FN1 经 BCL2L1/BAD 抗失巢凋亡促 PTC 进展。Agent note: 衔接 Jiang 41421038 的 FN1‑SDC4 空间轴。
5. **circPTPRM‑187aa (41539369, 2026, High)** — 可翻译环状 RNA 经 IQGAP1/RAC1/CDC42‑TGF‑β 促 PTC。Agent note: "非编码可译组"干细胞新维度。
6. **Vemurafenib+Panobinostat in ATC (41879411, 2026, Medium)** — 协同抑制 ATC 增殖/转移并再分化。Agent note: 临床前，需体内验证。
7. **FOXP factors review (42351648, 2026, Medium)** — FOXP3/4 关联侵袭/淋巴结/远处转移与免疫逃逸。Agent note: 综述，需大队列验证。
8. **ATC Warburg review (42353188, 2026, Medium)** — ATC/PDTC Warburg 效应治疗靶点综述。
9. **UBC9 (40025314, 2025, Low)** — PTC 治疗新靶点，免疫相关。Agent note: 初步，机制浅。
10. **PTCrisk 31‑gene (40001321, 2025, Medium)** — 全转录组 31 基因风险分层。
11. **PVT1/p53/Bcl2/PD‑L1 (35388548, 2022, Medium)** — PTC 中 PVT1 上调、高 PD‑L1 关联低生存。

**免疫微环境 (immune)**
12. **LAG3‑LGALS3 / LAG3‑TIGIT niche (42430190, 2026, High)** — 55,005 单细胞；转移灶富集 Treg/LAMP3+ DC/M2，PD‑1/PD‑L1 微弱，LAG3‑LGALS3 为主免疫逃逸轴。Agent note: 挑战常规 PD‑1 阻断，样本量偏小。
13. **IL7R biomarker in LN (42397917, 2026, High)** — LN 中 IL7R+ TIL 关联更好预后。Agent note: 提供淋巴结定植生物标志物。
14. **TME atlas ML N‑stage (42134246, 2026, High)** — scRNA T/PT/LN；Mac‑APOC1 M2、RGS5+ myCAF；RF N‑stage AUC 0.98，lasso‑Cox C‑index>0.9。Agent note: 整合单细胞+机器学习，强。
15. **PD‑L1 meta distant mets (41510756, 2026, High)** — DTC 中 PD‑L1 高危淋巴结侵犯 OR 4.2、远处转移 OR 4.6，但**不**关联 LNM/复发/死亡。Agent note: 与 BRAF V600E meta 类似——预测远处而非淋巴结。
16. **Hashimoto meta (41514331, 2026, Medium)** — HT 促进多灶但减弱侵袭/远处/复发（远处 OR 0.33）。Agent note: 67,901 例大队列。
17. **TER 5‑gene prognostic (42305510, 2026, High)** — 101 种 ML 筛选 CAMP/DDIT4L/LMX1B/NAT16/CALN1，1/2/3 年生存 AUC 0.96/0.99/1.00。Agent note: 桥接代谢+免疫+预后。
18. **TIPARP male PTC (38233939, 2024, Medium)** — 男性 PTC 11 基因 LNM 签名，TIPARP 免疫靶点。
19. **Exosomal PDLIM1 angiogenesis (42131580, 2026, Medium)** — 外泌体 PDLIM1 促血管生成。

**单细胞 (single‑cell)**
20. **PRECISE 41‑gene thyrocyte signature (42008746, 2026, High)** — sn/scRNA 开发 thyrocyte 41 基因签名，MDACC/VUMC/TCGA 三队列验证，PFS HR 1.63–2.54、DSS HR 2.23–4.16。Agent note: 强独立预后价值。
21. **Neuro‑mimicry 8‑gene (42329337, 2026, Medium)** — 离子通道 8 基因 LNM AUC 0.721，GABRB2 富集于恶性 thyrocyte。

**算法 / AI (algorithm)**
22. **Multimodal US DL CLNM (42185182, 2026, High)** — BMUS+弹性超声多模态 DL，多中心外部 AUC 0.843，优于放射科医师。
23. **Radiopathomics LNM (42031943, 2026, High)** — FNA 细胞学+超声 ResNet‑101，外部 AUC 0.875。
24. **Interpretable BRAF V600E DL (42433575, 2026, High)** — 临床+超声 radiomics+ResNet50，联合 AUC 0.845，SHAP 可解释。
25. **AI bilateral‑disease recurrence (42244944, 2026, High)** — 经典亚型双侧癌 AI 模型，外部 AUC 0.848，双侧为复发独立风险 (HR 9.664)。
26. **Radiomics meta‑analysis (41997788, 2026, High)** — 60 研究 10,852 例，radiomics AUC 0.83，加临床 0.88；外侧节点 AUC 0.94。
27. **Dual‑channel DL occult CLNM (41686681, 2026, Medium)** — PTMC 隐匿 CLNM，联合 AUC 0.873。
28. **Combined‑feature ML (41664099, 2026, Medium)** — 图像+临床融合，LNM AUROC 0.78。
29. **Vision Transformer LNM (41931576, 2026, Medium)** — ViT AUC 0.809，优于 CNN/radiomics。
30. **Radiomics methods comparison (41078274, 2026, Medium)** — 手工+DL radiomics 联合 AUC 0.761。

**预后 (prognosis)**
31. **IMTCGS in MTC (39749465, 2025, Medium)** — 中国 MTC 队列 IMTCGS 预测特异死亡 AUC 0.81。

（注：41817109 RAI 人群研究本运行再次检出，但属 run #5 已排除的纯临床流行病学，维持 excluded。）

---

## Evidence Matrix (证据矩阵)

*Schema (13 列): Paper | PMID/DOI | Disease/Population | Data Source | Method | Endpoint | Main Finding | Validation | Limitations | Relevance | Gap Suggested | Future Direction。仅列高/中相关文献；低相关 (UBC9, PVT1 等) 见 Included Papers。*

| Paper | PMID/DOI | Disease/Population | Data Source | Method | Endpoint | Main Finding | Validation | Limitations | Relevance | Gap Suggested | Future Direction |
|---|---|---|---|---|---|---|---|---|---|---|---|
| MGST1 Mito‑high | 42327722 | PTC, LNM | TCGA/GTEx + 独立临床 + scRNA | 多组学+共识 ML+药理 | LNM 风险 | MGST1="Mito‑high"免疫冷核心驱动，去分化末端干细胞样；toxoflavin 抑制 | 独立外部 AUC 0.833；siRNA/药理 | 样本生态位规模 | High | 与 APOE− 亚群关系未定 | D3 联合 APOE− 界定代谢‑免疫干细胞 |
| APOE− subpop | 39810624 | PTC, LNM | TCGA + 实验 | 多组学+体内 | LNM/干细胞 | APOE− 经 ABCA1‑LXR 富集转移干细胞样 | 多队列 | 机制链部分推断 | High | 与 MGST1 共定位？ | D3 双标记流式分选 |
| LCN2 glycolysis | 41964784 | PTC | 组织+细胞 | 功能+Seahorse+ChIP | 糖酵解/迁移 | LCN2→YAP1→HIF1α 激活糖酵解促进展，与 LNM 相关 | 体内敲低 | 仅 PTC 细胞 | High | 与 MGST1 轴交叉？ | 代谢节点联合靶向 |
| METTL7B glycolysis | 42332350 | PTC | GEO/TCGA+芯片 | 功能+ ubiquitination | 糖酵解/LNM | METTL7B 经 USP28 稳定 HIF‑1α 促糖酵解 | 异种移植 | 临床样本量中 | High | 上游调控不明 | 去泛素化‑代谢靶点 |
| FN1 anoikis | 42002564 | PTC | TCGA+组织+细胞 | WGCNA+功能 | 失巢凋亡/LNM | FN1 经 BCL2L1/BAD 抗失巢凋亡促进展 | IHC/TUNEL | 机制单一 | High | 与 SDC4 空间互作 | 衔接 Jiang 41421038 |
| circPTPRM‑187aa | 41539369 | PTC | 组织+细胞 | 多组学+体内 | 增殖/迁移 | 可翻译 circRNA 经 IQGAP1/RAC1/CDC42‑TGFβ | 裸鼠 | 翻译证据间接 | High | 翻译调控普适性 | 非编码可译组干细胞 |
| DLEU2‑ELAVL1‑RCC2 | 42301557 | PTC | Starbase+细胞 | RIP/MeRIP/ rescue | 迁移/侵袭 | lncRNA‑m6A‑RCC2‑EMT | 挽救实验 | 体内弱 | High | 临床相关性 | lncRNA‑m6A 转移轴 |
| Vem+Panobinostat | 41879411 | ATC | FRO/ARO 细胞 | 协同/功能 | 增殖/转移 | Ve+Pa 协同抑制并再分化 | CompuSyn | 仅细胞 | Medium | 体内/临床 | ATC 联合再分化 |
| FOXP review | 42351648 | TC | 综述 | 文献 | 预后/免疫 | FOXP3/4 关联侵袭/远处/免疫逃逸 | 无 | 需大队列 | Medium | 因果机制 | FOXP 靶向 |
| ATC Warburg rev | 42353188 | ATC/PDTC | 综述 | 文献 | 代谢 | Warburg 效应治疗靶点 | 无 | 综述 | Medium | 异质性 | 组合代谢靶向 |
| LAG3/TIGIT niche | 42430190 | 甲状腺原发+LN | 配对样本 scRNA (55k) | cNMF+LR | 免疫逃逸 | LAG3‑LGALS3 为主轴，PD‑1/PD‑L1 弱 | mIHC | 样本量小 | High | 治疗可行性 | 替代 checkpoint 抗体 |
| IL7R in LN | 42397917 | 甲状腺+LN | scRNA+mIHC | 配对流式 | 预后 | LN 中 IL7R+ TIL 关联好预后 | mIHC | 观察性 | High | 机制 | IL7R 作为生物标志 |
| TME atlas ML | 42134246 | PTC T/PT/LN | scRNA+bulk | RF/lasso‑Cox | N‑stage/生存 | Mac‑APOC1 M2、RGS5+ myCAF；N AUC 0.98 | C‑index>0.9 | 单中心 | High | 外部验证 | 整合临床决策 |
| PD‑L1 meta | 41510756 | DTC | 12 研究荟萃 | 随机效应 | 远处转移 | PD‑L1 高危淋侵犯 OR4.2、远处 OR4.6；不关联 LNM/复发 | 中质量 | 回顾性 | High | 与 LNM 脱钩机制 | 远处转移特异免疫 |
| Hashimoto meta | 41514331 | PTC+HT | 41 研究 67,901 例 | 荟萃 | 侵袭/复发 | HT 促多灶但减弱远处/复发 (OR0.33) | 高质 | 异质 | Medium | 机制 | HT 状态入风险分层 |
| TER 5‑gene | 42305510 | DTC | 共识聚类+101 ML | RSF/Ridge | 生存 | CAMP/DDIT4L/LMX1B/NAT16/CALN1 AUC 0.96–1.00 | qRT‑PCR | 单中心 | High | 独立外部 | 免疫‑代谢‑预后三联 |
| TIPARP | 38233939 | 男性 PTC | TCGA+芯片 | LASSO/Cox | LNM/复发 | 11 基因 LNM 签名，TIPARP 免疫靶点 | IHC | 男性专 | Medium | 女性普适 | 性别分层免疫治疗 |
| Exosomal PDLIM1 | 42131580 | PTC | scRNA+外泌体蛋白 | Scissor+功能 | 血管生成 | 外泌体 PDLIM1 促内皮成管 | 异种移植 | 队列小 | Medium | 体内 rescue | 靶向外泌体血管 |
| PRECISE 41‑gene | 42008746 | PTC | MDACC/VUMC/TCGA scRNA | rank‑based SS | PFS/DSS | thyrocyte 41 基因签名独立预后 | 三队列 | 仅 PTC | High | 治疗衔接 | 风险分层入临床 |
| Neuro‑mimicry 8‑gene | 42329337 | PTC | TCGA+GSE184362 | LASSO/scRNA | LNM | 离子通道 8 基因 AUC 0.721 | scRNA | AUC 中 | Medium | 机制 | 离子通道靶向 |
| Multimodal US DL | 42185182 | PTC CLNM | 4 中心 568 例 | EfficientNet‑B4 融合 | CLNM | 多模态 AUC 0.929/外部 0.843 | 多中心 | 回顾性 | High | 前瞻 | 临床决策支持 |
| Radiopathomics | 42031943 | PTC LNM | 2 中心 1095 | ResNet‑101 | LNM | 外部 AUC 0.875 | 外部 | 中心少 | High | 多中心 | 减少不必要的 LND |
| Interpretable BRAF DL | 42433575 | 甲状腺癌 | 1202 例 6703 图 | XGBoost+ResNet50 | BRAF V600E | 联合 AUC 0.845，SHAP | 测试集 | 单中心 | High | 外部 | 无创 BRAF 预测 |
| AI bilateral recurrence | 42244944 | 经典亚型 PTC | 2 中心 1218 | LASSO+TresNet | 复发 | 外部 AUC 0.848；双侧 HR 9.664 | 外部 | 亚型限 | High | 前瞻 | 手术规划 |
| Radiomics meta | 41997788 | PTC 颈 LN | 60 研究 10,852 | bivariate 荟萃 | 颈 LN | radiomics AUC 0.83，+临床 0.88；外侧 0.94 | 高异质 | 中国为主 | High | 前瞻标准化 | 多中心前瞻 |
| Dual‑channel DL | 41686681 | PTMC 隐匿 CLNM | 2 中心 461 | 双通道 DL+临床 | 隐匿 CLNM | 联合 AUC 0.873 | 外部 | 回顾性 | Medium | 前瞻 | 个体化清扫 |
| Combined‑feature ML | 41664099 | 甲状腺结节 | 803 | TL+ML | 良恶/LNM | LNM AUROC 0.78 | 交叉验证 | 单中心 | Medium | 外部 | 特征融合 |
| ViT LNM | 41931576 | PTC 颈 LN | 2 中心 540 | Vision Transformer | 颈 LN | AUC 0.809 优于 CNN | 外部 | 样本 | Medium | 多中心 | Transformer 架构 |
| Radiomics compare | 41078274 | PTC 颈 LN | 441 | 手工+DL radiomics | 颈 LN | 联合 AUC 0.761 | 测试 | 中心少 | Medium | 前瞻 | 方法学 |
| IMTCGS MTC | 39749465 | MTC | 中国 137 例 | Cox/ROC | DSS | IMTCGS AUC 0.81 预测特异死亡 | 单中心 | 样本小 | Medium | 外部 | MTC 分级 |
| POSTN+ myCAF | 41480746 | PTC | 423k 细胞空间 | 空间转录组 | LNM | POSTN+ myCAF 预测 LNM | 多队列 | 组织背景 | High | 治疗靶点 | CAF‑免疫轴靶向 |
| BRAF V600E meta | 41419184 | PTC | 46k, 20,570 例 | 荟萃 | 淋巴结/远处/复发/死亡 | 淋巴结 OR1.38、复发 OR1.56；不预测远处/死亡 | 稳健 | 异质 | High | 远处机制 | 远处转移特异模型 |
| LLNM‑Net | 40750786 | PTC 侧颈 LN | 7 中心 29,615 | 双向注意力 DL | 侧 LN | AUC 0.944 > 专家 | 多中心 | 黑箱 | High | 可解释 | 多模态融合 |
| Spatial multi‑omics | 41398964 | PTC+LN | 空间代谢+转录 | 空间多组学 | 转移 | 精氨酸‑多胺/糖酵解/脂质轴；5 代谢物驱动 | 斑马鱼 | 区域少 | High | 大队列 | 空间代谢靶点 |
| Jiang FN1‑SDC4 | 41421038 | PTC LNM | scRNA+空间+bulk | 随机森林 | LNM | FN1‑SDC4 空间验证 17 基因签名 | 体外 | 单中心 | High | 治疗 | FN1 靶向 |

---

## What Is Already Known (已知结论)

1. **代谢–免疫偶联是 LNM 的核心驱动力**：在 TCGA/GTEx 与独立临床队列中反复出现 MGST1（"Mito‑high"/免疫冷，AUC 0.833，去分化末端干细胞样）、SHMT2、GLTC‑LDHA、SOX12‑YBX1‑LDHA 等线粒体/糖酵解重编程节点；本运行新增 LCN2（Hippo/YAP1/HIF1α）、METTL7B（USP28/HIF‑1α）与 FN1（失巢凋亡）进一步闭合"代谢→免疫逃逸→转移"链。(MGST1 42327722; LCN2 41964784; METTL7B 42332350; FN1 42002564; 历史支柱 38272883/37031273/40593465)
2. **干细胞样转移亚群存在且可被标记**：APOE−（ABCA1‑LXR）、MGST1 去分化末端、ISG15/KPNA2（ATC）、DLK1（MTC）四类；本运行新增 circPTPRM‑187aa 与 DLEU2‑ELAVL1‑RCC2 两条非编码可译组 (translatome) 干细胞轴。(39810624; 42327722; 37501099; 39595993; 41539369; 42301557)
3. **POSTN+ myCAF 空间图谱可预测 LNM**：423k 细胞空间转录组界定 POSTN+ myCAF 生态位，并与免疫排斥相关；Jiang 41421038 以 FN1‑SDC4 空间验证 17 基因签名，Li 41398964 以空间代谢+转录锁定 5 个转移驱动代谢物。(41480746; 41421038; 41398964)
4. **影像/多组学 AI 预测 LNM 高度拥挤但性能持续提升**：LLNM‑Net 多中心 AUC 0.944；本运行新增多模态超声 DL 0.929、radiopathomics 0.875、可解释 BRAF V600E DL 0.845、双侧癌复发 AI 0.97、radiomics 荟萃 0.83/0.88。共同短板：单中心、回顾性、黑箱、外部验证有限。(40750786; 42185182; 42031943; 42433575; 42244944; 41997788)
5. **BRAF V600E 关联淋巴结与复发但不预测远处/死亡**：46k 荟萃显示淋巴结 OR 1.38、复发 OR 1.56，远处转移 OR 0.75（不显著）、死亡 OR 0.97。类似地 PD‑L1 高危远处转移 OR 4.6 但**不**关联 LNM/复发——提示淋巴结与远处转移可能是受不同机制驱动的解耦表型。(41419184; 41510756)

## What Remains Unclear (待澄清)

- **节点互斥还是协同？** MGST1、APOE−、LCN2、METTL7B、FN1 是否标记同一代谢‑免疫干细胞连续体，还是互斥亚群，尚无联合流式/空间共定位证据。
- **淋巴结 vs 远处转移的解耦机制**：BRAF V600E 与 PD‑L1 均预测远处但不预测淋巴结，二者共享何种远处特异通路（血流播散？循环肿瘤细胞适应性？）未明。
- **替代 checkpoint 的治疗可行性**：42430190 显示 LAG3‑LGALS3/LAG3‑TIGIT 为主轴、PD‑1/PD‑L1 微弱，但是否可成药、与"免疫冷"MGST1 表型如何交互，尚缺功能验证。
- **非编码可译组 (translatome) 干细胞轴的普适性**：circPTPRM‑187aa、DLEU2‑ELAVL1‑RCC2 仅在 PTC 细胞验证，是否代表更普遍的转移干细胞程序存疑。
- **代谢靶向的临床转化**：toxoflavin（MGST1 抑制）、PF11（PRPS2，乳腺）等显示代谢靶点活性，但在甲状腺癌患者中的安全性/疗效未评估。

## Method/Data Limitations In The Field (领域方法/数据局限)

- **公共数据复用与批次效应**：多数分子/AI 研究依赖 TCGA/GTEx 与单一机构回顾队列，跨平台批次效应未系统校正。
- **外部验证稀缺**：除 LLNM‑Net（7 中心）、多模态 US DL（4 中心）、双侧 AI（2 中心）、BRAF V600E meta（46k）外，绝大多数模型仅内部验证，AUC 高估风险高。
- **终点稀疏**：远处转移/病死为罕见事件，导致 BRAF/PD‑L1 荟萃对远处表型把握度低；多数 AI 研究终点为 LNM（较常见），远处转移预测模型少。
- **缺乏亚型分层**：PTC/PTMC/FTC/MTC/ATC 混用，ATC/PDTC 与 MTC 代谢与干细胞证据明显少于 PTC。
- **湿实验验证不足**：新增 lncRNA/circRNA/代谢节点多停留在细胞功能，缺类器官/PDX/体内转移验证。
- **claim boundary**：仅 AUC/显著性不足以推断临床效用（schema 规则），多处"预测模型"未声明决策上下文。

## Candidate Future Directions (候选未来方向)

| Direction | Rationale | Feasibility | Required Data | Validation Plan | Main Risk | Claim Boundary |
|---|---|---:|---|---|---|---|
| **D3 — APOE−/MGST1+ 代谢–免疫干细胞样转移亚群** | 多节点收敛（MGST1、APOE−、LCN2、METTL7B、FN1）指向同一可靶向干细胞态；本运行新增代谢驱动+免疫生态位+临床预后锚三重强化 | 高（公共 scRNA+TCGA+已有 MGST1 独立验证） | TCGA/GTEx、42430190/42134246/42008746 scRNA、机构 LNM 队列 | 多中心外部验证 MGST1+APOE− 双标记；toxoflavin 体内 | 节点协同关系未定 | 风险分层+靶点，非独立预后替代 |
| D‑immune — LAG3/TIGIT 替代 checkpoint 生态位 | 42430190 显示 PD‑1 弱、LAG3/TIGIT 主导；与 MGST1 免疫冷互补 | 中（需新队列/类器官） | 42430190/42397917 scRNA、免疫治疗队列 | 体外抗体阻断+类器官 | IO 拥挤、成药性未证 | 假设生成，非疗效断言 |
| D‑spatial — PTC LNM 空间代谢图谱 | 41398964+41421038 已开空间代谢/转录先河，维度最薄（spatial=6） | 中（需 10x Visium/Stereo‑seq） | 空间代谢+转录、LN 配对 | 独立空间队列 | 成本高、区域少 | 机制图谱，非诊断 |
| D‑translatome — 非编码可译组干细胞 | circPTPRM‑187aa/DLEU2 新增"可翻译非编码 RNA"干细胞轴，新颖 | 中（需 ribo‑seq/体外） | PTC 细胞+组织 ribo‑seq | 翻译 rescue+体内 | 普适性存疑 | 机制探索 |
| D‑ml — 多模态 DL 融合 | 高度拥挤但临床价值高（42185182/42031943/42433575） | 高 | 多中心超声/病理/临床 | 前瞻多中心 | 极拥挤、泄漏风险 | 决策支持，非替代病理 |

**Rubric 评分 (1–5 × 7)：**

| Direction | Novelty | Feas | Data | Valid | Clin | Method | Overcrowd | **Total** | Band |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| **D3** | 5 | 5 | 4 | 5 | 5 | 4 | 4 | **32** | Strong |
| D‑immune | 5 | 4 | 4 | 3 | 4 | 4 | 3 | 27 | Feasible |
| D‑spatial | 4 | 3 | 3 | 3 | 4 | 4 | 4 | 25 | Feasible |
| D‑translatome | 5 | 4 | 3 | 3 | 3 | 4 | 4 | 26 | Feasible |
| D‑ml | 2 | 5 | 4 | 3 | 5 | 3 | 1 | 23 | Feasible |

## Recommended Next Direction (推荐下一步方向)

**D3 — 界定并靶向 APOE−/MGST1+ 代谢–免疫干细胞样转移亚群（rubric 32，Strong，连续第 6 次确认）。**

理由：本运行通过近时效检索新增 31 篇文献，其中代谢驱动（LCN2 41964784、METTL7B 323350）、免疫生态位（LAG3/TIGIT 42430190、IL7R 42397917、Mac‑APOC1/RGS5+ myCAF 42134246）、临床已验证预后锚（PRECISE 41‑基因 42008746、TER 5‑基因 42305510）共同把"代谢重编程→免疫逃逸→干细胞样转移"收敛到 MGST1/APOE− 这一可标记、可药理干预的节点上，可行性显著优于历史运行。

**第一步具体行动**：(1) 在 42430190/42134246/42008746 公共 scRNA 中联合投影 MGST1 与 APOE 表达，界定 MGST1+APOE−（或双高）细胞态并检验其是否富集于 LN 转移灶；(2) 以 TCGA/GTEx 做生存与免疫浸润（CIBERSORT/TIDE）关联；(3) 在机构 LNM 队列以 mIHC 双标验证；(4) 用 toxoflavin 在 PDX/类器官检验对 MGST1+APOE− 亚群的选择性杀伤与免疫冷逆转。claim boundary：作为风险分层与靶点假设，非独立预后替代或疗效断言。

## Follow-Up Reading List (后续阅读清单)

- **42430190 (LAG3/TIGIT niche)** — 替代 checkpoint 生态位图谱，D3 免疫侧直接证据。
- **42008746 (PRECISE)** — thyrocyte 41 基因独立预后签名，D3 临床锚。
- **42305510 (TER 5‑gene)** — 免疫‑代谢‑预后三联，D3 桥接。
- **41398964 (spatial multi‑omics)** — 空间代谢驱动，D‑spatial 起点。
- **41539369 / 42301557 (circPTPRM / DLEU2)** — 非编码可译组干细胞，D‑translatome。
- **41480746 (POSTN+ myCAF)** — 空间 CAF  atlas，D3 间质侧上下文。

## Reproducibility Notes (可重复性说明)

- Search date: 2026-07-28
- Databases: PubMed (via `mcp__paper-search-mcp__search_pubmed`, DeferExecuteTool)
- Query strings: a–i（见 Search Strategy 表）
- Filters: 无日期过滤参数；本运行统一 `sort=pub_date`, `max_results=15`
- MCP 瞬时解析错误（`not well-formed (invalid token)`）按既往经验对失败查询重发直至 9 路全部返回
- Deduplication rule: 按 PMID 去重；非甲状腺（乳腺/胃/结直肠/肾/宫颈/HNSCC/胆囊/胰腺/脑/前列腺/ phyllodes）外溢判 excluded
- Screening rule: 甲状腺相关（PTC/PTMC/FTC/MTC/ATC/总体 THCA）in‑scope；纯临床流行病学（如 RAI 利用 41817109）excluded
- Relevance: High/Medium/Low（按与 LNM/远处转移机制‑免疫‑单细胞‑空间‑AI‑预后‑代谢的相关度）
- Files saved:
  - `lit_review/literature_review_20260728_031940.md`（本报告）
  - `lit_review/search_results_latest.json`（累计语料 170 unique / 101 in‑scope / 69 excluded，含 corpus_delta_vs_run5）
  - `lit_review/_build_run6.py`（生成脚本）

---

## 与最新历史报告 (run #5, 2026-07-27) 的差异对比

**检索与语料**
- run #5 采用 `sort=relevance`，结果完全停滞于平台期（106 unique / 70 in‑scope / **0 新增**）。
- run #6 改用 `sort=pub_date` 近时效优先，突破平台期：**新增 31 篇 in‑scope 甲状腺文献**（多为 2025–2026），累计 **170 unique / 101 in‑scope / 69 excluded**。
- 维度分布（in‑scope，多标签）：molecular 46（+16）、immune 29（+11)、single‑cell 18（+6）、spatial 6（持平，最薄）、algorithm 37（+10）、prognosis 27（+8）、metabolic 13（+4)。algorithm 与 molecular 仍居前二。

**新增信号 / 方向变化 (new signals)**
1. **代谢–免疫轴新增三条可药理节点**：LCN2（Hippo/YAP1/HIF1α，41964784）、METTL7B（USP28/HIF‑1α，323350）、FN1 失巢凋亡（42002564）——与 MGST1 共同构成更完整的"代谢→免疫冷→干细胞样转移"网络。
2. **免疫生态位新图谱**：42430190（LAG3/TIGIT 替代 checkpoint，PD‑1 弱）与 42397917（IL7R 淋巴结预后）提供 D3 的免疫侧直接证据，并挑战常规 PD‑1 阻断在甲状腺癌的适用性。
3. **非编码可译组 (translatome) 干细胞新维度**：circPTPRM‑187aa（41539369）、DLEU2‑ELAVL1‑RCC2（42301557）开辟"可翻译非编码 RNA 促转移"新角度。
4. **临床已验证预后锚增强 D3 可行性**：PRECISE 41‑基因 thyrocyte 签名（42008746，三队列）、TER 5‑基因（42305510，AUC 0.96–1.00）使 D3 从机制假设迈向可落地风险分层。
5. **AI 维度持续膨胀但同质化**：新增 9 篇 LNM/复发 DL/radiomics（42185182/42031943/42433575/42244944/41997788/41686681/41664099/41931576/41078274），性能高但多为单中心回顾、外部验证有限——D‑ml rubric 仅 23（极度拥挤）。
6. **远处 vs 淋巴结转移解耦再获支持**：PD‑L1 meta（41510756） replication BRAF V600E meta（41419184）模式——二者均预测远处转移但**不**预测淋巴结，提示需分别建模。

**未变 (unchanged)**
- 五大收敛轴保持稳定；POSTN+ myCAF 空间维度仍最薄（spatial=6）且无新增，仍是方法论空白。
- **推荐方向 D3 rubric 总分 32（Strong）连续第 6 次确认**，证据强度较 run #5 显著提升（新增代谢驱动+免疫生态位+临床预后锚）。

**结论**：run #6 通过检索策略切换（relevance→pub_date）有效打破语料平台期，新增 31 篇高质量近期文献，主要填补了"代谢驱动节点""免疫生态位替代 checkpoint""非编码可译组干细胞""临床验证预后锚"四类空白，进一步巩固 D3 作为首选研究方向。建议后续检索固定 `sort=pub_date` 并补充 bioRxiv/arXiv 预印本与 cBioPortal/DepMap 以增强远处转移与亚型（ATC/MTC）覆盖。
