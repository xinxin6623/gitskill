---
type: repo
repo: soniqo/speech-swift
domain: misc
status: active
decision: harvest
discovered: 2026-05-22
last_reviewed: 2026-05-22
theme: voice-2
intent_matched: "Apple Silicon 本地全栈语音（ASR/TTS/Streaming/Alignment）"
signals:
  stars: 749
  last_commit: 2026-05-22
  language: Swift
  license: Apache-2.0
url: https://github.com/soniqo/speech-swift
absorption:
  harvested: false
  used: false
  used_in: []
---

# Speech Swift · 小白说明书

## 🧐 这是什么

**专为 Apple Silicon 优化的语音全栈 Swift SDK**。MLX + CoreML 双引擎，覆盖：ASR（Qwen3-ASR 52 语言、Parakeet TDT、Omnilingual 1672 语言）、TTS（Qwen3-TTS、CosyVoice）、流式 dictation、forced alignment（词级时间戳）、speech-to-speech。全部本地跑，**不联网、不要 API key、数据不出设备**。

Product Hunt 推过，作者是 Soniqo 团队，HF 上叫 `aufklarer`。

## 💡 解决什么问题

你是 Mac 用户做语音项目最尴尬的事：

- whisper.cpp 又老又慢
- Python 生态在 macOS 上 GPU 加速不行
- 用云端 ASR 隐私 + 网络 + 钱包都难受

speech-swift **直接用 MLX（Apple 官方 ML 框架）+ CoreML（Neural Engine 直跑）**，在 M 系列芯片上性能拔群，而且是 Swift 原生 SDK，可以直接嵌进 macOS / iOS app。

## 🎯 谁该用 / 谁别用

**适合你如果：**
- Mac mini M4 / MacBook 用户（你正是）
- 在做或想做 macOS / iOS 上的语音 app
- 想做"完全本地、隐私优先"的语音工具

**别浪费时间如果：**
- 不是 Apple 平台
- 不愿意写 Swift（不过有 Python 包装的话另说）
- 要支持 Windows / Linux

## 🚀 三分钟上手

```bash
# 文档：https://soniqo.audio
# HuggingFace 模型：https://huggingface.co/aufklarer

# Swift 项目里加依赖
# Package.swift:
.package(url: "https://github.com/soniqo/speech-swift.git", from: "0.x.x")

# 然后
import SpeechSwift
let asr = try await Qwen3ASR.load()
let text = try await asr.transcribe(audioURL: url)
```

## 🔑 关键文件 / 关键概念

- **MLX** — Apple 出的 ML 框架，类 PyTorch 但原生支持 Metal
- **CoreML** — 直接跑在 Neural Engine 上，能耗最低
- **Omnilingual ASR** — Meta 出的 1672 语言模型，小语种神器
- **Parakeet-EOU** — 流式 dictation 专用，实时出 partial + 检测说完

## ⚠️ 踩坑提示

- 只跑 Apple Silicon，Intel Mac 不行
- 模型从 HF 下，国内首次需挂代理
- Swift Package Manager 不熟的话先 README 学一下

## 🤔 为什么这次推它给你

**你正好是 MacBook + Mac mini M4 主力用户**，这个项目是为你这种硬件量身定做的。**1672 语言的 Omnilingual ASR + Qwen3 全栈 + Parakeet 流式**——这三个能力组合本地跑，是其他平台羡慕不来的。直接 harvest，作为你 Mac 上做任何语音工具的首选 SDK。pattern 候选：`apple-silicon-local-speech-stack`。

---
*由 /gitout 生成 · 2026-05-22 · theme: 语音 pipeline 补充角度*
