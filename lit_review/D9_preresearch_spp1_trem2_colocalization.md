# D9 预研方案：SPP1+ × TREM2+ 空间共定位验证 (D9 Pre-Research: SPP1+ × TREM2+ Spatial Co-localization)

> 延续 Run #22（2026-09-11）文献监测报告之「推荐下一步方向 / Recommended Next Direction」。
> 本报告首选可执行产出：**以空间共定位验证厘清 D8（TREM2+ AHR–IDO1）↔ D9（SPP1–CD44 / SPP1+ TAM）关系**。
> 生成日期：2026-09-11 ｜ 数据源：OpenAlex（主源，直连稳定）；Zenodo 仅浏览器可访问（本机 TLS 主机名校验失败，不影响引用）。

---

## 1. 背景与目标 (Background & Objective)

Run #22 最强收敛信号为 **SPP1+ TAM 轴强势浮现**（两独立证据：Zenodo AI 多组学存档 + JCO 摘要 RAI 难治去分化），直接将 **D9 由 rubric 28 升 31**。但两条证据均属降档证据（仓库存档 / 会议摘要），且 **SPP1+ 与既往 TREM2+（D8，run #21 已获 scRNA+scATAC+CyTOF+空间+体内直接证据）是否为同一/不同 TAM 生态位尚未厘清**。

**核心科学问题**：SPP1+ TAM 与 TREM2+ TAM 在 PTC 原发–淋巴结转移（LNM）微环境中是**共定位同一生态位**，还是**空间分隔的不同功能亚群**？这决定 D8↔D9 是合并、层级还是平行关系。

**目标**：在公开空间/单细胞图谱上，用可复现流程量化 SPP1 × TREM2 的空间共定位强度，并关联 LNM 状态与 RAI 难治去分化，为后续体内功能闭环提供假设与签名（signature）。

---

## 2. 公开数据集清单 (Public Dataset Inventory)

