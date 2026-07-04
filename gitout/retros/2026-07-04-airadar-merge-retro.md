# 2026-07-04 · 合并 ai-radar 到 gitskill · retro

## 做了什么

把 `~/Documents/git search/`（ai-radar / radar-system-v2.1）合并进 gitskill。
核心动作：把 ai-radar 的 **Rubric-as-Interface** 理念移植到已落地的 gitout skill 上。

### 合并判断

两个项目目标相同（找 GitHub 开源项目），但设计哲学差异大：

| 维度 | gitout（gitskill） | ai-radar（git search） |
|---|---|---|
| 触发 | 按需一次性 | 持续监测 cron |
| 架构 | 单 skill 七段式 | 三 skill 五步管线 |
| 判断逻辑 | 写死在 SKILL.md | **外化为 rubric markdown** |
| 可迭代 | 改 SKILL.md | 改 rubric（零代码，git track） |
| 成熟度 | 已落地 129 项目 | 设计 v2.1 + 少量实战数据 |

结论：gitout 是已落地的运行底座，ai-radar 的 Rubric-as-Interface 是更先进的判断层设计。
合并 = 移植理念，不照搬架构。

### 取舍

**保留 gitout 的**：单 skill 七段式、自然语言意图抽取、按需触发、已落地的目录骨架与 129 个 entry
**吸收 ai-radar 的**：
- Rubric-as-Interface — 判断规则外化到 `gitout/rubrics/{scan,triage,deepdive}.md`
- decisions.md override 反哺 — 对结果有异议记 `gitout/decisions.md`，积累后提炼进 rubric
- 设计文档 `radar-system-v2.1.md` 迁入根目录与 v1.2 并列

**舍弃 ai-radar 的**：
- 三 skill 五步管线（gitout 单 skill 更轻）
- LiteLLM + 外部模型路由（Claude Code 一步到位）
- cron 持续监测（gitout 按需触发）
- Python 脚本（triage.py / deepdive.py / scan.sh / _lib）— gitout 不走外部模型管线
- config.yaml 模型路由 — 同上
- runs/ 可审计 trace — 暂用 raw/ + retros/ 替代，未单独建 runs/
- voice-pipeline 实战数据（candidates/inbox/entries/refs）— 风格不同，不混入 gitout/voice-pipeline

### 落地清单

1. ✅ 新建 `gitout/rubrics/scan.md` — 查询生成 + input_type 分流 + 负面词 + flag 规则
2. ✅ 新建 `gitout/rubrics/triage.md` — reject 规则 + 重排序权重 + 停更扫描
3. ✅ 新建 `gitout/rubrics/deepdive.md` — entry schema + 写作约束 + 协议风险段
4. ✅ 新建 `gitout/decisions.md` — override 反哺入口
5. ✅ 迁入 `radar-system-v2.1.md` + 加实施状态段
6. ✅ 更新 `radar-system-v1.2.md` 实施状态（指向 v2.1 已合并）
7. ✅ 重写 `skills/gitout/SKILL.md` v2.2 — 瘦身为流程骨架，判断逻辑引用 rubric
8. ✅ `.claude/skills/gitout` 改 symlink → `skills/gitout`（修复版本不同步）
9. ✅ 更新 `INDEX.md` 目录树 + 导航
10. ✅ 更新 `AGENTS.md` 目录约定 + §2 第 8 条 rubric 维护规则
11. ✅ 更新 `CHANGELOG.md` + `retros/INDEX.md` 两张表

## 关键发现

1. **git search 项目有实战数据**：voice-pipeline 跑通了 ai-radar 三步管线（1 entry + 3 inbox + 大量 runs trace），证明 rubric + LLM 管线能跑通。但这些数据风格（结构化技术 entry）与 gitout（小红书小白文档）不同，不直接并入 gitout/voice-pipeline，避免混乱。
2. **.claude/skills/gitout 是过时拷贝**：不是 symlink，SKILL.md 停在五段式旧版，而 skills/gitout/SKILL.md 已是七段式 v2.1。改成 symlink 一劳永逸。
3. **rubric 外化后 SKILL.md 从 488 行降到约 230 行**：判断规则移走后，SKILL 只剩流程骨架 + 安装 + 子命令 + 安全边界，更易维护。

## 下一步建议

- 第一次跑 gitout v2.2 时，验证 Claude 能正确读 `rubrics/*.md` 并按规则执行
- 如果 rubric 有遗漏，直接改 `gitout/rubrics/*.md`，不动 SKILL.md
- git search 项目可后续删除（有价值内容已迁入），或保留作历史参考
