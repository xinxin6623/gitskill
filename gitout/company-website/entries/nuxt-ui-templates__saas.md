---
type: repo
repo: nuxt-ui-templates/saas
domain: company-website
status: active
discovered: 2026-05-27
last_reviewed: 2026-05-27
intent_matched: "Nuxt 公司站模板，含 landing+pricing+docs+blog 全套展示页"
signals:
  stars: 549
  last_commit: 2026-05-27
  language: Vue
  license: MIT
url: https://github.com/nuxt-ui-templates/saas
absorption:
  harvested: false
  used: false
  used_in: []
---

# Nuxt SaaS Template · 小白说明书

## 🧐 这是什么
Nuxt 官方团队出的公司展示站模板，**Landing 页 + Pricing 页 + 文档页 + 博客页**一次给齐，全用 Nuxt UI 组件搭，跑 `npm create nuxt@latest -- -t ui/saas` 就直接起项目。

## 💡 解决什么问题
你想做个公司站，最痛的点是"前端从零搭一个好看的 hero/feature/pricing 真的太烦"。这个模板把这些常见区块都做好了，**改文案改图片就能上线**。

它还自带博客和文档系统（基于 Nuxt Content），你后续加新闻 / changelog / 帮助中心都不用再装东西。

## 🎯 谁该用 / 谁别用
**适合你如果：**
- 团队里有人会 Vue 或愿意学（比 React 学习曲线低很多）
- 想要"开箱就好看"，不愿意自己调 hero 区的 hover 状态
- 内容用 Markdown 写就行（README、博客、产品页都能用）

**别浪费时间如果：**
- 你只会 React，不愿碰 Vue 生态
- 你的官网需要复杂的后端逻辑（这个偏静态展示）
- 想要 Tailwind UI 那种付费精致组件（Nuxt UI 风格偏简洁实用）

## 📜 协议风险
- **License：** MIT
- **商用 / 魔改 / 闭源：** ✅ 无风险，公司官网随便用
- **对外提供 SaaS / 给客户部署：** ✅ 无传染义务

## 🚀 三分钟上手
```bash
npm create nuxt@latest -- -t ui/saas my-company-site
cd my-company-site
pnpm install
pnpm dev
# 打开 http://localhost:3000
```

部署到 Vercel：仓库 README 有一键 Deploy 按钮；想自建 VPS 就 `pnpm build` 出静态文件丢 nginx。

## 🔑 关键文件 / 关键概念
- `content/` — 博客和文档 Markdown 都写这里（Nuxt Content 自动扫）
- `app.config.ts` — 站点配色、Logo、SEO 元信息，**改公司站从这里开始**
- `pages/` — Nuxt 的文件路由，加新页面就在这建 `.vue`
- `nuxt.config.ts` — 模块配置，要不要 i18n、要不要 analytics 在这开关

## ⚠️ 踩坑提示
- Nuxt UI 的 Pro 组件部分是收费的（Pro 那一档），但这个 SaaS 模板用的都是免费组件，**别误以为整个模板要付费**
- 默认主题是浅色 + 蓝色调，要改公司色把 `app.config.ts` 里的 `ui.colors` 全部换掉，**别只改一处**
- Nuxt Content 改了 markdown 文件要等几秒才热更新，别以为坏了

## 🤔 为什么这次推它给你

1. **命中 intent.what：** 你要"公司展示站，展示为主+轻量部署+现代风+移动端"，这个模板 landing+pricing+docs+blog 一次到位，**官方维护、Tailwind 风、自带响应式**，开箱直接能跑。
2. **命中 soft pref：** Markdown 写内容直接对接你想要的 "CLI/Git 管理"（写完 `git push` 就部署），Nuxt UI 组件库设计感在线，**AI 改 Vue 代码也越来越好用**。
3. **没命中的 trade-off：** 你之前提到熟悉 React/Next 选项，这个是 **Vue/Nuxt 阵营**——如果你完全不想碰 Vue，跳过这个直接看 #2 或 #3。

---
*由 /gitout 生成 · 2026-05-27 · intent: "公司网站项目，不需要太多功能，展示为主，轻量部署，代码优化，维护简洁，风格现代，有手机端适配，支持 api 管理最好能支持 cli 管理"*
