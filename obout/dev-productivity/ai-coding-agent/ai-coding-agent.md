# AI Coding Agent · 自主代码生成代理框架

> 2026-05-23 · intent: "个人提效工具，skill ide coding harness 工程"
> 这是 /gitout 在【AI Coding Agent 方向】的产出。聚焦 **agent 框架本体**（不是 IDE 插件、不是 prompt 集合）。
> 你已经在用 Claude Code，所以这里都是**与 Claude Code 形成差异**的代理框架。

## 📊 健康度

| 项目 | Stars | 最近 commit | 语言 | License | 活跃度 |
|---|---:|---|---|---|---|
| OpenHands/OpenHands | 74,593 | 2026-05-23 | Python | MIT | 🟢 极活跃 |
| cline/cline | 62,207 | 2026-05-23 | TypeScript | Apache-2.0 | 🟢 极活跃 |
| Aider-AI/aider | 45,196 | 2026-05-22 | Python | Apache-2.0 | 🟢 极活跃 |
| iannuttall/ralph | 924 | 2026-02-04 | TypeScript | MIT | 🟡 稳定 |
| dollspace-gay/OpenClaudia | 71 | 2026-05-22 | Rust | MIT | 🟢 活跃但小众 |

## 🗺️ 选型建议

按你的诉求"个人提效 + 工程参考"分场景：

### 想立刻多一个 agent 用
- **首选 Cline**：装 VS Code 扩展 5 分钟上手，和 Claude Code 体验最接近但**不绑 Anthropic 一家模型**
- **次选 Aider**：纯终端、想跑 DeepSeek/本地 Qwen、想要 git 化工作流

### 想跑"派出去不管"的全自动 agent
- **OpenHands**：Devin 开源平替，Docker 沙箱里跑，能批量起 agent

### 想读 / 抄架构
- **Cline 的 sdk/**：一份核心引擎驱动 5 个壳的范本（TypeScript）
- **OpenHands 的 controller + runtime**：学术界引用最多的工程实现（Python）
- **Aider 的 repomap.py**：tree-sitter 做 codebase 索引的老牌方案
- **Ralph**：100 行级别看清"agent loop = while + file + git"
- **OpenClaudia**：Rust 实现，等于看一份 Claude Code 逆向版

### 想自己写 harness
- **Ralph** 是最佳起点，Claude Code 当 backend，外层逻辑你写
- **OpenHands software-agent-sdk** 是 Python 程序员的更重选项

## 🎯 入选 5 个的逻辑

任务漏斗（6 个 query × 10 = 60 候选，去重后约 44 个）：
1. `pushedAt < 2025-05-23` reject 掉沉睡项目
2. `stars < 50` reject（AI coding 赛道竞争激烈，低星多为水货）
3. **`description` 含 "awesome" / 是 prompt 集合 / 是 IDE 扩展配套 / 是 MCP server / 是教程仓** → reject
4. **是 Claude Code 本体或其子项目** → reject（用户已默认使用）
5. **archived** → reject（如 opencode-ai/opencode 已搬迁到 charmbracelet/crush）

剩下按"agent 架构完整度 / 多 LLM 支持 / 工程化程度 / 与 Claude Code 的差异化"重排，选 5。

## 📁 详情

每个项目的小白说明书在 `entries/` 下：

- [[dev-productivity/ai-coding-agent/entries/OpenHands__OpenHands|`OpenHands__OpenHands.md`]]
- [[dev-productivity/ai-coding-agent/entries/cline__cline|`cline__cline.md`]]
- [[dev-productivity/ai-coding-agent/entries/Aider-AI__aider|`Aider-AI__aider.md`]]
- [[dev-productivity/ai-coding-agent/entries/iannuttall__ralph|`iannuttall__ralph.md`]]
- [[dev-productivity/ai-coding-agent/entries/dollspace-gay__OpenClaudia|`dollspace-gay__OpenClaudia.md`]]

机读索引：[[dev-productivity/ai-coding-agent/index|`index.yaml`]]
