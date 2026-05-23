---
type: repo
repo: chyinan/Kokoro-Engine
domain: misc
status: active
decision: harvest
discovered: 2026-05-22
last_reviewed: 2026-05-22
intent_matched: "可 DIY AI 对话机器人，Live2D + MOD 高自由度定制"
signals:
  stars: 82
  last_commit: 2026-05-22
  language: Rust
  license: MIT
url: https://github.com/chyinan/Kokoro-Engine
absorption:
  harvested: false
  used: false
  used_in: []
---

# Kokoro Engine · 小白说明书

## 🧐 这是什么

一个**用 Rust + Tauri v2 + React 写的跨平台桌面 AI 角色引擎**。强调"All-in-one + 本地优先 + MOD 可拓展"——意思是 Live2D 渲染、LLM 调用、TTS、STT 全装在一个壳里，数据存本地 SQLite，而且整个 UI 可以靠 MOD（HTML/CSS/JS + QuickJS 沙箱）整套替换。

跨平台是真跨：Windows / macOS / Linux 都构建出包了。

## 💡 解决什么问题

你看上了 AIRI 的功能但有这些顾虑：

- TypeScript monorepo 太重，跑不动
- 想要数据完全本地（隐私 + 可控）
- 想自己写 UI 主题、整套换皮

Kokoro Engine 用 Rust 做核（性能 + 二进制小），Tauri 做壳（比 Electron 轻），MOD 系统让你**像装游戏 mod 一样改 UI**。内置一个原神风格主题做示范。

## 🎯 谁该用 / 谁别用

**适合你如果：**
- 喜欢 Rust + Tauri 技术栈
- 在乎跨平台一致性（macOS 友好）
- 想做高自由度 UI 改造（MOD 系统是它独家优势）

**别浪费时间如果：**
- 排斥 Rust（编译慢、生态相对小众）
- 只想要个简单聊天框
- 不打算自己 build（release 版本可能晚于源码）

## 🚀 三分钟上手

```bash
# 路径 1：下安装包
# https://github.com/chyinan/Kokoro-Engine/releases

# 路径 2：源码构建（需要 Node 18+ 和 Rust stable）
git clone https://github.com/chyinan/kokoro-engine.git
cd kokoro-engine
npm install
npm run tauri dev
```

## 🔑 关键文件 / 关键概念

- **Tauri v2** — Rust 后端 + Web 前端的跨平台框架，比 Electron 轻很多
- **QuickJS MOD 沙箱** — 让用户写脚本扩展但不能搞坏系统
- **SQLite + FTS5 BM25 + RRF 混合检索** — 长期记忆方案，文档里讲得很细
- **MCP Server 支持** — 能挂外部工具

## ⚠️ 踩坑提示

- Rust 工具链首次安装较大（~2GB）
- macOS 上 Tauri 签名问题需要自己处理
- MOD 文档相对新，示例少

## 🤔 为什么这次推它给你

**命中"高自由度定制"和"本地优先"两条 soft preference 最强**。你说"都可以 DIY"——这个项目把"DIY"做到了 MOD 系统级别，UI 可以整套换。trade-off 是 stars 不如 AIRI 多、社区小一些，但**架构图非常清晰**（README 里 mermaid 图直接画出 IPC 链路），适合作为"想自己搭一个 Tauri 桌宠"的最佳学习样本。

---
*由 /gitout 生成 · 2026-05-22 · intent: "可 DIY 的 AI 对话机器人，眼神/口型/表情都可改"*
