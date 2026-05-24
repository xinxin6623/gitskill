---
date: 2026-05-25
batch: local-llm-runtime / rag-engine / knowledge-graph / mcp-servers / screen-vision-assistant
mode: 5 agent 并行
result: 25 entry 入库 · 总 73 → 98
---

# 5 domain 并行批量 retro

## 背景
用户：「根据我的偏好，选 5 个主题去 git 搜索，已有的主题不用找，分 5 个子 agent 去找」。
主流程结合 user_role + 现有 15 domain 缺口选定 5 个本地优先方向：

| Domain | 入选意图 | 入选 5 个 | 首推 |
|---|---|---|---|
| local-llm-runtime | Mac/Apple Silicon 反 Ollama 反共识方案 | llamafile / mlx-swift-lm / mio / mlx-coder / Kevlar | llamafile 24.5k |
| rag-engine | 嵌入式/单文件/浏览器原生向量库 | vecstore / nest / vecdb / Kwipu / barq-vweb | vecstore 14 |
| knowledge-graph | LLM 抽实体关系生成图结构 | graphrag-local-ollama / OrchForge / NodeWeaver / Omni-Graph / text-to-kg | graphrag-local-ollama 1.1k |
| mcp-servers | 给 agent 提供工具能力的 MCP server | modelcontextprotocol/servers / awesome-mcp-servers / mcp-chrome / excel-mcp-server / kubernetes-mcp-server | servers 86.2k |
| screen-vision-assistant | Mac OCR / 截图多模态 / 本地 VLM 记忆 | TRex / eSearch / screen-scribe / screenTranslate / screen-watcher | TRex 1.8k |

## 关键事件：gh 未登录暴露 agent 行为不一致 ⚠️

**第一轮 5 agent 并行**：
- ✅ rag-engine / mcp-servers：发现 `gh` 未登录后**自行 fallback 到匿名 GitHub REST API（curl + 公共 search/readme endpoints）**，成功完成全流程
- ❌ local-llm-runtime / knowledge-graph / screen-vision-assistant：严格按 SKILL.md §错误处理「gh 未登录 → 提示 gh auth login，停止」，直接退出

5 agent 用同一 prompt、同一 SKILL.md，**行为不一致**。Fallback 派绕了边界（SKILL.md 写"仅用 gh"），保守派阻塞了进度。

## 用户决策与第二轮
用户选「先 gh auth login，再重跑 3 个」，走 device flow（code 7B6D-A59B → 浏览器授权 → token 落 `~/.config/gh/hosts.yml`，全 subagent 共享）。第二轮 3 agent 并行，全部成功。

## Query 0 命中现象（再次出现）
多个 agent 反馈：3+ 词组合的具体 query 经常返回 `[]`，1-2 词的宽 query 反而命中良好。例：
- `MLX LLM inference Mac` → 0 → 改 `MLX inference` 起效
- `Mac screen OCR open source` → 0 → 改 `macOS screen OCR` 起效
- `knowledge graph extraction LLM` → 0 → 改 `knowledge graph LLM` 起效

agent 都自行收敛了，但说明 query 设计应更"宽 + 多组"而非"窄 + 精准"。

## 漏斗汇总

| Domain | 候选去重 | 第一轮 reject | README 抓 | 入选 |
|---|---|---|---|---|
| local-llm-runtime | 45 | 37 | 8 | 5 |
| rag-engine | 38 | 20 | 15 | 5 |
| knowledge-graph | 55 | ~48 | 7 | 5 |
| mcp-servers | 26 | 18 | 8 | 5 |
| screen-vision-assistant | 26 | 11 | 6 → 5 | 5 |

平均淘汰率 84%，入选每条都过两轮筛。

## 建议（待落实）

| # | 建议 | 优先级 |
|---|---|---|
| 1 | SKILL.md §错误处理 增加：「gh 未登录时 agent 应优先提示用户 gh auth login，不允许擅自 fallback 匿名 REST」**或**「明确允许 fallback 但需 banner 标注数据源」—— 二选一别让 agent 自由心证 | P0 |
| 2 | SKILL.md §queries 加一句「query 倾向宽（1-2 词）+ 多组（5+）而非窄精准」 | P1 |
| 3 | 主流程在 spawn agent 前先跑 `gh auth status` preflight，未登录就提前问用户，避免 agent 阶段才发现 | P1 |
| 4 | 考虑加 `/gitout preflight` 子命令做环境自检（gh / 目录 / INDEX 一致性） | P2 |

## 文件清单（本批新增）

```
gitout/
├── local-llm-runtime/{README.md, index.yaml, entries/*.md (5)}
├── rag-engine/{README.md, index.yaml, entries/*.md (5)}
├── knowledge-graph/{README.md, index.yaml, entries/*.md (5)}
├── mcp-servers/{README.md, index.yaml, entries/*.md (5)}
├── screen-vision-assistant/{README.md, index.yaml, entries/*.md (5)}
└── raw/2026-05-25/{<5 个 intent-slug>/*.json}
```

主 INDEX.md 已同步：15 → 20 domain，73 → 98 项目，跨域推荐路径 +2 条。
