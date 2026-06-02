---
type: repo
repo: caprover/caprover
domain: server-ops
status: active
discovered: 2026-05-26
last_reviewed: 2026-05-26
intent_matched: "一台 VPS 轻松部署多个应用，CLI + 一键商店"
signals:
  stars: 15039
  last_commit: 2026-05-26
  language: TypeScript
  license: Other
url: https://github.com/caprover/caprover
absorption:
  harvested: false
  used: false
  used_in: []
---

# CapRover · 小白说明书

## 🧐 这是什么
"加强版 Heroku"——底层是 Docker + Nginx + Let's Encrypt，但给你包了一层简单的 Web UI 和 CLI。一键装数据库、一键装 WordPress，不需要懂 Docker 和 Nginx 配置。

## 💡 解决什么问题
- 你想要类 Heroku 体验但不想每月花 250 刀（同样配置 VPS 只要 5 刀）
- 你想从一个"应用商店"里点击安装 MySQL、Redis、WordPress 等
- 你想 CLI 部署，但偶尔也从 Web UI 看看日志和监控

## 🎯 谁该用 / 谁别用
**适合你如果：**
- 你想要 Web UI + CLI 两手都有
- 你喜欢"应用商店"式体验，点击装数据库/缓存
- 你有 1GB+ 内存 VPS

**别浪费时间如果：**
- 你需要原生 Docker Compose 支持（CapRover 用自己的抽象层）
- 你追求最新技术栈（项目更新节奏偏慢）
- 你 100% CLI-only，不想装 Web UI

## 🚀 三分钟上手
```bash
# 安装 CapRover（VPS 需要预装 Docker）
docker run -p 80:80 -p 443:443 -p 3000:3000 \
  -e ACCEPTED_TERMS=true \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v /captain:/captain \
  caprover/caprover

# 本地安装 CLI
npm install -g caprover

# CLI 初始化 + 部署
caprover serversetup  # 绑域名、启用 SSL
caprover deploy       # 选择 tar/git 部署方式
```

## 🔑 关键文件 / 关键概念
- `captain-definition` — 项目根目录的部署描述文件（指定 Dockerfile 或 buildpack）
- One-Click Apps — 社区维护的应用模板库（600+ 个）
- 自定义 Nginx 模板 — 每个 app 可以覆盖 Nginx 配置
- Docker Swarm — 底层编排引擎（单机也用 Swarm mode）

## ⚠️ 踩坑提示
- 底层用 Docker Swarm，不是纯 Docker Compose——你的 compose 文件需要转换
- 项目更新节奏慢于 Coolify/Dokploy，但核心功能稳定
- 必须先有一个域名的通配符 DNS 指向 VPS（`*.apps.yourdomain.com`）

## 🤔 为什么这次推它给你
**Claude Code 友好度：中。** 有 CLI（`caprover deploy`）和 API，Claude Code 可以用 CLI 完成部署。但初始配置（serversetup）有交互式提示，需要人工参与一次。之后的日常部署 Claude Code 可以接管。适合"想要商店体验 + 偶尔 CLI 部署"的场景。trade-off：比 Dokku 重，比 Coolify 功能少，更新慢。

---
*由 /gitout 生成 · 2026-05-26 · intent: "一台 VPS 部署多个小网站，适合 Claude Code 操作"*
