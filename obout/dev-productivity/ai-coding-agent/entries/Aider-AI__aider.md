---
type: repo
repo: Aider-AI/aider
domain: dev-productivity/ai-coding-agent
status: active
discovered: 2026-05-23
last_reviewed: 2026-05-23
intent_matched: "终端里的老牌 AI 结对编程，repo-map + git commit 自动化是亮点"
signals:
  stars: 45196
  last_commit: 2026-05-22
  language: Python
  license: Apache-2.0
url: https://github.com/Aider-AI/aider
absorption:
  harvested: false
  used: false
  used_in: []
---

# Aider · 小白说明书

## 🧐 这是什么
2023 年就有的终端 AI 结对编程鼻祖，靠**repo-map（用 tree-sitter 给整个 codebase 画地图）+ 自动 git commit** 两大杀手锏成名，最近一次发布里 88% 的代码是 Aider 自己写的（singularity 88%）。

## 💡 解决什么问题
- 你不想离开终端，也不想装 IDE 扩展
- 你想要"每次 AI 改动**自动一个 git commit**"，diff、undo、review 全用熟悉的 git
- 你想要一个**模型无关**的 harness：Claude、GPT、DeepSeek、Gemini、本地 Ollama 全部能跑

## 🎯 谁该用 / 谁别用
**适合你如果：**
- 你是 vim / tmux / git 重度用户，喜欢一切在终端解决
- 想用本地模型（DeepSeek R1、Qwen 等）当编程伙伴
- 想读一份"如何用 tree-sitter 生成 repo 地图喂给 LLM"的成熟工程实现

**别浪费时间如果：**
- 你想要全自动、放手不管的 agent（Aider 更像 pair programmer，每次改完会停下来等你）
- 你需要复杂的 multi-agent / 子任务编排
- 你已经在用 Claude Code 终端版，Aider 的工作流和它高度重叠（但 Aider 模型选择更自由）

## 🚀 三分钟上手
```bash
pip install aider-install
aider-install

# 进入 git repo 直接跑
cd your-project
aider --model deepseek-chat   # 或 sonnet / gpt-4o / 本地 ollama
```

## 🔑 关键文件 / 关键概念
- `aider/repomap.py` — repo-map 实现，值得抄
- `aider/coders/` — 不同编辑策略（whole / diff / udiff / editblock）
- `aider/llm.py` — 通过 litellm 接所有模型
- `.aider.conf.yml` — 项目级配置

## ⚠️ 踩坑提示
- repo-map 在超大 repo 上会消耗很多 token，可以 `--map-tokens 0` 关掉
- 默认每次都自动 commit，如果你不想污染历史用 `--no-auto-commits`
- 不同模型用不同 edit format 效果差很多，看官方推荐配置

## 🤔 为什么这次推它给你
你已经有 Claude Code，但 Claude Code 锁死 Anthropic 模型。Aider 让你用**同样的工作流**跑 DeepSeek、本地 Qwen、GPT 等任意模型——这是它最大差异化。另外 repo-map 这个工程实践被无数后来者抄（Cline、Plandex 都借鉴），读源码学一份**老牌、稳定、被验证过**的 codebase indexing 方案。trade-off 是 Aider 偏 pair programming，没有 Claude Code/OpenHands 那种"扔过去不管"的自动度。

---
*由 /gitout 生成 · 2026-05-23 · intent: "个人提效工具，skill ide codeing harness 工程"*
