---
type: repo
repo: continuedev/continue
domain: dev-productivity/ide-augment
status: active
discovered: 2026-05-23
last_reviewed: 2026-05-23
intent_matched: "把 AI 检查变成可版本控制的 markdown 文件，IDE 编辑、CI 强制"
signals:
  stars: 33334
  last_commit: 2026-05-22
  language: TypeScript
  license: Apache-2.0
url: https://github.com/continuedev/continue
absorption:
  harvested: false
  used: false
  used_in: []
---

# Continue · 小白说明书

## 🧐 这是什么
一个开源 AI 编程助手框架：既能在 VSCode / JetBrains 里当 Copilot 替代品，也能把"AI 审查规则"写成 markdown 提交到仓库，在 CI 里作为 GitHub Status Check 跑。

## 💡 解决什么问题
- 你想要 Copilot/Cursor 体验，但要换 LLM、跑本地模型、对接公司私有部署
- 你不想让 AI 提示词散落在每个人的 Cursor 配置里，而是希望"安全审查、风格审查"作为可版本控制的检查规则进仓库
- 你想把 IDE 里的 AI 助手和 CI 检查共用同一套 prompt + context

## 🎯 谁该用 / 谁别用
**适合你如果：** 团队需要可控可审计的 AI；你写 VSCode/JetBrains 插件想找架构样板；你想自托管 AI 助手并对接私有模型
**别浪费时间如果：** 你只是单兵开发想要 Copilot 即插即用（直接用 Copilot 更省事）；你不接受 monorepo + 复杂 build

## 🚀 三分钟上手
```bash
# CLI（本地或 CI 跑 AI 检查）
curl -fsSL https://raw.githubusercontent.com/continuedev/continue/main/extensions/cli/scripts/install.sh | bash

# 或者直接装 VSCode 扩展：在市场里搜 "Continue"
# 然后在仓库根加 .continue/checks/security.md 写检查 prompt
```

## 🔑 关键文件 / 关键概念
- `extensions/vscode/` — VSCode 扩展源码，看完你也能写一个 IDE AI 插件
- `extensions/intellij/` — Kotlin 写的 JetBrains 插件
- `extensions/cli/` — `cn` CLI 工具，CI 里跑 AI 检查的入口
- `core/` — 核心逻辑（context provider、LLM adapter、agent loop），跨编辑器复用
- `.continue/checks/*.md` — 用户仓库里写的检查规则，纯 markdown + YAML frontmatter

## ⚠️ 踩坑提示
- Monorepo 很大，第一次 clone 慢；想看插件实现直接进 `extensions/`
- 2025 年项目方向从纯 IDE 助手往"AI checks in CI"转，README 重点变了，但 IDE 插件依然在维护
- 自托管 LLM 时注意 context window 配置，默认是为 GPT-4 级别调的

## 🤔 为什么这次推它给你
你的诉求是"skill / IDE / coding harness 工程"，Continue 同时给了三件事：跨编辑器插件架构样板（VSCode + JetBrains 复用 core）、把 prompt/skill 变成仓库里的 markdown 文件（和你 ~/knowledge wiki 思路同源）、还有完整的 CLI + CI 整合路径。trade-off 是项目体量大、上手成本高于"装个插件就完事"。

---
*由 /gitout 生成 · 2026-05-23 · intent: "个人提效工具，skill ide codeing harness 工程"*
