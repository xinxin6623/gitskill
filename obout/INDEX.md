# gitout · 主题导航索引

> 用 `/gitout` 累积的 GitHub 项目地图。每个 domain 一个目录，每条都有大白话简介 + 详细文档链接。
<<<<<<< HEAD
> 最后更新：2026-05-26 · stars 数据快照于同日

---

## 🧭 21 个 domain 一览

| Domain | 一句话 | 项目数 | 首推 |
| --- | --- | --- | --- |
| [[#cli-wrap--cli-包装--把工具变成-ai-能用的命令|📦 cli-wrap]] | 让 AI 调命令行，或把任意软件包装成 Agent 接口 | 5 | open-interpreter (63.6k) |
| [[#voice-pipeline--语音-pipeline--实时对话技术栈|🎙️ voice-pipeline]] | 跟 AI 实时语音对话的底座 | 5 | fastrtc (4.6k) |
| [[#claude-skills--claude-code-生态--skill-和-hooks|⚙️ claude-skills]] | Claude Code skill/hook/subagent 入门 | 11 | mattpocock/skills (105k) |
| [[#im-export--聊天记录导出--个人数据归档|💬 im-export]] | 微信/iMessage/Discord 历史导出 | 5 | WeChatMsg (41.5k) |
| [[#personal-kb--个人知识库--markdown-wiki|📚 personal-kb]] | 本地优先的 Markdown 笔记 + 互链 + 可发布 | 5 | logseq (43.0k) |
| [[#ai-avatar--ai-虚拟角色--live2d-桌宠|🤖 ai-avatar]] | 给 AI 套个皮：能动嘴、有表情、能聊天 | 5 | airi (39.5k) |
| [[#server-ops--服务器搭建管理面板|🖥️ server-ops]] | Web 面板 + 轻量 PaaS + 反代（VPS 多站部署） | 10 | Dokku (32k) / Coolify (56k) |
| [[#iot-platform--物联网平台|🌐 iot-platform]] | MQTT + 规则引擎 + Dashboard 完整 IoT 后台 | 4 | FastBee (2.2k) |
| [[#personal-site--个人网站全栈模板|🏠 personal-site]] | 博客 + 项目展示 + Now 页一个 starter 搞定 | 4 | digital-garden (331) |
| [[#dev-productivityclaude-workflow--claude-code-工作流工程化|🛠️ dev-productivity/claude-workflow]] | skill 工厂 / hook SDK / 自学习 harness | 5 | Continuous-Claude-v3 (3.8k) |
| [[#dev-productivityai-coding-agent--ai-coding-agent-框架|🚀 dev-productivity/ai-coding-agent]] | Claude Code 之外的自主代码代理参考 | 5 | OpenHands (74.6k) |
| [[#dev-productivityide-augment--ide-增强--编辑器-ai-集成|✏️ dev-productivity/ide-augment]] | VSCode/Neovim 里的 AI 编程插件 | 5 | continue (33.3k) |
| [[#dev-productivitypersonal-tools--开发者生产力工具非-ai|🧰 dev-productivity/personal-tools]] | 不带 AI 也能让你 10x 的工具 | 5 | tuios (2.7k) |
| [[#xiaozhi-ai--xiaozhi-语音对话硬件生态|🗣️ xiaozhi-ai]] | ESP32 + LLM 端侧 AI 语音盒子生态 | 5 | xiaozhi-esp32 (26.7k) |
| [[#local-llm-runtime--mac-本地-llm-推理运行时|🦙 local-llm-runtime]] | Mac/Apple Silicon 本地跑 7B-30B 模型的反共识方案 | 5 | llamafile (24.5k) |
| [[#rag-engine--本地优先的-rag--向量检索引擎|🔍 rag-engine]] | 嵌入式/自托管/浏览器原生的向量库 | 5 | vecstore (14) |
| [[#knowledge-graph--文本笔记知识图谱-抽取与可视化栈|🕸️ knowledge-graph]] | 文本/笔记自动抽实体关系、生成可视化图谱 | 5 | graphrag-local-ollama (1.1k) |
| [[#mcp-servers--mcp-server-生态合集|🔌 mcp-servers]] | 给 Claude/Codex/Cursor 扩展工具能力的 MCP server | 5 | servers (86.2k) |
| [[#screen-vision-assistant--mac-屏幕-ocr--截图理解--视觉助手|📷 screen-vision-assistant]] | Mac 桌面 OCR + 截图多模态 + 本地 VLM 屏幕记忆 | 5 | TRex (1.8k) |
| [[#git-self-host--自建-git-仓库--依赖代理|🗄️ git-self-host]] | 自建 Git 服务器 + 国内依赖代理 + git push 部署网站 | 5 | piku (6.6k) |

**合计 114 个项目**

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

**⭐ 首推 `mattpocock/skills`（105k）：** Total TypeScript 创办人那套"工程派"skill，`/grill-me` `/tdd` `/improve-codebase-architecture` 直接装。安全方向看 `trailofbits/skills`（30+ 审计 plugin），中文学习看 `dianyike/claude-code-insights`，全景索引看 `ComposioHQ/awesome-claude-skills`。

| Repo | ⭐ | 大白话 | 详细文档 |
| --- | ---: | --- | --- |
| [mattpocock/skills](https://github.com/mattpocock/skills) | 105k | Total TypeScript 创办人的工程派 skill，`/grill-me` `/tdd` 源头 | [[claude-skills/entries/mattpocock__skills|📄]] |
| [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | 61.8k | 6 万星头部 awesome list + 500 应用 connect plugin | [[claude-skills/entries/ComposioHQ__awesome-claude-skills|📄]] |
| [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | 44.5k | Claude Code 整个生态的"黄页" | [[claude-skills/entries/hesreallyhim__awesome-claude-code|📄]] |
| [VoltAgent/awesome-claude-code-subagents](https://github.com/VoltAgent/awesome-claude-code-subagents) | 20.3k | 131+ 个角色化 subagent，一键安装 | [[claude-skills/entries/VoltAgent__awesome-claude-code-subagents|📄]] |
| [slavingia/skills](https://github.com/slavingia/skills) | 8.9k | Gumroad 创始人把《极简创业》变成 10 个 slash command | [[claude-skills/entries/slavingia__skills|📄]] |
| [anthropics/claude-agent-sdk-python](https://github.com/anthropics/claude-agent-sdk-python) | 7.0k | 官方 Python SDK | [[claude-skills/entries/anthropics__claude-agent-sdk-python|📄]] |
| [trailofbits/skills](https://github.com/trailofbits/skills) | 5.4k | Trail of Bits 安全审计 30+ plugin marketplace | [[claude-skills/entries/trailofbits__skills|📄]] |
| [disler/claude-code-hooks-mastery](https://github.com/disler/claude-code-hooks-mastery) | 3.7k | 13 种 hook 事件全讲清楚，附完整示例 | [[claude-skills/entries/disler__claude-code-hooks-mastery|📄]] |
| [coleam00/claude-memory-compiler](https://github.com/coleam00/claude-memory-compiler) | 1.1k | 聊天记录自动整理成知识库 | [[claude-skills/entries/coleam00__claude-memory-compiler|📄]] |
| [TheCraigHewitt/skills](https://github.com/TheCraigHewitt/skills) | 104 | 在 mattpocock 上做 `/shape` + `/ralph` 自动闭环 | [[claude-skills/entries/TheCraigHewitt__skills|📄]] |
| [dianyike/claude-code-insights](https://github.com/dianyike/claude-code-insights) | 54 | 中文最完整的 CLAUDE.md/Skill/Subagent 三件套指南 | [[claude-skills/entries/dianyike__claude-code-insights|📄]] |

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

**解决什么：** 你买了台 VPS 或家里有台小主机，但配 Nginx、装 MySQL、跑 Docker 一堆命令背不下来。这些项目让你浏览器点点就能搞定。第二批（2026-05-26）增加轻量 PaaS 方向：一台 VPS 跑 2-3 个小站、自动反代 + SSL、适合 Claude Code 操作。

**⭐ 面板首推 `1Panel`（35.5k）：** 不知道选啥就用它。**多站部署首推 `Dokku`（32k）：** 100% CLI、git push 就上线，Claude Code 友好度最高。要 Web UI + CLI 两手抓选 `Dokploy`（34k），功能最全选 `Coolify`（56k）。

### 管理面板

| Repo | ⭐ | 大白话 | 详细文档 |
| --- | ---: | --- | --- |
| [1Panel-dev/1Panel](https://github.com/1Panel-dev/1Panel) | 35.5k | 国产现代化全能面板，165+ 应用一键装、容器管理一体化 | [[server-ops/entries/1Panel-dev__1Panel|📄]] |
| [IceWhaleTech/CasaOS](https://github.com/IceWhaleTech/CasaOS) | 33.9k | 家用小主机的"个人云"系统，UI 像 iPad，NAS 场景 | [[server-ops/entries/IceWhaleTech__CasaOS|📄]] |
| [webmin/webmin](https://github.com/webmin/webmin) | 5.7k | 1997 年至今的"祖师爷"，传统 Linux 服务管理王者 | [[server-ops/entries/webmin__webmin|📄]] |
| [aaPanel/aaPanel](https://github.com/aaPanel/aaPanel) | 3.0k | 宝塔国际版，60M 内存就能跑，PHP 建站老朋友 | [[server-ops/entries/aaPanel__aaPanel|📄]] |
| [acepanel/panel](https://github.com/acepanel/panel) | 2.8k | Go 单文件运行、轻量不破坏系统的中文面板（耗子面板新版） | [[server-ops/entries/acepanel__panel|📄]] |

### 轻量 PaaS / 多站部署（Claude Code 友好）

| Repo | ⭐ | 大白话 | CC 友好度 | 详细文档 |
| --- | ---: | --- | --- | --- |
| [coollabsio/coolify](https://github.com/coollabsio/coolify) | 56k | 最火自托管 PaaS，280+ 一键模板，有 API | 中高 | [[server-ops/entries/coollabsio__coolify|📄]] |
| [Dokploy/dokploy](https://github.com/Dokploy/dokploy) | 34k | 现代 PaaS，CLI + API + Traefik 自动路由 + Docker Compose 原生 | 高 | [[server-ops/entries/Dokploy__dokploy|📄]] |
| [NginxProxyManager/nginx-proxy-manager](https://github.com/NginxProxyManager/nginx-proxy-manager) | 33k | 最流行反代 GUI，自动 SSL，不懂 Nginx 也能用 | 低 | [[server-ops/entries/NginxProxyManager__nginx-proxy-manager|📄]] |
| [dokku/dokku](https://github.com/dokku/dokku) | 32k | 100% CLI 的 mini-Heroku，git push 就部署 | **极高** | [[server-ops/entries/dokku__dokku|📄]] |
| [caprover/caprover](https://github.com/caprover/caprover) | 15k | Docker+Nginx PaaS，600+ 一键应用商店 | 中 | [[server-ops/entries/caprover__caprover|📄]] |

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

## local-llm-runtime — Mac 本地 LLM 推理运行时

**解决什么：** 不想被 OpenAI/Anthropic 卡着钱包，又嫌 Ollama 太大众？这里挑反共识方案——单文件可执行、Apple MLX 原生、Swift in-process。专为 M 系列 Mac 选。

**⭐ 首推 `llamafile`（24.5k）：** 把模型权重 + 推理代码塞一个可执行文件，下载即跑、零安装、跨 OS；Mozilla 长期维护，唯一星数级生态。`mlx-swift-lm` 是 Apple 官方 Swift 库（嵌 macOS/iOS app 必备）；想用 Claude Code 但跑本地模型上 `Kevlar`（Anthropic API 兼容层）；想试投机解码新论文用 `mio`；纯 Swift coding agent 看 `mlx-coder`。

| Repo | ⭐ | 大白话 | 详细文档 |
| --- | ---: | --- | --- |
| [mozilla-ai/llamafile](https://github.com/mozilla-ai/llamafile) | 24.5k | 单文件 LLM 旗舰：权重+推理捆一个可执行，下载即跑 | [[local-llm-runtime/entries/mozilla-ai__llamafile|📄]] |
| [ml-explore/mlx-swift-lm](https://github.com/ml-explore/mlx-swift-lm) | 523 | Apple 官方 Swift LLM 库，把 mlx-lm 那套搬进 Xcode | [[local-llm-runtime/entries/ml-explore__mlx-swift-lm|📄]] |
| [eduardogoncalves/mlx-coder](https://github.com/eduardogoncalves/mlx-coder) | 8 | Swift 写的 in-process coding agent，与 MLX 推理同进程 | [[local-llm-runtime/entries/eduardogoncalves__mlx-coder|📄]] |
| [nikholasnova/Kevlar](https://github.com/nikholasnova/Kevlar) | 7 | 让 Claude Code 跑你本地 MLX 模型的 Anthropic API 兼容层 | [[local-llm-runtime/entries/nikholasnova__Kevlar|📄]] |
| [Ruler-Dev/mio](https://github.com/Ruler-Dev/mio) | 4 | DFlash 投机解码 + PolarQuant KV 压缩的极致 MLX 引擎 | [[local-llm-runtime/entries/Ruler-Dev__mio|📄]] |

---

## rag-engine — 本地优先的 RAG / 向量检索引擎

**解决什么：** Pinecone 这类云向量库锁数据、按月收钱。本地能跑、嵌入式/单文件/浏览器原生的向量引擎才是个人知识库的底座。

**⭐ 首推 `vecstore`（14）：** Rust 嵌入式 + 浏览器 WASM + hybrid search，最贴近"SQLite of vectors"的体验，进程内就能跑、API 干净；想要"build-once-ship-many"用 `nest`（单文件 `.nest` 容器、可签名分发）；想要 server 形态 `vecdb`；想直接拿来用的端到端 Graph RAG 选 `Kwipu`（83⭐ 自带 Obsidian/MCP）；做纯浏览器 RAG 用 `barq-vweb`。

| Repo | ⭐ | 大白话 | 详细文档 |
| --- | ---: | --- | --- |
| [benmaster82/Kwipu](https://github.com/benmaster82/Kwipu) | 83 | 本地 Graph RAG 给 Obsidian/markdown 用，自带 MCP server | [[rag-engine/entries/benmaster82__Kwipu|📄]] |
| [YASSERRMD/barq-vweb](https://github.com/YASSERRMD/barq-vweb) | 19 | 浏览器原生 Rust+WASM 向量库，自带 MiniLM embedding，零后端 | [[rag-engine/entries/YASSERRMD__barq-vweb|📄]] |
| [PhilipJohnBasile/vecstore](https://github.com/PhilipJohnBasile/vecstore) | 14 | "向量界 SQLite"，Rust 嵌入式 + 浏览器 WASM + hybrid search | [[rag-engine/entries/PhilipJohnBasile__vecstore|📄]] |
| [zaydmulani09/vecdb](https://github.com/zaydmulani09/vecdb) | 7 | 单二进制自托管 Rust 向量服务，hybrid + 类 SQL 查询 | [[rag-engine/entries/zaydmulani09__vecdb|📄]] |
| [hoffresearch/nest](https://github.com/hoffresearch/nest) | 5 | 整个 RAG 知识库塞进 `.nest` 单文件，签名可校验、像分发 SQLite db | [[rag-engine/entries/hoffresearch__nest|📄]] |

---

## knowledge-graph — 文本/笔记→知识图谱 抽取与可视化栈

**解决什么：** Obsidian 双链是手动连的；这里要的是**LLM 自动抽实体关系**生成真正的图结构（HTML/JSON/Neo4j），喂给 GraphRAG 或可视化。

**⭐ 首推 `graphrag-local-ollama`（1.1k）：** 微软 GraphRAG 本地化 + Ollama 接入，含 Web UI 图可视化和 5 种查询模式，是入门 GraphRAG 最直接的路径。想要"双引擎 + MCP server" 用 `OrchForge/RAG-GraphRAG-Knowledge-Base`；用 agent 把 PDF 织成 Obsidian markdown 知识图谱选 `NodeWeaver`；想要完整 KG 平台（13 工具 MCP）用 `Omni-Graph`；想读懂"文本→实体→图→查询"全流程从 `text-to-kg` 开始。

| Repo | ⭐ | 大白话 | 详细文档 |
| --- | ---: | --- | --- |
| [TheAiSingularity/graphrag-local-ollama](https://github.com/TheAiSingularity/graphrag-local-ollama) | 1.1k | 微软 GraphRAG 本地化 + Ollama + Web UI 可视化 | [[knowledge-graph/entries/TheAiSingularity__graphrag-local-ollama|📄]] |
| [vaishcodescape/Omni-Graph](https://github.com/vaishcodescape/Omni-Graph) | 3 | 端到端 KG 平台，FastAPI + pgvector，4 种 search + 13 工具 MCP | [[knowledge-graph/entries/vaishcodescape__Omni-Graph|📄]] |
| [arun1729/text-to-kg](https://github.com/arun1729/text-to-kg) | 3 | CogDB 最小 demo，"文本→实体→图→查询"全流程入门读物 | [[knowledge-graph/entries/arun1729__text-to-kg|📄]] |
| [OrchForge/RAG-GraphRAG-Knowledge-Base](https://github.com/OrchForge/RAG-GraphRAG-Knowledge-Base) | 0 | Node 自托管 RAG+GraphRAG 双引擎 + 图编辑器 + Claude Desktop MCP | [[knowledge-graph/entries/OrchForge__RAG-GraphRAG-Knowledge-Base|📄]] |
| [Seif-Yasser-Ahmed/NodeWeaver](https://github.com/Seif-Yasser-Ahmed/NodeWeaver) | 0 | agent 把 PDF 啃成 Obsidian markdown 知识图谱，遍历 wikilink 推理 | [[knowledge-graph/entries/Seif-Yasser-Ahmed__NodeWeaver|📄]] |

---

## mcp-servers — MCP server 生态合集

**解决什么：** Claude/Codex/Cursor 通过 MCP 协议吃工具，这里收**工具端的实现**（不是 Claude skill 那种 agent 侧组织方式，那归 `claude-skills/`）。

**⭐ 首推 `modelcontextprotocol/servers`（86.2k）：** Anthropic 官方参考 server 合集 + 全 SDK 入口，找现成 MCP server 第一站；想翻"全网 MCP server 大目录"上 `awesome-mcp-servers`（5.5k 社区版）；要接管已登录浏览器（自动化淘宝/微信网页版）选 `mcp-chrome`；处理 Excel 不依赖 Office 用 `excel-mcp-server`；操 K8s 用原生 Go 的 `kubernetes-mcp-server`（不包 kubectl）。

| Repo | ⭐ | 大白话 | 详细文档 |
| --- | ---: | --- | --- |
| [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) | 86.2k | Anthropic 官方 MCP 参考 server 合集 + 全 SDK 入口 | [[mcp-servers/entries/modelcontextprotocol__servers|📄]] |
| [hangwin/mcp-chrome](https://github.com/hangwin/mcp-chrome) | 11.7k | Chrome 扩展型 MCP server，接管你已登录的真实 Chrome | [[mcp-servers/entries/hangwin__mcp-chrome|📄]] |
| [appcypher/awesome-mcp-servers](https://github.com/appcypher/awesome-mcp-servers) | 5.5k | 社区 MCP server 大目录，按场景翻清单 | [[mcp-servers/entries/appcypher__awesome-mcp-servers|📄]] |
| [haris-musa/excel-mcp-server](https://github.com/haris-musa/excel-mcp-server) | 3.9k | Python 写的 Excel MCP server，不依赖 Microsoft Office | [[mcp-servers/entries/haris-musa__excel-mcp-server|📄]] |
| [containers/kubernetes-mcp-server](https://github.com/containers/kubernetes-mcp-server) | 1.6k | Go 原生 K8s MCP server，直接走 API，不包 kubectl | [[mcp-servers/entries/containers__kubernetes-mcp-server|📄]] |

---

## screen-vision-assistant — Mac 屏幕 OCR / 截图理解 / 视觉助手

**解决什么：** 看到屏幕上的文字想复制？截图问 AI 帮翻译？后台监控屏幕做语义记忆（Rewind 平替）？五条不同形态对照矩阵。

**⭐ 首推 `TRex`（1.8k）：** Swift 菜单栏小恐龙，框一块屏幕、文字进剪贴板，纯离线 Apple Vision，最贴 Mac 原生哲学；要 OCR+翻译+以图搜图全家桶（容忍 Electron）选 `eSearch`（6.4k 但反 native 偏好）；公式表格转 LaTeX/Markdown 选 `screen-scribe`（Apple Vision + Gemini）；全本地翻译（隐私至上）用 `screenTranslate`；做 Rewind 风格本地 VLM 屏幕记忆挑 `screen-watcher`。

| Repo | ⭐ | 大白话 | 详细文档 |
| --- | ---: | --- | --- |
| [xushengfeng/eSearch](https://github.com/xushengfeng/eSearch) | 6.4k | 截屏+离线 OCR+翻译+以图搜图全家桶，跨平台 Electron | [[screen-vision-assistant/entries/xushengfeng__eSearch|📄]] |
| [amebalabs/TRex](https://github.com/amebalabs/TRex) | 1.8k | 菜单栏小恐龙，框一块屏幕，文字到剪贴板，纯离线 Swift | [[screen-vision-assistant/entries/amebalabs__TRex|📄]] |
| [SamuelZ12/screen-scribe](https://github.com/SamuelZ12/screen-scribe) | 86 | Apple Vision OCR + Gemini 多模态，专治公式表格转 LaTeX | [[screen-vision-assistant/entries/SamuelZ12__screen-scribe|📄]] |
| [hcmhcs/screenTranslate](https://github.com/hcmhcs/screenTranslate) | 37 | 全本地 Apple Vision + Apple Translation，隐私优先翻译 | [[screen-vision-assistant/entries/hcmhcs__screenTranslate|📄]] |
| [ljch2018/screen-watcher](https://github.com/ljch2018/screen-watcher) | 0 | 本地 VLM 后台默默看屏，做 Rewind 平替的语义记忆 | [[screen-vision-assistant/entries/ljch2018__screen-watcher|📄]] |

---

## git-self-host — 自建 Git 仓库 / 依赖代理

**解决什么：** 在自己的 VPS（典型 4C4G 国内云）上跑代码托管 + 国内依赖镜像 + `git push` 一键部署个人网站。两条主线：Git 服务器本体 + 依赖代理。

**⭐ 首推 `piku`（6.6k）：** `git push` 即上线的最小 PaaS，跑在 256MB 树莓派都行，4C4G 简直奢侈，正好对接"git 管理个人网站"诉求。要完整 GitHub 体验 + mirror 国外依赖用 `gitea`（35.5k 自托管事实标准）；只要极简 SSH-only Git server 用 `soft-serve`；Go 依赖国内代理直接用 `goproxy.cn`，企业级私服上 `athens`。

| Repo | ⭐ | 大白话 | 详细文档 |
| --- | ---: | --- | --- |
| [piku/piku](https://github.com/piku/piku) | 6.6k | `git push` 即上线的最小 PaaS，树莓派都能跑 | [[git-self-host/entries/piku__piku|📄]] |
| [go-gitea/gitea](https://github.com/go-gitea/gitea) | 55.9k | 自托管 Git 平台事实标准，单二进制 + mirror | [[git-self-host/entries/go-gitea__gitea|📄]] |
| [charmbracelet/soft-serve](https://github.com/charmbracelet/soft-serve) | 6.9k | 单二进制 SSH-only Git server，省内存极简风 | [[git-self-host/entries/charmbracelet__soft-serve|📄]] |
| [goproxy/goproxy.cn](https://github.com/goproxy/goproxy.cn) | 7.1k | 国内 Go 依赖代理（公共服务，七牛云运维） | [[git-self-host/entries/goproxy__goproxy.cn|📄]] |
| [gomods/athens](https://github.com/gomods/athens) | 4.8k | 企业级自建 Go module 代理 + 缓存（CNCF 沙箱） | [[git-self-host/entries/gomods__athens|📄]] |

---

## 📊 整体统计

- **总项目数**：114（cli-wrap 5 + voice-pipeline 5 + claude-skills 11 + im-export 5 + personal-kb 5 + ai-avatar 5 + server-ops 10 + iot-platform 4 + personal-site 4 + dev-productivity 20 + xiaozhi-ai 5 + personality-test 5 + local-llm-runtime 5 + rag-engine 5 + knowledge-graph 5 + mcp-servers 5 + screen-vision-assistant 5 + git-self-host 5）
- **stars 总和**：约 206 万⭐ · 单条最高 modelcontextprotocol/servers 86.2k · 中位数约 2k
- **已停更但仍收录**：3 个（WeChatMsg 41.5k、dendron 7.4k、DiscordChatExporter 维护模式）—— 思路或窗口期价值还在
- **重型参考向（别整站 clone）**：jetlinks、kentcdodds.com、OpenHands —— 给你读架构的，不是拿来用的
- **新一批 reach（2026-05-25）**：local-llm-runtime / rag-engine / knowledge-graph / mcp-servers / screen-vision-assistant 五个本地优先方向，平均星数低但意图匹配度高

## 🎯 跨域推荐路径

1. **想搭个人产品起点：** personal-site/`thedevdavid/digital-garden` + Claude Code（配套 claude-skills/`awesome-claude-code` 入门）
2. **想搞个 VPS 跑点东西：** 管理面板选 server-ops/`1Panel`（万能） · 一台 VPS 跑多站选 `Dokku`（Claude Code 友好）或 `Dokploy`（Web UI + CLI）
3. **想做 Agent 产品：** cli-wrap/`open-interpreter` + claude-skills/`anthropics-sdk` + dev-productivity/ai-coding-agent/`OpenHands`（读架构）
4. **想升级 skill 工程：** dev-productivity/claude-workflow/`Continuous-Claude-v3` 是直接对照样板
5. **想做微信记录归档：** im-export/`WeChatMsg` 趁能用赶紧研究 · 长线靠 `HPI` 的"个人数据包"思路立差异
6. **想搭本地 AI 栈：** local-llm-runtime/`llamafile` 跑模型 + rag-engine/`vecstore` 做检索 + knowledge-graph/`graphrag-local-ollama` 做图谱 + mcp-servers/`modelcontextprotocol/servers` 把工具接到 Claude Code
7. **想让 Mac 桌面变 AI 助手：** screen-vision-assistant/`TRex` 选字 + screen-watcher 屏幕记忆 + 本地 MLX 模型做语义查询

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
*local-llm-runtime / rag-engine / knowledge-graph / mcp-servers / screen-vision-assistant 由 /gitout 5 agent 并行模式生成 · 2026-05-25*
*claude-skills 增补 6 entries（mattpocock/trailofbits/dianyike/slavingia/ComposioHQ/TheCraigHewitt）由 /gitout 自然语言模式生成 · 2026-05-26*
*git-self-host 由 /gitout 自然语言模式生成 · 2026-05-26 · 主题：国内 4C4G 自建 Git + 依赖代理 + 网站部署*
*server-ops 增补 5 entries（dokku/dokploy/coolify/caprover/nginx-proxy-manager）由 /gitout 自然语言模式生成 · 2026-05-26 · 主题：一台 VPS 多站部署 + Claude Code 友好*
