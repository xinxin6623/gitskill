# document-parsing · 文档结构化解析（PDF/DOCX → Markdown）

> "复杂文档（PDF / 扫描件 / DOCX / PPTX） → 结构化 Markdown / JSON" 工具集合。MinerU 同档位的开源对标方案，重点筛选**适合 Mac mini（Apple Silicon, 无 CUDA）的本地路线**。

## 健康度

- entries 数：5
- 最后更新：2026-06-02
- 状态：active

## 速览（按 stars）

| Repo | ⭐ | 路线 | 许可证 | 一句话 |
| --- | ---: | --- | --- | --- |
| [docling-project/docling](./entries/docling-project__docling.md) | 60.8k | 多模型流水线 | MIT | IBM 出品，多格式吃，Mac MPS 一等支持 |
| [datalab-to/marker](./entries/datalab-to__marker.md) | 35.6k | 多模型流水线 | GPL-3.0 | MinerU 最直接对标，英文论文精度第一梯队 |
| [allenai/olmocr](./entries/allenai__olmocr.md) | 17.4k | VLM 端到端 | Apache-2.0 | AllenAI 7B VLM 直接读 PDF，前沿但吃硬件 |
| [Unstructured-IO/unstructured](./entries/Unstructured-IO__unstructured.md) | 14.8k | 多格式管线框架 | Apache-2.0 | LangChain 默认推荐，25 种格式统一接口 |
| [RapidAI/RapidDoc](./entries/RapidAI__RapidDoc.md) | 163 | ONNX 轻量管线 | Apache-2.0 | 无 PyTorch 依赖，Mac mini 内存友好（反共识首选） |

## 怎么选

- **想要最高精度 + 多格式 + MIT 许可**：上 `docling`，这是 8GB Mac mini 上的默认推荐
- **只处理英文学术 PDF，要榜单第一**：上 `marker`，准备好 16GB 内存
- **想跟 VLM 端到端的前沿**：上 `olmocr`，准备好 16GB 内存 + 等首次 14GB 模型下载
- **要做 RAG 管线，要统一接口处理 25 种格式**：上 `unstructured`，写一层 reducer 拿 md
- **Mac mini 8GB / 想躲 PyTorch / 中文为主**：上 `RapidDoc`，最轻量最干净的安装

## 与原始 MinerU 的差别

MinerU 本身就在它的 AGPL-3.0 许可证下；本 domain 不收录 MinerU，但 5 条 entries 都是按"和 MinerU 同档位、Mac mini 可跑"标准筛出的同行。如果 MinerU 用得顺手，**docling + RapidDoc 是最值得对比测试的两个候补**。
