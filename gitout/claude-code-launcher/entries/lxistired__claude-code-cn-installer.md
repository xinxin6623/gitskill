---
type: repo
repo: lxistired/claude-code-cn-installer
domain: claude-code-launcher
status: active
discovered: 2026-06-03
last_reviewed: 2026-06-03
intent_matched: "Windows 11 一键装 Claude Code + 依赖 + 国产 API 的中国版懒人包"
signals:
  stars: 20
  last_commit: 2026-05-12
  language: PowerShell
  license: unknown
url: https://github.com/lxistired/claude-code-cn-installer
absorption:
  harvested: false
  used: false
  used_in: []
tags:
  - claude-code-launcher
  - windows
  - installer
  - chinese
  - glm
---

# Claude Code 一键安装 (Windows 中国版) · 小白说明书

## 🧐 这是什么

国人写的 Windows 一键安装包，**自动给你装好 Node.js + Git + Claude Code，再帮你把国产大模型 API（默认智谱 GLM）配上**。配套一个 `.iss` 文件可以打包成 `.exe` 安装程序，发给家里小白都能装。

## 💡 解决什么问题

- 你想用 Claude Code，但不懂 Node、不会装 Git、看到环境变量就头疼
- Anthropic 官方账号申请不下来 / 信用卡进不去，需要走国产模型替代
- 想把"装好的环境"给朋友/同事，做成 `.exe` 双击就能装的那种

## 🎯 谁该用 / 谁别用

**适合你如果：**
- Windows 11 用户，编程基础接近 0
- 想用智谱 GLM-5 / GLM-4.7 平替 Claude，月费几十块
- 是公司 IT，要批量给同事装 Claude Code 内部工具链

**别浪费时间如果：**
- 你已经在用 Anthropic 官方账号 + 习惯命令行（直接 `npm install -g @anthropic-ai/claude-code` 即可）
- 你不想被默认绑定智谱（虽然脚本提供菜单 [4] 配自定义 Anthropic 兼容 API，但默认体验是 GLM 优先）
- Mac / Linux 用户（脚本只针对 Windows）

## 📜 协议风险

- **License：** ⚠️ **仓库未声明 LICENSE 文件**（GitHub API license 字段为 null）
- **商用 / 魔改 / 闭源：** ⚠️ **协议未明确**，建议商用前自行咨询作者或 fork 时只留个人参考
- **对外提供 SaaS / 给客户部署：** ⚠️ 个人玩没问题，企业内分发请先确认协议

> 因为是 Windows 用户友好的一键脚本，自用风险低；但若公司打算把这个 .exe 内嵌到员工电脑里批量部署，**请先开 issue 让作者补 LICENSE**。

## 🚀 三分钟上手

```powershell
# 1. 下载仓库 zip 并解压
# 2. 右键「一键安装.bat」→ 以管理员身份运行
# 3. 跟着菜单走：选模型 → 输 API Key → 完成

# 验证装好了
claude --version
claude  # 进交互模式
```

打包成 `.exe` 给小白：

```
# 装 Inno Setup → 打开 ClaudeCodeInstaller.iss → Build → Compile
# 输出 ClaudeCode-Setup-v1.0.0.exe
```

## 🔑 关键文件 / 关键概念

- `一键安装.bat` — 用户双击入口
- `install.ps1` — 真正干活的 PowerShell 主脚本（装 Node + Git + Claude Code）
- `configure-api.ps1` — 配置/换模型/换 API Key 的菜单工具
- `ClaudeCodeInstaller.iss` — Inno Setup 工程文件，打包成 `.exe` 用
- `%USERPROFILE%\.claude\settings.json` — Claude Code 配置最终落地的位置

## ⚠️ 踩坑提示

- **Claude Code v2.0 bug**：必须 `ANTHROPIC_AUTH_TOKEN`（不是 `ANTHROPIC_API_KEY`），且 `~/.claude.json` 里设 `hasCompletedOnboarding: true`，脚本默认已经处理，但手动改配置时记得
- **API 必须是 Anthropic 兼容端点**（如智谱 `/api/anthropic`），**不能用纯 OpenAI 格式**的 `/v1/chat/completions`，需要额外转换层
- 默认走 `npmmirror.com` 国内镜像，公司内网代理时可能撞证书
- 脚本要求管理员权限，跑之前先关 Windows Defender 实时保护或加白名单（PowerShell 脚本常被误杀）
- 仓库 stars 才 20，不是审核充分的项目，**生产环境别裸用**

## 🤔 为什么这次推它给你

1. **命中 intent.what：** 这是名单里唯一同时 cover "Windows 11 + 自动装 Node/Git/Claude Code + 中文菜单 + 国产 API 默认 + 可打包成 .exe 发给小白" 五个点的项目，最贴近"懒人包"语义
2. **命中 soft pref：** 中文友好、国产模型驱动（你的"cc Switch 以及依赖环境"诉求的"依赖环境"部分这家全管了）
3. **没命中的 trade-off：** stars 只有 20、license 未声明、有"国产 API 中转推广"色彩；如果你追求高 star/官方背书项目，看 farion1231/cc-switch 旗舰版

---
*由 /gitout 生成 · 2026-06-03 · intent: "搜索 部署 claude code cc Switch以及依赖环境的，适合 Windows 11 直接部署的懒人包"*
