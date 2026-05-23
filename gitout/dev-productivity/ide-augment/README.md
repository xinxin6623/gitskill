# IDE 增强 / 编辑器提效 · 方向 C

> intent: "个人提效工具，skill ide codeing harness 工程"
> 生成于 2026-05-23

## 健康度概览

| 指标 | 值 |
|---|---|
| 入选项目 | 5 |
| 全部近一年活跃 | 是（最旧 push 2026-03） |
| Star 总量 | 101.7k |
| 主语言分布 | Lua×3 / TS×1 / Rust×1 |
| 协议 | 全部 Apache-2.0（Tabby 含企业模块例外） |

## 项目对比表

| 项目 | Stars | 语言 | 一句话 | 适配编辑器 |
|---|---|---|---|---|
| [continuedev/continue](entries/continuedev__continue.md) | 33.3k | TS | 跨编辑器 AI + AI checks in CI | VSCode / JetBrains |
| [TabbyML/tabby](entries/TabbyML__tabby.md) | 33.5k | Rust | 自托管 Copilot server | VSCode / IntelliJ / Vim |
| [yetone/avante.nvim](entries/yetone__avante.nvim.md) | 17.9k | Lua | Neovim 版 Cursor，含 ACP | Neovim |
| [olimorris/codecompanion.nvim](entries/olimorris__codecompanion.nvim.md) | 6.6k | Lua | Neovim AI 框架，模块化扩展 | Neovim |
| [mason-org/mason.nvim](entries/mason-org__mason.nvim.md) | 10.3k | Lua | Neovim 跨平台工具包管理器 | Neovim |

## 选型建议（按你的诉求）

**如果你想"装上就用"**
→ 用 VSCode 选 **Continue**；用 Neovim 选 **avante.nvim**

**如果你想"研究工程实践"**
→ 看 **Continue** 的 monorepo 跨编辑器复用；看 **Tabby** 的 Rust server 架构；看 **mason** 的安装器协议抽象

**如果你想"构建自己的 skill / harness 体系"**
→ 重点看 **CodeCompanion** 的 prompt library + slash command + adapter 模式，和你 `~/knowledge` wiki + skills 思路最对口
→ Continue 的 `.continue/checks/*.md` 把 prompt 当代码版本管理，和你 KB 思想同源

**如果你要私有部署**
→ **Tabby** 是唯一一票，Rust + Docker 一键部署

## 漏斗记录

- raw 候选（9 个 query 合计去重后）：约 95
- 经 pushedAt >= 2025-05-23 + stars >= 30 筛选：22
- 剔除 awesome 列表 / 单语言 snippet / Copilot 纯 wrapper：8
- 抓 README 语义筛 + 工程完整度排序：5

## 排序依据

不按 star 直排。综合三项：
1. **工程实践完整度**（架构是否值得抄）
2. **通用性**（跨编辑器 / 跨语言）
3. **和 intent 的契合度**（skill / harness / 工程）

最终 fit_score 5 的三个（Continue / avante / CodeCompanion）都直接命中"skill + harness"诉求。

## 与已有知识的关系

- **不重复**：foam（已在 KB）属于 PKM/wiki，不在本批
- **可联动**：CodeCompanion 的 prompt library + Continue 的 `.continue/checks/*.md` 思想，可以反哺你 `~/knowledge` 的 skill 主题页
- **下一步可挖**：avante 的 ACP 协议、mason 的 registry 设计，都值得单独开主题深读

---
*由 /gitout 生成 · 2026-05-23*
