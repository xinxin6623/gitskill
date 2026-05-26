# /gitout 实跑复盘 · personality-test（MBTI 主题）

> 来源：2026-05-24 本轮 `/gitout mbit 测试 app 或程序或网页端或小程序，现在比较流行的`
> 目的：把本轮 LLM 的实际行为 vs SKILL.md 设计 的偏差记下来，提下次的搜索质量

---

## 一、本轮关键时间线

| 阶段 | 实际做了什么 | 耗时占比 | 收益 |
|---|---|---|---|
| Step 1 意图抽取 | 1 次推理 → 输出 yaml，判定 input_type=need | 5% | ✅ 顺 |
| Step 2 歧义判断 | 识别 "mbit" 是 "MBTI" 笔误 → AskUserQuestion 给 3 选项 | 5% | ✅ 关键，否则可能跑成 micro:bit |
| Step 2.5 taxonomy | 查表无命中 → 新建 personality-test domain + append yaml | 5% | ✅ 顺 |
| Step 3b 并行检索 | 5 query 后台并发 → **全部失败**（字段名 bug）→ 串行重跑 | 25% | ❌ 一轮白跑 |
| Step 4 reject + README | 40→7 一轮过滤，并行抓 7 个 README，3 个返空 | 20% | ⚠️ README 返空率高 |
| Step 5-6 重排序 + 写 5 篇 | 5 篇小白文档一次性并发 Write | 30% | ✅ 顺 |
| Step 7 索引 + 自检 | INDEX.md 三处 Edit + diff 自检 | 10% | ✅ 0 缺 0 孤儿 |

---

## 二、本轮暴露的具体问题

### 2.1 ⚠️ `archivedAt` 字段不存在（gh CLI 实际是 `isArchived`）

**现象：** 5 个 query 并行后台跑，**全部 exit 1**，错误信息：
```
Unknown JSON field: "archivedAt"
Available fields: ... isArchived, pushedAt, ...
```

**根因：** SKILL.md Step 3a / 3b 的 `--json` 列表写了 `archivedAt`（推测来自旧 gh 版本或 GraphQL API 直觉），实际 `gh search repos --json` 支持的字段名是 `isArchived`。

**影响：** 浪费一整轮 5 个并行 gh 调用（约 30s）+ 一次错误诊断。

**已修：** 同本轮 PR 把 SKILL.md 三处 `archivedAt` 改为 `isArchived`；顺手把 `pushedAt` 加进默认 `--json` 列表（一轮 reject 第一条规则要用，之前漏列）。

**给下次的硬规则：**
- SKILL.md 里所有 `gh` flag 在写之前必须先 `gh <subcommand> --help` 或 `--json help` 校对一遍
- 已经在 SKILL.md 写了"元规则"但本身没遵守过 → **下次首跑前自检 SKILL.md 里的字段名 vs `gh search repos --json help` 的实际清单**

### 2.2 ⚠️ 多个高 star repo 抓 README 返空

抓了 7 个 README，3 个返空：
- `lilemy/mbti-mini` (0 行) — 仓库本身 README 几乎是空的（合理）
- `suyadong-dev/MBTI-` (0 行) — 同上（合理）
- `MskTmi/MBTI` (10 行) — README 很短（合理但够用）

**问题：** SKILL.md 没规定"README 返空 / 极短"该怎么处理。本轮是凭直觉决定 `lilemy/mbti-mini` 仍然入选（因为命中"小程序"软偏好），但这个判断没记录在 entry 文档里，未来回溯会困惑。

**给下次的规则：**
- README 行数 < 10 → entry frontmatter 加字段 `readme_quality: thin`
- "为什么这次推它给你"第二/第三句必须明确写"README 极短，判断基于代码语言 + 仓库结构 + 软偏好命中"

### 2.3 ⚠️ Query 策略：中文 query 命中率出乎意料地高

本轮 5 个 query 里 `mbti 小程序`（中文）返回 8 条，比 `mbti react` 命中更精准（前者多为微信小程序，后者很多是 0 star 学生作业）。

**反例验证设计假设：** SKILL.md 写 "queries 全英文"，但**对于"中文文化场景特别强的主题"（MBTI、八字、命理、知乎风）中文 query 反而更准**。

**给下次的规则：**
- need 模式生成 query 时，如果意图含"中文场景"信号（小程序 / 微信 / 国产化 / 中文用户），**强制至少 1 个中文 query**
- 把 SKILL.md Step 3b "全英文" 改为 "默认全英文；命中中文场景信号时强制 1 条中文"

### 2.4 ⚠️ "现在比较流行的" 这个表述被部分忽略

用户原文 "**现在比较流行的**"，意图里我抽成 "近 2 年活跃"，但最终入选里有 `lilemy/mbti-mini` (1 star)。

