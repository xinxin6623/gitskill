---
type: repo
repo: ml-explore/mlx-swift-lm
domain: local-llm-runtime
status: active
discovered: 2026-05-25
last_reviewed: 2026-05-25
intent_matched: "Apple MLX 原生 Swift 跑 LLM"
signals:
  stars: 523
  last_commit: 2026-05-22
  language: Swift
  license: MIT
url: https://github.com/ml-explore/mlx-swift-lm
absorption:
  harvested: false
  used: false
  used_in: []
---

# mlx-swift-lm · 小白说明书

## 🧐 这是什么
Apple 官方 MLX 团队出的 **Swift 语言 LLM/VLM 库**，让你用 Swift 直接在 Mac/iPhone/iPad 上加载、推理、微调大模型，全程不离开 Apple 生态。

## 💡 解决什么问题
- "我在做 macOS / iOS app，想嵌入本地 LLM，不想跑 Python server" → 这是 Apple 官方答案
- "Python mlx-lm 能跑的模型，我能不能在 Swift app 里直接用" → 能，这个库就是 Python 版的 Swift 对位
- "想做 LoRA 微调但又不想离开 Xcode" → 内置 LoRA / 全量微调，量化模型也能调

## 🎯 谁该用 / 谁别用
**适合你如果：** 是 Apple 平台原生开发者；要把 LLM 嵌入 SwiftUI / AppKit app；想要 Apple 官方背书与持续维护；做 iOS 端侧推理
**别浪费时间如果：** 只想命令行跑模型（用 mlx-lm Python 版更顺）；想要现成的 chat UI（去看 mlx-swift-examples）；非 Apple 设备

## 🚀 三分钟上手
```swift
// Package.swift 加依赖
.package(url: "https://github.com/ml-explore/mlx-swift-lm", .upToNextMajor(from: "3.31.3")),
.package(url: "https://github.com/huggingface/swift-huggingface", from: "0.9.0"),

// Swift 里用 macro 加载 HF 模型
import MLXLLM
let model = try await MLXHuggingFace.load("mlx-community/Qwen3.5-7B-Instruct-4bit")
let output = try await model.generate(prompt: "你好")
```

## 🔑 关键文件 / 关键概念
- `MLXLLMCommon` — LLM/VLM 通用 API 层（先看这个）
- `MLXLLM` / `MLXVLM` / `MLXEmbedders` — LLM、视觉语言模型、embedding 三套模型实现
- `MLXHuggingFace` macro — Swift 里直接拉 HF 模型的语法糖
- 注：main 分支已升到 3.x，从 2.x 升要看 upgrade 文档

## ⚠️ 踩坑提示
- SwiftPM 命令行**编不出 Metal shader**，必须用 Xcode 构建（命令行 swift build 会运行时崩）
- 库本身不带下载器和 tokenizer，需要另选 `swift-huggingface` + `swift-transformers` 集成
- 文档链接经常 404，直接看 GitHub 源码里 `Documentation.docc` 更靠谱

## 🤔 为什么这次推它给你
**核心命中**：你 soft preference 写明"Swift 或 MLX 原生"，这是同时满足两者的 Apple 官方实现。
**反共识维度**：在 llama.cpp / Ollama 主导的 C++ 生态外，MLX 走的是"Metal + Swift 一等公民"路线，能耗与延迟在 M 系列上确实更优。
**Trade-off**：上手成本比 Ollama 高（要会 Swift、要会 Xcode），适合开发者；纯 CLI 用户更适合下面的 mio 或 llamafile。

---
*由 /gitout 生成 · 2026-05-25 · intent: "Mac/桌面本地跑 LLM 推理的轻量运行时"*
