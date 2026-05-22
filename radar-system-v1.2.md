# 个人技术雷达系统 设计方案 v1.2

| 项目          | 说明                                             |
| ----------- | ---------------------------------------------- |
| 版本          | v1.2(融合 v1.0 平台版反馈 + v1.1 个人化收缩)              |
| 日期          | 2026-05-20                                     |
| 状态          | 待审核                                            |
| 适用范围        | 个人开发者技术吸收系统,单人维护,3-12 个月生命周期                  |
| 依赖基础设施      | 已有 Agent Kernel + Vault + LiteLLM + MCP        |
| 预计实施周期(MVP) | 3 周(单方向首闭环),9 周(完整三方向)                        |

---

## 摘要

本方案在前两版讨论基础上,把"技术雷达"从一个**通用 agentic 发现系统**,收缩为一个**面向个人开发者、带容量硬上限、以"吸收率"为核心指标的技术消化系统**。

最核心的认知转变是:**雷达的价值不在"发现多少",而在"被吸收多少"**。围绕这条主线,系统在数据模型、流水线、Skill 设计、可观测性四个维度做了一致性收敛。

关键设计承诺:

- 月吸收目标:每月至少 2–4 个外部项目的设计或代码片段被实际引用进个人项目
- 单方向容量硬上限:活跃 repo ≤ 30、pattern ≤ 20、snippet ≤ 50、open question ≤ 10
- 安全默认:雷达全链路只读,任何写操作需显式 skill 授权(MCP Trust Tier 强制隔离)
- 不引入新基础设施,不重写主干,可在 3 周内完成首方向闭环验证

---

## 一、系统目标与非目标

### 1.1 目标

每周稳定发现 5–15 个高质量项目,经本地粗筛后 1–3 个进入深度分析,**最终每月至少 2–4 个进入实际项目**(代码引用、架构借鉴、或文档化的 pattern 沉淀)。

### 1.2 非目标(MVP 阶段明确不做)

- 不做全网技术信号覆盖,HN / arXiv / Papers with Code 等次级信源不在首期接入
- 不做大规模 contributor / dependency / fork-tree 图谱(数据量不足前无意义)
- 不做实时推送或日推 TTS(已验证会制造"伪学习感")
- 不做自动删除(改用 stale → archive 双阶段降级)
- 不主动同时开多方向(首方向跑透 90 天再扩张)

### 1.3 反模式

以下做法已在前两版讨论中验证有害,本系统明确拒绝:

- 累积式 inbox(产生知识债)
- 数字化精确评分(如 `score: 8.5`,产生伪精确感)
- 多方向同时开荒(注意力被稀释)
- 评估只看产出数量(忽略真实吸收行为)

---

## 二、设计原则

| 原则           | 含义                                       | 落地点                                |
| ------------ | ---------------------------------------- | ---------------------------------- |
| 问题驱动 ≥ 70%   | 雷达 query 主要由 `questions.md` 中的具体问题派生     | `radar.scan` 必须挂接 question id     |
| Rejection-first | Triage 输出三档(reject / maybe / deepdive),先快速丢垃圾 | `radar.triage` rubric              |
| 容量上限         | 每个方向硬上限,超过则触发 prune                      | `index.yaml` 自检 + 月度 review        |
| Pattern 沉淀   | repo 会过时,pattern 不会;repo 必须沉淀为 pattern   | 被动相似度检测 + 主动周回顾                    |
| 安全边界         | 雷达全链路默认只读,写操作显式授权                        | MCP Trust Tier + Skill 白名单         |
| 可观测从 Day 1   | 用户事件 + LLM trace 一开始就记录                  | `events.jsonl` + LiteLLM callback  |

---

## 三、总体架构

### 3.1 四模块流水线

```
Sources                          
  ↓                              
[Module 1] Daily lightweight intake  ── GitHub MCP T0 + 手动种子
  ↓                              
[Module 2] Local triage (Qwen3 14B)  ── rejection-first,~90% 死在本地
  ↓                              
Weekly deep dive shortlist        
  ↓                              
[Module 2] Deep dive (远端强模型)     ── 经 LiteLLM 路由,每条 5K–20K token
  ↓                              
Radar entry (Repo Entry)          
  ↓                              
[Module 3] Snippet / Pattern extraction
  ↓                              
[Module 4] Usage tracking         ── Git hook + 周 review checklist
  ↓                              
Rubric update (月度)               
```

