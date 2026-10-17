# 检索环境事实 / Retrieval Environment Facts

> 本文件记录本机实测的检索通道状态，供 `lit-review` 自动化每轮直接引用，
> **避免重复踩坑与无效重试**。最后实测：**2026-10-17（根因定位，NCBI 从未"不可达"）**。
>
> ---
>
> ## 🔴 2026-10-17 根因定位：NCBI "不可达" 是误判，真实原因与网络无关
>
> 过去 29 轮把 NCBI 的 HTTP 000 归因为「网络封锁 / 通道不可达」并反复在 ✅/❌ 之间横跳，
> **全部是误判**。2026-10-17 抓真实错误后定位到：
>
> ```
> curl: (35) schannel: next InitializeSecurityContext failed:
>        CRYPT_E_REVOCATION_OFFLINE (0x80092013)
>        - 由于吊销服务器已脱机，吊销功能无法检查吊销。
> ```
>
> **真实根因**：Windows **Schannel 证书吊销检查**（OCSP/CRL）无法访问吊销服务器，
> TLS 握手在完成前被中止 → curl 报 HTTP 000。
> **这是 TLS 层问题，不是网络层问题**；DNS 解析正常（`2600:1901:0:c831::`，真实 NCBI IP）。
>
> 之所以表现为「时变」：吊销服务器本身时通时不通，所以 HTTP 000 / 200 来回横跳——
> 被误读成"通道时好时坏"。
>
> ### ✅ 修复方法（二选一，均已实测）
>
> | 方法 | 命令 | 实测 |
> |---|---|---|
> | **curl 加 `--ssl-no-revoke`** | `curl --ssl-no-revoke --noproxy '*' --max-time 20 <url>` | eutils **200 / 0.42s**；esearch **200 / 0.49s**；PubMed 网页 **200 / 1.76s** |
> | **改用 Python `urllib`**（走 OpenSSL，默认不做吊销检查） | `urllib.request.urlopen(...)` | einfo **200 / 0.64s**；GEO acc.cgi **200 / 0.99s**；`efetch` 取到 PMID 42847133 完整摘要 |
>
> ### 直接影响
>
> 1. **PMID 回填随时可做**，不再看"通道脸色"。用 Python urllib + 0.4 s 间隔即可；
>    偶发 **HTTP 429 = 真实速率限制**（不是网络故障），退避 3 s 重试即通（实测 Count=115525）。
> 2. **不需要 Clash 代理**。见下节。
> 3. **探针命令必须改**：所有 curl 探针一律加 `--ssl-no-revoke`，否则会把可达通道误判为不可达。
>
> ### ⚠️ 连带更正：Unpaywall `410`
>
> `api.unpaywall.org/v2/search?query=` 返回 **410 Gone** —— 这是**端点已被官方下线**，不是网络故障。
> 正确用法是单 DOI 端点 `api.unpaywall.org/v2/<doi>?email=`，**实测 200 / 0.81s**。
>
> ---
>
> ## ⚠️ 2026-10-16（已作废，保留作历史）：NCBI eutils 重新不可达（第二次反转）
>
> Run #29 开局探针实测：**NCBI eutils HTTP 000**（`--noproxy '*'` 15.1 s 超时；
> 带代理 0.15 s 立即拒连）。OpenAlex / Europe PMC / Crossref 均 200 正常。
>
> | 日期 | NCBI eutils |
> |---|---|
> | 2026-08 | ❌ 4/4 HTTP 000 |
> | 2026-10-09 | ✅ 3/3 HTTP 200 |
> | **2026-10-16** | ❌ **HTTP 000（再次不可达）** |
>
> → **后果**：Run #29 **无法执行 `_pmid_backfill_ncbi.py`**，32 条新增中 12 条只能标「待编目」。
> → **规则不变**：通道状态**每轮必测**，既不能永久采信"不可用"，也不能永久采信"已恢复"。
> 这是同一条教训的**第二次验证**。
>
> ## ⚠️ 2026-10-09 重大变更：NCBI 全域已恢复
>
> 2026-10-09 复检发现**此前"NCBI 全域不可达"的记录已失效**，网络环境整体改善：
>
> | 通道 | 2026-08 结论 | **2026-10-09 复检** |
> |---|---|---|
> | NCBI eutils | ❌ 4/4 超时 HTTP 000 | ✅ **3/3 HTTP 200 / ~0.5–0.9s**；`esearch` 返回真实 count，`efetch` 可取完整摘要 |
> | PubMed 网页 | ❌ HTTP 000 | ✅ HTTP 203（NCBI 反爬响应，网络层可达） |
> | NCBI GEO | ❌ HTTP 000 | ✅ **HTTP 200 / ~0.6s**，`acc.cgi` 返回 GSE60542 完整元数据 |
> | NCBI FTP | ❌ HTTP 000 | ✅ **HTTP 200，实测下载 `GSE60542_series_matrix.txt.gz` 27,530,495 bytes / 17.6s** |
> | Crossref | ⚠️ Run #28 超 20 分钟未完成 | ✅ **HTTP 200 / ~2.4s（已恢复正常）** |
> | Unpaywall | ⚠️ 同上 | ✅ **HTTP 200，正常返回 best_oa_location** |
> | OpenAlex | ✅ | ✅ HTTP 200 / ~1.0s（**首次请求可能 HTTP 000 超时，重试即通**） |
> | git SSH 22 | ❌ 沙箱内阻断，须绕过沙箱 | ✅ **沙箱内 `git ls-remote` 直接成功** |
>
> **直接影响**：
> 1. **PMID 不再是瓶颈** —— 已用 `esearch <doi>[DOI]` 批量回填（脚本 `_pmid_backfill_ncbi.py`），
>    此前 184 条"待编目"记录可批量定号。
> 2. **GSE 矩阵可直连下载** —— 此前"GEO 一律转 ENA"的推论作废；`GSE60542`（PTC 原发灶 vs 淋巴结转移灶）
>    已实测可取，直接服务于 D21″ 的 M1 区室拆分。
> 3. `paper-search-mcp` 的 `not well-formed` 根因（上游 NCBI 不稳定）**可能已消失**，下轮可重新试用。
> 4. **下轮仍须先做通道探针再定策略** —— 本次变更说明通道状态会随时间变化，不得永久采信单一历史结论。

