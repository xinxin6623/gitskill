---
type: repo
repo: OpenMOSS/MOSS-TTS
domain: misc
status: active
decision: harvest
discovered: 2026-05-22
last_reviewed: 2026-05-22
theme: voice-2
intent_matched: "高质量开源 TTS（中文 + 多说话人 + 流式）"
signals:
  stars: 1854
  last_commit: 2026-05-22
  language: Python
  license: Apache-2.0
url: https://github.com/OpenMOSS/MOSS-TTS
absorption:
  harvested: true
  harvested_into: function-to-realtime-stream
  used: false
  used_in: []
---

# MOSS-TTS Family · 小白说明书

## 🧐 这是什么

复旦 MOSS 团队 + MOSI.AI 出的**开源 TTS 模型家族**。覆盖：高保真单人 TTS、多人对话 TTS、声音/角色设计、环境音效、实时流式 TTS。Apache 协议，HuggingFace + ModelScope 双发布。已经被 mlx-audio 集成，Mac M 系列也能跑。

中文圈做开源 TTS 第一梯队（GPT-SoVITS、CosyVoice、MOSS-TTS 三大家）。

## 💡 解决什么问题

你做中文语音应用最头疼的：

- 国外 TTS（ElevenLabs / Cartesia）对中文一般，按字符收费
- 国内闭源（讯飞 / 阿里）要 API key、要审核、商用条款复杂
- GPT-SoVITS 效果好但模型小，复杂场景翻车

MOSS-TTS 给你**学术级表现 + 工业级稳定**的中文 TTS，还把 TTS 拆分成"基础语音"、"对话语音"、"音效"等子模型，按需用。

## 🎯 谁该用 / 谁别用

**适合你如果：**
- 做中文为主的语音应用
- 想要可商用的开源 TTS（Apache 2.0）
- 用 Mac M 系列想本地跑（mlx-audio 已支持）

**别浪费时间如果：**
- 只做英文，那 Kokoro 或 Piper 更轻
- 没 GPU 又不接受云端
- 要 sub-100ms 延迟（这是质量优先非极速优先）

## 🚀 三分钟上手

```bash
git clone https://github.com/OpenMOSS/MOSS-TTS.git
cd MOSS-TTS

# 走 HuggingFace 模型
pip install -r requirements.txt
# 模型从 https://huggingface.co/collections/OpenMOSS-Team/moss-tts 拉

# Mac 用户走 mlx-audio
pip install mlx-audio
```

## 🔑 关键文件 / 关键概念

- **MOSS-TTS Family** — 母仓库索引，子模型各自有 repo
- **MOSS-TTSD** — 对话场景特化（多说话人长篇）
- **MOSS-Audio-Tokenizer** — 自家音频 tokenizer
- **流式 TTS** — 关键能力，配合实时对话不卡

## ⚠️ 踩坑提示

- 模型体积不小，初次下载耐心
- 多个相关 repo（MOSS-TTS / MOSS-TTSD / MOSS-Audio-Tokenizer），别拿混
- 2026.4 在收集 v2 需求，v1 文档可能近期变动

## 🤔 为什么这次推它给你

**上轮搜索 voice pipeline 都偏英文生态，这次补一个中文 TTS 主力**。你做 openclaw-voice-bot 或任何中文语音应用，TTS 选型绕不开这家。**Apache 协议 + 学术背景 + 商业可用 + Mac 本地能跑**四件都齐。直接 harvest。

---
*由 /gitout 生成 · 2026-05-22 · theme: 语音 pipeline 补充角度*
