---
type: repo
repo: haris-musa/excel-mcp-server
domain: mcp-servers
status: active
discovered: 2026-05-25
last_reviewed: 2026-05-25
intent_matched: "让 agent 直接读写 Excel，不用装 Office"
signals:
  stars: 3861
  last_commit: 2026-04-12
  language: Python
  license: MIT
url: https://github.com/haris-musa/excel-mcp-server
absorption:
  harvested: false
  used: false
  used_in: []
---

# haris-musa/excel-mcp-server · 小白说明书

## 🧐 这是什么
一个 Python 写的 MCP server，让 agent 直接操作 `.xlsx` 文件——**不需要装 Microsoft Excel**。能创建/读取/修改工作簿、写公式、做图表、建透视表、加条件格式、写 Excel 表格，本质是把 openpyxl 那一套封成 MCP 工具。

## 💡 解决什么问题
- 你想让 agent 帮你处理一堆 Excel 报表，但 Mac 上没装 Office / 服务器无图形界面——这个纯 Python，不依赖 Excel 安装。
- 让模型读财务表、改单元格、加汇总公式、生成图表——常规"代码解释器"也行，但用 MCP 接到 Claude Code / Cursor 工作流里更顺手。
- 想做一个"AI 报表机器人"挂在内网服务器上——它支持 streamable HTTP 模式，可以当远程服务用。

## 🎯 谁该用 / 谁别用
**适合你如果：** 工作里频繁用 Excel；想给 Claude Code 加"会写 xlsx"的能力；要做内部 AI 报表服务。
**别浪费时间如果：** 你只处理 CSV / Parquet（直接用 pandas / DuckDB 更快）；你需要操作 Excel **应用本身**（启动 Excel、跑 VBA、读取已打开的工作簿）——这个不行，它只动文件。

## 🚀 三分钟上手
```bash
# stdio 模式（本地用最简单）
uvx excel-mcp-server stdio

# Claude / Cursor 配置
{
  "mcpServers": {
    "excel": {
      "command": "uvx",
      "args": ["excel-mcp-server", "stdio"]
    }
  }
}

# 远程模式（streamable HTTP）
EXCEL_FILES_PATH=/path/to/files uvx excel-mcp-server streamable-http
```

## 🔑 关键文件 / 关键概念
- `TOOLS.md` — 所有工具的完整 reference，先翻这个
- **三种 transport**：stdio（本地）、SSE（已弃用）、streamable-http（推荐做远程）
- 环境变量 **`EXCEL_FILES_PATH`** — 远程模式下所有文件路径必须相对它（防目录穿越）
- `FASTMCP_PORT` — 远程模式监听端口（默认 8017）

## ⚠️ 踩坑提示
- 远程模式下用绝对路径或 `..` 会被拒——这是安全设计，别绕开。
- SSE transport 已标 deprecated，新部署直接上 streamable-http。
- 它是文件级操作，不能读"用户当前打开的 Excel 进程"，也不会跟 Excel 实例同步。

## 🤔 为什么这次推它给你
你想要"高质量单功能 server"——这是文档处理类里最有代表性的一份：3.8k star、Python、有 PyPI 包、有 smithery 一键装、三种 transport 都支持、有专门 TOOLS.md。命中 soft preferences（单功能强、TypeScript/Python 实现、含部署文档）。trade-off：场景偏窄（只处理 xlsx），不像浏览器/K8s 那么"通用"，但 Excel 在企业场景刚需，留一份在收藏夹很值。

---
*由 /gitout 生成 · 2026-05-25 · intent: "MCP server 生态合集 — 给 agent 加工具能力"*