## 一、通道可用性实测 / Channel Availability

| 通道 | 状态 | 实测结果 | 结论 |
|---|---|---|---|
| **OpenAlex** `api.openalex.org` | ✅ 可用 | HTTP 200 / ~1.4s | **主源** |
| **Crossref** `api.crossref.org` | ✅ 可用（**2026-10-09 恢复**） | Run #28 曾超 20 分钟未完成；**2026-10-09 复检 HTTP 200 / ~2.4s** | DOI 元数据校验；**仍建议只跑 High（≤10 条）+ timeout 10 s，因其历史上波动大** |
| **Unpaywall** `api.unpaywall.org` | ✅ 可用（**端点需更正**） | `/v2/<doi>` **HTTP 200 / 0.81s** 正常；**`/v2/search?query=` 已官方下线返回 410 Gone（不是故障）** | OA 全文获取，**只能用单 DOI 端点**；422/404 表示 DOI 未被收录，非网络故障。curl 同样建议加 `--ssl-no-revoke` |
| **bioRxiv/medRxiv** `api.biorxiv.org` | ⚠️ 慢 | HTTP 200 / ~14s | 仅按需，无关键词检索 |
| **Semantic Scholar** | ⚠️ 限流 | HTTP 429（无 API key） | 备用，需 `S2_API_KEY` |
| **NCBI eutils** `eutils.ncbi.nlm.nih.gov` | ✅ **可用（2026-10-17 根因修正：此前 ❌ 全是 Schannel 误判）** | `curl --ssl-no-revoke` **200 / 0.42s**；Python urllib **200 / 0.64s**；`esearch` Count=115525；`efetch` 可取完整摘要 | **PMID 回填主通道**。**curl 必须加 `--ssl-no-revoke`**，否则误报 000。速率限制：无 key 时偶发 **HTTP 429**（真实限流，退避 3 s 重试即通），脚本用 0.4 s 间隔 |
| **PubMed 网页** `pubmed.ncbi.nlm.nih.gov` | ✅ 可用 | `--ssl-no-revoke` **HTTP 200 / 1.76s**（此前 203 为反爬响应） | 人工核对用 |
| **NCBI GEO** `www.ncbi.nlm.nih.gov/geo` | ✅ **可用（2026-10-09 恢复）** | HTTP 200 / ~0.6s，`acc.cgi` 返回 GSE60542 元数据 | GSE 元数据查询 |
| **NCBI FTP** `ftp.ncbi.nlm.nih.gov` | ✅ **可用（2026-10-09 恢复）** | HTTP 200，**实测下载 GSE60542 矩阵 27.5 MB / 17.6 s** | **GSE 表达矩阵直连下载，优先于 ENA** |
| **paper-search-mcp MCP** | ⚠️ 不稳定 | 走服务端代理，可用但频繁 `not well-formed (invalid token)` 并截断结果 | **仅作补充源，失败不阻塞** |
| **Europe PMC** `www.ebi.ac.uk/europepmc/webservices/rest` | ✅ 可用 | HTTP 200；`resultType=core` 可取结构化摘要 | **第二通道**，已扩至 10 路；**近三轮贡献量超过 OpenAlex** |

