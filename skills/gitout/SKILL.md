---
name: gitout
description: 自然语言驱动的 GitHub 项目发现引擎。用户用自然语言描述需求（"我想找能打断 TTS 的语音 pipeline"），LLM 推断意图 → 生成多组查询词 → gh CLI 多轮检索 → reject 筛选 → LLM 按意图重排序 → 输出 3-5 份小红书风格小白说明文档到 ./gitout/。支持子命令 list / open / prune / --quick。
---

# /gitout — 自然语言 GitHub 项目发现 Skill

## 安装

> ⚠️ **重要：本 skill 必须放在 `~/.claude/skills/gitout/SKILL.md` 才能被 Claude Code 识别。**
> 仅放在仓库的 `skills/gitout/` 下不会被自动加载。

推荐用 symlink，源码修改即时生效：

```bash
mkdir -p ~/.claude/skills
ln -sf /Users/qoragufimo390gmail.com/Documents/gitskill/skills/gitout ~/.claude/skills/gitout
```

或拷贝（修改源码后需重新拷贝）：

```bash
mkdir -p ~/.claude/skills/gitout
cp /Users/qoragufimo390gmail.com/Documents/gitskill/skills/gitout/SKILL.md ~/.claude/skills/gitout/
```

安装后**重启 Claude Code 会话**，输入 `/gitout` 验证是否可被识别。

---

## 触发场景

- `/gitout <自然语言描述>` — 主流程。**输入是需求，不是关键词。**
  - 例：`/gitout 能打断 TTS 的轻量语音 pipeline`
  - 例：`/gitout 有没有 Rust 写的、能跑在 Mac 上的本地向量数据库`
- `/gitout <自然语言> --domain <名称>` — 指定 domain（不指定时 LLM 推断）
- `/gitout <专名> --quick` — 轻量模式：跳过 README 抓取、300-500 字 mini 文档
- `/gitout list` — 列出已收纳 entries
- `/gitout open <repo>` — 查看某条小白文档
- `/gitout prune` — 容量、陈旧、raw 归档检查

## 核心定位

把"我想找个能做 X 的工具但不知道关键词怎么搜"压成一句话。**输入是模糊需求，输出是 3-5 份让你三分钟看懂"这玩意能不能解决你问题"的小白文档。**

与上一版的根本差异：**不再做关键词字面匹配 + stars 排序**，而是 LLM 推断意图 → 多策略检索 → 按意图重排序。

---

## 主流程：七段式

### Step 1：意图抽取 + 输入分流（LLM 推理，不调外部工具）

读用户输入，先做 **input_type 判断**：

| input_type | 触发特征 | 走哪条路 |
|---|---|---|
| `brand` | 单/双词专名（"xiaozhi"、"obsidian"、"home assistant"）；用户在找已知项目周边 | 走"种子探针"分支（Step 3a） |
| `need` | 自然语言需求描述（"能打断 TTS 的"、"Rust 写的本地向量库"）；含动词、约束 | 走多策略检索（Step 3b） |
| `mixed` | 专名 + 修饰需求（"xiaozhi 的 Android 客户端"） | 先种子探针锁母仓，再周边主题词扩展 |

抽出结构化意图：

```yaml
intent:
  input_type: brand | need | mixed
  what: "<一句话本质>"
  scenario: "<典型使用场景>"
  hard_constraints: ["<例：必须是 Rust>"]
  soft_preferences: ["<例：代码量少更好>"]
  anti_patterns: ["<例：不要 SaaS 商业绑定>"]
  queries: []   # need 模式才在 Step 3b 生成；brand 模式由探针决定
```

### Step 2：歧义判断 → 决定是否问用户

LLM 自检意图清晰度：

- **直接跑** 当意图明确
- **问用户** 当：关键名词多义、硬约束缺失、推出 2+ 完全不同方向

用 AskUserQuestion 给 2-3 个意图选项，**不要罗列 4+ 个**。

### Step 2.5：查 taxonomy 决定 domain

**强制查 `./gitout/_taxonomy.yaml`** 找 domain 强匹配（按 `name` + `aliases` 字段）：

