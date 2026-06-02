---
type: repo
repo: charmbracelet/soft-serve
domain: git-self-host
status: active
discovered: 2026-05-26
last_reviewed: 2026-05-26
intent_matched: "极简自托管 Git 服务器，单二进制，省内存"
signals:
  stars: 6939
  last_commit: 2026-05-19
  language: Go
  license: MIT
url: https://github.com/charmbracelet/soft-serve
absorption:
  harvested: false
  used: false
  used_in: []
---

# Soft Serve · 小白说明书

## 🧐 这是什么

Charm 出品的"命令行版 GitHub"。一个 Go 二进制，跑起来就是个 SSH Git server，自带一个**通过 SSH 访问的 TUI**（用 ssh 命令直接在终端里翻仓库、看文件、加语法高亮）。完全没有 Web UI，全靠 SSH 玩。

## 💡 解决什么问题

- 你只想要"放代码 + push/pull"的 Git server，不想要 Gitea 那一坨 issue/wiki/CI
- 想给自己的 dotfiles、博客源码、私有脚本找个家，4G 服务器还要留资源跑别的应用
- 喜欢命令行胜过浏览器（`ssh git.your-server.com` 直接进 TUI 翻仓库）

## 🎯 谁该用 / 谁别用

**适合你如果：**
- 个人单兵作战，仓库 < 30 个
- 资源敏感（soft-serve 启动占内存只有几十 MB）
- 准备配合 git hooks 写自动部署脚本（"网站 push 上线"刚好用得上）

**别浪费时间如果：**
- 需要 Web UI 给协作者用（同事不一定愿意背 SSH key 来翻仓库）
- 想要 PR / Issue / Code Review 流程
- 不会写 `post-receive` 钩子，又指望开箱即用的 CI/CD

## 🚀 三分钟上手

```bash
# Mac/Linux 安装
brew install charmbracelet/tap/soft-serve

# 服务器后台跑
soft serve &

# 本地：把 ~/.ssh/id_ed25519.pub 加进 admin（首次连接者自动成 admin）
ssh -p 23231 your-server.com

# 在 TUI 里建仓库，或本地直接 push 建：
git remote add origin ssh://your-server.com:23231/my-blog
git push -u origin main
```

## 🔑 关键文件 / 关键概念

- `~/.soft-serve/` — 服务器端数据目录（仓库、配置、key 都在这）
- **SSH-only**：不开 80/443 端口，只听 23231 SSH——攻击面小但你也别指望浏览器访问
- **post-receive hook**：在仓库的 `hooks/` 里写脚本，比如 push 后自动 `rsync` 到 nginx web root，**这就是你"git 管理网站"的最小实现**
- `soft serve` vs `soft browse` — 前者起服务器，后者在本地翻仓库 TUI

## ⚠️ 踩坑提示

- **没有 Web UI** 是设计取舍不是 bug——非要 UI 就上 Gitea
- 默认端口 23231，记得在火山云安全组放行（别开 22 跟系统 SSH 抢）
- 第一个连进来的 SSH key 自动是 admin——**别让陌生人在你启动后第一个连上**，建议启动前先 `soft serve --initial-admin-keys ~/.ssh/your_key.pub`

## 🤔 为什么这次推它给你

1. **命中 intent.what：** 你既想"自建 Git 仓库"又强调"网站发布"——soft-serve 的 post-receive hook 是最干净的实现：push 上来直接 rsync 到 nginx 目录，零依赖、零中间件。
2. **命中 soft pref：** 单 Go 二进制 + 几十 MB 内存占用，4C4G 服务器还能省 3.5G 干别的事。
3. **没命中的 trade-off：** 没有 Web UI 也没有 mirror 功能——如果你的核心诉求是"国内拉 GitHub 依赖"，soft-serve 帮不上，得用 Gitea；soft-serve 只适合你"私人代码 + push 部署"这一条线。

---
*由 /gitout 生成 · 2026-05-26 · intent: "搜索git仓库自建相关项目，国内拉依赖+管理个人网站，4C4G 火山云"*
