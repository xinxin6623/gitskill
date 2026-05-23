<!-- panvimdoc-ignore-start -->

<p align="center">
<a href="https://codecompanion.olimorris.dev"><img src="https://github.com/user-attachments/assets/64da6a69-a54d-4799-b034-59d9efd27b76" alt="CodeCompanion.nvim" /></a>
</p>

<p align="center">
<a href="https://github.com/olimorris/codecompanion.nvim/stargazers"><img src="https://img.shields.io/github/stars/olimorris/codecompanion.nvim?color=c678dd&logoColor=e06c75&style=for-the-badge"></a>
<a href="https://github.com/olimorris/codecompanion.nvim/actions/workflows/ci.yml"><img src="https://img.shields.io/github/actions/workflow/status/olimorris/codecompanion.nvim/ci.yml?branch=main&label=tests&style=for-the-badge"></a>
<a href="https://github.com/olimorris/codecompanion.nvim/releases"><img src="https://img.shields.io/github/v/release/olimorris/codecompanion.nvim?style=for-the-badge"></a>
</p>

<p align="center">A Neovim AI coding assistant for coding with LLMs (Anthropic, OpenAI, Gemini, Copilot and <a href="https://codecompanion.olimorris.dev/getting-started.html">more</a>) and AI agents. With built-in support for <a href="https://agentclientprotocol.com">Agent Client Protocol (ACP)</a>, <a href="https://codecompanion.olimorris.dev/model-context-protocol">Model Context Protocol (MCP)</a>, and agents like <a href="https://docs.anthropic.com/en/docs/claude-code/overview">Claude Code</a> and <a href="https://openai.com/codex">Codex</a></p>

<p align="center">New features are always announced <a href="https://github.com/olimorris/codecompanion.nvim/discussions/categories/announcements">here</a></p>

## :purple_heart: Sponsors

Thank you to the following people:

<p align="center">
<!-- sponsors --><a href="https://github.com/unicell"><img src="https:&#x2F;&#x2F;github.com&#x2F;unicell.png" width="60px" alt="User avatar: Qiu Yu" /></a><a href="https://github.com/jfgordon2"><img src="https:&#x2F;&#x2F;github.com&#x2F;jfgordon2.png" width="60px" alt="User avatar: Jeff Gordon" /></a><a href="https://github.com/JuanCrg90"><img src="https:&#x2F;&#x2F;github.com&#x2F;JuanCrg90.png" width="60px" alt="User avatar: Juan Carlos Ruiz" /></a><a href="https://github.com/Alexander-Garcia"><img src="https:&#x2F;&#x2F;github.com&#x2F;Alexander-Garcia.png" width="60px" alt="User avatar: Alexander Garcia" /></a><a href="https://github.com/LumenYoung"><img src="https:&#x2F;&#x2F;github.com&#x2F;LumenYoung.png" width="60px" alt="User avatar: Lumen Yang" /></a><a href="https://github.com/alzwded"><img src="https:&#x2F;&#x2F;github.com&#x2F;alzwded.png" width="60px" alt="User avatar: Vlad Meșco" /></a><a href="https://github.com/JPFrancoia"><img src="https:&#x2F;&#x2F;github.com&#x2F;JPFrancoia.png" width="60px" alt="User avatar: JPFrancoia" /></a><a href="https://github.com/pixlmint"><img src="https:&#x2F;&#x2F;github.com&#x2F;pixlmint.png" width="60px" alt="User avatar: Christian Gröber" /></a><a href="https://github.com/itskyedo"><img src="https:&#x2F;&#x2F;github.com&#x2F;itskyedo.png" width="60px" alt="User avatar: Kyedo" /></a><a href="https://github.com/jsit"><img src="https:&#x2F;&#x2F;github.com&#x2F;jsit.png" width="60px" alt="User avatar: Jay Sitter" /></a><a href="https://github.com/harrisoncramer"><img src="https:&#x2F;&#x2F;github.com&#x2F;harrisoncramer.png" width="60px" alt="User avatar: Harrison (Harry) Cramer" /></a><!-- sponsors -->
</p>

<p align="center">If <i>you</i> love CodeCompanion and use it in your workflow, please consider <a href="https://github.com/sponsors/olimorris">sponsoring me</a></p>

<!-- panvimdoc-ignore-end -->

## :sparkles: Features

