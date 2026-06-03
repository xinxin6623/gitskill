# retros · 时序索引

> 每次 /gitout 跑完或阶段性修改后，**必须在此 append 一行摘要**。
> 时序倒序（最新在最上）。命名约定见同目录 README.md。
> 本文件是 retros 目录唯一的导航入口，与 `gitout/INDEX.md`（项目 entry 索引）职责分开、互不替代。

---

## 📅 时序记录

| 日期 | 类型 | 文件 | 一句话摘要 |
| --- | --- | --- | --- |
| 2026-06-03 | retro | — | claude-code-launcher 主题首跑（mixed 模式）：5 路 query 全有效返回，9 候选进二轮 README，1 个因 macOS 专属 reject；新建 domain；首推 lxistired (Windows 中国版懒人包) + cc-switch 旗舰组合；发现 cc/cc- 前缀名容易混 Claude Code vs Claude Desktop |
| 2026-06-02 | retro | — | document-parsing 主题首跑：找 MinerU 同档位 Mac mini 友好替代；首轮 5 query 因带引号返空（gh CLI 行为差异），改用无引号重试 OK；最终入选 docling / marker / olmocr / unstructured / RapidDoc 五条 |
| 2026-05-27 | retro | — | company-website 主题首跑：need 模式 9 query 中 4 个零返回（多词 AND 命中低），改单/双词后补足 5 entry；新建 domain 与 personal-site 区分（公司 brand/CTA vs 个人 portfolio/blog）；首次主动应用 SKILL v2.1 的"诉求覆盖广度"权重排序 |
| 2026-05-26 | 阶段性修改 | — | SKILL.md v2.1：落地 git-self-host followup 的 5 项改进——intent 加 license_sensitivity / agent_friendly 字段、Step 2.1 GPL 强制追问、Step 5 加"诉求覆盖广度"权重、entry 模板加"📜 协议风险"强制段、汇报模板补两字段；文末加 ChangeLog |
| 2026-05-26 | 阶段性修改 | — | 新增 `followups/` 目录承接 /gitout 搜索后的讨论 / 选型 / 反馈；CLAUDE.md 升级为三 INDEX 体系（gitout / retros / followups 互不混塞）；首份样板 followup = git-self-host（Gitea 选型 + 推飞书 + feedback 给出协议维度漏抽取等 5 项 SKILL 改进建议） |
| 2026-05-26 | retro | [2026-05-26-git-self-host-retro.md](./2026-05-26-git-self-host-retro.md) | git-self-host 主题首跑：5 query 全有效返回；新建 domain；候选池有 GitLab 重型项目被合理 reject；piku/gitea/soft-serve/goproxy.cn/athens 5 entries 入库 |
| 2026-05-26 | retro | [2026-05-26-claude-skills-collections-retro.md](./2026-05-26-claude-skills-collections-retro.md) | mattpocock/skills 等 6 entries 增补 claude-skills；mixed 模式分流 OK；README noise filter 漏过 `<source>/<picture>/<p align>` 需扩展 |
| 2026-05-25 | retro | [2026-05-25-5-domain-parallel-batch-retro.md](./2026-05-25-5-domain-parallel-batch-retro.md) | 5 agent 并行扫 local-llm-runtime / rag-engine / knowledge-graph / mcp-servers / screen-vision-assistant 共 25 entry 入库；首轮暴露 gh 未登录时 agent 行为不一致（2 个走匿名 REST、3 个严守 SKILL 停了）；总 73→98 |
| 2026-05-24 | 阶段性修改 | — | 按 `2026-05-23-skill-optimization-checklist.md` 全部接受落实 17 项优化：SKILL.md 重写（安装节/INDEX 自检/input_type 分流/反 buzzword 抓取/停更扫描/三句硬模板/批量 subagent/--quick/结构化汇报）+ 新增 `_taxonomy.yaml` + `.gitignore` 重写 + symlink 安装 + radar v1.2 加实施状态段 |
| 2026-05-24 | retro | [2026-05-24-personality-test-retro.md](./2026-05-24-personality-test-retro.md) | MBTI 主题首跑：5 query 并发因 `archivedAt` 字段名 bug 全失败需串行重跑；README 返空率偏高；INDEX 自检 0 缺 0 孤儿 |
| 2026-05-23 | 优化清单 | [2026-05-23-skill-optimization-checklist.md](./2026-05-23-skill-optimization-checklist.md) | 综合 05-22 + 05-23 两份复盘 + radar 蓝本对照，输出 17 项可勾选优化清单（P0×6 / P1×6 / P2×5） |
| 2026-05-23 | retro | [2026-05-23-xiaozhi-ai-retro.md](./2026-05-23-xiaozhi-ai-retro.md) | xiaozhi 专名主题：5 个初始 query 只 1 个有结果，暴露 brand vs need 输入未分流问题；候选池一半是周边集成 |
| 2026-05-22 | retro | [2026-05-22-voice-avatar-multi-theme-retro.md](./2026-05-22-voice-avatar-multi-theme-retro.md) | 单会话连跑三轮（voice pipeline / AI 对话机器人 / 5 主题批量）35 个项目入库；首次记录 `--sort best-match` 报错等 8 个坑 |

---

## 🔧 阶段性修改时间线

按对 SKILL.md 或主流程结构产生影响的改动倒序排列。每条对应一次"非单纯 retro 的"配置/结构升级。

| 日期 | 动作 | 影响范围 |
| --- | --- | --- |
| 2026-05-30 | 结构性改造：关系索引 + 图谱 + 成长库 + 四 INDEX 体系 | relationships/ + insights/ + graph.json 配色 + _taxonomy.yaml 补全 + obout/ 重生成 + CLAUDE.md §2ter §3.4 |
| 2026-05-26 | 新增 `followups/` 目录 + CLAUDE.md 三 INDEX 体系 | followups/ 承接搜索后讨论 / 选型 / 反馈；CLAUDE.md §1.3 / §2bis / §3.3 新规定；首份样板 git-self-host 落地（含飞书副本归档机制） |
| 2026-05-24 | 17 项优化清单全部落实 | SKILL.md 由五段式升为七段式；新增 `_taxonomy.yaml` / batch subagent 模式 / `--quick` 子命令 / INDEX 自检 / 三句硬模板；radar v1.2 加"实施状态"段；symlink 到 ~/.claude/skills |
| 2026-05-23 | gitout 目录由 misc 拆为 6 个一级 domain | 把早期 misc/ 下 30 个 entry 拆成 cli-wrap / voice-pipeline / claude-skills / im-export / personal-kb / ai-avatar 六个独立 domain |
| 2026-05-23 | 新增 dev-productivity 多子域 + 多 agent 并行实操 | dev-productivity/{claude-workflow,ai-coding-agent,ide-augment,personal-tools} 四子域 20 个 entry 首次用 subagent 并行生成 |
| 2026-05-22 | /gitout skill v2 上线 | 从"关键词 + stars 排序"重构为"自然语言意图 → 多策略 query → LLM 重排序"五段式 |

---

## 🛠 维护约定

- **每次 /gitout 跑完** → 在"时序记录"表 append 一行（type=retro）+ 同时新建 `<YYYY-MM-DD>-<domain>-retro.md`
- **每次阶段性修改 SKILL/主流程/目录结构** → 在两张表都 append（type=阶段性修改）；retro 文件可有可无
- **摘要硬约束**：一句话 ≤ 80 字，含"做了什么 + 关键发现/影响"
- **不删旧行**：表只追加，retro 文件本身陈旧也不删
- 本 INDEX 与 `gitout/INDEX.md`（项目 entry 索引）**分头维护**，互不冲突