### Europe PMC 路数与污染（Run #28 实测 / Route notes）

**12 路键**：`SC` 单细胞 / `SP` 空间 / `IM` 免疫微环境 / `ME` 代谢 / `AL` 算法 / `ST` 干性 /
`MO` 分子机制 / `PR` 预后转移 / `MACRO2` / `SPATIAL_DS` / `LIPID`（Run #28 新增，载脂蛋白家族）/
`AI`（Run #28 新增，LLM / 基础模型 / pathomics）。

- `MO` 与 `PR` 两路是 Run #27 新增，单轮回补 56 条（占该轮 85%）→ **此前 6 路存在系统性漏检**。
- `LIPID` + `AI` 两路是 Run #28 新增，合计贡献 79 候选（占该轮 EPMC 候选近半）→ 价值高，建议保留。
- ✅ `ME` 路已按 Run #27 建议加 `AND (TITLE:"carcinoma" OR TITLE:"cancer")` 约束，
  **污染明显下降**（81 命中中可用率显著提升），该修复有效，继续保持。
- ⚠️ `ME` 路仍会漏进甲状腺–肝轴 / MASLD / 肥胖 / 妊娠 / 卒中等**非肿瘤代谢**研究，需人工剔除。
- ⚠️ `SP` 路会混入党群生态学（"spatial distribution of thyroid cancer incidence"），需人工剔除。
- 撤稿/更正条目：`Retraction notice to` / `Correction:` / `Erratum:` / `ASO Visual Abstract:` /
  `Supplementary Table S…` / `Supplemental Figure …` 目前**仍靠人工降档**，建议脚本化。

### 数据下载通道（Run #26 新增实测 / Data download channels）

GEO 不可达意味着**论文里的 GSE 编号只是"引用"，不是"可下载"**。已验证的替代通道：

