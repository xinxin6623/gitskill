---
type: repo
repo: xushengfeng/eSearch
domain: screen-vision-assistant
status: active
discovered: 2026-05-25
last_reviewed: 2026-05-25
intent_matched: "截屏 + 离线 OCR + 翻译 + 屏幕搜索 全家桶"
signals:
  stars: 6403
  last_commit: 2026-05-22
  language: TypeScript
  license: gpl-3.0
url: https://github.com/xushengfeng/eSearch
absorption:
  harvested: false
  used: false
  used_in: []
---

# eSearch · 小白说明书

## 🧐 这是什么

中文作者写的「锤子大爆炸 + 小米传送门」开源复刻，把**截屏、离线 OCR、屏幕翻译、以图搜图、贴图、滚动截屏、录屏**塞到一个 Electron 应用里，三平台通吃。

## 💡 解决什么问题

- 想截图但还想顺手把图里的字抠出来
- 想截图后立刻拿去 Google / 百度搜
- 老板会议屏幕共享外文 PPT，框一下当场翻译
- 网页超长内容截不下，要滚动截屏拼一张
- 想把某块区域"贴"在屏幕上当便签

## 🎯 谁该用 / 谁别用

**适合你如果：**
- 一个工具就想搞定截图相关的所有事
- 接受 Electron 的内存开销，换功能密度
- 喜欢中文文档和中文作者持续维护

**别浪费时间如果：**
- 你已经在用 CleanShot / Shottr，eSearch 替代不了它们的细节体验
- 严苛挑剔原生体验、嫌 Electron 笨重
- 想要 LLM 多模态问答，eSearch 不接 GPT/Claude

## 🚀 三分钟上手

```bash
# Mac 暂时没 Homebrew，去 release 下 dmg
open https://github.com/xushengfeng/eSearch/releases/latest
# 默认快捷键 Alt+C 唤起截屏
```

## 🔑 关键文件 / 关键概念

- 离线 OCR — 内置 PaddleOCR/Tesseract 模型，不需联网
- 框选后自动执行 — 在设置里可以配"框完直接 OCR / 直接翻译 / 直接搜"流水线
- 贴图 — 截完的图能"钉"在桌面上当浮动便签
- 滚动截屏 — 横向竖向都行，识别页面变化拼接

## ⚠️ 踩坑提示

- Mac 上没有 Homebrew cask，每次升级要手动下 dmg
- Electron 应用，常驻内存 200~400MB，电池党慎用
- 默认快捷键 Alt+C 和某些输入法冲突，记得自定义
- GPL-3.0，闭源商用要小心

## 🤔 为什么这次推它给你

命中"开源 + Mac + 离线 OCR + 不上云"四条硬约束，且**功能广度第一名**——你说不清自己到底要 OCR 还是翻译还是搜索时，先装它一个全有了。**trade-off：**违反 soft preference 里"原生不友好（Electron 笨重）"——所以它是"全家桶 vs 原生"的 trade-off 代表，配合上面 TRex 形成"轻 vs 重"两极。

---
*由 /gitout 生成 · 2026-05-25 · intent: "Mac 桌面屏幕 OCR / 截图理解 / 视觉助手"*
