# Literature Review: 甲状腺癌侵袭、淋巴结与远处转移、复发、预后及其分子机制、肿瘤免疫微环境、单细胞与空间组学、机器学习/深度学习方法
# Thyroid Cancer (PTC/PTMC/FTC/MTC/ATC): Invasion, Nodal & Distant Metastasis, Recurrence, Prognosis, Molecular Mechanisms, Tumor Immune Microenvironment, Single-Cell & Spatial Omics, and ML/DL Methods

**Run #29 (第 29 轮) · 检索日 / Search date: 2026-10-16 · 时间戳 TS: `20261016_030414`**
**Sources**: OpenAlex（主）, Europe PMC（第二通道）, Crossref（DOI 校验）, OpenAlex 定向基因深挖（第三通道）
**Search window**: 30 d = 2026-09-16 → 2026-10-16；90 d = 2026-07-18 → 2026-10-16；Europe PMC `PUB_YEAR:2026`；深挖 `from_publication_date:2026-06-01`
**Baseline**: 527 → **559**（本轮新增 32）

---

## 中文摘要

本轮三通道并行检索，去重后唯一新增 **32 条**（OpenAlex 30 d 窗口 14 / Europe PMC 15 / 定向基因深挖 3），相对基线 527 累积至 **559**。按维度计：算法方法 AL 17、预后转移 PR 11、分子机制 MO 5、代谢重编程 ME 3、单细胞 SC 1、空间组学 SP 1、免疫微环境 IM 1；按相关性 High 2 / Medium 21 / Low 9；严格预印本 1 条（Research Square）；12 条尚无 PMID（PubMed 编目滞后，本轮 NCBI 通道不可用，无法回填，见 §12）。

**本轮最突出的不是某一条新通路，而是一组彼此独立的「证伪 / 校准 / 负结果」**：

1. ⭐⭐⭐ **Zenodo 存档（10.5281/zenodo.23319288）** 对甲状腺癌"复发相关高危肿瘤细胞状态"做了方法学极为完整的再分析：53 个分析脚本、公开 scRNA + bulk + 空间 + H&E 形态计量、**12 个已发表签名的基准竞技场（12-signature benchmark）**、以及**随机签名零校准（random-signature null calibration）与 family-wide FDR 控制**。核心结论：高危状态中**可重复的那一部分是甲状腺分化丧失（dedifferentiation），而不是增殖（proliferation）**。这是 29 轮以来第一次有研究系统性检验"已发表签名是否真的优于同等大小的随机基因集"。
2. ⭐⭐ **多模态大模型（MLLM）在甲状腺的三条独立负结果**： clinician 记录的结构化 ACR TI-RADS 特征单独输入即可达 84.2% 准确率，**与"图像+特征"合并输入完全相同**，而纯图像输入仅 73.8% → 图像本身**未提供增量**；6 款公开 MLLM 灰度超声分类中最佳者（Gemini 3.1 Pro）κ=0.580 / AUC 77.1%，**资深放射科医师优于全部 6 款**；甲状腺 FNA 细胞学上 ChatGPT / Gemini 的 Bethesda 分类准确率仅 **26.2% / 23.6%**，MTC 与 ATC 几乎从不识别正确。
3. ⭐⭐ **ATA 2025 vs 2015 风险分层（n=1508）**：2025 版区分度更高（5 年 AUC 0.78 vs 0.73，p=0.004），但把 **38.8% 的无复发患者也上调了风险类别**，绝对 NRI 为 **−22.6%**（加性 NRI 仅 +9.7%）→ 区分度提升并不等于净临床获益。

机制侧最强的三条原发证据：**MIB2 经 RING 结构域介导 HK2 的 K48 连接多聚泛素化降解、抑制糖酵解、从而限制 PTC 侵袭**（*Endocr-Relat Cancer*, PMID 42847133）；**CAF 在缺氧下经 ROS/NF-κB 产生 IL-6，旁分泌驱动 PTC 的 MAPK 激活，IL-6R 阻断剂托珠单抗（tocilizumab）体内显著抑瘤**（PMID 42847132，已上市药物可再利用）；**CRABP1 甲基化下调标记侵袭性恶性上皮状态**，且作者明确声明"甲基化与地西他滨结果不确立 CRABP1 特异或位点特异的表观因果"（r=−0.2069, R²=0.0428）——是本轮**主张边界写得最严谨**的一篇。

**持续跟踪方向 D3″（APOE×MGST1）**：第 29 轮复检，OpenAlex 全库 `MGST1 × thyroid` 命中 **仍为 1**（连续 4 轮零增长），`APOE × MGST1 × thyroid` 共现 **= 0**。维持 Run #28 的**归档终判（阴性）**，不再投入。

**推荐下一步**：**D26 签名与模型的可信度审计（null calibration + benchmark arena）**，rubric **32**——以本轮 Zenodo 存档已释放的 53 个 MIT 许可脚本为引擎，① 复现 12 签名基准；② 把随机签名零校准推广到 LNM 签名与影像组学 / ML 模型；③ 检验"分化丧失轴"是否在跨队列上真正优于已发表签名。与 **D15（去分化 / ATC，31）** 共享同一数据骨架，可合并为一条执行路线。

---

## English Abstract

This run used three parallel channels and yielded **32 de-duplicated new records** (OpenAlex 30-day window 14 / Europe PMC 15 / targeted gene deep-dig 3), extending the cumulative baseline from **527 to 559**. Distribution: AL (algorithmic methods) 17, PR (prognosis & metastasis) 11, MO (molecular mechanism) 5, ME (metabolic reprogramming) 3, SC (single-cell) 1, SP (spatial omics) 1, IM (immune microenvironment) 1. Relevance: High 2 / Medium 21 / Low 9. One strict preprint (Research Square). Twelve records lack a PMID (PubMed indexing lag; NCBI was unreachable this run so backfill was impossible — see §12).

**The dominant signal of Run #29 is not a new pathway but a cluster of independent falsification / calibration / negative results.**

1. ⭐⭐⭐ A **Zenodo deposit** (10.5281/zenodo.23319288) re-analyses the recurrence-associated high-risk thyroid tumor cell state with 53 analysis scripts over public single-cell, bulk, spatial transcriptomic and H&E histopathology data, including a **12-signature benchmark arena** and **random-signature null calibration with family-wide FDR control**. Its conclusion: the reproducible component of the high-risk state is **loss of thyroid differentiation, not proliferation**. This is the first study in 29 surveillance rounds to test systematically whether published signatures actually outperform size-matched random gene sets.
2. ⭐⭐ **Three independent negative results for multimodal large language models (MLLMs) in thyroid.** Clinician-recorded structured ACR TI-RADS features alone reached 84.2% accuracy — **exactly equal to image+feature input** — while image-only input gave 73.8%, i.e. the image contributed no increment. Across 6 public MLLMs on grayscale ultrasound, the best (Gemini 3.1 Pro) reached κ = 0.580 / AUC 77.1%, and **a senior radiologist outperformed all six**. On thyroid FNA cytology, ChatGPT and Gemini achieved only **26.2% / 23.6%** accuracy on Bethesda categories, with MTC and ATC almost never correctly identified.
3. ⭐⭐ **ATA 2025 vs 2015 risk stratification (n = 1508)**: the 2025 system discriminates better (5-year AUC 0.78 vs 0.73, p = 0.004) but **up-classified 38.8% of recurrence-free patients**, yielding an **absolute NRI of −22.6%** (additive NRI only +9.7%) — better discrimination is not net clinical benefit.

The three strongest primary mechanistic findings: **MIB2 promotes K48-linked polyubiquitination and proteasomal degradation of HK2 via its RING domain, suppressing glycolysis and restricting PTC invasiveness** (*Endocr-Relat Cancer*, PMID 42847133); **cancer-associated fibroblasts produce IL-6 under hypoxia through a ROS/NF-κB axis, driving PTC MAPK activation in parallel, and the approved IL-6R blocker tocilizumab suppresses tumour growth in vivo** (PMID 42847132); **methylation-associated downregulation of CRABP1 marks an aggressive malignant epithelial state**, with the authors explicitly stating that the methylation/decitabine findings "do not establish CRABP1-specific or locus-specific epigenetic causality" (r = −0.2069, R² = 0.0428) — the most carefully bounded claims of this run.

**Tracked direction D3″ (APOE × MGST1)**: at round 29, OpenAlex returns **still 1** hit for `MGST1 × thyroid` (four consecutive rounds of zero growth) and **0** for `APOE × MGST1 × thyroid`. The Run #28 **archival negative verdict stands**; no further investment.

**Recommended next step**: **D26 — credibility auditing of signatures and models (null calibration + benchmark arena)**, rubric **32**. Use the 53 MIT-licensed scripts released with this run's Zenodo deposit as the engine to (i) reproduce the 12-signature benchmark, (ii) extend random-signature null calibration to LNM signatures and radiomics/ML models, and (iii) test whether the differentiation-loss axis genuinely outperforms published signatures across cohorts. D26 shares a data backbone with **D15 (dedifferentiation / ATC, 31)** and can be executed as a single route.

---

## 一、检索策略 (Search Strategy)

### 1.1 通道探针 / Channel probe（本轮开局必做，结果有变化）

| 通道 | 本轮实测（2026-10-16） | Run #28 补充时结论 | 判定 |
|---|---|---|---|
| OpenAlex `api.openalex.org` | ✅ HTTP 200 / 1.18 s | ✅ | 主通道，正常 |
| Europe PMC `www.ebi.ac.uk` | ✅ HTTP 200 / 1.79 s | ✅ | 第二通道，正常 |
| Crossref `api.crossref.org` | ✅ HTTP 200 / 1.39 s（9/10 DOI 校验成功） | ✅ | 恢复正常（Run #28 曾超 20 min 未完成） |
| **NCBI eutils** | ❌ **HTTP 000 / 15.1 s（绕过代理）**；带代理 000 / 0.15 s（连接立即被拒） | ✅ 200 / 0.5–0.9 s | ⚠️ **再次不可达**〔**2026-10-17 已订正，见下**〕 |

> 🔴 **2026-10-17 订正（根因推翻，非通道问题）**：上表「NCBI 再次不可达」及此前 29 轮的全部 ✅/❌ 横跳**均为误判**。抓真实错误后定位为：
>
> ```
> curl: (35) schannel: next InitializeSecurityContext failed:
>        CRYPT_E_REVOCATION_OFFLINE (0x80092013)
> ```
>
> **根因是 Windows Schannel 证书吊销检查（OCSP/CRL）连不上吊销服务器 → TLS 握手被中止**，
> 属 **TLS 层**问题，**不是网络封锁**（DNS 正常解析到真实 NCBI IP `2600:1901:0:c831::`）。
> 吊销服务器时通时不通，故表现为「时变」，被误读成通道横跳。
>
> **修复**：`curl --ssl-no-revoke` → eutils **200 / 0.42 s**；或 Python `urllib`（走 OpenSSL，默认不查吊销）
> → einfo **200 / 0.64 s**、`efetch` 可取完整摘要。偶发 **HTTP 429 = NCBI 真实限流**（非故障），退避 3 s 即通。
>
> **已于 2026-10-17 补跑回填**（脚本 `_pmid_backfill_run29b.py`，urllib + 429 退避 + 标题回退相似度校验）：
> 559 条中 **19 条成功定号**，27 条预印本/数据集按规则跳过，余 131 条截至该日 PubMed 尚未收录。
> → 本报告中仍标「待编目*」者意为 **PubMed 尚未编目（非检索失败）**，见 §附录 C。

