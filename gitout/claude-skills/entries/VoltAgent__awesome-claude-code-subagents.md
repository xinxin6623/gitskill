---
type: repo
repo: VoltAgent/awesome-claude-code-subagents
domain: misc
status: active
decision: harvest
discovered: 2026-05-22
last_reviewed: 2026-05-22
theme: claude-skills
intent_matched: "131+ 专业 subagent 集合，按职业角色组织"
signals:
  stars: 20329
  last_commit: 2026-05-22
  language: Shell
  license: MIT
url: https://github.com/VoltAgent/awesome-claude-code-subagents
absorption:
  harvested: false
  used: false
  used_in: []
---

# Awesome Claude Code Subagents · 小白说明书

## 🧐 这是什么

**131+ 个职业角色化的 subagent 集合**。每个 subagent 是一个专门干某事的 Claude——比如"Rust 专家"、"Kubernetes 运维"、"代码 reviewer"、"安全 audit"。可以直接通过 plugin marketplace 安装：`claude plugin install voltagent-lang`。

VoltAgent 团队同时维护 awesome-agent-skills、awesome-openclaw-skills、AI Agent Papers 等多个生态合集。20k 星，MIT。

## 💡 解决什么问题

Claude Code 主对话用一个 model 干所有事情有缺点：

- 上下文一长就乱
- 用通用 Claude 改专业代码不如领域专家 prompt
- 想让 Claude "切换角色"很麻烦

Subagent 机制让你**把任务委托给"专门的 Claude"**——它们有独立 context window、专属 system prompt、独立工具白名单。这个 repo 就是"131 个职业角色的 system prompt 模板库"。

## 🎯 谁该用 / 谁别用

**适合你如果：**
- 经常做跨领域工作（前端 + 后端 + DevOps）
- 想用 Claude marketplace 一键装专家
- 自己写 subagent 想看好范本

**别浪费时间如果：**
- 单一领域开发，通用 Claude 已经够用
- 嫌 subagent 切换成本高
- 不熟 subagent 机制（先看 disler/hooks-mastery）

## 🚀 三分钟上手

```bash
# 加 marketplace
claude plugin marketplace add VoltAgent/awesome-claude-code-subagents

# 装某类专家
claude plugin install voltagent-lang     # 各语言专家
claude plugin install voltagent-infra    # 基建 / DevOps
claude plugin install voltagent-meta     # orchestration 协调

# 然后在 Claude Code 里 @<subagent-name> 就能调
```

## 🔑 关键文件 / 关键概念

- **plugin marketplace 模式** — Claude Code 新出的发布渠道，比手动 clone 友好
- **categories/** — 按职业大类分组（Lang / Infra / Security / Meta）
- **voltagent-meta** — 协调多个 subagent 的"调度专家"
- **subagent.md 模板** — 看任何一个都是好 system prompt 教材

## ⚠️ 踩坑提示

- subagent 多了会乱，按需装别贪多
- 自家的 voltagent-meta 推荐配合其他 category 用
- 都是英文 prompt，中文场景效果可能略降

## 🤔 为什么这次推它给你

**最实用的"现成专家库"**。你做 OpenClaw 或者日常开发都用得上。**重点学的不是单个 agent 写得多好，而是"目录组织 + plugin marketplace 发布方式"**——你以后想把 gitout / mem 推出去，可以走同样的渠道。pattern 候选：`subagent-by-role-categorization`、`plugin-marketplace-distribution`。

---
*由 /gitout 生成 · 2026-05-22 · theme: Claude Code Skill / hooks*
