---
type: repo
repo: vaishcodescape/Omni-Graph
domain: knowledge-graph
status: active
discovered: 2026-05-25
last_reviewed: 2026-05-25
intent_matched: "端到端 KG 平台，文档→实体→4 种 search 策略，含 MCP server"
signals:
  stars: 3
  last_commit: 2026-05-12
  language: Python
  license: unknown
url: https://github.com/vaishcodescape/Omni-Graph
absorption:
  harvested: false
  used: false
  used_in: []
---

# Omni-Graph · 小白说明书

## 🧐 这是什么
"企业级 KG 平台的开源版"。FastAPI + PostgreSQL（pgvector，19 张表）+ Claude 抽实体 + Voyage AI 做 embedding。一套核心引擎对外暴露 3 个口子：REST API（14 endpoint）、MCP server（13 工具）、终端 TUI。

## 💡 解决什么问题
- 想给团队/公司做一个**带权限控制**的内部知识库（RBAC + 4 级敏感度）
- 同时要 fulltext / semantic / graph / hybrid 四种检索，按场景选
- 想要带引用的对话式问答（Claude Opus 跑 tool-use 循环）
- 文档源杂：PDF / DOCX / URL / 纯文本都要吃

## 🎯 谁该用 / 谁别用
**适合你如果：**
- 想看一个**架构清晰**的 KG 平台是怎么落地的（数据库 schema 完整公开）
- 需要 SHA-256 去重 + 自动版本管理 + audit log
- 用得起 Claude API + Voyage AI（或愿意改 provider）

**别浪费时间如果：**
- 想要纯本地 + 免费——Claude/Voyage 都要付费 API
- 只是个人笔记几百条，19 张表 schema 是过度设计
- 不想搞 Docker + PostgreSQL

## 🚀 三分钟上手
```bash
git clone https://github.com/vaishcodescape/Omni-Graph
cd Omni-Graph
docker-compose up -d  # 起 PostgreSQL + pgvector + FastAPI
# 填 .env：ANTHROPIC_API_KEY / VOYAGE_API_KEY

# 终端 TUI 走一遍
python -m omnigraph.cli

# 或直接调 API
curl -X POST localhost:8000/api/v1/documents/upload -F file=@paper.pdf
curl -X POST localhost:8000/api/v1/search -d '{"query":"...","strategy":"hybrid"}'
```

## 🔑 关键文件 / 关键概念
- 4 种 search 策略：`fulltext`（tsvector）/ `semantic`（pgvector 余弦）/ `graph`（递归 CTE BFS）/ `hybrid`（加权混合）
- MCP 13 工具含 `search` / `find_experts` / `find_related_concepts` / `get_entity_documents`
- RBAC 4 级敏感度，row-level 强制
- Claude Haiku 抽 entity（带 LLM 不可用时的 keyword fallback），Claude Opus 做 agent RAG

## ⚠️ 踩坑提示
- 抽 entity + embedding 都要付费 API，document 多了账单会涨
- PostgreSQL 19 张表 schema，第一次跑前最好通读一遍 `database-schema.jpeg`
- 只有 3 stars，**早期项目**，breaking change 风险高
- Voyage 是小厂 embedding provider，国内访问要梯子

## 🤔 为什么这次推它给你
你说"输出真实图结构" + "LLM 驱动抽取"——Omni-Graph 是候选池里**架构最完整、search 策略最丰富**的实现。19 张表 + 4 种 search + MCP + REST + TUI 三接口，几乎是一份"KG 平台教科书"。Trade-off：付费 API 依赖把它推离了"纯本地"硬约束，但你可以照着它的 schema 设计去理解工业级 KG 该长什么样。

---
*由 /gitout 生成 · 2026-05-25 · intent: "从非结构化文本自动抽取实体关系、构建可视化知识图谱"*
