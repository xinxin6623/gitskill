---
type: repo
repo: karlicoss/HPI
domain: misc
status: active
decision: harvest
discovered: 2026-05-22
last_reviewed: 2026-05-22
theme: im-export
intent_matched: "个人数据统一编程接口（社交/健康/笔记全部 Python import）"
signals:
  stars: 1606
  last_commit: 2026-05-22
  language: Python
  license: MIT
url: https://github.com/karlicoss/HPI
absorption:
  harvested: false
  used: false
  used_in: []
---

# HPI (Human Programming Interface) · 小白说明书

## 🧐 这是什么

karlicoss 多年构建的**"我的人生作为 Python 包"项目**。HPI 是 `my` 这个 Python 包的代号——把你的社交网络帖子、阅读历史、annotations、todos、健康数据（睡眠/运动/心率）、位置、照片、浏览历史、聊天记录全部统一成"导入即用"的 Python 对象。

代码示例：
```python
import my.reddit.all
from collections import Counter
Counter(s.subreddit for s in my.reddit.all.saved()).most_common(4)
# → ('orgmode', 62), ('emacs', 60), ...
```

把"我的生活数据"变成"导入即用的 Python 数据"。1.6k 星，MIT，作者博客 beepb00p.xyz 是个人数据信徒圣经。

## 💡 解决什么问题

你的数据散落在 N 个地方：

- 微信、iMessage、Discord、Twitter、Reddit、Gmail
- Fitbit、Apple Health、Strava
- Pocket、Kindle、Hypothesis
- Org-mode、Obsidian、Notion

**每个平台的导出格式都不一样**，要做任何跨平台分析都要先解析半天。HPI 把所有这些数据源做成统一 Python 模块——每个模块自己处理"找数据 / 解析 / 缓存 / 错误处理"，你只关心 `import my.x` 就好。

## 🎯 谁该用 / 谁别用

**适合你如果：**
- 你信"数字痕迹是身份的一部分"（extended mind 理念）
- Python 用户做个人数据分析
- 想长期建设"个人数据中枢"，不是一次性导出

**别浪费时间如果：**
- 不愿意定期手动维护数据导出 pipeline
- 嫌 org-mode + Python 生态太极客
- 只想一次导出走人

## 🚀 三分钟上手

```bash
pip install HPI
# 或 git clone + pip install -e .

# 配每个模块，比如 reddit
# 见 doc/MODULES.org

# 然后
python -c "import my.reddit.all; print(len(list(my.reddit.all.saved())))"
```

每个 module 都有独立 SETUP 文档，配置粒度细。

## 🔑 关键文件 / 关键概念

- **`my/`** 包 — 所有数据访问入口
- **每个 module 一个数据源** — `my.reddit`、`my.twitter`、`my.imessage` 等
- **org-mode 文档驱动** — 作者用 org-mode 写所有文档（可能要装插件预览）
- **缓存层（cachew）** — 慢解析自动缓存到本地

## ⚠️ 踩坑提示

- 设置成本高，每个 module 要配数据源路径
- 文档大部分是 .org 不是 .md，GitHub 预览不完美
- 作者本人风格强烈，可能要适应

## 🤔 为什么这次推它给你

**你做 weixinjilu 的"终极想法版"**。你导出微信记录之后呢？放进什么系统？HPI 给的答案是：**把它当成"my.wechat" 模块，跟 my.reddit / my.imessage 平起平坐，统一 Python 接口**。这套理念可以指导你长期方向。pattern 候选：`personal-data-as-python-package`、`module-per-data-source`、`extended-mind-as-codebase`。

---
*由 /gitout 生成 · 2026-05-22 · theme: 聊天记录 / 个人数据遗产化*
