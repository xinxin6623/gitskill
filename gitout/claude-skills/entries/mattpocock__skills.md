---
type: repo
repo: mattpocock/skills
domain: claude-skills
status: active
discovered: 2026-05-26
last_reviewed: 2026-05-26
intent_matched: "知名开发者维护的 Claude Code skill 集合"
signals:
  stars: 105366
  last_commit: 2026-05-20
  language: Markdown
  license: MIT
url: https://github.com/mattpocock/skills
absorption:
  harvested: false
  used: false
  used_in: []
---

# mattpocock/skills · 小白说明书

## 🧐 这是什么
Matt Pocock（Total TypeScript 创始人）从自己 `.claude/` 目录里掏出来的一整套 skill，专门给"真做工程"而不是"vibe coding"的人用。10 万+ stars 不是白来的——这是当下 Claude Code skill 圈最有影响力的单库。

## 💡 解决什么问题
- Agent 没干你想要的事 → `/grill-me` 在动手前逼它问清楚
- Agent 啰嗦得要命 → `/grill-with-docs` 帮你和 agent 建立 `CONTEXT.md` 共享术语
- 代码跑不起来 → `/tdd` 红绿重构 + `/diagnose` 标准排错环
- 代码越改越烂 → `/improve-codebase-architecture` 每隔几天救一次"屎山"

## 🎯 谁该用 / 谁别用
**适合你如果：**
- 想用 Claude Code 做真实项目，不是写玩具 demo
- 受不了 BMAD / Spec-Kit 那种"流程吃掉你"的重型方法
- 愿意花 10 分钟读完 README 再用（每个 skill 都有设计哲学）

**别浪费时间如果：**
- 你想要"装上就 10x"的银弹（这套需要你配合 `/grill-me` 认真思考）
- 你的项目不需要 PRD / ADR / 架构关怀（小脚本用不上）
- 你抗拒英文 skill 文档（虽然有 [vinvcn/mattpocock-skills-zh-CN](https://github.com/vinvcn/mattpocock-skills-zh-CN) 中文版可选）

## 🚀 三分钟上手
```bash
npx skills@latest add mattpocock/skills
# 选 skills 时务必勾上 /setup-matt-pocock-skills
# 装完在 Claude Code 里跑一次
/setup-matt-pocock-skills
# 它会问你：用啥 issue tracker、triage 用啥 label、文档放哪
```

## 🔑 关键文件 / 关键概念
- `skills/engineering/grill-me/` — 最招牌的"逼问"skill，每次改动前先跑
- `skills/engineering/grill-with-docs/` — 增强版，顺带建 `CONTEXT.md` + ADR
- `skills/engineering/tdd/` — 红绿重构循环，反 vibe coding
- `skills/engineering/improve-codebase-architecture/` — 救屎山，每周跑一次
- `skills/engineering/zoom-out/` — 让 agent 跳出当前函数看全局
- `skills/engineering/to-prd/` + `to-issues/` — 把对话凝成 PRD 再拆成 issue

## ⚠️ 踩坑提示
- **必须先跑 `/setup-matt-pocock-skills`**，否则 triage / to-issues 等 skill 没配置不工作
- `/grill-me` 第一次用会觉得"问得也太细了"，但这就是设计——别跳过
- skill 之间有依赖链：to-prd → to-issues → tdd，单独用某一个效果折扣
- 跟 `CONTEXT.md` 强绑定，没建这文档很多 skill 收益减半

## 🤔 为什么这次推它给你

1. **命中 intent.what：** 你看到的 `/tad`（应为 `/tdd`）、`/improve-codebase-architecture`、`/grill-me` 三个 skill 的源头就是这里——一站锁定
2. **命中 soft pref：** Matt Pocock 是 TypeScript 圈头牌讲师 + aihero.dev 创办人，知名度和文档质量你想要的都给了
3. **没命中的 trade-off：** 这是单作者口味强烈的工程派 skill，业务/营销/创作类没有；想要那些得另外组合 TheCraigHewitt 或 alirezarezvani

---
*由 /gitout 生成 · 2026-05-26 · intent: "mattpocock/skills + aihero.dev + Claude Code skill 集合"*