### 1.2 检索矩阵 / Query matrix

| Source | Query / Route | Filters | 命中 | 在范围 | Notes |
|---|---|---|---:|---:|---|
| OpenAlex `oa_search.py` | 九路布尔矩阵（a 分子机制+预后转移 / b 分子机制 / c 算法方法 / d 免疫微环境 / e 单细胞 / f 空间组学 / g 预后转移 / h 转移干性 / i 代谢重编程） | `--days 30`, `per-page 25`, `sort=publication_date:desc` | 86（去重后） | 62 | 脚本内建三类清洗（补充材料剔除、多版本合并、顺带提及剔除） |
| OpenAlex `oa_search.py` | 同上九路 | `--days 90`, `per-page 50` | 251（去重后） | 172 | 30 d 为其子集；本轮 90 d **未产出额外增量**（历史欠采样已由 Run #26–#28 回填完毕） |
| **Europe PMC**（第二通道） | 12 路：`SC / SP / IM / ME / AL / ST / MO / PR / MACRO2 / SPATIAL_DS / LIPID / AI` | `PUB_YEAR:2026`, `sort=P_PDATE_D desc` | 见 §1.3 | 人工筛入 15 | Run #29：LIPID 补 LPL/VLDLR/CD36；AI 补 agentic/multimodal |
| **定向基因深挖**（第三通道） | 面板 34 → **42**（新增 CRABP1 / HK2 / CTSS / MIB2 / TCF4 / XPR1 / ACBD7 / METTL7B / TMED2 / DGKB） | `from_publication_date:2026-06-01` | 42 基因 | 筛入 3 | 见 §1.3 |
| Crossref | 按 DOI 校验题录元数据 | timeout 10 s（Run #28 建议） | 10 | 9 成功 | Zenodo `10.5281/zenodo.23319288` 返回 404（数据集型 DOI 未被 Crossref 收录，非网络故障） |
| Unpaywall | 本轮未跑 | — | — | — | 通道未实测；以 OpenAlex `oa_status` 为权威 |
| NCBI eutils | 未用 | — | — | — | ❌ 不可达，见 §1.1 |
| `paper-search-mcp` | 未用 | — | — | — | 本会话未连接 |

### 1.3 通道产出质量对比（本轮关键方法学观察）

| 通道 | 候选 | 实际筛入 | 可用率 | 说明 |
|---|---|---:|---:|---|
| OpenAlex 30 d | 86 | 14 | 16% | 本轮**真新增**主要来源（10 月新文） |
| OpenAlex 90 d | 251 | 0（增量） | 0% | **历史欠采样已回填完毕** → 90 d 窗口不再产出增量，这是一个**正向信号**：三通道固化后欠采样已被消除 |
| Europe PMC | 12 路合计 | 15 | 低 | 污染显著回升：`AI` 路 31 候选中大量为甲状腺眼病（TED）/ 消融 / 兽医；`LIPID` 路 27 候选中绝大多数为 **MASLD / 甲状腺-肝轴 / 肥胖 / 妊娠**（非肿瘤代谢）；`MO`/`ME`/`PR` 路大量为撤稿与更正条目 |
| 定向基因深挖 | 42 基因 | 3 | 极低 | 绝大多数命中为**补充材料附件**（如 HIF-1α/ACSL4 论文的 9 个 figshare "Additional file N"）、双相障碍小鼠、海水驯化鱼类等非相关文献 |

> 📌 **方法学结论**：本轮新增数（32）低于 Run #28（70）与 Run #27（66），但**不是领域平台期**，而是三通道固化后**历史欠采样回填已基本完成**（90 d 窗口零增量即为直接证据）。本轮 32 条中 30 条发表于 2026-08 之后，属真实当期产出。**Europe PMC 与深挖通道已进入"边际递减"阶段**，下轮应考虑降低其配额或进一步收紧查询式。

---

## 二、纳入论文 (Included Papers)

### 2.1 High 相关性（2 条，逐条要点）

**H1. Analysis code and derived data for: the recurrence-associated high-risk thyroid tumor cell state is primarily a dedifferentiation program**
Zenodo, 2026-10-12. DOI: 10.5281/zenodo.23319288. PMID: 待编目*. 维度 SP/SC/PR. OA: 数据集（MIT 脚本 + CC BY 4.0 表格）.
*Author claim*: 重新分析公开 single-cell、bulk 与空间转录组数据及公开 H&E 病理图像，发现复发相关高危状态中**可重复的成分是甲状腺分化丧失，而非增殖**。含 53 个分析脚本：事件表推导、单细胞状态识别与跨队列比较、**带 12 签名基准的 bulk 模型拟合**、**随机签名零校准（family-wide FDR 控制）**、空间转录组处理、H&E 图像形态计量、**区室解析的 GeoMx 校验**、驱动突变协变量模型。
*Agent note*: ⭐ 本轮最重要条目。它不是又一篇"新签名"，而是**对已有签名做可信度审计**的方法学基础设施，且代码与派生表格**全部公开可 fork**（MIT / CC BY 4.0）。注意：Zenodo 数据集型存档，无同行评审，证据强度按 deposit 降档；但其脚本与 `docs/DATA_SOURCES.md` 的透明度远高于多数已发表签名论文。**注意区分**「存档本身的可信度」与「其结论的可复现性」——后者可用其脚本直接检验。

**H2. MIB2-mediated ubiquitination of HK2 inhibits glycolysis in PTC**
*Endocrine-Related Cancer*, 2026-10-07. DOI: 10.1530/erc-26-0049. PMID: 42847133. 维度 MO/PR/ME.
*Author claim*: MIB2 在 PTC 中显著下调，低表达与淋巴结转移、甲状腺外侵犯相关；MIB2 过表达抑制增殖/迁移/侵袭与体内成瘤。机制上 MIB2 经其 **RING 结构域**直接结合 **HK2**，促进 **K48 连接多聚泛素化**及蛋白酶体降解，抑制糖酵解通量。作者称此为首次证明 MIB2 通过靶向 HK2 降解调控糖酵解从而抑制 PTC 侵袭。
*Agent note*: ⭐ 本轮机制侧最完整的因果链（生物信息学 → 临床标本 → 体外功能 → 体内成瘤 → 泛素化连接类型 → 代谢通量）。**泛素化–糖酵解–侵袭**是此前 28 轮未出现过的三层连接。HK2 是糖酵解第一步限速酶，使该轴具备直接的代谢重编程解释力。限定：单一细胞系模型家族，未见独立外部队列的蛋白水平验证。

### 2.2 Medium 相关性（21 条，压缩列出）

