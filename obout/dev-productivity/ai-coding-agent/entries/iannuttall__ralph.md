---
type: repo
repo: iannuttall/ralph
domain: dev-productivity/ai-coding-agent
status: active
discovered: 2026-05-23
last_reviewed: 2026-05-23
intent_matched: "把 Claude Code / Codex / opencode 当 backend 的极简 agent loop，文件即记忆"
signals:
  stars: 924
  last_commit: 2026-02-04
  language: TypeScript
  license: MIT
url: https://github.com/iannuttall/ralph
absorption:
  harvested: false
  used: false
  used_in: []
---

# Ralph · 小白说明书

## 🧐 这是什么
一个**只有几百行 TypeScript 的极简 agent loop**，把 PRD（JSON 写需求） + git + 文件夹当"agent 的记忆"，每次迭代起一个干净的 claude / codex / droid / opencode 子进程做一个 story，做完 commit、清空、做下一个。

## 💡 解决什么问题
- 你已经有 Claude Code / Codex CLI，但**它们没有循环驱动机制**——Ralph 给你套一层 outer loop
- 你想要"AI 写完一个 story 自动开始下一个"的无人值守模式，但又不想搞一套 OpenHands 那种重量级架构
- 你想读"agent loop 最小可行实现"的代码，理解原理

## 🎯 谁该用 / 谁别用
**适合你如果：**
- 已经付费 Claude Max / Codex，想榨干用更多
- 喜欢"文件即真理、git 即历史"的工程哲学
- 想自己 fork 一个改造，但需要一个 100% 看得懂的起点

**别浪费时间如果：**
- 你想要开箱即用的完整产品（Ralph 是个 framework，需要你写 PRD、配 AGENT_CMD）
- 你不喜欢"另起一个进程跑 CLI"这种胶水做法，想要原生 SDK 集成
- 你的任务很简单，不需要拆 story（直接用 Claude Code 就行）

## 🚀 三分钟上手
```bash
npm i -g @iannuttall/ralph
ralph prd               # 交互式生成 PRD（JSON 描述 stories）
ralph build 1           # 跑一次循环：选 1 个 open story，做完 commit

# 切 backend
# 编辑 .agents/ralph/config.sh
AGENT_CMD="claude -p --dangerously-skip-permissions \"\$(cat {prompt})\""
# 或 codex / droid / opencode
```

## 🔑 关键文件 / 关键概念
- `.agents/tasks/prd-*.json` — 你写的需求，含 stories 列表
- `.ralph/progress.md` — append-only 进度日志
- `.ralph/guardrails.md` — "Signs"，agent 学到的教训会记这
- `AGENT_CMD` — 真正干活的 CLI，Ralph 只负责调度

## ⚠️ 踩坑提示
- 最近一次 commit 是 2026-02，相对其他项目更新慢，但代码量小，自己维护成本低
- 强制要求 git，每个 story 一个 commit，不喜欢可以 `--no-commit`
- 需要先装好 backend agent（claude / codex 任一），Ralph 自己不会调 LLM

## 🤔 为什么这次推它给你
你最近在做 /gitout 这种**用 Claude Code 当原语、自己写 harness** 的工程。Ralph 思路一模一样：**别重新发明 agent，把现成的 Claude Code 包一层 loop**。代码极简（一个下午能读完）、概念清晰（文件就是 memory）、可切换 backend——这是给你"看完直接想抄"的项目。trade-off 是社区小、生态浅，要点自己动手能力。

---
*由 /gitout 生成 · 2026-05-23 · intent: "个人提效工具，skill ide codeing harness 工程"*
