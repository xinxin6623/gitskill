---
name: gitout
description: 自然语言驱动的 GitHub 项目发现引擎。用户用自然语言描述需求（"我想找能打断 TTS 的语音 pipeline"），LLM 推断意图 → 生成多组查询词 → gh CLI 多轮检索 → reject 筛选 → LLM 按意图重排序 → 输出 3-5 份小红书风格小白说明文档到 ./gitout/。支持子命令 list / open / prune。
---

# /gitout — 自然语言 GitHub 项目发现 Skill

## 触发场景

- `/gitout <自然语言描述>` — 主流程。**输入是需求，不是关键词。**
  - 例：`/gitout 能打断 TTS 的轻量语音 pipeline`
  - 例：`/gitout 有没有 Rust 写的、能跑在 Mac 上的本地向量数据库`
- `/gitout <自然语言> --domain <名称>` — 指定 domain（默认 misc）
- `/gitout list` — 列出已收纳 entries
- `/gitout open <repo>` — 查看某条小白文档
- `/gitout prune` — 容量与陈旧检查

## 核心定位

把"我想找个能做 X 的工具但不知道关键词怎么搜"这种最常见的真实场景，压缩成一句话。**输入是模糊需求，输出是 3-5 份让你三分钟看懂"这玩意能不能解决你问题"的小白文档。**

与上一版的根本差异：**不再做关键词字面匹配 + stars 排序**，而是 LLM 推断意图 → 多策略检索 → 按意图重排序。

---

## 主流程：五段式

### Step 1：意图抽取（LLM 推理，不调外部工具）

读用户的自然语言输入，在心里（不写文件）抽出以下结构化意图：

```yaml
intent:
  what: "<用户到底想找一个能做什么的东西>"        # 一句话本质
  scenario: "<典型使用场景>"                      # 用户在什么情境下用
  hard_constraints:                              # 硬性约束（命中 → reject）
    - "<例：必须是 Rust>"
    - "<例：必须本地可跑>"
  soft_preferences:                              # 软性偏好（影响重排序）
    - "<例：代码量少更好>"
    - "<例：依赖少更好>"
  anti_patterns:                                 # 用户明显不想要的
    - "<例：不要 SaaS 商业绑定>"
queries:                                         # 3-5 组检索词
  - "<query 1>"
  - "<query 2>"
  - "<query 3>"
```

**queries 生成策略：**
- 至少包含 1 个"主题词"（最直白的英文术语）
- 至少包含 1 个"特性词"（如 "interruptible TTS"、"streaming voice"）
- 至少包含 1 个"反共识词"（避开热门生态绑定，如 "lightweight"、"minimal"、"single-file"）
- 全部用英文（GitHub 检索友好）

### Step 2：歧义判断 → 决定是否问用户

LLM 自检意图清晰度：

- **直接跑** 当意图明确（用户描述具体、术语清晰、约束完整）
- **问用户** 当出现以下任一情况：
  - 关键名词有多重含义（如"agent"可指 AI agent / browser user agent / SRE agent）
  - 硬性约束矛盾或缺失关键信息（如未说语言、未说本地/云端）
  - LLM 推出 2+ 个完全不同方向

用 AskUserQuestion 工具给 2-3 个意图选项让用户挑，**不要罗列 4+ 个**。明确意图后立即进入 Step 3。

### Step 3：多策略检索（并行调 gh CLI）

对每条 query，并行执行（**同一消息内多个 Bash 调用**）：

```bash
gh search repos "<query>" \
  --limit 8 \
  --json fullName,description,stargazersCount,updatedAt,language,url,owner,license
```

**关键变化：**
- **省略 `--sort`** —— gh CLI 默认就是 best-match 相关度排序；`--sort` 只接受 `{forks|help-wanted-issues|stars|updated}`，传 best-match 会报错
- 多组 query 取并集，按 `fullName` 去重
- 总候选池目标 **15-20 条**（3-5 query × 8 limit，去重后约这个量）

所有原始 JSON 落地到 `./gitout/raw/<YYYY-MM-DD>/<intent-slug>/`。

### Step 4：Reject 筛选 + README 抓取（两轮）

**第一轮 Reject（基于元数据，不抓 README）：**

对候选池每一条，命中以下任一 → reject：

1. `pushedAt` 超 365 天（明显废弃）
2. 命中用户的 `hard_constraints` 反面（如要求 Rust 但实际是 Python）
3. `stargazersCount < 3` 且 `pushedAt < 90 天` 双低（既冷门又不活跃）
4. fullName 或 description 命中 `anti_patterns` 关键词

剩下的进入第二轮。**目标剩 8-12 条。**

**第二轮 README 抓取（并行）：**

```bash
gh api repos/<owner/name>/readme --jq '.content' | base64 -d | head -c 8000
```

