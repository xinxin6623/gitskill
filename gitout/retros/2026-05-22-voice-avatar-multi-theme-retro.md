# /gitout Skill 复盘与优化建议

> 基于 2026-05-22 单次会话连跑三轮（voice pipeline → AI 对话机器人 → 5 主题批量扫描）的实战观察。
> 目的：把"踩到的坑"和"用着顺手的地方"沉淀成下一版 SKILL.md 的改造清单。

---

## 一、本次会话做了什么

| 轮次 | 输入 | 入选项目 | 产出 |
| --- | --- | --- | --- |
| 1 | 关键词 `voice pipeline` | 5 | 5 份小白文档 |
| 2 | 自然语言"AI 对话机器人 + DIY 角色" | 5 | 5 份小白文档 |
| 3 | 5 主题批量扫描 | 25 | 25 份小白文档 + INDEX.md 导航页 |

**累计**：35 个项目说明文档 + 1 个导航页 + 2 次 SKILL.md 迭代。

---

## 二、踩到的坑（按出现顺序）

### 坑 1：`gh search --sort best-match` 报错
- **现象**：第二轮第一次跑 5 组 query 全部失败，错误信息显示 `--sort` 只接受 `{forks|help-wanted-issues|stars|updated}`。
- **根因**：SKILL.md 写了 `--sort best-match`，但 gh CLI 的默认排序就是 best-match，**省略 `--sort` 才对**，传这个值反而报错。
- **修复**：当场改 SKILL.md，记录在注释里。
- **教训**：写 SKILL.md 时引用 CLI flag 必须先 `<tool> --help` 实测，**别凭语义猜**。

### 坑 2：多关键词字面 AND 匹配命中率极低
- **现象**：第三轮主题 1 用 `"CLI wrapper for GUI"` 这种长词组 + 默认匹配字段（只搜 name+description），返回 0-2 条且全是噪音；主题 4 用 `"wechat export chat"` 也全空。
- **根因**：gh search repos 默认 AND 所有词且只搜 name+description；超过 3 个词基本零命中。
- **修复**：临时加 `--match name,description,readme` 扩匹配字段，并把长词组拆短。
- **教训**：query 设计应该是"短词组 + readme 匹配"为基线，**不是把整句意图丢进去**。

### 坑 3：知名项目直接 `gh api repos/owner/name` 比搜索更快
- **现象**：主题 4 找微信导出工具时，5 组 query 都没找到 LC044/WeChatMsg（41k 星）和 PyWxDump（9.7k 星），最后是我凭记忆直接 `gh api` 拿元数据才补上。
- **根因**：GitHub 搜索 SEO 对中文项目偏弱，知名 repo 反而不一定在 query 结果里。
- **教训**：意图抽取后，**LLM 应该先列"已知的 N 个该领域名仓库"，并行直接 `gh api repos/...` 验证，再走 search 补长尾**。这一步当前 SKILL.md 缺失。

### 坑 4："stars 降权"在第一轮形同虚设
- **现象**：第一轮搜 voice pipeline 时按 stars 排序直接返回 5 个，caLLMe（20 star 但最契合）险些被切掉。
- **根因**：v1 SKILL 只用 `--sort stars --limit 5`，没有候选池扩大 + 重排序逻辑。
- **修复**：第二轮的 SKILL.md 改写引入"候选池 15-20 → reject → LLM 重排序 → 选 3-5"流程。
- **效果验证**：第二轮 39 星的 Live2D-LLM-Chat 成功排在 445 星的 AI-Vtuber 前面，证明重排逻辑生效。

### 坑 5：废弃 / 停更项目没有提前过滤
- **现象**：第二轮收到 livekit-examples/voice-pipeline-agent-python（README 顶部明示 outdated）；第三轮收到 LC044/WeChatMsg（作者声明停更）、Dendron（maintenance only）、PyWxDump（描述就是"删库"）。
- **根因**：reject 规则只看 `pushedAt`，**没看 README 顶部的状态徽章 / 警告语**。
- **改进方向**：reject 阶段除了元数据筛选，再做一次 README 前 500 字的 "deprecated / archived / outdated / maintenance only / 停更" 关键词扫描。

### 坑 6：容量上限 35/30 触发但无自动响应
- **现象**：本次批量扫描后 `active_entries: 35/30`，README 健康度变 red，但 SKILL.md 没有自动提示用户拆 domain 或 prune。
- **教训**：触发红色状态后应该**主动建议下一步**，而不是把警告写进面板就结束。

### 坑 7：subagent 风格选项重复 + 选项数超限
- **现象**：第二次 AskUserQuestion 时给了 4 个选项里有"以上都不要"这种逻辑上属于"不选"的选项，浪费容量；第一次还触发 `too_big` 校验（>4 选项）。
- **教训**：AskUserQuestion 选项必须互斥且不超 4 个；"不选"用空答案而不是占一个 slot。

### 坑 8：单轮写 25 份文档时 token 消耗大
- **现象**：第三轮一口气写完 5 主题，主对话上下文越积越长，后期工具调用响应明显变慢；几次 system-reminder 提醒 TaskCreate。
- **教训**：批量任务应该用**子 agent 并行处理（每个主题派一个 Explore/general-purpose 子 agent）**，主对话只做编排和最终汇报。这是本次没做、但应该做的最大优化。

