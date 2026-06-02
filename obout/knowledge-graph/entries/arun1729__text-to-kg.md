---
type: repo
repo: arun1729/text-to-kg
domain: knowledge-graph
status: active
discovered: 2026-05-25
last_reviewed: 2026-05-25
intent_matched: "最小可读 demo：文本→实体→图+embedding→3 种查询"
signals:
  stars: 3
  last_commit: 2026-02-19
  language: Python
  license: unknown
url: https://github.com/arun1729/text-to-kg
absorption:
  harvested: false
  used: false
  used_in: []
---

# text-to-kg · 小白说明书

## 🧐 这是什么
CogDB（嵌入式图数据库）官方的"文本→知识图"最小 demo。整套 pipeline 就 2 个 .py 文件 + 1 个 .sh：抽实体、抽关系、entity resolution、embedding、塞进 CogDB，然后演示三种查询（图遍历 / 语义 / 混合）。

## 💡 解决什么问题
- 想搞懂"text → knowledge graph"流程到底每一步在干啥，但 GraphRAG / Omni-Graph 那套读不动
- 想要个 ≤300 行的参考实现，看完直接 fork 改成自己的
- 不想装 Neo4j / PostgreSQL，要个**嵌入式**图库

## 🎯 谁该用 / 谁别用
**适合你如果：**
- 第一次接触 KG 构建，需要一个**能在 10 分钟内跑完**的最小例子
- 在评估 CogDB 这种 Python embedded 图库
- 想看典型的"entity → relation → resolution → embed → query"五段范式怎么写

**别浪费时间如果：**
- 要上生产，CogDB 还偏小众
- 文档量大——demo 写得最小化，scale 要自己加 batching
- 想要 UI / 可视化，这就是个命令行 demo

## 🚀 三分钟上手
```bash
git clone https://github.com/arun1729/text-to-kg
cd text-to-kg
echo 'OPENAI_API_KEY=sk-...' > .env
./run.sh
# 第一次：调 OpenAI 抽 entity/relation，缓存到 kg_data.json
# 之后：直接读 cache 跑查询
./run.sh --clean  # 想推倒重来
```

## 🔑 关键文件 / 关键概念
- `etl.py` — Extract → Resolve → Embed → Load 全流程
- `query.py` — A 段图遍历 / B 段语义 kNN / C 段混合（BFS + embedding 过滤）
- `kg_data.json` — 抽完缓存，省 API 钱
- 范例数据：`planetary-habitability.txt`（行星宜居性，60 行文本）

## ⚠️ 踩坑提示
- 必须 OpenAI（demo 写死 gpt-5 + text-embedding-3-small），换 provider 要自己改
- CogDB 是 embedded 库，**多进程并发会冲突**
- entity resolution 只做最简单的 alias 归并，复杂场景要自己加规则
- demo 只演示 60 行文本，几千行就要自己加 chunking

## 🤔 为什么这次推它给你
你说"开源、能本地跑、输出真实图结构"——text-to-kg 是候选池里**最容易啃完源码**的一个。它不解决你的生产问题，但解决你的**理解问题**：把 GraphRAG 那些花哨的 community / DRIFT 全剥掉，剩下的就是"抽 entity → 抽 relation → 归并 → embed → 三种查询"五步。看完再去读 graphrag-local-ollama / Omni-Graph 会顺很多。Trade-off：纯 demo，3 stars，别拿它直接生产。

---
*由 /gitout 生成 · 2026-05-25 · intent: "从非结构化文本自动抽取实体关系、构建可视化知识图谱"*