抓完后 LLM 做语义级 reject：
- README 全是 buzzword 无具体实现
- 是空壳/教程/awesome-list 型 repo
- 与用户意图实质不符（描述沾边但本质不同）

### Step 5：LLM 重排序 + Top 3-5 选择

按以下加权要素对剩余候选打分排序（**不写出数字分，只输出排序**）：

| 维度 | 权重 | 说明 |
|------|------|------|
| 意图匹配度 | 高 | 是否真的解决用户描述的问题 |
| 实现质量信号 | 中 | 代码可读性、文件组织、README 是否有实操内容 |
| 软偏好命中 | 中 | 用户 soft_preferences 命中数 |
| 活跃度 | 低 | last_commit、contributor 数 |
| stars | 最低 | **明确降权，避免热门绑架** |

**输出 3-5 个**（候选 ≥ 5 时强制 5；候选 < 5 时按实际数）。

### Step 6：生成小白说明文档

对入选的每个 repo，生成 `./gitout/<domain>/entries/<owner>__<name>.md`：

```markdown
---
type: repo
repo: <owner/name>
domain: <domain>
status: active
discovered: <today>
last_reviewed: <today>
intent_matched: "<对应 intent.what 的简写>"   # 新增：标注命中哪条意图
signals:
  stars: <n>
  last_commit: <iso-date>
  language: <lang>
  license: <spdx>
url: <html_url>
absorption:
  harvested: false
  used: false
  used_in: []
---

# <项目名> · 小白说明书

## 🧐 这是什么
<一句话本质定位，不抄 README。>

## 💡 解决什么问题
<代入式描述用户痛点 2-3 条。>

## 🎯 谁该用 / 谁别用
**适合你如果：** <2-3 条>
**别浪费时间如果：** <2-3 条>

## 🚀 三分钟上手
```bash
<具体安装/最小示例命令>
```

## 🔑 关键文件 / 关键概念
- `<path>` — <作用>

## ⚠️ 踩坑提示
- <真实坑点>

## 🤔 为什么这次推它给你
<新增段：明确说出本 repo 命中了用户哪条意图、哪条 soft preference，
以及没命中的 trade-off。这是 LLM 重排序逻辑的透明化。>

---
*由 /gitout 生成 · <date> · intent: "<原始自然语言输入>"*
```

**写作硬约束：**

1. 正文 ≤ 1000 字
2. 小红书风格、第二人称"你"、emoji 小标题
3. 全中文，代码/标识符保留英文
4. 不抄 README、必须包含"谁别用"、不打数字分
5. **必须有"为什么这次推它给你"段** —— 解释命中意图的逻辑

### Step 7：更新 index 与汇报

- `./gitout/<domain>/index.yaml` append 新 entries
- `./gitout/<domain>/README.md` 更新健康度
- 给用户输出一段汇报，**必须包含：**
  - 抽出的意图（what / 关键约束）
  - 用的 3-5 组 query
  - 候选池数 → reject 数 → 入选数 漏斗
  - 文件路径

---

## 子命令分支

### `/gitout list`
读 `./gitout/*/index.yaml`，按 domain 分组列出 entry 和 `intent_matched`。

### `/gitout open <repo>`
模糊匹配 entry 文件，Read 后呈现。

### `/gitout prune`
扫 `./gitout/<domain>/entries/*.md`：
- `last_reviewed` 超 30 天 → 提示移入 graveyard
- 数量 > 30 → 红色警告
- 输出建议清单，**不自动删除**

---

## 安全边界（继承 v1.2 §7）

- **全链路只读**：仅用 `gh search` / `gh repo view` / `gh api repos/*/readme`
- 禁止任何 GitHub 写操作（issue / PR / comment / fork / clone）
- 写盘仅限 `./gitout/` 子目录

---

## 错误处理

- `gh` 未登录 → 提示 `gh auth login`，停止
- API 配额触顶 → 直接告知用户休息，不重试
- 所有 query 加起来 0 结果 → 反馈给用户、给 2-3 个改写建议、停止
- README 抓取失败 → 该 repo 标记 reject，继续

---

## 设计借鉴说明

本 Skill 是 `radar-system-v1.2.md` 的轻量化落地版 + 自然语言增强版：

- **保留**：v1.2 的目录骨架、Repo Entry 模型、容量上限、graveyard、只读安全边界
- **简化**：v1.2 的"本地 Qwen3 粗筛 + 远端强模型 deepdive"两级引擎 → 由 Claude Code 一步到位
- **新增**：
  - 自然语言意图抽取（Step 1）—— 解决"不知道用什么关键词搜"
  - 多策略 query 生成 + best-match 排序（Step 3）—— 解决"stars 排序偏向热门生态"
  - 两轮 reject + LLM 重排序（Step 4-5）—— 解决"低星但高契合的项目被埋"
  - 小白文档"为什么推它给你"段 —— 让 LLM 推理过程对用户透明
