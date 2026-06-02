---
type: repo
repo: RapidAI/RapidDoc
domain: document-parsing
status: active
discovered: 2026-06-02
last_reviewed: 2026-06-02
intent_matched: "MinerU 同类：复杂 PDF → md，ONNX 轻量、无需 PyTorch（Mac mini 反共识首选）"
signals:
  stars: 163
  last_commit: 2026-05-24
  language: Python
  license: Apache-2.0
url: https://github.com/RapidAI/RapidDoc
absorption:
  harvested: false
  used: false
  used_in: []
---

# RapidAI/RapidDoc · 小白说明书

## 🧐 这是什么
RapidAI 团队（RapidOCR / RapidLayout 同一拨人）出的"PDF → Markdown / JSON"管线。最大反共识点：**全 ONNX Runtime 跑，不带 PyTorch / CUDA 依赖**——在 Mac mini 上这意味着干净的 pip 安装、不卡 16GB 内存、CPU 也能跑得动。

## 💡 解决什么问题
- Mac mini 8GB / 不想装 PyTorch 那 5GB 依赖，但又要 MinerU 那级别的结构化输出
- 想要中文场景的开箱即用（RapidOCR 系列中文识别社区强口碑）
- 团队 / 个人对许可证敏感（Apache-2.0，比 MinerU 的 AGPL-3.0、marker 的 GPL-3.0 自由）

## 🎯 谁该用 / 谁别用
**适合你如果：** Mac mini 内存紧张；想跳过 PyTorch 装机；处理中英混杂 PDF / 票据 / 报告；想跑在 ARM Linux / 端侧
**别浪费时间如果：** 要榜单第一的纯英文学术论文精度（marker / olmocr 强）；项目 stars 太低会担心维护风险（这条目前只有 163 星）

## 🚀 三分钟上手
```bash
pip install rapid-doc        # 几十 MB 依赖，不拉 torch
# CLI
rapid_doc your.pdf -o out/
# Python API
python -c "from rapid_doc import RapidDoc; \
  print(RapidDoc()('your.pdf').to_markdown())"
```

首次跑会下 ONNX 模型（~200MB，比 marker / docling 都轻）。

## 🔑 关键文件 / 关键概念
- `rapid_doc/main.py` — 单入口，串起 layout / OCR / table / formula
- 子模型全是 RapidAI 兄弟项目：`RapidLayout` / `RapidOCR` / `RapidTable` / `RapidLatexOCR`
- 模型都是 ONNX，可以 CoreML 转换走 Apple Neural Engine（社区有方案）
- 输出可直接 md，或 JSON 结构化

## ⚠️ 踩坑提示
- 163 星算小项目，issue 响应快但生态文章少，遇到坑得自己读源码
- 表格 / 公式精度比 MinerU / docling 略弱，但比 pymupdf4llm 强很多
- 中文版式优势明显，英文学术论文（双栏 + 大量公式）建议先小样本测
- 默认模型偏中文，纯英文场景可换 RapidOCR 的英文模型

## 🤔 为什么这次推它给你
- 强命中"Mac mini 系统" → ONNX-only，无 PyTorch 依赖，安装包 / 模型都比 marker / docling 轻一档
- 命中"MinerU 差不多" → 同样是"复杂 PDF → 结构化 md"四件套（layout + OCR + 表格 + 公式）
- 命中"软偏好：反共识 / 轻量 / 中文友好" → 163 星的小众选手，但作者团队 RapidOCR 累计 25k+ stars，工程口碑稳
- trade-off：stars 低、英文论文精度不顶；适合"我想要 MinerU 但更轻"的人，不适合"我要 SOTA"

---
*由 /gitout 生成 · 2026-06-02 · intent: "寻找和 MinerU 差不多的开源项目，适合 Mac mini 系统的"*