### 3.2 顶层目录

```
~/.ai-vault/
├─ skills/             # Module 入口,见第六节
├─ radar/              # Module 2-3 输出:长期知识资产
│   └─ {domain}/       # voice-pipeline / ai-agents / knowledge-base
├─ intake/             # Module 1 输出:短期候选池
│   ├─ raw/            # 原始采集,只读
│   ├─ inbox/          # 待 review 候选
│   ├─ orphans/        # 不属于任何 domain 的候选(季度 review)
│   └─ archive/        # 30 天未升级 → 自动归档(非删除)
├─ eval/               # Module 4 输出
└─ db/                 # SQLite + Parquet,可选迁移 pgvector
```

完整目录骨架见**附录 A**。

---

## 四、数据模型

### 4.1 Repo Entry

```yaml
---
type: repo
repo: owner/name
domain: voice-pipeline
status: active | watch | graveyard
decision: harvest | adopt | watch | reject
discovered: 2026-05-20
last_reviewed: 2026-05-20

# 必填:必须 map 到 questions.md 中某条具体问题
# 没有对应 question 不准进 deepdive
answers_question: "voice-pipeline/Q3"

signals:
  stars: 3200
  star_velocity: 47/week
  last_commit_age_days: 3
  active_contributors: 6

absorption:
  harvested: false
  used: false
  used_in: []           # 由 Git hook 自动写入,见 §5.1
  pattern_candidate: null  # 由相似度检测自动填,见 §5.2
---
```

正文必须包含:**一句话定位 / 对应问题 / 适合我的地方 / 不适合的地方 / 关键文件 / 可吸收片段 / 下一步**。

完整模板见**附录 B**。

### 4.2 Pattern Entry

```yaml
---
type: pattern
domain: voice-pipeline
pattern: interruptible-streaming-pipeline
source_repos:
  - owner/a
  - owner/b
  - owner/c
confidence: low | medium | high
used_in: [openclaw-voice-bot]
created: 2026-05-25
last_validated: 2026-05-25
---
```

正文:**问题描述 / 最小实现 / 参考项目 / 我的实现备忘**。

### 4.3 Questions 模型

每个 domain 维护**两个**问题文件,这是与 v1.1 的关键差异:

```
{domain}/
├─ questions.md            # 当前开放问题(≤ 10,超过必须删)
└─ questions_resolved.md   # 历史问题 + 当时的解法/参考 repo
```

`questions_resolved.md` 是长期最值钱的资产,它记录的不是项目,而是**认知演进路径**。

### 4.4 Events 模型

```jsonl
{"event": "discovered", "repo": "owner/name", "domain": "voice-pipeline", "ts": "2026-05-20T10:00:00Z", "source": "github-mcp"}
{"event": "triaged", "repo": "owner/name", "decision": "deepdive", "ts": "2026-05-20T10:01:00Z"}
{"event": "deepdived", "repo": "owner/name", "ts": "2026-05-21T20:30:00Z", "tokens": 12400}
{"event": "harvested", "repo": "owner/name", "files": ["src/utils/audio_buffer.py"], "ts": "2026-05-22T11:00:00Z"}
{"event": "used", "repo": "owner/name", "project": "openclaw-voice-bot", "commit": "a1b2c3d", "ts": "2026-05-23T15:00:00Z"}
```

事件不可变,append-only。**`used` 事件由 §5.1 描述的双重机制自动写入。**

---

## 五、关键机制(本版强化)

### 5.1 Used 检测:Git hook + 周 checklist 双重机制

这是 v1.1 最大的隐藏漏洞,本版的最优先修复。**没有可靠的 used 检测,所有 eval 指标都是装饰。**

**机制 A:Git hook 自动捕获**

在所有个人项目仓库的 `commit-msg` 或 `prepare-commit-msg` hook 中部署一段脚本,匹配 commit message 或 PR description 中的引用标记:

