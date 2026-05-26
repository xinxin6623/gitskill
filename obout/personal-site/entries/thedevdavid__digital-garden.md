---
type: repo
repo: thedevdavid/digital-garden
domain: personal-site
status: active
discovered: 2026-05-23
last_reviewed: 2026-05-23
intent_matched: "可扩展的全栈个人超级主页模板"
signals:
  stars: 331
  last_commit: 2026-03-04
  language: TypeScript
  license: MIT
url: https://github.com/thedevdavid/digital-garden
absorption:
  harvested: false
  used: false
  used_in: []
---

# Digital Garden by thedevdavid · 小白说明书

## 🧐 这是什么
专为开发者做的"个人 digital garden"开源模板。**Next.js App Router + MDX + Contentlayer + Tailwind + shadcn/ui**——现在 React 生态最主流的"内容站"组合。配置文件几乎全在 `utils/` 下的 TS 数据文件，改起来直白到不像模板。

## 💡 解决什么问题
- 你想要"博客 + projects + uses + now + about"五件套但不想自己拼脚手架
- 你看了一圈"个人站"都是别人本人站、改起来一头雾水，需要明确文档的 starter
- 你的工作流是 Markdown 写作，需要前置自动化（RSS / Analytics / Newsletter）

## 🎯 谁该用 / 谁别用
**适合你如果：**
- 你写 Next.js / React，喜欢 shadcn/ui 这套设计语言
- 你要的是"个人产品化的站"——含数据分析、邮件订阅、SEO
- 你用 Claude Code 改代码（TS + 主流栈，AI 改起来无障碍）

**别浪费时间如果：**
- 你追求"零 JS 极致性能" → 用 [[apvarun__digital-garden-hugo-theme]]
- 你拒绝 Tailwind / shadcn 设计语言
- 你只想要博客一项功能（杀鸡用牛刀，用 [[vercel__nextjs-portfolio-starter]]）

## 🚀 三分钟上手
```bash
# 把仓库作为 GitHub template 用，然后：
pnpm install
# 编辑这五个文件
# - utils/metadata.ts        基本信息
# - utils/uses-data.ts       设备/软件清单
# - utils/projects-data.ts   项目列表
# - utils/navigation-links.ts 导航
# - content/pages/now & about
pnpm dev
```

## 🔑 关键文件 / 关键概念
- `content/posts/` — 博文（MDX）
- `content/projects/` — 项目页
- `content/pages/now` 与 `about` — Now 页 + 关于
- `utils/*-data.ts` — 所有列表性内容用 TS 数组配置（Claude 改起来最舒服）
- `app/` — Next.js App Router 路由
- 已内置：MailerLite / Umami / Plausible / Vercel Analytics / Google Analytics 切换

## ⚠️ 踩坑提示
- README 自称 "always evolving"，有些 roadmap 功能未完工，看 [Features & Roadmap] 章节确认
- Contentlayer 这两年维护进度时快时慢，注意 Next.js 升级时的兼容
- 默认部署假定 Vercel，迁到 Cloudflare/自建要改 build 配置

## 🤔 为什么这次推它给你
**命中：** 集成型（√，blog/projects/uses/now/about 全套）、可扩展（√，模块化 utils 配置）、近期活跃 2026-03（√）、文档极完整（强命中，README 目录覆盖 Fonts/Colors/Analytics/Newsletter 等十几项）、TS 栈适合 Claude 改（√）。
**Trade-off：** 331 stars 不算热门、不如 [[kentcdodds__kentcdodds-com]] 那样"全栈含 DB"。但你强调"代码量适中" → 它不带 Prisma 不带 Express server，刚好是适中那一档。**综合下来这次首推它。**

---
*由 /gitout 生成 · 2026-05-23 · intent: "再搜一组个人网站全栈项目，具备通用性 扩展性"*
