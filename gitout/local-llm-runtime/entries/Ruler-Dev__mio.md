---
type: repo
repo: Ruler-Dev/mio
domain: local-llm-runtime
status: active
discovered: 2026-05-25
last_reviewed: 2026-05-25
intent_matched: "性能能耗优化的 MLX 推理 server"
signals:
  stars: 4
  last_commit: 2026-04-21
  language: Python
  license: unknown
url: https://github.com/Ruler-Dev/mio
absorption:
  harvested: false
  used: false
  used_in: []
---

# mio · 小白说明书

## 🧐 这是什么
一个**把三项推理性能 trick 打包默认启用**的 Apple Silicon 本地推理引擎：DFlash 投机解码 + PolarQuant 4-bit KV-cache 压缩 + Caveman 提示词压缩。再叠一层 Claude-style 聊天 UI 和编码 agent。

## 💡 解决什么问题
- "MLX 跑 35B 模型每秒就那几个 token，性能优化论文一堆但没人集成" → mio 把 DFlash（~4.1× 加速）和 PolarQuant（KV cache 缩 3.8×）默认开起来
- "本地跑大模型最大的瓶颈是 KV cache 吃显存" → PolarQuant 在 0 速度损失下把 cache 砍掉 3/4
- "想要 Claude.ai 那种聊天体验但跑在自己 Mac 上" → 内置 Mio UI，有 artifacts / skills / personas / 语音

## 🎯 谁该用 / 谁别用
**适合你如果：** 有 M3 Max / M4 Pro 想压榨极限性能；关心 KV cache 占用；想试投机解码这种"新鲜玩具"；要在 64GB+ 内存的 Mac 跑 30B+ 模型
**别浪费时间如果：** 只有 16GB 内存（默认模型是 35B MoE）；想要稳定生产环境（passion project 维护强度有限）；不接受 OpenAI 兼容 API 之外的玩法

## 🚀 三分钟上手
```bash
git clone https://github.com/Ruler-Dev/mio.git
cd mio
pip install -e .          # 一键装好整套
mio serve                 # 起 OpenAI 兼容 API server
mio chat                  # 或直接进 CLI 聊天
```

## 🔑 关键文件 / 关键概念
- `MioEngine` — 推理核心，包 DFlash + PolarQuant
- **DFlash** — 投机解码，用小模型先猜 token 再让大模型验证
- **PolarQuant** — KV cache 用极坐标 4-bit 量化，矩阵乘还更快
- **Caveman mode** — 系统提示词层面压缩，让模型少输出 15-75% token
- 默认模型：Qwen 3.5 35B-A3B MoE Q4，128K context

## ⚠️ 踩坑提示
- 默认模型 35B MoE，至少要 32GB 统一内存才跑得动，建议 64GB
- license 不明，注意商用风险
- 是 passion project（4 star），作者愿意接 PR 但响应不保证
- 自带的 Mio UI 是 Claude-style，不是 ChatGPT-style，习惯一下

## 🤔 为什么这次推它给你
**核心命中**：你 anti-pattern 明说"不要 Ollama 本体"，mio 是同生态位的反共识替代——而且把研究级性能优化默认开起来，这正是 Ollama 不做的事。
**反共识维度**：4 star 项目，但 README 技术含量极高（DFlash + PolarQuant 都是 2025 年新论文），适合喜欢"提前几个月体验未来"的人。
**Trade-off**：维护稀薄、模型默认偏大、license 不清——是个赌注，但你的 Mac 配置如果够，赌赢了收益巨大。

---
*由 /gitout 生成 · 2026-05-25 · intent: "Mac/桌面本地跑 LLM 推理的轻量运行时"*