| # | 资源 / Resource | 类型 | DOI / 链接 | OA | 本轮用途 |
|---|---|---|---|---|---|
| A | Integrated sc + spatial atlas of thyroid cancer progression (prognostic fibroblast subpops, **POSTN+ myCAF**) | 期刊论文 + 数据 | 10.1172/jci.insight.191990 | gold | **主空间图谱**：提供 PTC 原发/转移空间转录组与 myCAF 注释，作 SPP1/TREM2 投影底图 |
| B | Decoding the spatiotemporal heterogeneity of TAMs | 期刊论文 | 10.1186/s12943-024-02064-1 | gold | TAM 时空异质性方法学与巨噬细胞亚群注释参考 |
| C | SPP1+ Macrophages and Spatially Organized Immunosuppression in Cancer | 期刊论文 | 10.3390/biomedicines14020294 | gold | SPP1+ TAM 空间免疫抑制机制框架 |
| D | Pan-cancer atlas of TAMs as immunotherapy-response regulators | 期刊论文 | 10.1038/s41467-024-49885-8 | gold | TAM 泛癌签名，可作交叉验证 |
| E | SPP1+ TAM AI multi-omics (Zenodo deposit, Run #22 关键项) | 仓库存档 | 10.5281/zenodo.22290057 | — | SPP1+ TAM scRNA+空间+ML 签名（**未评议，降档**；本机 TLS 不可达，浏览器取） |
| F | TLS-like spatial transcriptional organization in PTC (Zenodo deposit) | 仓库存档 | 10.5281/zenodo.22661715 | — | PTC 空间生态位可复现数据，D3↔D8 空间验证可复用 |
| G | Paired primary–LNM scRNA atlas（Run #21 引用 PMID 42430190） | 期刊论文 | **10.1080/2162402x.2026.2701504**（OncoImmunology 2026, gold OA）| gold | **配对原发–LNM 单细胞**，SPP1/TREM2 亚群在转移前后丰度变化主证据；Run #23 已用 OpenAlex `pmid:42430190` 解析 DOI |

> 注：资源 G 的 DOI 已于 Run #23 经 OpenAlex `pmid:42430190` 解析为 10.1080/2162402x.2026.2701504（OncoImmunology, gold OA）；其 sister 方案 `D3_D9_spatial_anchor_preresearch.md` 将资源 G 与 Run #23 新增主引擎资源 H（Mol Cancer 2026 snRNA+Visium+GeoMx）整合。

---

## 3. 方法学方案 (Methodology)

### 3.1 空间共定位量化 (Spatial Co-localization)
- **底图**：资源 A（JCI Insight 2026）空间切片（原发 vs LNM 配对），叠加资源 E 的 SPP1+ TAM 签名与 TREM2 标记。
- **指标**：
  - 邻域分数（neighborhood fraction）：以 SPP1+ 像素/spot 为中心，统计 TREM2+ 在 r=50/100 µm 邻域内的富集比（vs 随机置换 p 值）。
  - Ripley's K / L 函数（空间点模式），分原发/转移分层。
  - 空间相关性：SPP1 与 TREM2 表达场的局部 Pearson / 空间滞后回归。
- **工具**：Squidpy / Giotto（空间图神经网络）、R `SPATA2` / `spacexr`（平台效应校正）、Python `scanpy`。

### 3.2 单细胞解卷积 (scRNA Deconvolution)
- 用资源 A + E 的 SPP1+ TAM 与 TREM2+ 签名，对资源 G（配对原发–LNM）做 CIBERSORTx / MuSiC 解卷积，得两亚群在转移前后的**丰度变化 Δ**。
- 假设 H1：LNM 侧 SPP1+ TAM 丰度显著升高（呼应 Zenodo 项 LNM 预测）。

### 3.3 关联与假设检验 (Association)
- 以资源 A 临床注释，做 SPP1+ TAM 丰度 × LNM 状态 × RAI 难治 × 生存（log-rank / Cox）的关联，检验 JCO 摘要「SPP1+ 巨噬细胞调控 RAI 难治去分化」假说。
- 多重检验校正（FDR），效应量 + 95% CI。

### 3.4 体内功能闭环 (In Vivo, 实验申请)
- PTC 类器官 / PDX 中敲低 / 过表达 SPP1+ TAM 信号轴，评估 LNM 与 RAI 难治去分化——验证 JCO 摘要去分化假说（D9 最高优先级验证）。

---

## 4. 工具栈 (Tooling)
- 空间：Squidpy、Giotto、SPATA2、spacexr、Seurat v5
- 单细胞：Scanpy / Seurat、CellChat（细胞间通讯）
- 多重免疫荧光（湿实验）：HALO / Akoya 平台（SPP1 + TREM2 + CD68 + 组织边界多重染色）
- 统计：R (`survival`, `limma`, `edgeR`)、Python (`scipy`, `statsmodels`)

---

## 5. 里程碑与交付 (Milestones)
- **M1（本轮已完成）**：公开数据集定位与元数据对齐（资源 A–F 已获 DOI/OA；G 待 Run #23 补 DOI）。
- **M2（下一轮）**：拉取资源 A/E/G 原始计数矩阵 → 空间共定位分析脚本 + 中间结果（邻域分数、Ripley's K）。
- **M3（下一轮）**：关联统计与假设检验，产出 SPP1+ × TREM2 共定位图谱 + LNM/RAI 关联表。
- **M4（实验联动）**：体内功能闭环方案与动物/类器官实验申请。

---

## 6. 风险与前提 (Risks & Caveats)
- 资源 E/F 为 **Zenodo 仓库存档（未同行评议）**，证据降档；资源 JCO 摘要为初步结果——正式发表全文 + 独立队列验证前，claim 限定为「假设生成」。
- SPP1+ 与 TREM2+ 可能是**不同生态位**（前者促 LNM、后者免疫抑制）或**重叠**；共定位分析需同时报告「共定位」与「空间分隔」两种可能，不得预设结论。
- 空间平台效应（Visium vs 10x HD vs 多重 IF）需 `spacexr` 校正，避免批次混淆。
- 配对原发–LNM 样本稀缺（资源 G 为关键），若不可得则用资源 A 的原发/转移空间切片替代并标注局限。

---

## 7. 与下一轮监测联动 (Next-Run Sync)
- 将验证所得的 **SPP1+ TAM 与 TREM2+ TAM 签名基因集**回灌 Run #23 检索词，作为独立查询维度，追踪正式发表与独立队列验证。
- Run #23 建议对 ME/SC/SP 维度默认 90 天窗口（消除低频高分维度欠采样，Run #20–#22 已三度证伪「30 天=0」）。

---

*本方案为 Run #22 推荐的「首选可执行产出」之落地预研；数据集与签名将随 Run #23 滚动更新。*