```
radar:owner/name              # 用了某 repo
pattern:interruptible-pipeline # 用了某 pattern
```

匹配到则向 `~/.ai-vault/eval/events.jsonl` append 一条 `used` 事件。要求自己在 commit 时养成写引用标记的习惯,**该习惯本身就是雷达系统的副作用之一,即"代码与思想来源可溯"**。

**机制 B:周 Review checklist 兜底**

每周日晚 60 分钟 review 中,本周所有 `deepdived` 状态的 entry 必须显式标记:

- `used` —— 已写进某项目
- `not_yet` —— 还在评估
- `abandoned` —— 决定不用

不允许空着进入下周。`not_yet` 累计 4 周自动降级为 `abandoned`。

### 5.2 Pattern 触发:被动检测 + 主动回顾

**被动触发:** `radar.triage` 在写入新 Repo Entry 时,先在当前 domain 的 entries 中做 embedding 相似度检索(top-3, threshold > 0.78)。若命中,自动在新 entry 中追加:

```yaml
pattern_candidate: 
  similar_to: [owner/a, owner/b]
  hint: "可能与 interruptible-streaming-pipeline 相关"
```

并在 `intake/inbox/` 中投递一条 pattern 候选提醒。

**主动触发:** Weekly review checklist 第一项固定为:

> 扫 `snippets/` 目录,检查是否有 3 个以上相似实现指向同一思想。

无主动扫描,pattern 层永远不会启动,知识库会退化成项目目录。

### 5.3 容量控制与月度 Prune

每个 domain 的 `README.md` 顶部固定包含健康度面板:

```yaml
domain: voice-pipeline
active_repos: 18 / 30
patterns: 7 / 20
snippets: 31 / 50
open_questions: 5 / 10
last_pruned: 2026-05-20
health: green | yellow | red
```

健康状态规则:

| 状态     | 触发条件                      | 处理                  |
| ------ | ------------------------- | ------------------- |
| green  | 所有指标 ≤ 80% 上限             | 正常运转                |
| yellow | 任一指标 > 80% 上限             | 下次 review 必须 prune  |
| red    | 任一指标超限,或 30 天未 review     | 停止新增 deepdive,只做整理  |

月度 Prune 规则:

1. `active_repos` > 30 → 删至 20–25,被删项目进 `graveyard.md`
2. `snippets` > 50 → 必须合并为 pattern 或删除
3. 60 天无 `used` 事件的 repo → 移入 graveyard
4. 3 个 repo 指向同一思想 → 生成 pattern,源 repo 状态降为 watch
5. 无对应 open question 的 repo → 拒绝 deepdive

### 5.4 Graveyard 制度

`graveyard.md` 不是垃圾桶,是**反查机制**,避免三个月后重复研究同一项目。

```markdown
## owner/name

淘汰日期: 2026-06-15
淘汰原因:
  - 太重,不适合个人项目
  - audio buffer 实现已被 pattern X 吸收
保留价值:
  - websocket reconnect 模式可作参考
不再 deepdive 的触发条件:
  - 除非作者发布 v2 且 README 明确说明轻量化
```

---

## 六、Skill 设计

五个 Skill 构成完整闭环,每个 Skill 必须遵守 §7 的 Trust Tier 隔离。

| Skill                  | 输入                  | 输出                              | 允许的 MCP 工具(Tier) |
| ---------------------- | ------------------- | ------------------------------- | ----------------- |
| `radar.scan`           | question id / 关键词   | `intake/raw/{date}/*.jsonl`     | T0                |
| `radar.triage`         | raw jsonl           | `intake/inbox/{date}/*.md`      | T0 + 本地 embed     |
| `radar.deepdive`       | inbox 条目 id         | `radar/{domain}/entries/*.md`   | T0                |
| `radar.find_similar`   | 自然语言 query          | top-N entries + patterns + snippets | 仅本地 db        |
| `radar.harvest`        | entry id + file 列表  | `radar/{domain}/snippets/`      | T1(仅写 snippets/) |

