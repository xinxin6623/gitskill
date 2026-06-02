---
type: repo
repo: TheAiSingularity/graphrag-local-ollama
domain: knowledge-graph
status: active
discovered: 2026-05-25
last_reviewed: 2026-05-25
intent_matched: "本地跑的 GraphRAG，把文本变成实体图 + 社区摘要 + 可视化"
signals:
  stars: 1102
  last_commit: 2026-05-08
  language: Python
  license: MIT
url: https://github.com/TheAiSingularity/graphrag-local-ollama
absorption:
  harvested: false
  used: false
  used_in: []
---

# graphrag-local-ollama · 小白说明书

## 🧐 这是什么
微软 GraphRAG 的"本地白嫖版"。把 OpenAI API 全替换成 Ollama 本地模型，原版那套"抽实体 → 建知识图 → 社区摘要 → 全局问答"流程完整保留。

## 💡 解决什么问题
- 想试 GraphRAG 但不想每次 indexing 烧几十刀 OpenAI 费用
- 想问"这堆文档的主要主题是什么"这种**全局问题**（普通向量 RAG 答不了）
- 数据敏感，不能进云端 API
- 想要一个能在浏览器里直接看的**交互式知识图**

## 🎯 谁该用 / 谁别用
**适合你如果：**
- 有一台带 GPU 的机器（或 Mac M 系列），Ollama 能跑 llama3/qwen/mistral
- 文档量在几万到百万 token，普通 RAG 已经力不从心
- 想理解"GraphRAG 到底是个什么东西"，需要一个能跑通的参考实现

**别浪费时间如果：**
- 只是想找个向量数据库，那直接用 chromadb / qdrant 更简单
- 笔记只有几百条，纯 Obsidian 双链就够了
- 没耐心装 Docker / 配 Ollama

## 🚀 三分钟上手
```bash
git clone https://github.com/TheAiSingularity/graphrag-local-ollama
cd graphrag-local-ollama
cp .env.example .env
docker-compose up --build
# 把 .txt 丢进 ./input/，自动索引
# 浏览器开 http://localhost:7860 看 Web UI
```

## 🔑 关键文件 / 关键概念
- `docker-compose.yml` — Ollama + GraphRAG 一键起
- `app.py` — Web UI（索引 / 查询 / 图可视化 / 设置 四个 tab）
- `settings.yaml` — 切 LazyGraphRAG 模式、调 chunk size、改模型名
- **5 种查询模式**：Global（全局摘要）/ Local（精准实体）/ DRIFT（迭代推理）/ Basic（快速向量）/ Lazy（建索引快 99%）

## ⚠️ 踩坑提示
- LazyGraphRAG 索引快但**首次查询慢**——summaries 在查询时才算
- Ollama 跑小模型抽 entity 质量明显不如 GPT-4，复杂文档考虑 qwen2.5:7b+
- DRIFT 模式必须有 community reports，开了 lazy 就用不了
- CJK 支持是新加的，老 issue 里 fix 可能没合

## 🤔 为什么这次推它给你
你说"开源、能本地跑、输出真实图结构（非简单 wiki 双链）"——这条命中三个核心硬约束：纯本地 Ollama、生成的是带 community 的真实知识图、还附带 HTML 可视化。1100+ stars 是本类目里**唯一过千星且能本地跑的 GraphRAG 实现**，文档完备到 docker-compose 直接起。trade-off：底子还是微软 GraphRAG，离个人工作流嵌入有点重，更像研究/原型平台。

---
*由 /gitout 生成 · 2026-05-25 · intent: "从非结构化文本自动抽取实体关系、构建可视化知识图谱"*
