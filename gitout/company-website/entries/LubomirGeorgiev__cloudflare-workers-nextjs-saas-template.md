---
type: repo
repo: LubomirGeorgiev/cloudflare-workers-nextjs-saas-template
domain: company-website
status: active
discovered: 2026-05-27
last_reviewed: 2026-05-27
intent_matched: "Next.js + Cloudflare Workers，内置 CMS+R2 媒体库，API/CLI 管理最完整"
signals:
  stars: 765
  last_commit: 2026-05-27
  language: TypeScript
  license: MIT
url: https://github.com/LubomirGeorgiev/cloudflare-workers-nextjs-saas-template
absorption:
  harvested: false
  used: false
  used_in: []
---

# Cloudflare Workers Next.js SaaS Template · 小白说明书

## 🧐 这是什么
**Next.js + Cloudflare Workers 全套 SaaS 模板**，跑在 CF 边缘节点上，**自带完整 CMS**（TipTap 编辑器 + R2 图床 + 标签分类 + 草稿/发布/定时发布 + 版本历史 + 全文搜索）+ 文档站 + 博客系统。

技术栈：Vinext（CF 实验性的 Vite-based Next.js 实现）+ Drizzle ORM + D1（SQLite）+ KV（缓存）+ R2（媒体）+ Lucia Auth。

## 💡 解决什么问题
你原话"**支持 API 管理最好能支持 CLI 管理**"——5 个候选里**这个是真正把 API/CLI 管理做到位的**：
- CMS 是配置驱动的（`cms.config.ts`），blog/docs collection 你可以自定义字段
- 媒体库走 R2 + 图像优化 API
- 部署用 GitHub Actions 全自动，CI 跑 typecheck/lint/E2E
- AI agents 友好：仓库专门有 `AGENTS.md` 让 Claude/Cursor 接手时有上下文

## 🎯 谁该用 / 谁别用
**适合你如果：**
- 公司站不只是展示，未来会加客户登录 / 订阅 / 团队管理
- 想全栈托管在 Cloudflare（一个账号搞定 域名+CDN+Workers+D1+R2+图床）
- 喜欢"AI agent 维护"思路，README 反复强调"AI-friendly"

**别浪费时间如果：**
- 你只要 5 页静态展示，这个模板**功能多到你 80% 用不上**（auth/billing/multi-tenant/admin/credit 系统）
- 不熟 Cloudflare 生态（D1/KV/R2/Wrangler 学习曲线不小）
- 想要 Vercel 部署——这个深度绑 CF Workers，迁移成本高

## 📜 协议风险
- **License：** MIT
- **商用 / 魔改 / 闭源：** ✅ 无风险
- **对外提供 SaaS / 给客户部署：** ✅ 无传染义务
- **注意：** 项目 README 里有 AgenticDev 工作室的 promo 段落，**上线前清理掉那段免得用户以为是关联广告**

## 🚀 三分钟上手
```bash
git clone https://github.com/LubomirGeorgiev/cloudflare-workers-nextjs-saas-template.git my-site
cd my-site
pnpm install
pnpx wrangler login                   # CF 账号登录
cp .env.example .env                  # 填环境变量
pnpm db:migrate:dev                   # 建本地 SQLite
pnpm db:seed                          # 灌测试数据
pnpm dev                              # http://localhost:3000
```

部署：仓库根有 `.agents/skills/prepare-cloudflare-production-deployment/SKILL.md`，**走那个 AI skill 引导一遍 CF 资源 + GitHub Actions secrets + Wrangler 部署**，按文档走基本不会出错。

## 🔑 关键文件 / 关键概念
- `cms.config.ts` — CMS 集合定义（blog/docs 各自字段），**改公司站 CMS 结构主要看这个**
- `wrangler.jsonc` — Cloudflare 绑定（D1/KV/R2 名字），改完要跑 `pnpm run cf-typegen`
- `src/constants.ts` — 站点常量（名字/URL/邮箱），上线前必改
- `AGENTS.md` — 给 AI agent 看的项目说明，**你也可以读这个理解项目结构**
- `.agents/skills/` — 部署用的 Claude Code skill

## ⚠️ 踩坑提示
- Vinext 是 CF 实验性技术，**API surface 可能有边角**——遇到怪 bug 先跑 `pnpm run check:vinext`
- E2E 测试用 Playwright，第一次跑要 `pnpm exec playwright install chromium`
- R2 媒体上传需要 CF 账号开通 R2 服务（付费但便宜，前 10GB 免费）
- 模板默认是"完整 SaaS"，你只做展示站要**删掉 admin/billing/multi-tenant 几个目录**否则代码看着吓人

## 🤔 为什么这次推它给你

1. **命中 intent.what：** 你说"支持 API 管理最好能支持 CLI 管理"——这个模板**配置驱动 CMS + Wrangler CLI + GitHub Actions 全自动部署**，5 个候选里 agent_friendly 维度满分。
2. **命中 soft pref：** Cloudflare Workers 全球边缘部署 = **真·轻量部署**（一行 `pnpm deploy`），加上自带的 AGENTS.md/.agents/skills/ 设计，**AI agent 接手维护门槛最低**。
3. **没命中的 trade-off：** ① 功能"严重过剩"——你说不要太多功能，但这个塞了 auth/billing/multi-tenant/admin/credit 一堆模块，要花半天裁剪；② 锁死 Cloudflare 生态，未来不好迁；③ Vinext 还是实验阶段，**生产环境用前最好先跑一周 staging**。

---
*由 /gitout 生成 · 2026-05-27 · intent: "公司网站项目，不需要太多功能，展示为主，轻量部署，代码优化，维护简洁，风格现代，有手机端适配，支持 api 管理最好能支持 cli 管理"*