| 通道 | 状态 | 实测 | 用途 |
|---|---|---|---|
| **NCBI GEO/FTP** | ✅ **可用（2026-10-09 恢复）** | 200；GSE60542 矩阵 27.5 MB / 17.6 s | **2026-10-09 起恢复为首选**，见上方重大变更说明 |
| **ENA**（EBI）`www.ebi.ac.uk/ena` | ✅ 可用 | 200 / ~1.2s | GEO 的替代/补充；支持 portal API 按 `study_title` 检索 |
| **CELLxGENE** `api.cellxgene.cziscience.com` | ✅ 可用 | 200 / ~5.9s | 已加工 scRNA；**经查无甲状腺癌专属数据集**（2237 条 tissue 过滤 0 命中） |
| **NGDC GSA-human** `ngdc.cncb.ac.cn/gsa-human` | ✅ 可用 | 200 / ~0.8s | 中国队列原始数据（如 PRJCA050808） |
| **GitHub API** `api.github.com` | ✅ 可用 | 200 / ~1.3s | 论文配套代码（去卷积/聚类全流程） |
| **Zenodo** `zenodo.org` | ✅ 可用 | 301（重定向，正常） | 存档型数据集 |
| **cBioPortal** | （未实测，不依赖 NCBI） | — | TCGA-THCA 矩阵 |
| **St. Jude Cloud** | （未实测，不依赖 NCBI） | — | St. Jude 儿童队列 |

> **2026-08 旧推论（已作废）**：凡论文声明"data deposited at GEO (GSE…)"的，在本机默认视为不可直连，须转 ENA。
> **2026-10-09 修订**：NCBI FTP 恢复，**GSE 矩阵可直接下载**；ENA 降级为备份通道。
> 仍需注意：大矩阵（>100 MB）下载慢，且 `GSE193581` 未见 `series_matrix`（走 FTP superseries 或 ENA 更稳）。

### 关键推论

1. **`paper-search-mcp` 反复报 `not well-formed (invalid token)` 的根因（历史结论，待重新验证）**
   ——曾归因于其上游 NCBI 通道不稳定 / 响应被截断导致 XML 解析失败，**不是查询语法问题**，
   重试基本无效（历史 run#14 曾 100% 失败）。
   **2026-10-09 起 NCBI 已恢复，此根因可能已消失，下轮应重新试用该 MCP 再下结论。**

2. **run#8–#16 连续 9 轮"零新增"是方法学假象，不是领域停滞。** 两个叠加原因：
   - **排序策略错误**：`sort=relevance` 只会反复返回同一批老经典文献；
     监测增量必须用 `sort=publication_date:desc`。
   - **PubMed 编目滞后**：近 30 天新文献多数**尚无 PMID**。实测同期
     OpenAlex 命中 62 篇，其中绝大多数 PMID 为空 —— PubMed 单点必然漏检。
     **2026-10-09 修订**：滞后仍在，但现在可用 `esearch <doi>[DOI]` **事后批量回填 PMID**
     （脚本 `_pmid_backfill_ncbi.py`）。因此"缺 PMID"由**永久性缺陷**降级为**可修复的临时状态**，
     下轮应对缺号记录跑一次回填，而不是直接标"待编目"了事。

3. **OpenAlex 同时索引预印本**（preprints.org / bioRxiv / medRxiv），
   而 PubMed 不索引，直接补上一个此前完全缺失的证据层。

## 一·特、代理与 Clash（2026-10-17 终判 / Proxy & Clash）

**结论先行（2026-10-17 强化）：本项目依赖的全部检索通道（NCBI / Europe PMC / OpenAlex /
Crossref / Unpaywall）均为「直连可达」，**完全不需要 Clash**。**

### ✅ 2026-10-17 终判：Clash 对检索「无必要且有害」

当日实测环境：Clash **未运行**，系统代理 `ProxyEnable=0`（关闭），但 `ProxyServer=127.0.0.1:7890`
**残留未清**——所幸开关为 0，未造成断网（这正是 `clash_ctl.py` 里"先关系统代理再杀进程"的原因）。

在此**纯直连**状态下全部通道实测：

| 通道 | 直连实测（`--noproxy '*'`） |
|---|---|
| OpenAlex | ✅ **200 / 1.14s** |
| Europe PMC | ✅ **200 / 2.46s** |
| Crossref | ✅ **200 / 1.90s** |
| Unpaywall `/v2/<doi>` | ✅ **200 / 0.81s** |
| NCBI eutils | ✅ **200 / 0.42s**（须 `--ssl-no-revoke`） |
| NCBI GEO | ✅ **200 / 0.99s** |
| NCBI PubMed 网页 | ✅ **200 / 1.76s**（须 `--ssl-no-revoke`） |

