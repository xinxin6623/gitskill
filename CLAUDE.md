# gitskill 项目约定

本仓库是 James 的 Claude Code skill 实验场，主体是 `/gitout`（GitHub 项目发现引擎）的产出归档。

## 1. 目录约定（强约束）

```
gitskill/
├── CLAUDE.md                          # 本文件
├── radar-system-v1.2.md               # 雷达系统设计（项目级文档）
├── skills/                            # 项目级 skill 源码
│   └── gitout/SKILL.md
└── gitout/                            # /gitout 全部产出归这里
    ├── INDEX.md                       # 主题总入口（必须维护）
    ├── README.md                      # gitout 简介
    ├── <domain>/                      # 每个主题一个独立 domain 目录
    │   ├── README.md                  # 健康度 + 速览表
    │   ├── index.yaml                 # 结构化索引（机器可读）
    │   └── entries/
    │       └── <owner>__<repo>.md     # 每个项目一个小白文档
    ├── raw/<YYYY-MM-DD>/<intent-slug>/  # gh 检索原始 JSON 归档（只读）
    └── retros/<YYYY-MM-DD>-<主题>-retro.md  # /gitout 复盘总结
```

### 1.1 命名规范
- **domain 目录名**：kebab-case，名词或名词短语，反映主题领域（不是动词）
  - ✅ `voice-pipeline` / `personal-kb` / `iot-platform`
  - ❌ `misc` / `voice` / `tools`（太泛或太宽）
- **entry 文件名**：`<owner>__<repo>.md`（双下划线分隔，照搬 GitHub fullName）
- **retro 文件名**：`<YYYY-MM-DD>-<主题或批次>-retro.md`
- **raw 目录**：`raw/<YYYY-MM-DD>/<intent-slug>/`，intent-slug 与 domain 名对齐

### 1.2 sub-domain（仅在必要时使用）
- 默认 **一级 domain**。只有当一个一级 domain 自然分裂成 ≥3 个明显独立的子方向时，才嵌套 sub-domain。
- 现存唯一例外：`dev-productivity/` 下分 `claude-workflow / ai-coding-agent / ide-augment / personal-tools` 四子域。
- sub-domain 也必须有自己的 `README.md` + `index.yaml` + `entries/`。

## 2. /gitout 产出强约束

每跑一轮 `/gitout` 必须：

1. **不要新建 `misc/` 或叫它"misc"**。每次扫描必须有明确 domain 名（用户没说就主动起一个 kebab-case 名）。
2. **要么复用已有 domain，要么新建独立 domain**——绝不允许把不相关项目堆进现有 domain 的 `entries/` 凑数。
3. 新建 domain 时同步落地：`<domain>/README.md` + `<domain>/index.yaml` + `<domain>/entries/*.md`。
4. 跑完后 **必须更新 `gitout/INDEX.md`**：
   - 在主题表新增一行
   - 在正文新增一个 `## <domain> — <一句话>` 小节，含完整 entry 表格
   - 更新底部"总项目数"统计
5. 原始 gh JSON 落 `raw/<日期>/<intent-slug>/`，**不进 INDEX**。
6. 复盘文档（如有）落 `retros/<日期>-<主题>-retro.md`，**不进 INDEX**。

## 3. INDEX.md 维护职责

INDEX.md 是**目录树的唯一真相源**，每次目录变动后立刻同步：
- 新增 domain → 加表头行 + 加正文小节
- 删除/合并 domain → 同步删表头行和正文小节
- 重命名 → 全文替换路径
- 项目数变动 → 更新该 domain 的 `项目数` 列 + 底部"总项目数"

## 4. 语言与风格
- 中文优先（James 母语）；entry 文档遵循 SKILL.md 里的小红书风格小白说明。
- 代码/路径/repo 名保持英文。
- INDEX 与各 README 的"一句话讲它干嘛的"必须人话，不抄 GitHub description。

## 5. 不要做的事
- ❌ 不要重建 `misc/`（之前 30 个 entries 已拆成 6 个独立 domain，**不要回滚**）
- ❌ 不要把 retros 或 raw 加进 INDEX 的主题表
- ❌ 不要在 `gitout/` 根目录直接放散文（如 zongjie.md），所有内容都得归 domain 或 retros
- ❌ 不要在 entry 文档外另起 `.md` 文件做"补充说明"——补充内容写进 entry 本身或 README

## 6. 已知历史
- 2026-05-22 ~ 23：14 个主题、68 个项目入库；同步把早期 `misc/` 拆成 6 个一级 domain（cli-wrap / voice-pipeline / claude-skills / im-export / personal-kb / ai-avatar）。
- 两份 zongjie.md 归档到 `gitout/retros/`。
