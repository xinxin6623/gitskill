---
type: repo
repo: Unstructured-IO/unstructured
domain: document-parsing
status: active
discovered: 2026-06-02
last_reviewed: 2026-06-02
intent_matched: "MinerU 同类：多格式文档 → 结构化 element，Mac 兼容"
signals:
  stars: 14821
  last_commit: 2026-06-01
  language: HTML
  license: Apache-2.0
url: https://github.com/Unstructured-IO/unstructured
absorption:
  harvested: false
  used: false
  used_in: []
---

# Unstructured-IO/unstructured · 小白说明书

## 🧐 这是什么
LangChain 默认推荐的"文档预处理瑞士军刀"。一上来不只盯 PDF：PDF / DOCX / EML / HTML / PPTX / 图片 / EPUB 二十多种格式都吃，统一吐 `Element` 列表（Title / NarrativeText / Table 等），下游你想怎么组就怎么组。也能输出 md / JSON。

## 💡 解决什么问题
- 个人 RAG 库要一份「能处理 25 种格式」的统一接口，而不是 PDF 一套、邮件一套
- 想要分级策略：能算的快 PDF（pdfminer / pdfplumber）走快路径，扫描件 / 表格才上模型
- 想要老牌、成熟、企业用过的方案，不是只跑通 demo 的实验项目

## 🎯 谁该用 / 谁别用
**适合你如果：** 文档类型杂、要喂给 LangChain / LlamaIndex；要稳、要长期维护；偏好"组合式" API 而不是"一键转 md"
**别浪费时间如果：** 只关心一两个 PDF 的极致 md 质量（用 marker / MinerU 更直接）；不想装 tesseract / poppler 等系统依赖；希望模型权重 < 100MB

## 🚀 三分钟上手
```bash
brew install poppler tesseract libmagic
pip install "unstructured[pdf]"   # 装多格式版用 [all-docs]
python -c "from unstructured.partition.auto import partition; \
  els = partition('your.pdf', strategy='hi_res'); \
  print('\n\n'.join(str(e) for e in els))"
```

`strategy` 三档：`fast`（pdfminer，秒级）/ `ocr_only`（纯扫描走 tesseract）/ `hi_res`（YOLOX layout + 表格模型）。

## 🔑 关键文件 / 关键概念
- `unstructured/partition/auto.py` — 自动路由入口
- `unstructured/partition/pdf.py` — PDF 三档策略源码
- `Element` 数据类 — 每段都带 type + metadata（页码 / 坐标 / 父子关系）
- 配套服务 `unstructured-api`（FastAPI 包装）便于本地起 server

## ⚠️ 踩坑提示
- 系统依赖多（poppler / tesseract / libmagic），Mac 上 brew 一把梭但首次装不算丝滑
- `hi_res` 策略要拉 ~500MB 模型，Mac mini 8GB 配合大 PDF 注意内存
- 输出是 `Element` 列表而不是直接 md，写一层简单 reducer 才能拿到漂亮 md
- 公司有 SaaS 版（Unstructured Platform），文档偶尔会跳到付费功能，注意区分

## 🤔 为什么这次推它给你
- 命中"MinerU 差不多" → 同样做"复杂文档 → 结构化"，但定位更偏"管线编排框架"
- 命中"Mac mini" → 纯 Python + 可选模型，最小配置可低至 1GB 内存
- 命中"软偏好"：Apache-2.0 商用友好；多格式统一接口适合个人知识库
- trade-off：默认输出不是 md 而是 `Element`，要包一层；纯 PDF→md 质量不如 marker

---
*由 /gitout 生成 · 2026-06-02 · intent: "寻找和 MinerU 差不多的开源项目，适合 Mac mini 系统的"*
