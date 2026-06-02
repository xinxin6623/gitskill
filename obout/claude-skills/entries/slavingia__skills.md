---
type: repo
repo: slavingia/skills
domain: claude-skills
status: active
discovered: 2026-05-26
last_reviewed: 2026-05-26
intent_matched: "知名创业者维护的 Claude Code skill 集合（非工程方向）"
signals:
  stars: 8858
  last_commit: 2026-04-14
  language: Markdown
  license: MIT
url: https://github.com/slavingia/skills
absorption:
  harvested: false
  used: false
  used_in: []
---

# slavingia/skills · 小白说明书

## 🧐 这是什么
Gumroad 创始人 Sahil Lavingia 把自己畅销书《The Minimalist Entrepreneur》提炼成 10 个 Claude Code skill。从"找到你的社群"到"定价"到"可持续增长"，把一本极简主义创业方法论变成了 10 条可调用的 slash command。

## 💡 解决什么问题
- 有创业想法但不知道下一步该干啥 → 10 个 skill 对应创业 10 个阶段
- 跟 AI 聊创业话题它老说套话 → 这套 skill 让它按 Sahil 的极简方法论回答
- 想读完《The Minimalist Entrepreneur》但没空 → 把书的决策框架直接装进 Claude

## 🎯 谁该用 / 谁别用
**适合你如果：**
- 独立开发者 / 想做 micro-SaaS / 一人公司
- 喜欢 Sahil Lavingia / 37signals 这一派"反 VC、反规模化"的极简风
- 想看头部创业者怎么把"思维框架"工程化成 skill 而不是工程类 skill

**别浪费时间如果：**
- 你找的是写代码/调架构的 skill（这套完全不沾代码）
- 你做的是 VC 路线、要快速规模化（方法论相反）
- 你没读过《The Minimalist Entrepreneur》且不打算读（skill 是书的浓缩，缺背景看不出深度）

## 🚀 三分钟上手
```text
# 在 Claude Code 里
/plugin marketplace add slavingia/skills
/plugin install minimalist-entrepreneur
# 装完直接用
/find-community         # 找你的目标人群
/validate-idea          # 验证想法
/mvp                    # 第一版产品范围
/first-customers        # 找前 100 客户
/pricing                # 定价
/minimalist-review      # 任何决策来一次"极简主义体检"
```

## 🔑 关键文件 / 关键概念
- `/find-community` — 找社群（创业起点）
- `/validate-idea` — 验证问题是否值得解
- `/mvp` + `/processize` — 先手动交付再产品化
- `/first-customers` — 一对一拿到前 100 客户
- `/pricing` + `/marketing-plan` + `/grow-sustainably` — 定价、营销、可持续增长
- `/company-values` — 文化和招聘
- `/minimalist-review` — 万能"极简体检"，任何决策都来一发

## ⚠️ 踩坑提示
- 10 个 skill 跟书的章节严格对齐，不读书直接用会觉得"道理我都懂但不知道怎么用"
- 全英文，且包含 Sahil 个人语境（"build the house you want to live in" 等），翻译损失大
- 没有代码相关 skill，跟 mattpocock / trailofbits 完全不冲突，可以并存
- 4 月以后没新 commit，可能 Sahil 已经发完就不维护了

## 🤔 为什么这次推它给你

1. **命中 intent.what：** 你要"知名开发者的 skill 集合"——Sahil Lavingia 是 Gumroad 创始人 + 畅销书作者，知名度对得起
2. **命中 soft pref：** 给你看了"skill 不只能做工程"这个完全不同的方向——把方法论书变成可执行 slash command，对你设计 skill 有启发
3. **没命中的 trade-off：** 跟你 gitskill 仓库主要服务的"工程/AI/工具"方向不一样，主要是开阔视野；真要拿来用你得先认同 Sahil 那套极简主义价值观

---
*由 /gitout 生成 · 2026-05-26 · intent: "mattpocock/skills + aihero.dev + Claude Code skill 集合"*
