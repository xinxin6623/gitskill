---
type: repo
repo: go-gitea/gitea
domain: git-self-host
status: active
discovered: 2026-05-26
last_reviewed: 2026-05-26
intent_matched: "自托管 Git 平台，支持镜像同步国外仓库做依赖代理"
signals:
  stars: 55916
  last_commit: 2026-05-26
  language: Go
  license: MIT
url: https://github.com/go-gitea/gitea
absorption:
  harvested: false
  used: false
  used_in: []
---

# Gitea · 小白说明书

## 🧐 这是什么

自托管 Git 平台的事实标准。可以理解为"GitHub 的开源单机版"——单个 Go 二进制，跑起来就是个完整网站：仓库、PR、issue、wiki、CI/CD、包仓库全都有。Gogs 的 fork，但已经把原版甩开很远。

## 💡 解决什么问题

- 国内 `git clone github.com/xxx` 慢/断——你在 Gitea 上开 mirror，它定时帮你同步，你 clone 自己服务器秒速到位。
- 公司/个人想要 GitHub 的体验但代码不能放公网——内网部署 Gitea，权限可控。
- 想自己玩 PR / Code Review 工作流，但又不想被 GitHub 政策牵着走。

## 🎯 谁该用 / 谁别用

**适合你如果：**
- 4C4G 火山云想跑个像样的代码托管 + 国外依赖镜像中继
- 团队 1-50 人都合适（百人级也能扛）
- 想顺便有 Container Registry / npm / PyPI / Maven 私服（Gitea 自带 Packages 功能）

**别浪费时间如果：**
- 只是个人放几个项目 + 不想看 Web UI（那 soft-serve 单文件更香）
- 想要 GitLab 那种完整 DevOps 闭环（Gitea Actions 还在追赶 GitLab CI）
- 服务器 < 1GB 内存（启动占 200MB 左右，并发起来 1G 起步保险）

## 🚀 三分钟上手

```bash
# Docker Compose 一把梭
mkdir gitea && cd gitea
cat > docker-compose.yml <<'EOF'
version: "3"
services:
  gitea:
    image: gitea/gitea:latest
    ports: ["3000:3000", "2222:22"]
    volumes:
      - ./data:/data
    restart: always
EOF
docker compose up -d
# 浏览器开 http://your-server:3000 走安装向导
```

镜像 GitHub 仓库的姿势：新建仓库 → 选"Migrate" → 填 GitHub URL → 勾"Mirror" → 它就定时帮你拉。

## 🔑 关键文件 / 关键概念

- `app.ini` — Gitea 全局配置（`/data/gitea/conf/app.ini`），改 SSH 端口、DB、邮件都在这
- **Mirror 仓库** — 国内拉依赖的核心姿势：把上游 GitHub 仓库做成 mirror，本地用你的 Gitea URL
- **Packages** — 自带 Container/npm/PyPI/Maven 私服，配合 mirror 等于一站式依赖中转
- **Actions** — Gitea 自带 CI（兼容 GitHub Actions YAML 语法），可以触发 webhook 自动部署你的网站

## ⚠️ 踩坑提示

- **SSH 端口冲突**：默认 Gitea SSH 端口 22 会撞系统 SSH，要么改成 2222（如示例），要么用 Gitea 内置 SSH server
- 数据库默认 SQLite 没问题，但**超过 50 个仓库 / 100 用户上 PostgreSQL**，否则锁表
- Mirror 拉国外仓库**仍然吃你服务器的出口带宽**——不是魔法，只是把"你 clone 慢"变成"服务器拉一次大家都快"
- 4G 内存够用，但**别同时开 Actions runner + Indexer + Elasticsearch**，会爆

## 🤔 为什么这次推它给你

1. **命中 intent.what：** 你想"自建 Git 仓库 + 国内拉依赖"——Gitea 的 Mirror 功能就是为这个场景设计的，目前没有更标准的方案。
2. **命中 soft pref：** 单 Go 二进制、Docker 一行起、4C4G 跑得动、有完整中文文档和国内社区。
3. **没命中的 trade-off：** 比 piku 重得多，启动就吃 200MB 内存——如果你只想要"git push 推网站"不要 Web UI，soft-serve 更省资源。另外，Forgejo（Gitea 的社区分叉）也值得关注，但主仓在 Codeberg.org 不在 GitHub 上。

---
*由 /gitout 生成 · 2026-05-26 · intent: "搜索git仓库自建相关项目，国内拉依赖+管理个人网站，4C4G 火山云"*
