---
type: repo
repo: anthropics/claude-agent-sdk-python
domain: misc
status: active
decision: harvest
discovered: 2026-05-22
last_reviewed: 2026-05-22
theme: claude-skills
intent_matched: "官方 Python SDK，把 Claude Code 嵌进你自己的程序"
signals:
  stars: 7008
  last_commit: 2026-05-22
  language: Python
  license: MIT
url: https://github.com/anthropics/claude-agent-sdk-python
absorption:
  harvested: false
  used: false
  used_in: []
---

# Claude Agent SDK (Python) · 小白说明书

## 🧐 这是什么

**Anthropic 官方出的 Python SDK**，让你用代码方式调用 Claude Code（不是只能在终端里用）。`pip install claude-agent-sdk` 之后写几行 async Python 就能让 Claude 帮你跑工具、写文件、执行命令——SDK 自动捆绑了 Claude Code CLI，无需额外安装。MIT 协议。

简单说：**Claude Code 的"程序化入口"**。

## 💡 解决什么问题

你想做的东西超出"我在终端里跟 Claude 聊"的范畴：

- 想做一个 web 应用让 Claude 帮用户改代码
- 想用 cron 定时让 Claude 自动审 PR
- 想在自己的 CLI 里集成 Claude 的能力但不要把整个 Claude Code 暴露出来

SDK 给你 **`query()` async iterator + `ClaudeAgentOptions` 配置**，可以精确控制 tool 白名单、permission mode、工作目录、最大轮次。还能配 `can_use_tool` 回调做自定义权限决策。

## 🎯 谁该用 / 谁别用

**适合你如果：**
- 想做 OpenClaw 这种"嵌入 Claude 能力"的产品
- Python 主力开发者
- 想做自动化 / 定时任务用 Claude

**别浪费时间如果：**
- 只在终端用 Claude Code 就够了
- 用 TypeScript（去 anthropics/claude-agent-sdk-typescript）
- 需要无 Claude 订阅的方案（这个仍然走你的订阅 quota）

## 🚀 三分钟上手

```bash
pip install claude-agent-sdk
```

```python
import anyio
from claude_agent_sdk import query, ClaudeAgentOptions

async def main():
    options = ClaudeAgentOptions(
        system_prompt="你是个 Python reviewer",
        allowed_tools=["Read", "Bash"],
        max_turns=3,
    )
    async for msg in query(prompt="审一下 src/main.py", options=options):
        print(msg)

anyio.run(main)
```

## 🔑 关键文件 / 关键概念

- **`query()`** — 核心 async iterator
- **`ClaudeAgentOptions`** — 配置中心（system prompt / 工具 / 权限 / cwd）
- **`allowed_tools` / `disallowed_tools`** — 白名单 + 黑名单组合
- **`can_use_tool` 回调** — 程序化决定每次工具调用是否允许
- **`permission_mode`** — `acceptEdits` / `bypassPermissions` / `default`

## ⚠️ 踩坑提示

- 仍然要 Claude 订阅，SDK 不绕开计费
- 工具默认全开，生产环境一定要设白名单
- Python 3.10+ 强制

## 🤔 为什么这次推它给你

**你做 OpenClaw 的最关键参考——但是反向参考**。OpenClaw 想做"自托管 agent"，这个 SDK 是"基于 Claude 订阅的 agent"。看它的 **API 设计、权限模型、工具调用抽象**，是你 OpenClaw 设计自家 SDK 时的对照样本。也可以直接用它做 gitskill 项目的高级自动化（比如自动 prune entries）。pattern 候选：`agent-sdk-permission-as-callback`。

---
*由 /gitout 生成 · 2026-05-22 · theme: Claude Code Skill / hooks*
