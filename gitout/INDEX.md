# gitout · 主题导航索引

> 你用 `/gitout` 一路扫下来攒的 GitHub 项目地图。每个主题挑了 4-6 个，每条都有大白话简介 + 详细文档链接。
> 最后更新：2026-05-23

---

## 🧭 13 个主题一览

| 主题 | 一句话讲它是干嘛的 | 项目数 |
| --- | --- | --- |
| [📦 1. CLI 包装 / 把工具变成 AI 能用的命令](#主题-1cli-包装--把工具变成-ai-能用的命令) | 让 AI 像人一样调命令行，或者把任意软件包装成 Agent 能调的工具 | 5 |
| [🎙️ 2. 语音 pipeline / 实时对话技术栈](#主题-2语音-pipeline--实时对话技术栈) | 跟 AI 实时语音对话需要的底座：WebRTC、TTS、本地推理 | 5 |
| [⚙️ 3. Claude Code 生态 / Skill 和 Hooks](#主题-3claude-code-生态--skill-和-hooks) | 怎么把 Claude Code 改造成自己的工作流：skill、hook、subagent | 5 |
| [💬 4. 聊天记录导出 / 个人数据归档](#主题-4聊天记录导出--个人数据归档) | 把微信、iMessage、Discord 等历史聊天记录拿到本地，变成自己的数据资产 | 5 |
| [📚 5. 个人知识库 / Markdown wiki](#主题-5个人知识库--markdown-wiki) | 用 Markdown 文件做笔记 + 互相链接 + 可发布的知识管理系统 | 5 |
| [🤖 6. AI 虚拟角色 / Live2D 桌宠](#主题-6ai-虚拟角色--live2d-桌宠) | 给 AI 套个皮：能动嘴、有表情、能聊天的虚拟形象 | 5 |
| [🖥️ 7. 服务器搭建管理面板](#主题-7服务器搭建管理面板) | 不想敲命令配 Nginx？用 Web 面板鼠标点点搞定服务器 | 5 |
| [🌐 8. 物联网平台](#主题-8物联网平台) | 一套能管 MQTT 设备 + 规则引擎 + Dashboard + 手机 App 的完整 IoT 后台 | 4 |
| [🏠 9. 个人网站全栈模板](#主题-9个人网站全栈模板) | 自己的"超级主页"：博客、项目展示、Now 页、订阅，一个 starter 搞定 | 4 |
| [🛠️ 10. Claude Code 工作流工程化](#主题-10claude-code-工作流工程化) | skill 工厂 / hook SDK / 自学习 harness——把 Claude Code 玩出工程化体系 | 5 |
| [🚀 11. AI Coding Agent 框架](#主题-11ai-coding-agent-框架) | Claude Code 之外的自主代码代理（Aider/Cline/OpenHands）参考样本 | 5 |
| [✏️ 12. IDE 增强 / 编辑器 AI 集成](#主题-12ide-增强--编辑器-ai-集成) | VSCode/Neovim 里的 AI 编程插件 + 包管理器，提效工程范本 | 5 |
| [🧰 13. 开发者生产力工具（非 AI）](#主题-13开发者生产力工具非-ai) | 命令行加速器 / TUI / dotfile 管理——纯手工提效，跟 AI 路线做对照 | 5 |

**合计 63 个项目**

---

## 主题 1：CLI 包装 / 把工具变成 AI 能用的命令

**这一组解决什么：** AI 想真正帮你干活，得能调用电脑上的工具。这里的项目要么让 AI 直接跑命令，要么帮你把任意软件包装成 AI 可以理解的接口。

| Repo | 大白话讲它干嘛的 | 详细文档 |
| --- | --- | --- |
| [openinterpreter/open-interpreter](https://github.com/openinterpreter/open-interpreter) | 你用自然语言提需求，它让 AI 直接在你电脑上写代码并执行 | [📄](./misc/entries/openinterpreter__open-interpreter.md) |
| [danielmiessler/Fabric](https://github.com/danielmiessler/Fabric) | 把"问 AI"做成 Unix 命令，几百个现成的 prompt 像管道一样组合 | [📄](./misc/entries/danielmiessler__Fabric.md) |
| [simonw/llm](https://github.com/simonw/llm) | 命令行里调各种大模型的"瑞士军刀"，所有对话自动存到 SQLite | [📄](./misc/entries/simonw__llm.md) |
| [TheR1D/shell_gpt](https://github.com/TheR1D/shell_gpt) | 你描述要干啥（如"找出最大的 5 个文件"），它生成 shell 命令让你确认再跑 | [📄](./misc/entries/TheR1D__shell_gpt.md) |
| [kellyjonbrazil/jc](https://github.com/kellyjonbrazil/jc) | 把 150+ Unix 命令的输出变成 JSON，AI 一眼能读懂 | [📄](./misc/entries/kellyjonbrazil__jc.md) |

---

## 主题 2：语音 pipeline / 实时对话技术栈

**这一组解决什么：** 想做个能跟你说话的 AI，得拼一堆东西：怎么接听麦克风、怎么生成自然语音、怎么不卡顿。这里挑了不同环节的代表。

| Repo | 大白话讲它干嘛的 | 详细文档 |
| --- | --- | --- |
| [gradio-app/fastrtc](https://github.com/gradio-app/fastrtc) | 写个 Python 函数就能变成 WebRTC 视频/语音流，甚至能接电话 | [📄](./misc/entries/gradio-app__fastrtc.md) |
| [OpenMOSS/MOSS-TTS](https://github.com/OpenMOSS/MOSS-TTS) | 复旦开源的中文 TTS，文字转语音、流式输出、商用友好 | [📄](./misc/entries/OpenMOSS__MOSS-TTS.md) |
| [OpenMOSS/MOSS-TTSD](https://github.com/OpenMOSS/MOSS-TTSD) | 给你一份剧本，它生成多人对话语音——做播客/有声书神器 | [📄](./misc/entries/OpenMOSS__MOSS-TTSD.md) |
| [soniqo/speech-swift](https://github.com/soniqo/speech-swift) | Mac M 系列本地跑语音识别+合成，不用上云、不用付费 | [📄](./misc/entries/soniqo__speech-swift.md) |
| [Liquid4All/liquid-audio](https://github.com/Liquid4All/liquid-audio) | 1.5B 小模型直接"听到→说出"，跳过文字中转，速度更快 | [📄](./misc/entries/Liquid4All__liquid-audio.md) |

---

## 主题 3：Claude Code 生态 / Skill 和 Hooks

**这一组解决什么：** Claude Code 不只是聊天，能装 skill（技能）、配 hook（自动化触发）、塞 subagent（多角色协作）。这里的项目是教你把它玩花的最佳起点。

| Repo | 大白话讲它干嘛的 | 详细文档 |
| --- | --- | --- |
| [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | Claude Code 整个生态的"黄页"——找 skill、找 hook、找扩展都来这 | [📄](./misc/entries/hesreallyhim__awesome-claude-code.md) |
| [disler/claude-code-hooks-mastery](https://github.com/disler/claude-code-hooks-mastery) | 13 种 hook 事件全讲清楚，附完整可跑示例 | [📄](./misc/entries/disler__claude-code-hooks-mastery.md) |
| [anthropics/claude-agent-sdk-python](https://github.com/anthropics/claude-agent-sdk-python) | 官方 Python SDK，把 Claude 的能力嵌进你自己的程序 | [📄](./misc/entries/anthropics__claude-agent-sdk-python.md) |
| [VoltAgent/awesome-claude-code-subagents](https://github.com/VoltAgent/awesome-claude-code-subagents) | 131+ 个角色化 subagent（前端工程师、PM、运维…），可一键安装 | [📄](./misc/entries/VoltAgent__awesome-claude-code-subagents.md) |
| [coleam00/claude-memory-compiler](https://github.com/coleam00/claude-memory-compiler) | 把你跟 Claude 的聊天记录自动整理成知识库 | [📄](./misc/entries/coleam00__claude-memory-compiler.md) |

---

## 主题 4：聊天记录导出 / 个人数据归档

**这一组解决什么：** 你的微信/iMessage/Discord 历史都锁在 App 里，要把它导出来变成自己的资产（喂给 AI、做数据分析、留档）。三种主流路线 + 一个"人生即 Python 包"的终极思路。

| Repo | 大白话讲它干嘛的 | 详细文档 |
| --- | --- | --- |
| [LC044/WeChatMsg](https://github.com/LC044/WeChatMsg) | 中文圈微信导出工具之王，**作者已不再更新**，趁还能用赶紧导 | [📄](./misc/entries/LC044__WeChatMsg.md) |
| [ReagentX/imessage-exporter](https://github.com/ReagentX/imessage-exporter) | Rust 写的 iMessage 完整导出器，Mac/iCloud 都能搞定 | [📄](./misc/entries/ReagentX__imessage-exporter.md) |
| [Tyrrrz/DiscordChatExporter](https://github.com/Tyrrrz/DiscordChatExporter) | Discord 频道/私信完整导出成 HTML 或 JSON | [📄](./misc/entries/Tyrrrz__DiscordChatExporter.md) |
| [karlicoss/HPI](https://github.com/karlicoss/HPI) | 大开脑洞：把你的人生数据做成 Python 包，`import my.reddit` 就能用 | [📄](./misc/entries/karlicoss__HPI.md) |
| [karlicoss/promnesia](https://github.com/karlicoss/promnesia) | 浏览器插件：你打开一个网页，它告诉你"你两年前在哪聊过这个" | [📄](./misc/entries/karlicoss__promnesia.md) |

---

## 主题 5：个人知识库 / Markdown wiki

**这一组解决什么：** 你想把笔记、想法、文章用 Markdown 存起来，互相链接，最好还能发布成网站。Notion 那一套但完全本地、完全自己掌控。五大流派各挑一个代表。

| Repo | 大白话讲它干嘛的 | 详细文档 |
| --- | --- | --- |
| [logseq/logseq](https://github.com/logseq/logseq) | 大纲式笔记，每段话都可单独链接和引用，对标 Roam Research | [📄](./misc/entries/logseq__logseq.md) |
| [foambubble/foam](https://github.com/foambubble/foam) | 让 VSCode 变成 Obsidian——边写代码边记笔记的天然选择 | [📄](./misc/entries/foambubble__foam.md) |
| [jackyzha0/quartz](https://github.com/jackyzha0/quartz) | 一文件夹 Markdown 一键变成漂亮的"数字花园"网站 | [📄](./misc/entries/jackyzha0__quartz.md) |
| [dendronhq/dendron](https://github.com/dendronhq/dendron) | 用文件名做层级的 PKM（如 `tech.rust.lifetime.md`），**已停更但思路值得参考** | [📄](./misc/entries/dendronhq__dendron.md) |
| [silverbulletmd/silverbullet](https://github.com/silverbulletmd/silverbullet) | 浏览器里跑的笔记，Lua 脚本能给笔记加任何动态功能 | [📄](./misc/entries/silverbulletmd__silverbullet.md) |

---

## 主题 6：AI 虚拟角色 / Live2D 桌宠

**这一组解决什么：** 想给 AI 套个皮：可以动嘴、有表情、能眨眼、会撒娇。这里是开源虚拟主播 / Live2D 桌宠 / 互动角色的代表方案。

| Repo | 大白话讲它干嘛的 | 详细文档 |
| --- | --- | --- |
| [moeru-ai/airi](https://github.com/moeru-ai/airi) | 带 2D/3D 形象的对话机器人，眼神、口型、表情全可定制 | [📄](./misc/entries/moeru-ai__airi.md) |
| [elevenyellow/handcrafted-persona-engine](https://github.com/elevenyellow/handcrafted-persona-engine) | Live2D + 口型 + 表情一条龙，DIY 自由度最高 | [📄](./misc/entries/elevenyellow__handcrafted-persona-engine.md) |
| [whoiswennie/AI-Vtuber](https://github.com/whoiswennie/AI-Vtuber) | 全栈虚拟主播方案，含意图识别、长短期记忆 | [📄](./misc/entries/whoiswennie__AI-Vtuber.md) |
| [chyinan/Kokoro-Engine](https://github.com/chyinan/Kokoro-Engine) | Live2D + MOD 系统，高自由度的可玩法对话角色 | [📄](./misc/entries/chyinan__Kokoro-Engine.md) |
| [suzuran0y/Live2D-LLM-Chat](https://github.com/suzuran0y/Live2D-LLM-Chat) | 眼神追踪 + 口型同步的最小可学示例，几百行代码读完 | [📄](./misc/entries/suzuran0y__Live2D-LLM-Chat.md) |

---

## 主题 7：服务器搭建管理面板

**这一组解决什么：** 你买了台 VPS 或家里有台小主机，但配 Nginx、装 MySQL、跑 Docker 一堆命令背不下来。这些项目让你用浏览器点点鼠标就能搞定，**装个面板等于装了套图形化运维工具**。

📁 详细文档在 `gitout/server-ops/entries/`

| Repo | 大白话讲它干嘛的 | 详细文档 |
| --- | --- | --- |
| [acepanel/panel](https://github.com/acepanel/panel) | Go 单文件运行，极轻量、不破坏系统的中文面板（"耗子面板"的新版） | [📄](./server-ops/entries/acepanel__panel.md) |
| [1Panel-dev/1Panel](https://github.com/1Panel-dev/1Panel) | 国产现代化全能面板，165+ 应用一键装、容器管理一体化（不知道选啥就用它） | [📄](./server-ops/entries/1Panel-dev__1Panel.md) |
| [IceWhaleTech/CasaOS](https://github.com/IceWhaleTech/CasaOS) | 给家用小主机做的"个人云"系统，UI 像 iPad，适合 NAS 场景 | [📄](./server-ops/entries/IceWhaleTech__CasaOS.md) |
| [aaPanel/aaPanel](https://github.com/aaPanel/aaPanel) | 宝塔国际版，号称 60M 内存就能跑，PHP 建站老朋友 | [📄](./server-ops/entries/aaPanel__aaPanel.md) |
| [webmin/webmin](https://github.com/webmin/webmin) | 1997 年至今的"祖师爷"，传统 Linux 服务管理（DNS/邮件/Samba）王者 | [📄](./server-ops/entries/webmin__webmin.md) |

---

## 主题 8：物联网平台

**这一组解决什么：** 你有一堆设备（传感器、灯、网关）要联网管理，需要一套完整后台：MQTT 接入、设备列表、规则引擎（如"温度超过 30 就报警"）、可视化大屏、手机 App。这些项目是开源的完整方案。

📁 详细文档在 `gitout/iot-platform/entries/`

| Repo | 大白话讲它干嘛的 | 详细文档 |
| --- | --- | --- |
| [kerwincui/FastBee](https://github.com/kerwincui/FastBee) | 国产全栈轻量 IoT 平台，含 Web 控制台 + 微信小程序 + App，开箱即用 | [📄](./iot-platform/entries/kerwincui__FastBee.md) |
| [IoTSharp/IoTSharp](https://github.com/IoTSharp/IoTSharp) | .NET 版的"小号 ThingsBoard"，规则链、多租户该有的都有 | [📄](./iot-platform/entries/IoTSharp__IoTSharp.md) |
| [seslabSJU/tinyIoT](https://github.com/seslabSJU/tinyIoT) | 纯 C 写的极简 IoT 服务，几千行代码能完整读完，学底层最佳教材 | [📄](./iot-platform/entries/seslabSJU__tinyIoT.md) |
| [jetlinks/jetlinks-community](https://github.com/jetlinks/jetlinks-community) | 企业级响应式 IoT 平台，模块切分最规范，**作为架构参考别通读** | [📄](./iot-platform/entries/jetlinks__jetlinks-community.md) |

---

## 主题 9：个人网站全栈模板

**这一组解决什么：** 你想搭个自己的"超级主页"——博客、项目展示、Now 页、关于、订阅、统计什么的全都要，但又不想从零写。这些是开源可二次开发的模板/starter。

📁 详细文档在 `gitout/personal-site/entries/`

| Repo | 大白话讲它干嘛的 | 详细文档 |
| --- | --- | --- |
| [thedevdavid/digital-garden](https://github.com/thedevdavid/digital-garden) | 集成度最高的 Next.js 模板：博客/项目/Now/订阅/Analytics 都齐了 | [📄](./personal-site/entries/thedevdavid__digital-garden.md) |
| [vercel/nextjs-portfolio-starter](https://github.com/vercel/nextjs-portfolio-starter) | Vercel 官方最小起步模板，从干净画布慢慢往上盖 | [📄](./personal-site/entries/vercel__nextjs-portfolio-starter.md) |
| [apvarun/digital-garden-hugo-theme](https://github.com/apvarun/digital-garden-hugo-theme) | Hugo 主题，极致加载速度，写文章多的人首选 | [📄](./personal-site/entries/apvarun__digital-garden-hugo-theme.md) |
| [kentcdodds/kentcdodds.com](https://github.com/kentcdodds/kentcdodds.com) | React 大佬本人站源码，**不是给 clone 的**，是给你看"个人站当产品做"是啥样 | [📄](./personal-site/entries/kentcdodds__kentcdodds-com.md) |

---

## 主题 10：Claude Code 工作流工程化

**这一组解决什么：** 你已经在用 Claude Code 了，怎么把它玩出体系？这一组是 **skill 工厂、hook SDK、自学习 harness** 等"把 Claude Code 当框架来工程化"的代表项目。是你做 gitout / mem / kb 自己的 skill 时的直接参考库。

📁 详细文档在 `gitout/dev-productivity/claude-workflow/entries/`

| Repo | 大白话讲它干嘛的 | 详细文档 |
| --- | --- | --- |
| [alirezarezvani/claude-code-skill-factory](https://github.com/alirezarezvani/claude-code-skill-factory) | skill / agent / hook / slash 批量生产脚手架，5 条产线带验证 + 打包 ZIP | [📄](./dev-productivity/claude-workflow/entries/alirezarezvani__claude-code-skill-factory.md) |
| [GowayLee/cchooks](https://github.com/GowayLee/cchooks) | Claude Code hook 的 Python SDK，9 种事件类型化，一行代码灭样板 | [📄](./dev-productivity/claude-workflow/entries/GowayLee__cchooks.md) |
| [parcadei/Continuous-Claude-v3](https://github.com/parcadei/Continuous-Claude-v3) | 109 skill + 32 agent + 30 hook 的完整自学习 harness 样板 | [📄](./dev-productivity/claude-workflow/entries/parcadei__Continuous-Claude-v3.md) |
| [BayramAnnakov/claude-reflect](https://github.com/BayramAnnakov/claude-reflect) | 监听你纠正 Claude 的瞬间 → 自动 `/reflect` 写进 CLAUDE.md，从 session 历史挖 skill | [📄](./dev-productivity/claude-workflow/entries/BayramAnnakov__claude-reflect.md) |
| [starbaser/ccproxy](https://github.com/starbaser/ccproxy) | LiteLLM 代理 + hook pipeline + 规则引擎，多模型路由器 | [📄](./dev-productivity/claude-workflow/entries/starbaser__ccproxy.md) |

---

## 主题 11：AI Coding Agent 框架

**这一组解决什么：** Claude Code 之外，**自主 AI 编程代理**还有哪些值得参考？这里挑了 5 个差异化样本——从 SWE-Bench 冠军到极简文件循环 agent，看不同的 agent loop / 工具使用 / 沙箱设计如何拼出来。

📁 详细文档在 `gitout/dev-productivity/ai-coding-agent/entries/`

| Repo | 大白话讲它干嘛的 | 详细文档 |
| --- | --- | --- |
| [OpenHands/OpenHands](https://github.com/OpenHands/OpenHands) | SWE-Bench 77.6 分，Devin 开源平替，Docker 沙箱 + event stream 架构教科书 | [📄](./dev-productivity/ai-coding-agent/entries/OpenHands__OpenHands.md) |
| [cline/cline](https://github.com/cline/cline) | 一套核心引擎驱动 CLI/SDK/VS Code/JetBrains/Kanban 五形态，工程化范本 | [📄](./dev-productivity/ai-coding-agent/entries/cline__cline.md) |
| [Aider-AI/aider](https://github.com/Aider-AI/aider) | 老牌终端 pair programmer，repo-map + 自动 git commit，最不挑模型 | [📄](./dev-productivity/ai-coding-agent/entries/Aider-AI__aider.md) |
| [iannuttall/ralph](https://github.com/iannuttall/ralph) | 极简 file-based agent loop，把 Claude Code/Codex 当 backend，跟 /gitout 同哲学 | [📄](./dev-productivity/ai-coding-agent/entries/iannuttall__ralph.md) |
| [dollspace-gay/OpenClaudia](https://github.com/dollspace-gay/OpenClaudia) | Rust 写的 Claude Code 复刻品，相当于逆向工程版 + 多模型解锁 | [📄](./dev-productivity/ai-coding-agent/entries/dollspace-gay__OpenClaudia.md) |

---

## 主题 12：IDE 增强 / 编辑器 AI 集成

**这一组解决什么：** 你在 VSCode 或 Neovim 里写代码，怎么把 AI 助手装进编辑器、怎么用包管理器统一各种 LSP/格式化器。这里的 5 个项目代表"编辑器层工程化"的当下最佳实践。

📁 详细文档在 `gitout/dev-productivity/ide-augment/entries/`

| Repo | 大白话讲它干嘛的 | 详细文档 |
| --- | --- | --- |
| [continuedev/continue](https://github.com/continuedev/continue) | 跨 VSCode/JetBrains 的开源 AI 助手，core 复用 + prompt 版本化的 monorepo 范本 | [📄](./dev-productivity/ide-augment/entries/continuedev__continue.md) |
| [TabbyML/tabby](https://github.com/TabbyML/tabby) | 自托管的 Copilot 替代，Rust server + 多 IDE 客户端 + OpenAPI | [📄](./dev-productivity/ide-augment/entries/TabbyML__tabby.md) |
| [yetone/avante.nvim](https://github.com/yetone/avante.nvim) | Neovim 版 Cursor，含 ACP 对接 Claude Code，`avante.md` 同构 CLAUDE.md | [📄](./dev-productivity/ide-augment/entries/yetone__avante.nvim.md) |
| [olimorris/codecompanion.nvim](https://github.com/olimorris/codecompanion.nvim) | Neovim 里的 prompt library + slash command + adapter，最契合 skill 体系 | [📄](./dev-productivity/ide-augment/entries/olimorris__codecompanion.nvim.md) |
| [mason-org/mason.nvim](https://github.com/mason-org/mason.nvim) | Neovim 跨平台包管理器，管 LSP/DAP/Linter/Formatter，工程化教科书 | [📄](./dev-productivity/ide-augment/entries/mason-org__mason.nvim.md) |

---

## 主题 13：开发者生产力工具（非 AI）

**这一组解决什么：** 故意挑一组**不带 AI 也能让你 10x** 的工具——命令行加速器、TUI 应用、dotfile 管理。给前面三个 AI 方向做反向参照：很多事情其实手工流水线就够好用，不一定都要 LLM。

📁 详细文档在 `gitout/dev-productivity/personal-tools/entries/`

| Repo | 大白话讲它干嘛的 | 详细文档 |
| --- | --- | --- |
| [Gaurav-Gosain/tuios](https://github.com/Gaurav-Gosain/tuios) | 现代版 terminal multiplexer，Charm 栈 + BSP 布局 + Kitty 图形协议 | [📄](./dev-productivity/personal-tools/entries/Gaurav-Gosain__tuios.md) |
| [fpgmaas/justx](https://github.com/fpgmaas/justx) | 给 `just` 任务运行器套个 TUI 启动器，支持全局 recipe 库 | [📄](./dev-productivity/personal-tools/entries/fpgmaas__justx.md) |
| [SuperCuber/dotter](https://github.com/SuperCuber/dotter) | Rust 写的 dotfile 管理器，模板渲染 + symlink 双层，跨机器差异化配置 | [📄](./dev-productivity/personal-tools/entries/SuperCuber__dotter.md) |
| [abhixdd/ghgrab](https://github.com/abhixdd/ghgrab) | 不用 clone 整个仓库就能挑文件下载，支持 GitHub/GitLab/Gitea 等 5 大 forge | [📄](./dev-productivity/personal-tools/entries/abhixdd__ghgrab.md) |
| [alejandroqh/term39](https://github.com/alejandroqh/term39) | 复古 MS-DOS 风 terminal multiplexer，全平台 + framebuffer + 锁屏，趣味工程 | [📄](./dev-productivity/personal-tools/entries/alejandroqh__term39.md) |

---

## 📊 整体统计

- **总项目数**：63（30 misc + 5 server-ops + 4 iot-platform + 4 personal-site + 20 dev-productivity）
- **已停更但仍收录**：3 个（WeChatMsg、dendron、Discord 导出器维护模式）—— 思路或窗口期价值还在
- **重型参考向（别整站 clone）**：jetlinks、kentcdodds.com、OpenHands —— 是给你读架构的，不是给你拿来用的

## 🎯 几条快速建议

1. **想搭个人产品起点：** 主题 9 选 `thedevdavid/digital-garden`，配合 Claude Code 改起来最顺
2. **想搞个 VPS 跑点东西：** 主题 7 不知道选啥就 `1Panel`，想轻量就 `AcePanel`
3. **想做 OpenClaw / Agent 产品：** 主题 1 + 主题 3 + 主题 11 一起看，先看 `open-interpreter` 学自托管 agent，再看 `OpenHands` 学 sandbox/event stream，最后看 `iannuttall/ralph` 学极简 agent loop
4. **想升级自己的 skill 工程：** 主题 10 是直接对照，`claude-code-skill-factory` 看产线、`cchooks` 看 hook SDK 设计、`claude-reflect` 看"自学习"机制
5. **想做 weixinjilu：** 主题 4 `LC044/WeChatMsg` 趁能用赶紧研究，长线靠 `HPI` 的"个人数据包"思路立差异

---

## 🔗 相关位置

- 各 domain 健康度：`gitout/<domain>/README.md`
- 各 domain 索引：`gitout/<domain>/index.yaml`
- dev-productivity 是四子域：`gitout/dev-productivity/{claude-workflow, ai-coding-agent, ide-augment, personal-tools}/`
- 原始 gh search 数据：`gitout/raw/<日期>/<主题>/`

*主题 1-6 由 /gitout 主题批量扫描生成 · 2026-05-22*
*主题 7-9 由 /gitout 自然语言模式分别生成 · 2026-05-23*
*主题 10-13 由 /gitout 多 agent 并行模式生成 · 2026-05-23*