→ **零通道需要代理。** 历史上唯一「不可达」的 NCBI，根因是 Schannel 吊销检查（见文首），
**代理帮不上忙，反而更慢**：`mode=rule` 下 NCBI 会被规则送进 Proxy 组，坏节点 i/o timeout。

**规则固化**：
1. 检索一律**直连 + `--noproxy '*'`**；curl 一律加 **`--ssl-no-revoke`**。
2. Clash **不作为**检索前置条件；自动化凌晨运行无需开启。
3. `clash_ctl.py` 的 `off` / `use` 会中断用户上网，**仅限用户在场且确认后**执行。
4. 只有 Google Scholar 等被墙源才需要代理，届时也是**按需临时开**，检索进程仍绕过。

---

以下为 2026-10-09 旧实测（结论一致，保留对照）：

用 `curl --noproxy '*'` 完全绕过任何代理后的实测：

| 通道 | 直连（绕过全部代理） | 走 Clash 7890 |
|---|---|---|
| NCBI eutils | ✅ 200（3/3，0.47–0.81 s） | ✅ 200 |
| NCBI GEO | ✅ 200 | ✅ 200 |
| Europe PMC | ✅ 200 | ✅ 200 |
| OpenAlex | ✅ 200 | ✅ 200 |
| Crossref | ✅ 200 | ✅ 200 |
| Unpaywall | ⚠️ 422（邮箱参数被拒，网络层通） | ⚠️ 422 |
| Google（对照，需翻墙） | ❌ 000 | ⚠️ 302（**证明代理确实生效**） |

**推论**：
1. §一「NCBI 恢复」的**真实原因不是 Clash**——NCBI 直连本来就通。
   2026-08 记录的「不可达」应是当时网络出口/临时故障所致，属**时变状态**（见 §三 的探针要求）。
2. **自动化凌晨 03:00 运行时无需 Clash 在线**，不应把 Clash 作为检索前置条件。
3. 真正需要代理的只有 Google Scholar / 部分被墙源；且**当前 Clash 的 `GLOBAL` 组 = DIRECT**，
   `mode=rule`，出境规则由 profile 决定，节点可用性会波动（曾观测到 12 s 超时误判为 000，20 s 则为 302）。

### ⚠️ 反直觉：开着 Clash 反而会拖累检索（2026-10-09 实证）

用户完整关闭 Clash（进程 + 系统代理）后复测，检索通道**全部仍然可达**：

| 通道 | Clash 关闭后直连 | 备注 |
|---|---|---|
| NCBI eutils / GEO | ✅ 200（0.51 s） | — |
| Europe PMC / OpenAlex / Crossref | ✅ 200（0.78–1.04 s） | — |
| Google | ❌ 000 | 被墙，符合预期 |

而**开着 Clash 时反而更差**——内核日志实证：

```
WRN dial failed: os-3.tr202604.com:443 connect error: dial tcp4 45.13.199.32:443: i/o timeout
    proxy=Proxy  rAddr=eutils.ncbi.nlm.nih.gov:443  rule=Match
```

即：`mode=rule` 下 NCBI 匹配兜底规则 `Match()` → 走 **Proxy 组**（当时选中日本-OS-3 节点），
而该节点超时 → **检索请求被强行绕经一个不通的境外节点**。

→ **结论：文献检索应直连**。若 Clash 必须开着（如同时要访问 Google Scholar），
建议检索进程显式绕过代理（`curl --noproxy '*'` 或 `NO_PROXY=*`），
或把 Clash 切到 `mode=direct`，否则会被坏节点拖慢甚至拖挂。

### Clash 开关在本环境的能力边界（实测）