---

## 三、用着顺手的地方（保留并强化）

1. **小红书风格 + "谁别用" + "为什么推它给你"三件套** — 用户没有反复要求改格式，证明模板设计抓到了"小白快速判断"的真痛点。
2. **意图抽取 → 歧义判断 → 多策略检索 → reject → 重排** 五段式流程 — 第二轮证明能挤掉热门生态绑架的项目。
3. **frontmatter + 正文分离** — `intent_matched` / `theme` 字段让后续 `/gitout list` 能按主题筛，扩展性好。
4. **raw/ 目录留 gh search 原始 JSON** — 调试和复现都靠它，**别为了清爽删掉**。
5. **TaskCreate 跟踪 5 主题进度** — 第三轮在长任务里防止漏交付，最后逐个 completed，清晰可查。

---

## 四、下一版 SKILL.md 改造清单（按优先级）

### P0（必改，影响成功率）

1. **`gh search` 命令模板修正**
   - 删掉 `--sort best-match`（省略即可）
   - 默认加 `--match name,description,readme`
   - query 短词组化，**禁止超过 3 个词的长 query**
   - 在 SKILL.md 注明"`gh <subcmd> --help` 验证过的 flag 才能写进来"

2. **意图抽取后增加"知名仓库直查"步骤（新 Step 2.5）**
   ```
   Step 2.5：LLM 列出该领域 3-5 个公认知名 repo（owner/name 形式），
            并行 gh api repos/<owner>/<name> 拿元数据，跟 gh search 结果合并。
   ```
   解决坑 3。

3. **reject 阶段加 README 头部状态扫描**
   - 抓 README 前 500 字
   - 命中 `deprecated|archived|outdated|maintenance only|不再更新|停更|删库` → reject 或降级为 watch
   - 保留时必须在小白文档里标"⚠️ 已停更"

### P1（强烈推荐，影响体验）

4. **批量任务（>5 项目）自动派子 agent**
   - 当用户输入是"多主题"或"扫描"时，主对话只做意图抽取和最终汇报
   - 每个主题用 `Agent(subagent_type: general-purpose)` 并行跑搜索 + 写文档
   - 主对话 token 压力大幅下降

5. **容量超限时自动提议拆 domain**
   - `active_entries > 上限` → 在用户面前直接给出"建议拆成 X / Y / Z 三个 domain"的清单
   - 配合 `/gitout split <domain>` 子命令（新增）

6. **`gh search` 返回 < 3 条时自动降级策略**
   - 第一次空 → 拆词重试（去掉次要词）
   - 第二次仍空 → 改 `--match readme` 单独搜
   - 第三次仍空 → 报告"该领域可能没有匹配关键词的开源项目"并建议换主题

### P2（锦上添花）

7. **AskUserQuestion 选项约束**
   - SKILL.md 明确写"最多 4 选项、必须互斥、不要给'都不要'这种 meta 选项"

8. **小白文档加入"License 商用警告"字段**
   - GPL / AGPL 协议自动在"踩坑提示"里标红
   - 本次有 4 个项目是 AGPL / GPL，但没有统一警告

9. **`/gitout` 命令支持 `--theme <name>` 多主题批量入口**
   - 当前批量扫描是手动驱动，应该让用户直接 `/gitout batch theme1,theme2,...`
   - 配合 P1 第 4 点自动派 subagent

---

## 五、产出质量自评

| 维度 | 当前表现 | 改进空间 |
| --- | --- | --- |
| 命中度 | ✅ 第二轮起 LLM 重排有效 | 仍依赖 LLM 记忆补长尾，缺"知名仓库直查"机制 |
| 写作风格 | ✅ 用户无修改要求 | 可以再加 "License 商用警告" 字段 |
| 漏斗透明度 | ✅ 汇报含意图 → query → 漏斗数字 | 重排序权重表可视化 |
| 容量管理 | ⚠️ 超限只警告不响应 | 需自动建议拆 domain |
| 执行效率 | ⚠️ 25 份文档单主对话写完，token 高 | 必须改成子 agent 并行 |
| 错误恢复 | ⚠️ 一次性 CLI 错误后才发现 | SKILL.md 应预校验所有 flag |

---

## 六、跨会话留给下一次的提醒

- **第一次跑某 query 前，先 `gh search repos "<query>" --limit 1` 探一下**。返回为空就拆词，不要 5 组 query 并行才发现策略错误。
- **意图抽取阶段先让 LLM 报"该领域我知道的 top 5 repo"**，再 search 验证 + 补长尾。一句话替代 10 次 search 失败。
- **批量任务（≥3 主题）必须用 subagent**。当前主对话 + 全工具调用模式只适合单主题。
- **小白文档的"为什么推它给你"段是核心价值点**，写的时候要紧扣用户具体项目（如 OpenClaw、weixinjilu），不要写通用感想。

---

*生成时间：2026-05-22 · 数据基础：本次会话三轮共 35 个项目搜索 + 写作*
