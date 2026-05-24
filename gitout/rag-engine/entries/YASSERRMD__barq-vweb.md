---
type: repo
repo: YASSERRMD/barq-vweb
domain: rag-engine
status: active
discovered: 2026-05-25
last_reviewed: 2026-05-25
intent_matched: "浏览器原生本地向量检索"
signals:
  stars: 19
  last_commit: 2026-03-13
  language: Rust
  license: MIT
url: https://github.com/YASSERRMD/barq-vweb
absorption:
  harvested: false
  used: false
  used_in: []
---

# barq-vweb · 小白说明书

## 🧐 这是什么
Rust 写、编成 WASM 跑在**浏览器里**的向量数据库。自带 MiniLM 句嵌入模型（在 Web Worker 里跑）、HNSW 索引、BM25 + 向量 RRF 融合、SIMD 加速、用 OPFS / IndexedDB 持久化——一行 npm install 就能给前端加语义搜索，**零后端**。

## 💡 解决什么问题
- 你做 web app 想加"搜笔记 / 搜对话历史 / 搜文档"，但不想自己起向量服务。
- 你做隐私敏感产品（医疗记录 / 律师案件 / 个人日记），数据**禁止离开浏览器**。
- 你做 Chrome extension / Electron 应用，想就地建本地 RAG 又不想绑 Python 后端。

## 🎯 谁该用 / 谁别用
**适合你如果：**
- 你是前端工程师，想用 TS/JS 就能用上"完整的 RAG 检索栈"。
- 你的数据规模在万到十万向量级别（README benchmark 10k 向量 kNN 1.2ms，M2 Pro 实测）。
- 你需要 WebGPU / SIMD 加速且能接受较新的浏览器（Chrome/Edge 113+、Safari 17+）。

**别浪费时间如果：**
- 你的产品要兼容老浏览器（OPFS / WebGPU 都要新版本）。
- 你的向量量级 >100 万（浏览器 IndexedDB 不是为这设计的）。
- 你需要 Node.js 后端用——它定位明确是 browser-native。

## 🚀 三分钟上手
```bash
npm install barq-vweb
```

```typescript
import { BarqVWeb } from "barq-vweb";

const db = new BarqVWeb("my-collection");
await db.init();   // 加载 WASM + SIMD + MiniLM embedding 模型

await db.insertTexts([
  "Rust is a systems programming language focused on safety.",
  "WebAssembly enables near-native speed in the browser."
]);

const results = await db.search("fast systems programming", { limit: 5 });
```

## 🔑 关键文件 / 关键概念
- 自带 `all-MiniLM-L6-v2` embedding（Transformers.js + Web Worker）——**真的零依赖能算 embedding**。
- HNSW + Product Quantization 双重提速。
- 持久化走 OPFS（首选）/ IndexedDB（兜底）。
- 同作者另一项目 `barq-wasm` 提供 16-wide SIMD / WebGPU kernel。

## ⚠️ 踩坑提示
- 首次 `init()` 要下载 WASM + MiniLM 模型（**几十 MB**），做好 loading UI。
- README benchmark 是 M2 Pro 数据，普通 PC + 老机型会显著降速。
- 最近 commit 2026-03 月，相对没那么活跃，遇 issue 自查能力要 ok。

## 🤔 为什么这次推它给你
其他四个项目都是"本地进程 / 本地 server"形态，barq-vweb 是这一批里**唯一把战场放到浏览器**的，给"本地优先 RAG"开了第二条路：当你的"本地"指**用户的浏览器**而不是你的服务器时，它是最直接的选择。命中 hard constraint「本地可运行」+ soft pref「Rust 高性能 / hybrid search」，软偏好里"单文件"换成了"单 npm 包"。Trade-off 是规模上限低、需要现代浏览器；但场景独特性极强，值得为"web 端个人知识库 / 浏览器扩展"这条赛道留一份。

---
*由 /gitout 生成 · 2026-05-25 · intent: "本地优先的 RAG / 向量检索引擎"*
