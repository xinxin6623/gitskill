---
type: repo
repo: simonw/llm
domain: misc
status: active
decision: harvest
discovered: 2026-05-22
last_reviewed: 2026-05-22
theme: cli-agent
intent_matched: "标准化的 LLM CLI 工具，插件化模型支持"
signals:
  stars: 11909
  last_commit: 2026-05-22
  language: Python
  license: Apache-2.0
url: https://github.com/simonw/llm
absorption:
  harvested: false
  used: false
  used_in: []
---

# llm (simonw) · 小白说明书

## 🧐 这是什么

Simon Willison（Django 共同创始人 + 个人技术博主标杆）写的 **LLM 命令行工具的"事实标准"**。一个 `llm "问题"` 就跟模型对话，支持 OpenAI / Claude / Gemini / Llama 等几十种模型，全部走插件扩展（`llm install llm-gemini` 就接通 Gemini）。所有问答自动存进 SQLite，未来可以回溯/检索/重放。11.9k 星，Apache 协议。

## 💡 解决什么问题

每个模型 CLI 工具都自己一套，你换模型还要重学：

- OpenAI 的 CLI 跟 Anthropic 的 CLI 长得不一样
- 想批量跑 prompt 处理一堆数据没有标准管道
- 跟模型对话过的内容到哪儿找？

llm 用 Click 框架做了一套统一接口，**模型只是插件**，core 极小。所有交互自动落 SQLite，可以 `llm logs` 翻历史，可以 `llm embed` 算嵌入。

## 🎯 谁该用 / 谁别用

**适合你如果：**
- 喜欢 Unix 哲学（小而美、可组合、纯文本）
- Python 用户，希望 CLI 同时能 import 进项目
- 想看"插件式架构"的优雅实现

**别浪费时间如果：**
- 想要图形界面
- 只用单一模型不需要多供应商
- 不需要历史记录

## 🚀 三分钟上手

```bash
pip install llm        # 或 brew install llm
llm keys set openai    # 粘贴 OpenAI key

llm "写一首给猫的诗"

# 加 Claude
llm install llm-claude-3
llm keys set claude
llm -m claude-3.5-sonnet "..."

# 从文件
cat code.py | llm -s "解释这段代码"

# 看历史
llm logs
```

## 🔑 关键文件 / 关键概念

- **插件系统** — `llm install llm-<provider>` 就接通新模型
- **SQLite 自动日志** — 在 `~/.config/io.datasette.llm/logs.db`
- **embedding 命令** — `llm embed` 算嵌入，配合 sqlite-vss 做本地 RAG
- **schemas** — 支持结构化输出（JSON schema 约束）

## ⚠️ 踩坑提示

- 默认模型 gpt-4o-mini，要换默认用 `llm models default <id>`
- Homebrew 装的版本有时滞后 PyPI
- 跨机器同步日志要自己 rsync `~/.config/io.datasette.llm/`

## 🤔 为什么这次推它给你

**OpenClaw / CLI-Anything 都该看的"教科书项目"**。Simon 的代码工程质量极高，**插件加载机制 + SQLite 日志 + Click CLI** 这三件套组合是 Python CLI 工具的金标准。你想给 OpenClaw 加 LLM provider 切换、想给 CLI-Anything 设计统一日志，都能直接参考。pattern 候选：`plugin-as-pip-package`、`cli-tool-and-library-dual-purpose`。

---
*由 /gitout 生成 · 2026-05-22 · theme: CLI 包装 / Agent 工具化*
