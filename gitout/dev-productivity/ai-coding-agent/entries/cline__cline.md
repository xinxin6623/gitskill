---
type: repo
repo: cline/cline
domain: dev-productivity/ai-coding-agent
status: active
discovered: 2026-05-23
last_reviewed: 2026-05-23
intent_matched: "同一个 agent 引擎跑 CLI / SDK / VS Code / JetBrains 四种形态，工程化教科书"
signals:
  stars: 62207
  last_commit: 2026-05-23
  language: TypeScript
  license: Apache-2.0
url: https://github.com/cline/cline
absorption:
  harvested: false
  used: false
  used_in: []
---

# Cline · 小白说明书

## 🧐 这是什么
一个核心 agent 引擎打包成 CLI、SDK、VS Code 扩展、JetBrains 插件、Kanban 多 agent 面板**五种形态**的开源代理框架。原生就是"一套核心 + 多个壳"的工程范式。

## 💡 解决什么问题
- 你想要一个 agent 既能在终端跑（无头 CI/CD）又能挂在 IDE 里（人机协作），不用学两套工具
- 你想读"如何把一个 agent core 抽象出来支撑多客户端"的真实工业代码
- 你想用 Plan / Act 双模式：Plan 模式让它先理解和规划，确认后切 Act 模式才动手

## 🎯 谁该用 / 谁别用
**适合你如果：**
- 你重度用 VS Code 或 JetBrains，希望编辑器里有个能跑命令、改文件的 agent
- 想看一份成熟的 TypeScript agent 框架代码（diff 审查、checkpoint、tool approval 都做了）
- 想用 `@cline/sdk` 在自己的产品里嵌入 agent

**别浪费时间如果：**
- 你想要纯 Python 栈（Cline 是 TypeScript）
- 你抗拒 IDE 集成，只要纯 CLI 那 Aider 更轻
- 你已经全套 Claude Code，Cline 的 CLI 体验和 Claude Code 高度重叠

## 🚀 三分钟上手
```bash
# CLI 模式
npm i -g cline
cline

# 或在 VS Code Marketplace 装扩展，搜 "Cline"
# SDK 模式
npm install @cline/sdk
```

## 🔑 关键文件 / 关键概念
- `sdk/` — 核心 agent 引擎，所有形态共用
- `sdk/apps/cli/` — 终端壳
- Plan vs Act — 两种模式切换，是 Cline 标志性设计
- Checkpoint — 每次编辑可回滚的快照机制

## ⚠️ 踩坑提示
- VS Code 扩展现在还在迁移到 monorepo 里，目录会变
- 默认每个 tool call 都要你点确认，长任务请开 auto-approve（自担风险）
- 自带浏览器 use（让它打开网页看效果），但占资源很猛

## 🤔 为什么这次推它给你
你想要"skill ide coding harness 工程"，Cline 把"一套 agent 核心 + 多个 UI 壳"的工程模式做到了开源圈最完整。和 Claude Code（闭源、单形态）比，Cline 让你看到**怎么把同一个 agent 跑在 5 个地方**——这正是你想学的"engineering"。trade-off 是 TypeScript 栈，Python 用户可能要硬啃。

---
*由 /gitout 生成 · 2026-05-23 · intent: "个人提效工具，skill ide codeing harness 工程"*
