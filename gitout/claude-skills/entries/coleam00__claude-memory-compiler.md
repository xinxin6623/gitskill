---
type: repo
repo: coleam00/claude-memory-compiler
domain: misc
status: active
decision: harvest
discovered: 2026-05-22
last_reviewed: 2026-05-22
theme: claude-skills
intent_matched: "对话自动编译进知识库（Karpathy LLM wiki 架构落地）"
signals:
  stars: 1079
  last_commit: 2026-05-22
  language: Python
  license: unknown
url: https://github.com/coleam00/claude-memory-compiler
absorption:
  harvested: false
  used: false
  used_in: []
---

# Claude Memory Compiler · 小白说明书

## 🧐 这是什么

一个**让 Claude Code 自动把对话编译成个人知识库**的 hook 套件。架构借鉴 Karpathy 的 LLM Knowledge Base（你的 kb skill 也是这个理念）：用 SessionEnd / PreCompact hook 捕获对话 → 后台 Claude Agent SDK 提炼出"决策 / 经验 / 模式 / 坑点" → 写入每日日志 → 编译成结构化概念页 → 下次 SessionStart 时把索引注入回来。

**不用向量数据库、不用 embedding，纯 markdown + 索引文件**。明确声明：personal use 走你的 Claude 订阅，不要额外 API key。

## 💡 解决什么问题

Claude Code 跟你聊了无数次，但每次开新会话它都"失忆"：

- 你解释过项目的特殊约定，下次还要再解释
- 这周踩过的坑下周可能再踩
- 跨项目共通的经验没法沉淀

这个项目把对话变成你的**"二阶大脑"**——Karpathy 那篇 gist 的精神是 LLM 不应只是产生答案，还应该帮你维护一个互链的 wiki。

## 🎯 谁该用 / 谁别用

**适合你如果：**
- 你已经在做 kb skill、mem skill（这个项目是你的同道）
- 重视长期个人知识沉淀
- 用 Claude Code 频率高

**别浪费时间如果：**
- 单次用 Claude，不积累
- 不接受"对话被自动分析"
- 已经有自己的知识系统不想被替换

## 🚀 三分钟上手

```bash
# 作者给的 vibe coding 风格指令
# 直接告诉 Claude Code：
# "Clone https://github.com/coleam00/claude-memory-compiler into this project.
#  Set up the hooks. Read AGENTS.md."

# Claude 会自动 clone + uv sync + 合并 settings.json

# 或手动
git clone https://github.com/coleam00/claude-memory-compiler.git
cd claude-memory-compiler
uv sync
```

## 🔑 关键文件 / 关键概念

- **flush.py** — SessionEnd 触发，用 Claude Agent SDK 提取知识
- **compile.py** — 每日 6 PM 后编译当日 logs 成结构化文章
- **daily/YYYY-MM-DD.md** — 每日原始日志
- **knowledge/concepts/** + **connections/** + **qa/** — 编译后的三层结构
- **SessionStart hook 注入索引** — 闭环关键

## ⚠️ 踩坑提示

- 个人用免费（Claude 订阅覆盖），团队 / 商业要看 Anthropic 政策
- 6 PM 时间是默认的，要根据你时区改
- 编译需要 Claude Agent SDK 跑后台进程，CPU 高峰可能感知

## 🤔 为什么这次推它给你

**这是 mem skill + kb skill 的直接亲戚 / 升级版**。你已经有：
- mem skill（项目 .claude/memory/ 手工维护）
- kb skill（~/knowledge/ 互链 wiki）

但**缺少自动编译这一环**——你目前还是手动 `/mem save` 才落地。这个项目就是把"手动 → 自动"的桥。可以直接借鉴它的 **flush.py / compile.py / hook 串联模式**升级你的 mem。pattern 候选：`session-to-knowledge-pipeline`、`karpathy-llm-wiki-as-hook`。

---
*由 /gitout 生成 · 2026-05-22 · theme: Claude Code Skill / hooks*
