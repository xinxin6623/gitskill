---
type: synthesis
topic: 本地 AI 栈
created: 2026-05-30
domains:
  - gitout/local-llm-runtime/
  - gitout/rag-engine/
  - gitout/knowledge-graph/
  - gitout/mcp-servers/
status: draft
---

# 本地 AI 栈 · 跨域洞见

## 背景

用户不满足于 Ollama 跑模型——想要一套**完全本地的 AI 基础设施**：推理 + 检索 + 图谱 + 工具接入。这 4 个 domain 是互锁的底座。

## 涉及 domain 一览

| Domain | 核心贡献 | 局限 |
|--------|---------|------|
| [[gitout/local-llm-runtime/README.md\|local-llm-runtime]] | Apple Silicon 本地推理运行时，7B-30B 模型 | 需要 16GB+ 内存；30B 以上需量化 |
| [[gitout/rag-engine/README.md\|rag-engine]] | 本地优先向量检索引擎，嵌入式/WASM/自托管 | 生态较新，不成熟；大多数星数低 |
| [[gitout/knowledge-graph/README.md\|knowledge-graph]] | LLM 驱动的实体关系抽取，可查询图结构 | 小规模文本效果波动；非 GraphRAG 模式开销大 |
| [[gitout/mcp-servers/README.md\|mcp-servers]] | 给 agent 扩展工具的 MCP server 实现 | 需要 Claude Code/Codex 支持 MCP；兼容性需验证 |

## 综合结论

1. **llamafile + vecstore 是最短本土 RAG 路径**：单文件推理 + 嵌入式向量库，两个 Rust 二进制就搭起检索问答
2. **GraphRAG 是可选升级**：当"总结这堆文档的主要主题"这类全局问题出现时再上，不做默认
3. **MCP servers 是连接层**：把前三者的能力暴露给 AI agent，实现"本地推理 → 本地检索 → agent 工具调用"闭环
4. **当前不适合生产级**：除 llamafile 外星数普遍 ≤100，接口稳定性待观察

## 推荐路径

1. 起点：[[gitout/local-llm-runtime/entries/mozilla-ai__llamafile.md|llamafile]] + [[gitout/rag-engine/entries/PhilipJohnBasile__vecstore.md|vecstore]] + [[gitout/mcp-servers/entries/modelcontextprotocol__servers.md|MCP reference servers]]
2. 进阶：加 [[gitout/knowledge-graph/entries/TheAiSingularity__graphrag-local-ollama.md|graphrag-local-ollama]] 做全局查询
3. 延展：用 [[gitout/rag-engine/entries/benmaster82__Kwipu.md|Kwipu]] 给 Obsidian 直接挂 Graph RAG

## 更新历史

- 2026-05-30：初稿，覆盖 4 domain 的跨域分析
