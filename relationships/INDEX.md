# relationships · 关系索引

> 第四套 INDEX 系统，追踪 `gitout/` 各 domain/entry 之间的非目录关系。
> 与 `gitout/INDEX.md`（项目入口）`retros/INDEX.md`（复盘）`followups/INDEX.md`（决策）**职责不重叠**。
> 最后更新：2026-05-30 · 关系数：22

---

## 关系类型一览

| 类型 | 标签 | 对称 | 含义 |
|------|------|------|------|
| `depends-on` | 依赖 | 否 | A 依赖 B |
| `alternative-to` | 替代 | 是 | A 可替代 B |
| `complements` | 互补 | 是 | A 补充 B |
| `supersedes` | 取代 | 否 | A 取代 B |
| `similar-to` | 相似 | 是 | A 相似于 B |
| `related-to` | 关联 | 是 | A 关联 B |
| `cross-domain-recommendation` | 跨域推荐 | 否 | 路径链 |

完整词表见 [[relationships/_types.yaml]]。

---

## 🎯 跨域推荐路径

移植自 [[gitout/INDEX.md#🎯-跨域推荐路径]]。每个路径是一条**起点 → 终点**的链式推荐，步数不限。

1. **个人产品起点**：[[gitout/personal-site/entries/thedevdavid__digital-garden.md|digital-garden]] → [[gitout/claude-skills/entries/hesreallyhim__awesome-claude-code.md|awesome-claude-code]] → 用 Claude Code 定制
2. **VPS 多站**：[[gitout/server-ops/entries/1Panel-dev__1Panel.md|1Panel]] 管理面板 — 或 [[gitout/server-ops/entries/dokku__dokku.md|Dokku]] git push 部署
3. **Agent 产品参考**：[[gitout/cli-wrap/entries/openinterpreter__open-interpreter.md|open-interpreter]] + [[gitout/claude-skills/entries/anthropics__claude-agent-sdk-python.md|SDK]] + [[gitout/dev-productivity/ai-coding-agent/entries/OpenHands__OpenHands.md|OpenHands 架构]]
4. **Skill 工程样板**：[[gitout/dev-productivity/claude-workflow/entries/parcadei__Continuous-Claude-v3.md|Continuous-Claude-v3]]
5. **微信记录归档**：[[gitout/im-export/entries/LC044__WeChatMsg.md|WeChatMsg]] 趁能用 → 长线看 [[gitout/im-export/entries/karlicoss__HPI.md|HPI]] 思路
6. **本地 AI 栈**：[[gitout/local-llm-runtime/entries/mozilla-ai__llamafile.md|llamafile]] → [[gitout/rag-engine/entries/PhilipJohnBasile__vecstore.md|vecstore]] → [[gitout/knowledge-graph/entries/TheAiSingularity__graphrag-local-ollama.md|graphrag-local-ollama]] → [[gitout/mcp-servers/entries/modelcontextprotocol__servers.md|MCP servers]]
7. **Mac 桌面 AI**：[[gitout/screen-vision-assistant/entries/amebalabs__TRex.md|TRex]] + [[gitout/screen-vision-assistant/entries/ljch2018__screen-watcher.md|screen-watcher]] + 本地 MLX

---

## 条目间关系

### 🔄 替代关系（alternative-to）

| A | B | 说明 |
| --- | --- | --- |
| [[gitout/server-ops/entries/dokku__dokku.md|dokku]] | [[gitout/git-self-host/entries/piku__piku.md|piku]] | piku 是 dokku 的更轻量替代（树莓派级） |
| [[gitout/git-self-host/entries/go-gitea__gitea.md|Gitea]] | [[gitout/git-self-host/entries/charmbracelet__soft-serve.md|soft-serve]] | Gitea 功能全 vs soft-serve 极简 SSH-only |
| [[gitout/server-ops/entries/coollabsio__coolify.md|Coolify]] | [[gitout/server-ops/entries/Dokploy__dokploy.md|Dokploy]] | Coolify 功能全 vs Dokploy CLI+API 双模 |

### 📎 相似关系（similar-to）

| A | B | 说明 |
| --- | --- | --- |
| [[gitout/server-ops/entries/coollabsio__coolify.md|Coolify]] | [[gitout/server-ops/entries/dokku__dokku.md|dokku]] | 同属轻量 PaaS 赛道，coolify 有 Web UI，dokku 纯 CLI |
| dotter | toml-bombadil | 同属 dotfile 管理器（toml-bombadil 在 rejected_samples 中） |
| dotter | yadm | 同为 dotfile 管理，yadm 是"老朋友"已排除 |

### 🧩 互补关系（complements）

| A | B | 说明 |
| --- | --- | --- |
| [[gitout/voice-pipeline/entries/gradio-app__fastrtc.md|FastRTC]] | [[gitout/voice-pipeline/entries/OpenMOSS__MOSS-TTS.md|MOSS-TTS]] | FastRTC 管道 + MOSS-TTS 中文 TTS |
| [[gitout/voice-pipeline/entries/gradio-app__fastrtc.md|FastRTC]] | [[gitout/voice-pipeline/entries/Liquid4All__liquid-audio.md|Liquid Audio]] | FastRTC 管道 + Liquid Audio 端到端语音理解 |
| [[gitout/local-llm-runtime/entries/mozilla-ai__llamafile.md|llamafile]] | [[gitout/rag-engine/entries/PhilipJohnBasile__vecstore.md|vecstore]] | 推理 + 检索 = 本地 RAG 底座 |
| [[gitout/local-llm-runtime/entries/mozilla-ai__llamafile.md|llamafile]] | [[gitout/knowledge-graph/entries/TheAiSingularity__graphrag-local-ollama.md|graphrag-local-ollama]] | 推理后端 + 图谱查询 |
| [[gitout/rag-engine/entries/PhilipJohnBasile__vecstore.md|vecstore]] | [[gitout/knowledge-graph/entries/TheAiSingularity__graphrag-local-ollama.md|graphrag-local-ollama]] | 向量检索 + 图谱检索互补 |
| [[gitout/personal-kb/entries/logseq__logseq.md|Logseq]] | [[gitout/personal-kb/entries/jackyzha0__quartz.md|Quartz]] | 记笔记 + 发布数字花园 |

### 📡 关联关系（related-to）

| A | B | 说明 |
| --- | --- | --- |
| [[gitout/claude-skills/entries/mattpocock__skills.md|mattpocock/skills]] | [[gitout/dev-productivity/claude-workflow/entries/parcadei__Continuous-Claude-v3.md|Continuous-Claude-v3]] | 同为 skill 生态，前者首发后者工程化 |
| [[gitout/xiaozhi-ai/entries/78__xiaozhi-esp32.md|xiaozhi-esp32]] | [[gitout/voice-pipeline/entries/gradio-app__fastrtc.md|FastRTC]] | xiaozhi 语音链路可用 FastRTC 做 WebRTC 入口 |

### ⬆️ 依赖关系（depends-on）

| A | 依赖 B | 说明 |
| --- | --- | --- |
| [[gitout/xiaozhi-ai/entries/xinnan-tech__xiaozhi-esp32-server.md|xiaozhi-esp32-server]] | [[gitout/xiaozhi-ai/entries/78__xiaozhi-esp32.md|xiaozhi-esp32]] | server 是硬件固件的后端 |

### ⬆️ 取代关系（supersedes）

| A | 取代 B | 说明 |
| --- | --- | --- |
| [[gitout/personal-kb/entries/logseq__logseq.md|Logseq]] | [[gitout/personal-kb/entries/dendronhq__dendron.md|Dendron]] | Dendron 已停更，Logseq 是当前活跃替代 |

---

## 维护约定

- **新增关系**：修改 `index.yaml` append 条目 + 更新本 INDEX. 对应小节
- **新增关系类型**：必须先在 `_types.yaml` 注册
- **source/target 路径**：优先使用 `gitout/...` 相对路径；外部引用使用完整 URL
- **删除关系**：保留记录，在 index.yaml 加 `archived: true`；本 INDEX 移除行
- **只追加不删**（本 INDEX append-only，已有行不删不改）
