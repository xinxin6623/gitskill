---
type: repo
repo: dianyike/claude-code-insights
domain: claude-skills
status: active
discovered: 2026-05-26
last_reviewed: 2026-05-26
intent_matched: "中文社群对 mattpocock skills 的本地化和方法论解读"
signals:
  stars: 54
  last_commit: 2026-04-22
  language: Markdown
  license: MIT
url: https://github.com/dianyike/claude-code-insights
absorption:
  harvested: false
  used: false
  used_in: []
---

# dianyike/claude-code-insights · 小白说明书

## 🧐 这是什么
台湾接案工程师 dianyike（典億創研工作室）整理的"中文社群最完整 Claude Code 进阶指南"。三大块：CLAUDE.md 架构论、Skills 写作论、Subagent 编排论，外加把 mattpocock skills 改成中文 + 加 Gotchas 段的实战范例。

## 💡 解决什么问题
- 看不懂 mattpocock 英文 skill 哲学 → 中文重写并解读
- 不知道 CLAUDE.md / Skill / Subagent 啥时候用哪个 → 决策矩阵直给
- 想自己写 skill 不知道 frontmatter 怎么填 → 详细字段参考
- 写完 skill 不知道好不好用 → `skill-eval-toolkit` 量化评测

## 🎯 谁该用 / 谁别用
**适合你如果：**
- 中文母语，想系统学 Claude Code 进阶（CLAUDE.md / Skill / Subagent 三件套）
- 想看别人怎么把 mattpocock 的 skill 改造本地化（加 `templates/` / `reference/` / Gotchas）
- 接案/独立开发者，单人单仓多项目 workflow

**别浪费时间如果：**
- 你只想要直接装来用的 skill 集合（这是方法论库，不是 plugin marketplace）
- 你已经熟 mattpocock 那一套了（重复度高，主要价值在中文化）
- 你不写 skill，只是用现成的（直接装 mattpocock 即可）

## 🚀 三分钟上手
```bash
git clone https://github.com/dianyike/claude-code-insights.git
# 先读三大指南
open claude-md-best-practices.md
open skills-best-practices.md
open subagent-best-practices.md
# 范例可直接复制到 .claude/skills/
cp -r examples/grill-me ~/.claude/skills/
cp -r examples/write-prd ~/.claude/skills/
cp -r examples/tdd ~/.claude/skills/
```

## 🔑 关键文件 / 关键概念
- `claude-md-best-practices.md` — 三层架构：Enforcement / High-Frequency Recall / On-Demand Reference
- `skills-best-practices.md` — Skill 触发词写法、Gotchas 迭代法、Hub-and-Spoke 架构
- `subagent-best-practices.md` — Subagent "黑盒问题"和解法
- `examples/grill-me` / `write-prd` / `tdd` / `prd-to-plan` — mattpocock 改造版（加 Gotchas）
- `examples/write-a-skill` + `examples/skill-eval-toolkit` — 写 skill + 量化评测的元 skill
- `examples/rules` — 6 文件的 `.claude/rules/` starter，含 pragmatism layer

## ⚠️ 踩坑提示
- 部分链接 TODO 没填完（README 里 `<!-- TODO -->` 注释还在）
- 范例 skill 是 mattpocock 改造版，跟原版有差异，混装可能冲突
- 繁体中文版（README.zh-TW.md）才是作者母语版，简体是机翻
- "Gotchas Are the Soul of a Skill" 这观点很重要，但作者只在 skills-best-practices.md §4.3 一笔带过，要自己挖

## 🤔 为什么这次推它给你

1. **命中 intent.what：** 你提到的 `/grill-me` `/improve-codebase-architecture` 都源自 mattpocock，这库给了你**中文方法论 + 改造范本**，比直接读英文 README 上手快
2. **命中 soft pref：** 你是中文母语 + 维护着 gitskill 这种 skill 实验场，这库的"Gotchas 迭代法 + skill-eval-toolkit"对你写自己的 skill 直接可借鉴
3. **没命中的 trade-off：** 只 54 stars，影响力小、社群验证少；如果你要"跟着大家用"应该看 mattpocock 原版，这库的价值在**方法论密度**而非热度

---
*由 /gitout 生成 · 2026-05-26 · intent: "mattpocock/skills + aihero.dev + Claude Code skill 集合"*
