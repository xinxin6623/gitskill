---
type: repo
repo: ComposioHQ/awesome-claude-skills
domain: claude-skills
status: active
discovered: 2026-05-26
last_reviewed: 2026-05-26
intent_matched: "头部 awesome list — Claude Code skill 全景索引"
signals:
  stars: 61797
  last_commit: 2026-05-22
  language: Markdown
  license: Apache-2.0
url: https://github.com/ComposioHQ/awesome-claude-skills
absorption:
  harvested: false
  used: false
  used_in: []
---

# ComposioHQ/awesome-claude-skills · 小白说明书

## 🧐 这是什么
Composio（500+ 应用 OAuth 中间层公司）维护的 Claude Skill 全景 awesome list，号称 1000+ skill 和 plugin，覆盖 Claude.ai / Claude Code / Codex / Cursor / Gemini CLI / Antigravity 等多家 agent。同名 awesome 库一搜一大把（travisvn / karanb192 / yibie 都有同名仓），但这家是社区 stars 最高、维护最活跃的。

## 💡 解决什么问题
- 不知道有哪些 skill 可用 → 一份索引看到底
- 想让 Claude 真去发邮件 / 建 issue / 发 Slack 而不只是生成文本 → `connect-apps` plugin 接 500+ 应用
- 在多家 agent 之间迁移 skill → 这库的索引按多 agent 兼容性标注
- 想了解 skill 生态全貌再决定深挖哪个 → 这种导航 list 适合开路

## 🎯 谁该用 / 谁别用
**适合你如果：**
- skill 圈新人，需要一份索引建立全景认知
- 想让 Claude 不止生成文本而是真去操作外部 SaaS（Composio 集成）
- 不想被单一作者的口味绑定，想看跨派别的 skill

**别浪费时间如果：**
- 你已经知道要装哪个 skill（直接去那个 repo 就行）
- 你不想 Composio 商业化绑定（connect-apps 要 Composio API key）
- 你只关心代码工程类 skill（这库覆盖太广，工程类占比反而小）

## 🚀 三分钟上手
```bash
# 看 README 索引就够了
git clone https://github.com/ComposioHQ/awesome-claude-skills.git
open awesome-claude-skills/README.md

# 想用 Composio 的 500+ 应用连接：
claude --plugin-dir ./connect-apps-plugin
/connect-apps:setup
# 粘贴 dashboard.composio.dev 的免费 API key
```

## 🔑 关键文件 / 关键概念
- `README.md` — 主索引，按场景分类（Document / Dev / Business / Creative …）
- `connect/` — Composio connect-apps plugin 源码，500+ 应用 OAuth 一站式
- 各类别下的外链 — 实际 skill 不在这库，是指针索引

## ⚠️ 踩坑提示
- 是 awesome list，不是 plugin marketplace——`/plugin install` 装不了，只能照着链接去原 repo 装
- "1000+ skill"水分要看：很多是重复列同一个 skill 的不同变体
- connect-apps 走 Composio 商业服务，免费额度够个人用，团队/企业要付费
- 同名 awesome 仓有十几个分叉（karanb192/travisvn/JayZeeDesign/yibie 等），选这家因为活跃度最高，但内容跟其他 awesome 仓有大量重叠

## 🤔 为什么这次推它给你

1. **命中 intent.what：** 你不止要"知名开发者的 skill"还要"社区 skill 库" —— 这是社群索引的当下最优解，一站看全
2. **命中 soft pref：** 6 万 stars + 本周还有更新 + 大公司背书（Composio），活跃度和权威性都顶
3. **没命中的 trade-off：** 是导航不是仓库本身，深度上不如直接看 mattpocock / trailofbits；且 connect-apps 是 Composio 的商业入口，纯粹的开源洁癖党可能不喜欢

---
*由 /gitout 生成 · 2026-05-26 · intent: "mattpocock/skills + aihero.dev + Claude Code skill 集合"*
