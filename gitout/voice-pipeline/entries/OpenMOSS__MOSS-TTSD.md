---
type: repo
repo: OpenMOSS/MOSS-TTSD
domain: misc
status: active
decision: watch
discovered: 2026-05-22
last_reviewed: 2026-05-22
theme: voice-2
intent_matched: "多说话人对话 TTS（播客/双人对话/相声）"
signals:
  stars: 1326
  last_commit: 2026-05-22
  language: Python
  license: Apache-2.0
url: https://github.com/OpenMOSS/MOSS-TTSD
absorption:
  harvested: false
  used: false
  used_in: []
---

# MOSS-TTSD · 小白说明书

## 🧐 这是什么

MOSS-TTS Family 里**专门做"多人对话长篇"的子模型**。常规 TTS 是"文本一句话 → 一段音频"，MOSS-TTSD 是"**剧本 → 整段对话**"：你给一个带说话人标记的脚本，它合成出多人切换、有情绪起伏、长达几分钟的连续对话。播客、配音、有声书、相声小品都是它的目标场景。

支持零样本声音克隆（短样本就能复刻一个角色的音色）。

## 💡 解决什么问题

你想用 AI 做"内容生产"而不是"客服回复"：

- 想把博客文章自动转成双人播客
- 给小说做有声书但每个角色都要不同的声音
- 想做"AI 相声"或多人辩论 demo

普通 TTS 拼出来生硬不连贯，MOSS-TTSD **把"剧本到对话"当一个整体生成任务**，转场和情绪连续性是设计目标。

## 🎯 谁该用 / 谁别用

**适合你如果：**
- 做内容生产（播客 / 有声书 / 配音）
- 需要多说话人切换且要自然
- 接受 Apache 协议

**别浪费时间如果：**
- 只做实时单人对话（用 MOSS-TTS 单人版更轻）
- 没 GPU 跑大模型
- 需要 sub-200ms 实时（这模型偏离线生成）

## 🚀 三分钟上手

```bash
# HuggingFace 试玩入口
open https://huggingface.co/spaces/OpenMOSS-Team/MOSS-TTSD

# 本地跑
git clone https://github.com/OpenMOSS/MOSS-TTSD.git
cd MOSS-TTSD
pip install -r requirements.txt
# 模型从 https://huggingface.co/OpenMOSS-Team/MOSS-TTSD-v1.0 拉
```

## 🔑 关键文件 / 关键概念

- **script-to-conversation** — 设计哲学，对应论文 arXiv:2603.19739
- **零样本声音克隆** — 短音频样本就能复刻角色音色
- **长篇连续生成** — 数分钟级别的对话不掉链子
- **HuggingFace Space** — 不下模型也能先玩

## ⚠️ 踩坑提示

- 模型大，GPU 显存要求高
- 中英混合场景效果不一定与单语持平
- 这是 v1.0，论文级稳定性但还在迭代

## 🤔 为什么这次推它给你

**voice pipeline 不止是"实时对话"，还有"内容生产"。** 你做 OpenClaw / weixinjilu 这种工具，未来可能要把"聊天记录"转成播客、把"知识库"转成有声笔记，MOSS-TTSD 就是这个场景的解。pattern 候选：`script-to-multi-speaker-conversation`。

---
*由 /gitout 生成 · 2026-05-22 · theme: 语音 pipeline 补充角度*
