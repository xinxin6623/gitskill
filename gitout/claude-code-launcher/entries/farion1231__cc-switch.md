---
type: repo
repo: farion1231/cc-switch
domain: claude-code-launcher
status: active
discovered: 2026-06-03
last_reviewed: 2026-06-03
intent_matched: "cc-switch 旗舰——跨平台桌面 GUI 管理 Claude Code / Codex / Gemini 等多 agent 的供应商配置"
signals:
  stars: 90016
  last_commit: 2026-06-03
  language: Rust
  license: unknown
url: https://github.com/farion1231/cc-switch
absorption:
  harvested: false
  used: false
  used_in: []
tags:
  - claude-code-launcher
  - cross-platform
  - desktop-gui
  - tauri
  - cc-switch
---

# CC Switch · 小白说明书

## 🧐 这是什么

**cc-switch 的旗舰版**——一个 Tauri 写的跨平台桌面 GUI，**Windows / macOS / Linux 都有 installer 安装包直接下**。它不装 Claude Code 本身，而是装好之后**统一管理 Claude Code / Claude Desktop / Codex / Gemini CLI / OpenCode / OpenClaw / Hermes Agent 这一堆工具的供应商配置**（API Key、Base URL、模型名等），一键切换。

> ⚠️ **关于 90k stars**：这数字异常高，**疑似刷量**或仓库结构特殊。但项目本身真实活跃（trendshift 收录 + 多语言 README + 完整赞助商体系），生态周边也多（cli fork、web fork、JetBrains 插件版都基于它）。看待 stars 时打个折，看实际功能。

## 💡 解决什么问题

- 你买了好几家 API（智谱 + DMXAPI + 火山……），手动改 `~/.claude/settings.json` 切换烦死
- 你既用 Claude Code 又用 Codex 又用 Gemini CLI，每个工具配置文件分散
- 你想在 Windows 11 上点点鼠标就能搞定，不想碰 PowerShell

## 🎯 谁该用 / 谁别用

**适合你如果：**
- Windows 11 用户，想要图形化 + 双击安装
- 同时用 2+ 个 AI Coding agent（Claude Code / Codex / Gemini CLI）
- 同时维护 2+ 个供应商账户

**别浪费时间如果：**
- 你还没装 Claude Code（这玩意是"装好之后切供应商"，不是"装 Claude Code"——需要装的话先看 lxistired 或 RRrrrrick 的 Windows installer）
- 你只有一个供应商，从来不切（直接编辑 `settings.json` 更轻量）
- 你不喜欢满屏赞助商 banner（README 顶部有十几个 API 中转服务的合作链接）

## 📜 协议风险

- **License：** ⚠️ **GitHub API license 字段 null**，README 头部也未显式声明
- **商用 / 魔改 / 闭源：** ⚠️ **协议状态不明**，建议商用前查仓库 LICENSE 文件或开 issue 询问作者
- **对外提供 SaaS / 给客户部署：** ⚠️ 个人使用风险低，企业批量分发请先确认协议

> 它的 CLI fork `SaladDay/cc-switch-cli` 显式声明 MIT，但本仓库未明确。生态周边偏商业化（赞助商体系），不要假设它一定是宽松协议。

## 🚀 三分钟上手

```
1. 访问 https://github.com/farion1231/cc-switch/releases
2. 下载 Windows 安装包（.msi 或 .exe）
3. 双击安装 → 启动
4. 在 GUI 里添加各家供应商的 Base URL + API Key
5. 一键切换
```

也可以走官网 https://ccswitch.io 找最新安装包。

## 🔑 关键文件 / 关键概念

- **`%APPDATA%\cc-switch\`** — Windows 上 cc-switch 自己的配置目录
- **它会改写 `%USERPROFILE%\.claude\settings.json` 等各 agent 的实际配置**——切换时直接改环境变量/配置文件
- Tauri 2 框架（Rust 后端 + Web 前端），所以是真正的原生应用，比 Electron 轻量

## ⚠️ 踩坑提示

- **必须先有 Claude Code（或 Codex / Gemini CLI 等任一目标 agent）**，cc-switch 是管理工具，不是安装器
- README 头部有大量赞助商 / API 中转商推广，**不影响功能**但要意识到作者商业模式
- 90k stars 反常，**别完全用 stars 判断质量**，请去 issues / discussions / commit 历史看真实活跃度
- license 不明，**不建议作为公司内部产品依赖**，自用没关系
- WebDAV 同步功能可以跨设备同步配置，但你的 API Key 走 WebDAV 传输，**确认对方服务器可信**

## 🤔 为什么这次推它给你

1. **命中 intent.what：** "cc Switch" 在你输入里出现，这就是它本人。Windows 安装包直接下，**桌面 GUI 鼠标点点就能切供应商**——懒人包语义命中
2. **命中 soft pref：** 全平台（Windows/macOS/Linux）+ 多 agent 支持 + GUI 图形界面
3. **没命中的 trade-off：** ① 不是安装器，**它不帮你装 Claude Code 本身**——你还得搭配 lxistired 或 RRrrrrick 的 installer ② 协议未声明 ③ 商业气息浓

---
*由 /gitout 生成 · 2026-06-03 · intent: "搜索 部署 claude code cc Switch以及依赖环境的，适合 Windows 11 直接部署的懒人包"*