**`radar.find_similar` 必须额外暴露为 Claude Code slash command**,因为日常写代码时 90% 触达点在 Claude Code 里。命令形式:

```
/radar voice interrupt
/radar agent memory architecture
```

返回:3 个 repo 候选 + 2 个相关 pattern + 3 个可用 snippet,直接渲染在 Claude Code 会话中。

**这一条是吸收率能否从 5% 提升到 20% 的关键工程决定。**

---

## 七、安全边界(本版强化)

### 7.1 MCP Trust Tier 表

| Tier | 工具范围                                | 权限          | 雷达使用 |
| ---- | ----------------------------------- | ----------- | ---- |
| T0   | GitHub search / read repo / read file | 自动允许        | ✅    |
| T1   | clone / fetch selected files        | 允许,仅可写 `snippets/` | ✅(仅 harvest) |
| T2   | issue / PR / comment / repo mutation | 雷达系统禁用      | ❌    |
| T3   | shell / filesystem write / git write | 默认禁用,人工触发   | ❌    |

### 7.2 强制执行机制

不依赖人为约束,通过 **Agent Kernel 的 skill loader 白名单** 强制:

```python
# 伪代码,放在 Skill loader 中
SKILL_TIER_WHITELIST = {
    "radar.scan":         {"github-mcp": ["search", "read"]},
    "radar.triage":       {"github-mcp": ["read"], "local-embed": ["*"]},
    "radar.deepdive":     {"github-mcp": ["read"]},
    "radar.find_similar": {"local-db": ["*"]},
    "radar.harvest":      {"github-mcp": ["fetch_file"],
                          "filesystem": ["write:snippets/*"]},
}
```

任何 Skill 试图 load 白名单外的 MCP tool,Skill loader 拒绝执行并写一条 T-violation 事件到 `eval/events.jsonl`。

### 7.3 写入 Schema Validation

所有进入 Vault / snippets / db 的写操作必须先过 JSON Schema validation。Schema 文件版本化存放于 `~/.ai-vault/schemas/`,与代码一起 git track。

---

## 八、可观测性

### 8.1 双层 trace(Day 1 启用)

```
~/.ai-vault/eval/
├─ events.jsonl       # 用户级事件:discover / triage / deepdive / harvest / used
└─ llm_traces.jsonl   # 模型级 trace:由 LiteLLM callback 自动写入
```

`llm_traces.jsonl` 由 LiteLLM 的 callback hook 自动产出,零额外开发成本。这避免了 v1.1 "暂缓 Langfuse" 导致的观测窗口丢失。等数据积累到 100+ trace 后,可一次性导入 Langfuse,无迁移痛点。

### 8.2 周报指标

| 指标                              | 含义                                     | 目标            |
| ------------------------------- | -------------------------------------- | ------------- |
| `used / deepdive` (本月)          | **核心指标**,真实吸收率                         | ≥ 30%         |
| 本周新增 deepdive 数                 | 防止过度产出                                 | ≤ 5           |
| 本周新增 pattern 数                  | pattern 沉淀活跃度                          | ≥ 1 / 4 周     |
| `stale 14d` 条目数                 | 候选池消化能力                                | ≤ 当周新增 80%    |
| `signal_source → used` 漏斗       | 哪个信号源真正贡献吸收                            | 用于信源调优        |
| domain health 红黄绿               | 单方向健康度                                 | 不允许连续 2 周 red |

**有意不看的指标:** discover 总数、star 累计、模型 token 总消耗。这些数字会污染判断。

---

## 九、执行计划

### 9.1 Phase 1:Week 1–3,单方向跑通(voice-pipeline)

**Week 1:骨架与种子**

- 部署 GitHub MCP Server,挂接 Agent Kernel,验证 T0 工具可用
- 创建 `radar/voice-pipeline/` 完整目录骨架(见附录 A)
- 写 `questions.md` 初版 5–8 条具体问题(附录 C 已起草)
- 写 `radar.triage/SKILL.md` 初版 rubric(附录 D 已起草)
- 手动添加 5–10 个种子 repo 作 triage 训练集

**Week 2:接入 MCP + 本地粗筛**

