# patterns · 跨项目抽象模式

> 从 2+ gitout entry 提炼的通用设计/架构模式。
> 上限 20 条，达到上限后需归档旧模式才能新增。

---

| 模式 | 来源 | 状态 | 创建日期 |
|------|------|------|---------|
| [[insights/patterns/function-to-realtime-stream.md\|Function → Realtime Stream]] | FastRTC + MOSS-TTS | draft | 2026-05-30 |
| [[insights/patterns/agent-feedback-loop.md\|Agent Feedback Loop]] | claude-reflect + Continuous-Claude-v3 | draft | 2026-05-30 |

---

## 创建规则

- **必须**关联 ≥2 个 source repo（来自 gitout/entries）
- 使用模板：复制 [[insights/_templates/pattern.md]]
- 文件名：kebab-case（如 `interruptible-streaming-pipeline.md`）
- 新建后更新本 INDEX、同步更新 source entry 的 `absorption.harvested` 字段
