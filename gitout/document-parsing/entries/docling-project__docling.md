---
type: repo
repo: docling-project/docling
domain: document-parsing
status: active
discovered: 2026-06-02
last_reviewed: 2026-06-02
intent_matched: "MinerU 同类：多格式 → Markdown / JSON，Apple Silicon 友好"
signals:
  stars: 60780
  last_commit: 2026-06-01
  language: Python
  license: MIT
url: https://github.com/docling-project/docling
absorption:
  harvested: false
  used: true
  used_in: ["docmd-skill"]
---

# docling-project/docling · 小白说明书

## 🧐 这是什么
IBM Research 出品的"文档 → 结构化 Markdown"转换器，现已捐给 LF AI & Data。不光收 PDF：DOCX / PPTX / XLSX / HTML / PNG 全吃，统一吐 Markdown 或 DoclingDocument JSON。Mac 上是 MPS 友好的明星级方案，James 自己的 /docmd skill 里也已经把它列为 PDF 回退引擎。

## 💡 解决什么问题
- 知识库 / RAG 想统一吃多格式文档，不希望 docx 走一套 / pdf 走一套
- 想要"开箱即用"的高准确度版式 + 表格识别，又不想啃 MinerU 的模型权重大坑
- 想保留图片 / 公式的 caption 关联（DoclingDocument 把它们结构化挂在一起）

## 🎯 谁该用 / 谁别用
**适合你如果：** 文档类型杂（不光 PDF）；要 MIT 许可证（商用无压力）；想要长期维护有大厂背书
**别浪费时间如果：** 只处理纯中文古籍 / OCR 重度场景（MinerU / olmocr 强）；硬件极弱（树莓派别想）

## 🚀 三分钟上手
```bash
pip install docling
# 单文件
docling your.pdf --to md --output out/
# Python API
python -c "from docling.document_converter import DocumentConverter; \
  print(DocumentConverter().convert('your.pdf').document.export_to_markdown())"
```

## 🔑 关键文件 / 关键概念
- `DocumentConverter` — 入口类，所有格式走它
- `DoclingDocument` — 中间表示，可序列化为 JSON / Markdown / HTML
- `pipeline_options` — 切 OCR 引擎 / 关图片描述 / 改模型，调优都在这里
- 默认模型 ~300MB，比 marker 轻；首次跑自动下载
- 配套兄弟项目：`docling-eval`（评测）、`docling-sdg`（合成数据）、`docling-graph`（→ KG）

## ⚠️ 踩坑提示
- 表格识别（TableFormer 模型）在双栏复杂版式仍会漏行，看场景测过再上
- 默认不做 OCR，纯扫描 PDF 要显式 `pipeline_options.do_ocr=True` 才走 EasyOCR
- 配套 `docling-sdg` / `docling-eval` 不必装，只要主包就能跑

## 🤔 为什么这次推它给你
- 命中"MinerU 差不多" → 同样是"复杂文档 → 结构化 md"赛道里的旗舰，并且 stars 比 MinerU 还高
- 命中"Mac mini 系统" → MPS 一等支持，模型轻，8GB 也能跑（marker 容易 OOM 它不容易）
- 命中"软偏好：MIT 友好" → 比 marker（GPL-3.0）、MinerU（AGPL-3.0）许可证宽松得多
- trade-off：默认不开 OCR，扫描件场景需手动配置；纯中文优势不如 MinerU

---
*由 /gitout 生成 · 2026-06-02 · intent: "寻找和 MinerU 差不多的开源项目，适合 Mac mini 系统的"*
