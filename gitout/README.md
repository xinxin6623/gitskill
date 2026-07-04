# gitout · 项目搜索与吸收目录

> 🚨 **装错地方调不出！** `/gitout` skill 必须放在 `~/.claude/skills/gitout/SKILL.md`。
> 仅放在本仓库 `skills/gitout/` 下 Claude Code **不会**识别。安装方法见 `../skills/gitout/SKILL.md` 顶部"安装"节。

> 由 `/gitout` skill 自动维护。目录骨架借鉴自 `radar-system-v1.2.md`，
> 判断规则外化（Rubric-as-Interface）借鉴自 `radar-system-v2.1.md`（v2.2 起合并）。
> **v2.4 起项目与数据分离**：skill 源码 + rubrics 在 `~/Documents/myskills/gitout/`，本目录只存数据。

## 目录结构

```
gitout/                        # 数据仓库（总库，~/Documents/gitskill/gitout/）
├─ README.md                  # 本文件
├─ INDEX.md                   # 主题导航索引（domain 一览 + 每 domain entry 表）
├─ _taxonomy.yaml             # domain 分类词表（防命名漂移）
├─ raw/{YYYY-MM-DD}/          # gh search 原始 JSON，只读审计痕迹
├─ decisions.md               # 人工 override 记录 → 反哺 rubric
├─ retros/                    # 流程复盘 + 阶段性修改时间线
└─ <domain>/                  # 按 domain 分类（kebab-case 名词短语）
    ├─ README.md              # 健康度面板
    ├─ index.yaml             # 活跃 entry 索引（≤ 30）
    └─ entries/               # 每个 repo 一份小白说明书（≤ 1000 字）
```

> rubrics/（判断规则）已搬到 `~/Documents/myskills/gitout/rubrics/`（项目代码侧），不在本数据目录。

## Rubric-as-Interface（v2.2 起）

判断规则不写死在 SKILL.md 里，外化为 `rubrics/` 下三份可版本化的 markdown：
- 改 rubric = 改 gitout 的判断标准，零代码，`git commit -m "rubric: <which> <change>"`
- 对结果有异议 → 记 `decisions.md` → 积累后提炼进 rubric
- 详见 `../skills/gitout/SKILL.md` 的 Rubric-as-Interface 段

## 容量上限（沿用 v1.2 §5.3）

| 资源类型 | 单 domain 上限 |
| ---- | ----------- |
| active entries | 30 |

超上限自动进入 yellow / red 状态，需用 `/gitout prune` 整理。

## 使用入口

- `/gitout <自然语言需求>` — 搜索并生成小白说明（输入是需求，不是关键词）
- `/gitout list` — 列出已收纳
- `/gitout open <repo>` — 查看某条
- `/gitout prune` — 容量与陈旧检查

Skill 源码：`../skills/gitout/SKILL.md`
