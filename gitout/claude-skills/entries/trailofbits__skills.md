---
type: repo
repo: trailofbits/skills
domain: claude-skills
status: active
discovered: 2026-05-26
last_reviewed: 2026-05-26
intent_matched: "知名安全团队维护的 Claude Code skill 集合"
signals:
  stars: 5392
  last_commit: 2026-05-16
  language: Python
  license: AGPL-3.0
url: https://github.com/trailofbits/skills
absorption:
  harvested: false
  used: false
  used_in: []
---

# trailofbits/skills · 小白说明书

## 🧐 这是什么
Trail of Bits（顶级安全审计公司）官方开放的 Claude Code plugin marketplace，30+ 个 skill 全是安全审计、漏洞挖掘、智能合约审计、模糊测试这一类硬核场景。不是教学库，是他们内部审 bug 的家伙事直接开源。

## 💡 解决什么问题
- 想用 AI 做代码审计但不知道审什么、怎么审 → 30+ 垂直 plugin 给你工作流
- 智能合约 / Rust 加密代码的常见 footgun → `sharp-edges` / `zeroize-audit` / `constant-time-analysis` 直接扫
- 自己写 Semgrep 规则太累 → `semgrep-rule-creator` 让 Claude 帮你写
- 不会配 fuzzer / mutation testing → 现成的工作流照搬

## 🎯 谁该用 / 谁别用
**适合你如果：**
- 安全研究员、智能合约审计员、CTF 选手
- 写底层 C/C++/Rust 代码、特别关心未定义行为和时序侧信道
- 想看顶级团队怎么把"内部审计 SOP"工程化成 skill

**别浪费时间如果：**
- 你做的是普通 web 后端、CRUD 业务（这里全是审计/逆向/RE）
- 你只想要快速生产力工具（这套要求你懂 Semgrep / DWARF / YARA 等基本盘）
- 你的项目跟密码学、智能合约、二进制安全无关

## 🚀 三分钟上手
```bash
# 在 Claude Code 里
/plugin marketplace add trailofbits/skills
/plugin menu                       # 浏览 30+ plugin
# 比如装智能合约审计套件
/plugin install building-secure-contracts
```

Codex 用户走 sidecar：
```bash
git clone https://github.com/trailofbits/skills.git ~/.codex/trailofbits-skills
~/.codex/trailofbits-skills/.codex/scripts/install-for-codex.sh
```

## 🔑 关键文件 / 关键概念
- `plugins/building-secure-contracts/` — 6 条链的智能合约漏洞扫描器
- `plugins/differential-review/` — 基于 git 历史的安全 diff 审计
- `plugins/semgrep-rule-creator/` — 写自定义 Semgrep 规则
- `plugins/fp-check/` — 系统性消除安全报告的 false positive
- `plugins/second-opinion/` — 用 Codex / Gemini 跨模型 code review
- `plugins/workflow-skill-design/` — 教你怎么设计工作流型 skill

## ⚠️ 踩坑提示
- AGPL-3.0 协议，商业项目集成前先看清楚条款
- 大部分 plugin 假设你装好了 Semgrep / CodeQL / fuzzer 等底层工具，不是开箱即用
- `building-secure-contracts` 等智能合约 plugin 需要相应 SDK（Foundry / Hardhat）
- 文档密度高，新手不读 README 直接 install 会一头雾水

## 🤔 为什么这次推它给你

1. **命中 intent.what：** 你要的是"知名团队的 skill 集合"——Trail of Bits 是行业内安全审计第一梯队，比 mattpocock 在安全方向更专精
2. **命中 soft pref：** 活跃维护（本周还有 commit）、Trophy Case 列了实战 bug 战绩、姊妹仓库 [skills-curated](https://github.com/trailofbits/skills-curated) / [claude-code-config](https://github.com/trailofbits/claude-code-config) 形成完整生态
3. **没命中的 trade-off：** 全是垂直安全场景，没有通用工程 skill（`/grill-me` 类的）；想做日常开发还得搭 mattpocock 那套

---
*由 /gitout 生成 · 2026-05-26 · intent: "mattpocock/skills + aihero.dev + Claude Code skill 集合"*
