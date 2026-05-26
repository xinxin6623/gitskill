# followups · /gitout 搜索之后的讨论 / 选型 / 反馈

> 每次 /gitout 跑完，**通常还会有一段后续讨论**：追问、改约束、拍板、推飞书、回头给搜索打分。
> 这些"搜索之后"的产出归这里——既是知识沉淀，也是对 /gitout 搜索质量的反向反馈。

## 这个目录在解决什么

`gitout/` 只管"发现 GitHub 项目"（搜索 → entry 卡片 → 流程复盘）；但用户拿到 5 个候选之后还有大量决策动作：

- 追问硬约束（协议风险、agent 友好性、未来扩展）
- 在候选里二次筛选 / 拍板
- 把结论推送到外部系统（飞书 / Notion / 团队群）
- 实际部署后的踩坑反馈
- 回头评价"这次搜索给的候选够不够、有没有遗漏维度"

这些都是 `gitout/retros/`（流程复盘）和 `gitout/<domain>/entries/`（项目卡片）都接不住的内容。

## 目录约定

```
followups/
├── README.md                        # 本文件
├── INDEX.md                         # 时序索引（最新在上）
└── <YYYY-MM-DD>-<domain-or-topic>/
    ├── README.md                    # 本次 followup 主索引
    ├── discussion.md                # 后续讨论的关键节点摘要
    ├── decision.md                  # 最终选型结论（独立可读）
    ├── feedback.md                  # 对 /gitout 这次搜索的反向打分
    └── exports/                     # 一次性导出产物
        └── feishu-<slug>.md         # 推送过的飞书文档本地副本（含 URL）
```

### 命名

- 目录名：`<YYYY-MM-DD>-<domain-or-topic>`，日期对齐当时 /gitout 的 retro 日期
- domain-or-topic 与 `gitout/<domain>/` 保持一致（如本次 `git-self-host`）；如果跨多个 domain，用主题词

### 三个文件分工

| 文件 | 写什么 | 不写什么 |
|---|---|---|
| `discussion.md` | 追问/转折/二次筛选的关键节点摘要 | 逐字 transcript、原始对话历史 |
| `decision.md` | 拍板结论 + 理由（脱离上下文也能读懂）| 中间犹豫、被推翻的方案细节 |
| `feedback.md` | 对 /gitout 这次搜索的反向打分 + 改进建议 | 抒情、流程复盘（那是 gitout/retros/ 的活） |

## 与 gitout/ 的边界

| 它写 | 归哪 |
|---|---|
| 「项目卡片，三分钟看懂能不能用」 | `gitout/<domain>/entries/<repo>.md` |
| 「这次 /gitout 流程哪里跑得顺/堵」 | `gitout/retros/<date>-<topic>-retro.md` |
| 「搜索之后我们怎么聊的、最后选了啥、推到哪、效果如何」 | `followups/<date>-<topic>/` ← 本目录 |

## 飞书联动

**本地是真相源，飞书不同步。**

`exports/feishu-*.md` 是飞书文档的**一次性快照副本**，目的是：

- 本地能搜到飞书发过什么
- 飞书文档万一被删/改名，本地还有底稿
- 不会反向同步——飞书改了不影响本地，本地改了也不自动推飞书

如果需要更新飞书文档，**先改本地，再手动用 `lark-cli docs +update` 推一次**，不靠自动化。

## 维护节奏

- /gitout 跑完后**如果有后续讨论**，就开一个 followup 目录
- 短期讨论（一两轮就结束）也建议开，哪怕 decision.md 只有 3 行——价值在 feedback.md
- 旧的不删，作为时序档案
