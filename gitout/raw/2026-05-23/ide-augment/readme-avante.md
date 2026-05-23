<div align="center">
  <img alt="logo" width="120" src="https://github.com/user-attachments/assets/2e2f2a58-2b28-4d11-afd1-87b65612b2de" />
  <h1>avante.nvim</h1>
</div>

<p align="center">
  <a href="https://neovim.io/" target="_blank"><img src="https://img.shields.io/static/v1?style=flat-square&label=Neovim&message=v0.10%2b&logo=neovim&labelColor=282828&logoColor=8faa80&color=414b32" alt="Neovim: v0.10+" /></a>
  <a href="https://github.com/yetone/avante.nvim/actions/workflows/lua.yaml" target="_blank"><img src="https://img.shields.io/github/actions/workflow/status/yetone/avante.nvim/lua.yaml?style=flat-square&logo=lua&logoColor=c7c7c7&label=Lua+CI&labelColor=1E40AF&color=347D39&event=push" alt="Lua CI status" /></a>
  <a href="https://github.com/yetone/avante.nvim/actions/workflows/rust.yaml" target="_blank"><img src="https://img.shields.io/github/actions/workflow/status/yetone/avante.nvim/rust.yaml?style=flat-square&logo=rust&logoColor=ffffff&label=Rust+CI&labelColor=BC826A&color=347D39&event=push" alt="Rust CI status" /></a>
  <a href="https://github.com/yetone/avante.nvim/actions/workflows/pre-commit.yaml" target="_blank"><img src="https://img.shields.io/github/actions/workflow/status/yetone/avante.nvim/pre-commit.yaml?style=flat-square&logo=pre-commit&logoColor=ffffff&label=pre-commit&labelColor=FAAF3F&color=347D39&event=push" alt="pre-commit status" /></a>
  <a href="https://discord.gg/QfnEFEdSjz" target="_blank"><img src="https://img.shields.io/discord/1302530866362323016?style=flat-square&logo=discord&label=Discord&logoColor=ffffff&labelColor=7376CF&color=268165" alt="Discord" /></a>
  <a href="https://dotfyle.com/plugins/yetone/avante.nvim"><img src="https://dotfyle.com/plugins/yetone/avante.nvim/shield?style=flat-square" /></a>
</p>

**avante.nvim** is a Neovim plugin designed to emulate the behaviour of the [Cursor](https://www.cursor.com) AI IDE. It provides users with AI-driven code suggestions and the ability to apply these recommendations directly to their source files with minimal effort.

[查看中文版](README_zh.md)

> [!NOTE]
>
> 🥰 This project is undergoing rapid iterations, and many exciting features will be added successively. Stay tuned!

<https://github.com/user-attachments/assets/510e6270-b6cf-459d-9a2f-15b397d1fe53>

<https://github.com/user-attachments/assets/86140bfd-08b4-483d-a887-1b701d9e37dd>

## Sponsorship ❤️

If you like this project, please consider supporting me on Patreon, as it helps me to continue maintaining and improving it:

[Sponsor me](https://patreon.com/yetone)

## Features

- **AI-Powered Code Assistance**: Interact with AI to ask questions about your current code file and receive intelligent suggestions for improvement or modification.
- **One-Click Application**: Quickly apply the AI's suggested changes to your source code with a single command, streamlining the editing process and saving time.
- **Project-Specific Instruction Files**: Customize AI behavior by adding a markdown file (`avante.md` by default) in the project root. This file is automatically referenced during workspace changes. You can also configure a custom file name for tailored project instructions.

## Avante Zen Mode

Due to the prevalence of claude code, it is clear that this is an era of Coding Agent CLIs. As a result, there are many arguments like: in the Vibe Coding era, editors are no longer needed; you only need to use the CLI in the terminal. But have people realized that for more than half a century, Terminal-based Editors have solved and standardized the biggest problem with Terminal-based applications — that is, the awkward TUI interactions! No matter how much these Coding Agent CLIs optimize their UI/UX, their UI/UX will always be a subset of Terminal-based Editors (Vim, Emacs)! They cannot achieve Vim’s elegant action + text objects abstraction (imagine how you usually edit large multi-line prompts in an Agent CLI), nor can they leverage thousands of mature Vim/Neovim plugins to help optimize TUI UI/UX—such as easymotions and so on. Moreover, when they want to view or modify code, they often have to jump into other applications which forcibly interrupts the UI/UX experience.

Therefore, Avante’s Zen Mode was born! It looks like a Vibe Coding Agent CLI but it is completely Neovim underneath. So you can use your muscle-memory Vim operations and those rich and mature Neovim plugins on it. At the same time, by leveraging [ACP](https://github.com/yetone/avante.nvim#acp-support) it has all capabilities of claude code / gemini-cli / codex! Why not enjoy both?

Now all you need to do is alias this command to avante; then every time you simply type avante just like using claude code and enter Avante’s Zen Mode!

```bash
alias avante='nvim -c "lua vim.defer_fn(function()require(\"avante.api\").zen_mode()end, 100)"'
```

The effect is as follows:

<img alt="Avante Zen Mode" src="https://github.com/user-attachments/assets/60880f65-af55-4e4c-a565-23bb63e19251" />

## Project instructions with avante.md

<details>

<summary>
The `avante.md` file allows you to provide project-specific context and instructions to the ai. this file should be placed in your project root and will be automatically referenced during all interactions with avante.
</summary>

### Best practices for avante.md

to get the most out of your project instruction file, consider following this structure:

#### Your role

define the ai's persona and expertise level for your project:

```markdown
### your role

you are an expert senior software engineer specializing in [technology stack]. you have deep knowledge of [specific frameworks/tools] and understand best practices for [domain/industry]. you write clean, maintainable, and well-documented code. you prioritize code quality, performance, and security in all your recommendations.
```

#### Your mission

clearly describe what the ai should focus on and how it should help:

```markdown
### your mission

your primary goal is to help build and maintain [project description]. you should:

- provide code suggestions that follow our established patterns and conventions
- help debug issues by analyzing code and suggesting solutions
- assist with refactoring to improve code quality and maintainability
- suggest optimizations for performance and scalability
- ensure all code follows our security guidelines
- help write comprehensive tests for new features
```

#### Additional sections to consider

- **project context**: brief description of the project, its goals, and target users
- **technology stack**: list of technologies, frameworks, and tools used
- **coding standards**: specific conventions, style guides, and patterns to follow
- **architecture guidelines**: how components should interact and be organized
- **testing requirements**: testing strategies and coverage expectations
