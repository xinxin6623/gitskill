---
type: repo
repo: dokku/dokku
domain: server-ops
status: active
discovered: 2026-05-26
last_reviewed: 2026-05-26
intent_matched: "一台 VPS CLI 部署多个小站，适合 Claude Code 操作"
signals:
  stars: 31903
  last_commit: 2026-05-26
  language: Shell
  license: MIT
url: https://github.com/dokku/dokku
absorption:
  harvested: false
  used: false
  used_in: []
---

# Dokku · 小白说明书

## 🧐 这是什么
最小的自托管 PaaS——你可以把它理解成"在你自己 VPS 上跑的 mini Heroku"。纯 CLI 操作，`git push` 就部署，没有 Web 界面的心智负担。

## 💡 解决什么问题
- 你有一台 VPS 想跑 2-3 个独立站，但不想每次手动配 Nginx + SSL + Docker
- 你想用 Claude Code 一条命令就完成"建站 → 绑域名 → 拿 SSL → 上线"全流程
- 你受够了每次部署都要 SSH 上去手动操作

## 🎯 谁该用 / 谁别用
**适合你如果：**
- 你习惯命令行，或者让 Claude Code 帮你敲命令
- 你就一台小 VPS（1-2GB 内存就够）
- 你想要 Heroku 式的 `git push` 部署体验

**别浪费时间如果：**
- 你完全不想碰终端，只想点 Web UI
- 你需要多机集群 / 高可用
- 你的应用强依赖 Docker Compose 编排多容器

## 🚀 三分钟上手
```bash
# 在 VPS 上安装 Dokku
wget -NP . https://dokku.com/bootstrap.sh
sudo DOKKU_TAG=v0.35.15 bash bootstrap.sh

# 创建应用
dokku apps:create my-blog

# 绑域名 + 自动 SSL
dokku domains:add my-blog blog.example.com
dokku letsencrypt:enable my-blog

# 本地 git push 部署
git remote add dokku dokku@your-vps:my-blog
git push dokku main
```

## 🔑 关键文件 / 关键概念
- `Procfile` — 告诉 Dokku 怎么启动你的应用（和 Heroku 一样）
- `dokku apps:*` — 应用生命周期全在这组命令里
- `dokku proxy:*` — 内置 Nginx 反代，自动按域名分流
- 插件机制 — `dokku-letsencrypt`、`dokku-postgres` 等按需装

## ⚠️ 踩坑提示
- 默认用 Herokuish buildpack 检测语言，如果你的项目结构非标准可能识别失败——建议加 `Dockerfile`
- 多容器应用（如前端+后端+数据库）得拆成多个 Dokku app，不支持 docker-compose 式编排
- 内存 512MB 的 VPS 跑 2 个 app 会吃力，建议至少 1GB

## 🤔 为什么这次推它给你
**Claude Code 友好度：极高。** 所有操作都是 bash 命令，没有任何 GUI 依赖。Claude Code 可以直接：`dokku apps:create`、`dokku domains:add`、`dokku letsencrypt:enable`、`git push` 完成全流程。对于"一台 VPS 跑 2-3 个小站"这个场景，Dokku 是最轻量、最 CLI 原生的选择。trade-off 是没有 Web UI——如果你偶尔想鼠标点点看状态，它不提供。

---
*由 /gitout 生成 · 2026-05-26 · intent: "一台 VPS 部署多个小网站，适合 Claude Code 操作"*
