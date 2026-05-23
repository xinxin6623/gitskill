# /gitout Skill 优化总结

> 来源：本次 xiaozhi-ai 主题实跑（2026-05-23）+ 之前 13 个主题积累
> 目的：提升下一版 skill 的产出**质量**和**效率**

---

## 一、本次实跑暴露的问题

### 1.1 初始 query 命中率太低
跑 5 组初始 query，**只有 1 组（"xiaozhi esp32 ai"）有结果**，其余 4 组（`ai voice assistant esp32 llm` / `chatgpt voice assistant esp32` / `llm voice chatbot embedded` / `ai companion device open source`）全部 0 返回。

**根因：** Step 1 的 query 生成策略要求"主题词 + 特性词 + 反共识词"，但当用户输入本身就是一个**专有名词品牌**（xiaozhi）时，特性词/反共识词反而把搜索打散了——GitHub 搜不到"通用语音盒子"，只搜得到"xiaozhi"这个生态本身。

**结果：** 浪费了 4 次 gh CLI 调用 + 一轮 token，被迫追加 2 轮补搜（q6 / q7 / q8 / q9 / q10 / q11）才把候选池补够。

### 1.2 候选池里"周边 vs 同类型"区分模糊
搜出来 ~20 条里有大量 **HA 集成 / MCP 插件 / 个人 fork demo**，这些都不是用户要的"同类型"。skill 在 reject 规则里没有"周边项目识别"，靠 LLM 临场判断，容易漏。

### 1.3 候选池规模上限不清晰
理论上 5 query × 8 limit = 40 条上限，但实际只有 ~20 条，且大量重复。reject 后剩 5 条 —— 跟"目标 8-12"差距不大但流程上没有"自动补搜"机制。

### 1.4 流程时间分布失衡
- Step 1（意图抽取）：≤ 5%
- Step 3（检索）：~30% （应≤15%）
- Step 4（reject + README 抓取）：~30%
- Step 5（重排序）：≤ 5%
- Step 6（写文档）：~30%

**问题：** 检索阶段占比过高，是因为补搜走的是"被动响应"而非"主动设计"。

### 1.5 raw 文件夹存大量"无效证据"
本次留下 7 个 q*.json，但其中 4 个是 0 返回的空 query，**仍然产生了文件**。这些文件对未来追溯零价值，是噪音。

---

## 二、质量层面优化方向

### 2.1 区分"专名输入"和"需求描述输入"

skill 在 Step 1 应该先做一次**输入类型判断**：

| 输入类型 | 例子 | 检索策略 |
|---------|------|---------|
| 专名/品牌 | "xiaozhi ai" / "claude code" | 优先用专名直搜，**反共识词降级为可选** |
| 需求描述 | "能打断 TTS 的语音 pipeline" | 当前策略最佳 |
| 混合 | "类似 dify 但更轻量" | 双轨：专名 + 特性 |

**落地：** Step 1 输出新增字段 `input_type: brand|need|mixed`，Step 3 据此切换 query 生成模板。

### 2.2 引入"周边 vs 同类型"显式判断

当输入是专名时，在 reject 规则里加一条：

```
若 fullName / description 命中以下模式 → 标记为"周边"而非"同类型"：
- "<品牌名> + (integration|plugin|client|bridge|hub|mcp|hacs|esphome)"
- "<品牌名> + (admin|ui|dashboard|panel)"（除非用户明说要管理界面）
- "<品牌名>-<功能词>"（衍生工具）
```

周边项目可以**单独列入"相关周边"段落**，但不占主入选 3-5 个名额。

### 2.3 README 抓取阶段加入"反 buzzword 检测"

本次 5 个入选项目的 README 头部都是大量 trendshift 徽章 + 多语言切换 + 赞助按钮，**前 1500 字几乎没有实质信息**。

**优化：** README 抓取后先用启发式跳过：
- 跳过 `<img>` `<a>` 等 markdown 链接行
- 跳过空行
- 跳过 ` ![徽章]` 行
- 截取**前 200 行有效内容**而非前 6000 字

预期：同样 token 拿到 3-5 倍的有效信息密度。

### 2.4 入选文档"为什么推它给你"段标准化

