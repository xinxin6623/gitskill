# gitout · 主题导航索引

> 用 `/gitout` 累积的 GitHub 项目地图。每个 domain 一个目录，每条都有大白话简介 + 详细文档链接。
> 最后更新：2026-05-23

---

## 🧭 14 个 domain 一览

| Domain（目录） | 一句话 | 项目数 |
| --- | --- | --- |
| [📦 cli-wrap](#cli-wrap--cli-包装--把工具变成-ai-能用的命令) | 让 AI 调命令行，或把任意软件包装成 Agent 能调的接口 | 5 |
| [🎙️ voice-pipeline](#voice-pipeline--语音-pipeline--实时对话技术栈) | 跟 AI 实时语音对话需要的底座：WebRTC、TTS、本地推理 | 5 |
| [⚙️ claude-skills](#claude-skills--claude-code-生态--skill-和-hooks) | 把 Claude Code 改造成自己工作流的入门样本（skill / hook / subagent / SDK） | 5 |
| [💬 im-export](#im-export--聊天记录导出--个人数据归档) | 把微信/iMessage/Discord 历史导出，变成自己的数据资产 | 5 |
| [📚 personal-kb](#personal-kb--个人知识库--markdown-wiki) | 本地优先的 Markdown 笔记 + 互链 + 可发布 | 5 |
| [🤖 ai-avatar](#ai-avatar--ai-虚拟角色--live2d-桌宠) | 给 AI 套个皮：能动嘴、有表情、能聊天的虚拟形象 | 5 |
| [🖥️ server-ops](#server-ops--服务器搭建管理面板) | 不想敲命令配 Nginx？Web 面板鼠标点点搞定服务器 | 5 |
| [🌐 iot-platform](#iot-platform--物联网平台) | 一套能管 MQTT 设备 + 规则引擎 + Dashboard + 手机 App 的完整 IoT 后台 | 4 |
| [🏠 personal-site](#personal-site--个人网站全栈模板) | 个人"超级主页"：博客、项目展示、Now 页、订阅一个 starter 搞定 | 4 |
| [🛠️ dev-productivity/claude-workflow](#dev-productivityclaude-workflow--claude-code-工作流工程化) | skill 工厂 / hook SDK / 自学习 harness——Claude Code 玩出工程化体系 | 5 |
| [🚀 dev-productivity/ai-coding-agent](#dev-productivityai-coding-agent--ai-coding-agent-框架) | Claude Code 之外的自主代码代理（Aider/Cline/OpenHands）参考样本 | 5 |
| [✏️ dev-productivity/ide-augment](#dev-productivityide-augment--ide-增强--编辑器-ai-集成) | VSCode/Neovim 里的 AI 编程插件 + 包管理器 | 5 |
| [🧰 dev-productivity/personal-tools](#dev-productivitypersonal-tools--开发者生产力工具非-ai) | 命令行加速器 / TUI / dotfile 管理——纯手工提效，跟 AI 路线做对照 | 5 |
| [🗣️ xiaozhi-ai](#xiaozhi-ai--xiaozhi-语音对话硬件生态) | ESP32 + LLM 端侧 AI 语音盒子：原版固件 + 多语言后端 + 跨端客户端 | 5 |

**合计 68 个项目**

---

## cli-wrap — CLI 包装 / 把工具变成 AI 能用的命令

**解决什么：** AI 想真正帮你干活，得能调用电脑上的工具。这里要么让 AI 直接跑命令，要么帮你把任意软件包装成 AI 可理解的接口。

| Repo | 大白话 | 详细文档 |
| --- | --- | --- |
| [openinterpreter/open-interpreter](https://github.com/openinterpreter/open-interpreter) | 自然语言提需求，AI 直接在电脑上写代码并执行 | [📄](./cli-wrap/entries/openinterpreter__open-interpreter.md) |
| [danielmiessler/Fabric](https://github.com/danielmiessler/Fabric) | 把"问 AI"做成 Unix 命令，几百个现成 prompt 像管道组合 | [📄](./cli-wrap/entries/danielmiessler__Fabric.md) |
| [simonw/llm](https://github.com/simonw/llm) | 命令行调各种大模型的瑞士军刀，对话自动存 SQLite | [📄](./cli-wrap/entries/simonw__llm.md) |
| [TheR1D/shell_gpt](https://github.com/TheR1D/shell_gpt) | 描述要干啥（如"找出最大 5 个文件"）→ 生成 shell 命令 | [📄](./cli-wrap/entries/TheR1D__shell_gpt.md) |
| [kellyjonbrazil/jc](https://github.com/kellyjonbrazil/jc) | 把 150+ Unix 命令输出变成 JSON，AI 一眼能读懂 | [📄](./cli-wrap/entries/kellyjonbrazil__jc.md) |

---

## voice-pipeline — 语音 pipeline / 实时对话技术栈

**解决什么：** 想做能跟你说话的 AI，得拼麦克风接入、自然语音生成、低延迟。这里挑了不同环节的代表。

| Repo | 大白话 | 详细文档 |
| --- | --- | --- |
| [gradio-app/fastrtc](https://github.com/gradio-app/fastrtc) | 写 Python 函数就能变 WebRTC 视频/语音流，甚至能接电话 | [📄](./voice-pipeline/entries/gradio-app__fastrtc.md) |
| [OpenMOSS/MOSS-TTS](https://github.com/OpenMOSS/MOSS-TTS) | 复旦开源中文 TTS，文字转语音、流式输出、商用友好 | [📄](./voice-pipeline/entries/OpenMOSS__MOSS-TTS.md) |
| [OpenMOSS/MOSS-TTSD](https://github.com/OpenMOSS/MOSS-TTSD) | 给一份剧本，生成多人对话语音——做播客/有声书神器 | [📄](./voice-pipeline/entries/OpenMOSS__MOSS-TTSD.md) |
| [soniqo/speech-swift](https://github.com/soniqo/speech-swift) | Mac M 系列本地跑语音识别+合成，不用上云 | [📄](./voice-pipeline/entries/soniqo__speech-swift.md) |
| [Liquid4All/liquid-audio](https://github.com/Liquid4All/liquid-audio) | 1.5B 小模型直接"听到→说出"，跳过文字中转 | [📄](./voice-pipeline/entries/Liquid4All__liquid-audio.md) |

---

## claude-skills — Claude Code 生态 / Skill 和 Hooks

**解决什么：** Claude Code 不只是聊天，能装 skill、配 hook、塞 subagent。这里是把它玩花的入门起点（工程化体系向见 `dev-productivity/claude-workflow`）。

| Repo | 大白话 | 详细文档 |
| --- | --- | --- |
| [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | Claude Code 整个生态的"黄页" | [📄](./claude-skills/entries/hesreallyhim__awesome-claude-code.md) |
| [disler/claude-code-hooks-mastery](https://github.com/disler/claude-code-hooks-mastery) | 13 种 hook 事件全讲清楚，附完整示例 | [📄](./claude-skills/entries/disler__claude-code-hooks-mastery.md) |
| [anthropics/claude-agent-sdk-python](https://github.com/anthropics/claude-agent-sdk-python) | 官方 Python SDK | [📄](./claude-skills/entries/anthropics__claude-agent-sdk-python.md) |
| [VoltAgent/awesome-claude-code-subagents](https://github.com/VoltAgent/awesome-claude-code-subagents) | 131+ 个角色化 subagent，一键安装 | [📄](./claude-skills/entries/VoltAgent__awesome-claude-code-subagents.md) |
| [coleam00/claude-memory-compiler](https://github.com/coleam00/claude-memory-compiler) | 聊天记录自动整理成知识库 | [📄](./claude-skills/entries/coleam00__claude-memory-compiler.md) |

---

## im-export — 聊天记录导出 / 个人数据归档

**解决什么：** 微信/iMessage/Discord 历史锁在 App 里，导出来才能变成数据资产。三条主流路线 + 一个"人生即 Python 包"的终极思路。

| Repo | 大白话 | 详细文档 |
| --- | --- | --- |
| [LC044/WeChatMsg](https://github.com/LC044/WeChatMsg) | 中文圈微信导出工具之王，**作者已不再更新**，趁能用赶紧导 | [📄](./im-export/entries/LC044__WeChatMsg.md) |
| [ReagentX/imessage-exporter](https://github.com/ReagentX/imessage-exporter) | Rust 写的 iMessage 完整导出器 | [📄](./im-export/entries/ReagentX__imessage-exporter.md) |
| [Tyrrrz/DiscordChatExporter](https://github.com/Tyrrrz/DiscordChatExporter) | Discord 频道/私信完整导出 HTML / JSON | [📄](./im-export/entries/Tyrrrz__DiscordChatExporter.md) |
| [karlicoss/HPI](https://github.com/karlicoss/HPI) | 大开脑洞：把人生数据做成 Python 包 | [📄](./im-export/entries/karlicoss__HPI.md) |
| [karlicoss/promnesia](https://github.com/karlicoss/promnesia) | 浏览器插件：打开网页就提醒"两年前在哪聊过这个" | [📄](./im-export/entries/karlicoss__promnesia.md) |

---

## personal-kb — 个人知识库 / Markdown wiki

**解决什么：** Notion 那一套但本地、可掌控。Markdown + 互链 + 可发布。五大流派各挑代表。

| Repo | 大白话 | 详细文档 |
| --- | --- | --- |
| [logseq/logseq](https://github.com/logseq/logseq) | 大纲式笔记，对标 Roam Research | [📄](./personal-kb/entries/logseq__logseq.md) |
| [foambubble/foam](https://github.com/foambubble/foam) | 让 VSCode 变 Obsidian——边写代码边记笔记 | [📄](./personal-kb/entries/foambubble__foam.md) |
| [jackyzha0/quartz](https://github.com/jackyzha0/quartz) | Markdown 一键变"数字花园"网站 | [📄](./personal-kb/entries/jackyzha0__quartz.md) |
| [dendronhq/dendron](https://github.com/dendronhq/dendron) | 用文件名做层级的 PKM，**已停更但思路值得参考** | [📄](./personal-kb/entries/dendronhq__dendron.md) |
| [silverbulletmd/silverbullet](https://github.com/silverbulletmd/silverbullet) | 浏览器里跑的笔记，Lua 脚本加任何动态功能 | [📄](./personal-kb/entries/silverbulletmd__silverbullet.md) |

---

## ai-avatar — AI 虚拟角色 / Live2D 桌宠

**解决什么：** 给 AI 套个皮：能动嘴、有表情、能眨眼、会撒娇。开源虚拟主播 / Live2D 桌宠 / 互动角色代表方案。

| Repo | 大白话 | 详细文档 |
| --- | --- | --- |
| [moeru-ai/airi](https://github.com/moeru-ai/airi) | 带 2D/3D 形象的对话机器人，眼神/口型/表情全可定制 | [📄](./ai-avatar/entries/moeru-ai__airi.md) |
| [elevenyellow/handcrafted-persona-engine](https://github.com/elevenyellow/handcrafted-persona-engine) | Live2D + 口型 + 表情一条龙，DIY 自由度最高 | [📄](./ai-avatar/entries/elevenyellow__handcrafted-persona-engine.md) |
| [whoiswennie/AI-Vtuber](https://github.com/whoiswennie/AI-Vtuber) | 全栈虚拟主播方案，含意图识别、长短期记忆 | [📄](./ai-avatar/entries/whoiswennie__AI-Vtuber.md) |
| [chyinan/Kokoro-Engine](https://github.com/chyinan/Kokoro-Engine) | Live2D + MOD 系统，高自由度可玩对话角色 | [📄](./ai-avatar/entries/chyinan__Kokoro-Engine.md) |
| [suzuran0y/Live2D-LLM-Chat](https://github.com/suzuran0y/Live2D-LLM-Chat) | 眼神追踪 + 口型同步最小可学示例 | [📄](./ai-avatar/entries/suzuran0y__Live2D-LLM-Chat.md) |

---

## server-ops — 服务器搭建管理面板

**解决什么：** 你买了台 VPS 或家里有台小主机，但配 Nginx、装 MySQL、跑 Docker 一堆命令背不下来。这些项目让你浏览器点点就能搞定。

| Repo | 大白话 | 详细文档 |
| --- | --- | --- |
| [acepanel/panel](https://github.com/acepanel/panel) | Go 单文件运行、轻量不破坏系统的中文面板（耗子面板新版） | [📄](./server-ops/entries/acepanel__panel.md) |
| [1Panel-dev/1Panel](https://github.com/1Panel-dev/1Panel) | 国产现代化全能面板，165+ 应用一键装、容器管理一体化 | [📄](./server-ops/entries/1Panel-dev__1Panel.md) |
| [IceWhaleTech/CasaOS](https://github.com/IceWhaleTech/CasaOS) | 家用小主机的"个人云"系统，UI 像 iPad，NAS 场景 | [📄](./server-ops/entries/IceWhaleTech__CasaOS.md) |
| [aaPanel/aaPanel](https://github.com/aaPanel/aaPanel) | 宝塔国际版，60M 内存就能跑，PHP 建站老朋友 | [📄](./server-ops/entries/aaPanel__aaPanel.md) |
| [webmin/webmin](https://github.com/webmin/webmin) | 1997 年至今的"祖师爷"，传统 Linux 服务管理王者 | [📄](./server-ops/entries/webmin__webmin.md) |

---

## iot-platform — 物联网平台

**解决什么：** 一堆设备（传感器、灯、网关）要联网管理，需要一套完整后台：MQTT 接入、设备列表、规则引擎、可视化大屏、手机 App。

| Repo | 大白话 | 详细文档 |
| --- | --- | --- |
| [kerwincui/FastBee](https://github.com/kerwincui/FastBee) | 国产全栈轻量 IoT 平台，含 Web + 小程序 + App，开箱即用 | [📄](./iot-platform/entries/kerwincui__FastBee.md) |
| [IoTSharp/IoTSharp](https://github.com/IoTSharp/IoTSharp) | .NET 版"小号 ThingsBoard"，规则链 + 多租户齐全 | [📄](./iot-platform/entries/IoTSharp__IoTSharp.md) |
| [seslabSJU/tinyIoT](https://github.com/seslabSJU/tinyIoT) | 纯 C 极简 IoT 服务，几千行能读完，学底层最佳教材 | [📄](./iot-platform/entries/seslabSJU__tinyIoT.md) |
| [jetlinks/jetlinks-community](https://github.com/jetlinks/jetlinks-community) | 企业级响应式 IoT 平台，**架构参考别通读** | [📄](./iot-platform/entries/jetlinks__jetlinks-community.md) |

---

## personal-site — 个人网站全栈模板

**解决什么：** 想搭"超级主页"——博客、项目展示、Now 页、关于、订阅、统计全都要，但又不想从零写。

| Repo | 大白话 | 详细文档 |
| --- | --- | --- |
| [thedevdavid/digital-garden](https://github.com/thedevdavid/digital-garden) | 集成度最高的 Next.js 模板：博客/项目/Now/订阅/Analytics 全齐 | [📄](./personal-site/entries/thedevdavid__digital-garden.md) |
| [vercel/nextjs-portfolio-starter](https://github.com/vercel/nextjs-portfolio-starter) | Vercel 官方最小起步模板 | [📄](./personal-site/entries/vercel__nextjs-portfolio-starter.md) |
| [apvarun/digital-garden-hugo-theme](https://github.com/apvarun/digital-garden-hugo-theme) | Hugo 主题，极致加载速度，文章党首选 | [📄](./personal-site/entries/apvarun__digital-garden-hugo-theme.md) |
| [kentcdodds/kentcdodds.com](https://github.com/kentcdodds/kentcdodds.com) | React 大佬本人站源码，**不是给 clone 的**，看"个人站当产品做"是啥样 | [📄](./personal-site/entries/kentcdodds__kentcdodds-com.md) |

---

## dev-productivity/claude-workflow — Claude Code 工作流工程化

**解决什么：** 已经用 Claude Code 了，怎么玩出体系？skill 工厂、hook SDK、自学习 harness 等"把 Claude Code 当框架工程化"的代表项目。

| Repo | 大白话 | 详细文档 |
| --- | --- | --- |
| [alirezarezvani/claude-code-skill-factory](https://github.com/alirezarezvani/claude-code-skill-factory) | skill / agent / hook / slash 批量生产脚手架 | [📄](./dev-productivity/claude-workflow/entries/alirezarezvani__claude-code-skill-factory.md) |
| [GowayLee/cchooks](https://github.com/GowayLee/cchooks) | Claude Code hook 的 Python SDK，9 种事件类型化 | [📄](./dev-productivity/claude-workflow/entries/GowayLee__cchooks.md) |
| [parcadei/Continuous-Claude-v3](https://github.com/parcadei/Continuous-Claude-v3) | 109 skill + 32 agent + 30 hook 的自学习 harness 样板 | [📄](./dev-productivity/claude-workflow/entries/parcadei__Continuous-Claude-v3.md) |
| [BayramAnnakov/claude-reflect](https://github.com/BayramAnnakov/claude-reflect) | 监听你纠正 Claude → 自动 `/reflect` 写进 CLAUDE.md | [📄](./dev-productivity/claude-workflow/entries/BayramAnnakov__claude-reflect.md) |
| [starbaser/ccproxy](https://github.com/starbaser/ccproxy) | LiteLLM 代理 + hook pipeline + 规则引擎，多模型路由器 | [📄](./dev-productivity/claude-workflow/entries/starbaser__ccproxy.md) |

---

## dev-productivity/ai-coding-agent — AI Coding Agent 框架

**解决什么：** Claude Code 之外，还有哪些值得参考的自主 AI 编程代理？从 SWE-Bench 冠军到极简文件循环 agent。

| Repo | 大白话 | 详细文档 |
| --- | --- | --- |
| [OpenHands/OpenHands](https://github.com/OpenHands/OpenHands) | SWE-Bench 77.6 分，Devin 开源平替，Docker 沙箱 + event stream 教科书 | [📄](./dev-productivity/ai-coding-agent/entries/OpenHands__OpenHands.md) |
| [cline/cline](https://github.com/cline/cline) | 一套核心引擎驱动 CLI/SDK/VS Code/JetBrains/Kanban 五形态 | [📄](./dev-productivity/ai-coding-agent/entries/cline__cline.md) |
| [Aider-AI/aider](https://github.com/Aider-AI/aider) | 老牌终端 pair programmer，repo-map + 自动 git commit | [📄](./dev-productivity/ai-coding-agent/entries/Aider-AI__aider.md) |
| [iannuttall/ralph](https://github.com/iannuttall/ralph) | 极简 file-based agent loop，跟 /gitout 同哲学 | [📄](./dev-productivity/ai-coding-agent/entries/iannuttall__ralph.md) |
| [dollspace-gay/OpenClaudia](https://github.com/dollspace-gay/OpenClaudia) | Rust 写的 Claude Code 复刻品 | [📄](./dev-productivity/ai-coding-agent/entries/dollspace-gay__OpenClaudia.md) |

---

## dev-productivity/ide-augment — IDE 增强 / 编辑器 AI 集成

**解决什么：** 在 VSCode 或 Neovim 里写代码，怎么把 AI 助手装进编辑器、怎么用包管理器统一 LSP/格式化器。

| Repo | 大白话 | 详细文档 |
| --- | --- | --- |
| [continuedev/continue](https://github.com/continuedev/continue) | 跨 VSCode/JetBrains 开源 AI 助手，core 复用 + monorepo 范本 | [📄](./dev-productivity/ide-augment/entries/continuedev__continue.md) |
| [TabbyML/tabby](https://github.com/TabbyML/tabby) | 自托管 Copilot 替代，Rust server + 多 IDE 客户端 | [📄](./dev-productivity/ide-augment/entries/TabbyML__tabby.md) |
| [yetone/avante.nvim](https://github.com/yetone/avante.nvim) | Neovim 版 Cursor，含 ACP 对接 Claude Code | [📄](./dev-productivity/ide-augment/entries/yetone__avante.nvim.md) |
| [olimorris/codecompanion.nvim](https://github.com/olimorris/codecompanion.nvim) | Neovim 里的 prompt library + slash + adapter，最契合 skill 体系 | [📄](./dev-productivity/ide-augment/entries/olimorris__codecompanion.nvim.md) |
| [mason-org/mason.nvim](https://github.com/mason-org/mason.nvim) | Neovim 跨平台包管理器，管 LSP/DAP/Linter/Formatter | [📄](./dev-productivity/ide-augment/entries/mason-org__mason.nvim.md) |

---

## dev-productivity/personal-tools — 开发者生产力工具（非 AI）

**解决什么：** 故意挑一组**不带 AI 也能让你 10x** 的工具——命令行加速器、TUI 应用、dotfile 管理。给 AI 路线做反向参照。

| Repo | 大白话 | 详细文档 |
| --- | --- | --- |
| [Gaurav-Gosain/tuios](https://github.com/Gaurav-Gosain/tuios) | 现代版 terminal multiplexer，Charm 栈 + BSP 布局 | [📄](./dev-productivity/personal-tools/entries/Gaurav-Gosain__tuios.md) |
| [fpgmaas/justx](https://github.com/fpgmaas/justx) | 给 `just` 任务运行器套个 TUI 启动器 | [📄](./dev-productivity/personal-tools/entries/fpgmaas__justx.md) |
| [SuperCuber/dotter](https://github.com/SuperCuber/dotter) | Rust dotfile 管理器，模板渲染 + symlink 双层 | [📄](./dev-productivity/personal-tools/entries/SuperCuber__dotter.md) |
| [abhixdd/ghgrab](https://github.com/abhixdd/ghgrab) | 不用 clone 整仓库就能挑文件下载（GitHub/GitLab/Gitea 等） | [📄](./dev-productivity/personal-tools/entries/abhixdd__ghgrab.md) |
| [alejandroqh/term39](https://github.com/alejandroqh/term39) | 复古 MS-DOS 风 terminal multiplexer，全平台 + framebuffer | [📄](./dev-productivity/personal-tools/entries/alejandroqh__term39.md) |

---

## xiaozhi-ai — xiaozhi 语音对话硬件生态

**解决什么：** DIY 一个能跟你说话的 AI 小盒子。xiaozhi 是中文圈最火的 ESP32 + LLM 语音助手开源生态。原版固件 + 三语言后端 + 移动端客户端，组成完整链路。

| Repo | 大白话 | 详细文档 |
| --- | --- | --- |
| [78/xiaozhi-esp32](https://github.com/78/xiaozhi-esp32) | 虾哥本尊的 ESP32 AI 语音盒子原版固件（26.6k 星） | [📄](./xiaozhi-ai/entries/78__xiaozhi-esp32.md) |
| [xinnan-tech/xiaozhi-esp32-server](https://github.com/xinnan-tech/xiaozhi-esp32-server) | 社区最火自建后端，Python+Java+Vue 三件套 | [📄](./xiaozhi-ai/entries/xinnan-tech__xiaozhi-esp32-server.md) |
| [huangjunsen0406/py-xiaozhi](https://github.com/huangjunsen0406/py-xiaozhi) | 没硬件也能玩——Python 桌面客户端 | [📄](./xiaozhi-ai/entries/huangjunsen0406__py-xiaozhi.md) |
| [TOM88812/xiaozhi-android-client](https://github.com/TOM88812/xiaozhi-android-client) | Flutter 移动端，iOS/Android 双平台，带 AEC 回音消除 | [📄](./xiaozhi-ai/entries/TOM88812__xiaozhi-android-client.md) |
| [joey-zhou/xiaozhi-esp32-server-java](https://github.com/joey-zhou/xiaozhi-esp32-server-java) | Java 党的企业级后端，带完整前后端管理平台 | [📄](./xiaozhi-ai/entries/joey-zhou__xiaozhi-esp32-server-java.md) |

---

## 📊 整体统计

- **总项目数**：68（cli-wrap 5 + voice-pipeline 5 + claude-skills 5 + im-export 5 + personal-kb 5 + ai-avatar 5 + server-ops 5 + iot-platform 4 + personal-site 4 + dev-productivity 20 + xiaozhi-ai 5）
- **已停更但仍收录**：3 个（WeChatMsg、dendron、DiscordChatExporter 维护模式）—— 思路或窗口期价值还在
- **重型参考向（别整站 clone）**：jetlinks、kentcdodds.com、OpenHands —— 给你读架构的，不是拿来用的

## 🎯 几条快速建议

1. **想搭个人产品起点：** personal-site 选 `thedevdavid/digital-garden`，配合 Claude Code 改起来最顺
2. **想搞个 VPS 跑点东西：** server-ops 不知道选啥就 `1Panel`，想轻量就 `AcePanel`
3. **想做 OpenClaw / Agent 产品：** cli-wrap + claude-skills + dev-productivity/ai-coding-agent 一起看
4. **想升级自己的 skill 工程：** dev-productivity/claude-workflow 是直接对照
5. **想做 weixinjilu：** im-export 的 `LC044/WeChatMsg` 趁能用赶紧研究，长线靠 `HPI` 思路立差异

---

## 🔗 目录约定

```
gitout/
├── INDEX.md                          # 本文件，总入口
├── README.md                         # 简介
├── <domain>/                         # 每个 domain 一个目录（snake-case 或 kebab-case）
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
