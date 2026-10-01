# D9″ 空间耦合预研方案：SPP1⁺/APOC1⁺ TAM × 代谢–免疫干性亚群 (D9″ Spatial Coupling Pre-Research)

> 延续 Run #26（2026-10-02）文献监测报告之「推荐下一步方向 / Recommended Next Direction」。
> 报告首选方向 **D9″（rubric 28，强候选）**：在甲状腺癌中量化 SPP1⁺/APOC1⁺ TAM 生态位与 APOE/MGST1 代谢–免疫干性亚群的空间耦合。
> 生成日期：2026-10-02 ｜ 数据源：Europe PMC fullTextXML（全文实证）／OpenAlex／ENA／CELLxGENE／NGDC-GSA／GitHub API（可得性实测）
> 姊妹方案：`D9_preresearch_spp1_trem2_colocalization.md`（Run #22）、`D3_D9_spatial_anchor_preresearch.md`（Run #23）。**本方案取代二者对空间数据可得性的乐观假设。**

---

## 0. 本轮最关键的三个实证发现（推翻/修正既有前提）

### 0.1 ⭐ 发现一：26 轮的「APOE 共测空白」在**髓系层面被首次打破**

iScience 儿童 PTC 队列（`10.1016/j.isci.2026.116560`，PMC13378368，gold OA）原文：

> "Macro2 can be defined by the expression of **SPP1, APOC1, and APOE**, and showed high activity in **cholesterol homeostasis, epithelial-mesenchymal transition (EMT), KRAS, PI3K-AKT-MTOR** pathways, which promoting tumor cell migration and invasion."

**意义**：这是全部 26 轮监测中，**第一篇在同一细胞亚群中同时测量 SPP1、APOC1 与 APOE** 的文献。D3″ 长期依赖的「APOE 与 SPP1 从未被共同测量」这一前提**不再成立**。

- ✅ APOE 侧：首次获得与 SPP1⁺ TAM 共定位的**直接单细胞证据**，D9″ 与 D3″ 由此合并为同一可执行问题。
- ❌ MGST1 侧：该文 MGST1 提及数 = **0**；OpenAlex 全库 `APOE`×`MGST1`×`thyroid` 三词共现仍 = **0**。MGST1 孤岛**未被打破**。
- ⚠️ 重要修正：该 Macro2 的 APOE 表达位于**髓系（巨噬） compartment**，而非 Run #21–#25 假设的**癌细胞 compartment**。D3′/D3″ 原假设的「APOE 高表达肿瘤亚群」（Discover Oncology, PMID 42217128）与此是**不同细胞类型**——两者必须在分析中分开报告，**不得混为一谈**。

### 0.2 ⭐ 发现二：JCI Insight 图谱的**空间原始数据受 IRB 限制**，空间路线必须重设计

JCI Insight 图谱（`10.1172/jci.insight.191990`，PMC12890526，gold OA）原文：

> "The spatial transcriptomics data have the same restrictions, and the IRB has requested that we do not publicly share individual-level sequencing data. **Aggregate-level data** for bulk RNA sequencing and spatial transcriptomics will be shared by lead contact upon request. **Individual-level data are only available through collaboration** following approval of the lead contact and the VUMC IRB."

**同时确认可公开获取的部分**：
- **scRNA-seq 全部来自公开 GEO**：`GSE184362`、`GSE193581`、`GSE232237`、`GSE182416`、`GSE191288`；另有 GSA `HRA000686`、CNGB `CNP0004262`
- **bulk**：TCGA（cBioPortal）、`GSE213647`（CNUH/SNUH）、St. Jude Cloud、`GSE310793`（MD Anderson）
- **代码完全公开**：https://github.com/mloberg16/THCA_Fibroblast_Atlas，commit `9a70119`
- **去卷积方案已在文中实现**：*"Raw RNA counts and broad cluster labels from the integrated thyroid cancer single-cell RNA-sequencing atlas were used as a reference for deconvolution of spatial transcriptomics data. The broad stromal cluster labels were split into iCAF, myCAF, **APOE⁺ PVL**, pericyte, and vSMC subpopulations…"*（工具：BayesSpace）

