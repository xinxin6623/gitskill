---
type: repo
repo: TheR1D/shell_gpt
domain: misc
status: active
decision: watch
discovered: 2026-05-22
last_reviewed: 2026-05-22
theme: cli-agent
intent_matched: "把 shell 命令生成做成日常顺手工具"
signals:
  stars: 12065
  last_commit: 2026-05-22
  language: Python
  license: MIT
url: https://github.com/TheR1D/shell_gpt
absorption:
  harvested: false
  used: false
  used_in: []
---

# ShellGPT (sgpt) · 小白说明书

## 🧐 这是什么

**专注一件事的 LLM CLI：生成你想要的 shell 命令**。打 `sgpt --shell "find 当前文件夹下所有 json 文件"`，它直接给你 `find . -type f -name "*.json"`，问要不要执行。同时支持代码片段生成、文档查询、stdin 管道。跨平台 Linux/macOS/Windows，pip 一行装好。1.2 万星 MIT。

## 💡 解决什么问题

shell 命令最大的痛点是**记不住**：

- `find` 各种 flag 顺序怎么写来着
- `tar` 是 `xzvf` 还是 `czvf`
- `awk` 写个简单的求和都要查

sgpt 让你**用大白话描述要干啥，它给你正确的命令**。比上 Stack Overflow 复制粘贴快得多。还能管道接日志：`docker logs app | sgpt "找错"`。

## 🎯 谁该用 / 谁别用

**适合你如果：**
- 经常用 shell 但 flag 老记不住
- 想要轻量工具，不要复杂插件系统
- 是 Windows PowerShell / CMD 用户（也支持）

**别浪费时间如果：**
- 已经是 shell 老手，常用命令烂熟
- 需要多模型切换灵活性（用 simonw/llm 更合适）
- 想要完整 agent 体验（用 open-interpreter）

## 🚀 三分钟上手

```bash
pip install shell-gpt

# 第一次会让你粘贴 OpenAI key
sgpt "什么是斐波那契"

# 生成 shell 命令
sgpt --shell "压缩当前目录所有 log 文件"

# 管道
docker logs -n 20 app | sgpt "找错并给建议"

# 配 Ollama 走本地
# 改 ~/.config/shell_gpt/.sgptrc
```

## 🔑 关键文件 / 关键概念

- **`-s` shell 模式** — 生成命令后给你 E/D/A（执行/解释/中止）选择
- **`-c` chat 模式** — 多轮上下文
- **role 系统** — 自定义 system prompt，可以预设"代码 reviewer"之类
- **配置文件** — `~/.config/shell_gpt/.sgptrc`

## ⚠️ 踩坑提示

- 默认 GPT-4，本地 Ollama 效果会差，README 自己提醒了
- 不要把 `--shell` 输出直接 `eval`，看一眼再执行
- 中文 prompt 偶尔会被翻译成英文回答

## 🤔 为什么这次推它给你

**最直接的"shell 助手"参考**，规模适中（不像 open-interpreter 那么大），代码读起来轻松。**它的"生成命令 → 用户确认 → 执行"三段式交互**是给 OpenClaw / CLI-Anything 做命令推荐时可以直接抄的模式。trade-off 是聚焦窄、扩展性不如 simonw/llm。pattern 候选：`generate-then-confirm-then-execute`。

---
*由 /gitout 生成 · 2026-05-22 · theme: CLI 包装 / Agent 工具化*
