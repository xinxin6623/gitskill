---
type: repo
repo: alejandroqh/term39
domain: dev-productivity/personal-tools
status: active
discovered: 2026-05-23
last_reviewed: 2026-05-23
intent_matched: "想要一个有审美趣味的、跨平台的、自带 lockscreen 和系统菜单的终端工作台"
signals:
  stars: 191
  last_commit: 2026-03-23
  language: Rust
  license: MIT
url: https://github.com/alejandroqh/term39
absorption:
  harvested: false
  used: false
  used_in: []
---

# TERM39 · 小白说明书

## 🧐 这是什么
一个 Rust 写的"复古 MS-DOS 风格"终端多路复用器：蓝白配色、box-drawing 字符、~60fps 渲染，全屏接管你的终端，提供窗口、剪贴板、系统菜单、锁屏、命令面板。

## 💡 解决什么问题
- 你的终端审美已经到极限了，想看点"不一样的"
- 你需要跨平台（Linux / macOS / Windows / 各种 BSD / Termux）用同一套窗口操作逻辑
- 你想在 Linux TTY（没有 X / Wayland）下也能拖拽窗口、用鼠标
- 你需要一个能自带 lockscreen（PAM / macOS Directory Service / Windows Security）的"伪桌面"

## 🎯 谁该用 / 谁别用
**适合你如果：**
- 你是 retrocomputing 爱好者 / 想要复古主题（Amber、Green Phosphor、QBasic 主题都有）
- 你在裸 Linux 服务器上花大量时间，希望那也有"窗口管理 + 锁屏"
- 你想看一份"用 Rust + raw input device 做出像 GUI 的 TUI"的工程参考

**别浪费时间如果：**
- 你要的是会议演示用的优雅现代终端（看 TUIOS）
- 你只是想要 tmux 那种简单的会话保持，不需要"虚拟桌面"这一整套
- 你不在意视觉，只在意工作流（你会觉得它"花架子"）

## 🚀 三分钟上手
```bash
cargo install term39        # crates.io 发行
term39                      # 直接启动，全屏接管
term39 --theme amber        # 琥珀色显像管风
term39 --ascii              # 在不支持 box-drawing 的老终端上 fallback
```

## 🔑 关键文件 / 关键概念
- 主题：`--theme classic|dark|monochrome|green|amber|qbasic|...`（十几种）
- Linux 独有：`--fb` 直接走 `/dev/fb0`，连终端模拟器都不要
- 命令面板：`Ctrl+Space`；锁屏：`Shift+Q`
- 后台 daemon 在 Unix 上保会话（disconnect 后窗口还在）

## ⚠️ 踩坑提示
- "全屏接管"意味着它会蒙住你的 shell 提示符，按 `Ctrl+Alt+Q` 或菜单退出
- Linux framebuffer 模式需要 console 权限，普通用户可能要加入 `video` 组
- 锁屏功能依赖系统认证，macOS 上要授权 Directory Services 权限，第一次会被系统拦

## 🤔 为什么这次推它给你
你列了 "skill / ide / coding / harness / 工程" 这一串，说明你在收集"提效工具的工程参考"。Term39 的有趣之处是它把"GUI 思路（窗口、菜单栏、锁屏）整体搬进 TUI"，这种跨越式抽象在它的代码里组织得相当清楚，是看"用 Rust 做交互密集型 TUI"的好范本。trade-off：审美强烈，不是中性工具——你要么爱它，要么觉得它太花。

---
*由 /gitout 生成 · 2026-05-23 · intent: "个人提效工具，skill ide codeing harness 工程"*
