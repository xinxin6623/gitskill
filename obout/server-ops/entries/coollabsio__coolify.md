---
type: repo
repo: coollabsio/coolify
domain: server-ops
status: active
discovered: 2026-05-26
last_reviewed: 2026-05-26
intent_matched: "一台 VPS 全功能 PaaS，280+ 一键应用"
signals:
  stars: 56003
  last_commit: 2026-05-26
  language: PHP
  license: Apache-2.0
url: https://github.com/coollabsio/coolify
absorption:
  harvested: false
  used: false
  used_in: []
---

# Coolify · 小白说明书

## 🧐 这是什么
目前最火的开源自托管 PaaS，56k stars。一行命令装好，Web UI 管理一切：应用部署、数据库、SSL、备份。280+ 个一键模板。你可以理解为"自己服务器上的 Vercel + Railway"。

## 💡 解决什么问题
- 你想要"点一下就部署"的体验，但不想付 Vercel/Railway 的钱
- 你需要数据库（Postgres/MySQL/Redis）和应用部署在同一台机器上，统一管理
- 你想省心——SSL 自动签、备份自动跑、更新自动拉

## 🎯 谁该用 / 谁别用
**适合你如果：**
- 你想要最全功能、最省心的一站式方案
- 你有 2GB+ 内存的 VPS（推荐 4GB 以获得流畅体验）
- 你偶尔想从 Web UI 看看日志、监控

**别浪费时间如果：**
- 你的 VPS 只有 1GB 内存（Coolify 本身就要吃 1GB+）
- 你 100% 想用 CLI 操作、完全不碰浏览器
- 你追求极致轻量

## 🚀 三分钟上手
```bash
# 一键安装
curl -fsSL https://cdn.coollabs.io/coolify/install.sh | bash

# 装完后浏览器访问 http://your-vps:8000 做初始配置
# 之后可通过 API 操作（Claude Code 用这个）

# API 示例：创建应用
curl -X POST http://your-vps:8000/api/v1/applications \
  -H "Authorization: Bearer <api-token>" \
  -H "Content-Type: application/json" \
  -d '{"name":"my-app","git_repository":"https://github.com/you/app"}'
```

## 🔑 关键文件 / 关键概念
- 一键模板 — 280+ 预置应用（WordPress、Plausible、Umami 等），Docker Compose 模板
- Git 集成 — 连 GitHub/GitLab，push 自动部署
- API — v1 版 REST API，可编程操作（但文档还在补全中）
- 服务器管理 — 可管理多台远程服务器（SSH 连接）

## ⚠️ 踩坑提示
- 内存大户：Coolify 自身 + Traefik + 监控组件，空载就要 800MB-1GB
- API 文档不够完善，有些操作目前只能通过 Web UI
- v4 版本大改了架构，v3 的教程/插件不通用

## 🤔 为什么这次推它给你
**Claude Code 友好度：中高。** 有 API 可以程序化操作，但 API 文档仍在完善中，部分高级功能仍需 Web UI。对"2-3 个小站"场景，Coolify 功能过剩但胜在省心——数据库、备份、监控一条龙。trade-off：最吃内存，如果你的 VPS 只有 1-2GB，优先考虑 Dokku 或 Dokploy。

---
*由 /gitout 生成 · 2026-05-26 · intent: "一台 VPS 部署多个小网站，适合 Claude Code 操作"*