- 完成 `radar.scan` + `radar.triage` 两个 Skill
- 部署 Mac mini cron:每日一次 `gh search repos` → Qwen3 14B triage → `intake/inbox/`
- 部署 LiteLLM callback,启动 `llm_traces.jsonl`
- 每日上限:新增 maybe ≤ 5;每周上限:deepdive ≤ 5

**Week 3:召回 + 使用追踪**

- 完成 `radar.deepdive` + `radar.find_similar` + `radar.harvest`
- 在 `openclaw-voice-bot` 等活跃项目部署 Git hook
- 把 `radar.find_similar` 包成 Claude Code slash command
- 首份周报:`eval/weekly/2026-W23.md`

**Week 3 结束唯一成功标准:**

> 我能在 Claude Code 中 `/radar voice interrupt`,得到 1–3 个候选,最终把其中一个的代码片段或设计实际抄进了某个项目。**这一个完整闭环走通,胜过任何架构图。**

### 9.2 Phase 2:Month 2,加 ai-agents

仅当 Phase 1 满足以下条件才启动:

- voice-pipeline 至少有 1 个 pattern entry
- `used / deepdive` 至少有 1 次非零事件
- 30 天内无 red 状态

### 9.3 Phase 3:Month 3,加 knowledge-base

启动条件同上,且 voice-pipeline + ai-agents 各自健康度 ≥ yellow。

### 9.4 扩张限制

**永远不主动开第 4 个方向**,除非某个方向连续 3 个月健康 green 且月吸收 ≥ 3。这一条是本系统能否长期存活的最强约束。

---

## 十、成功标准与失败信号

### 10.1 成功标准

| 时间点         | 标准                                         |
| ----------- | ------------------------------------------ |
| Week 3 结束   | 单方向首闭环走通,至少 1 次实际代码引用                     |
| Month 1 结束  | ≥ 1 个 pattern entry,`used/deepdive` ≥ 20%  |
| Month 3 结束  | 三方向就位,月吸收 2–4,所有方向健康度 ≥ yellow            |
| Month 6 结束  | `questions_resolved.md` 累计 ≥ 15 条,可见认知轨迹  |

### 10.2 失败信号(任一触发即重新评估系统)

- 连续 2 周无新 `used` 事件
- 任一 domain 连续 2 周 red 状态
- `inbox` 累计 > 30 条未处理(信息债复发)
- 周 review 连续 2 周未发生(执行力崩溃)
- 月度 prune 不发生(容量上限失守)

### 10.3 退场标准

若 Month 3 结束时仍未达到"月吸收 ≥ 2",则:

1. 停止系统继续扩张
2. 进入 90 天观察期,只做手动 review
3. 若观察期内手动吸收仍 < 2/月,确认系统 ROI 不成立,关闭项目并归档至 `~/.ai-vault/sunset/`

---

## 十一、决策点(需审批确认)

以下决策已采用默认答案推进,若上级有不同意见请在 review 时指出:

| #  | 决策内容                          | 默认答案                                            | 备选                                |
| -- | ----------------------------- | ----------------------------------------------- | --------------------------------- |
| D1 | `used` 检测机制                   | Git hook + Weekly checklist 双重                  | 仅 hook / 仅 checklist / 反向扫描       |
| D2 | Entry 语言策略                    | YAML frontmatter 英文,正文中文,标识符英文                  | 全中 / 全英                           |
| D3 | 不属于任何 domain 的优质 repo 处理      | 进 `intake/orphans/`,季度 review                   | 直接 reject / 强行塞入最近 domain         |
| D4 | Weekly review 时间              | 周日 20:00–21:00,固定日历事件                          | 周六上午 / 周五晚                        |
| D5 | 首期方向选择                        | voice-pipeline(咬合最紧)                            | ai-agents 优先                      |
| D6 | DB 选型                         | Week 1 仅 SQLite + Parquet,不上 pgvector          | Day 1 直接上 pgvector                |

**任一决策反转都不需要重新设计架构,仅需调整 schema 与 cron 配置。**

---

## 十二、风险与缓解

