---
type: repo
repo: MskTmi/MBTI
domain: personality-test
status: active
discovered: 2026-05-24
last_reviewed: 2026-05-24
intent_matched: "MBTI 测试静态 webapp，零部署"
signals:
  stars: 161
  last_commit: 2026-04-11
  language: JavaScript
  license: unknown
url: https://github.com/MskTmi/MBTI
absorption:
  harvested: false
  used: false
  used_in: []
---

# MskTmi/MBTI · 小白说明书

## 🧐 这是什么
**纯静态 HTML/JS 的中文 MBTI 93 题测试**。fork 自更早的 `5songHb/mbti`（那个 2015 年就停了），这个版本翻新过、demo 还活着：mbti.msktmi.com。

## 💡 解决什么问题
- 想要一个**今晚 5 分钟就能挂到 Cloudflare Pages / Vercel / GitHub Pages** 的 MBTI 测试页
- 不想碰任何后端、数据库、Python/Java 环境
- 中文 93 题版本（比常见 28 题简化版严肃）

## 🎯 谁该用 / 谁别用
**适合你如果：** 你要的就是个**前端纯静态**展示页，挂个域名给朋友/社群玩；不需要存用户数据；接受"刷新即清空"。

**别浪费时间如果：** 想要用户注册/历史结果保存；要做小程序（这是 H5）；要做严肃的心理学研究（93 题版精度有限）。

## 🚀 三分钟上手
```bash
git clone https://github.com/MskTmi/MBTI.git
cd MBTI
# 双击 index.html 就能跑
# 或者：
python3 -m http.server 8000
```
部署：把整个目录推到 Cloudflare Pages / Vercel / GitHub Pages 即可。

## 🔑 关键文件 / 关键概念
- `index.html` — 入口页
- `js/` — 题目数据 + 计分逻辑（要改题就改这里）
- `css/` — 样式

## ⚠️ 踩坑提示
- 仓库**没写 license**，自己挂 demo 玩没事，要做商业产品先问作者
- 纯前端实现意味着**作弊很容易**（刷新、F12 改答案都行），别用于正式测评
- 93 题不是科学版，是流行版

## 🤔 为什么这次推它给你

1. **命中 intent.what：** 是"现在还活着的、能立刻挂上线"的 MBTI 测试 webapp 中最轻的——硬约束全满足且部署成本接近 0。
2. **命中 soft pref：** 全中文题库 + 中文 UI + 2026 年还在更新。
3. **没命中的 trade-off：** 没有后端意味着**不能存结果、不能多人统计**——团建后想看数据汇总得另外想办法。

---
*由 /gitout 生成 · 2026-05-24 · intent: "mbit 测试 app 或程序或网页端或小程序，现在比较流行的"*
