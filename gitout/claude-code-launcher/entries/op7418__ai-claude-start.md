---
type: repo
repo: op7418/ai-claude-start
domain: claude-code-launcher
status: active
discovered: 2026-06-03
last_reviewed: 2026-06-03
intent_matched: "跨平台 npm launcher，OS keychain 安全存 token，多 profile 切换"
signals:
  stars: 224
  last_commit: 2025-12-29
  language: TypeScript
  license: MIT
url: https://github.com/op7418/ai-claude-start
absorption:
  harvested: false
  used: false
  used_in: []
tags:
  - claude-code-launcher
  - cross-platform
  - npm
  - keychain
  - mit
---

# ai-claude-start · 小白说明书

## 🧐 这是什么

跨平台 npm launcher，**比 ccl 更注重安全**——用系统 keychain（macOS Keychain / Windows Credential Manager / Linux libsecret）存 API token，没法走 keychain 就 fallback 到本地文件。命令是 `claude-start`，自带 3 个 preset（Anthropic / Moonshot / IMDS），也能自定义。**MIT 协议**。

## 💡 解决什么问题

- 你担心 API token 明文存在 `~/.claude/settings.json` 里被翻到
- 你想要"一行命令切 profile"的简洁体验，不要 GUI 也不要 TUI 选择菜单
- 你想把 launcher 集成进自己的 shell 脚本 / CI

## 🎯 谁该用 / 谁别用

**适合你如果：**
- 你装了 Node.js，习惯 `npm install -g` 跨平台拿工具
- 关心 token 不要明文落盘
- 想要"shorthand 切换"：`claude-start -moonshot` 一行搞定

**别浪费时间如果：**
- 你电脑上还没装 Node.js（请用 Windows installer 系列先装好基础环境）
- 你要图形界面（用 cc-switch）
- 你只用一个 provider（没必要折腾）

## 📜 协议风险

- **License：** **MIT**（README badge 显式）
- **商用 / 魔改 / 闭源：** ✅ **无风险**——可自由商用、改、闭源分发
- **对外提供 SaaS / 给客户部署：** ✅ **无传染义务**

## 🚀 三分钟上手

```bash
# 全局装
npm install -g ai-claude-start

# 首次配置（向导）
ai-claude-start setup

# 启动（多 profile 时弹选择菜单）
claude-start

# 直接用某 profile
claude-start moonshot

# shorthand 语法
claude-start -bigmodel --version
```

## 🔑 关键文件 / 关键概念

- npm 包名：`ai-claude-start`
- 启动命令：`claude-start`（与 `claude` 区分）
- keytar 模块负责 OS 级 secure storage，没法用时 fallback 到本地文件
- `ANTHROPIC_AUTH_TOKEN` 统一注入（避免 `ANTHROPIC_*` 冲突）
- 内置 preset：Anthropic / Moonshot（月之暗面）/ IMDS / BigModel（智谱）

## ⚠️ 踩坑提示

- **要先装 Node 18+ 和 Claude Code 本体**
- Windows 上 keytar 可能要装 build tool（Visual C++ Redist），失败会 fallback 到文件
- `CLAUDE_CMD` 环境变量可以替换实际启动的命令，**测试时很有用**
- 不带桌面 GUI，**懒人包语义打折**

## 🤔 为什么这次推它给你

1. **命中 intent.what：** 多 profile 切换的诉求 cover 度高，**安全维度（keychain）是 cc-switch 全家桶和 lxistired/RRrrrrick 都没明确强调的**
2. **命中 soft pref：** MIT + 跨平台 + npm 全局 + 国产模型 preset 内置（Moonshot / 智谱）
3. **没命中的 trade-off：** ① 不装依赖（要你自己装 Node + Claude Code），不是"Windows 双击就装完"的懒人包 ② 命令行操作 ③ stars 224 中等

---
*由 /gitout 生成 · 2026-06-03 · intent: "搜索 部署 claude code cc Switch以及依赖环境的，适合 Windows 11 直接部署的懒人包"*
