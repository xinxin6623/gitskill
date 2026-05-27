---
type: repo
repo: nextify-limited/saasfly
domain: company-website
status: active
discovered: 2026-05-27
last_reviewed: 2026-05-27
intent_matched: "企业级 Next.js SaaS 模板，bun create 一键起，monorepo 架构"
signals:
  stars: 2874
  last_commit: 2026-05-27
  language: TypeScript
  license: MIT
url: https://github.com/nextify-limited/saasfly
absorption:
  harvested: false
  used: false
  used_in: []
---

# Saasfly · 小白说明书

## 🧐 这是什么
**企业级 Next.js + Bun + Turborepo SaaS 启动模板**，社区最热门的之一（2.8k+ 星），技术栈算"现代主流豪华版"：Next.js App Router + Clerk + Stripe + Kysely + Postgres + tRPC + shadcn + Framer Motion。

跑 `bun create saasfly` 一行生成项目。

## 💡 解决什么问题
如果你的"公司站"实际上是"**公司站 + 产品试用 + 用户登录 + 订阅付费**"，这个模板**少踩半年坑**——auth、payments、i18n、SEO、monorepo、CI、邮件、admin 全套预制好了。

## 🎯 谁该用 / 谁别用
**适合你如果：**
- 公司站只是冰山一角，未来 6 个月内要做用户系统/付费
- 团队会 TypeScript + 喜欢 monorepo 架构
- 想用 Vercel/Bun 这种偏前沿但社区活跃的栈

**别浪费时间如果：**
- 你真的只做"展示为主"——这个 hello world 就有 8 个 package，**学习曲线和你的诉求严重不匹配**
- 不愿意装 Bun（默认就是 bun-first，npm/pnpm 兼容但不顺手）
- 不想接 Clerk（云端认证服务，有免费档但锁定它生态）

## 📜 协议风险
- **License：** MIT
- **商用 / 魔改 / 闭源：** ✅ 无风险
- **对外提供 SaaS / 给客户部署：** ✅ 无传染义务
- **第三方服务依赖：** Clerk（认证）、Stripe（支付）、Resend（邮件）都有自己付费方案，**模板免费 ≠ 你的运行成本免费**

## 🚀 三分钟上手
```bash
# 装 Bun (macOS)
brew install oven-sh/bun/bun

# 起项目
bun create saasfly my-site
cd my-site

# 配环境
cp .env.example .env.local
# 至少要填 POSTGRES_URL（本地 docker 一个 postgres 就行）

bun db:push           # 建表
bun run dev:web       # http://localhost:3000
```

部署：Vercel 一键，但要先在 Vercel 上挂好 Postgres（或外接 Supabase/Neon）。

## 🔑 关键文件 / 关键概念
- `apps/nextjs/` — 主 Next.js 应用
- `packages/ui/` — 共享 UI 组件（shadcn 基底）
- `packages/db/` — Kysely schema 和迁移
- `packages/auth/` — Clerk 集成（之前是 NextAuth，2025-06 切到 Clerk，仓库还留了 NextAuth 分支）
- `packages/email/` — React Email 模板
- `turbo.json` — Turborepo 任务编排

## ⚠️ 踩坑提示
- **Auth 切换：** README 说 2025-06-01 后默认改 Clerk。如果你想要 NextAuth/Auth.js，要切到 `feature-nextauth` 分支
- **数据库必需：** 没 Postgres 跑不起来，**纯静态展示站根本用不到**——你只做展示就别选这个
- Bun + Turborepo 在 Windows 上偶尔抽风，**macOS/Linux 才是一等公民**
- `bun db:push` 是非破坏式同步 schema，要做生产迁移用 Prisma 命令（仓库说 Prisma 仅作 schema 工具，运行时用 Kysely）

## 🤔 为什么这次推它给你

1. **命中 intent.what：** 你列了"现代风、移动端、轻量部署、API 管理"——这个模板**所有维度都满分**（Next 15 + shadcn + tRPC API + Vercel 一键），技术栈是"未来 3 年不过时"的水平。
2. **命中 soft pref：** `bun create saasfly` 是真正的 CLI 启动器（命中你"CLI 管理"诉求），monorepo + Turborepo 设计让多 app 共享代码不重复。
3. **没命中的 trade-off：** ① **严重违背你"不要太多功能"原则**——这个模板把 SaaS 全套都给你了，你做展示站要删一堆代码；② 锁 Postgres + Clerk + Stripe，**展示站根本用不到这些依赖**；③ Bun 还在快速演进，偶尔升级会破坏兼容。**如果你确实只做展示，请选 #1 或 #2**。

---
*由 /gitout 生成 · 2026-05-27 · intent: "公司网站项目，不需要太多功能，展示为主，轻量部署，代码优化，维护简洁，风格现代，有手机端适配，支持 api 管理最好能支持 cli 管理"*
