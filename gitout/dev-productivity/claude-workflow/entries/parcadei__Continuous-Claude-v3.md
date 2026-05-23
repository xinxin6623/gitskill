---
type: repo
repo: parcadei/Continuous-Claude-v3
domain: dev-productivity/claude-workflow
status: active
discovered: 2026-05-23
last_reviewed: 2026-05-23
intent_matched: "把 skill / hook / agent / memory 拼成一个完整 harness 的参考架构"
signals:
  stars: 3780
  last_commit: 2026-01-26
  language: Python
  license: MIT
url: https://github.com/parcadei/Continuous-Claude-v3
absorption:
  harvested: false
  used: false
  used_in: []
---

# Continuous Claude · 小白说明书

## 🧐 这是什么
一个把 Claude Code 改造成"会自学习的开发环境"的完整工程实践：109 个 skill + 32 个 agent + 30 个 hook 拼成一个 harness，外加 5 层代码分析（TLDR）、daemon 自动从对话里提取 learning、YAML handoff 解决 context 压缩丢信息问题。

## 💡 解决什么问题
- Claude Code 上下文塞满后会 compact，session 之间的细微决策就丢了
- 每次新会话都得重新"教"Claude 项目背景，token 烧得肉疼
- skill / agent / hook 各自为政，没有一套"框架"让 Claude 自己挑哪个用
- 改一个文件 Claude 要读整个文件，token 浪费严重

## 🎯 谁该用 / 谁别用
**适合你如果：**
- 你想看一个**完整 harness 是怎么设计的**——skill 怎么命名、hook 怎么注入 system reminder、agent 怎么协同
- 你受够了每次会话从头交代背景
- 你想抄一套 "Compound, don't compact" 的 memory 系统

**别浪费时间如果：**
- 你只想要轻量启动模板（这个体量大，109 skill 是真有 109 个文件）
- 你反感"AI 自动改 CLAUDE.md"，更想手动控制
- 你对 daemon / 后台进程方案心存戒备

## 🚀 三分钟上手
```bash
git clone https://github.com/parcadei/Continuous-Claude-v3
cd Continuous-Claude-v3
# 看 INSTALL 文档跑一键脚本（会装 daemon + 写入 ~/.claude/）
./install.sh
# 之后正常用 claude code，自然语言触发即可，例如
# "Fix the login bug in auth.py" 会自动触发 fix + debug skill
```

## 🔑 关键文件 / 关键概念
- **Skill Activation Hook** — 每次 UserPromptSubmit 注入 "SKILL ACTIVATION CHECK" 系统提醒，把"该用哪个 skill"做成 critical/recommended/suggested 优先级
- **YAML handoff** — 会话末尾用 YAML 而不是 markdown 摘要，token 效率更高，供下次会话恢复
- **TLDR 5 层代码分析** — 不读全文，按 symbol/import/structure 分层喂 Claude
- **`create_handoff` skill** — 标记会话结束前必须调用的 skill（critical 优先级演示）
- **daemon** — 后台进程从 transcript 提取 learning，自动入 memory

## ⚠️ 踩坑提示
- 109 skill 很爽但不是所有都对你的 stack 有用，建议先 fork 后裁剪
- daemon 写 CLAUDE.md 默认要 review，但首次跑前一定要看 `--dry-run`
- "skill activation check" 这套机制是 hook 注入的，你的项目如果已经有自定义 PreToolUse/UserPromptSubmit hook 会冲突
- pushed 是 2026-01，半年没大动，issue 区看看再装

## 🤔 为什么这次推它给你
你要"harness 工程"。这个仓库就是"一个人能把 Claude Code 改造成什么样"的天花板参考：5 大子系统都有实现代码，README 里把设计原则（Prompt+Tools+Context+Memory+Model 五要素）讲得比大多数论文清楚。**不是抄全套，是抄它的拆分思路。** trade-off：体量大、有自己的世界观，不是即插即用。

---
*由 /gitout 生成 · 2026-05-23 · intent: "个人提效工具，skill ide codeing harness 工程"*
