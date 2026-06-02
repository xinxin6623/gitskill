---
type: repo
repo: hcmhcs/screenTranslate
domain: screen-vision-assistant
status: active
discovered: 2026-05-25
last_reviewed: 2026-05-25
intent_matched: "Apple Vision 本地 OCR + Apple 本地翻译，零云调用"
signals:
  stars: 37
  last_commit: 2026-05-24
  language: Swift
  license: gpl-3.0
url: https://github.com/hcmhcs/screenTranslate
absorption:
  harvested: false
  used: false
  used_in: []
---

# ScreenTranslate · 小白说明书

## 🧐 这是什么

Swift 6 写的 Mac 屏幕翻译，**OCR 用 Apple Vision、翻译用 Apple Translation framework**，默认全在设备上跑，不联网。可选接云引擎，但开箱就能用。

## 💡 解决什么问题

- 看英文 PDF/截图，想立刻看到中文翻译
- 不能复制的截图里的字，想直接框选翻译
- 不想再装一堆翻译 app + 不想付 DeepL 订阅
- 在意隐私，不希望屏幕文字被传到第三方服务器

## 🎯 谁该用 / 谁别用

**适合你如果：**
- macOS 15+ 用户，想吃满 Apple 原生 Translation 红利
- 隐私敏感、不想为翻译开账号
- 翻译质量"够用就行"——Apple 翻译比 DeepL 稍弱，但快和私

**别浪费时间如果：**
- macOS 还在 14 或更低
- 翻译质量要顶级——上 DeepL/GPT-4 更合适
- 想要 OCR 后做"问答"而不只是翻译

## 🚀 三分钟上手

```bash
# 去 release 下 dmg
open https://github.com/hcmhcs/screenTranslate/releases/latest
# Cmd+E 框选截图翻译
# Cmd+Option+Z 选中文本翻译（不走 OCR）
# Cmd+Shift+E 弹小窗手输翻译
```

首次使用要在「系统设置 → 通用 → 语言与地区」下载离线翻译包。

## 🔑 关键文件 / 关键概念

- 三个快捷键 = 三种触发路径，按使用场景拆分
- Apple Translation framework — 系统级翻译引擎，离线包要手动下
- 可选云引擎 — 设置里能切，但默认关闭

## ⚠️ 踩坑提示

- 必须 macOS 15 (Sequoia)，老系统装不上
- 中文 ↔ 英文翻译质量 OK，小语种偏弱
- 离线翻译包不下，会静默走在线兜底
- GPL-3.0 + 同时上了 ProductHunt，作者有商业化打算，留意未来 license 变动

## 🤔 为什么这次推它给你

**最贴你"隐私优先 + 本地 OCR 不上云"**——OCR 和翻译双双本地。命中"Swift/SwiftUI 原生 + Apple Vision Framework"两条 soft preference。**trade-off：**功能比 ScreenScribe 窄（只做翻译，不接 LLM 解读），而且强依赖 macOS 15。

---
*由 /gitout 生成 · 2026-05-25 · intent: "Mac 桌面屏幕 OCR / 截图理解 / 视觉助手"*
