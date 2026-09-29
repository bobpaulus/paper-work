# D3/D9 空间锚定预研方案：APOE−/MGST1+ 亚群锚定 + SPP1+ × TREM2+ 共定位 (D3/D9 Spatial Anchor Pre-Research)

> 延续 Run #23（2026-09-17）文献监测报告之「推荐下一步方向 / Recommended Next Direction」。
> 本报告首选可执行产出：**以 *Molecular Cancer* 2026 snRNA+空间去分化图谱为引擎，打通方法论（D14）→ 机制缺口（D3），并续接 Run #22 的 D9/D8 空间共定位验证**。
> 生成日期：2026-09-17 ｜ 数据源：OpenAlex（主源）；Europe PMC / PMC13374302（全文 XML，gold OA）；GitHub / KHDP（原始数据与代码）。

---

## 1. 背景与目标 (Background & Objective)

Run #23 最强原发证据为 **突变特异性去分化多组学图谱**（*Molecular Cancer* 2026, PMID 42458477, DOI 10.1186/s12943-026-02699-2, gold OA），整合 **snRNA-seq + Visium + GeoMx（双空间平台）+ 公共 bulk**，刻画 BRAF V600E vs RAS 驱动的 DTC→ATC 去分化轨迹与肿瘤–间质互作。该图谱直接提供 Run #22–#23 长期缺口所需的「高分辨率原发空间 + 单细胞」材料。

**两个核心科学问题（对应方向）**：
1. **D3（APOE−/MGST1+ 代谢–免疫干性转移亚群，连续 23 轮无直接锚定）**：在该图谱的癌细胞亚群中，是否存在 `APOE low ∧ MGST1 high` 双边界定义的代谢–免疫去分化亚群，且富集于去分化轨迹末端与间质互作热点？—— 这是补 D3 原发空间证据的唯一可行路径。
2. **D9/D8（SPP1+ × TREM2+ TAM 生态位关系）**：续接 Run #22 的 D9 预研，在该图谱（含 Visium + GeoMx 双空间）上量化 SPP1+ 与 TREM2+ TAM 的空间共定位，厘清两者是同一生态位还是空间分隔亚群。

**目标**：用可复现流程在公开图谱上 (a) 锚定 APOE−/MGST1+ 癌细胞亚群并检验其去分化/间质耦合，(b) 量化 SPP1 × TREM2 空间共定位，(c) 以细胞类型解析因果框架（D14）对去分化轨迹做驱动排序，产出可检验假设与签名。

---

## 2. 公开数据集清单 (Public Dataset Inventory)

### 2.1 本轮新增主引擎（Run #23 溢出 High SP 论文）
| # | 资源 / Resource | 类型 | DOI / 链接 | OA | 用途 |
|---|---|---|---|---|---|
| H | Mutation-specific dedifferentiation trajectories & tumor–stromal interactions in thyroid cancer | 期刊 + **原始数据 + 代码** | 10.1186/s12943-026-02699-2（正文）｜ 数据 **KHDP SNUH-THYROID-NGS2**｜ 代码 https://github.com/SNU-Thyroid/Thyroid_cancer_scRNA | gold | **主引擎**：snRNA-seq + Visium + GeoMx + 公共 WTS；BRAF V600E vs RAS 去分化轨迹 |
| H-code | SNU-Thyroid/Thyroid_cancer_scRNA | GitHub 仓库 | https://github.com/SNU-Thyroid/Thyroid_cancer_scRNA | 公开 | 单细胞/空间分析全流程代码（Seurat/Squidpy 类），直接复用 |
| H-data | SNUH-THYROID-NGS2 | Korea Health Data Platform | https://khdp.net/database/data-search-detail/701/SNUH-THYROID-NGS2/1.0.0 | 需申请 | 本研究生成计数矩阵（snRNA/Visium/GeoMx）；韩国健康数据平台，可能需机构邮箱/数据使用申请 |