> **结论**：JCI 图谱可作为**单细胞参考（公开）**与**方法学范本（代码公开）**，但**不可作为空间底图（个体级受限）**。Run #23 的 `D3_D9_spatial_anchor_preresearch.md` 把 JCI 列为"资源 A：主空间底图"——**该定位需下调**。

### 0.3 ⭐ 发现三：图谱已存在 **APOE⁺ perivascular-like (APOE⁺ PVL)** 基质亚群

JCI 图谱把基质亚群划分为 5 类：iCAF（CXCL12/APOD）、**myCAF（POSTN/FAP）**、**APOE⁺ PVL（cluster 4）**、pericyte（HIGD1B/COX4I2）、vSMC（ACTA2/TAGLN）。

**意义**：APOE 在**基质侧**也已被独立标注为一个亚群，且已被纳入空间去卷积标签。这提供了第二个 APOE 锚点（基质 PVL），与发现一的髓系 Macro2 形成**双 compartment APOE 证据**。

### 0.4 附带：D17 的 ENA 数据线索（本轮意外收获）

ENA 检索 `study_title="*thyroid*"` 命中 60 项研究，其中两条直接对应 D17（肠道/瘤内微生物群）：
- **`PRJEB49680`** — "Thyroid cancer gut microbiota"（ENA 可访问 ✅）
- **`PRJEB49964`** — "Alterations of Gut Microbiome and Metabolite Profiles Associated with Anabatic Lipid Dysmetabolism"（ENA 可访问 ✅）

二者为 D17 提供了**不依赖 NCBI 的现成原始数据**，建议列为 D17 预研的起步资源。

---

## 1. 背景与目标（修订版）

**核心科学问题（修订后）**

| 编号 | 问题 | 修订说明 |
|---|---|---|
| **Q1** | 在髓系 compartment 中，**SPP1⁺/APOC1⁺/APOE⁺ Macro2** 是否与 APOE⁺ PVL 基质亚群、POSTN⁺ myCAF 三者在空间上构成同一生态位？ | 由 0.1 + 0.3 合并而来，是本轮**新出现的可检验问题** |
| **Q2** | Macro2 的「胆固醇稳态 + EMT + KRAS + PI3K-AKT-mTOR」signature 能否预测 LNM 与复发？ | 直接可做的零湿实验产出 |
| **Q3** | MGST1 是否在任何甲状腺细胞 compartment 中与 APOE 共表达？ | **仍是空白**（26 轮）；本轮新增可检索的阴性证据 |
| **Q4**（原 D9） | SPP1⁺ 与 TREM2⁺ TAM 是同一生态位还是空间分隔？ | 本轮 TREM2 无新证据，降级为次优先 |

**目标**：以**公开 scRNA 为参考 + 公开/可申请空间数据为底图**，产出 (a) 三 compartment（髓系 Macro2 / 基质 APOE⁺ PVL / myCAF）空间耦合图谱，(b) Macro2 signature 的 LNM/复发预后价值，(c) MGST1 的正式阴性报告。

---

## 2. 数据集清单（含可得性实测 / Verified Availability）

> 可得性为本机 2026-10-02 实测（HTTP 状态码），非论文声称。

### 2.1 主引擎（单细胞参考）

