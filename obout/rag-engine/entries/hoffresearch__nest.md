---
type: repo
repo: hoffresearch/nest
domain: rag-engine
status: active
discovered: 2026-05-25
last_reviewed: 2026-05-25
intent_matched: "单文件可分发的本地 RAG 容器"
signals:
  stars: 5
  last_commit: 2026-05-19
  language: Rust
  license: MIT
url: https://github.com/hoffresearch/nest
absorption:
  harvested: false
  used: false
  used_in: []
---

# nest · 小白说明书

## 🧐 这是什么
一个 `.nest` 单文件容器把"chunks + 向量 + 源文档 span + ANN/BM25 索引"全部打包进去，Python 负责"建"，Rust 负责"读"，mmap + SIMD 直读硬盘出结果，**没有 server 这个概念**。

## 💡 解决什么问题
- 你想把一份精挑细选的知识库（比如公司内部文档 / 一本书 / 一个垂类语料）**像 SQLite 文件那样 ship 给用户**，而不是让用户去连你的云。
- 你做边缘部署 / 离线手机 app / 监管严格的环境（金融/医疗/政府），查询不允许出本地盒子。
- 你想要可复现 build：同样的输入 → 字节完全一致的 `.nest` 文件，方便审计和签名。

## 🎯 谁该用 / 谁别用
**适合你如果：**
- 你的 use case 是"分发知识库"而不是"频繁写入更新"——典型如教材、产品手册、法规库。
- 你想做"知识库随 app 一起出货"的产品形态。
- 你看重 SHA-256 校验、citation ID 稳定、reproducible build 这种"工程严肃性"。

**别浪费时间如果：**
- 你需要频繁增删改查（这是 build-once-serve-many 的模型）。
- 你想要现成的 UI / 完整 RAG 应用（这只是文件格式 + runtime）。
- 你完全不想接触 Python 构建链。

## 🚀 三分钟上手
```python
# Python 端：构建 .nest 文件
from nest_builder import build
build(
    chunks=[{"canonical_text": "...", "source_uri": "...",
             "byte_start": 0, "byte_end": 100, "embedding": [...]}],
    reproducible=True,
    preset="hybrid",   # exact | compressed | tiny | hybrid
)
```

```bash
# Rust 端：直接搜
nest search-text my-corpus.nest "查询内容" --model-path ./model
```

## 🔑 关键文件 / 关键概念
- `.nest` 容器 v1 格式：chunks / embeddings / ANN section 0x07 / BM25 section 0x08 全在一个文件。
- 四种 preset：`exact`（recall=1）/ `compressed`（float16+zstd）/ `tiny`（int8 量化，最小可分发）/ `hybrid`（向量+BM25）。
- `dat/corpus_next.v1.nest` 是 demo 语料（PT-BR 假新闻数据集）。

## ⚠️ 踩坑提示
- 才 5 星、是研究型 repo，准备好读 architecture 文档（`doc/arc/arc.md`）。
- "build once" 模型——更新内容意味着重新 build 整个文件，**不适合频繁写入**。
- 用 `--model-path` 才能完全离线，否则首次会去拉 embedding 模型。

## 🤔 为什么这次推它给你
命中你最反共识的 soft pref：**single-file / sovereign / 零 server**。和 vecstore 不同，nest 的设计哲学是"知识库就是一个可签名可校验的文件"——这对"个人知识库底层"是另一种思路：你可以把整个 RAG 索引版本化、git-commit、备份。Trade-off 是冷门（5 ⭐）+ build-once 模型，但意图匹配度上**罕见地把"可分发性"做成了一等公民**。值得收藏。

---
*由 /gitout 生成 · 2026-05-25 · intent: "本地优先的 RAG / 向量检索引擎"*
