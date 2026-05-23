---
type: repo
repo: jackyzha0/quartz
domain: misc
status: active
decision: harvest
discovered: 2026-05-22
last_reviewed: 2026-05-22
theme: personal-kb
intent_matched: "Markdown 文件夹 → 个人数字花园网站（一键发布）"
signals:
  stars: 12238
  last_commit: 2026-05-22
  language: TypeScript
  license: MIT
url: https://github.com/jackyzha0/quartz
absorption:
  harvested: false
  used: false
  used_in: []
---

# Quartz v4 · 小白说明书

## 🧐 这是什么

**把你本地一坨 markdown 文件直接发布成"数字花园"网站的静态站生成器**。1.2 万星 MIT。作者 jackyzha0（个人博客 jzhao.xyz 是 digital garden 圈名站）出品。开箱即用：克隆模板 → 把笔记扔进 `content/` → 部署 → 拿到一个带双向链接、图谱、搜索、目录的漂亮个人站。

引语用了 Richard Hamming："开着门工作的人会被各种打扰，但偶尔会得到关于这个世界什么是重要的暗示。"——精神是**"在公开场所思考"**。

## 💡 解决什么问题

你的笔记跟世界之间隔着一道墙：

- Obsidian / Logseq / Foam 都是私有工具
- 想分享某个页面要导出
- 想做"公开的笔记本"没有简单方案

Quartz **拿你已有的 markdown 文件夹直接渲染成网站**——双向链接、图谱、全文搜索、tag、Reading time 全自带。Cloudflare Pages / GitHub Pages 免费部署。

## 🎯 谁该用 / 谁别用

**适合你如果：**
- 已经有一堆 markdown 笔记想公开部分（你的 kb 就是）
- 喜欢 digital garden 文化
- 想要一个能 self-host 的个人站

**别浪费时间如果：**
- 不想公开任何笔记
- 不熟 TypeScript / Node（改主题麻烦）
- 笔记不在 Markdown（要先迁）

## 🚀 三分钟上手

```bash
git clone https://github.com/jackyzha0/quartz.git
cd quartz
npm install

# 把你的笔记放进 content/
cp -r ~/knowledge/concepts content/

# 本地预览
npx quartz build --serve

# 部署
npx quartz build
# 把 public/ 推到 GitHub Pages / Netlify / Cloudflare
```

## 🔑 关键文件 / 关键概念

- **content/** — 你的 markdown 文件夹
- **quartz.config.ts** — 主题、插件、域名配置
- **plugins** — 双向链接、图谱、搜索都是插件
- **transformers** — 处理 markdown 渲染前后

## ⚠️ 踩坑提示

- 默认配置面向英文，中文搜索要调
- Wikilink `[[ ]]` 语法支持，但需要前缀大小写一致
- 自定义主题要懂 Preact / CSS

## 🤔 为什么这次推它给你

**你 kb skill 长期可以走"私 + 公"双轨**——本地 markdown 文件夹用 kb / Foam 维护，**用 Quartz 把其中 `concepts/` 部分发布成公开站**。最少改动、最大杠杆。可以直接抄它的：**双向链接渲染、图谱组件、Reading time 计算**。pattern 候选：`markdown-folder-to-digital-garden`、`config-as-code-static-site`。

---
*由 /gitout 生成 · 2026-05-22 · theme: 个人知识库 / Markdown wiki*
