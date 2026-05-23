---
type: repo
repo: alirezarezvani/claude-code-skill-factory
domain: dev-productivity/claude-workflow
status: active
discovered: 2026-05-23
last_reviewed: 2026-05-23
intent_matched: "把 skill / agent / hook / slash command 当成产品来批量生产的工程脚手架"
signals:
  stars: 782
  last_commit: 2025-11-12
  language: Python
  license: MIT
url: https://github.com/alirezarezvani/claude-code-skill-factory
absorption:
  harvested: false
  used: false
  used_in: []
---

# Claude Code Skill Factory · 小白说明书

## 🧐 这是什么
一个把"做 skill / agent / hook / slash command"当成流水线作业的脚手架。你说一句"我要建个 skill"，它通过一组 interactive guide agent 用 4-5 个问题问你，然后自动吐出符合 Anthropic 规范的 SKILL.md / agent 定义 / hook 脚本 / ZIP 包。

## 💡 解决什么问题
- 你想给 Claude Code 加能力，但每次都得手写 YAML frontmatter、规范化 SKILL.md、配 hook 事件、补 bash 权限——重复劳动多
- 团队里 skill 风格不统一，没人愿意维护"skill 标准"
- 想做 hook，但又怕写错事件类型把环境搞炸

## 🎯 谁该用 / 谁别用
**适合你如果：**
- 你已经在用 Claude Code，想批量产 skill 而不是手写每一个
- 你想看 skill / agent / hook 的"参考实现"长啥样
- 你想给团队定一个 skill 生产规范

**别浪费时间如果：**
- 你只用过一次 Claude Code，连 skill 是什么都没搞清——先用官方文档
- 你想要 SDK 级别的程序化生成（这个偏自然语言交互）
- 你讨厌"用 Claude 生成 Claude 配置"这种套娃感

## 🚀 三分钟上手
```bash
git clone https://github.com/alirezarezvani/claude-code-skill-factory
cd claude-code-skill-factory
# 把 .claude/ 复制到你的项目或全局
cp -r .claude/skills ~/.claude/
cp -r .claude/agents ~/.claude/
# 在 Claude Code 里
/build skill            # 走交互式 skill 生成
```

## 🔑 关键文件 / 关键概念
- `documentation/templates/SKILLS_FACTORY_PROMPT.md` — 真正的 skill 生成 mega-prompt，照抄就能学
- `documentation/templates/HOOKS_FACTORY_PROMPT.md` — hook 工厂的 prompt，含 7 种事件类型 + 安全校验逻辑
- `documentation/templates/AGENTS_FACTORY_PROMPT.md` — agent YAML frontmatter 标准（tools/model/color/expertise）
- `generated-skills/prompt-factory/` — 一个 ready-to-use 的 skill 示例，含 69 个 preset
- `/build` / `/validate-output` / `/install-skill` — 4 层验证 + 自动 ZIP + 一键安装

## ⚠️ 踩坑提示
- "Factory" 思路是用 LLM 生成 LLM 配置，prompt 质量决定 skill 质量，不是傻瓜机
- 生成出来的 hook 自带安全校验，但你最好 `--dry-run` 看一眼再装
- 仓库 push 时间是 2025-11，没在持续高频更新，遇到 Claude Code 新事件类型可能要自己改 prompt

## 🤔 为什么这次推它给你
你想看"skill ide coding harness 工程"。这个仓库不是 awesome 链接堆，是 5 条产线（skill / agent / prompt / hook / slash）的 prompt + 模板 + 验证脚本，**把"做 Claude Code 配置"本身工程化了**。你抄完它的 SKILLS_FACTORY_PROMPT.md，就有了自己的 skill 生产规范。trade-off：偏个人/小团队，不是 SDK 级。

---
*由 /gitout 生成 · 2026-05-23 · intent: "个人提效工具，skill ide codeing harness 工程"*