| # | 标题（英文原文） | 来源 / 日期 | DOI / PMID | 维度 | 一句话中文要点 |
|---|---|---|---|---|---|
| M1 | Methylation-associated downregulation of CRABP1 marks an aggressive malignant epithelial cell state in thyroid carcinoma | Front Cell Dev Biol, 2026-10-14 | 10.3389/fcell.2026.1974822 / 待编目* | MO/SC | 17 例 PTC scRNA + CNV 推断鉴定 **CRABP1⁺ 恶性上皮亚群**（保留 CDH1/KRT19）；TCGA 中低 CRABP1 与 LNM、T 分期相关；敲低促迁移侵袭并伴 EMT 偏移；作者明确声明甲基化/地西他滨结果**不确立位点特异表观因果**（r=−0.2069, R²=0.0428） |
| M2 | Cancer-Associated Fibroblasts Drive Papillary Thyroid Cancer Progression through ROS/NF-κB/IL-6 Signaling in Hypoxic Microenvironment | Endocr-Relat Cancer, 2026-10-07 | 10.1530/erc-26-0198 / 42847132 | ME/IM/ST | scRNA 定位成纤维细胞为 IL-6 主要来源；缺氧经 **ROS→NF-κB** 驱动 IL-6；NAC/MitoQ/JSH-23 可阻断；**已上市药物托珠单抗（tocilizumab）体内显著抑瘤** |
| M3 | Association between primary tumor resection and survival in metastatic follicular thyroid carcinoma: a real-world population-based cohort Study | Sci Rep, 2026-10-08 | 10.1038/s41598-026-75182-z / 待编目* | PR | SEER 7636 例 FTC 中 363 例（4.75%）初诊即远处转移；PTR 组中位 OS **70 vs 27 月**、CSS **98 vs 47 月**；PSM 后方向一致但匹配队列小；PTR 组更年轻（65.2 vs 70.3 岁），**选择偏倚未排除** |
| M4 | Clinical and Molecular Genetic Testing Risk Stratification for Pediatric Papillary Thyroid Carcinoma Therapy | J Clin Endocrinol Metab, 2026-10-09 | 10.1210/clinem/dgag418 / 42857932 | PR/AL | 435 例 CAYA-PTC（2–18 岁）多中心；5 个独立预测因子：年龄 ≤15 岁、肿瘤 >4 cm、N1b、**合并桥本甲状腺炎**、RET/NTRK 融合；列线图 C-index 0.721 vs ATA 0.656；7 年 DFS 92.4/83.1/56.4% |
| M5 | Outcome of first-line chemotherapy for anaplastic thyroid cancer—a multicenter registry analysis | J Clin Endocrinol Metab, 2026-09-01 | 10.1210/clinem/dgag177 / 42046902 | PR/MO | 德国 7 中心 158 例 ATC；卡铂/紫杉醇（CP，n=97）与其他方案（n=61）**PFS 102 vs 89 天（p=0.23）、OS 278 vs 295 天（p=0.50），均无差异**；手术与较低死亡风险相关 → **阴性结果** |
| M6 | Comparative Performance of the 2015 and 2025 American Thyroid Association Initial Recurrence Risk Stratification Systems in DTC | Clin Endocrinol (Oxf)/Thyroid, 2026-10-07 | 10.1177/10507256261494916 / 42844696 | PR | 1508 例（中位随访 8.9 年）；2025 版 AUC 0.78 vs 0.73（p=0.004）**更优**，但同时把 38.8% 无复发者上调风险 → **绝对 NRI −22.6%**（加性 NRI +9.7%） |
| M7 | Impact of Clinician-Recorded ACR TI-RADS Features on ChatGPT-5.4-Based Thyroid Nodule Classification | Semin Ultrasound CT MRI, 2026-09-15 | 10.1053/j.sult.2026.09.001 / 42744256 | AL | 202 结节（153 例）前瞻；**features-only 84.2% = image+features 84.2% > image-only 73.8%**（Holm 校正 p=0.001）→ **图像输入未提供任何增量** |
| M8 | Comparative Performance of Multimodal Large Language Models in Grayscale Ultrasound-Based Classification of Thyroid Nodules | Semin Ultrasound CT MRI, 2026-08-22 | 10.1053/j.sult.2026.08.002 / 42632527 | AL | 178 例 / 239 结节；6 款公开 MLLM（ChatGPT-5.4、Gemini 3.1 Pro、Claude Opus 4.6、Qwen3.6-Plus、Kimi K2.5、ERNIE 5.0）；最佳 Gemini 3.1 Pro κ=0.580 / AUC 77.1%；**资深放射科医师优于全部 6 款** |
| M9 | Evaluating the diagnostic performance of multimodal large language models in thyroid cytology | Human Pathology, 2026-05-16 | 10.1016/j.humpath.2026.106156 / 42144078 | AL | 100 张 FNA 细胞学图（50 PTC / 50 非 PTC）；ChatGPT / Gemini 按 Bethesda 分类准确率仅 **26.2% / 23.6%**；**MTC 与 ATC 几乎从不识别正确** |
| M10 | Dual-discriminator GAN (DD-GAN) for Virtual Elastography Ultrasound in Thyroid Cancer Diagnosis | Academic Radiology, 2026-09-28 | 10.1016/j.acra.2026.09.019 / 42805865 | AL | 从常规 B 超**直接生成虚拟弹性成像（V-EUS）**；V-EUS 与真实 EUS 诊断 AUC **无显著差异**（内部 0.744 vs 0.774, p=0.318；外部 0.742 vs 0.759, p=0.461；前瞻 0.751 vs 0.761, p=0.772）；医师盲测**无法区分**；V-EUS 衍生的 Tsukuba 评分并入 TI-RADS 显著提升 AUC |
| M11 | Artificial intelligence-enabled analysis of radiology reports: epidemiology and outcomes of incidental thyroid findings | J Clin Endocrinol Metab, 2026-09-01 | 10.1210/clinem/dgag186 / 42037237 | AL/PR | Mayo Clinic 四院区 **115,683 例**；transformer NLP 识别偶发甲状腺发现（ITF）；ITF 患病率 **7.8%**；ITF 者后续结节诊断 OR **45**、活检 OR **46.8**；但**结节特征记录极差**（大小仅 44%、其他特征 <15%）→ 大规模**过度诊断级联**证据 |
| M12 | Multimodal radiomics based on dynamic contrast-enhanced ultrasound for predicting cervical LNM in PTC with Hashimoto's thyroiditis | Front Oncol, 2026-10-14 | 10.3389/fonc.2026.1840185 / 待编目* | AL/PR | 191 例 HT 合并 PTC；BMUS + DCE-US 参数图组学 + 临床特征；LASSO/RFE 筛选；三模型比较；**仅 7:3 随机拆分内部验证，无外部队列** |
| M13 | Deep Learning-Driven Multimodal Integration of Ultrasound and CT for Identifying Central Lymph Node Metastasis in PTC | Ultrasound Med Biol, 2026-10-01 | 10.1016/j.ultrasmedbio.2026.09.018 / PMID 42875362 | AL/PR | 超声 + CT 多模态融合判中央区 LNM；US+CT 双模态在甲状腺 LNM 上仍属相对少见设计 |
| M14 | A Multiparametric Approach Integrating Multimodal Ultrasound and Serum TPO-Ab for Differentiating Thyroid Carcinoma in Hashimoto's Thyroiditis | J Ultrasound Med, 2026-09-08 | 10.1002/jum.70419 / 42708642 | AL | 600 例 HT / 650 结节；单模态 2D-US 交叉验证 AUC 0.831，CEUS 0.671，TPO-Ab 0.621；三者联合 **0.849** → **多模态增量仅 +0.018** |
| M15 | Development and validation of a predictive model for thyroid nodule malignancy risk based on intralesional and perilesional ultrasound radiomic features | Gland Surgery, 2026-07-30 | 10.21037/gs-2026-0143 / 42725353 | AL | 147 例 C-TIRADS 4a/b；瘤内 + **瘤周 2 mm 外扩** ROI；PyRadiomics；LR/决策树/LightGBM；仍为单中心 7:3 拆分 |
| M16 | Clinical value of artificial intelligence ultrasound-assisted diagnostic system in the differential diagnosis of benign and malignant thyroid nodules | Medicine, 2026-08-01 | 10.1097/md.0000000000050126 / 42601685 | AL | 161 结节 / 91 例；AI-UADS AUC **0.933** vs 高年资超声医师 0.821（均 p<0.05）；亚组分析显示 ≤10 mm 与远离被膜结节优势更大；**回顾性病例对照，无外部验证** |
| M17 | Strategies for incorporating alternative splicing variants in thyroid nodule biopsy classification based on expression levels | Comput Methods Programs Biomed, 2026-06-06 | 10.1016/j.cmpb.2026.109506 / 42296790 | AL/MO | 335 例 HTA2.0 芯片；比较 TAC（探针组/连接点）与 EventPointer（剪接事件）两条流程；**分类质量强烈受处理流程影响**；TAC 变异 bootstrap 准确率 0.938；跨平台 RNA-seq 验证作者自述为"技术性复核而非完整独立验证" |
| M18 | Anaplastic Thyroid Carcinoma With Kinase Gene Fusions: Report of 3 Cases With Corresponding Cytologic, Histologic, and Molecular Findings | Diagn Cytopathol, 2026-07-18 | 10.1002/dc.70185 / 42470146 | MO | 3 例激酶融合型 ATC；**细胞学/组织学无法区分融合型与常规 ATC**；但 **BRAF V600E 与 RAS Q61R 免疫组化双阴性可作为早期做融合检测的指征** → 可直接落地的分诊规则 |
| M19 | UBE2C–TRIM21-driven NOS2 degradation stabilizes Tregs and suppresses pyroptotic signaling in thyrocytes in Hashimoto's thyroiditis | Inflamm Res, 2026-10-12 | 10.1007/s00011-026-02375-7 / PMID 42862325 | IM | HT 患者 Treg 中 UBE2C 持续下调；UBE2C–TRIM21 介导 NOS2 泛素化降解以稳定 Treg；EAT 模型过继转移工程化 Treg 验证。⚠️ **疾病为桥本甲状腺炎而非甲状腺癌**，仅作 UBE2C 基因的边界参考（UBE2C 在 Run #24 的 UBE2C⁺ ATC 样复发 FTC 中曾出现） |
| M20 | [Mechanism of timosaponin AⅢ liposomes loaded with auranofin in inducing ferroptosis in anaplastic thyroid carcinoma] | 中华肿瘤杂志, 2026-05-01 | 10.3760/cma.j.cn112152-20250914-00459 / 42151086 | ME | TAⅢ 脂质体载金诺芬（T-AUF-LPs）；CAL-62 细胞；Ferrostatin-1  rescue 确认铁死亡；ACSL4/NCOA4/GPX4、胞内铁、GSH、脂质过氧化；裸鼠异种移植验证 |
| M21 | Personalization of the extent of surgical treatment for papillary thyroid carcinoma based on preoperative immunocytochemical risk stratification | Clin Exp Exp Surg (cees), 2026-09-30 | 10.30978/cees-2026-3-53 / 待编目* | PR | 110 例 PTMC 前瞻对照；术前**细胞角蛋白 17（CK17）+ 甲状腺过氧化物酶（TPO）+ S 细胞**三联免疫细胞化学面板分层，指导手术范围个体化 |

### 2.3 Low 相关性（9 条，仅列题录）

| 标题 | 来源 / 日期 | DOI / PMID | 维度 | 剔除/降档理由 |
|---|---|---|---|---|
| Coal dust-stimulated macrophage-derived extracellular vesicles promote thyroid cancer cell phenotypes involving miR-205-5p, CAMK1G, and NF-κB-associated signaling | Front Immunol, 2026-10-14 | 10.3389/fimmu.2026.1856770 / 待编目* | MO/IM | 主题为**职业煤尘暴露**毒理学，甲状腺癌为下游表型；虽整合了 GSE274674 scRNA + TCGA-THCA + 双小鼠模型，但与本项目核心方向距离远 |
| Prognostic Analysis of Iodine-avid Residual Metastatic Lymph Nodes in Differentiated Thyroid Cancer | Research Square, 2026-10-14 | 10.21203/rs.3.rs-11024915/v1 / 待编目* | AL/PR | **预印本**（严格 `type=preprint`），证据强度降档；无摘要可得 |
| Risk Prediction Models for Postoperative Nausea and Vomiting in Adults Undergoing Thyroid Surgery | INPLASY, 2026-10-10 | 10.37766/inplasy2026.10.0046 / 待编目* | AL/PR | **研究方案注册**（protocol），非研究结果；终点为术后恶心呕吐，非肿瘤学终点 |
| Shaving Versus Resection on Recurrent Laryngeal Nerve in Thyroid Cancer Surgeries: A Systematic Review and Meta-Analysis | Head Neck, 2026-10-08 | 10.1002/hed.70509 / 42845094 | PR | 13 项回顾队列 / 532 例；刮除术复发更低（p=0.007）、声带活动更好；**作者自述刮除组病情更轻，存在选择偏倚** |
| Transforming the Imaging Assessment of Thyroid Nodules with Artificial Intelligence | J Digit Imaging, 2026-09-08 | 10.1007/s10278-026-02272-9 / 42711650 | AL | 叙述性综述，无原始数据 |
| Application of Artificial Intelligence in Diagnosis and Management of Thyroid Disease | Endocr Pract, 2026-08-29 | 10.1016/j.eprac.2026.08.018 / 42667959 | AL | 叙述性综述 |
| Artificial intelligence-driven transformation in the management of AUS thyroid nodules | Crit Rev Oncol Hematol, 2026-08-14 | 10.1016/j.critrevonc.2026.105538 / 42595195 | AL | 综述；AUS/意义未定异型性结节管理 |
| Letter to the Editor: Training the diagnostic artificial intelligence in thyroid sonography | Updates Surg, 2026-09-18 | 10.1007/s13304-026-02847-9 / 42758456 | AL | 致编辑信件，无原始数据 |
| The C-Cell Hyperplasia in Cellular Retinoic Acid Binding Protein 1 (CRABP1) Knockout Male Thyroid Gland | 2026-07-16 | 无 DOI / 无 PMID | MO | **无 DOI**；主题为 CRABP1 敲除雄性甲状腺 C 细胞增生，非癌；仅作 M1 的基因级旁证 |

---

## 三、证据矩阵 (Evidence Matrix)

> 列依 `evidence-matrix-schema.md`；**Relevance / Gap** 两列体现所属维度。OA 状态以 OpenAlex `oa_status` 为权威源。

### 3.1 High 相关性完整矩阵

