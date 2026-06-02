---
type: repo
repo: amebalabs/TRex
domain: screen-vision-assistant
status: active
discovered: 2026-05-25
last_reviewed: 2026-05-25
intent_matched: "Mac 屏幕选区 OCR 到剪贴板"
signals:
  stars: 1812
  last_commit: 2026-02-13
  language: Swift
  license: mit
url: https://github.com/amebalabs/TRex
absorption:
  harvested: false
  used: false
  used_in: []
---

# TRex · 小白说明书

## 🧐 这是什么

Mac 菜单栏里的小恐龙，按个快捷键框一块屏幕，文字就到剪贴板了。**全程离线、没 UI、不上云**，纯 Swift + Apple Vision 写的极简 OCR 工具。

## 💡 解决什么问题

- 看 PDF 文字不能选？框一下，到手了
- YouTube 视频里有句话想引用？框一下
- Zoom 同事在共享屏幕讲幻灯片？框一下
- 二维码懒得用手机扫？也能识别（条码也行）

## 🎯 谁该用 / 谁别用

**适合你如果：**
- 只想要"按下快捷键 → 选区 → 文字到剪贴板"这一件事，不要任何花活
- 在意隐私，全离线、不上云
- 偶尔也想从 QR 码读 URL

**别浪费时间如果：**
- 想要 AI 加持的"截图后让 LLM 解释这是啥"——TRex 只识字，不理解
- 想做屏幕翻译——TRex 不带翻译
- 想后台监控屏幕做记忆——TRex 是被动触发，不会自己截

## 🚀 三分钟上手

```bash
brew install --cask trex
# 启动后菜单栏出现小恐龙，去偏好设置绑全局快捷键，比如 ⌘⇧2
```

CLI 也能跑：

```bash
/Applications/TRex.app/Contents/MacOS/cli/trex
```

## 🔑 关键文件 / 关键概念

- 菜单栏图标 — 唯一 UI 入口
- 全局快捷键 — 真正用它的入口
- `trex://capture` URL scheme — 可被 Shortcuts、Alfred、Raycast 串联
- 自定义词表 — 提高人名/术语识别率

## ⚠️ 踩坑提示

- App Store 版本是付费的，GitHub Release 和 Homebrew 是免费的（同代码）
- 首次启动要给"屏幕录制"权限，不给就只能截到壁纸
- 识别中日韩文要在偏好里手动切语言，默认只开英文

## 🤔 为什么这次推它给你

命中你"Mac + 开源 + 本地 OCR 不上云"三条硬约束，soft preference 里"Apple Vision Framework"也完全吻合。**trade-off：**它就是个老老实实的 OCR，不接 LLM、不做问答交互——所以放在 5 个推荐里它代表"最纯粹的 OCR 基线"，跟下面带 AI 的几个形成对照。1.8k 星 + 2026 年还在更新，稳。

---
*由 /gitout 生成 · 2026-05-25 · intent: "Mac 桌面屏幕 OCR / 截图理解 / 视觉助手"*
