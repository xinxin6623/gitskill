# mcp-servers · MCP server 生态合集

## 健康度
- entries: 5
- last_updated: 2026-05-25
- focus: 给 Claude Code / Codex / Cursor 等 agent 扩展工具能力的 MCP server 实现（合集 + 单功能强 server）

## 当前条目
| Repo | 一句话 |
|------|--------|
| [modelcontextprotocol/servers](entries/modelcontextprotocol__servers.md) | Anthropic 官方 MCP 参考 server 合集 + 全 SDK 入口 |
| [appcypher/awesome-mcp-servers](entries/appcypher__awesome-mcp-servers.md) | 5.5k⭐ 社区 MCP server 大目录，按场景翻清单 |
| [hangwin/mcp-chrome](entries/hangwin__mcp-chrome.md) | Chrome 扩展型 MCP server，接管你已登录的真实 Chrome |
| [haris-musa/excel-mcp-server](entries/haris-musa__excel-mcp-server.md) | Python 写的 Excel MCP server，不依赖 Microsoft Office |
| [containers/kubernetes-mcp-server](entries/containers__kubernetes-mcp-server.md) | Go 原生 K8s MCP server，直接走 API，不包 kubectl |

## 区分说明
- 本 domain 收 **MCP server 实现**（agent 通过 MCP 协议调用的工具端）
- `claude-skills/` 收 Claude Code Skill / Hook / subagent 生态（agent 侧能力组织方式）
- 既属于 Skill 集合又含 MCP server 的项目（如 awesome-claude-code 系列），归 claude-skills 不重复收录