**这不是错**（已经在 entry 的 trade-off 段坦白了），但 reject 阈值（"stars < 3 且 pushedAt < 90 天双低"）和"流行度"语义之间有 gap：
- "流行" ≠ "高 star"，可以是"近期增长快"、"代码活跃"、"在中文社区被讨论"
- 但 gh search 默认 sort=best-match 不一定反映流行度

**给下次的规则：**
- 用户语义含 "流行 / 火 / 热门 / 主流" 时，意图里加 `popularity_floor: 50`（star 软门槛）
- Step 5 重排序时，候选里 star < 该 floor 的项目要么进周边段，要么 entry 第三句必须明确写"不符合流行度阈值，原因是 ..."

### 2.5 ⚠️ 并行后台 Bash 失败时无 fail-fast 机制

5 个 query 并行用 `run_in_background: true` 起，**全部失败** 5 次系统通知一次性到达。如果第 1 个失败就能 fail-fast，可以省后面 4 次浪费。

**给下次的规则：**
- 同一组 query 并行时，**先串行跑 1 个验证 flag 正确性**，再并行剩下的
- 或者用 `for + &&` 串起来，单条失败立刻停（损失并行收益但换稳定性）—— 推荐前者

---

## 三、本轮做得好的（保留）

### 3.1 ✅ AskUserQuestion 用得对

"mbit" 是个明显笔误，但有 3 个合理解读（MBTI / micro:bit / Mbit 网速）。**不问就跑容易跑歪**。问完 1 次确认，5s 收敛。

→ 下次遇到 ≤4 字的可疑专名输入，**默认问一次** 比默认推断更安全。

### 3.2 ✅ 周边 / 主入选 分流

`juncheong/MBTI-Test`（React 全栈但 2023 停更）、`suyadong-dev/MBTI-`（中文小程序但过小）—— 没硬塞进 5 个主入选，单列 domain README "相关周边"。

→ 保留 SKILL.md Step 4 周边过滤规则，本轮验证有效。

### 3.3 ✅ INDEX 自检脚本一次过

`comm -23` / `comm -13` 那段一行出结果：53=53，0 缺 0 孤儿。**完全可以固化成 hook 或 prune 子命令的自动检查**。

### 3.4 ✅ "为什么这次推它给你" 三句模板执行到位

5 个 entry 都写齐了 `命中 intent.what / 命中 soft pref / 没命中的 trade-off`。`lilemy/mbti-mini` 主动承认 "star=1 不符合流行度" 这种**反推荐式坦白**是这个模板的高价值产物，下次必须坚持。

---

## 四、给下次的可执行 checklist

抄给下次跑 `/gitout` 前先看一眼：

1. [ ] **先校 flag**：第一组 query 不要并行后台，先 `gh search repos "test" --json help` 确认所有字段名存在
2. [ ] **中文场景信号**：意图含小程序/微信/国产化 → 至少 1 个中文 query
3. [ ] **流行度软门槛**：用户说"流行/热门" → 默认 popularity_floor=50 star，低于的要么进周边要么 entry 解释清楚
4. [ ] **README 返空处理**：< 10 行的 entry frontmatter 标 `readme_quality: thin`，trade-off 段必须解释
5. [ ] **并行 fail-fast**：先串行 1 个验证，再并行剩下的
6. [ ] **AskUserQuestion 触发条件**：输入 ≤ 4 字符且非常见词时默认问一次

---

## 五、需要改的 SKILL.md 条款（提议）

| 位置 | 改前 | 改后 |
|---|---|---|
| Step 3a/3b `--json` | `... archivedAt` | `... pushedAt, isArchived` （**已改**） |
| Step 3b "全英文" | "queries 全英文" | "默认全英文；命中中文场景信号时强制 1 条中文" |
| Step 4 第一轮 reject | 现有 5 条规则 | 加第 6 条："用户语义含流行度 → star < popularity_floor 进周边" |
| Step 4 README 抓取 | 取前 200 行 | 加："< 10 行 → entry frontmatter readme_quality=thin" |
| Step 6 "三句硬模板" | 现状 | 加 "若 readme_quality=thin，第三句必须解释判断基于什么" |
| 新增 Step 3 前置 | 无 | "首跑当日：跑 `gh search repos --json help` 校对字段名清单" |

---

## 六、本轮数据快照

- query 漏斗：5 query × 8 limit = 40 条 → 去重 40 条 → 一轮 reject 后 7 → README 7 → 二轮 reject 后 5
- query 命中分布：mbti test(8) / personality quiz(8) / 16personalities(8) / mbti 小程序(8) / mbti react(8) — 全打满 limit，说明 limit=8 可能偏低
- 入选 5 个的 star 分布：385 / 310 / 161 / 54 / 1（量级跨 2.5 个数量级，符合"流行 + 长尾"组合）
- 失败重跑成本：~30s gh CLI + 一次诊断 + 一次 SKILL.md hotfix —— 总 ~3 分钟，可被 Step 3 前置校验完全消除
