---
type: repo
repo: Tyrrrz/DiscordChatExporter
domain: misc
status: active
decision: watch
discovered: 2026-05-22
last_reviewed: 2026-05-22
theme: im-export
intent_matched: "Discord 频道历史完整导出（GUI + CLI + Docker）"
signals:
  stars: 11175
  last_commit: 2026-05-22
  language: C#
  license: MIT
url: https://github.com/Tyrrrz/DiscordChatExporter
absorption:
  harvested: false
  used: false
  used_in: []
---

# DiscordChatExporter · 小白说明书

## 🧐 这是什么

**Discord 频道导出工具的事实标准**。C# / .NET 写的，11.2k 星，提供 GUI + CLI + Docker 三种用法。支持 DM、群聊、服务器频道全部导出，保留 Discord markdown 方言和大部分富媒体。作者明确标"maintenance"状态（不再加新功能但维护更新）。

## 💡 解决什么问题

Discord 现在是开发者 / AI 圈 / 游戏圈最重要的社区平台之一，但：

- 没有官方导出（Bot 才能用 API，普通号不行）
- 项目频道一关闭，所有讨论历史消失
- 想做"社区知识沉淀"或"AI 训练数据"无从下手

这个工具让你**把任何能访问的频道存成 HTML / TXT / JSON / CSV**，附件可选下载。HTML 输出几乎跟 Discord UI 一样好看。

## 🎯 谁该用 / 谁别用

**适合你如果：**
- 你是 Discord 频道 owner / mod，想归档历史
- 想把社区讨论喂给个人知识库
- 想看 C# / .NET 写跨平台 CLI 的范本

**别浪费时间如果：**
- 不用 Discord
- 不能接受"自动化用户账号违反 TOS"的风险（README 警告了）
- 嫌 C# / .NET 麻烦

## 🚀 三分钟上手

```bash
# Docker（推荐，不污染系统）
docker run -it --rm tyrrrz/discordchatexporter:stable \
  exportguild -t <TOKEN> -g <GUILD_ID>

# 或下二进制
# https://github.com/Tyrrrz/DiscordChatExporter/releases
```

需要 Discord token（README 有说明怎么拿；Bot 推荐，用户 token 违反 TOS）。

## 🔑 关键文件 / 关键概念

- **DiscordChatExporter.Cli** — CLI 版本
- **DiscordChatExporter.Gui** — Windows GUI
- **HTML 模板** — 几乎像素级还原 Discord UI
- **`exportguild` / `exportchannel` / `exportdm`** — 三种导出范围

## ⚠️ 踩坑提示

- 用户账号自动化违反 Discord TOS，可能被封号
- 推荐用 Bot token 走自动化（README 强调）
- 大频道导出可能持续数小时
- 项目在 "maintenance" 模式

## 🤔 为什么这次推它给你

**weixinjilu 的另一个维度参考**。同样是"导出 IM 历史"，但 Discord 走的是 Token + API 路线（不是本地数据库逆向）。**对比 LC044/WeChatMsg 走数据库解密、ReagentX/imessage-exporter 走本地 SQLite，DiscordChatExporter 走 API + Token** —— 三种典型路径都在你视野里了。pattern 候选：`api-token-based-history-export`。

---
*由 /gitout 生成 · 2026-05-22 · theme: 聊天记录 / 个人数据遗产化*
