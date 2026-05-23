---
type: repo
repo: fpgmaas/justx
domain: dev-productivity/personal-tools
status: active
discovered: 2026-05-23
last_reviewed: 2026-05-23
intent_matched: "把零散的 shell 别名 / Makefile / 脚本统一为带 TUI 的命令库"
signals:
  stars: 162
  last_commit: 2026-03-24
  language: Python
  license: MIT
url: https://github.com/fpgmaas/justx
absorption:
  harvested: false
  used: false
  used_in: []
---

# justx · 小白说明书

## 🧐 这是什么
一个建在 `just`（现代 Make 替代品）之上的 TUI 命令启动器：把你所有的 recipe 列成可浏览的面板，箭头键选择，回车执行。

## 💡 解决什么问题
- 你写了一堆 alias / shell function / Makefile target，一周后自己都想不起来名字
- `just --list` 输出在长 justfile 上不好看，没法预览参数
- 你想在不同项目、不同机器之间复用"通用 recipe"（git 工作流、docker 命令、ssh 跳板）

## 🎯 谁该用 / 谁别用
**适合你如果：**
- 已经在用 `just`，或者愿意从 Makefile 迁过来
- 你希望"全局 recipe + 项目本地 recipe"自动合并显示
- 你喜欢 textual TUI 的视觉风格

**别浪费时间如果：**
- 你完全不信任 just（坚持 Makefile）
- 你的工作流就是 fzf + zsh function，已经够用
- 你要的是图形 GUI 启动器（Alfred / Raycast）

## 🚀 三分钟上手
```bash
uv tool install justx        # 推荐，需要 uv
# 或 pip install justx
# 前置：先装 just（brew install just）

justx init --download-examples   # 初始化 ~/.justx 并下载示例 recipe
justx                            # 启动 TUI
```

## 🔑 关键文件 / 关键概念
- `~/.justx/*.just` — 全局 recipe，从任何目录都能调用
- 当前目录的 `justfile` — 局部 recipe，自动并入 TUI
- `justx run -g docker:shell my-image` — 跳过 TUI 直接执行命名 recipe
- 设计取舍：它**不**重新发明任务运行器，只在 just 之上加 TUI

## ⚠️ 踩坑提示
- 必须先装 `just` 二进制，justx 自身不带
- 全局 recipe 路径是 `~/.justx`，跟 `just` 的全局 justfile 不是同一个东西，看文档
- recipe 参数现在还只能在执行时输入，不支持 TUI 内交互式表单

## 🤔 为什么这次推它给你
你说要"skill / harness / 工程"。justx 是把"任务运行器"这个老概念再往前推一步：从 CLI 命令变成可发现、可分组、可全局共享的 recipe 库 —— 这正是 Claude Code skills、Makefile target、shell alias 这一族想解决但解决得都不彻底的事。trade-off：还小众（< 200 stars），但代码量小，自己 fork 改也不难。

---
*由 /gitout 生成 · 2026-05-23 · intent: "个人提效工具，skill ide codeing harness 工程"*
