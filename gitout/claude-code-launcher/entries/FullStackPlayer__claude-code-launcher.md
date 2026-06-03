---
type: repo
repo: FullStackPlayer/claude-code-launcher
domain: claude-code-launcher
status: active
discovered: 2026-06-03
last_reviewed: 2026-06-03
intent_matched: "ccl——专为国产编程模型（GLM/MiniMax/DeepSeek/Kimi）驱动 Claude Code 的轻量启动器"
signals:
  stars: 36
  last_commit: 2025-12-16
  language: TypeScript
  license: unknown
url: https://github.com/FullStackPlayer/claude-code-launcher
absorption:
  harvested: false
  used: false
  used_in: []
tags:
  - claude-code-launcher
  - chinese
  - domestic-llm
  - tui
---

# Claude Code Launcher (ccl) · 小白说明书

## 🧐 这是什么

一个**专门给国产编程模型（智谱 GLM-4.6 / MiniMax-M2 / DeepSeek-3.2 / Kimi-K2）做 Claude Code 启动器**的 TS 项目，单文件可执行，命令行交互界面（TUI）选模型。作者明说这是替代手动设环境变量这种"梗阻体验"用的，目前 4 家国产模型都直接提供 Anthropic 兼容 API，ccl 已全部支持。

## 💡 解决什么问题

- 你已经买了 GLM 编程套餐 + Kimi 编程套餐，想随时切，**不想每次手动改环境变量**
- 你需要同时开两个 Claude Code 进程跑不同模型解决不同问题
- 你想试国产模型替代 Claude，但又不想被 cc-switch 那种全家桶绑架

## 🎯 谁该用 / 谁别用

**适合你如果：**
- 已经买了至少 1-2 家国产 AI 编程套餐（GLM / MiniMax / DeepSeek / Kimi）
- 喜欢命令行 TUI 多于桌面 GUI
- 想要"装 Claude Code → 装 ccl → 完事"的极简栈

**别浪费时间如果：**
- 你用的是 Anthropic 官方 API 或非这 4 家国产模型（ccl 只预设了这几家）
- 你想要 GUI 图形界面（用 cc-switch 旗舰版）
- 你完全不懂命令行（用 lxistired 的安装包）

## 📜 协议风险

- **License：** ⚠️ **README 未声明，仓库 LICENSE 文件需自查**
- **商用 / 魔改 / 闭源：** ⚠️ **协议未明确**——个人玩没问题，公司用需先查
- **对外提供 SaaS / 给客户部署：** ⚠️ 协议未声明前不建议

## 🚀 三分钟上手

```bash
# 前置：装 Node + Claude Code 本体
npm install -g @anthropic-ai/claude-code

# 装 ccl
npm install -g ccl-cli-installer

# 第一次跑会生成 ccl.config.json，把里面 auth_token 改成你的 API Key
ccl

# 直接用某家模型
ccl --provider=DeepSeek-3.2

# 一次性提问
ccl -p GLM-4.6 --prompt "解释这段代码"
```

## 🔑 关键文件 / 关键概念

- `ccl.config.json` — 配置文件，4 家 provider 的 auth_token 改成你的 Key 即可
- `additionalOTQP` — 一次性请求附加提示词（如"请用中文回复"）
- 支持 bun 跑 TS 模式（跨平台），或下载预编译单文件二进制

## ⚠️ 踩坑提示

- **不装 Claude Code 本体它会自动尝试装**，但建议先手动装好
- 默认 4 家 provider 预设，**其它供应商需要自己加 config**（项目支持 Anthropic 兼容接口扩展）
- 作者明说大部分代码是阿里 Qoder 生成的——逻辑跑通了，但**代码质量请自行评估**
- stars 36，**小项目快速迭代中**，跟最新版前看 CHANGELOG

## 🤔 为什么这次推它给你

1. **命中 intent.what：** "cc Switch" 替代品中**唯一明确聚焦国产模型 + 中文**的 launcher，比 cc-switch 全家桶轻量很多
2. **命中 soft pref：** 中文 + 国产模型 + 命令行单文件可执行 + 跨平台
3. **没命中的 trade-off：** ① 不是 Windows 一键安装器（不装 Node 不装 Claude Code）② 协议未声明 ③ 没图形界面，纯 TUI

---
*由 /gitout 生成 · 2026-06-03 · intent: "搜索 部署 claude code cc Switch以及依赖环境的，适合 Windows 11 直接部署的懒人包"*