本次 5 篇文档的"为什么推它给你"段写法不一致：有的说了 trade-off，有的没说命中具体 soft preference。

**优化：** 段落模板硬性约束三个句子：
1. 命中了用户哪条意图（引用 Step 1 的 what）
2. 命中了哪条 soft preference
3. 没命中哪条（trade-off 透明化）

### 2.5 INDEX.md 同步不应该是手动一步

本次"同步 index"是用户主动要求才做的。**应该集成进 Step 7**：每次跑完自动 append 一个新主题节到 `gitout/INDEX.md`，按既有模板（章节标题 + 表格 + 详细文档链接）。

---

## 三、效率层面优化方向

### 3.1 query 生成改为"先 1 个种子词探针"

当前一次性生成 5 个 query 并行打。改为：

1. **先用 1 个最直白的种子词探针**（如 "xiaozhi"）
2. 看返回数量：
   - **≥ 15 条** → 直接进 reject，跳过其他 query
   - **5-15 条** → 再补 2 个 query 走特性词路线
   - **< 5 条** → 进入"需求描述"模式，5 个 query 并发

**收益：** 当输入是热门专名时，省 4 次 API 调用。本次 xiaozhi 直接用单词 "xiaozhi" 搜就能拿 15 条，q2-q5 全是浪费。

### 3.2 raw 文件夹只存"有效证据"

零返回的 query**不落盘**，但需要在 README 里记一行 `discarded_queries: [...]` 留痕。

### 3.3 README 并行抓取改为"按需触发"

当前是入选 5 个全部并行抓 README。改为：
- 元数据 reject 后剩 8-12 条 → 全抓
- 剩 5-7 条 → 全抓
- 剩 ≤ 5 条 → 直接全部入选，**只抓最终入选项**

**收益：** 候选池较小时省 README 抓取调用。

### 3.4 写文档阶段并行化

本次 5 篇文档是用一个 Write 块批量写的（同一消息 5 个 Write 调用并行）。这点已经做对了，**保留并明确写进 skill 文档**避免下次倒退。

### 3.5 内容长度预算硬约束

当前规则是"正文 ≤ 1000 字"。实际本次每篇 ~600-800 字，但**写作时没有显式预算引导**，可能在长项目（如原版固件）上偏长。

**优化：** 给 7 个小标题分配字数预算（如：这是什么 50 / 解决问题 100 / 谁该用 150 / 三分钟上手 100 / 关键文件 100 / 踩坑 100 / 为什么推它 150）—— LLM 写作时自动收敛。

---

## 四、流程层面优化方向

### 4.1 把"汇报"段做成结构化模板

本次最后的汇报段是手写的，每次跑出来格式可能略不同。改为固定结构：

```markdown
## 汇报
**意图：** {what}
**约束：** hard={...} soft={...}
**检索：** queries=N 候选=M reject=K 入选=L
**文件：** entries/, index.yaml, raw/
**建议下一步：** {prune | open <repo> | 跑另一组关键词}
```

### 4.2 增加"自评"段，喂给下一次自我改进

每次 Step 7 输出时，让 LLM 自评一句：

> 这次哪个环节最低效？下次相同主题应该怎么调整？

落到 `gitout/<domain>/README.md` 末尾的"反思"段。**长期积累后**作为 skill 升级的输入材料。

### 4.3 错误处理增加"重写 query"分支

当前规则：所有 query 0 返回 → 报告用户停止。

**实际场景：** 本次是部分 query 0 返回，没有触发错误处理，靠隐性补搜兜底。

**优化：** 当 5 个 query 总返回数 < 10 时，**主动触发一次 query 重写**（让 LLM 反思查询词为啥拉不到结果），而非沉默地往下走。

---

## 五、Skill 文档本身的优化建议

### 5.1 Step 1 加示例
当前 Step 1 只有意图结构定义，没有 worked example。建议加 2-3 个"输入 → 抽取结果"的具体例子（特别是专名 vs 需求描述对比）。

### 5.2 把"reject 规则"从段落改成 checklist
当前是文字描述。改成可勾选清单，LLM 跑 reject 时按格式输出 "[reject reason]" 标签，方便审计。

