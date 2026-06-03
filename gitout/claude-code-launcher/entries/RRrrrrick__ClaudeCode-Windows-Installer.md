---
type: repo
repo: RRrrrrick/ClaudeCode-Windows-Installer
domain: claude-code-launcher
status: active
discovered: 2026-06-03
last_reviewed: 2026-06-03
intent_matched: "Windows 11 一键装 Claude Code + 国内镜像加速 + 自定义 API（不绑定特定模型）"
signals:
  stars: 3
  last_commit: 2025-12-29
  language: PowerShell
  license: MIT
url: https://github.com/RRrrrrick/ClaudeCode-Windows-Installer
absorption:
  harvested: false
  used: false
  used_in: []
tags:
  - claude-code-launcher
  - windows
  - installer
  - mit
---

# ClaudeCode Windows 一键安装工具 · 小白说明书

## 🧐 这是什么

也是 Windows 一键脚本，**和 lxistired 那版功能类似但更通用**——不强绑定智谱，让你自己填 `ANTHROPIC_BASE_URL` 和 token，**MIT 协议**写得明明白白，是这次 5 个候选里"协议最干净的 Windows 安装器"。

## 💡 解决什么问题

- 你已经买好了某个第三方 API 中转服务（PackyCode / DMXAPI / 火山等），需要装 Claude Code 但不想手动配
- 你看不上默认捆绑某家国产模型的安装包，要纯净 installer 自己填 URL
- 你需要在多台 Windows 11 上重复部署，希望脚本是 MIT 协议可以 fork 改

## 🎯 谁该用 / 谁别用

**适合你如果：**
- Windows 10 / 11 用户
- 已经有自己的 API 渠道（任何 Anthropic 兼容端点）
- 想要协议清晰、可放心改的 installer 脚本

**别浪费时间如果：**
- 你要"装完就能跑、连账号都不用申请"的最懒包（用 lxistired 版默认引导 GLM 那套）
- 你已经在用 cc-switch（这玩意是装 Claude Code，cc-switch 是装好 Claude Code 之后切供应商）

## 📜 协议风险

- **License：** **MIT**（README badge 显式标注）
- **商用 / 魔改 / 闭源：** ✅ **无风险**——MIT 允许任意改、闭源、商用
- **对外提供 SaaS / 给客户部署：** ✅ **无传染义务**

## 🚀 三分钟上手

```powershell
# 1. 下载本仓库 zip 解压
# 2. 双击「一键安装ClaudeCode.bat」
# 3. 选「配置自定义 API」→ 填 BASE_URL + API_KEY

# 或者手动跑 ps1（带英文界面）
powershell -ExecutionPolicy Bypass -File install-claude-code-en.ps1

# 改配置
# 双击「修改配置.bat」 或编辑 %USERPROFILE%\.claude\settings.json
```

## 🔑 关键文件 / 关键概念

- `一键安装ClaudeCode.bat` — 用户入口（中文界面）
- `install-claude-code-en.ps1` — 英文界面版本
- `config-editor.ps1` — 配置编辑器
- `%USERPROFILE%\.claude\settings.json` — Claude Code 最终读的配置
- `%USERPROFILE%\.claude.json` — `hasCompletedOnboarding: true` 必须有，否则 v2.0 跑不起来

## ⚠️ 踩坑提示

- **`ANTHROPIC_API_KEY` 要清空**（设为 `""`），只用 `ANTHROPIC_AUTH_TOKEN`——Claude Code v2.0 这个坑作者已经在 README 说过
- 国内镜像默认 `npmmirror.com`，公司内网可能要先配代理
- README 里推广了一个 FoxCode 联盟链接，**不影响功能**，但意识下作者的盈利模式
- stars 只有 3，**自用 OK，商用部署前先 fork 走一遍**

## 🤔 为什么这次推它给你

1. **命中 intent.what：** Windows 11 一键装 + 自动管依赖（Node/Git/Claude Code），**和 lxistired 版功能并列**，差异是协议清晰 + 不预设国产模型
2. **命中 soft pref：** MIT 协议（这是你"懒人包"诉求里隐含的"可放心传播"维度）+ 中文界面
3. **没命中的 trade-off：** stars 只有 3，不是经验证的成熟项目；如果你已经选了 cc-switch 全家桶（farion1231 那个），这个就是冗余

---
*由 /gitout 生成 · 2026-06-03 · intent: "搜索 部署 claude code cc Switch以及依赖环境的，适合 Windows 11 直接部署的懒人包"*
