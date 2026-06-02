---
type: repo
repo: benmaster82/Kwipu
domain: rag-engine
status: active
discovered: 2026-05-25
last_reviewed: 2026-05-25
intent_matched: "本地 Graph RAG 给 markdown 笔记用"
signals:
  stars: 83
  last_commit: 2026-05-18
  language: Python
  license: MIT
url: https://github.com/benmaster82/Kwipu
absorption:
  harvested: false
  used: false
  used_in: []
---

# Kwipu · 小白说明书

## 🧐 这是什么
把你 Obsidian / 任意 markdown 文件夹的笔记，本地构建成**知识图谱 + 向量索引**，问一句话能跨多个文件拼答案。LLM 全走 Ollama 本地跑，自带 MCP server 可以塞进 Claude Desktop / Cursor / Windsurf。

## 💡 解决什么问题
- 你笔记越攒越多，关键词搜搜不出"我那篇关于 X 的想法"——需要语义搜。
- 你想让 Claude/Cursor 能"看见"你整个 vault，但不想把笔记上传到云。
- 你想要的不只是"找到那一篇"，而是"把分散在五篇里的相关片段拼起来回答我"。

## 🎯 谁该用 / 谁别用
**适合你如果：**
- 你已经是 Obsidian / markdown 重度用户，笔记数 50-500 篇。
- 你有一台还行的电脑（≥16GB RAM）能跑 7B 量化模型，或者愿意起 Ollama 远程。
- 你想 day-to-day 在 Claude/Cursor 里直接问"我之前在哪里写过 X"。

**别浪费时间如果：**
- 你没 GPU 又只有 3B 以下模型——构建会慢到怀疑人生（500+ 篇就别试了）。
- 你想要嵌入式 lib / SDK——这是个**完整可用的应用**而不是底层引擎。
- 你的笔记不是 markdown（PDF / Word 不在它适配范围内）。

## 🚀 三分钟上手
```bash
# 装 Ollama + 拉模型
ollama pull llama3.1:8b
ollama pull nomic-embed-text

# 装 Kwipu
git clone https://github.com/benmaster82/Kwipu && cd Kwipu
pip install -r requirements.txt

# 改 KNOWLEDGE_DIR 指向你的 vault，跑起来
python geode_graph.py
```

## 🔑 关键文件 / 关键概念
- `geode_graph.py` — 主程序（终端交互）。
- `kwipu_mcp_server.py` — MCP server，给 Claude Desktop / Cursor 当工具用。
- `storage_graph/` — 构建出的属性图持久化目录（自动生成）。
- Hybrid retrieval = 同义词 + 向量 + BM25 + 时间衰减融合。

## ⚠️ 踩坑提示
- **首次构建很慢**：每个 chunk 要 LLM 抽三元组，100 篇笔记 CPU 7B 要 3 小时（README 表格写得很清楚，先看）。
- 增量更新只对"修改 / 新增"快；**删除文件会触发全量重建**。
- 文档很大方提醒可以用云模型加速首次 build——你只想完全本地的话，准备好等。

## 🤔 为什么这次推它给你
直接命中你 scenario 描述的「已有 markdown 笔记，想本地建索引、混合检索、给 LLM 用」——这是这一轮唯一**端到端解决整个场景**的项目。其他四个偏底层 lib，Kwipu 是"开箱可用的本地 Graph RAG 应用"。MCP server 让它能直接挂到你用 Claude Code 的工作流里。Trade-off 是不轻量、必须 Ollama、build 慢；但意图匹配度上**它最像"个人知识库 RAG 的成品形态"**。

---
*由 /gitout 生成 · 2026-05-25 · intent: "本地优先的 RAG / 向量检索引擎"*
