---
type: repo
repo: abhixdd/ghgrab
domain: dev-productivity/personal-tools
status: active
discovered: 2026-05-23
last_reviewed: 2026-05-23
intent_matched: "不想为了一个 README 或一个 docker-compose.yml 去 git clone 整个仓库"
signals:
  stars: 996
  last_commit: 2026-05-20
  language: Rust
  license: MIT
url: https://github.com/abhixdd/ghgrab
absorption:
  harvested: false
  used: false
  used_in: []
---

# ghgrab · 小白说明书

## 🧐 这是什么
一个用 Rust + ratatui 写的 TUI 工具，让你在终端里浏览 GitHub / GitLab / Codeberg / Gitea / Forgejo 仓库的目录树，挑出**某一个文件或目录**单独下载，不用 `git clone` 整个仓库。

## 💡 解决什么问题
- "我只想看一下他们家的 docker-compose.yml" → 现在不用 clone 再 rm 了
- 在网速慢的地方拉 50 MB 仓库只为了 200 字节的脚本
- 想批量下载某个文件夹（dotfiles 仓库里的某个子目录），但 GitHub 网页不支持
- 想抓 release 二进制，但又不想去 Releases 页面点
- 自己搭了 Gitea / Forgejo，希望也能用同一工具

## 🎯 谁该用 / 谁别用
**适合你如果：**
- 你经常"参考别人项目里的某个文件"（GitHub Actions workflow、shell function）
- 你需要从公司自托管的 Gitea / Forgejo 拉东西，但他们不给你完整 git 凭证
- 你想从 release 页拉跟当前系统匹配的二进制（它会自动按 OS/arch 过滤）

**别浪费时间如果：**
- 你下载的目的是要继续维护这个仓库（那你需要的就是 `git clone`）
- 你只用 GitHub 一家，且 `gh repo view` 已经够用
- 你不喜欢 TUI，想要 GUI

## 🚀 三分钟上手
```bash
cargo install ghgrab        # 推荐
# 或 npm i -g @ghgrab/ghgrab
# 或 pipx install ghgrab    # 三种发行渠道都有

ghgrab                       # 进入 TUI，输入 owner/repo
ghgrab rel cli/cli           # 直接下载最新 release，自动匹配你的 OS/arch
ghgrab cli/cli docs/         # 抓整个 docs 目录
```

## 🔑 关键文件 / 关键概念
- 配置在 `~/.config/ghgrab/`，可加 token 提升 rate limit
- 主要模式：浏览模式（默认）、release 模式（`rel`）、批量模式（多选 + 一次性下载）
- 对大文件透明支持 GitHub LFS（不用额外装 lfs 客户端）

## ⚠️ 踩坑提示
- 不带 GitHub token 时 rate limit 60/h，搜索几次就触顶；建议先配 PAT
- 自托管 Gitea/Forgejo 要在配置文件里写实例 URL
- TUI 内的 fuzzy search 是仓库内的目录搜索，不是 GitHub 全站搜索

## 🤔 为什么这次推它给你
你在做"知识沉淀 / 工程参考"。ghgrab 把"看别人代码片段"这件事的成本从"clone + rm"降到"两次回车"，对个人提效是真实的杠杆。trade-off：它故意不做 git 操作，所以拿下来的文件没有 git 历史 —— 这是它能轻量到分发到 npm/cargo/pip 三个渠道的原因。

---
*由 /gitout 生成 · 2026-05-23 · intent: "个人提效工具，skill ide codeing harness 工程"*
