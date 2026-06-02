---
type: repo
repo: allenai/olmocr
domain: document-parsing
status: active
discovered: 2026-06-02
last_reviewed: 2026-06-02
intent_matched: "MinerU 同类：VLM-based PDF→md，Apple Silicon 可跑（吞吐受限）"
signals:
  stars: 17366
  last_commit: 2026-03-25
  language: Python
  license: Apache-2.0
url: https://github.com/allenai/olmocr
absorption:
  harvested: false
  used: false
  used_in: []
---

# allenai/olmocr · 小白说明书

## 🧐 这是什么
AllenAI 开源的"用视觉语言模型(VLM)直接读 PDF 一页 → 输出干净 md"的工具包。和 MinerU / marker "多个小模型流水线"的思路反着来：一个 7B 的 olmOCR-7B 模型端到端搞定 layout + OCR + 公式 + 表格。Apache-2.0 许可证。

## 💡 解决什么问题
- 想要"端到端 VLM"路线，少调一堆 layout / OCR / table 子模型
- 处理大批量学术 / arXiv 论文，需要可复现的训练级输出
- 希望许可证宽松能商用（Apache-2.0，比 MinerU 的 AGPL-3.0 友好）

## 🎯 谁该用 / 谁别用
**适合你如果：** 主要处理英文科研论文；接受拉一个 7B 模型权重（~14GB）；想跟进 VLM 文档解析最前沿
**别浪费时间如果：** Mac mini 8GB（吃不下 7B + KV cache）；要求毫秒级响应（VLM 推理是慢路径）；处理大量中文 / 复杂表格

## 🚀 三分钟上手
```bash
# 推荐用 uv 装，依赖较重
uv pip install olmocr
# 单文件
python -m olmocr.pipeline ./workdir --pdfs your.pdf
# 输出在 ./workdir/results/
```

Mac mini 跑要走 vLLM 的 MPS 后端或 llama.cpp 转 GGUF 版本（社区已有），原生 PyTorch + MPS 也行但慢。

## 🔑 关键文件 / 关键概念
- `olmocr/pipeline.py` — 主入口，单 / 批量都走它
- `olmocr/prompts/` — 提示词模板（很值得读，是这套方案的灵魂）
- 模型默认从 HF 拉 `allenai/olmOCR-7B-0225`，~14GB
- 同时提供"olmOCR-bench"评测集，可拿你自己的 PDF 对比 Marker / Docling / MinerU

## ⚠️ 踩坑提示
- 7B VLM 在 Mac mini 16GB 上每页约 5-15 秒，单机不是吞吐选手
- 默认 prompt 优化过英文学术论文，中文 / 工业票据要自己改 prompt
- 想跑 GGUF 量化版找社区 fork（仓库本身只发原始权重）

## 🤔 为什么这次推它给你
- 命中"MinerU 差不多" → 同领域、同梯队（17k stars），但走 VLM 端到端而非流水线
- 命中"Mac mini" → 能跑（PyTorch + MPS / GGUF + Metal），但需要 16GB 起步
- 软偏好命中：Apache-2.0 商用无压力 + 评测集自带，方便对比 MinerU
- trade-off：硬件门槛比 marker / docling 高；中文不强；吞吐慢

---
*由 /gitout 生成 · 2026-06-02 · intent: "寻找和 MinerU 差不多的开源项目，适合 Mac mini 系统的"*
