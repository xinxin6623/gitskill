# claude-workflow · Claude Code / AI 工作流工程化

## 健康度
- entries: 5
- last_updated: 2026-05-23
- focus: skill / hook / subagent / harness 工程实践

## 当前条目
| Repo | 一句话 | Lang | Stars |
|------|--------|------|-------|
| alirezarezvani/claude-code-skill-factory | skill / agent / hook / slash 批量生产脚手架（5 条产线） | Python | 782 |
| GowayLee/cchooks | Claude Code hook 的 Python SDK，干掉 stdin JSON 样板 | Python | 131 |
| parcadei/Continuous-Claude-v3 | 109 skill + 32 agent + 30 hook 拼成的完整自学习 harness | Python | 3780 |
| BayramAnnakov/claude-reflect | hook 捕获用户纠错 → 自动写入 CLAUDE.md，从历史 session 挖 skill | Python | 1041 |
| starbaser/ccproxy | 网络层代理 hook + 规则路由，把 Claude Code 请求分流到 OpenAI/Gemini/Perplexity | Python | 400 |

## 选型建议
- **想学 hook 怎么写**：从 cchooks 入门（小、纯、SDK 化），再看 ccproxy 的网络层 hook 思路对比抽象层
- **想批量产 skill**：claude-code-skill-factory 直接抄它的 SKILLS_FACTORY_PROMPT.md
- **想看完整 harness 架构**：Continuous-Claude-v3，它把"agent = Prompt+Tools+Context+Memory+Model 五要素"落地成代码
- **CLAUDE.md 乱了想自演化**：claude-reflect，自动捕获纠错 + skill mining
- **想接多 model provider**：ccproxy，配 LiteLLM 一个本地代理搞定

## 没选谁、为什么
- 各种 awesome-* 列表：用户硬约束"不要纯链接收集"，全部 reject
- VoltAgent/awesome-claude-code-subagents、disler/claude-code-hooks-mastery、anthropics/claude-agent-sdk-python：之前已经收录，不重复
- Piebald-AI/claude-code-system-prompts：极有价值的"反向 CC 内部 prompts"资料库，但偏文档归档而非工程实现，与用户"可跑代码"硬约束错位，候补
- daymade/claude-code-skills、levnikolaevich/claude-code-skills：偏 skill 市场/合集，工程化程度不如 skill-factory
- 各种 claude-code-template：多是个人 starter，差异化不够
