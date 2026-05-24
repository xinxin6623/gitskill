# retros · 时序索引

> 每次 /gitout 跑完或阶段性修改后，**必须在此 append 一行摘要**。
> 时序倒序（最新在最上）。命名约定见同目录 README.md。
> 本文件是 retros 目录唯一的导航入口，与 `gitout/INDEX.md`（项目 entry 索引）职责分开、互不替代。

---

## 📅 时序记录

| 日期 | 类型 | 文件 | 一句话摘要 |
| --- | --- | --- | --- |
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