| 风险                            | 概率 | 影响 | 缓解措施                                       |
| ----------------------------- | -- | -- | ------------------------------------------ |
| `used` 检测失效,eval 漏斗变成空跑       | 中  | 致命 | 双重机制(§5.1),首周即验证 hook 正常触发                |
| 三个月后失去耐心,系统进入僵尸态              | 高  | 高  | 容量上限 + 周 review 日历事件 + Month 3 退场标准       |
| GitHub API 配额耗尽(在京网络放大此风险)   | 中  | 中  | 全部走 GitHub MCP(走索引,非 API 轮询);本地粗筛吸收 90% 流量 |
| MCP 工具 prompt injection 风险    | 中  | 高  | Trust Tier 强制隔离(§7.2),雷达全链路只读             |
| 知识库膨胀至无法维护                    | 中  | 高  | 硬上限 + 月度 prune + Graveyard                 |
| Pattern 层永远是空的                | 高  | 中  | 被动相似度检测 + 主动周回顾(§5.2)                     |
| 模型粗筛误杀好项目                     | 中  | 中  | Triage 输出包含 `reason`,周 review 抽检 reject 样本 |

---

## 十三、资源与成本估算

| 项目                      | 估算                          |
| ----------------------- | --------------------------- |
| 开发投入(MVP 3 周)           | ~30–40 工时                   |
| 月度维护投入                  | ~4–6 工时(每周日 1 小时 + 月度 prune 2 小时) |
| 远端模型 token 月成本(estimate) | < $15(deepdive ≤ 20 次/月)    |
| 本地推理增量功耗                | Mac mini M4 常驻,边际成本可忽略       |
| 存储                      | < 1 GB / 年                  |

---

## 附录 A:目录骨架(Week 1 即创建)

```
~/.ai-vault/
├─ schemas/
│   ├─ repo_entry.schema.json
│   ├─ pattern_entry.schema.json
│   └─ events.schema.json
├─ skills/
│   ├─ radar.scan/SKILL.md
│   ├─ radar.triage/SKILL.md
│   ├─ radar.deepdive/SKILL.md
│   ├─ radar.find_similar/SKILL.md
│   └─ radar.harvest/SKILL.md
├─ radar/
│   └─ voice-pipeline/
│       ├─ README.md                  # 健康度面板 + 关注/不关注
│       ├─ questions.md               # 当前开放问题(≤ 10)
│       ├─ questions_resolved.md      # 历史问题(无上限,长期资产)
│       ├─ index.yaml                 # 活跃 repo 索引(≤ 30)
│       ├─ entries/                   # 每个 repo 一个 .md
│       ├─ patterns.md                # 抽象模式(≤ 20)
│       ├─ snippets/                  # 代码碎片(≤ 50)
│       └─ graveyard.md               # 淘汰项目 + 原因
├─ intake/
│   ├─ raw/{YYYY-MM-DD}/
│   ├─ inbox/{YYYY-MM-DD}/
│   ├─ orphans/                       # 见决策 D3
│   └─ archive/{YYYY-MM-DD}/
├─ eval/
│   ├─ events.jsonl
│   ├─ llm_traces.jsonl
│   ├─ weekly/{YYYY-WW}.md
│   └─ source_quality.md              # 信号源贡献追踪
└─ db/
    ├─ radar.sqlite
    └─ embeddings.parquet
```

---

## 附录 B:Repo Entry 完整模板

```markdown
---
type: repo
repo: owner/name
domain: voice-pipeline
status: active
decision: harvest
discovered: 2026-05-20
last_reviewed: 2026-05-20
answers_question: "voice-pipeline/Q3"

signals:
  stars: 3200
  star_velocity: 47/week
  last_commit_age_days: 3
  active_contributors: 6

absorption:
  harvested: false
  used: false
  used_in: []
  pattern_candidate: null
---

## 一句话定位
[本质上解决什么问题,不抄 README]

## 对应问题
voice-pipeline/Q3:如何处理 barge-in?

## 适合我的地方
- ...

## 不适合我的地方
- ...

## 架构观察
- ...

## 关键文件
- `src/streaming/buffer.py:42-180` — 增量推理核心
- `src/pipeline/interrupt.py` — barge-in 状态机

## 可吸收片段
- [ ] `gh cp owner/name:src/utils/audio_buffer.py snippets/`
- [ ] `gh cp owner/name:src/pipeline/interrupt.py snippets/`

## 可抽象模式候选
- Interruptible streaming pipeline

## 下一步
- [ ] 抓取核心文件
- [ ] 在 openclaw-voice-bot 试用
- [ ] 与 owner/b 对比 interrupt 机制
```