| Paper | PMID/DOI | Disease/Population | Data Source | Method | Endpoint | Main Finding | Validation | Limitations | Relevance | Gap Suggested | Future Direction |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Recurrence-associated high-risk thyroid tumor cell state = dedifferentiation program（Zenodo 存档） | 待编目* / 10.5281/zenodo.23319288 | THCA（PTC/ATC 等），复发 vs 非复发 | 公开 scRNA + bulk + 空间转录组 + H&E 病理图像；GEO & cBioPortal | 53 脚本：事件表推导、单细胞状态识别与跨队列比较、**12 签名基准竞技场**、**随机签名零校准 + family-wide FDR**、空间处理、H&E 形态计量、**区室解析 GeoMx 校验**、驱动突变协变量 | 复发（事件表推导） | 高危状态中**可重复成分是甲状腺分化丧失，而非增殖** | 跨队列重复性本身即验证；随机签名为阴性对照；GeoMx 区室复核 | **未经同行评审的数据集存档**；不重分发原始数据；依赖上游公开队列注释质量 | **High**（SP/SC/PR） | 12 个已发表签名中**哪些真正优于随机基因集**尚未逐条公开；零校准尚未推广到 LNM 签名与影像/ML 模型 | **D26 签名与模型可信度审计** |
| MIB2-mediated ubiquitination of HK2 inhibits glycolysis in PTC | 42847133 / 10.1530/erc-26-0049 | PTC；组织标本 + 细胞系 + 体内成瘤 | 生信 + 临床标本 + PTC 细胞系 | 生物信息学筛选、临床标本验证、体外增殖/迁移/侵袭、体内成瘤、**RING 结构域互作 + K48 连接多聚泛素化 + 蛋白酶体降解 + 糖酵解通量** | 侵袭性表型（LNM / ETE 相关） | MIB2 在 PTC 中下调；过表达抑制恶性表型，机制为经 RING 结构域促 HK2 的 K48 泛素化降解 → 抑糖酵解 | 临床标本 + 体外 + 体内三层 | 细胞系模型单一；**无独立外部队列的蛋白水平验证**；未测患者预后终点 | **High**（MO/PR/ME） | MIB2–HK2 轴与已有糖酵解/耐药通路（如 TRIM47–FBP1 乳酸化）的关系未检验；无预后层证据 | **D18 代谢–耐药轴** |

### 3.2 Medium 相关性压缩矩阵

| Paper | PMID/DOI | Population / Source | Method | Endpoint | Main Finding | Validation | Limitations | Relevance | Gap |
|---|---|---|---|---|---|---|---|---|---|
| CRABP1 甲基化与侵袭性上皮状态 | 待编目* / 10.3389/fcell.2026.1974822 | 17 例 PTC scRNA + TCGA-THCA + 细胞系 + 异种移植 | scRNA + CNV 推断 + 甲基化分析 + 敲低/过表达 + 地西他滨 | LNM / T 分期 / 迁移侵袭 | CRABP1⁺ 恶性上皮亚群保留上皮特征；低 CRABP1 ↔ LNM；敲低促 EMT 样偏移 | TCGA bulk + 体内异种移植 | **作者明确否认表观因果**（r=−0.2069, R²=0.0428） | Medium（MO/SC） | 甲基化位点与 CRABP1 表达的因果方向未确立 |
| CAF 缺氧 ROS/NF-κB/IL-6 | 42847132 / 10.1530/erc-26-0198 | PTC 患者 scRNA + 原代 CAF/NF + 非接触共培养 + 体内 | scRNA 来源定位、缺氧处理、NAC/MitoQ/JSH-23 阻断、**托珠单抗** | 增殖 / MAPK 激活 / 肿瘤生长 | 成纤维细胞是 IL-6 主要来源；缺氧 → ROS → NF-κB → IL-6；托珠单抗体内抑瘤 | 药理阻断 + 体内共注射 | 非接触共培养无法完全模拟体内空间；托珠单抗剂量未做剂量-效应 | Medium（ME/IM/ST） | 已上市药物可再利用，但**无甲状腺癌临床队列验证** |
| 转移性 FTC 原发灶切除 | 待编目* / 10.1038/s41598-026-75182-z | SEER 7636 例 FTC，其中 363 例初诊远处转移 | KM + log-rank + PSM + 多变量 Cox | OS / CSS | PTR 组中位 OS 70 vs 27 月、CSS 98 vs 47 月 | SEER 人群队列 + PSM | **PTR 组显著更年轻**（65.2 vs 70.3）；PSM 后匹配队列小 | Medium（PR） | 选择偏倚未排除；FTC 亚型（ minimally invasive vs widely invasive）未分层 |
| CAYA-PTC 临床基因组列线图 | 42857932 / 10.1210/clinem/dgag418 | 435 例 2–18 岁 PTC，多中心回顾 | 临床 + 术后病理 + 分子检测 → 列线图；与 ATA 儿科分层内部比较 | DFS | 5 个独立因子（年龄 ≤15、>4 cm、N1b、**合并桥本**、RET/NTRK 融合）；C-index 0.721 vs 0.656 | 多中心 + 内部比较 | **无外部验证**；分子检测 panels 可能跨中心不一致 | Medium（PR/AL） | 桥本甲状腺炎作为**风险因子**（与"保护性"叙事相反）需独立验证 |
| ATC 一线化疗（德国注册） | 42046902 / 10.1210/clinem/dgag177 | 158 例 ATC，7 中心，2000–2024 | KM + log-rank + Cox | PFS / OS | **CP 与其他方案无差异**（PFS 102 vs 89 d, p=0.23；OS 278 vs 295 d, p=0.50）；手术与较低死亡风险相关 | 多中心注册 | 回顾性、24 年跨度（治疗方案时代混杂）；无随机化 | Medium（PR/MO） | **阴性结果**：缺乏 ATC 一线化疗的随机证据 |
| ATA 2015 vs 2025 | 42844696 / 10.1177/10507256261494916 | 1508 例 DTC，中位随访 8.9 年 | AUC + NRI + DCA | 结构性无复发生存 | 2025 版 AUC 更优（0.78 vs 0.73）但**绝对 NRI −22.6%** | 单中心三级转诊队列 | 单中心（中国）；无外部验证 | Medium（PR） | 区分度提升 ≠ 净获益；**修订的多灶性标准**驱动了再分类 |
| ChatGPT-5.4 + TI-RADS | 42744256 / 10.1053/j.sult.2026.09.001 | 202 结节 / 153 例，前瞻横断 | 三种输入策略对比；Cohen κ；GEE + Holm 校正 | 与病理一致的准确率 | **features-only 84.2% = image+features 84.2% > image-only 73.8%** | 病理金标准 + 前瞻 | 单中心；单一模型版本（存在 version drift 风险） | Medium（AL） | **图像未提供增量**——MLLM 的"多模态"价值在甲状腺超声上未被证实 |
| 6 款 MLLM 灰度超声 | 42632527 / 10.1053/j.sult.2026.08.002 | 178 例 / 239 结节，前瞻 | 6 款公开 MLLM 统一提示词，无微调；κ + ROC；放射科医师基准 | 良恶性分类 | 最佳 Gemini 3.1 Pro κ=0.580 / AUC 77.1%；**资深放射科医师优于全部 6 款** | 病理金标准 + 医师基准 | 仅裁剪后的最大切面；模型版本快速迭代 | Medium（AL） | MLLM 仍显著低于人类专家；**未做人机协作（AI 辅助医师）增益检验** |
| MLLM 甲状腺细胞学 | 42144078 / 10.1016/j.humpath.2026.106156 | 100 张 FNA 图（50 PTC / 50 非 PTC） | ChatGPT 与 Gemini 各 5 轮 | Bethesda 分类准确率 | **26.2% / 23.6%**；MTC 与 ATC 几乎从不识别正确 | 专家病理复核 | 单张 40× 视野（非全片）；样本量小 | Medium（AL） | 细胞学场景 LLM **不可用于诊断**，仅可作教学/分诊探索 |
| DD-GAN 虚拟弹性成像 | 42805865 / 10.1016/j.acra.2026.09.019 | 甲状腺结节，内部 + 外部 + 前瞻三套测试集 | 双判别器 GAN 由 B 超生成 V-EUS；SR 一致性量化；医师盲测 | 良恶性诊断 AUC | V-EUS 与真实 EUS **AUC 无显著差异**；医师盲测不可区分；Tsukuba 评分并入 TI-RADS 显著提升 AUC | 内部 + **外部 + 前瞻**三套验证 | 生成式模型的幻觉风险未量化；前瞻样本量未报告 | Medium（AL） | **硬件无关的弹性成像**——便携设备场景价值未做卫生经济学评估 |
| NLP 偶发甲状腺发现（ITF） | 42037237 / 10.1210/clinem/dgag186 | Mayo 四院区 **115,683 例** | transformer NLP 抽取影像报告 | ITF 患病率与下游结局 | ITF 7.8%；后续结节诊断 OR **45**、活检 OR **46.8**；**结节特征记录极差**（大小 44%） | 多院区大样本 | 回顾性；NLP 抽取误差未与人工双读比较 | Medium（AL/PR） | **过度诊断级联**缺乏"是否改善患者结局"的证据 |
| DCE-US 多模态组学预测 CLNM（合并 HT） | 待编目* / 10.3389/fonc.2026.1840185 | 191 例 HT 合并 PTC | BMUS + DCE-US 参数图组学 + 临床/US 特征；LASSO/RFE；三模型 | 术前 CLNM | 联合模型优于单一模型（SHAP 解释） | **仅 7:3 随机拆分内部验证** | 无外部验证；HT 背景使组学特征稳定性存疑 | Medium（AL/PR） | 影像组学在 HT 背景下是否可迁移未检验 |
| 超声+CT 深度学习判中央区 LNM | PMID 42875362 / 10.1016/j.ultrasmedbio.2026.09.018 | PTC | US + CT 多模态融合 | 中央区 LNM | 多模态优于单模态（摘要未取回，细节待核） | 待核 | 摘要未获取 | Medium（AL/PR） | 需取回全文核实样本量与验证方式 |
| 多模态超声 + TPO-Ab（HT） | 42708642 / 10.1002/jum.70419 | 600 例 HT / 650 结节 | 2D-US + CEUS + TPO-Ab；LR + 6 分类器；分层 5 折交叉验证 | 结节良恶性 | 联合 AUC **0.849** vs 2D-US 单模态 0.831 | 交叉验证（**非外部**） | **多模态增量仅 +0.018**；各模态子集不完整（CEUS 475、TPO-Ab 452） | Medium（AL） | 增量过小，质疑"多模态"必要性 |
| 瘤内+瘤周组学（C-TIRADS 4a/b） | 42725353 / 10.21037/gs-2026-0143 | 147 例 C-TIRADS 4a/b | ITK-SNAP 勾画 + 2 mm 外扩瘤周 ROI；PyRadiomics；LR/树/LightGBM | 结节恶性风险 | 瘤内+瘤周 + 临床联合模型表现最佳 | 单中心 7:3 拆分 | **无外部验证**；4a/b 恶性率跨度大是选择难题 | Medium（AL） | 瘤周特征的生物学含义（炎症？浸润？）未解释 |
| AI-UADS vs 超声医师 | 42601685 / 10.1097/md.0000000000050126 | 161 结节 / 91 例，回顾病例对照 | AI-UADS vs 高年资超声医师；ROC 与亚组分析 | 良恶性鉴别 | AI-UADS AUC **0.933** vs 医师 0.821（均 p<0.05） | 手术病理金标准 | **回顾性病例对照**；"高年资医师"年资未量化；无外部验证 | Medium（AL） | 回顾性设计易高估 AI 性能（病例选择偏倚） |
| 可变剪接变异用于结节分类 | 42296790 / 10.1016/j.cmpb.2026.109506 | 335 例，HTA2.0 芯片 | TAC vs EventPointer 两条流程；bootstrap；去重 | Bethesda III/IV 分类 | **分类质量强烈受处理流程影响**；TAC 变异准确率 0.938 | 患者/样本级外部验证（公开芯片集） | RNA-seq 验证作者自述为"技术性复核" | Medium（AL/MO） | 流程依赖性是**可重复性隐患** |
| ATC 激酶融合 3 例 | 42470146 / 10.1002/dc.70185 | 3 例融合型 ATC | FNA 细胞学 + 组织学 + 分子 | 诊断分诊 | 细胞/组织学**无法**区分融合型与常规 ATC；**BRAF V600E + RAS Q61R 双阴性 IHC 提示应早期做融合检测** | 3 例自身对照 | n=3；融合靶向疗效受共突变限制 | Medium（MO） | 需更大队列验证该 IHC 分诊规则 |
| UBE2C–TRIM21–NOS2（桥本） | PMID 42862325 / 10.1007/s00011-026-02375-7 | HT 患者 vs 健康对照（**非癌症**） | Treg 转录组 + Flag IP-MS + CHX chase + Seahorse + EAT 模型 | Treg 稳定性 / 甲状腺细胞焦亡 | UBE2C 在 HT Treg 中下调；UBE2C–TRIM21 降解 NOS2 稳定 Treg | 体内 EAT 过继转移 | **疾病为桥本甲状腺炎，非甲状腺癌** | Medium（IM，**边界**） | 与 UBE2C⁺ ATC 样复发 FTC（Run #24）的连接为假设，未检验 |
| TAⅢ 脂质体载金诺芬诱导 ATC 铁死亡 | 42151086 / 10.3760/cma.j.cn112152-20250914-00459 | CAL-62 细胞 + 裸鼠异种移植 | 薄膜水化法制备；Fer-1 rescue；ACSL4/NCOA4/GPX4；Fe/GSH/脂质过氧化 | 铁死亡 / 体内抗肿瘤 | T-AUF-LPs 较常规脂质体粒径更小、摄取更高、显著诱导铁死亡 | 体外 + 异种移植 | 单一细胞系；无甲状腺癌临床标本；中文期刊 | Medium（ME） | 与已有铁死亡轴（HIF-1α–ACSL4、SLC7A11）未做机制连接 |
| PTMC 术前免疫细胞化学分层 | 待编目* / 10.30978/cees-2026-3-53 | 110 例 PTMC 前瞻对照 | CK17 + TPO + S 细胞三联术前面板 | 手术范围 / 区域转移 / 并发症 | 研究组按面板分层后个体化手术范围 | 前瞻对照（54 对照 / 56 研究） | 单中心；2024–2026；终点事件数可能不足 | Medium（PR） | CK17/TPO/S 细胞面板缺乏独立验证与标准化阈值 |

