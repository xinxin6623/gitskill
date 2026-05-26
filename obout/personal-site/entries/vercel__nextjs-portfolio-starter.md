---
type: repo
repo: vercel/nextjs-portfolio-starter
domain: personal-site
status: active
discovered: 2026-05-23
last_reviewed: 2026-05-23
intent_matched: "最简洁的官方个人站 starter"
signals:
  stars: 731
  last_commit: 2025-11-21
  language: JavaScript
  license: ""
url: https://github.com/vercel/nextjs-portfolio-starter
absorption:
  harvested: false
  used: false
  used_in: []
---

# Vercel Portfolio Starter · 小白说明书

## 🧐 这是什么
Vercel 官方出品的 Next.js + **Nextra** 个人站起步模板。Nextra 是基于 Next.js 的"Markdown 优先文档/博客"框架。**代码量极小、官方维护、零额外花活**——这是"我想要个看起来正常的个人站起点"的最小答案。

## 💡 解决什么问题
- 你想要 Vercel 官方背书的栈（升级、部署、生态零摩擦）
- 你只想要"博客 + 标签 + RSS"基础三件，不要花哨功能
- 你后续打算自己往里加模块——需要一张干净的画布

## 🎯 谁该用 / 谁别用
**适合你如果：**
- 你想从最小起点出发，自己往上盖楼
- 你是 Next.js 新手，需要官方范例确认"标准做法"
- 你已经决定部署到 Vercel

**别浪费时间如果：**
- 你想要"开箱即用的五件套" → 直接用 [[thedevdavid__digital-garden]]
- 你想要 Tailwind/shadcn 现代审美（这个是 Nextra 默认主题，偏文档站风格）
- 你想要 newsletter / analytics 等开箱集成

## 🚀 三分钟上手
```bash
npx create-next-app --example blog my-blog
cd my-blog
npm run dev
```

## 🔑 关键文件 / 关键概念
- `theme.config.js` — Nextra 主题配置（站名、底部、导航）
- `pages/posts/*.md` — 博文（Markdown 即文章）
- `pages/_document.js` — meta 标签
- `scripts/gen-rss.js` — RSS 生成

## ⚠️ 踩坑提示
- 没有 LICENSE 字段（Vercel 官方示例通常 MIT，但 GitHub 上没标 → 介意的话先去 issue 问）
- Nextra 升级到 v3/v4 时主题配置 API 有变，跟随 Nextra 文档而不是这个 starter
- 真的非常基础——你想要的扩展性需要自己加，不是它给你

## 🤔 为什么这次推它给你
**命中：** 通用性（强命中，官方 starter 是最通用起点）、近期活跃 2025-11（√，刚好一年内）、文档好（√，官方品质）、代码量适中（**最强命中**，极少代码）。
**Trade-off：** 扩展性靠你自己加——它没给你 Now 页、没给你 Projects 页、没给 Newsletter。但你勾了"代码量适中、文档好" → 这是这次榜单里**最干净的起点**，适合"我用 Claude Code 在它上面慢慢加"的工作方式。

---
*由 /gitout 生成 · 2026-05-23 · intent: "再搜一组个人网站全栈项目，具备通用性 扩展性"*
