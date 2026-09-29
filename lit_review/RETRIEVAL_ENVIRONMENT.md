# 检索环境事实 / Retrieval Environment Facts

> 本文件记录本机实测的检索通道状态，供 `lit-review` 自动化每轮直接引用，
> **避免重复踩坑与无效重试**。最后实测：2026-08-07。

## 一、通道可用性实测 / Channel Availability

| 通道 | 状态 | 实测结果 | 结论 |
|---|---|---|---|
| **OpenAlex** `api.openalex.org` | ✅ 可用 | HTTP 200 / ~1.4s | **主源** |
| **Crossref** `api.crossref.org` | ✅ 可用 | HTTP 200 / ~1.4s | DOI 元数据校验 |
| **Unpaywall** `api.unpaywall.org` | ✅ 可用 | 正常返回 OA PDF 链接 | OA 全文获取 |
| **bioRxiv/medRxiv** `api.biorxiv.org` | ⚠️ 慢 | HTTP 200 / ~14s | 仅按需，无关键词检索 |
| **Semantic Scholar** | ⚠️ 限流 | HTTP 429（无 API key） | 备用，需 `S2_API_KEY` |
| **NCBI eutils** `eutils.ncbi.nlm.nih.gov` | ❌ **不可达** | **4/4 超时，HTTP 000（60s）** | **禁止直连重试** |
| **PubMed 网页** `pubmed.ncbi.nlm.nih.gov` | ❌ **不可达** | HTTP 000 / 15s 超时 | 同上 |
| **paper-search-mcp MCP** | ⚠️ 不稳定 | 走服务端代理，可用但频繁 `not well-formed (invalid token)` 并截断结果 | **仅作补充源，失败不阻塞** |

### 关键推论

1. **`paper-search-mcp` 反复报 `not well-formed (invalid token)` 的根因**
   ——其上游 NCBI 通道不稳定 / 响应被截断导致 XML 解析失败，**不是查询语法问题**，
   重试基本无效（历史 run#14 曾 100% 失败）。

2. **run#8–#16 连续 9 轮"零新增"是方法学假象，不是领域停滞。** 两个叠加原因：
   - **排序策略错误**：`sort=relevance` 只会反复返回同一批老经典文献；
     监测增量必须用 `sort=publication_date:desc`。
   - **PubMed 编目滞后**：近 30 天新文献多数**尚无 PMID**。实测同期
     OpenAlex 命中 62 篇，其中绝大多数 PMID 为空 —— PubMed 单点必然漏检。

3. **OpenAlex 同时索引预印本**（preprints.org / bioRxiv / medRxiv），
   而 PubMed 不索引，直接补上一个此前完全缺失的证据层。

## 一·补、代码仓通道 / Git Remote

| 项 | 值 |
|---|---|
| 远端 | `git@github.com:bobpaulus/paper-work.git` |
| 本地工作区 | `D:\paperwork`（已 `git init`，默认分支 `main`，远端名 `origin`） |
| 认证 | SSH，`~/.ssh` 已配好，实测 `ssh -T git@github.com` 返回 `Hi bobpaulus!` ✅ |
| 提交身份 | 全局已配置 `baozewen <bobpaul@126.com>` ✅ |

**坑：GitHub SSH 22 端口在默认沙箱内被阻断**，表现为
`kex_exchange_identification: read: Software caused connection abort` 或
`Connection reset by 20.205.243.166 port 22`。
→ git 远程操作（pull / push）必须**绕过沙箱执行**；绕过沙箱后可连通，
但仍有**偶发 reset**，需重试（实测第 2 次即成功）。最多重试 3 次，间隔 3 秒。

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

1. 跑 `oa_search.py` 拿增量（主源，必做）
2. `paper-search-mcp` 补充检索（可选，**失败即跳过，不重试超过 1 次**）
3. 对 High 相关的新增，用 Crossref 校验 DOI 元数据、Unpaywall 取 OA 全文
4. 按 `lit-review` 技能的 template / schema / rubric 合成双语报告
5. 报告写 `literature_review_<YYYYMMDD_HHMMSS>.md`，原始结果写 `search_results_latest.json`

## 四、待改善 / Optional Improvements

设置以下环境变量可显著提升配额与可用性（当前**均未设置**）：

- `OPENALEX_API_KEY` — 推荐，提升配额
- `S2_API_KEY` — 解决 Semantic Scholar 429，打开引文图谱能力
- `NCBI_API_KEY` — 仅在 NCBI 网络恢复后才有意义
- `CORE_API_KEY` — 跨学科全文
