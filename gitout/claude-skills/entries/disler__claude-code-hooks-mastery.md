---
type: repo
repo: disler/claude-code-hooks-mastery
domain: misc
status: active
decision: harvest
discovered: 2026-05-22
last_reviewed: 2026-05-22
theme: claude-skills
intent_matched: "Claude Code Hooks 完整教学（13 个生命周期事件全示例）"
signals:
  stars: 3700
  last_commit: 2026-05-22
  language: Python
  license: unknown
url: https://github.com/disler/claude-code-hooks-mastery
absorption:
  harvested: false
  used: false
  used_in: []
---

# Claude Code Hooks Mastery · 小白说明书

## 🧐 这是什么

**学 Claude Code Hooks 的"教科书项目"**。作者 disler 把 Claude Code 全部 13 个 hook 生命周期事件（SessionStart / PreToolUse / PostToolUse / UserPromptSubmit / SessionEnd 等）每个都做了可运行示例，配上 mermaid 流程图。还展示了 sub-agents、Meta-Agent 和 Team-Based Validation 多 agent 协同模式。

用 Astral UV 做单文件 Python 脚本运行，依赖装起来快。3.7k 星。

## 💡 解决什么问题

你想用 hooks 给 Claude Code 加自动化，但：

- 官方文档简洁但缺实例
- 不知道 hook payload 里有啥字段
- 想做"工具调用前验证"、"会话结束总结"等高级用法没参考

这个项目**所有 13 个 hook 都有实战示例**，从最简单的"通知声音"到"team-based validation"（多 agent 互评）都齐了。配合 ElevenLabs MCP 还能给 hook 加语音播报。

## 🎯 谁该用 / 谁别用

**适合你如果：**
- 你已经在用 hooks（你的 session-start-memory.sh 就是一种）想做更高级的
- 想学 sub-agent 调度
- 喜欢"一个 repo 读完成专家"风格

**别浪费时间如果：**
- 不用 Claude Code（这是高度专属）
- 嫌 UV / Python 生态麻烦
- 已经熟到能自己写 hook

## 🚀 三分钟上手

```bash
# 装 UV（Astral 出的快速 Python 工具）
curl -LsSf https://astral.sh/uv/install.sh | sh

# Clone 试跑
git clone https://github.com/disler/claude-code-hooks-mastery.git
cd claude-code-hooks-mastery

# 复制 .claude/settings.json 到你的项目，看每个 hook 执行
```

## 🔑 关键文件 / 关键概念

- **`.claude/settings.json`** — hooks 的配置中枢
- **13 个 hook 事件** — 每个有独立目录 + 示例脚本
- **UV single-file scripts** — `#!/usr/bin/env -S uv run --script` 单文件即可跑
- **Meta-Agent** — 一个 agent 调度其他 agent 的设计模式

## ⚠️ 踩坑提示

- hook 脚本要 `chmod +x` 且 shebang 要对
- UV 单文件 script 在依赖大时第一次执行慢
- Mermaid 图在 GitHub 上预览正常，本地编辑器可能要插件

## 🤔 为什么这次推它给你

**你已经有 session-start-memory.sh，但只用了 1 个 hook**。这个项目能让你**把剩下 12 个 hook 也用起来**：PreToolUse 拦截危险命令、PostToolUse 记录日志、UserPromptSubmit 注入项目上下文。直接抄 settings.json 模式，省一周摸索。pattern 候选：`uv-single-file-hook-script`、`hook-driven-context-injection`。

---
*由 /gitout 生成 · 2026-05-22 · theme: Claude Code Skill / hooks*
