---
type: repo
repo: piku/piku
domain: git-self-host
status: active
discovered: 2026-05-26
last_reviewed: 2026-05-26
intent_matched: "git push 部署个人网站到自己服务器"
signals:
  stars: 6586
  last_commit: 2026-05-20
  language: Python
  license: MIT
url: https://github.com/piku/piku
absorption:
  harvested: false
  used: false
  used_in: []
---

# Piku · 小白说明书

## 🧐 这是什么

最小的 PaaS。你只要 `git push piku master`，它就把你的网站/应用跑起来——nginx + uwsgi + SSL（Let's Encrypt 自动续）全帮你配好。本质上是把 Heroku 的核心体验压成一个 Python 脚本塞进你的 VPS。

## 💡 解决什么问题

- 你想"代码一推就上线"，但不想为了这个去学 Docker、Kubernetes、Jenkins。
- 你想在火山云 4C4G 上同时跑几个网站，每个一个域名，自动 HTTPS。
- 你不想花钱买 Vercel/Netlify，更不想被它们的免费额度卡脖子。

## 🎯 谁该用 / 谁别用

**适合你如果：**
- 服务器配置不高（256MB 树莓派都能跑，4G 是奢侈）
- 想要 Heroku 体验但又是国内服务器
- 部署的东西是 Python / Node / Go / 静态站点（这正是你"个人网站"的典型形态）

**别浪费时间如果：**
- 你只是想要个代码仓库，不需要部署（那看 Gitea / soft-serve）
- 你的应用必须用 Docker（piku 是裸进程派，不跑容器）
- 团队 ≥5 人需要权限管理（piku 是单用户 PaaS）

## 🚀 三分钟上手

```bash
# 在火山云服务器上一行装好
curl https://piku.github.io/get | sh

# 本地：把你的网站项目加个 piku remote
cd ~/my-blog
git remote add piku piku@your-server.com:my-blog
git push piku master
# 它会自动检测语言、装依赖、起 nginx，访问 my-blog.your-server.com 就上线了
```

## 🔑 关键文件 / 关键概念

- `Procfile` — 写一行 `web: python app.py` 告诉 piku 怎么启动你的应用（照搬 Heroku 格式）
- `ENV` — 环境变量 + nginx 配置都放这里（虚拟主机、静态路径、缓存规则）
- `~/.piku/` — 服务器端 piku 自己的家，所有应用都在这下面
- `app:scale web=2` — 通过 SSH 远程命令调进程数，不用改代码

## ⚠️ 踩坑提示

- 走的是 SSH，所以**你本地的 SSH 公钥要先 `piku setup:ssh ~/.ssh/id_rsa.pub` 加到服务器**，否则 git push 会一直被拒
- nginx 配置改不开心？看 `ENV` 文件里 `NGINX_*` 系列变量，能覆盖大部分场景
- 国内 Let's Encrypt 偶尔触发限速，准备好 Cloudflare DNS-01 验证或 acme.sh 兜底

## 🤔 为什么这次推它给你

1. **命中 intent.what：** 你说"用 git 管理个人发布的网站"——piku 就是把这句话翻译成一条命令的项目，`git push` = 部署。
2. **命中 soft pref：** 4C4G 火山云对它来说是"豪华配置"——它本来就是给 ARM 板子设计的，所以你不用担心吃完内存。
3. **没命中的 trade-off：** 它只解决你"网站部署"的一半，不是 Git 服务器本体——如果你还想要 GitHub 那样的网页 UI 浏览仓库/提 issue/管理多个项目，得再装 Gitea，或者直接看 soft-serve（更轻）。

---
*由 /gitout 生成 · 2026-05-26 · intent: "搜索git仓库自建相关项目，国内拉依赖+管理个人网站，4C4G 火山云"*
