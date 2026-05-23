---
type: repo
repo: BayramAnnakov/claude-reflect
domain: dev-productivity/claude-workflow
status: active
discovered: 2026-05-23
last_reviewed: 2026-05-23
intent_matched: "把'纠错 Claude'这件事自动沉淀到 CLAUDE.md，再从历史会话挖出可复用 skill"
signals:
  stars: 1041
  last_commit: 2026-03-16
  language: Python
  license: MIT
url: https://github.com/BayramAnnakov/claude-reflect
absorption:
  harvested: false
  used: false
  used_in: []
---

# claude-reflect · 小白说明书

## 🧐 这是什么
一个让 Claude Code "记住你每次纠错"的自学习系统。你说"不是 gpt-5，是 gpt-5.1"，hook 把这条 correction 入队；你跑 `/reflect` 时人工确认，自动写进 CLAUDE.md。v2 还能扫历史 session 找出"你重复问过 12 次类似问题"的 pattern，提议把它做成一个 slash command。

## 💡 解决什么问题
- 同一个错你纠正 Claude 十遍，下次它还是错——因为没写进 memory
- CLAUDE.md 越写越乱，没人有耐心定期整理 / 去重
- 你做过的重复操作（"每天问 productivity 复盘"），其实早该提炼成 skill，但你没意识到

## 🎯 谁该用 / 谁别用
**适合你如果：**
- 你的 CLAUDE.md 已经一团乱，想要个自动整理工具
- 你想看"如何用 hook 监听用户纠错"的工程实践
- 你想从历史 session 里 mining 出 skill 候选

**别浪费时间如果：**
- 你刚开始用 Claude Code，连 CLAUDE.md 都没几行
- 你不信任 AI 自动改 memory（虽然有人工确认环节）
- 你不用 Claude plugin marketplace（这个用 plugin 安装）

## 🚀 三分钟上手
```bash
claude plugin marketplace add bayramannakov/claude-reflect
claude plugin install claude-reflect@claude-reflect-marketplace
# 重启 Claude Code 让 hook 生效
# 用一段时间后
/reflect              # 处理队列里的纠错，人工 review 后写入 CLAUDE.md
/reflect-skills       # 从最近 14 天 session 找 skill 候选
```

## 🔑 关键文件 / 关键概念
- **Stage 1: Capture（自动）** — hook 监听用户消息，识别"不是 X 是 Y"模式，入队
- **Stage 2: Process（手动 `/reflect`）** — 队列里的 correction 经 confidence score 排序，你确认后落盘
- **`/reflect-skills`** — 跨 session 分析，找出重复 pattern 提议生成 skill
- **`/reflect --dedupe`** — CLAUDE.md 长了之后做去重合并
- **decay**：旧的 correction 信心分会衰减，避免一年前的偏好污染当前 memory

## ⚠️ 踩坑提示
- 默认 hooks 自动跑、但 `/reflect` 是手动的，避免 AI 偷偷改你的 CLAUDE.md（这是好设计）
- "Stage 1 自动捕获"靠模式识别，会漏掉非典型纠错——别期待 100% 召回
- plugin 安装机制依赖 Claude Code 最新 marketplace，老版本可能跑不起来
- 多语言支持靠 LLM 理解，但 confidence 在小语种会偏低

## 🤔 为什么这次推它给你
你要"个人提效工具 + skill 工程"。这个仓库给了两条独特价值链：
1. **CLAUDE.md 自演化** — 从"静态配置文件"变成"自动学习的 memory 库"
2. **Skill mining** — 反向工程你自己的工作流，告诉你"这个动作你已经做过 12 次，该做成 skill 了"
trade-off：plugin 形式，你得接受它写你的 CLAUDE.md（虽然有 review）。

---
*由 /gitout 生成 · 2026-05-23 · intent: "个人提效工具，skill ide codeing harness 工程"*