---

## 附录 C:`voice-pipeline/questions.md` 初稿

```markdown
# voice-pipeline / 当前开放问题

## Q1. 低延迟 streaming pipeline
如何在 ASR → LLM → TTS 全链路中把端到端延迟控制在 500ms 以内?
- 关注:partial transcript 触发 LLM 的策略
- 不关注:WebRTC SFU 底层

## Q2. Partial transcript 与 LLM 触发时机
ASR partial result 在什么 confidence / token 数下应触发 LLM 增量推理?

## Q3. Barge-in 与中断状态机
用户说话打断 TTS 时,如何取消当前生成、保留上下文、快速恢复?
- 关注:cancellation token 设计 / playback queue 清理
- 不关注:多人会议场景

## Q4. Pipecat 的轻量化替代
Pipecat 架构能否简化成个人项目可维护的版本(< 2000 行核心代码)?

## Q5. 中英混合语境下 ASR/TTS 切换
Qwen3-ASR 在中英混说时的稳定性?是否需要语种检测层?

# 当前不关心
- 企业级 call center / IVR
- WebRTC SFU 底层实现
- 大规模多租户
```

---

## 附录 D:`radar.triage/SKILL.md` rubric 初稿

```markdown
# radar.triage Skill

## 目标
对 `intake/raw/` 中的候选 repo 做 rejection-first 粗筛,输出三档决策。

## 模型
本地 Qwen3 14B,温度 0.3。

## 输入
- repo metadata: name, description, stars, last_commit, languages
- README 前 2000 字
- 文件树(深度 2)

## 输出 schema
```yaml
repo: owner/name
decision: reject | maybe | deepdive
reason:
  - "..."
fit_domains:
  - voice-pipeline
answers_question_candidate: "voice-pipeline/Q3" | null
evidence:
  readme_excerpt: "..."
  file_tree_summary: "..."
  activity_signal: "last commit 3d ago, 6 active contributors"
next_action: none | read_architecture | inspect_core_file
```

## Reject 规则(任一命中即 reject)
1. README 关键词密度 > 阈值且无具体实现描述(buzzword-only)
2. 最后一次有意义提交 > 180 天
3. 明显面向企业级场景(K8s operator / multi-tenant / RBAC 关键词密集)
4. 文件树以非目标语言为主(Java / C# / .NET 等,除非问题特别需要)
5. 不能 map 到任何 fit_domain 的 open question

## Deepdive 规则(必须全部满足)
1. 至少 map 到一条 `answers_question_candidate`
2. 最近 30 天有提交
3. README 包含具体实现描述(非纯介绍)
4. 文件结构清晰,核心代码 < 5 个文件可定位

## Maybe(其他情况)
进 `intake/inbox/`,等周 review 人工确认。

## 相似度检测(同时执行)
对每条非 reject 的 repo,做 embedding 检索:
- 模型:bge-code-v1 或 jina-code-v2
- 检索范围:当前 fit_domain 的 entries
- 阈值:cosine similarity > 0.78
- 命中 ≥ 2 条 → 写入 pattern_candidate 字段

## 失败模式与抽检
周 review 抽检 5 条 reject 样本,人工复核误杀率。
连续 2 周误杀率 > 20% → 触发 rubric 调整。
```

---

## 审核请求

本方案请重点 review 以下三项:

1. **决策点 D1–D6**(§11)是否同意默认答案
2. **退场标准**(§10.3)是否合理
3. **资源估算**(§13)是否在可承受范围

如同意推进,本周即可开始 Phase 1 Week 1 实施。

---

*文档结束。版本 v1.2,2026-05-20。下一版本会在 Phase 1 结束后基于实际数据生成。*
