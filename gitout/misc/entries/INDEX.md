# gitout · 主题导航索引

> 按 James 当前的项目方向组织的 GitHub 项目地图。每条一句话简介 + 文档链接。
> 最后更新：2026-05-23 · 命令：`/gitout` 主题批量扫描

---

## 🧭 6 个主题

| 主题 | 对应你的项目 | 项目数 | 简介 |
| --- | --- | --- | --- |
| [📦 主题 1：CLI 包装 / Agent 工具化](#主题-1cli-包装--agent-工具化) | CLI-Anything、OpenClaw | 5 | 把任意软件/能力包装成 Agent 友好的命令行接口 |
| [🎙️ 主题 2：语音 pipeline 补充角度](#主题-2语音-pipeline--虚拟角色补充角度) | openclaw-voice-bot | 5 | 实时通信、s2s、中文 TTS、Apple Silicon 本地化 |
| [⚙️ 主题 3：Claude Code Skill / hooks](#主题-3claude-code-skill--hooks-生态) | mem、kb、gitout skill | 5 | 社区生态总索引 + hook 教程 + 官方 SDK + 自动化 |
| [💬 主题 4：聊天记录 / 个人数据遗产化](#主题-4聊天记录--个人数据遗产化) | weixinjilu | 5 | 微信 / iMessage / Discord 导出 + 数据为我所用 |
| [📚 主题 5：个人知识库 / Markdown wiki](#主题-5个人知识库--markdown-wiki) | kb skill | 5 | Logseq / Foam / Quartz / Dendron / SilverBullet 五大派 |
| [🤖 主题 6：AI 虚拟角色 / Live2D 对话机器人](#主题-6ai-虚拟角色--live2d-对话机器人) | openclaw-voice-bot 角色侧 | 5 | 可 DIY 的虚拟主播 / 桌宠 / Live2D 对话机器人方案 |

---

## 主题 1：CLI 包装 / Agent 工具化

把任意软件或能力变成 Agent 可调用的命令行工具。**给 OpenClaw 和 CLI-Anything 当对照样本。**

| Repo | 一句话 | 详细文档 |
| --- | --- | --- |
| [openinterpreter/open-interpreter](https://github.com/openinterpreter/open-interpreter) | 让 LLM 直接在你电脑上跑代码的"自然语言系统外壳" | [📄](./openinterpreter__open-interpreter.md) |
| [danielmiessler/Fabric](https://github.com/danielmiessler/Fabric) | 把 AI prompt 当 Unix 命令用的框架，几百个 pattern 可组合 | [📄](./danielmiessler__Fabric.md) |
| [simonw/llm](https://github.com/simonw/llm) | LLM CLI 的事实标准，插件化模型支持 + SQLite 自动日志 | [📄](./simonw__llm.md) |
| [TheR1D/shell_gpt](https://github.com/TheR1D/shell_gpt) | 专注 shell 命令生成的轻量 CLI，"生成 → 确认 → 执行"三段式 | [📄](./TheR1D__shell_gpt.md) |
| [kellyjonbrazil/jc](https://github.com/kellyjonbrazil/jc) | 150+ Unix 命令输出转 JSON，CLI-Anything 的直接亲戚 | [📄](./kellyjonbrazil__jc.md) |

---

## 主题 2：语音 pipeline / 虚拟角色（补充角度）

实时通信底座 + 中文 TTS + Apple Silicon 本地 + 端到端 s2s 等差异化角度。

| Repo | 一句话 | 详细文档 |
| --- | --- | --- |
| [gradio-app/fastrtc](https://github.com/gradio-app/fastrtc) | Python 函数变 WebRTC 实时流，自带 VAD/UI/电话号码 | [📄](./gradio-app__fastrtc.md) |
| [OpenMOSS/MOSS-TTS](https://github.com/OpenMOSS/MOSS-TTS) | 复旦 MOSS 团队开源 TTS 家族，中文 + 流式 + Apache | [📄](./OpenMOSS__MOSS-TTS.md) |
| [OpenMOSS/MOSS-TTSD](https://github.com/OpenMOSS/MOSS-TTSD) | "剧本 → 多人对话"长篇 TTS，做播客 / 有声书神器 | [📄](./OpenMOSS__MOSS-TTSD.md) |
| [soniqo/speech-swift](https://github.com/soniqo/speech-swift) | Apple Silicon 本地全栈语音 SDK（ASR/TTS/Streaming） | [📄](./soniqo__speech-swift.md) |
| [Liquid4All/liquid-audio](https://github.com/Liquid4All/liquid-audio) | 端到端 speech-to-speech 模型（1.5B 小模型实时对话） | [📄](./Liquid4All__liquid-audio.md) |

---

## 主题 3：Claude Code Skill / hooks 生态

直接关联你正在写的 mem skill / kb skill / gitout skill。

| Repo | 一句话 | 详细文档 |
| --- | --- | --- |
| [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | 整个 Claude Code 生态的总索引（skills/hooks/subagents） | [📄](./hesreallyhim__awesome-claude-code.md) |
| [disler/claude-code-hooks-mastery](https://github.com/disler/claude-code-hooks-mastery) | 13 个 hook 生命周期事件完整教学，meta-agent 模式 | [📄](./disler__claude-code-hooks-mastery.md) |
| [anthropics/claude-agent-sdk-python](https://github.com/anthropics/claude-agent-sdk-python) | 官方 Python SDK，把 Claude Code 嵌进自己程序 | [📄](./anthropics__claude-agent-sdk-python.md) |
| [VoltAgent/awesome-claude-code-subagents](https://github.com/VoltAgent/awesome-claude-code-subagents) | 131+ 职业角色化 subagent，plugin marketplace 一键装 | [📄](./VoltAgent__awesome-claude-code-subagents.md) |
| [coleam00/claude-memory-compiler](https://github.com/coleam00/claude-memory-compiler) | 对话自动编译成知识库（Karpathy LLM wiki 架构落地） | [📄](./coleam00__claude-memory-compiler.md) |

---

## 主题 4：聊天记录 / 个人数据遗产化

直接关联 weixinjilu。三种典型路径（数据库解密 / 本地 SQLite / API Token）+ 终极思路（HPI 把人生数据做成 Python 包）。

| Repo | 一句话 | 详细文档 |
| --- | --- | --- |
| [LC044/WeChatMsg](https://github.com/LC044/WeChatMsg) | 中文圈微信导出之王，**作者已停更**——你的窗口期 | [📄](./LC044__WeChatMsg.md) |
| [ReagentX/imessage-exporter](https://github.com/ReagentX/imessage-exporter) | Rust 写的 iMessage 完整导出器，工程质量标杆 | [📄](./ReagentX__imessage-exporter.md) |
| [Tyrrrz/DiscordChatExporter](https://github.com/Tyrrrz/DiscordChatExporter) | Discord 频道历史导出，API + Token 路线代表 | [📄](./Tyrrrz__DiscordChatExporter.md) |
| [karlicoss/HPI](https://github.com/karlicoss/HPI) | 人生作为 Python 包：`import my.reddit / my.imessage`... | [📄](./karlicoss__HPI.md) |
| [karlicoss/promnesia](https://github.com/karlicoss/promnesia) | 浏览器扩展：每个网页都告诉你你在哪个数据源里遇见过它 | [📄](./karlicoss__promnesia.md) |

---

## 主题 5：个人知识库 / Markdown wiki

直接关联 kb skill。五大流派各取代表。

| Repo | 一句话 | 详细文档 |
| --- | --- | --- |
| [logseq/logseq](https://github.com/logseq/logseq) | Roam 开源对标，outliner + 块引用 + 隐私优先 | [📄](./logseq__logseq.md) |
| [foambubble/foam](https://github.com/foambubble/foam) | VSCode 扩展把编辑器变 Obsidian，工作流最贴合你 | [📄](./foambubble__foam.md) |
| [jackyzha0/quartz](https://github.com/jackyzha0/quartz) | Markdown 文件夹一键变"数字花园"网站 | [📄](./jackyzha0__quartz.md) |
| [dendronhq/dendron](https://github.com/dendronhq/dendron) | 层级命名空间式 PKM，**已停更但思想值得**学 | [📄](./dendronhq__dendron.md) |
| [silverbulletmd/silverbullet](https://github.com/silverbulletmd/silverbullet) | 浏览器内可编程 PKM，Lua 脚本驱动 | [📄](./silverbulletmd__silverbullet.md) |

---

## 主题 6：AI 虚拟角色 / Live2D 对话机器人

可 DIY 的虚拟主播 / 桌宠 / Live2D 对话机器人方案 —— 给 openclaw-voice-bot 的"角色侧"做参考。

| Repo | 一句话 | 详细文档 |
| --- | --- | --- |
| [moeru-ai/airi](https://github.com/moeru-ai/airi) | 带 3D/2D 角色的对话机器人，眼神/口型/表情可定制 | [📄](./moeru-ai__airi.md) |
| [elevenyellow/handcrafted-persona-engine](https://github.com/elevenyellow/handcrafted-persona-engine) | Live2D + 口型 + 表情完整管线，可 DIY 程度高 | [📄](./elevenyellow__handcrafted-persona-engine.md) |
| [whoiswennie/AI-Vtuber](https://github.com/whoiswennie/AI-Vtuber) | 全栈虚拟主播方案（含意图识别 + 长短期记忆） | [📄](./whoiswennie__AI-Vtuber.md) |
| [chyinan/Kokoro-Engine](https://github.com/chyinan/Kokoro-Engine) | Live2D + MOD 高自由度定制对话机器人 | [📄](./chyinan__Kokoro-Engine.md) |
| [suzuran0y/Live2D-LLM-Chat](https://github.com/suzuran0y/Live2D-LLM-Chat) | 眼神追踪 + 口型同步实现可读，最小可参考实现 | [📄](./suzuran0y__Live2D-LLM-Chat.md) |

---

## 📊 整体统计

- **总项目数**：30
- **已停更但收录**：3（LC044/WeChatMsg、dendronhq/dendron、Tyrrrz/DiscordChatExporter 维护模式）

## 🎯 给 James 的快速建议（top 3 优先级）

1. **OpenClaw 设计参考**：先读 [open-interpreter](./openinterpreter__open-interpreter.md) 和 [claude-agent-sdk-python](./anthropics__claude-agent-sdk-python.md) —— 一个看"自托管 agent 长什么样"，一个看"基于订阅 agent 的工程标准"。
2. **kb skill 升级路线**：[claude-memory-compiler](./coleam00__claude-memory-compiler.md)（自动编译）+ [foam](./foambubble__foam.md)（编辑器内体验）+ [quartz](./jackyzha0__quartz.md)（发布）三件套组合，能把 kb 从命令行升级成完整工作流。
3. **weixinjilu 差异化定位**：[LC044/WeChatMsg](./LC044__WeChatMsg.md) 已停更是你的窗口，参考 [imessage-exporter](./ReagentX__imessage-exporter.md) 的 Rust 工程化思路，长期靠 [HPI](./karlicoss__HPI.md) 的"个人数据包"理念站住差异。

---

## 🔗 相关文件

- 原始 gh search 结果：[../../raw/2026-05-22/](../../raw/2026-05-22/) 下按主题分目录
- 健康度面板：[../README.md](../README.md)

*由 /gitout 主题批量扫描生成 · 2026-05-22 · 2026-05-23 同步实际 entries*
