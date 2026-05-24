---
type: repo
repo: SamuelZ12/screen-scribe
domain: screen-vision-assistant
status: active
discovered: 2026-05-25
last_reviewed: 2026-05-25
intent_matched: "截图 → Apple Vision OCR + Gemini 多模态解读 → Markdown/LaTeX"
signals:
  stars: 86
  last_commit: 2026-03-13
  language: Swift
  license: mit
url: https://github.com/SamuelZ12/screen-scribe
absorption:
  harvested: false
  used: false
  used_in: []
---

# ScreenScribe · 小白说明书

## 🧐 这是什么

菜单栏 Mac app，截一块屏后让 **Apple Vision 出文字、Gemini 出"看图说话"**。内置 LaTeX 公式识别、Markdown 提取，还能自定义 prompt——本质是给视觉 LLM 当一个截图前端。

## 💡 解决什么问题

- 看论文截一段公式，自动转 LaTeX 代码
- 截一段图文混排的页面，自动转干净 Markdown
- 想让 LLM 解读「这张图在讲什么」，但又不想打开浏览器贴图
- 想自己写 prompt 做特定任务（比如「把表格转成 csv」）

## 🎯 谁该用 / 谁别用

**适合你如果：**
- 写论文 / 写技术博客，经常要把图里公式或表格搬下来
- 想要"截图 + 多模态 LLM"的最短路径，不想折腾 API
- 接受用 Google Gemini（有免费额度）

**别浪费时间如果：**
- 想要完全本地、不联网——它的 AI 部分必须走 Gemini API
- 想接 OpenAI/Claude——目前锁死 Gemini
- 只要 OCR 不要 AI——直接装 TRex 更简单

## 🚀 三分钟上手

```bash
# 去 release 下 dmg
open https://github.com/SamuelZ12/screen-scribe/releases/latest
# 启动后菜单栏出现，去 Settings 贴 Gemini API key
# 全局快捷键截屏 → 选 prompt → 结果到剪贴板
```

去 [Google AI Studio](https://makersuite.google.com/app/apikey) 拿免费 key。

## 🔑 关键文件 / 关键概念

- Built-in prompts：LaTeX、Markdown 开箱即用
- 自定义 prompt — 可以写「把图里的代码原样抠出来 + 加注释」之类
- Per-prompt output 格式 — 每条 prompt 单独配换行/空格策略
- Default prompt — 设默认后一键直出，省一次选择

## ⚠️ 踩坑提示

- 必须 macOS 14 (Sonoma) 以上
- Gemini 免费额度有 RPM 限制，频繁用会被限流
- 默认 prompt 用 Gemini Flash，复杂表格建议换 Pro
- API key 存在 Keychain，但要手动每台机器各贴一次

## 🤔 为什么这次推它给你

它是这次推荐里**唯一一个把 Apple Vision OCR 和 LLM 多模态打包到位**的——命中你"支持 LLM 多模态"软偏好。**trade-off：**违反你"本地 OCR 不上云"中的「不上云」——OCR 离线但 AI 解读走 Gemini。所以它代表"OCR 本地 + LLM 远端"的混合派，跟下面纯本地的 screen-watcher 形成对照。

---
*由 /gitout 生成 · 2026-05-25 · intent: "Mac 桌面屏幕 OCR / 截图理解 / 视觉助手"*
