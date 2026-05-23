---
type: repo
repo: elevenyellow/handcrafted-persona-engine
domain: misc
status: active
decision: harvest
discovered: 2026-05-22
last_reviewed: 2026-05-22
intent_matched: "可 DIY AI 对话机器人，Live2D + 口型 + 表情完整管线"
signals:
  stars: 1270
  last_commit: 2026-05-22
  language: C#
  license: unknown
url: https://github.com/elevenyellow/handcrafted-persona-engine
absorption:
  harvested: false
  used: false
  used_in: []
---

# Persona Engine · 小白说明书

## 🧐 这是什么

一个**专注 Live2D 角色的"语音 + 动画 + 人格"三件套引擎**，C# / .NET 9 写的。麦克风听你说话 → LLM 思考 → 实时 TTS → 同步驱动 Live2D 角色的口型和表情，整个链路打包成一个 Windows 双击就能跑的 exe。还能通过 Spout 推流到 OBS，直接可用作直播工具。

自带一个名叫 Aria 的角色模型，开箱即用，也可以换自己的 Live2D 模型（看仓库的 Live2D.md）。

## 💡 解决什么问题

你想做一个 Live2D 虚拟形象但被这些劝退过：

- 看 30 个教程才知道 lipsync 怎么对
- ASR / TTS / LLM 三个 API 怎么连
- 表情该跟哪些情绪绑

Persona Engine 直接给你一个**"装好就能用"的完整人设引擎**，配置文件改 `personality.txt` 就能换性格，模型换文件夹就能换角色。VBridger 口型方案 + 可选 Audio2Face 表情方案都内置。

## 🎯 谁该用 / 谁别用

**适合你如果：**
- 是 Windows 用户 + 有 NVIDIA GPU
- 想直接拿到一个能用的 Live2D 直播工具
- C# 不抵触，想读读 .NET 的语音管线实现

**别浪费时间如果：**
- 不是 Windows / 没 NVIDIA 显卡（**ASR/TTS/RVC 全靠 CUDA**）
- 想要 3D 角色（这个纯 Live2D）
- 不想动 C# 代码

## 🚀 三分钟上手

```bash
# 1. 下 zip
# https://github.com/fagenorn/handcrafted-persona-engine/releases

# 2. 解压（留 16GB 空间，模型会自动下）

# 3. 双击
PersonaEngine.exe
# 选一个 profile：try / stream / build
```

## 🔑 关键文件 / 关键概念

- `personality.txt` — 人格配置文件，决定角色性格
- **VBridger** — 用于 Live2D 口型同步的方案
- **Audio2Face** — NVIDIA 的表情驱动方案（高阶 profile 才启用）
- **Spout 输出** — 直接桥接到 OBS

## ⚠️ 踩坑提示

- **平台锁死 Windows + NVIDIA**，Mac/AMD/CPU 都不行
- 推荐配 fine-tuned LLM，标准 OpenAI 模型也能用但效果差
- License 标注不清晰（README 没明确商用条款），商用前自己查

## 🤔 为什么这次推它给你

**命中"开箱即用"这条 soft preference 最强**。你要的眼神/口型/表情 DIY 它都有，而且比 AIRI 更聚焦（只做 Live2D 不分散）。trade-off 是 Windows + NVIDIA 锁定 + C# 技术栈——如果你在 Mac 上开发就直接跳过看 AIRI，如果你有 Windows PC 想快速验证 Live2D 全链路，这个是最省事的样本。

---
*由 /gitout 生成 · 2026-05-22 · intent: "可 DIY 的 AI 对话机器人，眼神/口型/表情都可改"*
