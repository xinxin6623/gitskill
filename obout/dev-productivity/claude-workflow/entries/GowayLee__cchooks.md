---
type: repo
repo: GowayLee/cchooks
domain: dev-productivity/claude-workflow
status: active
discovered: 2026-05-23
last_reviewed: 2026-05-23
intent_matched: "用 Python SDK 写 Claude Code hook，不用手撸 stdin JSON 解析"
signals:
  stars: 131
  last_commit: 2026-04-08
  language: Python
  license: MIT
url: https://github.com/GowayLee/cchooks
absorption:
  harvested: false
  used: false
  used_in: []
---

# cchooks · 小白说明书

## 🧐 这是什么
Claude Code hook 的 Python SDK。一行 `create_context()` 帮你做掉所有 stdin JSON 解析、事件类型判断、退出码处理，让你专心写 hook 的业务逻辑（"屏蔽 rm -rf"、"写完 .py 自动 black"）。已发到 PyPI（`pip install cchooks`）。

## 💡 解决什么问题
- 官方 hook 文档让你自己读 stdin JSON、判断事件类型、按 exit code 决定行为——一个简单 hook 也要 30 行模板代码
- 9 种 hook 事件（PreToolUse / PostToolUse / Stop / SessionStart...），字段还都不一样，记不住
- exit code 和"高级 JSON 控制"两种模式混用容易出错

## 🎯 谁该用 / 谁别用
**适合你如果：**
- 你已经在写 Claude Code hook，受够了样板 JSON 解析
- 你想用 Python 类型提示 + IDE 自动补全来写 hook
- 你想看一份"hook 工程化"的参考实现

**别浪费时间如果：**
- 你只想抄两个 hook 跑跑，不想引依赖（看 disler/claude-code-hooks-mastery 更直接）
- 你用 PHP 或 JS 写 hook（这是纯 Python）
- 你的 hook 已经稳定运行，不需要重构

## 🚀 三分钟上手
```bash
pip install cchooks
# 或 uv add cchooks

# hooks/env-guard.py
cat > hooks/env-guard.py <<'PY'
#!/usr/bin/env python3
from cchooks import create_context, PreToolUseContext
c = create_context()
assert isinstance(c, PreToolUseContext)
if c.tool_name == "Write" and ".env" in c.tool_input.get("file_path", ""):
    c.output.exit_deny("Nope! .env files are protected")
else:
    c.output.exit_success()
PY
chmod +x hooks/env-guard.py
# 然后在 .claude/settings.json 配 PreToolUse hook 指向这个脚本
```

## 🔑 关键文件 / 关键概念
- `create_context()` — 一行搞定 stdin 解析 + 自动识别 hook 类型
- `PreToolUseContext` / `PostToolUseContext` / `StopContext` / ... — 9 个类型化 context
- 两种输出模式：`exit_success()`/`exit_deny()`（简单退出码）vs `output.allow()`/`output.deny()`（带 reason 和 system_message 的 JSON 控制）
- `c.stop_hook_active` — Stop hook 并行执行时的防重入字段，文档里强调过的坑点

## ⚠️ 踩坑提示
- Claude Code 的 Stop hook 是并行跑的，写 Stop hook 必须先判断 `stop_hook_active`，否则会形成循环
- `exit_deny()` 让用户看到拒绝原因；`output.deny()` 让 Claude 看到——别搞反
- SDK 自动识别 hook 类型靠 stdin 数据，本地手动测试要 mock JSON 喂进去

## 🤔 为什么这次推它给你
你要"hook 工程化"。这个 SDK 把 hook 写法从"读 JSON+判 tool_name+printf exit code"压缩成 3 行业务逻辑，**是 hook 走向工程实践的关键一步**。stars 不高但是 PyPI 包、类型完整、9 种事件全覆盖——属于"小而精"的 infra 层项目。trade-off：仅 Python 生态。

---
*由 /gitout 生成 · 2026-05-23 · intent: "个人提效工具，skill ide codeing harness 工程"*
