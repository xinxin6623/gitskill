---
type: repo
repo: karlicoss/promnesia
domain: misc
status: active
decision: harvest
discovered: 2026-05-22
last_reviewed: 2026-05-22
theme: im-export
intent_matched: "浏览历史 + 上下文增强（个人数据反向赋能浏览体验）"
signals:
  stars: 1879
  last_commit: 2026-05-16
  language: Python
  license: MIT
url: https://github.com/karlicoss/promnesia
absorption:
  harvested: false
  used: false
  used_in: []
---

# promnesia · 小白说明书

## 🧐 这是什么

**"网页浏览的上下文外挂"浏览器扩展**（Chrome + Firefox + Firefox Android）。打开任何网页，它会告诉你：你以前来过吗？什么时候？怎么找到这个页面的？谁给你发的这个链接？你有没有在某个文件里引用过它？

HPI 同一作者 karlicoss 的姊妹项目，吃 HPI 的数据反向赋能浏览体验。1.9k 星，MIT。

## 💡 解决什么问题

浏览器的"历史记录"是个鸡肋功能：

- 只告诉你"哪天打开过"
- 不告诉你"为什么打开的"
- 不告诉你"在哪段对话里看过"
- 不告诉你"在你笔记的哪页提过"

promnesia **打通"网页 ↔ 你的所有数据源"**——某条 Twitter DM 提过这个链接？侧栏告诉你；你 Obsidian 某页引用过？侧栏告诉你。**网页变成你个人记忆的入口**。

## 🎯 谁该用 / 谁别用

**适合你如果：**
- 阅读量大，老觉得"这文章我以前看过但找不到"
- 重度 Obsidian / Org-mode 用户
- 已经用 HPI 或愿意建设个人数据基础设施

**别浪费时间如果：**
- 不愿装 HPI（promnesia 强依赖个人数据源）
- 嫌浏览器扩展打扰
- 浏览数据少（系统价值出不来）

## 🚀 三分钟上手

```bash
# 装扩展（Chrome / Firefox webstore）
open https://chrome.google.com/webstore/detail/promnesia/...

# 装后台索引服务
pip install promnesia
promnesia install
promnesia serve

# 配置数据源（依赖 HPI 配置好）
```

完整安装跟着 doc/GUIDE.org 走，第一次要一两小时。

## 🔑 关键文件 / 关键概念

- **三件套**：浏览器扩展 + 本地 indexer + HPI 数据
- **"visit"** — 系统的核心数据单位，比 visit-once 浏览历史强多了
- **child visits** — 同一个网址在不同上下文出现的全部"访问"
- **jump to source** — 不只显示来源，能直接跳到对应文件

## ⚠️ 踩坑提示

- 依赖 HPI，单独装意义不大
- 后台索引耗资源
- 文档是 org-mode 格式

## 🤔 为什么这次推它给你

**"个人数据为你服务"的最佳示范**。weixinjilu / WeChatMsg / imessage-exporter 都是"把数据导出来"，promnesia 是"**把导出来的数据反向赋能日常使用**"。你可以借鉴这个思路：导出聊天记录之后做个浏览器扩展，看任何链接告诉你"这个链接在你哪个聊天里出现过"。pattern 候选：`data-augmented-browsing`、`reverse-index-personal-mentions`。

---
*由 /gitout 生成 · 2026-05-22 · theme: 聊天记录 / 个人数据遗产化*
