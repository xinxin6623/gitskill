---
type: synthesis
topic: 个人产品起点
created: 2026-05-30
domains:
  - gitout/personal-site/
  - gitout/claude-skills/
  - gitout/server-ops/
status: draft
---

# 个人产品起点 · 跨域洞见

## 背景

想搭"个人品牌"——个人网站 + AI 辅助工作流 + 服务器部署——但不知道从哪开始。跨越三个 domain 的最小可行组合。

## 涉及 domain 一览

| Domain | 核心贡献 | 局限 |
|--------|---------|------|
| [[gitout/personal-site/README.md\|personal-site]] | 博客/项目/Now 页模板，Next.js/Hugo 可选 | 一旦选模板换起来麻烦 |
| [[gitout/claude-skills/README.md\|claude-skills]] | 让 Claude Code 变成个人生产力助手 | 部分 skill 质量参差；需 Claude Code 环境 |
| [[gitout/server-ops/README.md\|server-ops]] | 一台 VPS 跑多站 + SSL + 反代 | 面板选型纠结（Coolify vs Dokploy vs 1Panel） |

## 综合结论

1. **digital-garden 是个人站最优起点**：Next.js + 博客/项目/Now 三合一，改一个文件就能发布
2. **awesome-claude-code 是 skill 入口**：从 44.5k 星的索引里挑 3-5 个高频 skill 起步
3. **Dokku 是部署首选**：100% CLI、git push 就上线、Claude Code 可以全程操作
4. 三者合起来 = 个人站 → AI 辅助 → 自动部署，全链路

## 推荐路径

1. [[gitout/personal-site/entries/thedevdavid__digital-garden.md|digital-garden]] 建站（1 天）
2. [[gitout/claude-skills/entries/hesreallyhim__awesome-claude-code.md|awesome-claude-code]] 挑 skill（1 小时）
3. [[gitout/server-ops/entries/dokku__dokku.md|Dokku]] 部署到 VPS（1 天）

## 更新历史

- 2026-05-30：初稿