- 命中已有 domain → 复用，entry 落到对应目录
- 没命中 → 新建 domain（kebab-case 名词短语），并 **append 到 `_taxonomy.yaml`**

```yaml
# _taxonomy.yaml 格式
domains:
  - name: voice-pipeline
    cn: 语音 pipeline
    aliases: [voice, tts, asr, audio-stream, speech]
    desc: 跟 AI 实时语音对话的底座
```

### Step 2.6：检测 .gitignore

首次跑时检查项目根 `.gitignore`：
- 缺失 → 创建并写入下列条目
- 已存在 → diff 后只 append 缺失项

```
.DS_Store
.obsidian/
gitout/raw/**/*_empty.json
```

### Step 3：检索（分流到 3a / 3b）

#### Step 3a：brand 模式 — 种子探针

先单词搜，按返回数决定后续：

```bash
gh search repos "<brand-word>" \
  --match name,description \
  --limit 20 \
  --json fullName,description,stargazersCount,updatedAt,pushedAt,language,url,owner,license,isArchived
```

- 返回 ≥ 15 条 → **不再扩 query**，直接进 Step 4
- 返回 < 15 条 → 加 1-2 个相关词（如"<brand> server"、"<brand> client"）补足

#### Step 3b：need 模式 — 多策略并行

生成 3-5 组 query（**单 query 不超过 3 词**，多词 AND 命中率太低）：
- 至少 1 个"主题词"（最直白英文术语）
- 至少 1 个"特性词"（如 "interruptible TTS"、"streaming voice"）
- 至少 1 个"反共识词"（"lightweight"、"minimal"、"single-file"）
- 全英文

对每条 query **并行**执行（同一消息多个 Bash 调用）：

```bash
gh search repos "<query>" \
  --match name,description,readme \
  --limit 8 \
  --json fullName,description,stargazersCount,updatedAt,pushedAt,language,url,owner,license,isArchived
```

**关键 flag 规则：**
- `--match name,description,readme` 是**默认**写法
- 省略 `--sort`（默认就是 best-match；显式 `--sort best-match` 会报错）
- **元规则：写进本 SKILL 的任何 CLI flag 都必须先 `gh <cmd> --help` 验证过**

#### 零返回 query 处理

- 返回 0 的 query **不落盘**（不写 `q*.json`）
- 在 domain `README.md` 末尾 append `discarded_queries: ["<q>", ...]` 留痕

成功 query 的 JSON 落地到 `./gitout/raw/<YYYY-MM-DD>/<intent-slug>/q<N>.json`。

### Step 4：Reject + README 抓取（两轮）

**第一轮 Reject（基于元数据）：**

1. `pushedAt` 超 365 天（明显废弃）
2. 命中 `hard_constraints` 反面
3. `stargazersCount < 3` 且 `pushedAt < 90 天` 双低
4. fullName / description 命中 `anti_patterns`
5. **brand / mixed 模式额外加"周边过滤"**：fullName 命中 `<brand>-(integration|plugin|client|bridge|mcp|hacs|esphome|admin|ui|dashboard|adapter|exporter)` → 不进主入选，**单独列入"相关周边"段**

目标剩 8-12 条进第二轮。

**第二轮 README 抓取（并行，反 buzzword）：**

```bash
gh api repos/<owner/name>/readme --jq '.content' | base64 -d > /tmp/readme_<slug>.md
```

抓完后**按行过滤**而不是 `head -c 8000`：

- 跳过：`![...]`（徽章/图）、`<img ...>`、`<a ...>`、纯空行、`---` 分隔线、`<table>` 内的 shields
- 取前 **200 行有效内容**作为 LLM 阅读输入

**停更状态扫描**（在抓取后立刻做）：

- 扫前 500 字 + GitHub `isArchived` 字段 + 关键词命中：
  `deprecated | archived | outdated | maintenance only | no longer maintained | 不再更新 | 停更 | 删库 | sunset`
- 命中 → 不 reject，降级为 watch，标记 `status: deprecated`
- 小白文档头部**强制加 `⚠️ 已停更（最后更新 <date>）` 标记**

