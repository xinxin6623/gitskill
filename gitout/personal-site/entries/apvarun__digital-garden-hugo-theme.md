---
type: repo
repo: apvarun/digital-garden-hugo-theme
domain: personal-site
status: active
discovered: 2026-05-23
last_reviewed: 2026-05-23
intent_matched: "高性能个人 digital garden 主题"
signals:
  stars: 296
  last_commit: 2026-04-13
  language: HTML
  license: MIT
url: https://github.com/apvarun/digital-garden-hugo-theme
absorption:
  harvested: false
  used: false
  used_in: []
---

# Digital Garden Hugo Theme · 小白说明书

## 🧐 这是什么
Hugo（Go 写的静态站生成器）的 digital garden 主题。**多栏布局 + portfolio 区 + Newsletter 集成（Substack/Buttondown/Revue）+ KaTeX 数学公式 + Lighthouse 满分性能**。Hugo 本身的构建速度是 Next.js 这类的 10 倍以上。

## 💡 解决什么问题
- 你想要极致加载速度（静态 HTML + 不带 JS hydration）
- 你写笔记/技术文章多到内容量大（Hugo 处理几千篇内容不眨眼）
- 你想要"开箱可发邮件订阅"的简单方案，不想自己接 API

## 🎯 谁该用 / 谁别用
**适合你如果：**
- 你看重性能（Lighthouse 满分有官方截图）
- 你的内容主要是 Markdown 文章，少交互
- 你接受 Hugo template 语法（Go template，与 React 完全不同）

**别浪费时间如果：**
- 你的"个人站"需要动态后台（评论、用户登录、Dashboard）
- 你只熟 React/TS 生态（Hugo template 学习曲线另算）
- 你想用 Claude Code 大刀阔斧改逻辑（Claude 改 Go template 不如改 TS/TSX 自如）

## 🚀 三分钟上手
```bash
# 在你已有的 Hugo 站点根目录下
git submodule add https://github.com/apvarun/digital-garden-hugo-theme.git themes/digitalgarden
# 在 config.toml 中设置 theme = "digitalgarden"
hugo server -D
```

## 🔑 关键文件 / 关键概念
- `layouts/` — Hugo template（HTML + Go template 语法）
- `assets/` — CSS / JS 源文件
- `exampleSite/` — 示例配置（拿来改最快）
- Newsletter 集成在 partial template 里，配置时只填 Substack/Buttondown 用户名

## ⚠️ 踩坑提示
- 需要 Hugo `>= 0.82.1`，老版本不行
- Hugo template 调试很 painful（出错信息不友好）
- 默认搜索/评论需要自己接（Hugo 主题通病）

## 🤔 为什么这次推它给你
**命中：** 通用性（√，主题可套任意 Hugo 站点）、扩展性（√，partial template 切得清楚）、近期活跃 2026-04（√）、文档好（√，有独立文档站）、性能（额外加分）。
**Trade-off：** **不是 TS 栈，Claude Code 改起来不如 Next.js 项目顺手**——但用户勾了"看推荐"无技术栈硬约束，所以列出来作为"内容站性能路线"代表。如果你写作量很大、不需要复杂交互，性能优势会真的让你感受到。否则建议用 [[thedevdavid__digital-garden]]。

---
*由 /gitout 生成 · 2026-05-23 · intent: "再搜一组个人网站全栈项目，具备通用性 扩展性"*