| # | 资源 | DOI / 编号 | 类型 | OA | 实测可得 | 用途 |
|---|---|---|---|---|:-:|---|
| **A′** | Integrated sc + spatial atlas（POSTN⁺ myCAF；**含 APOE⁺ PVL 标注**） | 10.1172/jci.insight.191990｜PMC12890526 | 期刊 + 代码 | gold | ✅ 全文 | **单细胞参考 + 方法学范本**；空间个体级 ❌（IRB 限制） |
| **A′-code** | mloberg16/THCA_Fibroblast_Atlas | GitHub，commit `9a70119` | 代码 | 公开 | ✅ **200** | BayesSpace 空间去卷积 + 基质亚群划分全流程，**直接复用** |
| **P** | 儿童 PTC scRNA（**Macro2 = SPP1/APOC1/APOE**） | 10.1016/j.isci.2026.116560｜PMC13378368 | 期刊 + 原始数据 | gold | ✅ 全文 | **本轮新主引擎**：D9″/D3″ 的核心发现来源 |
| **P-data** | 儿童 PTC raw scRNA + RNA-seq | **PRJCA050808**（GSA-human） | 原始数据 | 申请制 | ✅ **200**（ngdc.cncb.ac.cn 可达） | 儿童队列矩阵下载 |
| **B** | 成人 PTC scRNA（**跨队列桥梁**） | **GSE193581** | 原始数据 | 公开 | ⚠️ **GEO 不可达** | 被 A′ 与 P **共同引用**，是唯一无需新数据的跨队列对照 |

### 2.2 验证/补充资源

| # | 资源 | DOI / 编号 | OA | 实测可得 | 用途 |
|---|---|---|---|:-:|---|
| **L** | PTC 三部位（T/PT/LN）scRNA + 空间 + bulk；17 基因 LNM 签名，FN1 枢纽 | 10.1016/j.compbiolchem.2025.108857 | ❌ closed | 仅摘要 | 17 基因签名可作 baseline 模型对照 |
| **M** | PTC TME 图谱；**Mac-APOC1** M2 样亚群 | 10.1016/j.molimm.2026.05.006 | ❌ closed | 仅摘要 | APOC1 独立复现队列 |
| **G** | 配对原发–LNM scRNA | 10.1080/2162402x.2026.2701504｜PMC13360498 | gold | ✅ 全文 | ⚠️ **数据仅"upon reasonable request"，未公开存档** → 可行性下调 |
| **H** | 去分化 snRNA + Visium + GeoMx 图谱 | 10.1186/s12943-026-02699-2 | gold | 全文 | 数据存 KHDP（需申请，Run #23 风险未解除） |
| **E17** | Thyroid cancer gut microbiota | **PRJEB49680** | — | ✅ ENA | D17 起步数据 |
| **E17b** | Gut microbiome + lipid dysmetabolism | **PRJEB49964** | — | ✅ ENA | D17 起步数据 |

### 2.3 公共 bulk 验证队列（论文引用，可直接取）

`GSE213647`（CNUH/SNUH）、`GSE310793`（MD Anderson）、TCGA-THCA（cBioPortal）、St. Jude Cloud。
⚠️ 前三者的 GEO 通道本机不可达；**TCGA 走 cBioPortal、St. Jude Cloud 走官网**均不依赖 NCBI，可优先使用。

---

## 3. 方法学（修订版：三 compartment 空间耦合）

> **关键修订**：因 JCI 空间个体级数据受限，路线由「直接用 JCI 空间底图」改为 **"公开 scRNA 参考 → 去卷积到可得空间底图"**。

### 3.1 Step 1 — 建立统一的髓系/基质亚群参考（零数据申请）
- 输入：**A′** 的整合 scRNA 图谱（公开 GEO 矩阵）+ **P** 的儿童 scRNA（PRJCA050808）。
- 处理：以 **A′-code**（GitHub）的聚类与注释流程为基准，确保与原文亚群标签一致（iCAF / myCAF / **APOE⁺ PVL** / pericyte / vSMC；髓系 Macro1/2/3）。
- 跨队列桥梁：**GSE193581** 同时被 A′ 与 P 使用 → 用于 harmonize 儿童 vs 成人批次（Harmony / scVI）。
- **输出**：统一注释的 thyroid TME 参考图谱（髓系 + 基质）。

