---
type: repo
repo: akash3444/pure-landing-shadcnui-template
domain: company-website
status: active
discovered: 2026-05-27
last_reviewed: 2026-05-27
intent_matched: "最轻量的 Next 15 + shadcn 单页 landing，纯展示零废料"
signals:
  stars: 81
  last_commit: 2026-05-27
  language: TypeScript
  license: none-declared
url: https://github.com/akash3444/pure-landing-shadcnui-template
absorption:
  harvested: false
  used: false
  used_in: []
---

# PureLanding · 小白说明书

## 🧐 这是什么
一个**纯净的 Next.js 15 + Shadcn UI + Tailwind 单页 landing 模板**。没有 auth、没有数据库、没有 billing——就一个 landing 页。clone 下来改文案就能上。

## 💡 解决什么问题
你说"不需要太多功能，展示为主"——很多 SaaS 模板硬塞 Stripe 和 Postgres，你要的明明是个落地页。这个模板**就是给你这种用户准备的**：没多余东西。

它内置了 shadcn UI Blocks（社区常用 landing 区块库），hero / feature / testimonial / pricing / footer 都有，**你只要选你要的几块拼起来**。

## 🎯 谁该用 / 谁别用
**适合你如果：**
- 公司站就一页（关于我们 + 产品 + CTA 联系）
- 用 React/Next 生态熟练，喜欢 shadcn 那种 "复制组件到自己仓库" 的灵活度
- 想 AI 改前端代码——shadcn 是 AI 改代码最舒服的栈（Claude/Cursor 训练数据多）

**别浪费时间如果：**
- 你要多页站点（关于、产品、新闻、博客分开）——这个只有 single page，自己加路由太累，不如选 #1 或 #3
- 想要现成的 Headless CMS 后台——这个纯静态，内容写在 React 组件里

## 📜 协议风险
- **License：** ⚠️ **仓库没声明 LICENSE 文件**
- **商用 / 魔改 / 闭源：** ⚠️ 严格来说没声明 license 默认"保留所有权利"，**用之前给作者发邮件确认或提 issue 请求加 MIT/Apache**，再不放心就 fork 后自己加 LICENSE 并 attribution
- **对外提供 SaaS / 给客户部署：** ⚠️ 同上，建议先确认 license 再商用

> ⚠️ **协议警告：仓库未声明 license，公司商用前务必先和作者确认或换 #2 / #3 这种明确 MIT 的模板。**

## 🚀 三分钟上手
```bash
git clone https://github.com/akash3444/pure-landing-shadcnui-template.git my-site
cd my-site
npm install
npm run dev
# 打开 http://localhost:3000
```

想用 Tailwind v4：`git checkout tailwind-v4`。

部署：Vercel 一键，或 `npm run build` 后把 `.next/` 丢 VPS。

## 🔑 关键文件 / 关键概念
- `app/page.tsx` — 主页面入口，所有 section 在这拼装
- `components/sections/` — hero/feature/pricing/cta 各自一个文件，**改公司站文案就改这里**
- `tailwind.config.ts` — 配色字体在这调
- shadcn 组件在 `components/ui/`，可以用 `npx shadcn add <name>` 加新组件

## ⚠️ 踩坑提示
- README 没说默认 dark mode 是否开启，看 `app/layout.tsx` 里 `ThemeProvider` 配置；想强制公司站只用浅色就删 dark 类
- 没 LICENSE 文件是这个项目最大的坑，**别让法务找你**
- 81 stars 不算热门，遇到 bug 自己改起来要会读 Next App Router 源码

## 🤔 为什么这次推它给你

1. **命中 intent.what：** 你说"不需要太多功能，展示为主"——这是候选里**真正最纯净的展示模板**，没多余依赖、没 auth、没数据库，单页 landing 就这一个使命。
2. **命中 soft pref：** Next.js + Tailwind + shadcn 是你列的"Vite+React+Tailwind"的现代延伸，**AI 改 shadcn 代码全网最熟**，未来要 AI 帮你做改版也最顺。
3. **没命中的 trade-off：** ① **没 LICENSE 是硬伤**，商用前必须解决；② 单页设计，多页公司站要自己加路由；③ 没内置 CMS/API，内容硬编码在 React 里——如果你想要 "API/CLI 管理内容" 这个不满足。

---
*由 /gitout 生成 · 2026-05-27 · intent: "公司网站项目，不需要太多功能，展示为主，轻量部署，代码优化，维护简洁，风格现代，有手机端适配，支持 api 管理最好能支持 cli 管理"*