---

## 四、已知结论 (What Is Already Known)

1. **甲状腺癌"复发相关高危状态"的可重复核心是分化丧失，而非增殖**（Zenodo 存档，10.5281/zenodo.23319288）。该结论建立在 12 个已发表签名的基准比较、随机签名零校准与 family-wide FDR 控制之上，并含区室解析的 GeoMx 复核。**注意**：存档未经同行评审，应以其已公开的脚本自行复现后再采信。
2. **糖酵解受泛素化层级调控，且与 PTC 侵袭性直接耦合**：MIB2 经 RING 结构域介导 HK2 的 K48 连接多聚泛素化与蛋白酶体降解，抑制糖酵解通量与 PTC 侵袭（PMID 42847133）。
3. **肿瘤相关成纤维细胞是 PTC 中 IL-6 的主要来源**，缺氧经 ROS → NF-κB 驱动其分泌，旁分泌激活 PTC 的 MAPK；**已上市的 IL-6R 阻断剂托珠单抗在体内显著抑瘤**（PMID 42847132）。这使该轴成为本轮**最靠近临床再利用**的机制。
4. **MLLM 在甲状腺影像与细胞学上的能力被三条独立证据压低**：结构化临床特征单独输入即可达到与"图像+特征"相同的准确率（PMID 42744256）；6 款公开 MLLM 均低于资深放射科医师（PMID 42632527）；细胞学 Bethesda 分类准确率仅约 24–26%（PMID 42144078）。
5. **风险分层系统的"升级"不必然带来净获益**：ATA 2025 版区分度优于 2015 版，但同时上调了大量无复发患者的风险类别，绝对 NRI 为负（PMID 42844696）。
6. **ATC 一线化疗缺乏方案间差异证据**：卡铂/紫杉醇并不优于其他细胞毒方案（PMID 42046902）；手术仍与较低死亡风险相关。
7. **偶发甲状腺发现（ITF）构成大规模下游检查级联**：115,683 例影像人群中 7.8% 存在 ITF，其后续结节诊断与活检的 OR 分别达 45 与 46.8，但结节特征记录质量极差（PMID 42037237）。
8. **儿童/青少年 PTC 可经临床-基因组列线图改善分层**，且**合并桥本甲状腺炎是更差 DFS 的独立预测因子**（PMID 42857932）——这与"桥本保护性"的常见叙事方向相反。
9. **转移性 FTC 的原发灶切除与更长生存相关**（SEER，OS 70 vs 27 月；CSS 98 vs 47 月），但组间年龄差异提示选择偏倚未排除（10.1038/s41598-026-75182-z）。
10. **融合型 ATC 无法靠形态学识别，但 BRAF V600E 与 RAS Q61R 免疫组化双阴性可作为早期分子检测的分诊指征**（PMID 42470146）。

---

## 五、未解问题 (What Remains Unclear)

1. **已发表签名中究竟有多少能击败同等大小的随机基因集？** Zenodo 存档做了 12 签名的基准与零校准，但**逐条的胜出/落败清单未以论文形式公开**。这是当前最大的单点信息缺口。
2. **分化丧失轴与增殖轴在跨队列上谁更稳？** 存档给出方向性结论，但其对"分化评分"的定义、阈值敏感性、以及在不同平台（scRNA vs Visium vs GeoMx vs H&E 形态计量）间的一致性尚未被第三方检验。
3. **MIB2–HK2 轴与已有代谢轴的关系**：与 TRIM47–FBP1 乳酸化正反馈（Run #26）、ZFP57–PKM2（Run #24）、ECT2–硫辛酸（Run #23）是否共享下游节点？无人检验。**MIB2 也无任何预后层证据**。
4. **CAF–IL-6 轴的临床可迁移性**：托珠单抗在甲状腺癌中**没有任何临床队列验证**；缺氧-ROS 轴在人体肿瘤内的空间分布未知；PTC 中 CAF 的异质性亚群划分仍未做。
5. **CRABP1 的表观因果被作者本人否认**：启动子区总甲基化升高与基因体 cg02276974 甲基化的弱负相关（r=−0.2069, R²=0.0428）不足以支持"甲基化导致 CRABP1 下调"。**CRABP1 究竟是驱动因子还是分化状态的被动标记**未定。
6. **ATA 2025 的再分类净伤害是否可修复？** 驱动再分类的是"修订的多灶性标准"与"≥2 个低危特征"；删除或加权其中某项是否能保住 AUC 增益而消除 NRI 负值，尚未检验。
7. **桥本甲状腺炎在儿童 PTC 中究竟是风险因子还是保护因子？** 本轮（PMID 42857932）为风险方向，既有多项成人研究多为保护/无关方向。**年龄特异效应**未解。
8. **MLLM 的人机协作增益未知**：三条负结果都是"AI 单独 vs 人类单独"，**没有一个检验"人类 + AI 是否优于人类单独"**——而后者才是部署场景的真实问题。
9. **影像组学在合并桥本背景下的可迁移性**：本轮两篇（10.3389/fonc.2026.1840185、10.1002/jum.70419）均在 HT 背景下建模，但 HT 会改变实质回声与弹性，**模型跨 HT 状态是否稳定**未检验。
10. **转移性 FTC 的选择偏倚**：PTR 组显著更年轻（65.2 vs 70.3 岁），PSM 后匹配队列变小；**FTC 的组织学亚型（minimally invasive vs widely invasive）未分层**是主要混淆源。

---

## 六、领域方法/数据局限 (Method/Data Limitations In The Field)

1. **签名与模型的"零校准"普遍缺失**。本轮 Zenodo 存档是 29 轮以来第一个系统做随机签名零校准的工作——这反衬出**绝大多数已发表签名从未与随机基因集比较过**。Run #28 已发现"分子变量跨中心增量不一致"，本轮从方法学层面给出了更根本的解释：可能这些签名本就不比随机好。
2. **单中心、内部拆分式验证仍是主流**。本轮 AL 维度 17 条中，至少 5 条（10.3389/fonc.2026.1840185、10.21037/gs-2026-0143、10.1097/md.0000000000050126、10.1002/jum.70419、10.1210/clinem/dgag418）**只有 7:3 随机拆分或交叉验证，无地理外部验证**。DCE-US 组学与 C-TIRADS 组学尤其典型。
3. **回顾性设计高估 AI 性能**。AI-UADS（AUC 0.933 vs 医师 0.821）采用回顾性病例对照，且"高年资超声医师"的年资未量化——这是**选择偏倚 + 对照设置偏弱**的组合。
4. **模型版本漂移（version drift）**。本轮 3 篇 LLM 论文分别使用 ChatGPT-5.4、Gemini 3.1 Pro、Claude Opus 4.6 等**具体版本**；结论在 6–12 个月内即可能失效。综述（PMID 42667959）已明确指出 LLM"未被批准用于诊断且易产生虚构引用"。
5. **流程依赖性是可重复性隐患**。可变剪接分类研究（PMID 42296790）明确显示"分类质量强烈受处理流程影响"（TAC vs EventPointer 差异显著，准确率 0.938 只在 TAC 路径下得到）——提示**同一份数据、不同流程可得到不同结论**。
6. **阴性结果的发表仍不充分但正在改善**。本轮 4 条明确负结果（ATC 化疗无差异、ATA 2025 绝对 NRI 为负、MLLM 图像无增量、多模态超声增量仅 +0.018）是 29 轮以来密度最高的一次，但均未见预注册的阴性分析计划。
7. **区室混用问题本轮未改善**（连续第三轮）。无一篇明确区分同一基因在 malignant epithelium / myeloid / fibroblast / 正常甲状腺滤泡细胞中的来源。Zenodo 存档做了"区室解析的 GeoMx 校验"，是唯一正面示例。
8. **空间组学维度仍极低产**（SP 仅 1 条且为数据集存档）。Run #28 提出的"全库普查以判定是真低产还是欠采样"**尚未执行**——本轮因 NCBI 不可达也未推进。
9. **预印本与数据集型存档的降档口径需统一**。本轮严格预印本 1 条（Research Square），另含 1 条 Zenodo 数据集存档（H1，本轮最强条目）。二者**都不应等同同行评审论文**，但 Zenodo 存档的脚本透明度又高于多数论文——需要在报告中明确分层而非简单降档。
10. **通道污染回升**。Europe PMC 的 `LIPID` 路 27 候选中绝大多数为 MASLD / 甲状腺-肝轴；`AI` 路 31 候选中大量为甲状腺眼病。Run #27 为 `ME` 路加的 carcinoma/cancer 约束有效，**但同类约束尚未推广到 `LIPID` 与 `AI` 路**。

