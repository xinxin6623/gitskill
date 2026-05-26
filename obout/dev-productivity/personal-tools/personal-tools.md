# 个人开发者生产力工具（非 AI 篇）

> 方向：covering 你列的 "skill / ide / coding / harness / 工程" 里**不依赖 AI** 的那一面。
> 故意挑跟 AI 无关的硬通货，给 AI agent / Claude Code skill / harness 这些方向作反向参照。
>
> 生成于 2026-05-23 · by `/gitout` 子 agent · 5 个入选 / ~210 个候选

## 一句话选型

| 想解决 | 推荐 | 一句话 |
|---|---|---|
| tmux 太老，要个现代多路复用器 | **tuios** | Bubble Tea + BSP + 命令面板，2.6k star |
| 别名 / Makefile 散得到处都是 | **justx** | 在 `just` 上加 TUI，全局 recipe 库 |
| 多台机器同步配置但要有差异 | **dotter** | Rust + 模板渲染 + symlink，跨平台单二进制 |
| 只想抄某个仓库的一个文件 | **ghgrab** | TUI 浏览 5 大 forge，不用 git clone |
| 想要一个有审美的终端工作台 | **term39** | 复古 DOS 风全平台 multiplexer + lockscreen |

## 健康度

- 全部 5 个项目最近一年内有 commit（最老 2026-03-23）
- 全部有 README + 多渠道安装指引（brew / cargo / pip / npm 至少其一）
- 语言分布：Rust × 3、Go × 1、Python × 1
- License：MIT × 4 + Unlicense × 1

## 入选明细

### 1. [Gaurav-Gosain/tuios](https://github.com/Gaurav-Gosain/tuios) — terminal multiplexer
- 2655 ⭐ · Go · MIT · 2026-04-13
- 卖点：vim 模态 + BSP 平铺 + 工作区 + 命令面板，Kitty 图形协议透传
- 工程参考：Charm 栈（Bubble Tea v2 + Lipgloss v2）事件驱动渲染样板
- 详见 [[dev-productivity/personal-tools/entries/Gaurav-Gosain__tuios|`entries/Gaurav-Gosain__tuios.md`]]

### 2. [fpgmaas/justx](https://github.com/fpgmaas/justx) — task runner TUI
- 162 ⭐ · Python · MIT · 2026-03-24
- 卖点：把 `just` 的 recipe 系统包成可浏览 TUI，支持全局 recipe 库
- 工程参考：在已有工具上"加 TUI 外壳"的极简思路
- 详见 [[dev-productivity/personal-tools/entries/fpgmaas__justx|`entries/fpgmaas__justx.md`]]

### 3. [SuperCuber/dotter](https://github.com/SuperCuber/dotter) — dotfile manager
- 1965 ⭐ · Rust · Unlicense · 2026-04-21
- 卖点：先渲染再 symlink 的双层设计，多 profile / 多机器差异化
- 工程参考：模块边界清晰，适合学"小工具大设计"
- 详见 [[dev-productivity/personal-tools/entries/SuperCuber__dotter|`entries/SuperCuber__dotter.md`]]

### 4. [abhixdd/ghgrab](https://github.com/abhixdd/ghgrab) — GitHub utility
- 996 ⭐ · Rust · MIT · 2026-05-20
- 卖点：跨 forge（GH/GL/Codeberg/Gitea/Forgejo）按文件 / 目录 / release 精准下载
- 工程参考：ratatui + tokio 异步 TUI 样板；npm/cargo/pip 三栈分发
- 详见 [[dev-productivity/personal-tools/entries/abhixdd__ghgrab|`entries/abhixdd__ghgrab.md`]]

### 5. [alejandroqh/term39](https://github.com/alejandroqh/term39) — retro multiplexer
- 191 ⭐ · Rust · MIT · 2026-03-23
- 卖点：MS-DOS 蓝白 + 60fps + Linux framebuffer 模式 + 跨平台 lockscreen
- 工程参考：把 GUI 思路（窗口、菜单、锁屏）整体搬进 TUI 的设计
- 详见 [[dev-productivity/personal-tools/entries/alejandroqh__term39|`entries/alejandroqh__term39.md`]]

## 为什么没有这些"老朋友"

按硬约束跳过：**fzf、zoxide、starship、ripgrep、bat、fd、tmux、yadm**。
不是它们不好，而是这些已经是事实标准，你大概率早就在用 —— 没必要再写一遍小白文档。

## 跟其他方向的关系

这份是 `/gitout` 三个方向之一：
- **个人提效（本份）**：纯手动工具，靠设计而非 AI 提速
- 另外两份在隔壁目录（AI / agent / harness 视角的工具）
- 如果你想把 justx 的"全局 recipe" 思路抄到 Claude skills 上，那就是这份与另两份的接口

---

*intent: "个人提效工具，skill ide codeing harness 工程" · /gitout · 2026-05-23*
