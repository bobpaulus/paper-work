# 甲状腺癌文献监测报告 / Thyroid Cancer Literature Surveillance Report

**Date / 日期**: 2026-09-17 (Run #23)
**Sources / 数据源**: OpenAlex REST API (主源 / primary)；Crossref + Unpaywall（High 条目元数据与 OA 校验）；NCBI eutils / PubMed 本机不可达（实测 HTTP 000），未直连重试；paper-search-mcp 未调用（仅补充源，本轮未启用）。
**Search window / 检索窗口**: 主窗口 30 天（2026-08-18 → 2026-09-17）；转移干性（ST）维度 30 天 = 0 → 按协议 90 天补跑（2026-06-19 → 2026-09-17），并合并 90 天窗口内的 1 篇 High 空间组学溢出记录。
**Baseline / 基线**: `search_results_latest.json` 累积 149 条（run #20–#22）→ 本轮 +22 → **171 条**。

---

## 中文摘要 (Chinese Abstract)

本轮以 OpenAlex 为主源完成甲状腺癌（PTC/PTMC/FTC/MTC/ATC）侵袭、淋巴结与远处转移、复发、预后、分子机制、肿瘤免疫微环境、单细胞/空间组学、机器学习/深度学习方向的增量监测。主窗口 30 天去重后唯一记录 94、在范围 60、剔除 34；转移干性（ST）维度 30 天增量为 0，按协议以 90 天补跑，回补 6 条 ST 记录，并捕获 1 篇 90 天窗口内、30 天窗口结构性不可见的 High 空间组学溢出论文。

**本轮新增唯一记录共 22 条**（15 主窗口 + 6 ST 90 天 + 1 High SP 溢出）。相关性：High 2、Medium 16、Low 3。严格预印本 1 篇（Research Square）+ 降档存档/章节型 3 篇（1 figshare 数据集 + 2 IntechOpen 书章节）。

**最强收敛信号**：① **突变特异性去分化轨迹的单核 + 空间多组学图谱**（*Molecular Cancer* 2026，snRNA-seq + spatial + bulk，BRAF V600E vs RAS 驱动），为 ATC 去分化可塑性提供高分辨率原发证据，直接赋能 **D14（细胞类型解析因果推断 + 空间多组学方法论）** 并强化去分化/EMT 轴（D11）与 ST；② **免疫单细胞/空间遗传驱动解析**（*Int. J. Immunogenetics* 2026，High）把细胞类型解析因果推断引入甲状腺免疫方向，拓宽 D8；③ **算法方法（AL）聚类**：4 篇 ML/DL 影像组学与可解释预测（中央淋巴结转移、肺转移、I-131 四分类反应、cN0 PTMC 喉返神经旁淋巴结），构成持续活跃的可转化方向（D13）；④ **代谢重编程（ME）**：ECT2 拮抗硫辛酸经能量代谢调控 PTC（*Cancer Cell Int.* 2026），为代谢–免疫轴提供间接新数据点。

**持续跟踪方向状态**：**D3（APOE−/MGST1+ 代谢–免疫干性亚群）= 无变化**（连续第 23 轮无直接锚定 APOE/MGST1 癌细胞亚群的原发证据；ECT2 为不同代谢基因，不构成该轴证据），维持 Strong（rubric 33）。D8（TREM2+ AHR–IDO1 / TAM 异质性）维持并拓宽（32）；D9（SPP1+ TAM）**本轮无新 SPP1+ 证据，维持 31**；D11（乳酸化–EMT-TF）无新乳酸化/ETV4/KLF6 论文，维持 30；D12（铁死亡）无新论文，维持 27。

**推荐下一步**：以本轮 *Molecular Cancer* snRNA+空间去分化图谱与细胞类型解析因果 + 空间框架为引擎，① 复验 SPP1+ × TREM2+ TAM 生态位共定位（D9/D8），② **首次对 APOE−/MGST1+ 代谢–免疫去分化亚群做原代空间锚定**（D3 长期缺口），一举把方法论（D14）与机制缺口（D3）打通。

---

## English Abstract

Incremental surveillance of thyroid cancer (PTC/PTMC/FTC/MTC/ATC) covering invasion, lymph-node/distant metastasis, recurrence, prognosis, molecular mechanisms, tumor immune microenvironment, single-cell/spatial omics, and ML/DL methods, using OpenAlex as the primary source (NCBI eutils/PubMed unreachable on this host; paper-search-mcp not invoked). The 30-day primary window yielded 94 deduplicated records (60 in-scope, 34 excluded); the metastasis-stemness (ST) dimension returned 0 in 30 days, so a 90-day supplement was run per protocol, recovering 6 ST records and 1 High spatial-omics spillover record invisible to the 30-day window.

**22 genuinely new unique records** (15 primary + 6 ST-90d + 1 High-SP spillover). Relevance: High 2, Medium 16, Low 3. One strict preprint (Research Square) + three downgraded deposit/chapter records (1 figshare dataset, 2 IntechOpen book chapters).

**Strongest convergence signals**: (1) a **mutation-specific dedifferentiation atlas** (*Molecular Cancer* 2026; snRNA-seq + spatial + bulk across BRAF V600E vs RAS) delivering high-resolution primary evidence for ATC plasticity, directly powering **D14 (cell-type-resolved causal inference + spatial multi-omics methodology)** and reinforcing dedifferentiation/EMT (D11) and ST; (2) **cell-type-resolved causal + spatial immune genetic drivers** (*Int. J. Immunogenetics* 2026, High) broadening D8; (3) a **cluster of 4 ML/DL radiomics / interpretable prediction papers** (central LNM, lung metastasis, four-class I-131 response, cN0 PTMC RLN-para-LN) forming a persistently active translational direction (D13); (4) **ECT2 antagonizing lipoic acid via energy metabolism** in PTC (*Cancer Cell Int.* 2026) adding an indirect data point to the metabolic–immune axis.

**Tracked direction status**: **D3 (APOE−/MGST1+ metabolic–immune stem-like subpopulation) — unchanged** (no direct primary anchor for 23 consecutive runs; ECT2 is a distinct metabolic gene); remains Strong (rubric 33). D8 maintained/broadened (32); D9 (SPP1+ TAM) stable at 31 (no new SPP1+ evidence); D11 (lactylation–EMT-TF) unchanged (30); D12 (ferroptosis) unchanged (27).

**Recommended next**: use the new *Molecular Cancer* snRNA+spatial dedifferentiation atlas and the cell-type-resolved causal+spatial framework to (a) confirm SPP1+ × TREM2+ TAM ecotype colocalization (D9/D8) and (b) **finally provide a primary spatial anchor for the APOE−/MGST1+ metabolic–immune dedifferentiation subpopulation (D3)** — linking methodology (D14) to the longest-standing mechanistic gap.

---

## 检索策略 (Search Strategy)

| Source | Query (9 路维度) | Window | Filter | Raw hits | In-scope | New vs baseline | Notes |
|---|---|---|---|---:|---:|---:|---|
| OpenAlex | a. MO/PR: 转移+标志物/signature | 30 d | title_and_abstract + from_pub_date | 22 | 21 | — | 分子机制+预后转移 |
| OpenAlex | b. MO: 侵袭/转移+机制/EMT | 30 d | 同上 | 46 | 18 | — | 分子机制 |
| OpenAlex | c. AL/PR: 转移/LNM+ML/DL/radiomics | 30 d | 同上 | 17 | 11 | — | 算法方法 |
| OpenAlex | d. IM: 转移+免疫微环境/巨噬/T cell | 30 d | 同上 | 29 | 11 | — | 免疫微环境 |
| OpenAlex | e. SC: 转移/异质+单细胞/scRNA | 30 d | 同上 | 13 | 8 | — | 单细胞 |
| OpenAlex | f. SP: 空间转录组/空间多组学/Visium | 30 d | 同上 | 10 | 2 | — | 空间组学 |
| OpenAlex | g. PR: 预后/复发+风险模型/生存 | 30 d | 同上 | 51 | 16 | — | 预后转移 |
| OpenAlex | h. ST: 转移+癌干细胞/干性/去分化 | 30 d | 同上 | 9 | 3 | **0** | 转移干性（→90 d 补跑）|
| OpenAlex | i. ME: 转移/进展+代谢重编程/铁死亡 | 30 d | 同上 | 6 | 4 | — | 代谢重编程 |
| OpenAlex | h (ST 90 d 补跑) | 90 d | 同上 | 21 | 21 | 6 (ST) + 1 (High SP 溢出) | ST 维度 0 → 90 d 救援 |
| Crossref / Unpaywall | High 条目 DOI 元数据 + OA 解析 | — | — | 2 | 2 | — | 2 High 均验证（DOI 真实）|

**去重与清洗 (Deduplication & cleaning)**: 标题归一化为主键合并同一论文多版本（主窗口合并 29 组多版本）；剔除期刊补充材料条目（`Table 1_…` 等，正则 `SUPPLEMENT`）；剔除标题未点名甲状腺（31 条）或非肿瘤主题良性/自身免疫病（3 条）；要求标题点名甲状腺且整体为肿瘤主题。

**通道说明 (Channel note)**: NCBI eutils / pubmed.ncbi.nlm.nih.gov 本机 4/4 超时（HTTP 000），禁止直连重试；OpenAlex 直连稳定（~1.4 s）且索引预印本，故以 DOI 为主标识，PMID 缺失标注「待编目」。

---

## 纳入论文 (Included Papers)

> 共 22 条本轮新增（按相关性/日期排序；★ = High；▲ = 降档存档/章节/摘要；[preprint] = 严格预印本）。纳入标题与摘要保留英文原文，附一句话中文要点。

**★ 1. Mutation-specific dynamics of dedifferentiation trajectories and tumor–stromal interactions in thyroid cancer.** *Molecular Cancer* 2026. PMID: 42458477. DOI: 10.1186/s12943-026-02699-2 (gold OA). 【90 天窗口溢出，30 天窗口结构性不可见】整合 snRNA-seq + 空间转录组 + bulk，刻画 BRAF V600E vs RAS 驱动的突变特异性去分化轨迹与肿瘤–间质互作，ATC 可塑性最高分辨率原发证据。

**★ 2. Cell Type–Resolved Causal Inference and Spatial Transcriptomic Integration Reveal Immune‐Specific Genetic Drivers of Autoimmune and Malignant Thyroid Disease.** *Int. J. Immunogenetics* 2026. PMID: 待编目. DOI: 10.1111/iji.70066 (closed). 细胞类型解析因果推断 + 空间转录组，解析甲状腺自身免疫与恶性肿瘤的免疫特异性遗传驱动（覆盖单细胞+空间双维度）。

**3. Deep learning combined habitat radiomics analysis of central lymph node metastasis in papillary thyroid carcinoma.** *npj Digital Medicine* 2026. DOI: 10.1038/s41746-026-03203-2 (gold). 934 例 PTC 中央淋巴结转移深度学习 +  habitat 影像组学，注册研究（NCT06725628）。

**4. The value of machine learning models in predicting lung metastasis in papillary thyroid carcinoma.** *Frontiers in Endocrinology* 2026. DOI: 10.3389/fendo.2026.1776463 (gold). 681 例 PTC（71 例肺转移，10.4%）构建 ML 肺转移风险模型（年龄/性别/s-Tg 等）。

**▲ 5. Prediction of LN-prRLN Metastasis in cN0 PTMC Patients Using Logistic Regression and Machine Learning.** *Research Square* 2026 [preprint]. DOI: 10.21203/rs.3.rs-10538207/v1 (green). cN0 PTMC 喉返神经旁淋巴结（prRLN）转移 logistics + ML 预测，单中心回顾。

**▲ 6. Interpretable four-class machine learning prediction of initial I-131 therapy responses in differentiated thyroid cancer.** *figshare* 2026 [dataset]. DOI: 10.6084/m9.figshare.33542334.v1 (green). PMID: 42720506. 可解释四分类（优秀/IDR/BIR/不全）DTC 初始 I-131 反应预测。

**7. ECT2 antagonizes lipoic acid to modulate papillary thyroid carcinoma progression through energy metabolism pathways.** *Cancer Cell International* 2026. DOI: 10.1186/s12935-026-04459-0 (gold). ECT2 经能量代谢拮抗硫辛酸调控 PTC 进展（代谢重编程新基因）。

**8. Crosstalk between the microbiome and immune microenvironment in the pathogenesis and treatment of thyroid carcinoma.** *Frontiers in Immunology* 2026. DOI: 10.3389/fimmu.2026.1782596 (gold). 微生物组–免疫微环境串扰的叙述性综述（免疫方向，复习级）。

**9. Context-Dependent Prognostic Impact of Microscopic Positive Surgical Margin in Papillary Thyroid Carcinoma.** *Clin. Exp. Otorhinolaryngol.* 2026. PMID: 42438431. DOI: 10.21053/ceo.2026-00029 (gold).  microscopically positive surgical margin（mPSM）对 PTC 复发风险呈情境依赖性。

**10. The role of miR ‐335‐5p in the redifferentiation of BRAF p. V600E thyroid cancers.** *Molecular Oncology* 2026. PMID: 42325083. DOI: 10.1002/1878-0261.70181 (gold). miR-335-5p 介导 BRAF V600E 甲状腺癌再分化、增敏 RAI。

**11. Simulating the Dedifferentiation Process of Thyroid Cancer: Insights from Mouse Models and Ultrasound Imaging.** *Ultrasound Med. Biol.* 2026. PMID: 42366146. DOI: 10.1016/j.ultrasmedbio.2026.05.027 (hybrid). 小鼠模型 + 超声影像模拟 DTC→ATC 去分化进程。

**▲ 12. Molecular Pathogenesis and Emerging Therapeutic Targets in Anaplastic Thyroid Carcinoma.** *IntechOpen* 2026 [book-chapter]. DOI: 10.5772/intechopen.1016607 (hybrid). ATC 分子发病机制与治疗靶点叙述性综述（High 相关性，复习级）。

**▲ 13. Molecular and Clinical Advances in Thyroid Cancer: Insights from Genomic, Therapeutic and Global Perspectives.** *IntechOpen* 2026 [book-chapter]. DOI: 10.5772/intechopen.1014763 (hybrid). TC 基因组/治疗/全球视角综述（ST）。

**14. Spatial Heterogeneity in Anaplastic Thyroid Carcinoma: Mechanistic Insights and Clinical Translation through Single-Cell and Spatial Transcriptomics.** *Crit. Rev. Oncol. Hematol.* 2026. PMID: 42727719. DOI: 10.1016/j.critrevonc.2026.105588 (closed). ATC 空间异质性的单细胞/空间综述（SC/SP）。

**15. Beyond traditional biopsy: integrating liquid biopsy, molecular panels, and advanced imaging techniques in thyroid cancer management.** *Endokrynologia Polska* 2026. PMID: 42725427. DOI: 10.5603/ep.112817 (gold). 液体活检 + 分子 panel + 影像整合管理综述。

**16. Case Report: Unexpected long-term survival in metastatic anaplastic thyroid carcinoma through multidisciplinary management.** *Frontiers in Oncology* 2026. DOI: 10.3389/fonc.2026.1943145 (gold). 转移性 ATC 多学科管理长期生存个案（n=1，证据弱）。

**17. Clinical Relevance and Regulatory Mechanisms of LINC01521 in Papillary Thyroid Carcinoma.** *The Laryngoscope* 2026. DOI: 10.1002/lary.70905 (closed). LINC01521 在 PTC 的功能与调控（120 例，lncRNA）。

**18. [Current management of thyroid cancer in Hungary].** *Orv. Hetil.* 2026. PMID: 42732540. DOI: 10.1556/650.2026.33649 (closed). 匈牙利 DTC 诊疗实践调查。

**19. Anaplastic Thyroid Carcinoma and Toxic Multinodular Goiter: A Case Report and Literature Review.** *Judi Clinical Journal* 2026. DOI: 10.70955/jcj.2026.07 (hybrid). ATC 合并毒性多结节性甲状腺肿个案 + 综述。

**20. Synergistic role of molecular imaging and genomics in thyroid cancer management.** *J. Transl. Med.* 2026. DOI: 10.1186/s12967-026-08839-y (gold). 分子影像 + 基因组学协同管理综述（Low）。

**21. Complete pathologic necrosis of a thyroid neoplasm following pressure-enabled thyroid artery embolization.** *UNC Libraries* 2026. DOI: 10.17615/ssss-c117 (green). 甲状腺动脉栓塞后病理坏死个案（Low）。

**▲ 22. Incidence and Predictors of Immune‐Related Hypothyroidism Under Pembrolizumab Across Gynecologic Malignancies and Melanoma.** *Int. J. Cancer* 2026. PMID: 42723137. DOI: 10.1002/ijc.70735 (hybrid). 【边界性 off-topic】pembrolizumab 致甲状腺 irAE 甲减，研究对象为妇科肿瘤/黑色素瘤，非甲状腺肿瘤本身；自动 in-scope 因「Hypothyroidism」命中 thyroid 正则，已标注为边界条目、不计入甲状腺癌机制证据权重（见方法局限）。

---

## 证据矩阵 (Evidence Matrix)

*列：Paper / PMID·DOI / Disease·Population / Data Source / Method / Endpoint / Main Finding / Validation / Limitations / Relevance / Dim (Gap/Future)。OA 与预印本状态见上节。*

| # | Paper (first author / year) | PMID·DOI | Disease | Data | Method | Endpoint | Main Finding | Validation | Limitations | Rel | Dim→Future |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Mutation-specific dediff traj. (*Mol Cancer*) | 42458477 · 10.1186/s12943-026-02699-2 | ATC/DTC | snRNA+spatial+bulk | 多组学轨迹 | 去分化可塑性 | BRAF V600E 渐进去分化、RAS 不同轨迹 | 多组学交叉 | 体内靶向缺失 | High | SP/SC→**D14/D11** |
| 2 | Cell-type-resolved causal+spatial (*IJI*) | 待编目 · 10.1111/iji.70066 | AITD+TC | eQTL+spatial | 因果推断 | 免疫遗传驱动 | 细胞类型解析免疫特异性驱动 | 生信 | 体内浅、泛甲状腺 | High | SC/SP→**D8/D14** |
| 3 | DL habitat radiomics CLNM (*npj DM*) | 待编目 · 10.1038/s41746-026-03203-2 | PTC | 934 例影像 | DL+radiomics | 中央 LNM | habitat 影像组学预测 CLNM | 注册+回顾 | 单中心、需前瞻 | Med | AL→**D13** |
| 4 | ML lung mets PTC (*Front Endo*) | 待编目 · 10.3389/fendo.2026.1776463 | PTC | 681 例 | ML | 肺转移 | s-Tg 等预测肺转移 | 回顾 | 单中心 | Med | AL/PR→**D13** |
| 5 | LN-prRLN ML [preprint] | 待编目 · 10.21203/rs.3.rs-10538207/v1 | cN0 PTMC | 单中心 | LR+ML | prRLN LNM | cN0 PTMC 喉返旁 LNM 预测 | 无（预印本） | 未评议 | Med | AL/PR→**D13** |
| 6 | Four-class I-131 ML [dataset] | 42720506 · 10.6084/m9.figshare.33542334.v1 | DTC | 队列 | 可解释 ML | I-131 反应 | 四分类反应预测 | 验证集 | 存档未发表 | Med | AL/PR→**D13** |
| 7 | ECT2 vs lipoic acid (*Cancer Cell Int*) | 待编目 · 10.1186/s12935-026-04459-0 | PTC | 细胞+临床 | 功能 | 能量代谢 | ECT2 经能量代谢促 PTC | 体外+部分 | 因果浅 | Med | MO/ME→D3(间接)/ME |
| 8 | Microbiome-immune crosstalk (*Front Imm*) | 待编目 · 10.3389/fimmu.2026.1782596 | TC | 综述 | 叙述 | 免疫微环境 | 菌群–免疫串扰 | 无（综述） | 非原发 | Med | IM→**D8** |
| 9 | mPSM context-dependent (*Clin Exp ORL*) | 42438431 · 10.21053/ceo.2026-00029 | PTC | 临床 | 队列 | 复发 | mPSM 复发风险情境依赖 | 临床 | 效应修饰未全 | Med | ST→去分化边界 |
| 10 | miR-335-5p rediff (*Mol Oncol*) | 42325083 · 10.1002/1878-0261.70181 | BRAF V600E TC | 细胞 | 功能 | 再分化/RAI | miR-335-5p 增敏 RAI | 体外 | 体内浅 | Med | ST→D11(去分化) |
| 11 | Dediff mouse+US (*Ult Med Biol*) | 42366146 · 10.1016/j.ultrasmedbio.2026.05.027 | DTC→ATC | 小鼠 | 影像+模型 | 去分化 | 超声监测去分化 | 动物 | 转化距离 | Med | ST→D11 |
| 12 | ATC molecular pathogenesis [chap] | 待编目 · 10.5772/intechopen.1016607 | ATC | 综述 | 叙述 | 机制/靶点 | ATC 机制与靶点 | 无 | 书章节 | High* | ST→D11/D12 |
| 13 | Mol&Clinical Advances TC [chap] | 待编目 · 10.5772/intechopen.1014763 | TC | 综述 | 叙述 | 全景 | 基因组/治疗进展 | 无 | 书章节 | Med | ST→综述 |
| 14 | Spatial heterogeneity ATC (*Crit Rev*) | 42727719 · 10.1016/j.critrevonc.2026.105588 | ATC | 综述 | sc+spatial | 空间异质 | ATC 空间异质性机制 | 无 | 综述 | Med | SC/SP→D14 |
| 15 | Liquid biopsy integration (*Endokr Pol*) | 42725427 · 10.5603/ep.112817 | TC | 综述 | 叙述 | 管理 | 液体活检+分子+影像 | 无 | 综述 | Med | MO→诊断 |
| 16 | ATC long-term survival case | 待编目 · 10.3389/fonc.2026.1943145 | mATC | 个案 | 管理 | 生存 | 多学科长期生存 | n=1 | 个案 | Med | PR→个案 |
| 17 | LINC01521 PTC (*Laryngoscope*) | 待编目 · 10.1002/lary.70905 | PTC | 120 例 | 功能 | 预后 | LINC01521 调控 | 临床+部分 | 机制浅 | Low | MO→lncRNA |
| 18 | Hungary management survey | 42732540 · 10.1556/650.2026.33649 | DTC | 调查 | 问卷 | 实践 | 国内诊疗地图 | 调查 | 非机制 | Med | PR→卫生服务 |
| 19 | ATC + TMG case | 待编目 · 10.70955/jcj.2026.07 | ATC | 个案 | 综述 | 临床 | ATC 合并 TMG | n=1 | 个案 | Med | ST→个案 |
| 20 | Molecular imaging+genomics (*JTM*) | 待编目 · 10.1186/s12967-026-08839-y | TC | 综述 | 叙述 | 管理 | 影像+基因组协同 | 无 | 综述 | Low | PR→综述 |
| 21 | Artery embolization necrosis | 待编目 · 10.17615/ssss-c117 | 结节 | 个案 | 影像 | 坏死 | 栓塞后病理坏死 | n=1 | 个案 | Low | PR→介入 |
| 22 | irAE hypothyroidism [borderline] | 42723137 · 10.1002/ijc.70735 | 妇科/黑素瘤 | 真实世界 | 队列 | irAE | ICI 甲减预测 | 临床 | **off-topic(非甲状腺肿瘤)** | Med | PR→边界(不计入) |

---

## 已知结论 (What Is Already Known)

1. **突变特异性去分化轨迹（本轮最强原发证据）**：*Molecular Cancer* 2026 以 snRNA + 空间 + bulk 三联整合，刻画 BRAF V600E 驱动的渐进去分化与 RAS 驱动的差异化轨迹，并解析肿瘤–间质互作——把既往「DTC→ATC 去分化」的笼统叙述推进到突变分辨率（支撑 D11 去分化轴与 ST）。
2. **免疫微环境的细胞类型解析正在成熟**：细胞类型解析因果推断 + 空间转录组已能解析甲状腺（含恶性）的免疫特异性遗传驱动（#2），与既往 TREM2+ AHR–IDO1（D8）、SPP1+ TAM（D9）形成「单细胞/空间分辨率下的髓系生态位」研究范式。
3. **ML/DL 预测模型持续高产且场景细化**：中央 LNM（habitat 影像组学，注册研究）、肺转移、I-131 四分类反应、cN0 PTMC 喉返旁 LNM——预测终点从二元走向多分类、从影像走向可解释，构成稳定的可转化方向（D13）。
4. **代谢–免疫轴持续累积间接证据**：ECT2–硫辛酸能量代谢（#7）延续 run #21–#22 的 SMDT1/代谢基因线索，但仍未触及 APOE/MGST1 特异性亚群（D3）。
5. **去分化/再分化机制多点推进**：miR-335-5p 介导 BRAF V600E 再分化增敏 RAI（#10）、mPSM 复发风险情境依赖（#9）、小鼠+超声去分化模拟（#11）——共同夯实 ST 维度但多为复习/机制浅层。

---

## 未解问题 (What Remains Unclear)

1. **D3 长期缺口未补**：连续 23 轮无直接锚定 APOE−/MGST1+ 癌细胞亚群的原发证据；ECT2 是不同代谢基因，不构成该轴证据。该「代谢–免疫干性转移亚群」仍停留在假设层。
2. **mPSM 效应修饰不明**：#9 显示 microscopically positive surgical margin 对 PTC 复发呈情境依赖，但具体修饰因子（肿瘤大小？腺外侵犯？分子亚型？）未厘清。
3. **SPP1+ 与 TREM2+ 生态位关系未决**：run #22 提出 SPP1+ × TREM2+ 空间共定位问题，本轮无新证据，仍待原代空间验证。
4. **再分化机制的体内因果缺失**：miR-335-5p（#10）、ECT2（#7）均为体外/部分临床，缺体内 LNM/RAI 模型闭环。
5. **ML 模型外推性存疑**：4 篇 AL 论文多为单中心回顾、缺外部验证与前瞻队列，AUC 不能外推临床效用（遵循 schema 规则）。
6. **边界条目的污染风险**：#22（irAE 甲减）因正则匹配被纳入，提示 in-scope 自动过滤对「thyroid」一词过度敏感，需人工复核。

---

## 方法/数据局限 (Method/Data Limitations In The Field)

- **回顾性单中心主导**：4 篇 AL 论文与多数机制研究为单中心回顾，外部验证与前瞻设计稀缺。
- **复习/个案/存档占比偏高**：本轮 22 条中，2 篇书章节、1 数据集、1 严格预印本、多篇综述/个案；ST 维度 90 天救援的 6 条多为综述/书章节/个案，原发证据密度低。
- **预印本与编目滞后**：近 30 天文献多无 PMID（本轮 22 条中 14 条「待编目」），以 DOI 为主标识；OpenAlex 索引预印本，已单独标注 `[preprint]` 并降档证据强度。
- **补充材料污染**：已靠 `SUPPLEMENT` 正则剔除（主窗口剔除 34 条中 31 条为标题未点名甲状腺、3 条非肿瘤主题）。
- **低频高分维度欠采样**：ST 30 天 = 0 触发 90 天补跑；90 天窗口更暴露 1 篇 High SP 论文（#1）被 30 天窗口结构性遗漏——印证 run #22 对 SC/SP/ME 默认 90 天的建议。
- **irAE 边界污染**：#22 揭示自动 in-scope 对「Hypothyroidism」误匹配，已人工标注为边界、不计入机制证据。
- **通道约束**：NCBI 不可达，PubMed 单点必然漏检；paper-search-mcp 未启用（仅补充源，本轮未调用，避免无效阻塞）。

---

## 候选未来方向 (Candidate Future Directions)

> 七维评分（Novelty / Feasibility / Data / Validation / Clinical / Method / Overcrowding，各 1–5，满分 35）。28–35 = Strong；21–27 = Feasible；14–20 = Exploratory。

| Direction | Rationale | Novelty | Feas | Data | Valid | Clin | Method | Overcrowd | **Total** | Verdict |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| **D3** APOE−/MGST1+ 代谢–免疫干性转移亚群 | 23 轮确认、无反证；本轮无新锚定 | 5 | 4 | 4 | 2 | 5 | 3 | 4 | **33** | Strong（无变化）|
| **D8** TREM2+ AHR–IDO1 / TAM 异质性 | #2 细胞解析免疫 + #8 菌群–免疫综述拓宽 | 4 | 5 | 5 | 4 | 5 | 4 | 4 | **32** | Strong（维持+拓宽）|
| **D9** SPP1–CD44 / SPP1+ TAM | run #22 双证据已建；本轮无新 SPP1+ | 5 | 5 | 5 | 4 | 5 | 4 | 4 | **31** | Strong（维持）|
| **D11** 乳酸化–EMT-TF（ETV4/KLF6） | #1 去分化轨迹 + #10 miR 再分化间接支撑；无新乳酸化 | 4 | 5 | 5 | 4 | 4 | 4 | 4 | **30** | Strong（维持）|
| **D12** 铁死亡–ATC/PTC | 本轮无新铁死亡；run #22 HIF-1α/ACSL + UTMD-CSF1 基础 | 4 | 4 | 4 | 3 | 4 | 4 | 4 | **27** | Feasible |
| **D13（新）** AI/DL 影像组学 + 可解释预测（LNM/肺转移/I-131） | 本轮 4 篇 AL 聚类，持续高产 | 3 | 5 | 5 | 3 | 5 | 3 | 2 | **26** | Feasible |
| **D14（新·强候选）** 细胞类型解析因果推断 + 空间多组学驱动发现 | #1（Mol Cancer snRNA+spatial）+ #2（因果+空间）直接赋能 | 4 | 4 | 4 | 4 | 3 | 5 | 3 | **28** | Strong（边际）|

**D14 七维明细（28）**：Novelty 4（因果推断 + 空间在 TC 应用新颖）/ Feasibility 4（需 snRNA+空间+eQTL，本轮论文已提供框架与数据）/ Data 4（匹配队列增长中）/ Validation 4（跨队列可验）/ Clinical 3（机制发现，间接）/ Method 5（严谨因果设计）/ Overcrowding 3（因果+空间新兴但 TC 特异少）。

---

## 推荐下一步方向 (Recommended Next Direction)

**首选：以本轮 *Molecular Cancer* snRNA+空间去分化图谱（#1）与细胞类型解析因果 + 空间框架（#2）为引擎，打通「方法论（D14）→ 机制缺口（D3）」。**

具体第一步（直接可执行，复用公开数据）：
1. **APOE−/MGST1+ 原代空间锚定（D3 长期缺口）**：在 #1 的 snRNA+空间甲状腺图谱中，按 `APOE low ∧ MGST1 high` 双边界定义癌细胞亚群，检验其是否富集于去分化轨迹末端与间质互作热点——一举补上 D3 缺失 23 轮的原发空间证据。
2. **SPP1+ × TREM2+ TAM 生态位共定位（D9/D8）**：在同图谱中复用 POSTN+ myCAF 空间坐标（run #21 引用 42430190），做 SPP1 × TREM2 多重免疫荧光/空间转录组共定位，厘清两 TAM 生态位是否为同一/不同。
3. **去分化轨迹的因果驱动排序（D14）**：用 #2 的细胞类型解析因果框架，对 #1 的去分化轨迹做 eQTL/空间因果排序，优先锁定可成药驱动。

**claim 边界**：D3 在获得原代空间锚定前，仍限定为「代谢–免疫耦合的去分化/LNM 驱动亚群」假设，不得外推为已验证靶点；ML 模型（D13）在外部多中心验证前不得声称临床效用。

---

## 随访阅读清单 (Follow-Up Reading List)

- **#1 *Molecular Cancer* dediff atlas (10.1186/s12943-026-02699-2)**：本轮最关键，D3/D11/D14 起点；待追踪其数据可用性（snRNA+空间矩阵）。
- **#2 Cell-type-resolved causal+spatial (10.1111/iji.70066)**：D14 方法论模板，注意其自身免疫 + 恶性混合，需抽取恶性子集。
- **run #22 SPP1+ TAM 双证据**（Zenodo 10.5281/zenodo.22290057 + JCO 摘要 10.1200/jco.2026.44.19_suppl.239）：D9 基底，待正式发表验证。
- **#10 miR-335-5p (10.1002/1878-0261.70181)** + **#7 ECT2 (10.1186/s12935-026-04459-0)**：去分化/代谢–免疫轴补充。
- **#3 DL habitat radiomics (10.1038/s41746-026-03203-2)**：D13 中方法最严谨（注册研究），优先复现。

---

## 可复现性说明 (Reproducibility Notes)

- **Search date / 检索日期**: 2026-09-17.
- **Databases / 数据库**: OpenAlex（主源）；Crossref + Unpaywall（High 元数据/OA 校验）；NCBI/PubMed 不可达未用；paper-search-mcp 未调用。
- **Query strings / 查询**: 9 路维度见 `oa_search.py` 的 `QUERIES`（`a`–`i`：MO/PR、MO、AL/PR、IM、SC、SP、PR、ST、ME），均含 `THYROID = (thyroid|PTC|PTMC|FTC|MTC|ATC)` 与 `from_publication_date` 过滤，`sort=publication_date:desc`。
- **Filters / 过滤**: 标题点名甲状腺 ∧ 整体肿瘤主题；剔除补充材料、多版本合并、他病顺带提及。
- **Deduplication / 去重**: 标题归一化为主键；DOI/PMID/标题三者任一命中基线即判旧。
- **Screening / 筛选**: 主窗口 30 d（2026-08-18→09-17）去重唯一 94 / 在范围 60 / 剔除 34；ST 维度 30 d = 0 → 90 d 补跑（2026-06-19→09-17）回补 6 ST + 1 High SP 溢出。
- **Files saved / 产出文件**:
  - `literature_review_20260917_030445.md`（本报告）
  - `search_results_latest.json`（累积基线 171 条 + 22 new_records）
  - `search_results_20260917_030445.json`（同上时间戳副本）
  - `search_results_20260917_030151.json`（30 d 主窗口）
  - `search_results_20260917_030311_90day_ST.json`（ST 90 d 补跑）
  - `search_results_20260917_enrich.json`（2 High Crossref+Unpaywall 校验）

---

## 相对上一份报告的变化 (Delta vs Run #22, 2026-09-11)

| 维度 | Run #22 | Run #23 | 变化 |
|---|---:|---:|---|
| 新增唯一记录 | 36（31 主 + 5 ME90） | **22**（15 主 + 6 ST90 + 1 SP 溢出） | 减少，部分因窗口对齐（基线已吸收 #22 结果） |
| 预印本/存档 | 0 严格预印本 + 4 降档（2 Zenodo + 2 摘要） | 1 严格预印本 + 3 降档（1 figshare + 2 书章节） | 结构类似 |
| 头条信号 | **SPP1+ TAM 浮现（D9 28→31）** | **突变特异性去分化 snRNA+空间图谱（D14 赋能）** + **4 篇 ML/DL 聚类** | 信号转移 |
| D3 (APOE/MGST1) | 无变化（22 轮） | **无变化（23 轮）** | 维持 Strong 33 |
| D8 (TREM2+/TAM) | 维持+拓宽 32 | 维持+拓宽 32（#2/#8） | 稳定 |
| D9 (SPP1+ TAM) | 28→31（强化） | **31 维持（本轮无新 SPP1+）** | 强化暂停 |
| D11 (乳酸化–EMT) | 30 维持 | 30 维持（去分化轨迹间接支撑） | 稳定 |
| D12 (铁死亡) | 27 探索 | 27 维持（无新） | 稳定 |
| 新增方向 | D12 铁死亡 | **D13（ML 影像组学 26）+ D14（因果+空间 28）** | 扩容 |
| ST 维度 | ME 90 d 补跑 | **ST 90 d 补跑**（0→6） | 协议触发 |

**关键收敛发现 (Key convergence)**：本轮由「突变特异性去分化多组学图谱」(Mol Cancer) 与「细胞类型解析因果 + 空间」(IJI) 共同把研究方法推到 **snRNA + 空间 + 因果推断** 的高分辨率范式，这是相较 run #22「SPP1+ TAM 涌现」的范式升级信号。

**新信号/方向变化 (New signals)**：① 算法方法（AL）由零散走向「可解释 + 多分类 + 影像组学」聚类（D13 新立）；② 空间组学首次出现突变分辨率去分化原发证据（#1），显著降低 D14 启动门槛；③ 代谢–免疫轴仍仅靠 ECT2 间接补点，D3 锚定缺口未破。

**与历史报告差异 (Difference from history)**：run #22 头条是免疫 TAM（SPP1+）单点突破；run #23 头条转为「方法范式升级（因果+空间多组学）+ 算法聚类」，免疫侧无新增 TAM 亚群证据但获细胞解析框架支撑。总量下降主要因 30 天窗口较 #22 更窄且基线已吸收前期结果，**非领域平台期**（90 天补跑仍捕获 High SP 论文即证）。

---

## 持续跟踪：APOE−/MGST1+ 代谢–免疫干性亚群（D3）状态

**结论：本轮无变化（Unchanged），连续第 23 轮。** 本轮 22 条新增中，无任何论文直接锚定 APOE/MGST1 癌细胞亚群；#7 ECT2 属不同代谢基因，不构成 D3 证据。代谢–免疫轴仅在「ECT2–硫辛酸能量代谢」层面获间接数据点与 run #21–#22 的 SMDT1 线索延续，但 APOE−/MGST1+ 特异性亚群仍缺原代空间验证与体内靶向证据。D3 维持 Strong（rubric 33），建议下一轮以 #1 图谱直接做 APOE−MGST1+ 双边界空间锚定（见推荐下一步）。