---

## 七、候选未来方向 (Candidate Future Directions)

按 `research-direction-rubric.md` 七维评分（各维 1–5，总分 7–35；**28–35 为强候选**）。**评分口径：Run #27 起按七维明细逐项求和**，跨轮比较请以重算值序列为准。

| 方向 | N 新颖 | F 可行 | D 数据 | V 验证 | C 临床 | M 严谨 | O 反拥挤 | **总分** | 状态（相对 Run #28） |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| **D26 签名与模型的可信度审计（null calibration + benchmark arena）** | 4 | 5 | 5 | 4 | 4 | 5 | 5 | **32** | 🆕 本轮新立，**本轮最高** |
| **D15 去分化 / ATC 轨迹** | 4 | 5 | 5 | 4 | 5 | 5 | 3 | **31** | ⬆️ 26 → **31**，本轮强化最强 |
| **D13 算法：从"造模型"到"嵌流程 / 评人 / 评公平"** | 4 | 5 | 5 | 4 | 5 | 4 | 3 | **30** | ⬆️ 29 → **30**，三条负结果到位 |
| **D21″ 脂代谢重编程 × 免疫生态位 × 获得性耐药（跨区室整合）** | 4 | 5 | 5 | 4 | 4 | 4 | 3 | **29** | ➡️ 维持（本轮无直接新证据） |
| **D27 偶发甲状腺发现（ITF）的过度诊断级联与分诊** | 4 | 4 | 4 | 3 | 5 | 4 | 4 | **28** | 🆕 本轮新立 |
| **D13-M 多模态 radiopathomics** | 4 | 5 | 4 | 4 | 4 | 4 | 3 | **28** | ➡️ 维持（本轮 3 篇但均无外部验证） |
| **D18 代谢–耐药轴** | 4 | 4 | 4 | 4 | 5 | 4 | 3 | **28** | ➡️ 维持（MIB2–HK2 为代谢侧新节点） |
| **D12′ 铁死亡–免疫逃逸耦合** | 4 | 4 | 4 | 4 | 4 | 4 | 4 | **28** | ➡️ 维持（TAⅢ/AUF 脂质体新增给药层） |
| **D8 肿瘤微环境（CAF/TAM）极化全景** | 3 | 5 | 4 | 4 | 5 | 4 | 3 | **28** | ⬆️ 24 → **28**，托珠单抗提供再利用切口 |
| **D20 儿童/AYA PTC** | 3 | 4 | 4 | 3 | 5 | 4 | 4 | **27** | ⬆️ 25 → **27**（435 例列线图） |
| **D25 生成式虚拟成像（V-EUS / 硬件无关弹性成像）** | 5 | 4 | 3 | 4 | 4 | 3 | 4 | **27** | 🆕 本轮新立 |
| **D11 EMT / 去分化轨迹的亚群特异通路** | 4 | 4 | 4 | 3 | 3 | 4 | 4 | **27** | ⬆️ 26 → **27**（CRABP1 + 分化丧失轴） |
| **D16 MTC / 远处转移** | 3 | 4 | 3 | 3 | 4 | 4 | 4 | **26** | ⬆️ 25 → **26**（转移性 FTC PTR） |
| **D9″ SPP1 髓系来源的空间共定位与区室解耦** | 4 | 4 | 4 | 4 | 4 | 4 | 2 | **26** | ➡️ 维持（本轮无新证据） |
| **D17 肠道/瘤内微生物群** | 4 | 4 | 4 | 3 | 3 | 3 | 3 | **24** | ➡️ 维持（本轮无新证据） |
| **D24 复发性颈部 LNM 的微创局部治疗分层** | 3 | 3 | 4 | 3 | 5 | 3 | 2 | **24** | ⬆️ 23 → **24**（RLN 刮除 meta） |
| **D3″ APOE × MGST1 代谢–免疫干性亚群** | — | — | — | — | — | — | — | **归档** | ❌ 终判阴性，见 §11.3 |

### 方向要点（Top 3）

**D26 签名与模型的可信度审计（null calibration + benchmark arena）— 32**
- **Research question**：在甲状腺癌中，已发表的复发/LNM/预后签名与影像组学模型，**有多少能真正击败同等大小的随机基因集 / 随机特征集**？分化丧失轴是否在其中胜出？
- **Novelty angle**：本轮 Zenodo 存档是本领域首个零校准工作，但它只覆盖"复发相关高危状态"一个终点，且**未把该方法推广到 LNM 签名与 ML/影像模型**（后者本轮有 17 条新文，全部无零校准）。
- **Required datasets**：Zenodo 10.5281/zenodo.23319288（53 个 MIT 脚本 + 全部派生表，**本轮即可 fork**）、TCGA-THCA、GEO（GSE60542 / GSE193581 / GSE29265 / GSE33630）、cBioPortal、LymphUs（338 例淋巴结超声，gold OA）。
- **Expected endpoint**：签名的跨队列 C-index / AUC 与其随机对照零分布的位置（empirical p 值），以及"模型性能 − 随机基线"的效应量分布。
- **Analysis strategy**：① fork 存档脚本，复现 12 签名基准；② 把随机签名零校准扩展到 LNM 签名（CENPM、CRABP1、MIB2 等本轮新标志物）与至少 5 个公开影像组学/ML 模型；③ 用 family-wide FDR 控制多重比较；④ 输出"签名可信度分级的公开表"。
- **Validation plan**：发现队列 TCGA-THCA → 跨队列 GSE 系列 → 影像模型部分用 LymphUs 做地理外部验证。
- **Major risk**：结论可能"得罪"整个领域（多数签名落败），投稿阻力大；且随机对照的构造方式（是否匹配基因长度、表达量、共表达结构）本身可争议。
- **Claim boundary**：**不可声称"某签名无效"**——只能声称"在 X 队列、Y 终点、Z 零模型下，该签名的跨队列性能与随机对照的差异为 W（empirical p = …）"。

**D15 去分化 / ATC 轨迹 — 31**
- **Research question**：去分化（甲状腺分化丧失）作为复发高危状态的**因果驱动 vs 被动标记**，能否在空间与区室层面被区分？
- **Novelty angle**：本轮 Zenodo 存档把"分化丧失"推到核心位置，但**没有做空间区室的因果分离**；同时 ATC 化疗阴性结果（PMID 42046902）打开了"替代治疗策略"的必要性。
- **Required datasets**：Zenodo 存档（含空间转录组处理 + GeoMx 区室解析代码）、TCGA-THCA（含 TDS 分化评分）、GSE193581（成人 PTC scRNA）、ATC 公开 scRNA。
- **Expected endpoint**：无复发生存 + 分化评分（TDS）的区室特异效应。
- **Analysis strategy**：① 用存档的 53 脚本重建分化轴；② 在 GeoMx/Visium 上做区室解析（恶性上皮 vs 基质 vs 免疫）；③ 检验 BRAF/RAS/TERT 驱动突变作为协变量时分化轴是否仍独立；④ 与 CRABP1（本轮新分化相关标志物）做共变分析。
- **Validation plan**：至少 2 个独立 scRNA 队列 + TCGA 生存层 + 空间区室复核。
- **Major risk**：分化评分定义不统一（不同研究 TDS 基因集不同）导致结论无法对齐。
- **Claim boundary**：**不可声称"去分化导致复发"**——只能声称"在控制驱动突变后，分化评分在 Y 区室仍与复发独立相关"。

**D13 算法：嵌流程 / 评人 / 评公平 — 30**
- **Research question**：甲状腺 AI 模型在**跨中心迁移、人机协作增益、部署净获益**三个环节上各自失败于何处？
- **Novelty angle**：本轮三条独立负结果（图像无增量、人类优于全部 MLLM、细胞学 24–26%）+ ATA 2025 的绝对 NRI 为负，共同指向"**性能提升 ≠ 净获益**"这一可量化命题；但**无人检验人机协作增益**。
- **Required datasets**：LymphUs（gold OA）、本轮三套 MLLM 评测所用的公开超声集、ATA 2015/2025 可复现分层规则（n=1508 队列需自建）。
- **Expected endpoint**：① 模型在地理外部队列的性能衰减幅度；② **人类 + AI 相对人类单独的 ΔAUC/Δκ**（核心缺口）；③ 再分类的绝对 NRI（而非仅 AUC）。
- **Analysis strategy**：① 复现 ATA 2015 vs 2025 的 NRI 分析框架；② 用 LymphUs 做跨中心域偏移基线；③ 设计 reader study，包含"医师单独"与"医师 + AI 建议"两臂（**本轮文献无人做第二臂**）。
- **Validation plan**：≥3 名不同年资医师 × ≥2 个外部中心。
- **Major risk**：超声 AI 已高度拥挤（O=3）；必须靠"评模型/评协作"而非"造模型"建立差异；LLM 版本漂移使结论保质期短。
- **Claim boundary**：**不可声称 AI 优于医师**——本轮证据方向相反；只能声称"在 X 队列上，人机协作相对人类单独的增益为 Y，且在 Z 亚组中……"。

---

## 八、推荐下一步方向 (Recommended Next Direction)

### 首选：D26 签名与模型的可信度审计（rubric 32）

**理由**：本轮最强条目（Zenodo 存档）**已经把引擎做出来并公开**（53 个 MIT 脚本 + 全部派生表，CC BY 4.0），因此这是 29 轮以来**启动成本最低、新颖度最高、方法学最严谨**的方向——零湿实验、零申请、当天即可 fork 复现。同时它直接回应了本轮暴露的领域级缺陷：AL 维度 17 条新文**全部没有零校准**，而 Run #28 已发现"分子变量跨中心增量不一致"——D26 能给出根本性解释。

**首批具体步骤（全部无需湿实验）**：
- **M0 复现（1–2 天）**：clone `10.5281/zenodo.23319288`，按 `docs/DATA_SOURCES.md` 与 `docs/` 的运行顺序复现 12 签名基准与随机签名零校准，确认 family-wide FDR 输出可重得。**这一步同时是对该存档可信度的检验**（它未经同行评审）。
- **M1 扩展到 LNM 签名**：把零校准框架套用到本轮与历史轮次出现的 LNM 标志物签名（CENPM、CRABP1、MGST1、MIB2、APOC1 等），输出"哪些 LNM 签名优于随机"的量化表。
- **M2 扩展到影像/ML 模型**：对至少 5 个公开甲状腺影像组学 / ML 模型做**随机特征对照**（匹配特征数量与边际分布），检验其在外部队列上的增量是否显著大于零模型。首批用 LymphUs（gold OA）。
- **M3 分化轴的跨队列胜出检验**：检验"分化丧失"轴是否在跨队列上真正优于 12 个已发表签名（此步与 D15 合并执行）。
- **M4 公开产物**：输出一份"甲状腺癌签名/模型可信度分级表"（含 empirical p 值、效应量、所用零模型定义），作为社区可引用的基准。

