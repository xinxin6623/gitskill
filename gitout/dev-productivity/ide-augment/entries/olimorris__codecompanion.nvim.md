---
type: repo
repo: olimorris/codecompanion.nvim
domain: dev-productivity/ide-augment
status: active
discovered: 2026-05-23
last_reviewed: 2026-05-23
intent_matched: "Neovim AI 协作框架：多 adapter、slash command、prompt library、MCP / ACP 全支持"
signals:
  stars: 6607
  last_commit: 2026-05-16
  language: Lua
  license: Apache-2.0
url: https://github.com/olimorris/codecompanion.nvim
absorption:
  harvested: false
  used: false
  used_in: []
---

# CodeCompanion.nvim · 小白说明书

## 🧐 这是什么
另一个 Neovim AI 助手，但走的是"框架 + 扩展点"路线：内置 prompt library、slash command、agent/tool 系统、rules 文件，所有东西都可以用户自定义。被誉为"Neovim 里最像 Zed AI 的实现"。

## 💡 解决什么问题
- 你想要 chat / inline / agent 三种 AI 交互模式，而不是只有补全
- 你想用 `CLAUDE.md`、`.cursor/rules` 这类规则文件统一管理 AI 行为
- 你想自己写 slash command（比如 `/explain-lsp-error`）、自己写 adapter 接公司内部 LLM

## 🎯 谁该用 / 谁别用
**适合你如果：** 你已经在用 avante 但想要更模块化的扩展点；你想学 Lua 写"prompt 即插件"的体系；你需要多 LLM 切换（Anthropic + Copilot + 本地 Ollama 共存）
**别浪费时间如果：** 你想要"装上就能用"零配置（这个偏框架，要写一些 lua）；你不打算自定义 prompt / command

## 🚀 三分钟上手
```lua
-- lazy.nvim
{
  "olimorris/codecompanion.nvim",
  dependencies = {
    "nvim-lua/plenary.nvim",
    "nvim-treesitter/nvim-treesitter",
  },
  opts = {
    adapters = {
      anthropic = function()
        return require("codecompanion.adapters").extend("anthropic", {
          env = { api_key = "ANTHROPIC_API_KEY" },
        })
      end,
    },
    strategies = {
      chat = { adapter = "anthropic" },
      inline = { adapter = "anthropic" },
    },
  },
}
```

## 🔑 关键文件 / 关键概念
- `lua/codecompanion/adapters/` — 多家 LLM 的统一适配层，写 adapter 的模板看这里
- `lua/codecompanion/strategies/` — chat / inline / cmd 三种交互模式的策略实现
- `lua/codecompanion/strategies/chat/slash_commands/` — slash command 实现，自己加新的扩展看这里
- `lua/codecompanion/strategies/chat/tools/` — agent 工具（file edit、shell run 等）实现
- 支持的规则文件：`CLAUDE.md` / `.cursor/rules` / 自定义路径

## ⚠️ 踩坑提示
- 配置项多，建议先抄 `:h codecompanion` 里的示例，别一次性堆所有 adapter
- ACP / MCP 支持是新功能，文档跟得不一定全，遇坑去 GitHub Discussions
- 跟 avante 选一个用就好，俩同时装会快捷键打架

## 🤔 为什么这次推它给你
你说"skill / harness 工程"——CodeCompanion 是 Neovim 生态里把"AI 插件"做成"prompt + tool 框架"做得最干净的，prompt library / slash command / rules 这套和你 ~/knowledge 里的 skill 思路完全可以拼起来。trade-off：定位偏框架，初学者会觉得选项太多。

---
*由 /gitout 生成 · 2026-05-23 · intent: "个人提效工具，skill ide codeing harness 工程"*
