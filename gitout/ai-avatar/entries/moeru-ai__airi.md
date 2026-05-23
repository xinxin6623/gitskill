---
type: repo
repo: moeru-ai/airi
domain: misc
status: active
decision: harvest
discovered: 2026-05-22
last_reviewed: 2026-05-22
intent_matched: "可 DIY AI 对话机器人，带 3D/2D 角色，眼神/口型/表情可定制"
signals:
  stars: 39452
  last_commit: 2026-05-22
  language: TypeScript
  license: MIT
url: https://github.com/moeru-ai/airi
absorption:
  harvested: false
  used: false
  used_in: []
---

# Project AIRI · 小白说明书

## 🧐 这是什么

一个**自托管的"AI 老婆/虚拟伙伴"容器**。本质上是想复刻 Neuro-sama（那个直播间里跟观众实时聊天的 AI 虚拟主播），让你能在自己电脑上养一个会动、会说、会玩游戏的 AI 角色。Web / macOS / Windows / Linux 全平台都能跑，TypeScript 写的，4 万星。

## 💡 解决什么问题

你想要一个 AI 角色：

- 看得见摸不着的不行，得有形象（2D Live2D / 3D VRM 都支持）
- 不能只是聊天，还要能实时语音对话、能玩 Minecraft 和 Factorio
- 不能锁死在某个 SaaS（你想自己改、自己挂自己的 LLM）

AIRI 把这些拼到一起，做成了**目前生态最完整、最活跃的开源方案**。

## 🎯 谁该用 / 谁别用

**适合你如果：**
- 想要一个能跑在自己机器上的"赛博伴侣"
- 喜欢 TypeScript / Vue 生态，愿意改前端
- 想看"实时语音 + 角色驱动"的最佳工程实践

**别浪费时间如果：**
- 只想做一个纯文字聊天框
- 极度看重轻量（这是个大型 monorepo，依赖一堆）
- 拒绝二次元向的产品定位

## 🚀 三分钟上手

```bash
# 最快路径：直接下安装包
# macOS: https://github.com/moeru-ai/airi/releases (下 .dmg)
# Windows: 下 setup.exe

# 或网页版直接体验
open https://airi.moeru.ai

# 想自己改源码
git clone https://github.com/moeru-ai/airi.git
cd airi && pnpm install && pnpm dev
```

## 🔑 关键文件 / 关键概念

- **moeru-ai/airi monorepo** — 多 package 组织，前端 + Tauri 桌面壳 + 角色驱动各自独立
- **Live2D / VRM 双轨支持** — 想要 2D 用 Live2D，想要 3D 直接用 VRM 标准格式
- **Neuro-sama 致敬** — 设计目标明确，整个架构围绕"实时直播级互动"展开

## ⚠️ 踩坑提示

- 仓库巨大，第一次 clone 慢，国内建议挂代理
- pnpm 不是 npm，先 `npm i -g pnpm`
- 默认 LLM/TTS 走云端 API，本地化要自己改配置

## 🤔 为什么这次推它给你

**命中意图最强的一个。** 你要"人物 + 动画 + 眼神 + 口型 + 表情都能 DIY"，AIRI 是少数同时覆盖这五项的项目（眼神追踪、口型 lipsync、表情切换、Live2D/VRM 双格式都在）。trade-off 是工程复杂度高——不是几百行就能读完的小项目，但**结构清晰、社区活跃、可以渐进地抄局部**。强烈建议作为 deepdive 的主样本。

---
*由 /gitout 生成 · 2026-05-22 · intent: "可 DIY 的 AI 对话机器人，眼神/口型/表情都可改"*
