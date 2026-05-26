# gitskill 项目约定

本仓库是 James 的 Claude Code skill 实验场，主体是 `/gitout`（GitHub 项目发现引擎）的产出归档，外加 `followups/` 承接搜索之后的讨论与选型沉淀。

## 1. 目录约定（强约束）

```
gitskill/
├── CLAUDE.md                          # 本文件
├── radar-system-v1.2.md               # 雷达系统设计（项目级文档）
├── skills/                            # 项目级 skill 源码
│   └── gitout/SKILL.md
├── gitout/                            # /gitout 全部产出归这里
│   ├── INDEX.md                       # 主题总入口（必须维护）
│   ├── README.md                      # gitout 简介
│   ├── <domain>/                      # 每个主题一个独立 domain 目录
│   │   ├── README.md                  # 健康度 + 速览表
│   │   ├── index.yaml                 # 结构化索引(机器可读)
│   │   └── entries/
│   │       └── <owner>__<repo>.md     # 每个项目一个小白文档
│   ├── raw/<YYYY-MM-DD>/<intent-slug>/  # gh 检索原始 JSON 归档(只读)
│   └── retros/<YYYY-MM-DD>-<主题>-retro.md  # /gitout 流程复盘
└── followups/                         # 搜索之后的讨论 / 选型 / 反馈
    ├── INDEX.md                       # 时序索引(必须维护)
    ├── README.md                      # followups 简介与边界
    └── <YYYY-MM-DD>-<domain-or-topic>/
        ├── README.md                  # 本次 followup 主索引
        ├── discussion.md              # 后续讨论关键节点摘要
        ├── decision.md                # 最终选型结论(独立可读)
        ├── feedback.md                # 对 /gitout 这次搜索的反向打分
        └── exports/feishu-<slug>.md   # 推送到外部系统的本地副本
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

### 1.3 followups 目录命名
- followup 目录名：`<YYYY-MM-DD>-<domain-or-topic>`，日期对齐对应 /gitout retro 日期
- domain-or-topic **优先与 `gitout/<domain>/` 同名**；跨多 domain 时用主题词（如 `2026-06-01-ai-coding-stack`）
- 四个标准文件名固定：`README.md` / `discussion.md` / `decision.md` / `feedback.md`
- exports 内文件命名：`<system>-<slug>.md`（如 `feishu-gitea-decision.md` / `notion-xxx.md`）

## 2. /gitout 产出强约束

每跑一轮 `/gitout` 必须：

1. **不要新建 `misc/` 或叫它"misc"**。每次扫描必须有明确 domain 名（用户没说就主动起一个 kebab-case 名）。
2. **要么复用已有 domain，要么新建独立 domain**——绝不允许把不相关项目堆进现有 domain 的 `entries/` 凑数。
3. 新建 domain 时同步落地：`<domain>/README.md` + `<domain>/index.yaml` + `<domain>/entries/*.md`。
4. 跑完后 **必须更新 `gitout/INDEX.md`**：
   - 在主题表新增一行
   - 在正文新增一个 `## <domain> — <一句话>` 小节，含完整 entry 表格
   - 更新底部"总项目数"统计
5. 原始 gh JSON 落 `raw/<日期>/<intent-slug>/`，**不进 `gitout/INDEX.md`**。
6. 复盘文档（如有）落 `retros/<日期>-<主题>-retro.md`，**不进 `gitout/INDEX.md`**，但 **必须同步在 `gitout/retros/INDEX.md` append 一行摘要**（见 §3.2）。
7. 任何对 SKILL.md / 主流程 / 目录结构的阶段性修改，也要在 `gitout/retros/INDEX.md` "阶段性修改时间线"表 append 一行。

## 2bis. followups 产出约束

每次 /gitout 跑完，**如有后续讨论 / 选型 / 推送外部**（飞书 / Notion / 群文档等），就开一个 followup 目录：

1. **触发条件**（任一即可）：用户在原始候选池上做了二次筛选 / 拍板 / 推送外部 / 给出实操反馈。一两轮对话也算，哪怕 decision.md 只有 3 行——价值在 feedback.md。
2. 四件套**齐全**：`README.md`（主索引）+ `discussion.md`（关键节点摘要）+ `decision.md`（拍板结论）+ `feedback.md`（反向打分）。
3. 推送外部时**必须**在 `exports/` 留本地副本，含 URL + 推送命令 + 同步策略说明。
4. **本地是真相源，外部系统不同步**。本地改了不自动推外部；要推就手动 `lark-cli docs +update` 推一次。
5. 完成后**必须更新 `followups/INDEX.md`** append 一行（最新在上），含日期 / 主题 / 关键决策 / 是否推送 / feedback 要点。
6. **不要做的事**：
   - 不要把逐字对话 transcript 写进 `discussion.md`——只记关键节点和决策转折
   - 不要把 /gitout 流程复盘塞进 `feedback.md`——那是 `gitout/retros/` 的活
   - 不要把项目卡片复制到 followups 里——entry 还在 `gitout/<domain>/entries/`

## 3. 三个 INDEX 的职责分工

仓库里有 **三个 INDEX.md**，职责互不重叠，**全部都要维护**：

### 3.1 `gitout/INDEX.md` —— 项目 entry 总入口
**目录树的唯一真相源**，每次目录变动后立刻同步：
- 新增 domain → 加表头行 + 加正文小节
- 删除/合并 domain → 同步删表头行和正文小节
- 重命名 → 全文替换路径
- 项目数变动 → 更新该 domain 的 `项目数` 列 + 底部"总项目数"

### 3.2 `gitout/retros/INDEX.md` —— 复盘与阶段性修改时序索引
按时序倒序记录所有 retro 文件 + 阶段性修改。**触发条件**：
- 每次 `/gitout` 跑完 → "时序记录"表 append 一行（type=retro）+ 链接对应 retro 文件
- 每次对 SKILL.md / 主流程 / 目录结构做阶段性修改 → 在"时序记录"和"阶段性修改时间线"两张表都 append（type=阶段性修改）
- 摘要 ≤ 80 字，含"做了什么 + 关键发现/影响"
- **只追加不删**

### 3.3 `followups/INDEX.md` —— 搜索后讨论与选型时序索引
按时序倒序记录每次 followup。**触发条件**：
- 每次开新的 followup 目录 → append 一行
- 列：日期 / 主题（链接到 followup 目录）/ 关键决策一句话 / 是否推送外部 / feedback 要点
- 摘要 ≤ 80 字
- **只追加不删**

三个 INDEX 各自负责一类东西，永远不要混塞：
- 项目 entry → 只进 `gitout/INDEX.md`
- 流程复盘 / SKILL 阶段性修改 → 只进 `gitout/retros/INDEX.md`
- 搜索后讨论 / 选型 / 外部推送 → 只进 `followups/INDEX.md`

## 4. 语言与风格
- 中文优先（James 母语）；entry 文档遵循 SKILL.md 里的小红书风格小白说明。
- 代码/路径/repo 名保持英文。
- INDEX 与各 README 的"一句话讲它干嘛的"必须人话，不抄 GitHub description。

## 5. 不要做的事
- ❌ 不要重建 `misc/`（之前 30 个 entries 已拆成 6 个独立 domain，**不要回滚**）
- ❌ 不要把 retros / raw / followups 加进 `gitout/INDEX.md` 主题表
- ❌ 不要在 followups/ 里放原始对话 transcript——摘要即可
- ❌ 不要把飞书 / Notion 等外部文档当真相源——本地 `decision.md` 才是
- ❌ 不要把 /gitout 流程复盘塞进 followups/feedback.md（那是 `gitout/retros/` 的活）
- ❌ 不要在 `gitout/` 根目录直接放散文（如 zongjie.md），所有内容都得归 domain 或 retros
- ❌ 不要在 entry 文档外另起 `.md` 文件做"补充说明"——补充内容写进 entry 本身或 README

## 6. 已知历史
- 2026-05-22 ~ 23：14 个主题、68 个项目入库；同步把早期 `misc/` 拆成 6 个一级 domain（cli-wrap / voice-pipeline / claude-skills / im-export / personal-kb / ai-avatar）。
- 两份 zongjie.md 归档到 `gitout/retros/`。
