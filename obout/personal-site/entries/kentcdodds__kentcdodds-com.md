---
type: repo
repo: kentcdodds/kentcdodds.com
domain: personal-site
status: active
discovered: 2026-05-23
last_reviewed: 2026-05-23
intent_matched: "全栈含 DB 的个人站参考典范"
signals:
  stars: 2488
  last_commit: 2026-05-20
  language: MDX
  license: GPL-3.0
url: https://github.com/kentcdodds/kentcdodds.com
absorption:
  harvested: false
  used: false
  used_in: []
---

# kentcdodds.com · 小白说明书

## 🧐 这是什么
Kent C. Dodds（React 圈名人、Epic Web/Epic React 课程作者）本人站源码。**Remix + React + TS + Express + Prisma + SQLite + Tailwind + Vitest + Playwright + Husky + npm workspaces**——一个货真价实的"个人站当作产品在做"的全栈仓库。**不是 template，是参考典范**。

## 💡 解决什么问题
- 你想看"个人站如何加用户系统/数据库/邮件系统/E2E 测试"
- 你想学一个真实 Remix 项目的目录组织、workspaces 切分、CI/Husky 怎么搭
- 你打算把个人站做成自己的"产品化基地"（含登录、内容订阅、评论、付费）

## 🎯 谁该用 / 谁别用
**适合你如果：**
- 你已经会做基础博客，想升级到"个人 SaaS 半身位"
- 你想看大佬级别的工程实践（lint:all/typecheck:all/build:all 全链路）
- 你能接受 GPL-3.0（个人用没问题，商用要小心）

**别浪费时间如果：**
- 你想"clone 改改名字就上线" → 这是本人站不是模板，违反用户约束
- 你只要博客功能（杀牛刀用法）
- 你不会 Remix（直接读起步成本高）

## 🚀 三分钟上手
```bash
git clone https://github.com/kentcdodds/kentcdodds.com
cd kentcdodds.com
cp services/site/.env.example services/site/.env
npm run setup -s  # 安装 + 重置 DB + 装 Playwright + 跑 e2e
npm run dev
```
要求：Node 24 + npm 10+。

## 🔑 关键文件 / 关键概念
- `services/site/` — 主站点（Remix）
- npm workspaces — 主站和 worker 共用 lockfile
- Prisma + SQLite — 用户、订阅、内容数据
- `app/routes/` — Remix 文件路由
- 完整 pre-commit 链：Prettier → lint:all → typecheck:all → build:all

## ⚠️ 踩坑提示
- 是 **GPL-3.0** —— 你 fork 来用，衍生站点必须开源，**别随手当个人站用**
- 是 Kent 本人站，里面**很多业务逻辑是绑死他自己的服务**（Epic React/Epic Web 课程系统）
- 不要试图整站克隆来用——拆模块学才是正确食用方法

## 🤔 为什么这次推它给你
**命中：** 通用性 + 扩展性（强命中，是这次榜单里**架构最完整的"个人站全栈仓库"参考**）、近期活跃 2026-05（强命中）、文档好（√，CONTRIBUTING + 各种 README）。
**Trade-off：** **违反你"必须是项目模板而非个人站本定"的硬约束**——所以列在第 4 位，**作为"想看真实工程实践长什么样"的参考资料**。**不是给你 clone 用的，是给你和 Claude Code 一起读、按模块挑想法搬到 [[thedevdavid__digital-garden]] 上的灵感库**。

---
*由 /gitout 生成 · 2026-05-23 · intent: "再搜一组个人网站全栈项目，具备通用性 扩展性"*
