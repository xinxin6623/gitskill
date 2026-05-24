---
type: repo
repo: OrchForge/RAG-GraphRAG-Knowledge-Base
domain: knowledge-graph
status: active
discovered: 2026-05-25
last_reviewed: 2026-05-25
intent_matched: "自托管 RAG+GraphRAG 完整栈，可嵌入 Claude Desktop 做个人工作流"
signals:
  stars: 0
  last_commit: 2026-05-09
  language: JavaScript
  license: unknown
url: https://github.com/OrchForge/RAG-GraphRAG-Knowledge-Base
absorption:
  harvested: false
  used: false
  used_in: []
---

# RAG-GraphRAG-Knowledge-Base · 小白说明书

## 🧐 这是什么
一套"向量 RAG + 知识图 GraphRAG 双引擎"的自托管知识库。Node.js 写的，Ollama 跑模型、Supabase + pgvector 存数据，自带可视化图编辑器和 MCP server——可以直接接进 Claude Desktop 当个人记忆。

## 💡 解决什么问题
- 想要"既能向量召回又能图遍历"的混合检索，但商业 SaaS（Mem0、Pinecone）不放心
- Claude Desktop 用着不爽，想给它接个能持久记忆 + 图推理的本地知识库
- 文档隐私分级，敏感内容只走本地 LLM，普通内容可走云
- 想看到 LLM 抽出来的实体图长啥样，最好能在浏览器里改

## 🎯 谁该用 / 谁别用
**适合你如果：**
- 会装 Node.js、有 Supabase 账号或想本地起 Postgres
- 重度用 Claude Desktop / Claude Code，想加个 MCP 知识库
- 喜欢"全本地 + 可选云"的渐进式隐私模型

**别浪费时间如果：**
- 不熟 Node 也不想学
- 只想要一键 GUI 应用（这是 CLI + Web 图编辑器）
- 文档不多，用普通向量库就够

## 🚀 三分钟上手
```bash
git clone https://github.com/OrchForge/RAG-GraphRAG-Knowledge-Base
npm install
cp .env.example .env  # 填 SUPABASE_URL + Ollama 配置
# 在 Supabase SQL Editor 跑 supabase_setup.sql
ollama pull bge-m3 && ollama pull qwen3:1.7b

node migrate.js 'docs/**/*.{md,txt,pdf}'   # 摄入
node graph_builder.js                       # 抽实体建图
node agents.js                              # 多 agent RAG+GraphRAG 问答
node graph_server.js                        # 浏览器看 / 改图
node server.js                              # 起 MCP server 给 Claude Desktop
```

## 🔑 关键文件 / 关键概念
- `agents.js` — Router → Researcher（向量） ‖ GraphExplorer（BFS 图遍历）→ Reranker → Synthesizer 五段 pipeline
- `graph_builder.js` — LLM 抽 entity + relation 写进 Supabase
- `graph_server.js` — Web 图编辑器（看节点、改关系、导出 PNG）
- `server.js` — MCP server，暴露 `query_knowledge_base` / `store_memory` 等工具
- 隐私分级：`local`（永不离机）/ `internal`（仅本地 LLM）/ `public`（可走云）

## ⚠️ 踩坑提示
- 强依赖 Supabase——不想用云端 Supabase 就得自己起 Postgres + pgvector
- 0 stars 新项目，README 干净但**没社区**，issue 不一定有人回
- 多 agent pipeline 每问一次要跑好几个 LLM call，小模型上要等
- `qwen3:1.7b` 默认配置抽 entity 偏弱，复杂文档建议换大模型

## 🤔 为什么这次推它给你
你说"易嵌入个人工作流" + "LLM 驱动抽取" + "本地跑" + "真实图结构"——这是候选池里**唯一同时具备 MCP server + 图编辑器 UI + 隐私分级**的实现。Node.js 栈对前端友好，pgvector + 图表分离的设计也比塞一个 Neo4j 轻量。Trade-off：星数 0，等于在押注实现质量；Supabase 依赖如果你抗拒云就要自建 Postgres。

---
*由 /gitout 生成 · 2026-05-25 · intent: "从非结构化文本自动抽取实体关系、构建可视化知识图谱"*
