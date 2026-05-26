# gitout · 主题导航索引

> 用 `/gitout` 累积的 GitHub 项目地图。每个 domain 一个目录，每条都有大白话简介 + 详细文档链接。
> 最后更新：2026-05-24 · stars 数据快照于同日

---

## 🧭 15 个 domain 一览

| Domain | 一句话 | 项目数 | 首推 |
| --- | --- | --- | --- |
| [[#cli-wrap--cli-包装--把工具变成-ai-能用的命令|📦 cli-wrap]] | 让 AI 调命令行，或把任意软件包装成 Agent 接口 | 5 | open-interpreter (63.6k) |
| [[#voice-pipeline--语音-pipeline--实时对话技术栈|🎙️ voice-pipeline]] | 跟 AI 实时语音对话的底座 | 5 | fastrtc (4.6k) |
| [[#claude-skills--claude-code-生态--skill-和-hooks|⚙️ claude-skills]] | Claude Code skill/hook/subagent 入门 | 5 | awesome-claude-code (44.5k) |
| [[#im-export--聊天记录导出--个人数据归档|💬 im-export]] | 微信/iMessage/Discord 历史导出 | 5 | WeChatMsg (41.5k) |
| [[#personal-kb--个人知识库--markdown-wiki|📚 personal-kb]] | 本地优先的 Markdown 笔记 + 互链 + 可发布 | 5 | logseq (43.0k) |
| [[#ai-avatar--ai-虚拟角色--live2d-桌宠|🤖 ai-avatar]] | 给 AI 套个皮：能动嘴、有表情、能聊天 | 5 | airi (39.5k) |
| [[#server-ops--服务器搭建管理面板|🖥️ server-ops]] | Web 面板鼠标点点搞定服务器 | 5 | 1Panel (35.5k) |
| [[#iot-platform--物联网平台|🌐 iot-platform]] | MQTT + 规则引擎 + Dashboard 完整 IoT 后台 | 4 | FastBee (2.2k) |
| [[#personal-site--个人网站全栈模板|🏠 personal-site]] | 博客 + 项目展示 + Now 页一个 starter 搞定 | 4 | digital-garden (331) |
| [[#dev-productivityclaude-workflow--claude-code-工作流工程化|🛠️ dev-productivity/claude-workflow]] | skill 工厂 / hook SDK / 自学习 harness | 5 | Continuous-Claude-v3 (3.8k) |
| [[#dev-productivityai-coding-agent--ai-coding-agent-框架|🚀 dev-productivity/ai-coding-agent]] | Claude Code 之外的自主代码代理参考 | 5 | OpenHands (74.6k) |
| [[#dev-productivityide-augment--ide-增强--编辑器-ai-集成|✏️ dev-productivity/ide-augment]] | VSCode/Neovim 里的 AI 编程插件 | 5 | continue (33.3k) |
| [[#dev-productivitypersonal-tools--开发者生产力工具非-ai|🧰 dev-productivity/personal-tools]] | 不带 AI 也能让你 10x 的工具 | 5 | tuios (2.7k) |
| [[#xiaozhi-ai--xiaozhi-语音对话硬件生态|🗣️ xiaozhi-ai]] | ESP32 + LLM 端侧 AI 语音盒子生态 | 5 | xiaozhi-esp32 (26.7k) |
| [[#personality-test--性格-心理测试|🧠 personality-test]] | MBTI 等性格测试的开源实现（webapp / 小程序 / 题库 API） | 5 | yudada (385) |

**合计 73 个项目**

---

## cli-wrap — CLI 包装 / 把工具变成 AI 能用的命令

**解决什么：** AI 想真正帮你干活，得能调用电脑上的工具。这里要么让 AI 直接跑命令，要么把任意软件包装成 Agent 可调接口。

**⭐ 首推 `open-interpreter`：** 入门最快的"自然语言→代码执行"路径，社区最大（63.6k 星），文档齐全；想要更 Unix 风的管道组合就上 `Fabric`；想做长期对话归档就用 `simonw/llm`（自动入 SQLite）。

| Repo | ⭐ | 大白话 | 详细文档 |
| --- | ---: | --- | --- |
| [openinterpreter/open-interpreter](https://github.com/openinterpreter/open-interpreter) | 63.6k | 自然语言提需求，AI 直接在电脑上写代码并执行 | [[cli-wrap/entries/openinterpreter__open-interpreter|📄]] |
| [danielmiessler/Fabric](https://github.com/danielmiessler/Fabric) | 41.8k | 把"问 AI"做成 Unix 命令，几百个现成 prompt 像管道组合 | [[cli-wrap/entries/danielmiessler__Fabric|📄]] |
| [simonw/llm](https://github.com/simonw/llm) | 11.9k | 命令行调各种大模型的瑞士军刀，对话自动存 SQLite | [[cli-wrap/entries/simonw__llm|📄]] |
| [TheR1D/shell_gpt](https://github.com/TheR1D/shell_gpt) | 12.1k | 描述要干啥（如"找出最大 5 个文件"）→ 生成 shell 命令 | [[cli-wrap/entries/TheR1D__shell_gpt|📄]] |
| [kellyjonbrazil/jc](https://github.com/kellyjonbrazil/jc) | 8.6k | 把 150+ Unix 命令输出变成 JSON，AI 一眼能读懂 | [[cli-wrap/entries/kellyjonbrazil__jc|📄]] |

---

## voice-pipeline — 语音 pipeline / 实时对话技术栈

**解决什么：** 想做能跟你说话的 AI，得拼麦克风接入、自然语音生成、低延迟。这里挑了不同环节的代表。

**⭐ 首推 `fastrtc`（4.6k）：** Python 函数 → WebRTC 流，是把"语音对话"做成 Web 服务最短的路径。中文 TTS 用 `MOSS-TTS`，多人对话生成（播客）用 `MOSS-TTSD`，Mac 本地推理用 `speech-swift`。

| Repo | ⭐ | 大白话 | 详细文档 |
| --- | ---: | --- | --- |
| [gradio-app/fastrtc](https://github.com/gradio-app/fastrtc) | 4.6k | 写 Python 函数就变 WebRTC 视频/语音流，甚至能接电话 | [[voice-pipeline/entries/gradio-app__fastrtc|📄]] |
| [OpenMOSS/MOSS-TTS](https://github.com/OpenMOSS/MOSS-TTS) | 1.9k | 复旦开源中文 TTS，文字转语音、流式输出、商用友好 | [[voice-pipeline/entries/OpenMOSS__MOSS-TTS|📄]] |
| [OpenMOSS/MOSS-TTSD](https://github.com/OpenMOSS/MOSS-TTSD) | 1.3k | 给一份剧本，生成多人对话语音——做播客/有声书神器 | [[voice-pipeline/entries/OpenMOSS__MOSS-TTSD|📄]] |
| [Liquid4All/liquid-audio](https://github.com/Liquid4All/liquid-audio) | 513 | 1.5B 小模型直接"听到→说出"，跳过文字中转 | [[voice-pipeline/entries/Liquid4All__liquid-audio|📄]] |
| [soniqo/speech-swift](https://github.com/soniqo/speech-swift) | 749 | Mac M 系列本地跑语音识别+合成，不用上云 | [[voice-pipeline/entries/soniqo__speech-swift|📄]] |

---

## claude-skills — Claude Code 生态 / Skill 和 Hooks

**解决什么：** Claude Code 不只是聊天，能装 skill、配 hook、塞 subagent。这里是把它玩花的入门起点（工程化体系向见 `dev-productivity/claude-workflow`）。

**⭐ 首推 `awesome-claude-code`（44.5k）：** 整个生态唯一聚合页，找 skill / hook / extension 第一站。学 hook 写法直接对照 `claude-code-hooks-mastery`（13 种事件完整示例），写自己的应用用官方 SDK。

| Repo | ⭐ | 大白话 | 详细文档 |
| --- | ---: | --- | --- |
| [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | 44.5k | Claude Code 整个生态的"黄页" | [[claude-skills/entries/hesreallyhim__awesome-claude-code|📄]] |
| [VoltAgent/awesome-claude-code-subagents](https://github.com/VoltAgent/awesome-claude-code-subagents) | 20.3k | 131+ 个角色化 subagent，一键安装 | [[claude-skills/entries/VoltAgent__awesome-claude-code-subagents|📄]] |
| [anthropics/claude-agent-sdk-python](https://github.com/anthropics/claude-agent-sdk-python) | 7.0k | 官方 Python SDK | [[claude-skills/entries/anthropics__claude-agent-sdk-python|📄]] |
| [disler/claude-code-hooks-mastery](https://github.com/disler/claude-code-hooks-mastery) | 3.7k | 13 种 hook 事件全讲清楚，附完整示例 | [[claude-skills/entries/disler__claude-code-hooks-mastery|📄]] |
| [coleam00/claude-memory-compiler](https://github.com/coleam00/claude-memory-compiler) | 1.1k | 聊天记录自动整理成知识库 | [[claude-skills/entries/coleam00__claude-memory-compiler|📄]] |

---

## im-export — 聊天记录导出 / 个人数据归档

**解决什么：** 微信/iMessage/Discord 历史锁在 App 里，导出来才能变成数据资产。三条主流路线 + 一个"人生即 Python 包"的终极思路。

**⭐ 首推 `WeChatMsg`（41.5k）：** 中文圈唯一可用的微信导出方案，**作者已停更**，趁还能用赶紧导。iMessage 用 `imessage-exporter`，Discord 用 `DiscordChatExporter`，长线学 `karlicoss/HPI` 的"人生即 Python 包"思路。

| Repo | ⭐ | 大白话 | 详细文档 |
| --- | ---: | --- | --- |
| [LC044/WeChatMsg](https://github.com/LC044/WeChatMsg) | 41.5k | 中文圈微信导出工具之王，**作者已不再更新**，趁能用赶紧导 | [[im-export/entries/LC044__WeChatMsg|📄]] |
| [Tyrrrz/DiscordChatExporter](https://github.com/Tyrrrz/DiscordChatExporter) | 11.2k | Discord 频道/私信完整导出 HTML / JSON | [[im-export/entries/Tyrrrz__DiscordChatExporter|📄]] |
| [ReagentX/imessage-exporter](https://github.com/ReagentX/imessage-exporter) | 5.2k | Rust 写的 iMessage 完整导出器 | [[im-export/entries/ReagentX__imessage-exporter|📄]] |
| [karlicoss/promnesia](https://github.com/karlicoss/promnesia) | 1.9k | 浏览器插件：打开网页就提醒"两年前在哪聊过这个" | [[im-export/entries/karlicoss__promnesia|📄]] |
| [karlicoss/HPI](https://github.com/karlicoss/HPI) | 1.6k | 大开脑洞：把人生数据做成 Python 包 | [[im-export/entries/karlicoss__HPI|📄]] |

---

## personal-kb — 个人知识库 / Markdown wiki

**解决什么：** Notion 那一套但本地、可掌控。Markdown + 互链 + 可发布。五大流派各挑代表。

**⭐ 首推 `logseq`（43.0k）：** 大纲式笔记 + 双链 + 本地优先，对标 Roam Research，社区生态最完整。VSCode 用户直接 `foam`（边写代码边记笔记），想发"数字花园"网站用 `quartz`。

| Repo | ⭐ | 大白话 | 详细文档 |
| --- | ---: | --- | --- |
| [logseq/logseq](https://github.com/logseq/logseq) | 43.0k | 大纲式笔记，对标 Roam Research | [[personal-kb/entries/logseq__logseq|📄]] |
| [foambubble/foam](https://github.com/foambubble/foam) | 17.1k | 让 VSCode 变 Obsidian——边写代码边记笔记 | [[personal-kb/entries/foambubble__foam|📄]] |
| [jackyzha0/quartz](https://github.com/jackyzha0/quartz) | 12.2k | Markdown 一键变"数字花园"网站 | [[personal-kb/entries/jackyzha0__quartz|📄]] |
| [dendronhq/dendron](https://github.com/dendronhq/dendron) | 7.4k | 用文件名做层级的 PKM，**已停更但思路值得参考** | [[personal-kb/entries/dendronhq__dendron|📄]] |
| [silverbulletmd/silverbullet](https://github.com/silverbulletmd/silverbullet) | 5.3k | 浏览器里跑的笔记，Lua 脚本加任何动态功能 | [[personal-kb/entries/silverbulletmd__silverbullet|📄]] |

---

## ai-avatar — AI 虚拟角色 / Live2D 桌宠

**解决什么：** 给 AI 套个皮：能动嘴、有表情、能眨眼、会撒娇。开源虚拟主播 / Live2D 桌宠 / 互动角色代表方案。

**⭐ 首推 `airi`（39.5k）：** Live2D + VRM 双轨支持，眼神/口型/表情都可定制，社区活跃。要"开箱即用 Windows + N 卡"上 `handcrafted-persona-engine`，要学原理读小巧的 `Live2D-LLM-Chat`。

| Repo | ⭐ | 大白话 | 详细文档 |
| --- | ---: | --- | --- |
| [moeru-ai/airi](https://github.com/moeru-ai/airi) | 39.5k | 带 2D/3D 形象的对话机器人，眼神/口型/表情全可定制 | [[ai-avatar/entries/moeru-ai__airi|📄]] |
| [elevenyellow/handcrafted-persona-engine](https://github.com/elevenyellow/handcrafted-persona-engine) | 1.3k | Live2D + 口型 + 表情一条龙，DIY 自由度最高 | [[ai-avatar/entries/elevenyellow__handcrafted-persona-engine|📄]] |
| [whoiswennie/AI-Vtuber](https://github.com/whoiswennie/AI-Vtuber) | 445 | 全栈虚拟主播方案，含意图识别、长短期记忆 | [[ai-avatar/entries/whoiswennie__AI-Vtuber|📄]] |
| [chyinan/Kokoro-Engine](https://github.com/chyinan/Kokoro-Engine) | 82 | Live2D + MOD 系统，高自由度可玩对话角色 | [[ai-avatar/entries/chyinan__Kokoro-Engine|📄]] |
| [suzuran0y/Live2D-LLM-Chat](https://github.com/suzuran0y/Live2D-LLM-Chat) | 39 | 眼神追踪 + 口型同步最小可学示例 | [[ai-avatar/entries/suzuran0y__Live2D-LLM-Chat|📄]] |

---

## server-ops — 服务器搭建管理面板

**解决什么：** 你买了台 VPS 或家里有台小主机，但配 Nginx、装 MySQL、跑 Docker 一堆命令背不下来。这些项目让你浏览器点点就能搞定。

**⭐ 首推 `1Panel`（35.5k）：** 国产现代化全能面板、165+ 应用一键装、Docker 一体化，不知道选啥就用它。家用 NAS / 小主机用 `CasaOS`（33.9k），要轻量纯中文用 `AcePanel`，老牌邮件/DNS 服务管理用 `webmin`。

| Repo | ⭐ | 大白话 | 详细文档 |
| --- | ---: | --- | --- |
| [1Panel-dev/1Panel](https://github.com/1Panel-dev/1Panel) | 35.5k | 国产现代化全能面板，165+ 应用一键装、容器管理一体化 | [[server-ops/entries/1Panel-dev__1Panel|📄]] |
| [IceWhaleTech/CasaOS](https://github.com/IceWhaleTech/CasaOS) | 33.9k | 家用小主机的"个人云"系统，UI 像 iPad，NAS 场景 | [[server-ops/entries/IceWhaleTech__CasaOS|📄]] |
| [webmin/webmin](https://github.com/webmin/webmin) | 5.7k | 1997 年至今的"祖师爷"，传统 Linux 服务管理王者 | [[server-ops/entries/webmin__webmin|📄]] |
| [aaPanel/aaPanel](https://github.com/aaPanel/aaPanel) | 3.0k | 宝塔国际版，60M 内存就能跑，PHP 建站老朋友 | [[server-ops/entries/aaPanel__aaPanel|📄]] |
| [acepanel/panel](https://github.com/acepanel/panel) | 2.8k | Go 单文件运行、轻量不破坏系统的中文面板（耗子面板新版） | [[server-ops/entries/acepanel__panel|📄]] |

---

## iot-platform — 物联网平台

**解决什么：** 一堆设备（传感器、灯、网关）要联网管理，需要一套完整后台：MQTT 接入、设备列表、规则引擎、可视化大屏、手机 App。

**⭐ 首推 `FastBee`（2.2k）：** 国产全栈轻量 IoT 平台，含 Web 控制台 + 微信小程序 + App，三件套开箱即用，最适合 PoC 起步。`jetlinks`（6.5k 但企业级）只看架构别整站 clone，`tinyIoT` 几千行纯 C 学底层最佳。

| Repo | ⭐ | 大白话 | 详细文档 |
| --- | ---: | --- | --- |
| [jetlinks/jetlinks-community](https://github.com/jetlinks/jetlinks-community) | 6.5k | 企业级响应式 IoT 平台，**架构参考别通读** | [[iot-platform/entries/jetlinks__jetlinks-community|📄]] |
| [kerwincui/FastBee](https://github.com/kerwincui/FastBee) | 2.2k | 国产全栈轻量 IoT 平台，含 Web + 小程序 + App，开箱即用 | [[iot-platform/entries/kerwincui__FastBee|📄]] |
| [IoTSharp/IoTSharp](https://github.com/IoTSharp/IoTSharp) | 1.3k | .NET 版"小号 ThingsBoard"，规则链 + 多租户齐全 | [[iot-platform/entries/IoTSharp__IoTSharp|📄]] |
| [seslabSJU/tinyIoT](https://github.com/seslabSJU/tinyIoT) | 9 | 纯 C 极简 IoT 服务，几千行能读完，学底层最佳教材 | [[iot-platform/entries/seslabSJU__tinyIoT|📄]] |

---

## personal-site — 个人网站全栈模板

**解决什么：** 想搭"超级主页"——博客、项目展示、Now 页、关于、订阅、统计全都要，但又不想从零写。

**⭐ 首推 `digital-garden`（331）：** Next.js 模板集成度最高，博客/项目/Now/订阅/Analytics 全齐，配 Claude Code 改起来最顺。要"从干净画布往上盖"用 Vercel 官方 starter；要极致加载速度的文章党用 Hugo 主题；`kentcdodds.com` 是大佬本人站源码，**给你读"个人站当产品做"，不是给 clone 的**。

| Repo | ⭐ | 大白话 | 详细文档 |
| --- | ---: | --- | --- |
| [kentcdodds/kentcdodds.com](https://github.com/kentcdodds/kentcdodds.com) | 2.5k | React 大佬本人站源码，**不是给 clone 的**，看"个人站当产品做"是啥样 | [[personal-site/entries/kentcdodds__kentcdodds-com|📄]] |
| [vercel/nextjs-portfolio-starter](https://github.com/vercel/nextjs-portfolio-starter) | 731 | Vercel 官方最小起步模板 | [[personal-site/entries/vercel__nextjs-portfolio-starter|📄]] |
| [thedevdavid/digital-garden](https://github.com/thedevdavid/digital-garden) | 331 | 集成度最高的 Next.js 模板：博客/项目/Now/订阅/Analytics 全齐 | [[personal-site/entries/thedevdavid__digital-garden|📄]] |
| [apvarun/digital-garden-hugo-theme](https://github.com/apvarun/digital-garden-hugo-theme) | 296 | Hugo 主题，极致加载速度，文章党首选 | [[personal-site/entries/apvarun__digital-garden-hugo-theme|📄]] |

---

## dev-productivity/claude-workflow — Claude Code 工作流工程化

**解决什么：** 已经用 Claude Code 了，怎么玩出体系？skill 工厂、hook SDK、自学习 harness 等"把 Claude Code 当框架工程化"的代表项目。

**⭐ 首推 `Continuous-Claude-v3`（3.8k）：** 109 skill + 32 agent + 30 hook 的自学习 harness 完整样板，直接对照搭自己的体系。批量做 skill 看 `skill-factory`，写 hook 用 `cchooks` 灭样板。

| Repo | ⭐ | 大白话 | 详细文档 |
| --- | ---: | --- | --- |
| [parcadei/Continuous-Claude-v3](https://github.com/parcadei/Continuous-Claude-v3) | 3.8k | 109 skill + 32 agent + 30 hook 的自学习 harness 样板 | [[dev-productivity/claude-workflow/entries/parcadei__Continuous-Claude-v3|📄]] |
| [BayramAnnakov/claude-reflect](https://github.com/BayramAnnakov/claude-reflect) | 1.0k | 监听你纠正 Claude → 自动 `/reflect` 写进 CLAUDE.md | [[dev-productivity/claude-workflow/entries/BayramAnnakov__claude-reflect|📄]] |
| [alirezarezvani/claude-code-skill-factory](https://github.com/alirezarezvani/claude-code-skill-factory) | 782 | skill / agent / hook / slash 批量生产脚手架 | [[dev-productivity/claude-workflow/entries/alirezarezvani__claude-code-skill-factory|📄]] |
| [starbaser/ccproxy](https://github.com/starbaser/ccproxy) | 400 | LiteLLM 代理 + hook pipeline + 规则引擎，多模型路由器 | [[dev-productivity/claude-workflow/entries/starbaser__ccproxy|📄]] |
| [GowayLee/cchooks](https://github.com/GowayLee/cchooks) | 131 | Claude Code hook 的 Python SDK，9 种事件类型化 | [[dev-productivity/claude-workflow/entries/GowayLee__cchooks|📄]] |

---

## dev-productivity/ai-coding-agent — AI Coding Agent 框架

**解决什么：** Claude Code 之外，还有哪些值得参考的自主 AI 编程代理？从 SWE-Bench 冠军到极简文件循环 agent。

**⭐ 首推 `OpenHands`（74.6k）：** SWE-Bench 77.6 分、Devin 开源平替，Docker 沙箱 + event stream 架构是教科书级参考。要"一套引擎多形态"看 `cline`；老牌终端 pair programmer 看 `aider`；极简哲学看 `ralph`（跟 /gitout 同路线）。

| Repo | ⭐ | 大白话 | 详细文档 |
| --- | ---: | --- | --- |
| [OpenHands/OpenHands](https://github.com/OpenHands/OpenHands) | 74.6k | SWE-Bench 77.6 分，Devin 开源平替，Docker 沙箱 + event stream 教科书 | [[dev-productivity/ai-coding-agent/entries/OpenHands__OpenHands|📄]] |
| [cline/cline](https://github.com/cline/cline) | 62.2k | 一套核心引擎驱动 CLI/SDK/VS Code/JetBrains/Kanban 五形态 | [[dev-productivity/ai-coding-agent/entries/cline__cline|📄]] |
| [Aider-AI/aider](https://github.com/Aider-AI/aider) | 45.2k | 老牌终端 pair programmer，repo-map + 自动 git commit | [[dev-productivity/ai-coding-agent/entries/Aider-AI__aider|📄]] |
| [iannuttall/ralph](https://github.com/iannuttall/ralph) | 924 | 极简 file-based agent loop，跟 /gitout 同哲学 | [[dev-productivity/ai-coding-agent/entries/iannuttall__ralph|📄]] |
| [dollspace-gay/OpenClaudia](https://github.com/dollspace-gay/OpenClaudia) | 71 | Rust 写的 Claude Code 复刻品 | [[dev-productivity/ai-coding-agent/entries/dollspace-gay__OpenClaudia|📄]] |

---

## dev-productivity/ide-augment — IDE 增强 / 编辑器 AI 集成

**解决什么：** 在 VSCode 或 Neovim 里写代码，怎么把 AI 助手装进编辑器、怎么用包管理器统一 LSP/格式化器。

**⭐ 首推 `continue`（33.3k）：** 跨 VSCode/JetBrains 的开源 AI 助手，core 复用 + prompt 版本化 monorepo 是工程化范本。要自托管 Copilot 替代用 `tabby`；Neovim 党看 `avante.nvim` 或更契合 skill 体系的 `codecompanion.nvim`；统一 LSP/Linter/Formatter 工具链用 `mason.nvim`。

| Repo | ⭐ | 大白话 | 详细文档 |
| --- | ---: | --- | --- |
| [TabbyML/tabby](https://github.com/TabbyML/tabby) | 33.5k | 自托管 Copilot 替代，Rust server + 多 IDE 客户端 | [[dev-productivity/ide-augment/entries/TabbyML__tabby|📄]] |
| [continuedev/continue](https://github.com/continuedev/continue) | 33.3k | 跨 VSCode/JetBrains 开源 AI 助手，core 复用 + monorepo 范本 | [[dev-productivity/ide-augment/entries/continuedev__continue|📄]] |
| [yetone/avante.nvim](https://github.com/yetone/avante.nvim) | 17.9k | Neovim 版 Cursor，含 ACP 对接 Claude Code | [[dev-productivity/ide-augment/entries/yetone__avante.nvim|📄]] |
| [mason-org/mason.nvim](https://github.com/mason-org/mason.nvim) | 10.3k | Neovim 跨平台包管理器，管 LSP/DAP/Linter/Formatter | [[dev-productivity/ide-augment/entries/mason-org__mason.nvim|📄]] |
| [olimorris/codecompanion.nvim](https://github.com/olimorris/codecompanion.nvim) | 6.6k | Neovim 里的 prompt library + slash + adapter，最契合 skill 体系 | [[dev-productivity/ide-augment/entries/olimorris__codecompanion.nvim|📄]] |

---

## dev-productivity/personal-tools — 开发者生产力工具（非 AI）

**解决什么：** 故意挑一组**不带 AI 也能让你 10x** 的工具——命令行加速器、TUI 应用、dotfile 管理。给 AI 路线做反向参照。

**⭐ 首推 `tuios`（2.7k）：** 现代版 terminal multiplexer，Charm 栈 + BSP 布局 + Kitty 图形协议，颜值与工程实力兼备。跨机器配置同步用 `dotter`；不 clone 整仓库就挑文件用 `ghgrab`；just 任务运行器套 TUI 用 `justx`；纯趣味工程看 `term39`（复古 MS-DOS 风）。

| Repo | ⭐ | 大白话 | 详细文档 |
| --- | ---: | --- | --- |
| [Gaurav-Gosain/tuios](https://github.com/Gaurav-Gosain/tuios) | 2.7k | 现代版 terminal multiplexer，Charm 栈 + BSP 布局 | [[dev-productivity/personal-tools/entries/Gaurav-Gosain__tuios|📄]] |
| [SuperCuber/dotter](https://github.com/SuperCuber/dotter) | 2.0k | Rust dotfile 管理器，模板渲染 + symlink 双层 | [[dev-productivity/personal-tools/entries/SuperCuber__dotter|📄]] |
| [abhixdd/ghgrab](https://github.com/abhixdd/ghgrab) | 996 | 不用 clone 整仓库就能挑文件下载（GitHub/GitLab/Gitea 等） | [[dev-productivity/personal-tools/entries/abhixdd__ghgrab|📄]] |
| [alejandroqh/term39](https://github.com/alejandroqh/term39) | 191 | 复古 MS-DOS 风 terminal multiplexer，全平台 + framebuffer | [[dev-productivity/personal-tools/entries/alejandroqh__term39|📄]] |
| [fpgmaas/justx](https://github.com/fpgmaas/justx) | 162 | 给 `just` 任务运行器套个 TUI 启动器 | [[dev-productivity/personal-tools/entries/fpgmaas__justx|📄]] |

---

## xiaozhi-ai — xiaozhi 语音对话硬件生态

**解决什么：** DIY 一个能跟你说话的 AI 小盒子。xiaozhi 是中文圈最火的 ESP32 + LLM 语音助手开源生态。原版固件 + 三语言后端 + 移动端客户端，组成完整链路。

**⭐ 首推 `xiaozhi-esp32`（26.7k）：** 虾哥本尊的原版固件，整个生态的"祖师爷"。配套自建后端选 `xiaozhi-esp32-server`（社区最火 Python+Java+Vue 三件套），没硬件先在 PC 上跑 `py-xiaozhi` 体验，移动端用 `xiaozhi-android-client`（带 AEC 回音消除）。

| Repo | ⭐ | 大白话 | 详细文档 |
| --- | ---: | --- | --- |
| [78/xiaozhi-esp32](https://github.com/78/xiaozhi-esp32) | 26.7k | 虾哥本尊的 ESP32 AI 语音盒子原版固件 | [[xiaozhi-ai/entries/78__xiaozhi-esp32|📄]] |
| [xinnan-tech/xiaozhi-esp32-server](https://github.com/xinnan-tech/xiaozhi-esp32-server) | 9.6k | 社区最火自建后端，Python+Java+Vue 三件套 | [[xiaozhi-ai/entries/xinnan-tech__xiaozhi-esp32-server|📄]] |
| [huangjunsen0406/py-xiaozhi](https://github.com/huangjunsen0406/py-xiaozhi) | 3.3k | 没硬件也能玩——Python 桌面客户端 | [[xiaozhi-ai/entries/huangjunsen0406__py-xiaozhi|📄]] |
| [TOM88812/xiaozhi-android-client](https://github.com/TOM88812/xiaozhi-android-client) | 1.5k | Flutter 移动端，iOS/Android 双平台，带 AEC 回音消除 | [[xiaozhi-ai/entries/TOM88812__xiaozhi-android-client|📄]] |
| [joey-zhou/xiaozhi-esp32-server-java](https://github.com/joey-zhou/xiaozhi-esp32-server-java) | 1.3k | Java 党的企业级后端，带完整前后端管理平台 | [[xiaozhi-ai/entries/joey-zhou__xiaozhi-esp32-server-java|📄]] |

---

## personality-test — 性格 / 心理测试

**解决什么：** 想给自己/团队/社群部署个 MBTI（或其他性格）测试，从"今晚挂个静态页"到"做个通用答题平台"全档位覆盖。

**⭐ 首推 `yudada`（385）：** 鱼皮老师的 AI 答题平台教学项目，MBTI 是第一阶段，后续可扩展到任意题型——三件套（网页 + 小程序 + 通用题库）唯一全覆盖。零部署玩玩选 `MskTmi/MBTI`，要 Python 自部署选 `zcw576020095/mbti-test`，前端 only 调 `16personalities-api`，做小程序参考 `lilemy/mbti-mini`。

| Repo | ⭐ | 大白话 | 详细文档 |
| --- | ---: | --- | --- |
| [liyupi/yudada](https://github.com/liyupi/yudada) | 385 | 鱼皮 AI 答题平台教学项目，MBTI 起步可扩展通用题库 | [[personality-test/entries/liyupi__yudada|📄]] |
| [zcw576020095/mbti-test](https://github.com/zcw576020095/mbti-test) | 310 | Django MBTI 系统 + PDF 导出，最快可上线 | [[personality-test/entries/zcw576020095__mbti-test|📄]] |
| [MskTmi/MBTI](https://github.com/MskTmi/MBTI) | 161 | 纯静态 93 题中文版，5 分钟挂 Pages | [[personality-test/entries/MskTmi__MBTI|📄]] |
| [SwapnilSoni1999/16personalities-api](https://github.com/SwapnilSoni1999/16personalities-api) | 54 | 16personalities.com 非官方 API，只写前端 | [[personality-test/entries/SwapnilSoni1999__16personalities-api|📄]] |
| [lilemy/mbti-mini](https://github.com/lilemy/mbti-mini) | 1 | TypeScript 微信小程序参考实现 | [[personality-test/entries/lilemy__mbti-mini|📄]] |

---

## 📊 整体统计

- **总项目数**：73（cli-wrap 5 + voice-pipeline 5 + claude-skills 5 + im-export 5 + personal-kb 5 + ai-avatar 5 + server-ops 5 + iot-platform 4 + personal-site 4 + dev-productivity 20 + xiaozhi-ai 5 + personality-test 5）
- **stars 总和**：约 95 万⭐ · 单条最高 OpenHands 74.6k · 中位数约 3k
- **已停更但仍收录**：3 个（WeChatMsg 41.5k、dendron 7.4k、DiscordChatExporter 维护模式）—— 思路或窗口期价值还在
- **重型参考向（别整站 clone）**：jetlinks、kentcdodds.com、OpenHands —— 给你读架构的，不是拿来用的

## 🎯 跨域推荐路径

1. **想搭个人产品起点：** personal-site/`thedevdavid/digital-garden` + Claude Code（配套 claude-skills/`awesome-claude-code` 入门）
2. **想搞个 VPS 跑点东西：** server-ops/`1Panel`（万能） · 想轻量就 `AcePanel`
3. **想做 Agent 产品：** cli-wrap/`open-interpreter` + claude-skills/`anthropics-sdk` + dev-productivity/ai-coding-agent/`OpenHands`（读架构）
4. **想升级 skill 工程：** dev-productivity/claude-workflow/`Continuous-Claude-v3` 是直接对照样板
5. **想做微信记录归档：** im-export/`WeChatMsg` 趁能用赶紧研究 · 长线靠 `HPI` 的"个人数据包"思路立差异

---

## 🔗 目录约定

```
gitout/
├── INDEX.md                          # 本文件，总入口
├── README.md                         # 简介
├── <domain>/                         # 每个 domain 一个目录（kebab-case）
│   ├── README.md                     # domain 健康度 + 当前条目速览
│   ├── index.yaml                    # 结构化条目索引（机器可读）
│   └── entries/<owner>__<repo>.md    # 单个项目的小白说明文档
├── raw/<YYYY-MM-DD>/<intent-slug>/   # gh 检索原始 JSON（只读归档，不进 INDEX）
└── retros/<YYYY-MM-DD>-<主题>-retro.md  # /gitout 复盘文档（不进 INDEX）
```

**详细规则见项目根 `CLAUDE.md`。**

*主题来源：cli-wrap/voice-pipeline/claude-skills/im-export/personal-kb/ai-avatar 由 /gitout 主题批量扫描 · 2026-05-22*
*server-ops/iot-platform/personal-site 由 /gitout 自然语言模式生成 · 2026-05-23*
*dev-productivity 四子域由 /gitout 多 agent 并行模式生成 · 2026-05-23*
*xiaozhi-ai 由 /gitout 自然语言模式生成 · 2026-05-23*
*personality-test 由 /gitout 自然语言模式生成 · 2026-05-24*
