---
type: repo
repo: Dokploy/dokploy
domain: server-ops
status: active
discovered: 2026-05-26
last_reviewed: 2026-05-26
intent_matched: "一台 VPS 现代化 PaaS，CLI + API 双通道"
signals:
  stars: 34245
  last_commit: 2026-05-26
  language: TypeScript
  license: Other
url: https://github.com/Dokploy/dokploy
absorption:
  harvested: false
  used: false
  used_in: []
---

# Dokploy · 小白说明书

## 🧐 这是什么
2024 年冒出来的新锐自托管 PaaS，定位"开源 Vercel + Netlify + Heroku"。内置 Traefik 做反代 + 自动 SSL，原生支持 Docker Compose，还有官方 CLI 和 API。

## 💡 解决什么问题
- 你想在一台 VPS 上一键部署多个完全不同的应用（Node/Python/Go/PHP 混着来）
- 你需要 Traefik 自动路由 + Let's Encrypt，但不想自己写 Traefik 配置
- 你想让 Claude Code 通过 CLI/API 操作部署，同时偶尔自己从 Web UI 看看状态

## 🎯 谁该用 / 谁别用
**适合你如果：**
- 你有 Docker Compose 项目想直接丢上去跑
- 你想要 Web UI 可视化 + CLI/API 自动化两手抓
- 你喜欢新工具、社区活跃、更新快

**别浪费时间如果：**
- 你的 VPS 只有 512MB 内存（Dokploy 本身吃约 300-400MB）
- 你只想最简方案，不需要数据库管理 / 备份 / 监控这些额外功能
- 你讨厌 Node/TypeScript 生态

## 🚀 三分钟上手
```bash
# 一键安装（VPS 上执行）
curl -sSL https://dokploy.com/install.sh | bash

# 安装 CLI（本地）
npm i -g @dokploy/cli

# CLI 部署示例
dokploy deploy --app my-api

# 或通过 API（Claude Code 可直接调用）
curl -X POST https://your-vps:3000/api/application/create \
  -H "Authorization: Bearer <token>" \
  -d '{"name":"my-blog","type":"docker-compose"}'
```

## 🔑 关键文件 / 关键概念
- Traefik — Dokploy 内部用 Traefik 做路由，你添加应用时自动生成路由规则
- Docker Compose 原生支持 — 扔 `docker-compose.yml` 就能跑
- Templates — 预设模板一键装 Postgres/Redis/Plausible 等
- API — 完整 REST API，所有 Web UI 能做的事 API 都能做

## ⚠️ 踩坑提示
- 比 Dokku 重不少，最低建议 2GB 内存 VPS
- 项目还年轻（2024 起步），偶有 breaking change
- Docker Swarm 模式的多节点功能还在完善，单机用没问题

## 🤔 为什么这次推它给你
**Claude Code 友好度：高。** 官方 CLI + 完整 REST API，Claude Code 可以通过 `curl` 或 CLI 完成创建应用、部署、绑域名等全部操作。比 Dokku 多了 Web UI 看状态 + 原生 Docker Compose 支持——你的"2-3 个不同功能小站"如果用 docker-compose 编排，Dokploy 比 Dokku 更顺手。trade-off：比 Dokku 吃更多内存，项目较新。

---
*由 /gitout 生成 · 2026-05-26 · intent: "一台 VPS 部署多个小网站，适合 Claude Code 操作"*
