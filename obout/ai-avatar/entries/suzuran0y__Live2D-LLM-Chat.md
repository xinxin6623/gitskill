---
type: repo
repo: suzuran0y/Live2D-LLM-Chat
domain: misc
status: active
decision: harvest
discovered: 2026-05-22
last_reviewed: 2026-05-22
intent_matched: "可 DIY AI 对话机器人，眼神追踪 + 口型同步实现可读"
signals:
  stars: 39
  last_commit: 2026-05-21
  language: Python
  license: Apache-2.0
url: https://github.com/suzuran0y/Live2D-LLM-Chat
absorption:
  harvested: false
  used: false
  used_in: []
---

# Live2D-LLM-Chat · 小白说明书

## 🧐 这是什么

一个**最适合"读代码学原理"的 Live2D + LLM 小项目**。Python 写的，把 ASR (SenseVoice) + LLM (GPT/DeepSeek) + TTS (CosyVoice) + Live2D 这一条链路用最直接的方式串起来。规模小（不到 50 stars 但活跃），适合作为入门样本。

最有意思的点：**作者自己实现了眼神追踪 + 眨眼 + 口型同步逻辑**，即使你的 Live2D 模型本身没有这些内置动作，也能跑起来。

## 💡 解决什么问题

你想搞懂 Live2D 角色"嘴是怎么动的、眼是怎么看你的"，但：

- AIRI / Kokoro 那种大项目代码读不完
- Persona Engine 是 C# 你不熟
- 商业方案是黑盒

这个项目几个 .py 文件就讲清了原理：**从 TTS 输出实时分析音量 → 算出嘴张多大 → 驱动 Live2D 嘴部参数**。眼神追踪是单独一段算法。

## 🎯 谁该用 / 谁别用

**适合你如果：**
- 想读懂"虚拟形象怎么对口型"的最小实现
- 是 Python 用户
- 接受 Windows 或 Linux（macOS 没明确支持）

**别浪费时间如果：**
- 想要一个能直接用的产品（这是学习级别）
- 没有 conda 经验（TTS 依赖 conda 环境）
- 要 3D 角色（纯 Live2D）

## 🚀 三分钟上手

```bash
git clone https://github.com/suzuran0y/Live2D-LLM-Chat.git
cd Live2D-LLM-Chat

python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
pip install funasr

# 还需要装 CosyVoice TTS 的 conda 环境，见 README §3.4
```

## 🔑 关键文件 / 关键概念

- **live2d-py + OpenGL** — Python 直接驱动 Live2D 模型的库
- **音量 → 嘴型参数映射** — 项目的核心 trick，代码里能直接读
- **SenseVoice ASR** — 阿里出的多语言 ASR，做中英混说效果好
- **每 5 轮对话生成 summary** — 简单粗暴但有效的长期记忆方案

## ⚠️ 踩坑提示

- TTS 必须 conda 环境，不能纯 pip
- ASR 模型从 ModelScope 下，国内速度快但国外用户要挂梯子
- 角色模型要自己准备，README 没附

## 🤔 为什么这次推它给你

**命中"代码可读、能改"这条 soft preference 最强**。你要 DIY，但 AIRI / Kokoro 那种几万行代码读起来劝退——这个项目就是"想看清原理"的最佳样本。**口型同步那段代码可以直接抄进任何 Live2D 项目**，是个高复用的 pattern 候选：`audio-volume-to-mouth-parameter`。trade-off 是工程化程度低，不适合做产品基础。

---
*由 /gitout 生成 · 2026-05-22 · intent: "可 DIY 的 AI 对话机器人，眼神/口型/表情都可改"*