**所需数据集**：Zenodo 10.5281/zenodo.23319288（MIT/CC BY 4.0）、TCGA-THCA、GSE60542 / GSE193581 / GSE29265 / GSE33630、cBioPortal、LymphUs（PMID 41940127，gold OA）。

**验证要求**：至少 2 个独立 scRNA/bulk 队列 + TCGA 生存层；影像部分需**地理外部验证**，不可用内部随机拆分充数。

**应避免的主张**：
- 不得声称"某签名无效"或"某研究造假"——只能报告在特定零模型下的经验 p 值与效应量。
- 不得把 Zenodo 存档的结论当作已同行评审的事实直接引用；**必须先自行复现**。
- 不得把不同区室（恶性上皮 / 髓系 / 基质）的签名评分为单一分数合并报告。

### 并行第二赛道：D15 去分化 / ATC（rubric 31）
与 D26 **共享数据骨架**（Zenodo 存档 + TCGA + GSE193581），M3 即为两者的交汇点，建议作为同一执行路线的两个输出。

---

## 九、随访阅读清单 (Follow-Up Reading List)

**必读（Tier 1）**
1. **10.5281/zenodo.23319288** — 复发相关高危状态 = 去分化程序。**为什么读**：本轮唯一做了随机签名零校准的工作，且代码全公开；是 D26/D15 的引擎。优先读 `docs/DATA_SOURCES.md` 与 `docs/` 运行顺序。
2. **PMID 42847133（10.1530/erc-26-0049）** — MIB2–HK2 泛素化–糖酵解。**为什么读**：本轮机制侧因果链最完整，且开辟"泛素化 → 代谢 → 侵袭"三层连接。
3. **PMID 42847132（10.1530/erc-26-0198）** — CAF 缺氧 ROS/NF-κB/IL-6 + 托珠单抗。**为什么读**：唯一有已上市药物可立即再利用的轴，可直接设计临床前验证。
4. **PMID 42844696（10.1177/10507256261494916）** — ATA 2015 vs 2025，绝对 NRI −22.6%。**为什么读**：提供了"区分度 ≠ 净获益"的标准化分析框架（AUC + NRI + DCA），可直接复用于任何新风险模型。
5. **PMID 42744256（10.1053/j.sult.2026.09.001）** — ChatGPT-5.4 TI-RADS。**为什么读**：features-only = image+features 是本轮最锋利的负结果，直接质疑 MLLM 多模态价值。

**应读（Tier 2）**
6. **PMID 42857932（10.1210/clinem/dgag418）** — CAYA-PTC 临床基因组列线图。**为什么读**：435 例多中心，且提出"桥本甲状腺炎 = 风险因子"这一反直觉结论。
7. **10.3389/fcell.2026.1974822** — CRABP1 甲基化。**为什么读**：**主张边界写作的范本**——作者主动声明表观因果未确立，值得作为本项目 claim boundary 的模板。
8. **PMID 42046902（10.1210/clinem/dgag177）** — ATC 一线化疗阴性结果。**为什么读**：158 例 7 中心，是本轮唯一高质量阴性治疗证据。
9. **PMID 42037237（10.1210/clinem/dgag186）** — ITF 级联，n=115,683。**为什么读**：规模空前的过度诊断实证，且提供了可复用的 NLP 抽取管线设计。
10. **PMID 42805865（10.1016/j.acra.2026.09.019）** — DD-GAN 虚拟弹性成像。**为什么读**：唯一做了内部 + 外部 + 前瞻三套验证的甲状腺 AI 论文，且开辟"生成式替代硬件"新赛道。

**选读（Tier 3）**
11. PMID 42632527 — 6 款 MLLM 对比（含放射科医师基准）。
12. PMID 42144078 — MLLM 细胞学（26.2%/23.6%，边界警示）。
13. PMID 42296790 — 可变剪接分类的流程依赖性（可重复性警示）。
14. PMID 42470146 — ATC 激酶融合的 IHC 分诊规则（可直接落地）。
15. 10.1038/s41598-026-75182-z — 转移性 FTC 原发灶切除（读其 PSM 与偏倚讨论）。

---

## 十、可复现性说明 (Reproducibility Notes)

- **Search date**: 2026-10-16（UTC+8），TS = `20261016_030414`
- **Databases**: OpenAlex（主）、Europe PMC（第二通道，12 路）、Crossref（DOI 校验）、OpenAlex 定向基因深挖（第三通道，42 基因面板）
- **Query strings**:
  - `oa_search.py` 内建九路布尔矩阵（维度 a–i），见脚本 `DIM_LABEL`；本轮 `--days 30 --per-page 25` 与 `--days 90 --per-page 50` 各跑一次
  - Europe PMC 12 路键见 `_epmc_run29.py` 的 `QS` 字典；Run #29 对 `LIPID` 补入 LPL/VLDLR/CD36、对 `AI` 补入 agentic/multimodal
  - 深挖面板 42 基因见 `_deep_run29.py` 的 `GENES`；Run #29 新增 CRABP1 / HK2 / CTSS / MIB2 / TCF4 / XPR1 / ACBD7 / METTL7B / TMED2 / DGKB
- **Filters**: OpenAlex `sort=publication_date:desc`（**不用 relevance**），`from_publication_date`；Europe PMC `PUB_YEAR:2026` + `sort=P_PDATE_D desc`
- **Deduplication rule**: 以 **DOI（小写）** 为主键，**归一化标题**（去非字母数字，截 90 字符）与 **PMID** 为辅键，三者任一命中基线即判重；同一论文的多个 OpenAlex 版本记录由 `oa_search.py` 按归一化标题合并
- **Screening rule**: `in_scope_thyroid = True`（要求标题点名甲状腺且整体为肿瘤主题）；撤稿/更正/补充材料/会议摘要/ASO Visual Abstract 人工降档；预印本（`type=preprint`）与数据集存档（Zenodo/figshare）单独标注并按 deposit 降档
- **Channel probe**: 每通道 `curl --noproxy '*' --max-time 20`，结果见 §1.1（**NCBI eutils 本轮 HTTP 000，不可用**）
- **Files saved**:
  - `search_results_20261016_030414.json`（累积基线 559）/ `search_results_latest.json`（同）
  - `search_results_20261016_030414_new.json`（本轮 32 条新增）
  - `search_results_20261016_030414_30d.json`（30 d 窗口，86 条）
  - `search_results_20261016_030414_90day.json`（90 d 窗口，251 条）
  - `search_results_20261016_030414_epmc.json`（Europe PMC 12 路候选）
  - `search_results_20261016_030414_deep.json`（42 基因深挖）
  - `search_results_20261016_030414_keyabs.json` / `_keyabs_b.json`（关键文献摘要）
  - `search_results_20261016_030414_enrich.json`（Crossref 校验，9/10 成功）
  - `search_results_latest_backup_run28.json`（Run #28 基线备份）
  - 脚本：`_epmc_run29.py`、`_deep_run29.py`、`_keyabs_run29.py`、`_final_run29.py`（未入库，同 `_build_*` 惯例）

---

## 十一、与历史报告的差异 (Delta vs Previous Runs)

### 11.1 本轮新增 vs Run #28（基线 527 → 559）

| 项 | Run #28 | **Run #29** | 变化 |
|---|---:|---:|---|
| 去重后唯一新增 | 70 | **32** | −38 |
| 通道构成 | OpenAlex 15 / EPMC 50 / 深挖 5 | OpenAlex 14 / EPMC 15 / 深挖 3 | EPMC 占比下降 |
| High / Medium / Low | 17 / 34 / 19 | **2 / 21 / 9** | High 大幅下降 |
| 严格预印本 | 2 | **1** | — |
| 无 PMID | 15 | **12** | 无法回填（NCBI 不可达） |
| 空间组学 SP | 1 | **1**（数据集存档） | 持平 |
| 单细胞 SC | 2 | **1** | 持平 |

### 11.2 关于「新增数腰斩」的判定 —— **不是领域平台期**

三条独立证据支持该判定：
1. **90 d 窗口零增量**：OpenAlex 90 d 251 条中，相对基线**无一条新**——说明 Run #26–#28 的历史欠采样回填**已经完成**。增量来源从"回填历史"切换为"当期新发"，数量自然回落。
2. **本轮 32 条中 30 条发表于 2026-08 之后**，且 10 月新文 9 条 → 属真实当期产出，非窗口问题。
3. **High 数量下降（17 → 2）是评分口径收敛的结果**：Run #28 的 17 条 High 中有大量为历史回填的高质量论文；本轮 High 仅 2 条，但**这两条的质量高于 Run #28 的多数 High**（一条是方法学基础设施，一条是完整因果链）。

**结论**：本轮是**检索体系成熟后的正常当期产出节奏**，不是领域停滞，也不是通道故障。**下轮调整建议**：
- ① 维持三通道，但**降低 Europe PMC 与深挖通道的配额**（本轮可用率显著下降，污染回升）。
- ② 为 Europe PMC 的 `LIPID` 与 `AI` 路补加 `TITLE:"carcinoma" OR TITLE:"cancer"` 约束（Run #27 为 `ME` 路加此约束已验证有效）。
- ③ 空间组学维度**执行全库普查**（Run #28 提出但连续两轮未执行），配置 SP 判定。
- ④ 若 NCBI 恢复，优先跑一次 `_pmid_backfill_ncbi.py` 回填本轮 12 条缺号记录。

### 11.3 持续跟踪方向状态：D3″（APOE × MGST1 代谢–免疫干性亚群）

**状态：❌ 维持归档（终判阴性），第 29 轮，无变化。**

本轮复检量化事实（OpenAlex 全库，2026-10-16）：

| 查询 | 命中总数 | 本轮新增 |
|---|---:|---:|
| `MGST1 × thyroid` | **1** | **0**（连续第 4 轮零增长） |
| `APOE × thyroid`（2026） | 9 | 3（均为非肿瘤：瑞司美替罗动脉粥样硬化、APOE 与甲状腺功能障碍的心血管代谢研究、呼吸-肌肉骨骼共病） |
| `APOE × MGST1 × thyroid` | **0** | **0** |

**结论不变**：以 MGST1 作为该代谢–免疫轴的锚点是**错误先验**。Run #28 已完成终判并归档，本轮复检**再次确认**。残余价值（APOE 的三区室拆分问题）已并入 D21″。**MGST1 不再投入任何检索或分析资源。**

**同时确认**：Run #28 提出的"本轮最强方向 D21″（脂代谢 × 免疫生态位）"在本轮**未获直接新证据**（MIB2–HK2 为糖酵解侧、TAⅢ/AUF 为铁死亡侧，均非脂代谢核心），D21″ 维持 29 分但**状态由"本轮强化"降为"维持"**。

