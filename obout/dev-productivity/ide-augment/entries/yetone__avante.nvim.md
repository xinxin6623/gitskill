---
type: repo
repo: yetone/avante.nvim
domain: dev-productivity/ide-augment
status: active
discovered: 2026-05-23
last_reviewed: 2026-05-23
intent_matched: "在 Neovim 里复刻 Cursor 体验，含 ACP 协议、avante.md 项目规则"
signals:
  stars: 17917
  last_commit: 2026-05-22
  language: Lua
  license: Apache-2.0
url: https://github.com/yetone/avante.nvim
absorption:
  harvested: false
  used: false
  used_in: []
---

# avante.nvim · 小白说明书

## 🧐 这是什么
一个 Neovim 插件，把 Cursor 的"边聊边改、一键 apply diff"体验搬进 Vim 操作流。底层有 Rust 模块加速，支持 Agent Client Protocol (ACP) 直接对接 claude code / gemini-cli / codex。

## 💡 解决什么问题
- 你重度 Neovim 用户，不想为了 AI 改去用 Cursor 牺牲 Vim 肌肉记忆
- 你想要"项目级 AI 行为定制"（在 repo 根放 `avante.md` 写规则，类似 CLAUDE.md）
- 你想在终端里有 vibe coding 体验但保留 Vim 文本对象、easymotion、各种 nvim 插件

## 🎯 谁该用 / 谁别用
**适合你如果：** Neovim 用户想要 Cursor 同款体验；想研究 Lua + Rust 混合插件的工程组织；想理解 ACP 怎么对接外部 agent
**别浪费时间如果：** 你用 VSCode（去看 Continue / Cline）；你不熟 Vim 配置（这个不是傻瓜级开箱即用）

## 🚀 三分钟上手
```lua
-- lazy.nvim
{
  "yetone/avante.nvim",
  event = "VeryLazy",
  build = "make",  -- 编译 Rust 模块
  opts = {
    provider = "claude",
    -- 或 "openai" / "copilot" / "ollama"
  },
  dependencies = {
    "nvim-treesitter/nvim-treesitter",
    "stevearc/dressing.nvim",
    "MunifTanjim/nui.nvim",
  },
}

-- 然后 alias 一个 Zen 模式入口（类似 claude code 启动方式）
-- alias avante='nvim -c "lua require(\"avante.api\").zen_mode()"'
```

## 🔑 关键文件 / 关键概念
- `lua/avante/` — 核心 Lua 代码，看 `providers/` 学多 LLM adapter 结构
- `crates/avante-*` — Rust 模块（tokenizer、diff、模糊匹配），插件性能瓶颈下沉到原生层
- `avante.md` 项目根文件 — 类似 CLAUDE.md，定义 AI 在这个 repo 里的角色 / 使命 / 编码规范
- ACP support — 可以把 claude code 当后端跑，UI 用 nvim

## ⚠️ 踩坑提示
- 第一次装要 `make` 编译 Rust 模块，需要 cargo
- 迭代很快，配置项经常变；锁版本或者每次升级看 CHANGELOG
- Zen Mode 是"看起来像 CLI 但其实是 nvim"，初学者会被切换交互搞迷

## 🤔 为什么这次推它给你
你提到"harness 工程"——avante 把"LLM 客户端"这个角色做成了可插拔的 harness：上层 UI 是 nvim，下层 agent 可以是 claude code / gemini-cli。同时它的 `avante.md` 规则文件思路和你正在用的 CLAUDE.md / skill 体系完全同构。trade-off：Lua 配置门槛 + 还在快速变。

---
*由 /gitout 生成 · 2026-05-23 · intent: "个人提效工具，skill ide codeing harness 工程"*
