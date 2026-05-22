---
type: repo
repo: openinterpreter/open-interpreter
domain: misc
status: active
decision: harvest
discovered: 2026-05-22
last_reviewed: 2026-05-22
theme: cli-agent
intent_matched: "把任意软件包装成 Agent 可调用接口"
signals:
  stars: 63614
  last_commit: 2026-05-22
  language: Python
  license: AGPL-3.0
url: https://github.com/openinterpreter/open-interpreter
absorption:
  harvested: false
  used: false
  used_in: []
---

# Open Interpreter · 小白说明书

## 🧐 这是什么

**让 LLM 直接在你电脑上跑代码的"自然语言系统外壳"**。装完之后终端打一个 `interpreter`，就能用大白话让它"帮我把这堆 PDF 合并成一个"、"画一下 AAPL 和 META 的股价对比"、"找出这文件夹里所有重复图片"。它会自己写 Python/JS/Shell 代码、问你授权、执行、给结果。6.3 万星，AGPL 协议（商用要注意）。

## 💡 解决什么问题

你用电脑天天遇到的麻烦：

- "我知道这事 Python 三行能写完，但每次写都要查"
- "想批量处理一堆文件但不想开 Jupyter"
- "想让 ChatGPT 帮我做但它没法碰我本地的东西"

Open Interpreter 把"ChatGPT 代码解释器"那套东西**搬到你自己电脑上**——LLM 想干啥就在本地实际执行，你电脑里所有文件、所有工具都能用。

## 🎯 谁该用 / 谁别用

**适合你如果：**
- 你做的 OpenClaw 想参考"自然语言执行系统"该长什么样
- 用 Mac/Linux 想要一个万能的脚本助手
- 接受 AGPL 协议（个人项目无所谓，商业要换思路）

**别浪费时间如果：**
- 严格要求 MIT/Apache 协议（AGPL 传染性强）
- 不想给 LLM 在本地跑代码的权限
- 想要纯 API 调用，不需要交互式 shell

## 🚀 三分钟上手

```bash
pip install open-interpreter

# 设个 OpenAI key 或者本地 Ollama
interpreter

# 然后大白话提需求
> 把 ~/Downloads 里所有 png 转成 jpg
```

## 🔑 关键文件 / 关键概念

- **每次执行前要授权** — 默认安全行为，避免 LLM 乱搞
- **支持本地模型** — 能挂 Ollama / LM Studio
- **Python lib 模式** — `from interpreter import interpreter` 嵌进你自己的项目
- **Computer API** — 抽象出鼠标、键盘、屏幕的统一接口

## ⚠️ 踩坑提示

- **AGPL 协议**：你的项目用了它就要开源，OpenClaw 想集成要小心
- 国内网络下载 GPT-4o 慢，建议挂 Ollama
- 大文件操作前手动 backup，授权按错会真的删

## 🤔 为什么这次推它给你

**OpenClaw 的对照样本**。你 VISION 里写"an assistant that can run real tasks on a real computer"，Open Interpreter 就是这个赛道最成熟的开源实现。直接抄不行（AGPL），但**它的 Computer API 抽象、授权链路、本地模型 fallback 设计**都是高价值参考。pattern 候选：`natural-language-to-local-execution`。

---
*由 /gitout 生成 · 2026-05-22 · theme: CLI 包装 / Agent 工具化*