### 3.2 Step 2 — 定义三个待检验 compartment
| compartment | 标记基因 | 来源 |
|---|---|---|
| **Macro2（髓系）** | SPP1、APOC1、APOE；功能签名 = 胆固醇稳态 + EMT + KRAS + PI3K-AKT-mTOR | 资源 P（iScience 原文） |
| **APOE⁺ PVL（基质）** | APOE + 中度血管周标志 | 资源 A′（JCI cluster 4） |
| **POSTN⁺ myCAF（基质）** | POSTN、FAP | 资源 A′（JCI cluster 2） |

> ⚠️ **必须分开报告**：Macro2（髓系 APOE）与 APOE⁺ PVL（基质 APOE）是不同 compartment；Run #21–#25 的「APOE 高表达**肿瘤**亚群」是第三个 compartment（上皮）。三者**不得合并**。

### 3.3 Step 3 — 空间耦合量化
- **底图（按优先级）**：
  1. JCI **aggregate-level** 空间数据（向 lead contact 申请；已在文中说明可索取）
  2. 资源 H 的 Visium + GeoMx（KHDP 申请；Run #23 已有联系路径）
  3. 其他公开甲状腺 Visium（下轮补检索；CELLxGENE 经查**无**甲状腺癌专属数据集，需另寻）
- **方法**：沿用 A′-code 的 BayesSpace + 去卷积路线（把 broad stromal 拆到亚群级别），叠加 **cell2location / RCTD** 作双算法交叉验证。
- **指标**：邻域富集 z-score（r = 50/100 µm，置换检验）、Ripley's K/L、表达场空间滞后回归。
- **假设（双向，不得预设）**：H₁ = 三者构成同一脂质-免疫生态位；H₀' = Macro2 与 APOE⁺ PVL 空间分隔（分别对应免疫抑制与血管周基质重塑）。

### 3.4 Step 4 — 预后关联（零湿实验可完成）
- Macro2 signature score（GSVA/ssGSEA）× LNM 状态 × 复发，在 **TCGA-THCA（cBioPortal）** 与 **GSE213647** 上做 Cox / log-rank，FDR 校正。
- 与资源 L 的 **17 基因 LNM 签名（FN1 枢纽）** 比较增量 AUC —— 直接回答"Macro2 是否带来新增量"。

### 3.5 Step 5 — MGST1 阴性报告（正式化）
- 在 Step 1 参考图谱的**所有 compartment** 中系统检索 MGST1 表达与 APOE 共表达；
- 若全阴性，产出**正式阴性结果**（可作为论文中的"we found no co-expression"表述），并更新 D3″ 状态为「已系统检验，阴性」。

---

## 4. 工具栈 / Tooling

- **去卷积与空间**：BayesSpace（复用 A′-code）、cell2location、spacexr/RCTD、Squidpy、Giotto
- **单细胞**：Scanpy / Seurat v5、Harmony / scVI（跨队列批次校正）、CellChat / NicheNet（配体–受体）
- **signature 与预后**：GSVA/ssGSEA、`survival`、`timeROC`；与 FN1 17 基因签名比较用 `pROC`
- **数据获取**：cBioPortal API（TCGA）、St. Jude Cloud、NGDC GSA（PRJCA050808）、ENA（PRJEB49680/49964）
- **湿实验联动（长期，非必需）**：HALO/Akoya 多重 IF（SPP1 + APOC1 + APOE + CD68 + POSTN）

---

## 5. 里程碑 / Milestones