### 2.2 复用 Run #22 D9 预研资源（更新 G 的 DOI）
| # | 资源 | 类型 | DOI / 链接 | OA | 用途 |
|---|---|---|---|---|---|
| A | Integrated sc + spatial atlas (POSTN+ myCAF) | 期刊 + 数据 | 10.1172/jci.insight.191990 | gold | 主空间底图（原发/转移） |
| B | Spatiotemporal heterogeneity of TAMs | 期刊 | 10.1186/s12943-024-02064-1 | gold | TAM 亚群注释参考 |
| C | SPP1+ Macrophages spatially organized immunosuppression | 期刊 | 10.3390/biomedicines14020294 | gold | SPP1+ TAM 机制框架 |
| D | Pan-cancer TAM atlas (immunotherapy response) | 期刊 | 10.1038/s41467-024-49885-8 | gold | 泛癌 TAM 签名交叉验证 |
| E | SPP1+ TAM AI multi-omics (Zenodo) | 存档 | 10.5281/zenodo.22290057 | — | SPP1+ TAM 签名（未评议，降档） |
| F | TLS-like spatial organization in PTC (Zenodo) | 存档 | 10.5281/zenodo.22661715 | — | PTC 空间生态位可复现数据 |
| **G（已补 DOI）** | **Paired primary–LNM scRNA (intratumoral heterogeneity & immunosuppressive TME)** | 期刊 | **10.1080/2162402x.2026.2701504** | gold | **配对原发–LNM 单细胞**：SPP1/TREM2 亚群转移前后丰度变化主证据（Run #23 经 OpenAlex `pmid:42430190` 解析） |

### 2.3 公共 bulk WTS 参考集（论文引用的公共数据集，供发现/验证队列）
GSE134355, GSE148673, GSE158291, GSE163203, GSE184362, GSE191288, GSE193581, GSE210347, GSE232237, GSE250521（TCGA/其他甲状腺 bulk；NCBI 本机不可达，需经 OpenAlex/ENA 或合作节点取矩阵）。

---

## 3. 方法学方案 (Methodology)

### 3.1 D3：APOE−/MGST1+ 癌细胞亚群空间锚定（核心缺口）
- **底图**：资源 H 的 snRNA-seq（癌细胞聚类）+ Visium/GeoMx 空间切片，叠加去分化轨迹注释（BRAF V600E vs RAS）。
- **定义**：在癌细胞簇内按 `APOE low ∧ MGST1 high` 双边界切分亚群（参考 run #21–#22 的 APOE/MGST1 代谢–免疫轴线索）。
- **检验 H_D3**：
  - 富集检验：APOE−/MGST1+ 亚群是否显著富集于**去分化轨迹末端**（伪时间/RNA 速率末端）与**间质互作热点**（CellChat / NicheNet 配体–受体，尤其与 CAF/巨噬的 MGST1 相关代谢–免疫串扰）？
  - 空间定位：在 Visium/GeoMx 上映射该亚群 spot，检验其是否靠近 POSTN+ myCAF（资源 A）与 SPP1+/TREM2+ 髓系生态位。
- **工具**：Scanpy/Seurat（亚群+伪时间）、Squidpy/Giotto（空间映射）、CellChat/NicheNet（配体–受体）。

### 3.2 D9/D8：SPP1+ × TREM2+ 空间共定位（续接 Run #22）
- **底图**：资源 H 的 Visium + GeoMx（**双空间平台交叉验证**，优于单平台）+ 资源 A/G 原发–LNM。
- **指标**（同 D9 预研 §3.1）：邻域分数（r=50/100 µm 富集比 + 置换 p）、Ripley's K/L、SPP1–TREM2 表达场空间滞后回归。
- **假设 H_D9**：LNM 侧 SPP1+ TAM 丰度升高；SPP1+ 与 TREM2+ 可能为**不同生态位**（前者促 LNM、后者免疫抑制）或重叠——同时报告两种可能，不得预设。

### 3.3 D14：细胞类型解析因果 + 空间驱动排序
- 复用 #2（*Int. J. Immunogenetics* 2026, 10.1111/iji.70066）的**细胞类型解析因果推断**框架：以资源 H 的 eQTL/空间共变，对去分化轨迹做因果驱动排序（Mendelian-randomization 式 / 空间因果图），优先锁定可成药驱动。
- 输出：去分化轨迹的「因果驱动基因集」，回灌 D3 的 APOE/MGST1 边界作机制解释。