LLM 二轮语义 reject：buzzword 无实现、空壳、awesome-list 型、本质不符。

### Step 5：LLM 重排序 + Top 3-5

| 维度 | 权重 | 说明 |
|---|---|---|
| 意图匹配度 | 高 | 是否真解决用户描述的问题 |
| 实现质量信号 | 中 | 代码可读性、README 实操内容 |
| 软偏好命中 | 中 | soft_preferences 命中数 |
| 活跃度 | 低 | last_commit、contributor 数 |
| stars | 最低 | **明确降权** |

**输出 3-5 个**（候选 ≥5 强制 5；<5 按实际）。

### Step 6：生成小白说明文档

`./gitout/<domain>/entries/<owner>__<name>.md`：

```markdown
---
type: repo
repo: <owner/name>
domain: <domain>
status: active | deprecated | watch
discovered: <today>
last_reviewed: <today>
intent_matched: "<对应 intent.what 的简写>"
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

> ⚠️ **已停更（最后更新 YYYY-MM-DD）**  ← 仅 status: deprecated 时加

# <项目名> · 小白说明书

## 🧐 这是什么
<一句话本质，不抄 README。>

## 💡 解决什么问题
<代入式痛点 2-3 条。>

## 🎯 谁该用 / 谁别用
**适合你如果：** <2-3 条>
**别浪费时间如果：** <2-3 条>

## 🚀 三分钟上手
```bash
<具体最小命令>
```

## 🔑 关键文件 / 关键概念
- `<path>` — <作用>

## ⚠️ 踩坑提示
- <真实坑点>

## 🤔 为什么这次推它给你

**三句硬模板**（每行必须有，下次起强制；现存 68 entry 不回填）：

1. **命中 intent.what：** <本 repo 怎么对上用户问的核心 X>
2. **命中 soft pref：** <本 repo 满足了哪条 soft_preferences>
3. **没命中的 trade-off：** <承认 anti_patterns / 反向偏好里没满足的部分>

---
*由 /gitout 生成 · <date> · intent: "<原始自然语言输入>"*
```

**写作硬约束：**

1. 正文 ≤ 1000 字（`--quick` 模式 300-500 字）
2. 小红书风格、第二人称"你"、emoji 小标题
3. 全中文，代码/标识符保留英文
4. 不抄 README、必须含"谁别用"、不打数字分
5. **"为什么这次推它给你"三句必须齐**

### Step 7：更新索引 + INDEX 自检 + 结构化汇报

#### 7.1 更新 domain 内
- `./gitout/<domain>/index.yaml` append entries
- `./gitout/<domain>/README.md` 更新健康度
- 在 README 末尾 append 本轮 **反思一句**：
  `> 反思 <date>：最低效环节 = <X>，下次改 <Y>`

#### 7.2 INDEX.md 一致性自检（**硬性收尾**）

```bash
# 列实际 entries
for d in gitout/*/; do
  domain=$(basename "$d")
  [ "$domain" = "raw" ] || [ "$domain" = "retros" ] && continue
  ls "$d/entries/" 2>/dev/null | sed "s|^|$domain/entries/|"
done | sort > /tmp/actual_entries.txt

# 列 INDEX.md 引用的 entries
grep -oE '\(\./[a-z-]+/entries/[^)]+\.md\)' gitout/INDEX.md \
  | sed 's|[()./]||g; s|^|  |' | sort > /tmp/indexed_entries.txt

diff /tmp/actual_entries.txt /tmp/indexed_entries.txt
```

- diff 有缺失（actual 多于 indexed）→ **自动 append 行到 INDEX.md 对应 domain 小节**
- diff 有孤儿（indexed 多于 actual）→ **告警，不自动删**

#### 7.3 raw 归档检查
- `find gitout/raw -mindepth 1 -maxdepth 1 -type d -mtime +90`
- 命中 → 提示用户 `/gitout prune` 归档；**不自动删**

#### 7.4 结构化汇报模板（每次必须按此输出）