### 11.4 相对上次的新信号 / 方向变化

| 变化 | 说明 |
|---|---|
| 🆕 **"证伪/校准"成为本轮主导信号** | 29 轮以来第一次出现**一组彼此独立的负结果与零校准工作**（Zenodo 零校准、ATA 绝对 NRI 为负、MLLM 图像无增量、ATC 化疗无差异、多模态超声增量 +0.018）。这不是偶然——Run #28 已观察到"分子变量跨中心增量不一致"，本轮从方法学层面给出了机制性解释。 |
| 🆕 **D26（32）与 D25（27）两个新方向** | 均由本轮的负结果/生成式方法直接催生。 |
| ⬆️ **D15 由 26 升至 31** | Zenodo 存档把"分化丧失"确立为复发高危状态的可重复核心，配合 ATC 化疗阴性结果。 |
| ⬆️ **D8 由 24 升至 28** | CAF–IL-6 轴 + 托珠单抗提供**已上市药物再利用**切口，是 29 轮以来 D8 最接近临床可执行的一次。 |
| ⬆️ **D13 由 29 升至 30** | 三条 MLLM 负结果 + ATA NRI 负值为"评模型"范式提供了决定性弹药。 |
| ⚠️ **D21″ 状态降级** | 由"本轮强化"→"维持"，本轮无脂代谢核心新证据。 |
| ⚠️ **NCBI 通道第二次反转** | Run #28 补充时恢复（3/3 200）→ 本轮再次不可达（000）。**通道状态的时变性再次被证实**。 |
| ➡️ **D12′ / D18 / D13-M / D9″ / D17 维持** | 无方向性变化。 |

---

## 十二、代码仓同步结果 (Repository Sync)

| 步骤 | 命令 | 结果 |
|---|---|---|
| 拉取 | `git pull --rebase --autostash origin main`（绕过沙箱，SSH `ConnectTimeout=20`） | ✅ **第 1 次尝试成功**：`Already up to date.` |
| 分支跟踪 | `git status -sb` | ✅ `## main...origin/main`，跟踪关系正常 |
| 提交文件 | 见下方 | 见下方 |
| 推送 | `git push origin main`（绕过沙箱） | 见最终回复 |

**本轮提交文件清单**：
- `lit_review/literature_review_20261016_030414.md`（本双语报告）
- `lit_review/search_results_20261016_030414.json`（累积基线 559）
- `lit_review/search_results_latest.json`（同 559）

**未提交**（按协议剔除）：`_epmc_run29.py`、`_deep_run29.py`、`_keyabs_run29.py`、`_final_run29.py` 及历轮 `_build_*` / `_enrich_*` / `_run2*.py` 一次性脚本、`analysis/`、`D3_D9_*.md`。提交前已用 `git status --porcelain` 核对暂存区仅含上述三个文件。

---

## 十三、通道状态变更记录（本轮新增章节 / Channel State Change Log）

| 日期 / Run | 通道 | 变更前 | 变更后 | 触发动作 |
|---|---|---|---|---|
| 2026-08 | NCBI eutils / GEO / FTP | ✅（默认） | ❌ 4/4 HTTP 000 | 改为"GEO 一律转 ENA" |
| 2026-10-09（Run #28 补充） | NCBI 全域 | ❌ | ✅ 3/3 HTTP 200；FTP 下载 27.5 MB / 17.6 s | 改回"首选 NCBI FTP"；建 `_pmid_backfill_ncbi.py` |
| **2026-10-16（Run #29）** | **NCBI eutils** | ✅ | ❌ **HTTP 000（15.1 s，绕过代理）**；带代理亦 000（0.15 s 立即拒连） | 曾判定"无法做 PMID 回填"；12 条标「待编目*」 |
| 2026-10-16（Run #29） | Crossref | ⚠️ Run #28 超 20 min 未完成 | ✅ 200 / 1.39 s，9/10 DOI 校验成功 | 维持"只跑 High/关键 Medium（≤10）+ timeout 10 s" |
| **2026-10-17（补充）** | **NCBI eutils** | ❌（**误判**） | ✅ **根因为 Schannel 吊销检查**，`--ssl-no-revoke` 或 Python urllib 均 **200 / <1 s** | **已补跑回填，19 条定号**；写入环境文档 |
| **2026-10-17（补充）** | **Unpaywall** | ⚠️ 曾记录"变慢" | `/v2/search?query=` **410 Gone = 端点官方下线**（非故障）；`/v2/<doi>` **200 / 0.81 s** | 改用单 DOI 端点 |

> **核心教训（第三次，且为根因级）**：前两次只观察到「时变」的表象，第三次才抓到真实错误码。
> 固化两条规则：① 通道状态**每轮必测**；② 失败时必须抓**真实 error**（`curl -sS`，而非只看 `%{http_code}`），
> **先分层判定 DNS / TLS / 网络再下"不可达"结论——`000` 不等于封网**。

---

## 附录 C：2026-10-17 PMID 补充回填 / Appendix C — PMID Backfill (2026-10-17)

> 本附录为 Run #29 报告发布**之后**的补充动作，起因是 §1.1 所述的根因订正。

### C.1 为什么现在能跑 / Why now

Run #29 判定「NCBI 不可达 → 无法回填」。2026-10-17 抓真实错误后确认该判定为误判，
真实根因是 **Windows Schannel 证书吊销检查**（`CRYPT_E_REVOCATION_OFFLINE`），
**Python `urllib` 走 OpenSSL、默认不做吊销检查，天然规避该问题**。
因此回填无需等待任何"通道恢复"，随时可执行。

### C.2 执行参数 / Execution

| 项 | 值 |
|---|---|
| 脚本 | `_pmid_backfill_run29b.py`（新建，替代旧 `_pmid_backfill_ncbi.py`） |
| 主标识 | DOI → `esearch <doi>[DOI]` |
| 回退 | 标题 `[Title]` 检索 + `esummary` 取真实标题，`difflib` 相似度 **≥ 0.88** 才采信 |
| 速率 | 无 key 时 0.4 s 间隔；**HTTP 429 退避 3 / 6 / 12 s**（真实限流，非故障） |
| 跳过规则 | `preprints / rs.3.rs- / zenodo / figshare / ssrn / biorxiv / medrxiv / researchsquare / inplasy` 等无 PMID 类型 |
| 回滚备份 | `search_results_latest_pre_backfill_20261017.json` |
| 耗时 | 3 min 59 s |

### C.3 结果 / Result

| 指标 | 数值 |
|---|---|
| 基线总量 | 559 |
| 回填前无 PMID | 150 |
| **本轮成功定号** | **19**（全部经 DOI 命中；标题回退 0 —— 相似度门槛生效，无误配） |
| 按规则跳过（预印本/数据集/方案注册） | 27 |
| 回填后仍无 PMID | **131**（其中大量为会议摘要、protocol、掠夺性期刊、极新文献） |

**19 条新定号明细（PMID | 发表日 | DOI | 标题）**

| PMID | 发表日 | DOI | 标题 |
|---|---|---|---|
| 42855402 | 2026-09-01 | 10.1016/j.surg.2026.110658 | Metabolic reprogramming in differentiated thyroid cancer |
| 42866447 | 2026-09-01 | 10.21037/gs-2026-0288 | Synchronous medullary and papillary thyroid carcinoma … |
| 42866471 | 2026-09-01 | 10.21037/gs-2026-0281 | Treatment strategies for unilateral papillary thyroid carcinoma … |
| 42866849 | 2026-09-01 | 10.21037/gs-2026-0333 | Prognostic factors in thyroid cancer with lung-only metastasis |
| 42870783 | 2026-09-01 | 10.21037/tcr-2026-1440 | Multi-omics analysis of GBP2 as a prognostic and immune-related biomarker |
| 42870788 | 2026-09-01 | 10.21037/tcr-2026-1398 | Analysis and validation of prognostic markers for thyroid … |
| 42876525 | 2026-09-30 | 10.3389/fendo.2026.1887201 | Prediction of early postoperative hypocalcemia and hypoparathyroidism |
| 42865346 | 2026-09-28 | 10.3389/fendo.2026.1866805 | Machine learning-based prediction of lymph node metastasis in PTC |
| 42865479 | 2026-09-28 | 10.3389/fendo.2026.1922413 | Anatomical location matters: risk modelling and surgical outcomes |
| 42870829 | 2026-09-29 | 10.3389/fendo.2026.1917885 | Prediction of gross extrathyroidal extension in PTC |
| 42876643 | 2026-09-30 | 10.3389/fonc.2026.1895987 | Two-year dynamic risk stratification and adjuvant radioiodine efficacy |
| 42814254 | 2026-09-30 | 10.1245/s10434-026-20503-9 | ASO Visual Abstract: 2015 vs 2025 ATA Risk Stratification |
| 42820252 | 2026-10-01 | 10.1177/00031348261494195 | The Price of Less Surgery: Completion Thyroidectomy After Lobectomy |
| **42875362** | 2026-10-01 | 10.1016/j.ultrasmedbio.2026.09.018 | Deep Learning-Driven US+CT for Central LNM in PTC |
| **42862325** | 2026-10-12 | 10.1007/s00011-026-02375-7 | UBE2C–TRIM21-driven NOS2 degradation stabilizes Tregs（HT） |
| 42882098 | — | 10.3390/jcm15197636 | Spatial Transcriptomics in Thyroid Cancer: PRISMA-style review |
| 42837078 | — | 10.1007/s13304-026-02875-5 | Recurrence patterns and survival in advanced PTC |
| 42597226 | — | 10.62347/qhyg5969 | （标题缺失） |
| 42296790 | 2026-06-06 | 10.1016/j.cmpb.2026.109506 | Alternative splicing variants incorporation strategies |

> 加粗两条为本报告正文/证据矩阵中已同步更新的条目。

### C.4 对 Run #29 结论的影响 / Impact

- **不改变**任何科学结论、方向评分或证据强度判定——仅补齐标识符。
- 报告正文与证据矩阵中仍标「**待编目\***」的 15 处，含义已明确为
  **「截至 2026-10-17 PubMed 尚未收录」**，而非"检索失败"或"通道不可用"。
- 其中 `10.5281/zenodo.23319288`（数据集）、`10.21203/rs.3.rs-11024915/v1`（预印本）、
  `10.37766/inplasy2026.10.0046`（方案注册）**本质上不会有 PMID**，属预期状态。
- 其余多为 2026-10-08 之后见刊的极新文献（如 CRABP1、FTC 原发灶切除、DCE-US 组学），
  PubMed 编目滞后属正常，建议 **下轮（Run #30）开局优先重跑一次回填**。

### C.5 后续建议 / Next

1. 下轮自动化第 3 步后，直接调用 `_pmid_backfill_run29b.py`（urllib 版），
   **不再依赖"NCBI 是否可达"的前置判断**。
2. 所有 `curl` 探针/抓取一律加 **`--ssl-no-revoke`**。
3. Unpaywall 只用 `/v2/<doi>` 单 DOI 端点（`/v2/search` 已 410 下线）。