### 3.4 关联与验证（统计）
- APOE−/MGST1+ 亚群丰度 × 去分化评分 × LNM 状态 × 生存（Cox/log-rank，FDR 校正）。
- SPP1+ × TREM2+ 共定位强度 × LNM/RAI 难治（呼应 JCO 摘要去分化假说）。

---

## 4. 工具栈 (Tooling)
- 空间：Squidpy、Giotto、SPATA2、spacexr、Seurat v5（平台效应校正）
- 单细胞：Scanpy / Seurat、CellChat、NicheNet（细胞间/配体–受体）
- 因果：TensorQTL / fastQTL（eQTL）+ 细胞类型解析因果推断（参考 #2 框架）
- 统计：R (`survival`, `limma`, `edgeR`)、Python (`scipy`, `statsmodels`)
- 湿实验联动（长期）：HALO/Akoya 多重 IF（APOE + MGST1 + SPP1 + TREM2 + CD68 多重染色）

---

## 5. 里程碑与交付 (Milestones)
- **M1（本轮已完成）**：定位主引擎资源 H（KHDP SNUH-THYROID-NGS2 + GitHub 代码）、解析资源 G 的 DOI（10.1080/2162402x.2026.2701504）、确认双空间平台（Visium+GeoMx）。
- **M2（下一轮）**：clone GitHub 仓库 → 复现 snRNA 癌细胞聚类与去分化轨迹注释 → 定义 APOE−/MGST1+ 双边界亚群并出富集/空间映射中间结果。
- **M3（下一轮）**：SPP1+ × TREM2+ 双空间（Visium+GeoMx）共定位分析 + 关联统计，产出共定位图谱与 LNM/RAI 关联表。
- **M4（方法）**：细胞类型解析因果框架套用去分化轨迹，产出因果驱动基因集。
- **M5（实验联动）**：多重 IF / 类器官–PDX 体内功能闭环，验证 D3 亚群与 D9 生态位假设。

---

## 6. 风险与前提 (Risks & Caveats)
- **数据获取风险（最高）**：SNUH-THYROID-NGS2 存于 **KHDP（韩国健康数据平台）**，可能需机构邮箱/数据使用申请，且对非韩国机构可能受限；若不可得，**GitHub 仓库可能含已处理矩阵/子集**应优先核查，或降级用资源 A/G（已全 gold OA）作替代底图并标注局限。
- **claim 边界**：D3 在获得原代空间锚定前仍限定为「代谢–免疫耦合的去分化/LNM 驱动亚群」假设；SPP1+/TREM2+ 共定位需同时报告「共定位」与「空间分隔」两种可能。
- **平台效应**：Visium（spot）vs GeoMx（ROI）vs 多重 IF 需 `spacexr` 校正，避免批次混淆；双平台交叉验证正是为对冲此风险。
- **降档证据**：资源 E/F 为 Zenodo 存档（未评议），正式发表 + 独立队列验证前 claim 限「假设生成」。
- **NCBI 不可达**：GSE 公共集需经 OpenAlex/ENA 或合作节点取矩阵，禁止直连 eutils 重试。

---

## 7. 与下一轮监测联动 (Next-Run Sync)
- 将本预研产出的 **APOE−/MGST1+ 癌细胞亚群签名** 与 **SPP1+/TREM2+ TAM 签名基因集** 回灌 Run #24 检索词，作为独立查询维度，追踪正式发表与独立队列验证。
- Run #24 建议 **SC/SP/ME 维度默认 90 天窗口**（Run #23 已证实 30 天窗口结构性遗漏 High SP 论文）。
- 若 KHDP 数据申请受阻，记录于 Run #24 记忆，降级方案以资源 A/G 双 gold-OA 图谱推进 D3/D9，保持主线不中断。

---

*本方案为 Run #23 推荐的「首选下一步」之落地预研；主引擎为 Run #23 溢出 High SP 论文（Mol Cancer 2026），数据集与签名将随 Run #24 滚动更新。与 Run #22 的 `D9_preresearch_spp1_trem2_colocalization.md` 互为姊妹方案，共享资源 A–G，新增资源 H 为主引擎。*
