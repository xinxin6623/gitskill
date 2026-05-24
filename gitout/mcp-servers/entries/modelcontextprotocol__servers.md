---
type: repo
repo: modelcontextprotocol/servers
domain: mcp-servers
status: active
discovered: 2026-05-25
last_reviewed: 2026-05-25
intent_matched: "想找现成 MCP server 直接装上让 agent 多一堆工具"
signals:
  stars: 86170
  last_commit: 2026-05-21
  language: TypeScript
  license: MIT
url: https://github.com/modelcontextprotocol/servers
absorption:
  harvested: false
  used: false
  used_in: []
---

# modelcontextprotocol/servers · 小白说明书

## 🧐 这是什么
Anthropic 官方维护的 MCP **参考 server 合集** + 通往全套官方 SDK + Registry 的总入口。仓库里直接打包了 7 个常用 server（Filesystem、Git、Fetch、Memory、Sequential Thinking、Time、Everything），全是给你照着抄的样板。

## 💡 解决什么问题
- 你刚接触 MCP，不知道怎么写第一个 server——它的 `src/filesystem`、`src/git` 就是最干净的参考实现。
- 你想让 Claude Code / Codex 立刻能"读本地文件 / 拉 git log / 抓网页"，不想自己撸——直接把仓库里的 server 配到 mcpServers 即可。
- 你在找官方 SDK（TS / Python / Go / Rust / Java / Swift / Kotlin / Ruby / PHP / C#）入口——这里一站式列齐。

## 🎯 谁该用 / 谁别用
**适合你如果：** 第一次接 MCP / 想要"原汁原味"的参考代码 / 需要 Filesystem 或 Git 这种基础工具。
**别浪费时间如果：** 你想要现成的、能直接用的"生产级" GitHub/GitLab/Slack server——这些已经从仓库**移到 archived**（README 写明）；你需要去 [MCP Registry](https://registry.modelcontextprotocol.io/) 或社区 fork 找替代。

## 🚀 三分钟上手
```bash
# 以 Filesystem server 为例（npx 一键跑）
npx -y @modelcontextprotocol/server-filesystem /Users/you/Documents

# Claude Desktop 配置（claude_desktop_config.json）
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/Users/you/Documents"]
    }
  }
}
```

## 🔑 关键文件 / 关键概念
- `src/filesystem/` — 文件读写 server，控制可访问目录的范例代码
- `src/git/` — Git 仓库读取与搜索 server
- `src/memory/` — 基于知识图谱的持久化记忆 server
- `src/sequentialthinking/` — 让模型分步反思的元 server，很多 agent 套件依赖它
- README 顶部的 SDK 表 — 10 种语言 SDK 入口

## ⚠️ 踩坑提示
- 官方明确写"reference implementations，不是 production-ready"。要上生产**自己做安全审计**。
- 大量原来在这里的 server（GitHub、Slack、PostgreSQL、Puppeteer、Brave 等）**已 archived**，被官方/第三方接管，别照着旧博客文章去 `src/github` 找——已经搬家了。
- Filesystem server 的"可访问目录"通过 CLI 参数传，**配错路径等于把整个家目录交给 agent**。

## 🤔 为什么这次推它给你
你的意图是"找现成 MCP server 扩展 Claude Code / Codex 能力"——这是**唯一不会出错的起点**。命中你的 hard_constraints（MCP 协议、开源 MIT、TypeScript），命中 soft preferences（多 server 聚合、含部署文档）。trade-off：合集本身只有 7 个 reference server，要找数据库/IM/SaaS 集成得跳到 appcypher/awesome-mcp-servers 或 MCP Registry 翻清单——这正是为什么我把这两个一起入选。

---
*由 /gitout 生成 · 2026-05-25 · intent: "MCP server 生态合集 — 给 agent 加工具能力"*