### 5.3 增加"轻量模式" flag
对于明确知道是热门专名的输入，用户可加 `--quick`：
- 跳过 query 多样化
- 直接专名搜 15 条
- 跳过 README 抓取，只用 description
- 文档减半（300-500 字）

**用例：** "xiaozhi 同类"这种就是典型 quick 场景。

---

## 六、优先级排序

按 ROI（效果 / 实施成本）排序：

| 优先级 | 优化项 | 收益 | 成本 |
|-------|--------|------|------|
| P0 | 3.1 单词种子探针 | 砍掉 50%+ 无效 API 调用 | 低 |
| P0 | 2.1 专名 vs 需求识别 | 命中率提升 ≥ 2x | 低 |
| P1 | 2.3 README 反 buzzword 截取 | 文档质量明显提升 | 中 |
| P1 | 2.5 INDEX.md 自动同步 | 省一次用户操作 | 低 |
| P1 | 2.2 周边 vs 同类型判断 | 入选质量提升 | 中 |
| P2 | 4.1 汇报结构化 | 用户体验一致性 | 低 |
| P2 | 4.2 自评落地 | 长期 skill 进化 | 低 |
| P2 | 5.3 轻量模式 flag | 高频场景提速 | 中 |
| P3 | 3.2 raw 文件夹清洁 | 仓库整洁度 | 极低 |
| P3 | 3.5 字数预算 | 文档一致性 | 低 |

---

## 七、一句话结论

**当前 skill 的最大瓶颈不是检索能力，是"不分输入类型一刀切"** —— 用统一的多样化 query 策略对待所有输入，导致专名场景大量浪费。下一版优先做"输入类型分流 + 单词探针 + 周边识别"三件套，预计能把同类任务的 API 调用减半、入选质量提升一档。

---
*生成时间：2026-05-23 · 基于 xiaozhi-ai 主题实跑复盘*

---

# 附录 · 第二轮复盘（2026-05-23 同日）

> 来源：本次"git init / push + INDEX 同步 + skill 安装路径"三件事的对话
> 角度：跳出"检索 → 文档"主链路，看 **skill 与项目仓库的协作面** 暴露的问题

## 八、本次对话暴露的新问题（链路外）

### 8.1 entries 与 INDEX.md 长期会漂移
- 现象：目录里实际有 30 个 `.md`，但 INDEX.md 只列了 25 个；多出的 5 个（airi / Kokoro-Engine / handcrafted-persona-engine / Live2D-LLM-Chat / AI-Vtuber）是上两轮搜索遗留，从未入 INDEX。
- 根因：每轮 `/gitout` 只 append 自己这一轮的主题节，**没有"目录-索引一致性"自检**。跑得越多，INDEX 越失真。
- 触发成本：用户必须**手动发现 + 主动要求**才会同步——本次就是这样。

### 8.2 SKILL.md 放错位置 → 完全调不出
- 现象：`Documents/gitskill/skills/gitout/SKILL.md` 是普通文件夹，**不是 Claude Code 识别的 skill 路径**。用户 `/gitout` 唤不起，以为 skill 坏了。
- 标准路径：`<project>/.claude/skills/<name>/SKILL.md` 或 `~/.claude/skills/<name>/SKILL.md`。
- 根因：SKILL.md 文档本身**完全没提"装到哪里才能用"**，是个孤立的设计文档，没有 install 章节。

### 8.3 .gitignore 是事后补的，不是 skill 内置约定
- 现象：首次 `git add -A` 把 `.DS_Store` 一起提交，事后 `git rm --cached` 删除；后来 Obsidian 打开 entries 目录又生成 `.obsidian/` 又得补一条。
- 根因：skill 假定用户在 `./gitout/` 下作业但**不管 git 化**。每个用 gitout 的用户都会踩同样两个坑。

### 8.4 raw/ 目录最终会爆炸
- 现象：本次仓库里 `gitout/raw/2026-05-22/` 已有 6 个主题、~50 个 `q*.json`。一年下来轻松上千文件。
- 根因：1.5 节已提到"零返回 query 不落盘"，但**没有定期清理策略**——所有 raw 永久留存。
- 后果：`git push` 体积膨胀；`prune` 子命令目前只管 entries 不管 raw。

