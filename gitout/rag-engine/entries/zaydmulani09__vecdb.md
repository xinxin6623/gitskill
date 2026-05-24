---
type: repo
repo: zaydmulani09/vecdb
domain: rag-engine
status: active
discovered: 2026-05-25
last_reviewed: 2026-05-25
intent_matched: "本地 hybrid search 向量数据库"
signals:
  stars: 7
  last_commit: 2026-05-18
  language: Rust
  license: Unknown
url: https://github.com/zaydmulani09/vecdb
absorption:
  harvested: false
  used: false
  used_in: []
---

# vecdb · 小白说明书

## 🧐 这是什么
纯 Rust 写的自托管向量库，**编出来是一个 10MB 左右的静态二进制**，启动 <1 秒，自带 HNSW + BM25 hybrid search 和一套类 SQL 的查询语法。Python / TypeScript SDK 都有。

## 💡 解决什么问题
- 你想要"向量服务"的形态（HTTP API、多客户端连接），但不想为它付云费、不想配 Docker compose。
- 你团队前后端是 Python + TS，想用同一个向量后端但 SDK 体验都要顺。
- 你想用 SQL 而不是花式 DSL 来写过滤条件（`WHERE VECTOR_SIM(vec, [...]) > 0.5 AND payload->>'year' > 2020`）。

## 🎯 谁该用 / 谁别用
**适合你如果：**
- 你要轻量自托管的"小 Qdrant 替代"——单二进制、scp 上去就能跑。
- 你想要 hybrid search 的 alpha 权重调控（向量 vs BM25 比例可调）。
- 你欣赏"SQL + 向量函数"这种直觉式查询。

**别浪费时间如果：**
- 你想要纯嵌入式（in-process）调用——它是 client-server 模型（默认 6333 端口）。
- 你看重许可证清晰度（README 写 MIT 但 GitHub 没识别出 license 文件，**用前先确认**）。
- 你需要成熟生态（这是个人项目、7 ⭐，**别拿来跑生产**）。

## 🚀 三分钟上手
```bash
# 编出 server
cargo build --release -p vecdb-server
./target/release/vecdb-server  # 监听 :6333

# Python SDK
pip install ./sdks/python
```

```python
from vecdb import VecDbClient, VectorRecord
client = VecDbClient(base_url="http://localhost:6333")
client.create_collection("docs", dimension=768)
client.upsert("docs", [VectorRecord(id="d1", vector=[...], text="...")])
results = client.search_hybrid("docs", vector=[...], query="ml", k=10, alpha=0.7)
```

## 🔑 关键文件 / 关键概念
- `alpha` 参数：1.0 纯向量、0.0 纯 BM25、0.7 偏语义。
- 类 SQL 查询：`VECTOR_SIM(vec, [...]) > threshold` + `payload->>'key'` 过滤。
- CLI 工具 `vecdb` 支持 ingest JSONL / dense / sparse / hybrid / sql 各种模式。

## ⚠️ 踩坑提示
- License 信号不一致（README 说 MIT，GitHub 没识别），**正式用前先看 LICENSE 文件**。
- 7 ⭐ 个人项目，没有社区，遇坑只能自己读源码。
- 是 client-server 模式，**不能像 vecstore 那样 in-process 嵌入**——这是设计哲学差异。

## 🤔 为什么这次推它给你
你 hard constraint 里写了"本地可运行（embedded 或自托管）"——vecdb 走的是"**自托管**"那条路，正好补 vecstore（embedded）的另一面：当你想"一个本地小 server 给多个工具/agent 共享同一份索引"时，单二进制 + SQL 风格的 vecdb 比起 Qdrant 那种重型 stack 友好太多。trade-off 是冷门、license 待确认；但作为"个人知识库共享后端"形态，它是这一批里最像样的。

---
*由 /gitout 生成 · 2026-05-25 · intent: "本地优先的 RAG / 向量检索引擎"*
