# decisions.md — 人工 override 累计记录

每次 /gitout 跑完后，如果对结果有异议（该 reject 的没 reject、排序不对、漏推了好项目），
记录在此。积累足够 override → 提炼进 `rubrics/*.md`。

> 这是 Rubric-as-Interface 的反馈入口：改 rubric 是治本，改 entry 是治标。
> 改 rubric 时 `git commit -m "rubric: <which> <change>"`，演化历史就是系统的"学习曲线"。

## 格式

```
### YYYY-MM-DD · <domain> · <owner/repo 或 "整体排序">
- **LLM 决策**: reject | 入选 | 排第 N
- **我的决策**: reject | 入选 | 该排第 N
- **理由**: 一段话，说清楚为什么 LLM 错了
- **是否已改 rubric**: yes（指向 commit）/ no（待积累）
```

---

<!-- override 记录从此处往下追加 -->

### 2026-07-07 · feishu-bitable-flow · 零返回 query 归因

- **LLM 决策**: 生成 4 条零返回 query（q3-q4, q6-q7），直接记 discarded 跳过
- **根因**: 词太多（query 超 3 词），违反 scan.md 已有"单 query ≤ 3 词"规则，LLM 未自检
- **零返回 query**:
  - `lark-base bitable automation` (3 词，命中 GitHub 无结果)
  - `feishu workflow automation bitable` (4 词，超长，GitHub AND 匹配失效)
  - `feishu bitable sdk` (3 词，命中 0 —— 飞书 SDK 仓库描述不用 "sdk" 关键词)
  - `lark suite bitable` (3 词，"suite" 太正式，GitHub 仓库用 "lark" 不带 "suite")
- **已改 rubric**: yes → `rubrics/scan.md` v2.1 加"query 长度自检"表 + "零返回根因归因"决策树（词太多→自动拆、冷门→换词、伪需求→记 decisions）
- **下次行为**: query 生成后按空格切词计数，>3 词自动拆成 2 条更短的，不等"下次注意"

### 2026-07-07 · feishu-bitable-flow · 候选池偏窄预警

- **LLM 决策**: 82 条去重后候选池达标（目标 15-20，实际 82）
- **但**: 有效 query 只有 5/9（44%），说明 query 策略命中率低
- **根因**: need 模式下"主题词+特性词"组合词太长，GitHub search 对长 query 不友好
- **是否已改 rubric**: yes（同上 scan.md v2.1 的 query 长度自检）
- **观察项**: 下次 need 模式跑完后，统计"有效 query / 总 query"比率，若持续 < 60% 说明 query 生成策略需重写（可能该改用 GitHub topics 而非关键词）
