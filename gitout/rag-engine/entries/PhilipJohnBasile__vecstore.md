---
type: repo
repo: PhilipJohnBasile/vecstore
domain: rag-engine
status: active
discovered: 2026-05-25
last_reviewed: 2026-05-25
intent_matched: "本地能跑的 RAG / 嵌入式向量检索"
signals:
  stars: 14
  last_commit: 2026-04-03
  language: Rust
  license: Apache-2.0
url: https://github.com/PhilipJohnBasile/vecstore
absorption:
  harvested: false
  used: false
  used_in: []
---

# VecStore · 小白说明书

## 🧐 这是什么
作者自封"向量搜索界的 SQLite"——一个 Rust 写的嵌入式向量库，像调 SQLite 一样 `open("vectors.db")` 就开干，不用起任何 server。

## 💡 解决什么问题
- 你想给 app 加一点语义搜索（比如本地文档问答），但不想拉起 Pinecone/Qdrant 这种重型服务。
- 你想让 RAG 在浏览器里跑（隐私敏感的法律/医疗场景），数据一字节都不要出用户设备。
- 你做 prototype 想三行代码验证想法，跑通了再决定上不上分布式。

## 🎯 谁该用 / 谁别用
**适合你如果：**
- 你写 Rust / Python / 前端 JS，想"嵌入一个向量 store"而不是"集成一个向量服务"。
- 你需要 hybrid search（向量 + BM25 + metadata 过滤），且预期数据量在百万级以内。
- 你想要一个能在浏览器 WASM 里跑的方案（同一份代码 server + 客户端通吃）。

**别浪费时间如果：**
- 你的数据是十亿级 + 多租户线上业务（作者也写了 alpha 阶段、API/文件格式可能变）。
- 你只想要 Python 上层框架糖（这是底层 store，不是 LangChain 替代）。
- 你完全不写代码，想要开箱 UI（这是库不是产品）。

## 🚀 三分钟上手
```bash
# Rust
cargo add vecstore

# Python
pip install vecstore-rs

# 浏览器
npm install vecstore-wasm
```

```rust
use vecstore::VecStore;
let mut store = VecStore::open("vectors.db")?;
store.upsert("doc1", vec![0.1, 0.2, 0.3], json!({"title": "Hello"}))?;
let results = store.query(&query_vec, 10)?;
```

## 🔑 关键文件 / 关键概念
- `VecStore::open()` — 像 SQLite 一样以单文件打开/创建数据库。
- HNSW 索引 + 9 种距离度量（cosine / L2 / dot product / Hamming / Jaccard …）。
- `query_with_filter` 支持 SQL 风格的 metadata 过滤表达式。
- WAL（write-ahead log）可选开启做崩溃恢复。

## ⚠️ 踩坑提示
- README 自标 0.1.x alpha——**文件格式和 API 可能改**，不要拿它存你重生成不出来的数据。
- 浏览器版要先 `await init()` 加载 WASM，初次加载有几百 KB 的成本。
- "Distributed system with Raft consensus" 这种 roadmap 项已经勾掉了，但跑生产前自己验证下稳定性。

## 🤔 为什么这次推它给你
直接对位你的 hard constraint「本地可跑 + 嵌入式」和 soft pref「SQLite 类单文件 DB / Rust 高性能 / hybrid search」——它三条全中。"SQLite of vector search" 这个 slogan 不是吹的：单文件、零 server、Rust core + Python/JS bindings，是这一轮里**最贴你"个人知识库底层"画像**的那个。Trade-off 是星数才 14、alpha 阶段；但意图匹配度优先于热度，符合你显式表达的"反过度框架化"偏好。

---
*由 /gitout 生成 · 2026-05-25 · intent: "本地优先的 RAG / 向量检索引擎"*
