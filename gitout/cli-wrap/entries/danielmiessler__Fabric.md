---
type: repo
repo: danielmiessler/Fabric
domain: misc
status: active
decision: harvest
discovered: 2026-05-22
last_reviewed: 2026-05-22
theme: cli-agent
intent_matched: "把 AI 能力做成可组合的 CLI pattern"
signals:
  stars: 41808
  last_commit: 2026-05-22
  language: Go
  license: MIT
url: https://github.com/danielmiessler/Fabric
absorption:
  harvested: false
  used: false
  used_in: []
---

# Fabric · 小白说明书

## 🧐 这是什么

一个**"把 AI 提示词当 Unix 命令用"的框架**。作者 Daniel Miessler（安全圈名人）观察到"AI 不是能力问题是集成问题"——每个聊天框都强但不能拼起来。Fabric 把高质量 prompt 整理成命名 pattern（比如 `summarize`、`extract_wisdom`、`create_quiz`），让你像用管道一样组合：`pbpaste | fabric -p summarize | fabric -p extract_wisdom`。4 万星，Go 写的，MIT。

## 💡 解决什么问题

你想用 AI 但每次都重新写 prompt 累不累：

- "总结这篇文章" 这种提示词每次都打一遍
- 想把多个 AI 步骤串起来，但 ChatGPT 网页不行
- 别人写的好 prompt 没法直接拿来用

Fabric 给你**几百个开箱即用的 pattern**（社区一直在加），CLI 直接调，标准输入输出，可以管道串。视频转录 → 提取金句 → 生成博客大纲三步走，一行命令搞定。

## 🎯 谁该用 / 谁别用

**适合你如果：**
- 命令行重度用户
- 想看"prompt as a library"该怎么组织
- 想给 OpenClaw 加一层 pattern 系统的参考

**别浪费时间如果：**
- 不熟 CLI，想 GUI 体验
- 不愿意维护本地 patterns 目录
- 只想要单次对话不需要复用

## 🚀 三分钟上手

```bash
# Mac
brew install fabric-ai

# 配 LLM key
fabric --setup

# 用一个 pattern
echo "你的内容" | fabric -p summarize

# 列出所有 pattern
fabric --listpatterns
```

## 🔑 关键文件 / 关键概念

- **patterns/** — 每个 pattern 是一个文件夹，含 system.md（系统提示）和 user.md
- **可作为 REST API 启动** — `fabric --serve` 转成服务给其他工具用
- **支持本地模型** — 接 Ollama 友好
- **Helper Apps** — Obsidian / Raycast / Alfred 等都有集成

## ⚠️ 踩坑提示

- pattern 目录默认在 `~/.config/fabric/patterns/`，第一次要 `--updatepatterns`
- Pattern 质量参差不齐，有些社区 PR 没经审核
- 配置文件位置在不同 OS 上不一样

## 🤔 为什么这次推它给你

**CLI-Anything 的姐妹参考**。你做的是"把 GUI 软件包成 CLI 让 Agent 用"，Fabric 做的是"把 AI 能力包成 CLI 让人用"。两边都在解"如何让 AI 和现有工具链 compose"的问题，但方向互补。**pattern 目录组织、CLI 输出格式（JSON/text 双模式）、Helper App 生态打法**都值得抄。pattern 候选：`prompt-as-library`、`compose-via-pipe`。

---
*由 /gitout 生成 · 2026-05-22 · theme: CLI 包装 / Agent 工具化*