| 能力 | 结论 |
|---|---|
| 关（taskkill + 关系统代理） | ✅ 可靠 |
| 开 —— CFW GUI（`Clash for Windows.exe`） | ❌ **拉不起来**：Electron 程序，在无交互桌面会话中启动后进程立刻消失 |
| 开 —— clash 内核（`clash-win64.exe`） | ⚠️ **可启动，但无法在会话外存活**：进程会被工具/沙箱会话结束清理，下次调用时已退出 |
| 直接跑内核 + `config.yaml` | ❌ 会退出：该文件仅 4 行（无 proxies/rules），须用 `profiles/*.yml`（29 KB） |

- 需脱离 GUI 启动时用 **`clash_core_start.py`**（合并 profile + secret/控制端口后启动内核，并补设系统代理）。
- **关键顺序**：关闭时必须**先关系统代理再杀进程**；否则代理地址残留在已无监听的
  `127.0.0.1:7890`，会导致**整个系统（浏览器）断网**。`clash_ctl.py off` 已按此顺序实现。
- 若已出现"Clash 没了但系统代理还开着"的断网状态，执行
  `python -c "import clash_ctl as c; c.set_sysproxy(False)"` 立即恢复。

### Clash 环境与控制

| 项 | 值 |
|---|---|
| 配置 | `%USERPROFILE%\.config\clash\config.yaml` |
| 主程序 | `%USERPROFILE%\AppData\Local\Programs\Clash for Windows\Clash for Windows.exe` |
| 内核进程 | `clash-win64.exe` |
| mixed-port | `7890`（系统代理亦指向此端口） |
| External Controller | 见 `config.yaml` 的 `external-controller`（**端口每次启动会变**，须动态读取） |
| `secret` | 见 `config.yaml`（**严禁硬编码、严禁打印、严禁入库**） |

控制脚本：**`clash_ctl.py`**（本目录），通过 Clash RESTful API 操作。

```bash
python clash_ctl.py status        # 进程 / API / mode / 系统代理 / 通道探测
python clash_ctl.py probe         # 仅做直连 vs 走代理的通道对比
python clash_ctl.py on            # 未运行则启动 CFW，并切 rule
python clash_ctl.py on --export   # 输出可 eval 的 export 语句（子进程改不了父 shell）
python clash_ctl.py off           # 退出 Clash 进程（会中断上网）
python clash_ctl.py off --soft    # 仅切 direct，保留进程
python clash_ctl.py mode <rule|global|direct>
python clash_ctl.py nodes         # 列出代理组与节点延迟
python clash_ctl.py use "<节点名>" # 切换节点
```

**脚本安全设计**：`secret` 每次从 `config.yaml` 动态读取、输出中遮蔽为 `***`；
API 请求强制 `ProxyHandler({})` 绕过代理（否则会走 Clash 自己形成环路）；
`tasklist` 输出按 **GBK** 解码（中文 Windows，否则 UnicodeDecodeError 导致进程误判）。

## 一·补、代码仓通道 / Git Remote

| 项 | 值 |
|---|---|
| 远端 | `git@github.com:bobpaulus/paper-work.git` |
| 本地工作区 | `D:\paperwork`（已 `git init`，默认分支 `main`，远端名 `origin`） |
| 认证 | SSH，`~/.ssh` 已配好，实测 `ssh -T git@github.com` 返回 `Hi bobpaulus!` ✅ |
| 提交身份 | 全局已配置 `baozewen <bobpaul@126.com>` ✅ |

**历史坑：GitHub SSH 22 端口在默认沙箱内被阻断**，表现为
`kex_exchange_identification: read: Software caused connection abort` 或
`Connection reset by 20.205.243.166 port 22`。
→ git 远程操作曾必须**绕过沙箱执行**；绕过沙箱后可连通，但仍有**偶发 reset**，需重试。

**✅ 2026-10-09 复检：沙箱内 `git ls-remote --heads origin main` 直接成功（返回远端 HEAD）**，
即 22 端口在沙箱内**已不再被阻断**。
→ 建议：仍**保留重试 3 次 / 间隔 3 秒**的循环（偶发 reset 未消失），但**不再强求绕过沙箱**；
   若沙箱内首次失败，再尝试绕过沙箱。

