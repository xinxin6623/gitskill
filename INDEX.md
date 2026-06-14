# gitskill

James 的 Claude Code skill 实验场。主体是 `/gitout`（GitHub 项目发现引擎）的产出归档，配套 `followups/`（搜索后讨论与选型）、`relationships/`（条目间关系）、`insights/`（个人消化与创造）四套互不重叠的索引。

> 🤖 Agent 上手先读 [`AGENTS.md`](./AGENTS.md) 的项目专属操作守则（通用三件套协议在 [`docs/trio-protocol.md`](./docs/trio-protocol.md)）；改动后记得追加 [`CHANGELOG.md`](./CHANGELOG.md)（强标签格式见文件顶部）。

<!--
## 当前接力点 (Handoff)

此段是项目"下一步动作"导航位，**永远只保留最新一条**，覆盖式更新。启用时去掉外层 HTML 注释。

- **YYYY-MM-DD**：<一句话下一步>；<关键命令 / 文件指针>；详见 obwiki <wiki page>。
-->

## 项目结构

```
gitskill/
├── AGENTS.md                  # 项目专属操作守则（v2 软链 CLAUDE.md → 此文件）
├── CLAUDE.md                  # → AGENTS.md（相对软链，单一真相源）
├── INDEX.md                   # 本文件，项目导航
├── CHANGELOG.md               # 演绎记录（强标签）
├── LICENSE.md
├── radar-system-v1.2.md       # 雷达系统设计（项目级文档）
├── docs/
│   └── trio-protocol.md       # 三件套通用协议（standard-v2）
├── skills/                    # 项目级 skill 源码
│   └── gitout/SKILL.md
├── scripts/                   # 项目辅助脚本（如 make_obout.py）
├── gitout/                    # /gitout 全部产出归这里
│   ├── INDEX.md              # 项目 entry 总入口（强约束维护）
│   ├── README.md
│   ├── <domain>/             # 每个主题一个独立 domain
│   │   ├── README.md
│   │   ├── index.yaml        # 结构化索引（机器可读）
│   │   └── entries/<owner>__<repo>.md
│   ├── raw/<YYYY-MM-DD>/<intent-slug>/   # gh 检索原始 JSON（只读）
│   └── retros/               # /gitout 流程复盘 + 阶段性修改时间线
│       └── INDEX.md          # 时序索引
├── followups/                # 搜索后讨论 / 选型 / 反馈
│   ├── INDEX.md              # 时序索引（强约束维护）
│   ├── README.md
│   └── <YYYY-MM-DD>-<topic>/
│       ├── README.md / discussion.md / decision.md / feedback.md
│       └── exports/          # 推送到飞书 / Notion 等的本地副本
├── relationships/            # 条目间关系索引（第四套 INDEX）
│   ├── INDEX.md              # 人类可读关系浏览器
│   ├── index.yaml            # 机器可读
│   ├── _types.yaml           # 关系类型词表（append-only）
│   └── domain-graph.mermaid
├── insights/                 # 成长型知识库（个人消化与创造）
│   ├── INDEX.md
│   ├── index.yaml
│   ├── _templates/
│   ├── patterns/             # 跨 2+ entry 抽象模式（上限 20）
│   ├── learning/             # 个人学习笔记（append-only）
│   ├── synthesis/            # 跨域综合洞见
│   └── projects/             # 自有项目文档
└── obout/                    # Obsidian 导出工作区（含 .obsidian/）
    ├── INDEX.md
    └── README.md
```

## 子模块导航

| 子目录 | 一句话定位 | 主入口 |
|---|---|---|
| `gitout/` | `/gitout` 跑出来的项目卡片归档（按 domain 组织） | [`gitout/INDEX.md`](./gitout/INDEX.md) |
| `followups/` | gitout 搜索之后的讨论 / 选型 / 推送外部的沉淀 | [`followups/INDEX.md`](./followups/INDEX.md) |
| `relationships/` | gitout entry 之间的非目录关系（替换 / 互补 / 跨域推荐） | [`relationships/INDEX.md`](./relationships/INDEX.md) |
| `insights/` | 个人消化与创造（patterns / learning / synthesis / projects） | [`insights/INDEX.md`](./insights/INDEX.md) |
| `skills/` | 项目级 skill 源码（gitout 等） | [`skills/gitout/SKILL.md`](./skills/gitout/SKILL.md) |
| `obout/` | Obsidian 导出工作区 | [`obout/INDEX.md`](./obout/INDEX.md) |
| `scripts/` | 项目辅助脚本 | （平铺，无 INDEX） |
| `docs/` | 三件套通用协议（trio-protocol.md） | [`docs/trio-protocol.md`](./docs/trio-protocol.md) |

## 四个 INDEX 的职责分工

仓库里有**四个 INDEX.md**，职责互不重叠，全部都要维护。详细见 [AGENTS.md §3](./AGENTS.md)：

| INDEX | 收什么 | 不收什么 |
|---|---|---|
| `gitout/INDEX.md` | 项目 entry 总入口（domain 表 + 每 domain 小节） | retros / raw / followups |
| `gitout/retros/INDEX.md` | /gitout 流程复盘 + SKILL.md 阶段性修改时间线 | 项目 entry |
| `followups/INDEX.md` | 搜索后讨论 / 选型 / 外部推送（按时序倒序） | /gitout 流程复盘 |
| `relationships/INDEX.md` | 条目间的非目录关系 | 项目 entry 本身 |

本根目录 `INDEX.md` 是**项目导航**，不是上面四个之一——只引导你去对应子模块的 INDEX。

## 常用操作

```bash
# 跑一轮 GitHub 项目发现
/gitout <自然语言需求描述>

# 列出 gitout/ 已有 domain
ls gitout/

# 检查四个 INDEX 是否最新
grep -l "总项目数" gitout/INDEX.md
```

## 相关链接

- 📓 演绎记录：[CHANGELOG.md](./CHANGELOG.md)
- 🤖 Agent 守则：[AGENTS.md](./AGENTS.md)
- 📐 三件套通用协议：[docs/trio-protocol.md](./docs/trio-protocol.md)
- 🎯 雷达系统设计：[radar-system-v1.2.md](./radar-system-v1.2.md)