### 8.5 主题命名靠 LLM 现编，跨轮不收敛
- 现象：本次补的"主题 6：AI 虚拟角色 / Live2D 对话机器人"是我现编的；上一轮的 "AI avatar" 主题在 index.yaml 里叫别的名字。
- 根因：没有**主题词表（taxonomy）**，每轮主题名都是 LLM 即兴翻译，导致语义近似的主题在 INDEX 里以不同名字出现，搜索/聚合困难。

---

## 九、新增优化方向

### 9.1 Step 7 增加"INDEX 一致性自检"
跑完后强制 diff：
```
actual = ls gitout/<domain>/entries/*.md
indexed = grep entries from INDEX.md
diff actual indexed → 自动补齐缺失行 / 提示孤儿条目
```
落地到 SKILL.md 的 Step 7，**作为硬性收尾步骤**，不再依赖用户提醒。

### 9.2 SKILL.md 增加 "Install" 章节
模板：
```markdown
## 安装
项目级：cp SKILL.md <project>/.claude/skills/gitout/SKILL.md
全局：cp SKILL.md ~/.claude/skills/gitout/SKILL.md
安装后**重启会话** 才能在 /xxx 列表里看到。
```
对应到 README 头部加一句"装错地方调不出"的醒目提示。

### 9.3 SKILL.md 内置 `.gitignore` 片段
首次在新仓库跑 `/gitout` 时，检测项目根有无 `.gitignore`：
- 没有 → 创建，写入 `.DS_Store` `.obsidian/` `gitout/raw/**/q*_empty.json`
- 有 → diff 后追加缺失行

### 9.4 raw/ 自动归档策略
扩展 `/gitout prune`：
- raw 超过 90 天 → 移入 `gitout/raw/_archive/<year-month>.tar.gz` 后删除原文件
- 提示用户但不强制（保持只读安全边界的精神）

### 9.5 主题词表（taxonomy）外置
在 `gitout/_taxonomy.yaml` 维护稳定主题名清单，例如：
```yaml
themes:
  - id: cli-agent-wrap
    cn: CLI 包装 / Agent 工具化
  - id: voice-pipeline
    cn: 语音 pipeline
  - id: ai-avatar
    cn: AI 虚拟角色 / Live2D
```
新主题入 INDEX 前先查 taxonomy，**找不到强匹配才允许新建**。LLM 现编主题名前必须读这个文件。

---

## 十、优先级更新（合并第一轮 + 第二轮）

| 优先级 | 优化项 | 收益 | 成本 |
|-------|--------|------|------|
| **P0** | 9.2 SKILL.md 加 Install 章节 | 解决"装错就用不了"的硬阻塞 | 极低 |
| **P0** | 9.1 Step 7 INDEX 自检 | 杜绝索引漂移 | 低 |
| P0 | 3.1 单词种子探针（原） | 砍掉 50%+ 无效 API | 低 |
| P0 | 2.1 专名 vs 需求识别（原） | 命中率 2x | 低 |
| **P1** | 9.3 内置 .gitignore | 每个用户都受益 | 极低 |
| **P1** | 9.5 主题 taxonomy | 长期可聚合可搜索 | 中 |
| P1 | 2.3 README 反 buzzword（原） | 文档质量 | 中 |
| P1 | 2.5 INDEX 自动同步（原） | 与 9.1 合并实施 | 低 |
| **P2** | 9.4 raw 归档 | 仓库体积控制 | 中 |
| P2 | 4.1 / 4.2 / 5.3（原） | 体验与长期进化 | 低-中 |

## 十一、一句话补充结论

第一轮结论说瓶颈在"输入类型一刀切"——那是**主链路**的问题；
第二轮发现：skill 与**项目仓库**的协作面（安装路径、INDEX 一致性、git 化、raw 膨胀、主题命名）**完全是盲区**。
下一版除了主链路三件套，还得补上"**项目侧基础设施五件套**"（Install 章节 / INDEX 自检 / 内置 gitignore / raw 归档 / taxonomy）—— 否则 skill 的用户体验在第 N 次跑之后会肉眼可见地崩塌。

---
*第二轮追加：2026-05-23 · 基于本次 git 推送 + INDEX 同步 + skill 安装对话*
