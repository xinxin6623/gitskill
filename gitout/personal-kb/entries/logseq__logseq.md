---
type: repo
repo: logseq/logseq
domain: misc
status: active
decision: harvest
discovered: 2026-05-22
last_reviewed: 2026-05-22
theme: personal-kb
intent_matched: "outliner + 块引用知识库（隐私优先 + 本地优先）"
signals:
  stars: 43019
  last_commit: 2026-05-22
  language: Clojure
  license: AGPL-3.0
url: https://github.com/logseq/logseq
absorption:
  harvested: false
  used: false
  used_in: []
---

# Logseq · 小白说明书

## 🧐 这是什么

**Roam Research 的开源对标**，43k 星。把"块（block）"当成基本单位（不是页面），每个段落都是可被引用的实体——你写笔记其实是在做"大纲 + 双向链接 + 块嵌入"三合一。隐私优先：所有数据**本地 markdown 文件**，可以 Git 同步、可以接 iCloud / Syncthing。

Clojure 写的（也是它独特个性的一部分），AGPL 协议。

## 💡 解决什么问题

你写笔记最痛的两件事：

- "我想引用之前写过的某一段，但只能引用整篇笔记"
- "笔记越多越乱，找不到东西"

Logseq 的解法：**outliner（大纲）让所有内容天然分块、块引用 `((block-id))` 让你随时插入任何段落、双向链接展示反向关系**。配合每日笔记（日报）模式，写久了笔记会自然形成网状结构。

## 🎯 谁该用 / 谁别用

**适合你如果：**
- Roam Research 思路认同但不想给 SaaS 钱
- 习惯"先记日报，后整理"
- 看重数据隐私，所有笔记本地 md

**别浪费时间如果：**
- 不接受 outliner 范式（喜欢长篇散文）
- AGPL 协议你不能接受
- 嫌 Electron 客户端重

## 🚀 三分钟上手

```bash
# Mac
brew install --cask logseq

# 或下安装包
open https://github.com/logseq/logseq/releases/latest

# 启动后选一个文件夹做 graph，里面就是你的 md 笔记
```

## 🔑 关键文件 / 关键概念

- **block** — 基本单位，每个 bullet 都有独立 ID
- **`[[ ]]` 双向链接** — 像 Roam 那套
- **`(( ))` 块引用** — 内嵌某个具体段落
- **journals/** — 每日笔记，主要工作面
- **pages/** — 主题页面，自动汇总反向链接

## ⚠️ 踩坑提示

- AGPL 协议，二次开发要开源
- Electron 客户端 200MB+
- Clojure 不熟的话改源码门槛高

## 🤔 为什么这次推它给你

**你做 kb skill 是基于"互链 Markdown wiki"理念，Logseq 是这个理念的工业级实现**。重点学：**块级双向链接的数据模型 / journals 模式 / Markdown 文件格式约定**。你的 kb 可以借鉴 Logseq 的元数据语法（`#tag` / `((ref))` / `property:: value`），保持兼容性意味着你的笔记将来可以无痛迁过去。pattern 候选：`block-as-primary-unit`、`journals-driven-pkm`。

---
*由 /gitout 生成 · 2026-05-22 · theme: 个人知识库 / Markdown wiki*
