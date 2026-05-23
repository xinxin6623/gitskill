---
type: repo
repo: whoiswennie/AI-Vtuber
domain: misc
status: watch
discovered: 2026-05-22
last_reviewed: 2026-05-22
intent_matched: "可 DIY AI 对话机器人，全栈虚拟主播方案（含意图识别 + 长短期记忆）"
signals:
  stars: 445
  last_commit: 2026-05-17
  language: Python
  license: MIT
url: https://github.com/whoiswennie/AI-Vtuber
absorption:
  harvested: false
  used: false
  used_in: []
---

# whoiswennie/AI-Vtuber · 小白说明书

## 🧐 这是什么

一个**对接 B 站直播间的高自由度 AI 虚拟主播全家桶**。Python 写的，整合了一堆"成熟开源组件"（so-vits-svc 语音转换 + GPT-SoVITS 语音合成 + UVR5 人声分离 + faster-whisper ASR + Stable Diffusion 画图 + EasyAIVTuber 数字人驱动），加上自己的意图识别、知识图谱、长短期记忆，做出一个能在直播间跟观众对话、唱歌、画画的 AI 主播。

带 Streamlit 客户端做可视化管理。

## 💡 解决什么问题

你想要的不只是"会动的角色"，而是"能直播营业的 AI 主播"：

- 观众弹幕来了要识别意图（聊天 / 点歌 / 让画图 / 搜索）
- 要有"上次说过什么"的记忆
- 要支持随时换人设、换声音
- 整合各种 AI 工具但不想自己 glue

这个项目把这些**用一个客户端串起来给你**。

## 🎯 谁该用 / 谁别用

**适合你如果：**
- 真的要做 B 站 AI 直播
- 有显卡能跑 SD（README 说能跑 SD 就能跑这个）
- 喜欢"整合大量第三方项目"的工程风格

**别浪费时间如果：**
- 只想要桌面伴侣不做直播（用 AIRI / Kokoro）
- 嫌完整部署 20+ GB 太重
- 不用 B 站生态（项目深度耦合）

## 🚀 三分钟上手

```bash
# 推荐用 release 整合包，普通安装太复杂
# 见 README 中的夸克网盘链接

# 源码起步
git clone https://github.com/whoiswennie/AI-Vtuber.git
cd AI-Vtuber

# 准备预训练模型放到指定目录（见 README）
# 然后
condaenv.bat  # 主环境搭建
start.bat     # 启动客户端
```

## 🔑 关键文件 / 关键概念

- **意图识别 → 路由** — 弹幕分流到聊天/搜索/画图/唱歌四条路径
- **图数据库 + 向量库混合知识库** — 比单纯 RAG 更结构化
- **多人设模板热切换** — 直播中实时换"性格"
- **so-vits-svc 整套训练-推理** — 语音转换方案

## ⚠️ 踩坑提示

- **完整部署 20+ GB**，作者自己承认占地大
- 强耦合 B 站直播 API
- README 主要是中文，国际化弱
- 作者大四生，v2 更新承认会慢

## 🤔 为什么这次推它给你

**命中"全栈 AI 角色应用"和"意图识别 + 记忆"这两条 soft preference**。如果你的"DIY 对话机器人"其实想做的是 AI 主播或直播玩具，这就是最完整的参考。**意图识别 + 知识图谱知识库的组合值得抄**，可作为 pattern 候选：`intent-routing-for-livestream-bot`。trade-off 是太重 + B 站耦合——纯学习的话只看意图识别和记忆模块即可。

---
*由 /gitout 生成 · 2026-05-22 · intent: "可 DIY 的 AI 对话机器人，眼神/口型/表情都可改"*
