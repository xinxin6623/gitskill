---
type: repo
repo: dollspace-gay/OpenClaudia
domain: dev-productivity/ai-coding-agent
status: active
discovered: 2026-05-23
last_reviewed: 2026-05-23
intent_matched: "Rust 写的 Claude Code 复刻品，支持任意 LLM provider 和本地模型"
signals:
  stars: 71
  last_commit: 2026-05-22
  language: Rust
  license: MIT
url: https://github.com/dollspace-gay/OpenClaudia
absorption:
  harvested: false
  used: false
  used_in: []
---

# OpenClaudia · 小白说明书

## 🧐 这是什么
一个**用 Rust 实现的 Claude Code 风格通用 agent harness**，把 Claude Code 的核心体验（30+ 工具、skills、hooks、subagent、worktree、plan mode）做成开源版，并且**任何 LLM 都能驱动**——Anthropic、OpenAI、Gemini、DeepSeek、Qwen、Ollama 本地模型都行。

## 💡 解决什么问题
- 你喜欢 Claude Code 的体验，但**想用本地 Ollama / DeepSeek**省钱或离线
- 你想要 Claude Code 的 skills / hooks / subagent 这套语义，但希望底层是**开源、可读、可改**的
- 你想看一份**用 Rust 写 agent harness** 的工程参考（生态里多是 Python / TS）

## 🎯 谁该用 / 谁别用
**适合你如果：**
- 你已经习惯 Claude Code 的 skills / hooks 思维，想在它之外有备份方案
- 想跑本地模型当主力（隐私、成本敏感）
- 喜欢 Rust，想要单文件二进制部署的 CLI agent

**别浪费时间如果：**
- 你只信任 star 多的大项目（这个只有 71 stars，单一作者）
- 你不会写 Rust，未来想自己改它
- 你的工作流深度依赖 Claude Code 自己的 plugin 生态（OpenClaudia 是仿，不是兼容）

## 🚀 三分钟上手
```bash
# 需要先装 Rust（rustup）
git clone https://github.com/dollspace-gay/openclaudia.git
cd openclaudia
cargo install --path .

# 跑起来，自动识别 provider
openclaudia -m gemini-2.5-flash
openclaudia -m deepseek-chat
openclaudia -m ollama:qwen2.5-coder
```

## 🔑 关键文件 / 关键概念
- `Behavioral Modes` — 三轴（agency / quality / scope）8 个预设
- `VDD（Verification-Driven Development）` — 用另一个 model 当对抗审查员
- `ACP Server` — Agent Control Protocol，stdin/stdout 接其他 agent
- `skills/` — markdown 写的可复用 prompt skill，和 Claude Code 兼容思路

## ⚠️ 踩坑提示
- 71 stars 单一作者项目，生产环境用要谨慎，把它当**学习样本 + 个人副驾**最合适
- 需要 Rust toolchain，第一次 `cargo build` 慢
- Windows 上强制依赖 Git Bash

## 🤔 为什么这次推它给你
你用 Claude Code，但 Claude Code **闭源**——你看不到它内部 loop、hooks、subagent 怎么实现的。OpenClaudia 几乎逐项复刻 Claude Code 的语义，**Rust 源码公开**。读它等于读"Claude Code 长什么样"的逆向工程版本。同时它解锁了 Claude Code 不支持的多模型（特别是本地 LLM）。trade-off：项目新、星少、稳定性比不上前面四个，定位是**学习 + 备份**而不是主力。

---
*由 /gitout 生成 · 2026-05-23 · intent: "个人提效工具，skill ide codeing harness 工程"*
