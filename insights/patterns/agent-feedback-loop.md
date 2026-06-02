---
type: pattern
name: agent-feedback-loop
sources:
  - gitout/dev-productivity/claude-workflow/entries/BayramAnnakov__claude-reflect.md
  - gitout/dev-productivity/claude-workflow/entries/parcadei__Continuous-Claude-v3.md
status: draft
created: 2026-05-30
last_reviewed: 2026-05-30
---

# Agent Feedback Loop（自学习反馈回路）

## 问题

Claude Code 每次会话是独立的，之前的纠错/偏好/项目上下文在 session 切换时丢失。用户反复纠正同一个问题，token 浪费在"重新教"上。

## 上下文

AI coding agent 的上下文窗口有限，session 间无状态。用户的纠错行为（"不是这样，是那样"）是最有价值的知识沉淀机会，但手动整理 CLAUDE.md 不持续、容易遗漏。

## 方案

建立**"纠错 → 确认 → 沉淀"**反馈回路：

```
用户纠错 → hook 捕获 correction → 队列暂存
                           ↓
用户跑 /reflect → 人工确认 → 写入 CLAUDE.md / skill
                           ↓
                    跨 session 扫描 → 发现重复 pattern → 自动提议 new skill
```

关键设计点：
- **Hook 拦截**：在 conversation 事件中捕获用户的否定/纠正语气
- **人工在环**：correction 入队但不自动写入，`/reflect` 命令让人确认
- **跨 session 挖掘**：扫描历史找出重复 3+ 次的同类操作，提议做成 slash command

## 已知实例

- [[gitout/dev-productivity/claude-workflow/entries/BayramAnnakov__claude-reflect.md|claude-reflect]] — correction hook + `/reflect` 命令 + cross-session 扫描
- [[gitout/dev-productivity/claude-workflow/entries/parcadei__Continuous-Claude-v3.md|Continuous-Claude-v3]] — 自学习 harness，109 skill + 32 agent + 30 hook 的完整样板

## 变体 / 取舍

- **轻量版（claude-reflect）**：只关注 correction → CLAUDE.md，适合个人使用
- **重型版（Continuous-Claude-v3）**：全栈 harness，适合团队/项目级工程化
- **手工版**：定期人工整理 CLAUDE.md，适合低频使用

## 相关模式

- [[insights/patterns/skill-factory-pipeline.md]]（待创建）— 批量生成/维护 skill 的流水线

---

*由 [[insights/INDEX.md]] 管理 · pattern 模板 v1*
