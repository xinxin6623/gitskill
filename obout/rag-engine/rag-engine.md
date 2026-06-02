# rag-engine · 本地优先的 RAG / 向量检索引擎

## 健康度
- entries: 5
- last_updated: 2026-05-25
- focus: 嵌入式 / 自托管 / 浏览器原生的向量库，可作为个人知识库底层

## 当前条目
| Repo | 一句话 |
|------|--------|
| [[rag-engine/entries/PhilipJohnBasile__vecstore|PhilipJohnBasile/vecstore]] | "向量界的 SQLite"，Rust 嵌入式 + 浏览器 WASM + hybrid search |
| [[rag-engine/entries/hoffresearch__nest|hoffresearch/nest]] | 把整个 RAG 知识库塞进一个 `.nest` 单文件，签名可校验、像分发 SQLite db |
| [[rag-engine/entries/zaydmulani09__vecdb|zaydmulani09/vecdb]] | 单二进制自托管 Rust 向量服务，hybrid + 类 SQL 查询 |
| [[rag-engine/entries/benmaster82__Kwipu|benmaster82/Kwipu]] | 本地 Graph RAG 给 Obsidian/markdown 用，自带 MCP server |
| [[rag-engine/entries/YASSERRMD__barq-vweb|YASSERRMD/barq-vweb]] | 浏览器原生 Rust+WASM 向量库，自带 MiniLM embedding，零后端 |

## 形态光谱
按"本地"的不同解读分四档：
- **嵌入式 in-process**：vecstore（最贴近 SQLite 体验）
- **可分发单文件容器**：nest（build-once-ship-many）
- **本地自托管 server**：vecdb（client-server，多客户端共享索引）
- **浏览器内**：barq-vweb（数据不离开用户设备）
- **完整应用**：Kwipu（端到端 Graph RAG，给 markdown 笔记直接用）

挑选时按"你想要的本地形态"对号入座即可。
