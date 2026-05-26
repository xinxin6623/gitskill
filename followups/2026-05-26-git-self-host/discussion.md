# discussion · 第二轮约束如何收窄到 Gitea

> 不抄逐字 transcript，只记关键节点和决策转折。

## 时间线

### 节点 1 · /gitout 首轮产出（背景）

候选池 5 个：piku / gitea / soft-serve / goproxy.cn / athens
首推顺序：piku（git push 部署网站方向）> gitea（万能但重）> soft-serve > goproxy.cn > athens

**首轮没有暴露的维度**：开源协议、agent 友好性、未来扩展性

### 节点 2 · 用户第二轮约束 ⭐

> "我的需求比较轻量，代码量不会很多，随着 AI 发展，一些依赖、项目源码、skills 源码等，你推荐部署哪个，没有版权和开源协议等风险，代码优雅且便于 agent 维护"

新增 4 个硬约束：

1. **代码量轻**（不需要 piku 那种 PaaS 复杂度）
2. **版权 / 开源协议无风险**（首轮完全没问）
3. **代码优雅**（这点是软偏好但对 agent 重要）
4. **便于 agent 维护**（要 REST API、要文档化的扩展点）

隐含还有一条：**AI 时代多种源码物料**（依赖、项目源码、skills 源码）。

### 节点 3 · 维度重新筛选

按新维度重排：

| 项目 | License | agent 友好 | 源码物料能力 |
|---|---|---|---|
| Gitea | MIT ✅ | REST API + Webhook + Actions ✅ | Packages（npm/PyPI/Container/Generic）+ Mirror + Releases ✅ |
| soft-serve | MIT ✅ | 只有 SSH，无 API ❌ | 只是 Git server ❌ |
| piku | MIT ✅ | Python 单文件，扩展靠 hack ⚠️ | 不是物料中心 ❌ |
| **Forgejo** | **GPL-3.0** ⚠️ | 同 Gitea | 同 Gitea |
| GitLab CE | MIT + EE 专有 ⚠️ | 强 | 强但重 |

**关键决策**：Forgejo 在第一次推荐时只在"相关周边"提过，没单列 entry——这次因为协议风险被显式淘汰。**GPL-3.0 在用户魔改+对外提供服务的场景下有传染风险**，soft-serve 没 API 对 agent 不友好，piku 单文件架构扩展会变 hack。

### 节点 4 · 拍板 Gitea

理由三层（详见 decision.md）：

1. MIT 协议最干净
2. 完整 REST API → agent 顺畅维护
3. Packages 私服直接对应"AI 时代多源码物料"诉求

并给出 `docker-compose.yml` 直接可抄。

### 节点 5 · 推飞书

> "把这个最后的结论推到我的飞书文档，是他更容易人类阅读"

用 lark-doc skill 创建文档，结构：

- 顶部 callout 一句话结论
- 三层维度对比（两张表 + 高亮）
- 部署方案（代码块）
- 双栏 callout 总结

成品 URL: https://ccn3ixoh82kp.feishu.cn/docx/J7NldnCe1oEgY6xJ1qNc4Ugnn6f

### 节点 6 · 用户提议建 followups/ 目录 ⭐

> "有必要在整个项目创建一个基于 github 结果的延续开发和产出文档的目录了，这样也能记录使用反馈和使用情况"

→ 触发本次 followup 目录创建（也就是你正在读的这个）。

## 关键转折

| 时刻 | 转折 |
|---|---|
| 节点 2 | 协议风险被引入 → Forgejo / GitLab 直接出局 |
| 节点 3 | "代码量轻"重新解读：不是"用最小工具"，而是"需求轻的话不要装两个" → piku 被合并进 Gitea Actions |
| 节点 4 | piku 从 /gitout 首推降级为"可选"——因为 Gitea Actions 能干同样的事 |

## 留待验证的假设

- Gitea Packages 真的能稳放 skills 物料？（待部署后试 npm/Generic 仓库）
- Gitea Actions + rsync 部署网站到底比 piku 麻烦多少？（待实际写 workflow）
- 4G 内存够不够 Gitea + 一两个 Actions runner 并行跑？（理论够但没测过）
