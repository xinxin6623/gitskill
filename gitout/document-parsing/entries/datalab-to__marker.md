---
type: repo
repo: datalab-to/marker
domain: document-parsing
status: active
discovered: 2026-06-02
last_reviewed: 2026-06-02
intent_matched: "MinerU 同类：PDF → 结构化 Markdown，Apple Silicon 可跑"
signals:
  stars: 35640
  last_commit: 2026-05-05
  language: Python
  license: GPL-3.0
url: https://github.com/datalab-to/marker
absorption:
  harvested: false
  used: false
  used_in: []
---

# datalab-to/marker · 小白说明书

## 🧐 这是什么
社区目前公认与 MinerU 最对标的"PDF → Markdown / JSON"转换器。底层是一套针对文档微调过的小模型组合（layout + OCR + 表格 + 公式），跑完一篇论文就能得到干净结构化的 md。

## 💡 解决什么问题
- 学术论文 / 财报 / 标书 → 喂给 RAG 或 LLM 前需要先转 md，普通 pdf2txt 把表格、公式、双栏全搅烂
- MinerU 模型权重大 + 中文社区为主，想换一个"英文文档优势更强、社区活跃度更高"的国际同行
- 想要批量处理几千份 PDF，要求每分钟几十页的吞吐

## 🎯 谁该用 / 谁别用
**适合你如果：** 主要处理英文学术 / 技术 PDF；想拿全网评测里第一梯队的准确率；Mac mini 上跑过 PyTorch + MPS 没障碍
**别浪费时间如果：** 处理大量中文古籍 / 扫描繁体（MinerU 更稳）；公司不允许 GPL-3.0 传染许可证；只是偶尔转一两份（用 pymupdf4llm 就够）

## 🚀 三分钟上手
```bash
pip install marker-pdf
# Mac mini Apple Silicon：自动走 MPS
marker_single your.pdf --output_dir out/
# 批量
marker /path/to/pdfs --workers 4 --output_dir out/
```

## 🔑 关键文件 / 关键概念
- `marker/converters/pdf.py` — 主 pipeline，看它就能改造
- `marker/builders/` — layout / text / OCR / table builders 各自独立，便于替换
- 默认走 surya（同作者的 layout/OCR 模型套件），首次跑会自动下权重 ~3GB
- `--use_llm` 开关：可挂 Claude / OpenAI 给低置信度区域复核

## ⚠️ 踩坑提示
- **GPL-3.0**：商用闭源产品要二想。研究 / 内部工具 / 个人不受影响
- Mac mini 8GB 跑大 PDF 会 OOM，分块跑或加 swap；16GB 起步舒服很多
- 首次跑会从 HuggingFace 拉权重，国内网络备好梯子或镜像
- 双栏 / 复杂图文混排的精度仍弱于 MinerU，论文场景 80 分但票据 / 扫描合同别期待太高

## 🤔 为什么这次推它给你
- 命中"MinerU 差不多" → marker 是社区评测里跟 MinerU 长期咬住前两名的同档位
- 命中"Mac mini 系统" → Python + PyTorch + MPS，无 CUDA 依赖，作者明确支持 Apple Silicon
- trade-off：许可证比 MinerU 严格（GPL-3.0 vs MinerU 的 AGPL-3.0，半斤八两）；中文表现略弱

---
*由 /gitout 生成 · 2026-06-02 · intent: "寻找和 MinerU 差不多的开源项目，适合 Mac mini 系统的"*
