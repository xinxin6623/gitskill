# 2026-05-26 · claude-skills 增补复盘

**触发输入：** "mattpocock/skills + aihero.dev + /tad + /improve-codebase-architecture + /grill-me，搜索这些关键词，应该是 github 的关于技能的"

**input_type：** mixed（含专名 mattpocock/skills + aihero.dev + 需求"Claude Code skill 集合"）

**意图判定：** 用户看到 Matt Pocock 推荐了几个 skill，想找源头仓库 + 类似的社区 skill 库。`aihero.dev` 是 mattpocock 的 newsletter 站点，不是 GitHub 仓库（搜索 0 hit 已确认）。

## 检索漏斗

- query 数：5 → 有效 4 / 零返回 1（aihero claude）
- 总候选池（去重后）：~40
- 一轮 reject（基于元数据 + 周边过滤）：剩 12
- 二轮 reject（README 实质审查）：剩 11
- 入选：6（mattpocock / trailofbits / dianyike / slavingia / ComposioHQ / TheCraigHewitt）

## 关键发现

### ✅ 顺利的部分

1. **种子探针准确**：`mattpocock skills` 单 query 直接命中 105k stars 顶级目标，且周边镜像（vinvcn 中文版、bbylw 中文版、amazingloft999 镜像）自动归入"相关周边"段，没误入主入选
2. **同名 awesome list 大量重复有效合并**：搜出 10+ 个 `awesome-claude-skills` 同名分叉（karanb192 / travisvn / yibie / JayZeeDesign / fleurytian 等），按 stars 选了 ComposioHQ 作代表，其他列周边
3. **mixed 模式分流有效**：mattpocock 这种顶级专名直接锁定，省了多 query 试探

### ⚠️ 暴露的问题

1. **README 抓取后前 30-50 行还是徽章 noise**：mattpocock 的 README 前 10 行全是 `<source>` / `<picture>` / `<img>` 标签，grep `-v` pattern 过滤不彻底（没过滤 `<source` 和 `<picture`）→ 下次扩展 pattern 列表
2. **aihero.dev 零返回是预期内但浪费一个 query 名额**：用户输入含明显非 GitHub 域名时应该在 Step 1 就识别为"newsletter / website 不必搜"，省一次 API 调用
3. **TheCraigHewitt/skills 只 104 stars 但入选**：因为它直接构建在 mattpocock 上做了 `/shape` + `/ralph` 闭环，意图匹配度高 → 验证 SKILL 里"明确降权 stars"的重排序策略起作用了
4. **dianyike/claude-code-insights 也只 54 stars**：但中文 + 方法论密度高 + 直接讨论 mattpocock skills 的本地化复用，对中文用户价值极高 → 进一步验证 stars 降权的合理性

### 🔑 用户视角的关键洞察

用户实际看到的"keywords"（`/tad` 是 `/tdd` 的笔误，`mattpocock/skills`，`aihero.dev`）信号很集中——都是 Matt Pocock 一个人的生态。所以这次实际上是"专名探针 + 横向竞品扫描"任务，而不是宽域需求扫描。这种场景的最佳输出策略：

- 把核心专名（mattpocock）做最详尽的 entry（强调 5 个核心 skill 的用法和依赖关系）
- 横向竞品（trailofbits、slavingia、ComposioHQ）每个体现一个**不同维度**（安全/业务/导航），不堆同质项目
- 二次创作（TheCraigHewitt）+ 方法论（dianyike）作为"周边深挖"

## 下次跑同类主题改什么

1. **零结果 query 应在 Step 1 预判**：含 `.dev` / `.com` / `.ai` 等明显非仓库域名的 token 直接跳过
2. **README noise filter 扩展**：当前 `grep -vE '^!\[|^<img|^<a |^---$|^\s*$|<table|shields\.io'`，需加 `^<source|^<picture|^<p align|<details`
3. **专名 + 周边镜像的归类逻辑可以固化**：fullName 含原专名 + 后缀（-zh-CN / -cn / -fork / -mirror）直接归周边，不进二轮抓取，省 README 调用
4. **TheCraigHewitt 这类"在他人之上做加法"的 repo 是个高价值模式**：可以在 SKILL 里加一条 LLM 提示——"对头部专名做加法的 repo（依赖 + 扩展）优先保留"

## 文件路径

- 新增 entries（6 个）：
  - `./gitout/claude-skills/entries/mattpocock__skills.md`
  - `./gitout/claude-skills/entries/trailofbits__skills.md`
  - `./gitout/claude-skills/entries/dianyike__claude-code-insights.md`
  - `./gitout/claude-skills/entries/slavingia__skills.md`
  - `./gitout/claude-skills/entries/ComposioHQ__awesome-claude-skills.md`
  - `./gitout/claude-skills/entries/TheCraigHewitt__skills.md`
- raw 归档：`./gitout/raw/2026-05-26/claude-skills-collections/`（4 个有效 JSON）
- INDEX 自检：手动同步，11 entries 全列入
- 同步：`gitout/INDEX.md` 总项目数 73 → 79；claude-skills 行从 5 / awesome-claude-code 顶推改为 11 / mattpocock 顶推
