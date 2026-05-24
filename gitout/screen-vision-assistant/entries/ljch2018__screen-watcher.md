---
type: repo
repo: ljch2018/screen-watcher
domain: screen-vision-assistant
status: active
discovered: 2026-05-25
last_reviewed: 2026-05-25
intent_matched: "本地 VLM 后台监控屏幕做语义记忆（Rewind 平替）"
signals:
  stars: 0
  last_commit: 2026-03-30
  language: Python
  license: mit
url: https://github.com/ljch2018/screen-watcher
absorption:
  harvested: false
  used: false
  used_in: []
---

# Screen Watcher · 小白说明书

## 🧐 这是什么

Mac 上的 **本地 VLM 屏幕记忆**——后台默默盯着你当前的前台窗口，用本地视觉大模型（走 Ollama）理解你看到的内容，存成可搜索的时间线。**完全离线，截图过完即焚**。

## 💡 解决什么问题

- 想要 Rewind.ai 那种"昨天在某文章里读到啥"，但不接受订阅 + 不接受云上传
- 想给自己建一份「我今天到底干了啥」的日志，不靠手动记录
- 想让 AI 知道你的工作上下文，但屏幕内容是隐私底线
- 想做下游：把这条时间线接到自己的 RAG / Agent / 日报里

## 🎯 谁该用 / 谁别用

**适合你如果：**
- 隐私洁癖、坚决不让屏幕内容出本机
- 已经在用 Ollama，对本地 VLM (qwen2.5-vl / llava 之类) 有基本认知
- 接受"截图 → VLM 推理"对 CPU/GPU 的持续开销

**别浪费时间如果：**
- 想要 polished GUI、像 Rewind 那样开箱即用
- M1 8G 内存——本地 VLM 跑不动
- 只想偶尔 OCR 一下，不需要后台常驻

## 🚀 三分钟上手

```bash
# 前置：装好 Ollama 并拉一个 VLM
brew install ollama
ollama pull qwen2.5vl:7b

# 装本体
git clone https://github.com/ljch2018/screen-watcher && cd screen-watcher
# 跟 README 里的 launchd 脚本启动 daemon
```

数据存在 `~/screen-watcher/` 的 JSONL 文件，可以 `grep` 可以删除。

## 🔑 关键文件 / 关键概念

- Ollama (`localhost:11434`) — 唯一外部依赖，唯一网络出口
- MD5 image hash 去重 — 屏幕没变就不重复推理
- 文本相似度去重 — 推理出的内容重复也跳过
- launchd daemon — 跟系统一起起来
- compact & merge — 每日按 app/window 合并去重，控制磁盘
- Work Insights skill — 配套的 OpenClaw skill，能读时间线主动给建议

## ⚠️ 踩坑提示

- 0 stars，作者个人项目，bug 风险自担
- 截图过 VLM 后**立刻删除**，但 JSONL 文本会一直存，敏感内容（密码框）也会被记录——记得加 noise filter 黑名单
- Ollama 模型本身占 5-10GB 磁盘
- 老款 Intel Mac 没 GPU，推理慢到没法用

## 🤔 为什么这次推它给你

**完美命中 anti-pattern 里的"不要 Rewind/Heptabase 类商业 SaaS"**——它就是开源、本地、能让你不用付订阅的"屏幕记忆"路线。同时硬约束"Mac + 开源 + 本地"全中。**trade-off：**0 stars 是真冷门，活跃度看起来还行（2026-03 更新）但作者一个人；GUI 几乎没有，你要接受命令行 + JSONL 的极客形态。这条是给你"如果未来想自己做屏幕记忆"留的种子。

---
*由 /gitout 生成 · 2026-05-25 · intent: "Mac 桌面屏幕 OCR / 截图理解 / 视觉助手"*