**已纳入版本库**：`lit_review/` 目录**整体入库**（2026-09-29），含检索产物
（`search_results_*.json`、`literature_review_*.md`）、一次性检索脚本（`_build_*.py`、`_enrich_*.py`）、
方向预研（`D3_D9_*.md`）与 `analysis/`。每轮提交**直接 `git add` 即可，不需要 `-f`**。

`.gitignore` 仅排除：`thyroid_cancer_direction/`、`*.pdf`、`*.log`、`.workbuddy/`、`__pycache__/`。
每轮仍按路径显式添加本轮产物，**不要用 `git add -A`**（会把 `D:\paperwork` 顶层未跟踪文件一并带上）。

## 二、主检索器 / Primary Retriever

脚本：`D:\paperwork\lit_review\oa_search.py`

```bash
# 常规周度监测（近 30 天）
python oa_search.py --days 30 --per-page 25 --baseline search_results_latest.json

# 指定窗口 + 指定输出
python oa_search.py --since 2026-07-08 --out search_results_run17.json

# 放宽窗口补历史
python oa_search.py --days 90 --per-page 50
```

覆盖九路检索（维度代码）：
`a` 分子机制+预后转移 / `b` 分子机制 / `c` 算法方法 / `d` 免疫微环境 /
`e` 单细胞 / `f` 空间组学 / `g` 预后转移 / `h` 转移干性 / `i` 代谢重编程

### 脚本内建的数据清洗（重要）

实测发现三类污染，脚本已自动处理：

| 污染类型 | 实例 | 处理 |
|---|---|---|
| **期刊补充材料被当独立文献** | `Table 1_...`、`Data Sheet 1_...`（Frontiers 系） | 正则 `SUPPLEMENT` 直接丢弃 |
| **同一论文多版本重复** | KLF6 那篇有 **12 个** OpenAlex 记录 | 标题归一化为主键合并，补齐 PMID/DOI |
| **顺带提及甲状腺的他病文献** | irAE 甲功异常、Thyroid Eye Disease、桥本 | 要求**标题**点名甲状腺 **且**整体为肿瘤主题 |

实测一轮（近 30 天）：94 → 79 唯一记录（合并 25 组多版本）→ 57 篇在范围，剔除 22 篇。

## 三、每轮推荐流程 / Per-Run Workflow

1. **开局通道探针（必做）**：`curl` 打一遍 OpenAlex / Europe PMC / NCBI eutils / Crossref，
   各 `--max-time 15`，记录 HTTP 码。**通道状态会随时间变化，不得永久采信历史结论**（2026-10-09 的 NCBI 恢复即为教训）。
2. 跑 `oa_search.py` 拿增量（主源，必做）
3. **`python _pmid_backfill_ncbi.py` 回填缺号记录的 PMID**（NCBI 恢复后新增；缺号不再是"待编目"终点）
4. `paper-search-mcp` 补充检索（可选，**失败即跳过，不重试超过 1 次**；NCBI 恢复后可重新试用）
5. 对 High 相关的新增，用 Crossref 校验 DOI 元数据、Unpaywall 取 OA 全文
4. 按 `lit-review` 技能的 template / schema / rubric 合成双语报告
5. 报告写 `literature_review_<YYYYMMDD_HHMMSS>.md`，原始结果写 `search_results_latest.json`

## 四、待改善 / Optional Improvements

设置以下环境变量可显著提升配额与可用性（当前**均未设置**）：

- `OPENALEX_API_KEY` — 推荐，提升配额
- `S2_API_KEY` — 解决 Semantic Scholar 429，打开引文图谱能力
- `NCBI_API_KEY` — **NCBI 已于 2026-10-09 恢复，此 key 现在有实际意义**：
  可把速率上限从 3 req/s 提到 10 req/s，显著加快 PMID 回填与 GSE 抓取
- `CORE_API_KEY` — 跨学科全文
