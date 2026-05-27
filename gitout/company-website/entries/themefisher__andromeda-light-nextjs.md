---
type: repo
repo: themefisher/andromeda-light-nextjs
domain: company-website
status: active
discovered: 2026-05-27
last_reviewed: 2026-05-27
intent_matched: "Next.js 多页公司站，PageSpeed 100，自带 Sitepins Git-CMS"
signals:
  stars: 114
  last_commit: 2026-05-27
  language: TypeScript
  license: MIT
url: https://github.com/themefisher/andromeda-light-nextjs
absorption:
  harvested: false
  used: false
  used_in: []
---

# Andromeda Light Nextjs · 小白说明书

## 🧐 这是什么
Themefisher 出的 **Next.js 公司站/SaaS 展示模板**，PageSpeed 跑分 100，**自带 7 个常用页面**（首页 + 关于 + 联系 + 元素 + 条款 + 博客列表 + 博客详情），可以接 Sitepins 这种 Git-based 无头 CMS 让非技术同事改内容。

## 💡 解决什么问题
你要的"多页公司站 + 现代风 + 移动端 + 支持 API/CLI 管理"，这个模板基本是最贴合的一个：
- 多页结构（不只是 landing）
- MDX 写博客和产品页（**Git 提交即发布，命中你的 CLI/Git 管理诉求**）
- 可选接 Sitepins 给非技术同事用图形后台改文案

## 🎯 谁该用 / 谁别用
**适合你如果：**
- 公司站要有"关于/产品/新闻/联系"几个独立页面
- 想用 MDX 写内容（比纯 Markdown 多一层 React 组件能嵌入图表/卡片）
- 在意 SEO 和加载速度（PageSpeed 100 不是吹的）

**别浪费时间如果：**
- 你只要一个 landing 页（这个略重，选 #2）
- 完全不想接 CMS，纯硬编码（也能用，但 MDX 学习成本比纯 .tsx 高一点点）
- Themefisher 是商业主题作坊，**你能接受免费版的 footer 默认带 "by Themefisher"**

## 📜 协议风险
- **License：** MIT（代码部分）
- **商用 / 魔改 / 闭源：** ✅ 代码 MIT 随便用
- **对外提供 SaaS / 给客户部署：** ✅ 无传染义务
- **⚠️ 图片 license：** README 明确说**演示图片有自己的 license，不能直接商用**，上线前必须把所有图换成你自己的或免费可商用素材（unsplash/pexels）

## 🚀 三分钟上手
```bash
git clone https://github.com/themefisher/andromeda-light-nextjs.git my-site
cd my-site
npm install
npm run dev
# 打开 http://localhost:3000
```

Vercel 一键部署或 VPS：`npm run build && npm run start`。

接 Sitepins（可选，非技术同事用）：仓库 README 里有 "Edit with Sitepins" 按钮，点了就走它的 onboarding。

## 🔑 关键文件 / 关键概念
- `src/content/` — 博客 MDX 文件 + 各页 frontmatter，**这是你内容管理的真相源**
- `src/config/` — 站点元数据、菜单、社交链接、theme 颜色都在这
- `src/components/` — hero/feature/cta 等可复用 React 组件
- `next.config.js` — SEO/i18n 等扩展配置

## ⚠️ 踩坑提示
- 默认 demo 图片**不能商用**，上线前必换
- MDX 里嵌 React 组件需要先在 `mdx-components.tsx` 注册，不然 `<MyCard />` 渲染不出来
- Sitepins 是付费产品有免费档，**别误以为模板用了 Sitepins 就要交钱**——纯 MDX 也能跑
- Themefisher 在 README 末尾会推他们的付费版（Bigspring Light），别被诱导走付费方案，免费版功能其实够公司站用

## 🤔 为什么这次推它给你

1. **命中 intent.what：** "公司网站，展示为主，多页+移动端+现代风+API/CLI 管理"——这个模板**同时 cover 多页结构 + Git 写内容 + PageSpeed 100 + 响应式**，是 5 个候选里"诉求覆盖广度"最高的一个。
2. **命中 soft pref：** MDX 让你 `git push` 即部署内容（最接近"CLI 管理"的体验），同时 Sitepins 又给非技术同事留了图形后台后路，**双赢**。
3. **没命中的 trade-off：** ① stars 只有 114，社区不算大，遇到难题官方文档可能不够细；② Themefisher 的免费模板隐隐带商业 upsell 信息，你可能要花几分钟"去广告化"。

---
*由 /gitout 生成 · 2026-05-27 · intent: "公司网站项目，不需要太多功能，展示为主，轻量部署，代码优化，维护简洁，风格现代，有手机端适配，支持 api 管理最好能支持 cli 管理"*
