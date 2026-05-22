---
type: repo
repo: Liquid4All/liquid-audio
domain: misc
status: active
decision: watch
discovered: 2026-05-22
last_reviewed: 2026-05-22
theme: voice-2
intent_matched: "端到端 speech-to-speech 模型（1.5B 小模型实时对话）"
signals:
  stars: 513
  last_commit: 2026-05-22
  language: Python
  license: Other
url: https://github.com/Liquid4All/liquid-audio
absorption:
  harvested: false
  used: false
  used_in: []
---

# Liquid Audio (LFM2.5-Audio) · 小白说明书

## 🧐 这是什么

Liquid AI 出的**端到端 speech-to-speech 基础模型**。和"ASR → LLM → TTS 三段拼起来"不同，这是**一个模型直接吃声音吐声音**——把"听-想-说"做成一次性 token 流。1.5B 参数，专为低延迟设计，最新 LFM2.5 版本 ASR 更强、TTS 音质提升。

提供两种模式：**interleaved**（边听边说，最适合实时对话）、**sequential**（适合 ASR/TTS 单独任务）。

## 💡 解决什么问题

传统语音 pipeline 的硬伤：

- ASR + LLM + TTS 三段串起来，延迟叠加难压
- 中间 token 化会丢"情感"信号（语调、停顿、犹豫）
- 同一个对话三个模型，状态难一致

speech-to-speech 模型直接**把音频 token 当 LLM 内部 token 流跑**，类似 OpenAI Realtime / Moshi 的思路。Liquid 这个的卖点是**小模型 + 端侧友好**，1.5B 可以跑在消费级 GPU 甚至 M 系列 Mac。

## 🎯 谁该用 / 谁别用

**适合你如果：**
- 想看下一代语音架构（不再是三段拼接）
- 关心端侧 / 边缘部署
- 想对比 Moshi / GPT-4o-audio 等同类设计

**别浪费时间如果：**
- 只想用最稳的方案做产品（这是新架构，生态不成熟）
- 需要中文优先（README 没看到强中文支持）
- License 必须 MIT/Apache（这个是 Other）

## 🚀 三分钟上手

```bash
pip install liquid-audio
pip install "liquid-audio[demo]"      # 加 demo deps
pip install flash-attn --no-build-isolation  # 可选加速

# 启动 Gradio demo
liquid-audio-demo
# → http://localhost:7860
```

## 🔑 关键文件 / 关键概念

- **LFM2.5-Audio-1.5B** — 当前最强版本，自家 LFM2.5 backbone
- **Mimi codebooks** — 8 个 codebook 表示一个音频 token，参考 Moshi 设计
- **interleaved vs sequential** — 两种生成模式
- **ChatState** — 多轮多模态对话的状态管理 helper

## ⚠️ 踩坑提示

- License 是 "Other"，商用前必须看
- flash-attn 编译复杂，可以跳过用 torch SDPA
- 端到端模型可控性差，传统 prompt 工程套路不一定有用

## 🤔 为什么这次推它给你

**voice pipeline 的范式革命样本**。你做 voice 项目如果只看"ASR + LLM + TTS"会错过未来——s2s 模型可能 1-2 年内就重塑整个行业。Liquid Audio 是少数**端到端 + 小尺寸 + 开源**三件齐的样本，看一眼，知道天花板在哪。先 watch，等 v2 或国产同类（千问 / MiniCPM 已经在做）成熟。pattern 候选：`end-to-end-speech-to-speech`。

---
*由 /gitout 生成 · 2026-05-22 · theme: 语音 pipeline 补充角度*
