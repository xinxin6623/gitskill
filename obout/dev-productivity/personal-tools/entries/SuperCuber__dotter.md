---
type: repo
repo: SuperCuber/dotter
domain: dev-productivity/personal-tools
status: active
discovered: 2026-05-23
last_reviewed: 2026-05-23
intent_matched: "跨机器同步 dotfiles，但每台机器要有不同变量（颜色、主屏 vs 笔记本）"
signals:
  stars: 1965
  last_commit: 2026-04-21
  language: Rust
  license: Unlicense
url: https://github.com/SuperCuber/dotter
absorption:
  harvested: false
  used: false
  used_in: []
---

# Dotter · 小白说明书

## 🧐 这是什么
用 Rust 写的 dotfile 管理器 + 模板引擎。它的核心招式：不直接 symlink 原文件，而是先把原文件当 Handlebars 模板渲染出"机器特定的副本"，再 symlink 副本。

## 💡 解决什么问题
- 用 `ln -s` 同步 dotfiles 时，台式机和笔记本配置经常需要二选一改文件
- GNU Stow 不支持模板，每次开新机要手工 patch
- 想要"有变量、有 profile、有 pre/post hook"，但不想引入 Ansible 那种重武器

## 🎯 谁该用 / 谁别用
**适合你如果：**
- 你有 2 台以上工作机，且配置只有少量差异（壁纸、字号、电池组件开关）
- 你能接受写一个 `global.toml` 描述"哪些文件去哪里 + 哪些变量"
- 你欣赏 Rust 单二进制 + crates.io 部署

**别浪费时间如果：**
- 你只有一台机器，根本没有"多 profile"需求
- 你已经用 chezmoi 用得很顺（chezmoi 是同赛道更主流的选项）
- 你不想学 Handlebars 模板语法

## 🚀 三分钟上手
```bash
brew install dotter         # macOS
# 或 cargo install dotter

cd ~/dotfiles               # 已有的 dotfiles 仓库
dotter init                 # 自动生成 global.toml + local.toml
dotter deploy               # 渲染 + symlink
dotter -d deploy            # dry-run，先看 diff
```

## 🔑 关键文件 / 关键概念
- `.dotter/global.toml` — 所有机器共享：哪些包 / 哪些文件 / 默认变量
- `.dotter/local.toml` — 当前机器特定：激活哪些包 + 覆盖变量
- `.dotter/cache/` — 渲染后的实际副本，symlink 指过去
- `pre_deploy.sh` / `post_deploy.sh` — 部署前后 hook
- `dotter watch` — 监听变化自动 redeploy，开发配置时很顺手

## ⚠️ 踩坑提示
- 第一次 deploy 会覆盖现有 dotfile，先 dry-run `-d` 或备份
- 模板里的变量在 `local.toml` 里覆盖，不在 `global.toml`，新手常搞反
- 跟 chezmoi 的最大区别：dotter 只做"模板 + symlink"，不做"远程同步加密"那一套；想要 GPG 加密看 toml-bombadil

## 🤔 为什么这次推它给你
你想看"工程参考"。Dotter 的代码量适中（Rust，不到一万行），配置 / 渲染 / cache / hook 这一套是典型的"小工具但模块边界清晰"的样板，适合抄设计。trade-off：模板能力没有 Ansible 那么强，但这也是它能保持"零依赖单二进制"的原因。

---
*由 /gitout 生成 · 2026-05-23 · intent: "个人提效工具，skill ide codeing harness 工程"*
