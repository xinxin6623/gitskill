---
type: repo
repo: zcw576020095/mbti-test
domain: personality-test
status: active
discovered: 2026-05-24
last_reviewed: 2026-05-24
intent_matched: "MBTI 测试 webapp 自部署，最快上线"
signals:
  stars: 310
  last_commit: 2026-01-19
  language: Python
  license: unknown
url: https://github.com/zcw576020095/mbti-test
absorption:
  harvested: false
  used: false
  used_in: []
---

# zcw576020095/mbti-test · 小白说明书

## 🧐 这是什么
一个开箱即用的 **Django MBTI 测试系统**，登录、分页答题、自动保存、PDF 报告导出全齐。作者自己挂了在线 demo：best-mbti-test.xin。**最接近"今晚就能上线"的那种。**

## 💡 解决什么问题
- 想给自己/团队/社群部署个 MBTI 测试站，**不想从零写题库和计分**
- Python 后端比 Java 全家桶更合胃口
- 需要导出 PDF 报告（团建场景常用）

## 🎯 谁该用 / 谁别用
**适合你如果：** 会用 Python + pip + Django，目标是**一周内把站点跑起来**；想要"现成的题库 + 现成的计分 + 现成的 PDF 导出"。

**别浪费时间如果：** 你想要小程序版本（这是 Web）；想要 React/Vue 现代前端（这里是 Bootstrap + jQuery 风格 SSR）；想要 license 清晰可商用（仓库没明确写）。

## 🚀 三分钟上手
```bash
git clone https://github.com/zcw576020095/mbti-test.git
cd mbti-test
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
# 题库导入脚本（README 第 4.1 节有）
python manage.py runserver
```
浏览器打开 http://127.0.0.1:8000 直接用。

## 🔑 关键文件 / 关键概念
- `mbti/` — Django app，含模型、视图、模板
- `mbti/migrations/` — 数据库迁移
- README 第 4.1 节 — 题库初始化脚本（必跑，否则没题）
- `requirements.txt` — `reportlab` 是 PDF 可选依赖

## ⚠️ 踩坑提示
- README 是中文，但仓库没写 license，**商用前问下作者**或者别用
- SQLite 是默认存储，多人并发上线得换 PostgreSQL
- PDF 导出靠 reportlab，字体不全的服务器会出中文豆腐块

## 🤔 为什么这次推它给你

1. **命中 intent.what：** 是一个**完整、可独立部署、有在线 demo** 的 MBTI 测试 webapp——硬约束（开源+题库齐+能算 16 型）全满足。
2. **命中 soft pref：** 全中文界面 + 中文 README + 近期还在维护（2026-01-19 推过 commit）。
3. **没命中的 trade-off：** 不是小程序（你提到的"小程序"场景需另选 [[lilemy__mbti-mini]]）；前端是传统 SSR，不是 React/Vue。

---
*由 /gitout 生成 · 2026-05-24 · intent: "mbit 测试 app 或程序或网页端或小程序，现在比较流行的"*
