---
type: repo
repo: Gaurav-Gosain/tuios
domain: dev-productivity/personal-tools
status: active
discovered: 2026-05-23
last_reviewed: 2026-05-23
intent_matched: "想要一个比 tmux 更现代、能跑图、有命令面板的终端多路复用器"
signals:
  stars: 2655
  last_commit: 2026-04-13
  language: Go
  license: MIT
url: https://github.com/Gaurav-Gosain/tuios
absorption:
  harvested: false
  used: false
  used_in: []
---

# TUIOS · 小白说明书

## 🧐 这是什么
一个用 Go 写的"终端里的窗口管理器"：vim 风格模态、BSP 平铺、工作区、命令面板，全部跑在你已有的终端里。

## 💡 解决什么问题
- tmux 的快捷键太古老，配置文件像古墓壁画
- 想在终端里直接看图片（Kitty 图形协议），不用切窗口
- 想要"命令面板（Cmd+K 那种）"风格地操作 pane 和 workspace

## 🎯 谁该用 / 谁别用
**适合你如果：**
- 你已经在用 Ghostty / Kitty / WezTerm 这类支持真彩 + 图形协议的现代终端
- 你想要一套类 i3/sway 的平铺逻辑，但只在终端里用
- 你愿意为 0.x 阶段的快速迭代付出"配置可能下个版本变"的代价

**别浪费时间如果：**
- 你只在 SSH 上挂 tmux 保会话，远端是老式 xterm
- 你已经把 tmux 调到肌肉记忆了，没有真痛点
- 你需要在多人协同终端会话里共享（tmux attach 那种），TUIOS 目前不是这个定位

## 🚀 三分钟上手
```bash
brew install tuios          # macOS / Linux
# 或
go install github.com/Gaurav-Gosain/tuios/cmd/tuios@latest

tuios                       # 直接进入
# 默认 leader 类似 vim，help 按 ?
```

## 🔑 关键文件 / 关键概念
- `docs/KEYBINDINGS.md` — 全部快捷键
- `docs/BSP_TILING.md` — BSP 预选 + 切分逻辑，理解这一页就基本会用了
- `docs/SESSIONS.md` — daemon 模式 + 会话持久化（这是它真正想替代 tmux 的地方）
- 架构：Bubble Tea v2 + Lipgloss v2，事件驱动渲染，空闲 CPU 接近 0

## ⚠️ 踩坑提示
- 在不支持真彩或图形协议的终端里启动会非常难看，先确认你的终端
- 还在 0.x，配置 schema 可能变；订阅 release notes
- "命令面板"是亮点，但默认绑定与某些 tmux 配置冲突，进来先看 keybindings

## 🤔 为什么这次推它给你
你说想看"工程实践 / 架构参考"。TUIOS 的代码是 Charm 栈（Bubble Tea + Lipgloss）的优秀范本，事件驱动 + 几乎零 CPU 占用的实现，比看 tmux 的 C 代码更适合现代工程师抄思路。trade-off 是它故意不去兼容旧终端 —— 这是它能保持简单的代价。

---
*由 /gitout 生成 · 2026-05-23 · intent: "个人提效工具，skill ide codeing harness 工程"*
