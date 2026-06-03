# claude-code-launcher · Claude Code 启动器 / 多账号切换器 / 一键安装包

> 用户痛点：Claude Code 装起来要 Node + Git + 申请账号 + 配 API + 多 provider 切换；Windows 11 用户更痛苦。
> 本 domain 收纳：**装 Claude Code 的 installer** + **管 Claude Code 配置的 GUI/CLI** 两类工具。

## 健康度速览（2026-06-03）

| 维度 | 状态 |
|---|---|
| entries | 5 |
| 容量上限 | 30 |
| 最新入库 | 2026-06-03 |
| 主要协议 | MIT (3) / 未声明 (2) |
| Windows 11 友好 | 5/5 |

## 速览表

| repo | stars | 角色 | Windows 一键装 Claude Code | 切供应商 | 协议 |
|---|---:|---|:---:|:---:|---|
| [lxistired/claude-code-cn-installer](entries/lxistired__claude-code-cn-installer.md) | 20 | Windows 中国版安装包 | ✅ + 默认 GLM | ⚠️ 简易 | 未声明 |
| [RRrrrrick/ClaudeCode-Windows-Installer](entries/RRrrrrick__ClaudeCode-Windows-Installer.md) | 3 | Windows 通用安装包 | ✅ + 自定义 API | ⚠️ 简易 | **MIT** |
| [farion1231/cc-switch](entries/farion1231__cc-switch.md) | 90k★ | 跨平台桌面 GUI 管理器（旗舰） | ❌ 只管不装 | ✅ 强 | 未声明 |
| [FullStackPlayer/claude-code-launcher (ccl)](entries/FullStackPlayer__claude-code-launcher.md) | 36 | 国产模型专用 TUI launcher | ❌ 自动尝试装 | ✅ 限 4 家 | 未声明 |
| [op7418/ai-claude-start](entries/op7418__ai-claude-start.md) | 224 | 跨平台 npm launcher + 安全存 token | ❌ 只管不装 | ✅ 中等 | **MIT** |

## 路径推荐

- **「我要 Windows 11 装好就能用」** → `lxistired`（默认 GLM）或 `RRrrrrick`（自填 API）
- **「我已经装好了，要切多家供应商」** → `farion1231/cc-switch`（GUI）或 `op7418/ai-claude-start`（CLI）
- **「我只想用国产模型，简单切」** → `FullStackPlayer/ccl`

## 相关周边

- **cc-switch 生态分支**：
  - `SaladDay/cc-switch-cli` (3216★, MIT) — CLI fork，跟旗舰版 WebDAV 同步兼容
  - `Laliet/cc-switch-web` (366★) — Web/Docker fork，云/无头部署
  - `zhukunpenglinyutong/jetbrains-cc-gui` (3850★, MIT) — JetBrains IDEA 插件版，IDE 内集成
- **不适配 Windows**：
  - `orange2ai/claude-code-now` (628★) — **macOS 专属**（Dock/Finder Toolbar 启动），README 下载链接是 `.macOS.zip`，**Windows 用户跳过**

## discarded_queries

无（5 路 query 全部有返回）

---

> 反思 2026-06-03：最低效环节 = 首轮把 chenhg5/cc-connect (11k★) 和 lonr-6/cc-desktop-switch 当成 cc-switch 同类（其实一个是 messaging bridge、一个是 Claude Desktop 不是 Claude Code），下次扫"cc"前缀名要先用 description 关键词区分 `Claude Code` vs `Claude Desktop`。