| 阶段 | 任务 | 产出 |
|---|---|---|
| **M1（本轮已完成）** | 实证核对 5 篇关键论文的数据可用性；发现 Macro2（SPP1/APOC1/APOE）；确认 JCI 空间受限；实测 GEO 不可达、ENA/GSA/GitHub 可达 | 本方案 + `d9_dataset_inventory_run26.json` |
| **M2** | clone A′-code → 申请 PRJCA050808 → 复现 JCI 基质亚群划分（含 APOE⁺ PVL）与 P 的 Macro1/2/3 | 统一注释的参考图谱 v1 |
| **M3** | 以 GSE193581 为桥梁做儿童 vs 成人 harmonize；输出 Macro2 signature | Macro2 signature 基因集 + 跨年龄丰度对比表 |
| **M4** | 向 JCI lead contact 索取 aggregate-level 空间数据；并行推进 KHDP（资源 H）申请 | 空间底图（至少一个） |
| **M5** | 三 compartment 空间耦合量化（双算法交叉） | 共定位图谱 + Ripley's K 表 |
| **M6** | TCGA-THCA + GSE213647 预后关联；与 FN1 17 基因签名比较增量 AUC | 预后表 + 增量 AUC |
| **M7** | MGST1 全 compartment 系统检索 → 阳性则升级 D3″，阴性则正式归档 | D3″ 状态终判 |

---

## 6. 风险与前提 / Risks & Caveats

| 风险 | 等级 | 说明与对冲 |
|---|:-:|---|
| **GEO 本机不可达** | 🔴 高 | 实测 `www.ncbi.nlm.nih.gov/geo` 与 `ftp.ncbi.nlm.nih.gov` 均 **HTTP 000**。所有 GSE 无法直连下载 → 对冲：① ENA（✅ 可达）取 SRA 等价数据；② 优先用不依赖 NCBI 的源（cBioPortal、St. Jude Cloud、GSA、GitHub）；③ 必要时经合作节点代取 |
| **JCI 空间个体级数据 IRB 限制** | 🔴 高 | 已确认仅 aggregate-level 可申请 → 对冲：改用"scRNA 参考 + 去卷积"路线，并并行申请资源 H（KHDP） |
| **配对原发–LNM（资源 G）数据未公开** | 🟠 中 | 原文明确"upon reasonable request"，无存档编号 → 不可作为主要验证队列，降级为可选 |
| **Macro2 的 APOE 位于髓系而非癌细胞** | 🟠 中 | 与原 D3′/D3″ 假设的 compartment 不同 → **必须在所有输出中显式区分三个 APOE compartment**，禁止混用 |
| **儿童队列 n=11** | 🟠 中 | 样本量小，结论需标注探索性；用成人 GSE193581 做交叉验证 |
| **MGST1 可能永久阴性** | 🟡 低-中 | 若 M7 全阴性，应归档 D3″ 为"已系统检验的阴性假设"，而非继续轮询检索 |
| **CELLxGENE 无甲状腺癌数据** | 🟡 低 | 已实测：2237 条 tissue 过滤结果中**无甲状腺癌专属数据集** → 空间底图需另寻（ENA / GSA / 直接申请） |

---

## 7. 与 Run #27 联动 / Next-Run Sync

1. **新增检索词回灌**：把 `Macro2 signature`（SPP1 / APOC1 / APOE / 胆固醇稳态 / EMT）与 `APOE⁺ PVL` 作为独立查询维度加入 Run #27 的定向基因深挖面板；同时把 `MGST1` 保留为**阴性对照词**。
2. **空间底图专项检索**：Run #27 增加一路 EPMC/OpenAlex 查询，专找**公开存档的甲状腺 Visium/GeoMx/Stereo-seq 数据集**（CELLxGENE 已排除）。
3. **D17 数据已就位**：PRJEB49680 / PRJEB49964 经 ENA 可达，Run #27 可直接启动 D17 的原始数据层预研，无需等待。
4. **环境事实更新**：GEO/FTP 不可达需写入 `RETRIEVAL_ENVIRONMENT.md`（本轮已实测），后续所有 run 不再尝试 NCBI 通道。
5. **D3″ 优先级**：若 M7 阴性，Run #27 起将 D3″ 从「候选方向」移入「已检验假设（阴性）」归档区，释放监测资源给 D9″ 与 D17。

---

*本方案基于 Europe PMC 全文 XML 实证与本机网络实测，所有可得性结论均以实测 HTTP 状态为准，未采信论文单方声明。取代 Run #22/Run #23 姊妹方案中对空间数据可得性的乐观假设。*