```
## /gitout 跑完汇报

**意图**
- input_type: <brand|need|mixed>
- what: <...>
- 关键约束: <...>

**检索漏斗**
- query 数: N (有效 M / 零返回 K)
- 候选池: X → 一轮 reject: Y → 二轮 reject: Z → 入选: W

**文件路径**
- 新增 entries: ./gitout/<domain>/entries/{a.md, b.md, ...}
- raw 归档: ./gitout/raw/<date>/<slug>/
- INDEX 自检: OK / 已补 N 行 / 孤儿 X 条

**周边项目（如有）**
- <repo1> — <为啥归周边>

**下一步建议**
- <下次跑同类主题时该调什么>
```

---

## 子命令分支

### `/gitout list`
读 `./gitout/*/index.yaml`，按 domain 分组列出 entry 和 `intent_matched`。

### `/gitout open <repo>`
模糊匹配 entry 文件，Read 后呈现。

### `/gitout prune`
扫 `./gitout/<domain>/entries/*.md`：
- `last_reviewed` 超 30 天 → 提示移入 graveyard
- 单 domain entries > 30 → 红色警告
- **raw 超 90 天 → 提示打包**：
  ```bash
  tar czf gitout/raw/_archive/<YYYY-MM>.tar.gz gitout/raw/<那些日期目录>/
  rm -rf gitout/raw/<那些日期目录>/
  ```
  **只提示，不自动执行**
- 输出建议清单，**不自动删除任何内容**

### `/gitout <自然语言> --quick`
专名/快速场景的轻量模式：
- 走 Step 3a 种子探针
- **跳过 Step 4 第二轮 README 抓取**，只用 description
- 文档 300-500 字 mini 版（删 "三分钟上手"、"关键文件"两段）

---

## 批量模式（≥3 主题用 subagent 并行）

当用户一次给 ≥3 个主题（如"帮我扫 voice / iot / personal-kb 三个方向"）：

1. **主对话只做**：Step 1 意图抽取（每主题一份）+ Step 2.5 taxonomy 查表 + 最终汇总
2. **每主题派一个 subagent**：
   ```
   Agent(subagent_type: "general-purpose",
         prompt: "...Step 3-6 全流程，落到 ./gitout/<domain>/...")
   ```
3. **并行发起所有 subagent**（同一消息多个 Agent 调用）
4. 全部回来后主对话做 Step 7 INDEX 自检 + 结构化汇报

**实操经验沉淀**（2026-05-23 dev-productivity 四子域那次）：
- subagent 之间不共享上下文，每个 prompt 必须自带 domain 名、taxonomy 节选、entry 模板
- subagent 写完不要让它改 INDEX.md（主对话来做，避免并发冲突）
- 主对话 token 占用降低约 60%，单主题 30 分钟降到 10 分钟

---

## 安全边界（继承 v1.2 §7）

- **全链路只读**：仅用 `gh search` / `gh repo view` / `gh api repos/*/readme`
- 禁止任何 GitHub 写操作（issue / PR / comment / fork / clone）
- 写盘仅限 `./gitout/` 子目录 + 项目根 `.gitignore`

---

## 错误处理

- `gh` 未登录 → 提示 `gh auth login`，停止
- API 配额触顶 → 直接告知用户休息，不重试
- 所有 query 加起来 0 结果 → 反馈用户、给 2-3 个改写建议、停止
- README 抓取失败 → 该 repo 标记 reject，继续

---

## 设计借鉴说明

本 Skill 是 `radar-system-v1.2.md` 的轻量化落地版 + 自然语言增强版：

- **保留**：v1.2 的目录骨架、Repo Entry 模型、容量上限、graveyard、只读安全边界
- **简化**：v1.2 的"本地 Qwen3 粗筛 + 远端强模型 deepdive"两级引擎 → Claude Code 一步到位
- **新增**：
  - 自然语言意图抽取（Step 1）+ 输入分流
  - 多策略 query 生成 + best-match 排序（Step 3）
  - 两轮 reject + LLM 重排序 + 停更扫描（Step 4-5）
  - 小白文档"为什么推它给你"三句硬模板
  - INDEX 自检 + 结构化汇报（Step 7）
  - 批量 subagent 并行模式
  - taxonomy 外置（_taxonomy.yaml）防 domain 命名漂移