- :speech_balloon: [Copilot Chat](https://github.com/features/copilot) meets [Zed AI](https://zed.dev/blog/zed-ai), in Neovim
- :zap: Integrates Neovim with LLMs and Agents in the CLI
- :electric_plug: Support for LLMs from Anthropic, Copilot, GitHub Models, DeepSeek, Gemini, Mistral AI, Novita, Ollama, OpenAI, Azure OpenAI, HuggingFace and xAI (or [bring your own](https://codecompanion.olimorris.dev/extending/adapters.html))
- :robot: Support for [Agent Client Protocol](https://agentclientprotocol.com/overview/introduction), enabling coding with agents like [Augment Code](https://docs.augmentcode.com/cli/overview), [Cagent](https://github.com/docker/cagent) from Docker, [Claude Code](https://docs.anthropic.com/en/docs/claude-code/overview), [Codex](https://openai.com/codex), [Copilot CLI](https://github.com/features/copilot/cli), [Gemini CLI](https://github.com/google-gemini/gemini-cli), [Goose](https://block.github.io/goose/), [Cursor CLI](https://cursor.com/docs/cli/overview), [Kimi CLI](https://github.com/MoonshotAI/kimi-cli), [Kiro](https://kiro.dev/docs/cli/), [Mistral Vibe](https://github.com/mistralai/mistral-vibe) and [OpenCode](https://opencode.ai)
- :heart_hands: User contributed and supported [adapters](https://codecompanion.olimorris.dev/configuration/adapters-http#community-adapters)
- :battery: Support for [Model Context Protocol (MCP)](https://codecompanion.olimorris.dev/model-context-protocol#model-context-protocol-mcp-support)
- :rocket: [Inline transformations](https://codecompanion.olimorris.dev/usage/inline.html), code creation and refactoring
- :art: [Editor Context](https://codecompanion.olimorris.dev/usage/chat-buffer/editor-context.html), [Slash Commands](https://codecompanion.olimorris.dev/usage/chat-buffer/slash-commands.html), [Agents/Tools](https://codecompanion.olimorris.dev/usage/chat-buffer/agents-tools) and [Workflows](https://codecompanion.olimorris.dev/usage/workflows.html) to improve LLM output
- :brain: Support for [rules](https://codecompanion.olimorris.dev/usage/chat-buffer/rules.html) files like `CLAUDE.md`, `.cursor/rules` and your own custom ones
- :sparkles: Built-in [prompt library](https://codecompanion.olimorris.dev/usage/action-palette.html) for common tasks like advice on LSP errors and code explanations
- :building_construction: Create your own [custom prompts](https://codecompanion.olimorris.dev/configuration/prompt-library.html#creating-prompts), Editor Context and Slash Commands
- :books: Have [multiple chats](https://codecompanion.olimorris.dev/usage/introduction.html#quickly-accessing-a-chat-buffer) open at the same time
- :art: Support for [vision and images](https://codecompanion.olimorris.dev/usage/chat-buffer/#images-vision) as input
- :muscle: Async execution for fast performance

<!-- panvimdoc-ignore-start -->

## :camera_flash: In Action

<div align="center">
  <p>
    <h3><a href="https://github.com/user-attachments/assets/aa109f1d-0ec9-4f08-bd9a-df99da03b9a4">The Chat Buffer</a></h3>
    <video controls muted src="https://github.com/user-attachments/assets/3cc83544-2690-49b5-8be6-51e671db52ef"></video>
  </p>
  <p>
    <h3><a href="https://github.com/user-attachments/assets/362b7cfd-e794-4d9c-9a74-90d5e2a87a32">Tools + Agentic Workflows</a></h3>
    <video controls muted src="https://github.com/user-attachments/assets/59efa262-e768-4f36-9901-9d02b018fcf0"></video>
  </p>
  <p>
    <h3><a href="https://github.com/user-attachments/assets/dcddcb85-cba0-4017-9723-6e6b7f080fee">Inline Interaction</a></h3>
    <video controls muted src="https://github.com/user-attachments/assets/11a42705-d9de-4eb5-a9ab-c8a2772fb4d4"></video>
  </p>
</div>

<!-- panvimdoc-ignore-end -->

## :rocket: Getting Started

Everything you need to know about CodeCompanion (installation, configuration and usage) is within the [docs](https://codecompanion.olimorris.dev).

## :toolbox: Troubleshooting

Before raising an [issue](https://github.com/olimorris/codecompanion.nvim/issues), there are a number of steps you can take to troubleshoot a problem:

**Checkhealth**

Run `:checkhealth codecompanion` and check all dependencies are installed correctly. Also take note of the log file path.

**Turn on logging**

Update your config and turn debug logging on:

```lua
-- lazy.nvim
{
  "olimorris/codecompanion.nvim",
  dependencies = {
    "nvim-lua/plenary.nvim",
    "nvim-treesitter/nvim-treesitter",
  },
  opts = {
    -- NOTE: The log_level is in `opts.opts`
    opts = {
      log_level = "DEBUG", -- or "TRACE"
    },
  },
},

-- Other package managers
require("codecompanion").setup({
