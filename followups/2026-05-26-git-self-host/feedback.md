# feedback · 对 /gitout 这次搜索的反向打分

> 站在"用户拿到候选 → 后续讨论 → 最终拍板"完整链路回看，/gitout 这次给的候选**够不够、维度全不全、推荐顺序对不对**。

## 总评

**3.5 / 5。** 候选池本身合格（5 个都活、都被引用、都对应不同子方向），但**关键决策维度（协议风险、agent 友好性）在 Step 1 意图抽取阶段完全缺位**，用户必须二轮追问才补上。如果用户没追问，可能按错误推荐去装了 Forgejo（GPL 风险）或 piku（agent 不友好）。

## 具体维度

### ✅ 做得好的

1. **5 query 全有效返回**：单词 query + 反共识词组合（lightweight / git push deploy / go module proxy）召回质量高
2. **候选池覆盖三条路线**：Git server / git push 部署 / 依赖代理——用户后续讨论确实在这三条之间切换
3. **周边项目处理得体**：gogs / Forgejo / goproxy 库降级为周边提及而不是硬挤进 Top 5
4. **soft pref "国内可用 + 4C4G" 都命中**：候选项都验证过资源占用，没出现 GitLab 这种 4G 跑不动的

### ❌ 关键漏抽取的维度

**协议风险**——这是用户的硬约束但首轮完全没问，导致 Forgejo 一开始还在"相关周边"提及。

后果：

- 如果用户更轻信首轮排序，直接装 piku（首推），用上去发现"我其实想要 Git 平台不是 PaaS"
- 如果用户看了"相关周边"装了 Forgejo，魔改+对外用就有 GPL 传染风险

**agent 友好性 / REST API**——AI 时代用户必然关心的维度，首轮也没问。soft-serve 不被淘汰唯一原因是"轻量"，但它没 API 这件事在 entry 里没强调。

### ⚠️ 排序问题

**piku 首推的合理性存疑。** 它解决的是"网站 push 部署"这一窄场景，而用户的真实诉求是"Git 服务器"+"网站部署"的并集，Gitea 一个就能 cover 两者。

首轮把"git push 部署"当成最 sexy 的卖点，导致 piku 排到 #1，但**用户真正需要的是 Gitea**——只是 Gitea 在首轮被描述得太"重"，掩盖了它的优越性。

## 对 /gitout SKILL 的具体建议

### 建议 1：Step 1 意图抽取加协议维度（P0）

在 `intent` 结构里强制加一字段：

```yaml
intent:
  ...
  license_sensitivity: strict | tolerant | ignore   # 默认 strict
```

判断逻辑：
- 用户提"商用 / 公司 / 客户 / 团队 / 闭源 / 二次开发"任意一个 → `strict`，自动 reject GPL/AGPL
- 用户明确说"个人玩 / 不分发" → `tolerant`，GPL 项目降级提示但不淘汰
- 用户说"无所谓 / 看 star" → `ignore`

### 建议 2：Step 1 加 agent 友好维度（P1）

```yaml
intent:
  ...
  agent_friendly: required | preferred | ignore
```

`required` 时，候选必须有 REST API 或文档化 CLI；纯 Web UI / 纯 SSH 项目降级。

### 建议 3：Step 2 歧义判断主动问协议偏好（P0）

意图抽取后，如果用户没暴露协议偏好但候选里有 GPL/AGPL 项目，**主动 AskUserQuestion**：

> 候选里有 X（GPL-3.0），如果你打算对外提供服务可能有传染风险，要排除吗？

### 建议 4：Step 5 排序加"诉求覆盖度"权重（P1）

当前权重表：意图匹配度 / 实现质量 / 软偏好命中 / 活跃度 / stars

建议加一条：**诉求覆盖广度**——能同时解决用户多个子诉求的项目排序应该高于单一诉求专精项目。

本次案例：Gitea cover {Git 平台, 依赖镜像, 网站部署 via Actions} 三条；piku 只 cover {网站部署} 一条。理论上 Gitea 应该首推。

### 建议 5：entry 模板加 License 字段显式展示（P2）

当前 entry frontmatter 有 `signals.license`，但正文里不强调。建议加一段：

```markdown
## 📜 协议风险

- License: MIT
- 商用 / 魔改 / 闭源：✅ 无风险
- 对外提供 SaaS 服务：✅ 无传染义务
```

GPL/AGPL 项目要在这段显式标红警告。

## 采纳状态

| 建议 | 状态 | 落地位置 |
|---|---|---|
| 1. Step 1 加 license_sensitivity 字段 | ✅ 已落 | SKILL.md Step 1 intent schema |
| 2. Step 1 加 agent_friendly 字段 | ✅ 已落 | SKILL.md Step 1 intent schema |
| 3. Step 2 候选有 GPL 时主动追问 | ✅ 已落 | SKILL.md Step 2.1（新增节）|
| 4. Step 5 加"诉求覆盖广度"权重 | ✅ 已落 | SKILL.md Step 5 权重表 |
| 5. entry 模板加显式协议风险段 | ✅ 已落 | SKILL.md Step 6 entry 模板 + 写作硬约束 |

落地时间：2026-05-26（同日），SKILL.md 升级为 v2.1，详见文末 ChangeLog。

## 留待下次验证

- 实际部署 Gitea 后回填使用感受到 [decision.md](./decision.md) 后续动作清单
- 如果部署遇到 SKILL 没预警的坑，更新这份 feedback 加"实操踩坑"段
- 下次跑 /gitout 时验证 5 项改进真的生效（重点看 license_sensitivity 字段有没有出现在结构化汇报里）
