# company-website · 公司展示站模板

> 找一个轻量、展示为主的公司官网/品牌站脚手架。Next.js/Nuxt + Tailwind + 移动端响应式 + 可程序化（API/CLI/Git）管理内容。

## 健康度

- entries: 5
- 最新更新: 2026-05-27
- 主要技术栈分布: Next.js (4) / Nuxt (1)
- license 分布: MIT (4) / 未声明 (1)
- 平均 stars: ~880（高方差，从 81 到 2874）

## 速览表

| 项目 | 一句话 | stars | 推荐场景 |
|---|---|---|---|
| [nuxt-ui-templates/saas](./entries/nuxt-ui-templates__saas.md) | Nuxt 官方公司站模板，landing+pricing+docs+blog 全 | 549 | 团队会 Vue，想开箱即好看 |
| [akash3444/pure-landing-shadcnui-template](./entries/akash3444__pure-landing-shadcnui-template.md) | Next 15 + shadcn 极简单页 landing | 81 | 只要一个落地页，最轻量 |
| [themefisher/andromeda-light-nextjs](./entries/themefisher__andromeda-light-nextjs.md) | Next 多页站 + Git-CMS + PageSpeed 100 | 114 | 多页公司站 + Markdown 管理内容 |
| [LubomirGeorgiev/cloudflare-workers-nextjs-saas-template](./entries/LubomirGeorgiev__cloudflare-workers-nextjs-saas-template.md) | Next + CF Workers + 完整 CMS + AI agent 友好 | 765 | API/CLI 管理诉求最强 + 全栈托管 CF |
| [nextify-limited/saasfly](./entries/nextify-limited__saasfly.md) | 企业级 Next + Bun monorepo + Clerk/Stripe | 2874 | 未来 6 月要做用户系统 + 付费 |

## 选型决策树

```
你的公司站性质 → 推荐
├─ 就一个 landing 落地页 (CTA 为主)
│   └─ #2 pure-landing-shadcnui-template
├─ 多页展示 (关于/产品/新闻/联系)
│   ├─ 团队会 Vue → #1 nuxt-ui-templates/saas
│   └─ 团队只会 React → #3 andromeda-light-nextjs
├─ 展示 + 客户登录/订阅/付费
│   ├─ 想全栈 Cloudflare → #4 cloudflare-workers-nextjs-saas-template
│   └─ 想 Vercel 生态 → #5 saasfly
```

## 反思 2026-05-27

最低效环节 = 三轮 query 撞 0 返回（"nextjs company website template"、"shadcn landing template"、"saas landing nextjs boilerplate"），多词 AND 即使加 readme 也命中率低。下次先用单/双词 + 已知品牌词（shadcn/magicui/saasfly）做种子探针，再逐步加修饰词。

discarded_queries:
- "nextjs company website template"
- "saas landing nextjs boilerplate"
- "shadcn landing template"
- "magicui marketing"
