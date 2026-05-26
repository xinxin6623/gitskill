---
type: repo
repo: TheCraigHewitt/skills
domain: claude-skills
status: active
discovered: 2026-05-26
last_reviewed: 2026-05-26
intent_matched: "在 mattpocock skills 之上做了自动化闭环的工作流套件"
signals:
  stars: 104
  last_commit: 2026-05-24
  language: Markdown
  license: MIT
url: https://github.com/TheCraigHewitt/skills
absorption:
  harvested: false
  used: false
  used_in: []
---

# TheCraigHewitt/skills · 小白说明书

## 🧐 这是什么
Craig Hewitt（创业者/营销人）把 mattpocock 的 `/grill-me` `/write-a-prd` `/prd-to-issues` 当地基，再补上 `/shape`（一键生成 PRD）和 `/ralph`（自主跑 TDD + code review）形成闭环。除了 coding 套件，还附赠 47 个 CEO / 销售 / YouTube / Cowork 场景 skill。

## 💡 解决什么问题
- mattpocock 的 PRD 流程需要你逐条回答 `/grill-me`，太慢 → `/shape` 自答 + 流式输出
- PRD 拆成 issue 后还得人工一个个跑 → `/ralph` 接力把 issue 一条条跑完
- 工程之外想用 Claude 干销售/营销/YouTube 内容 → 47 个非工程 skill 一并给你

## 🎯 谁该用 / 谁别用
**适合你如果：**
- 用过 mattpocock 那套但嫌 PRD 流程慢，想看自动化版
- 想看 `/ralph` 这种"autonomous coding loop"怎么落地（Docker sandbox 可选）
- 创业者 / 一人公司 / Solo dev，要工程 + 销售 + 营销 + YouTube 一篮子

**别浪费时间如果：**
- 你完全不用 mattpocock 那套（`/shape` `/ralph` 设计前提是兼容它的 PRD 格式）
- 你不信任"AI 自动跑 issue 到完成"（人不在场容易出事）
- 你只要工程 skill（CEO / sales / YouTube 那 47 个对你是噪音）

## 🚀 三分钟上手
```bash
# 全装
npx skills@latest add TheCraigHewitt/skills --full-depth

# 只装 coding 闭环（推荐入门）
npx skills@latest add TheCraigHewitt/skills/coding

# coding 套件依赖 mattpocock 的 grill-me / write-a-prd / prd-to-issues
npx skills@latest add mattpocock/skills -s grill-me
npx skills@latest add mattpocock/skills -s write-a-prd
npx skills@latest add mattpocock/skills -s prd-to-issues
```

## 🔑 关键文件 / 关键概念
- `coding/shape/` — 自动版 grill-me + write-a-prd，一步出 PRD
- `coding/ralph/` — Autonomous loop：拿 GitHub issue → TDD → code review → 下一条
- `ceo/` — 10 个 CEO 决策 skill（含 `strategic-sparring`）
- `sales/` — 21 个销售流程 skill
- `youtube/` — 15 个 YouTube 内容创作 skill
- `cowork/` — 16 个 Claude Cowork 协作 skill

## ⚠️ 踩坑提示
- `/ralph` 默认人在场，要全自主必须配 Docker sandbox（README 有指南），别在裸机直接跑
- `/shape` 自答的 PRD 质量取决于你的项目上下文够不够丰富——空项目跑出来是套话
- 跟 mattpocock 的 PRD 格式严格绑定，未来 mattpocock 改格式这里会断
- 非工程 skill（ceo/sales/youtube）和工程 skill 共享触发词可能误触发，按类别分开装更稳

## 🤔 为什么这次推它给你

1. **命中 intent.what：** 你看到 mattpocock 三个 skill 想了解周边，这是直接构建在它上面的二次创作，看二次创作能反推原版的能力边界
2. **命中 soft pref：** 跨工程和业务两端，让你看到 skill 怎么从"工具"升级成"工作流闭环"
3. **没命中的 trade-off：** 只 104 stars，社群验证少；且 `/ralph` 这种 autonomous loop 实战风险不低，作者本人没出过事故复盘——你要先小项目试

---
*由 /gitout 生成 · 2026-05-26 · intent: "mattpocock/skills + aihero.dev + Claude Code skill 集合"*
