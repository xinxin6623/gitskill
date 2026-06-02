# 2026-05-26 · git-self-host 主题首跑 retro

## 输入
`/gitout 搜索git 仓库自建相关项目，自己搭建 git 仓库主要是为了国内环境拉取相关依赖，还有一个想法是用 git 管理个人发布的网站，服务器 4 核4g，火山云服务器`

## 意图分流
- input_type: **need**（自然语言需求描述，无专名）
- what: 自托管 Git 服务器 + 国内依赖代理 + git push 部署网站
- 关键硬约束: 4C4G 火山云服务器、Linux、轻量
- 软偏好: 单二进制 / Docker 一键 / 国内可用 / 支持 webhook

## 检索漏斗
| 阶段 | 数量 |
|---|---|
| query 数 | 5（self-hosted git / lightweight git server / git deploy webhook / go module proxy / git push deploy） |
| 候选池（去重后） | 40 |
| 一轮 reject（元数据） | -31（停更超 365 天 + 无关误命中 + 服务器面板 + 0 star 噪音） |
| 二轮 reject（语义） | -3（gogs 被 gitea 覆盖；goproxy/goproxy 库降级周边；Forgejo 主仓不在 GitHub） |
| 入选 | **5** |

## 入选项目
| Repo | 角色 |
|---|---|
| piku/piku | 直击"git push 部署网站"的 PaaS |
| go-gitea/gitea | 自托管 Git + mirror（标准方案） |
| charmbracelet/soft-serve | 极简 SSH-only Git server |
| goproxy/goproxy.cn | 国内 Go 依赖代理消费端 |
| gomods/athens | 国内 Go 依赖代理企业端 |

## 关键发现 / 这次踩到的坑

1. **need 模式下 query 全 8 条返回率 100%**——单词 query（`self-hosted git`, `go module proxy`）质量明显优于多词 query，验证 SKILL "单 query ≤3 词"规则有效。
2. **5 个 query 跨语义维度差异大**：`go module proxy` 和 `git push deploy` 几乎零重叠，但都是用户意图的关键面向——5-query 多策略并行抓到了"全景"。
3. **GitLab 类必须主动 reject**：明确写"4G 内存"硬约束后，`turnkeylinux-apps/gitlab` 这种镜像项目仍然被 query 召回，要靠语义 reject 拦掉。
4. **Forgejo 困境**：Forgejo 是值得推的项目，但主仓在 Codeberg.org 不在 GitHub 上，本 skill 受限于 gh CLI 工具看不到——只能在 Gitea entry 里口头提一句。这是 gh search 工具的固有局限。
5. **goproxy.cn vs Athens 同维度对比**：两个项目角色互补不冲突，分别给"消费"和"企业自建"两条路径，文档里互相 cross-link。

## 下次改进

- need 模式 5 query 全有效是新纪录，可以小规模放手让 LLM 自由发挥 query 数（3-7 浮动）
- 当遇到"非 GitHub 但重要"的项目（如 Forgejo @ Codeberg），SKILL 应该考虑加一条"周边提示规则"：检测到 gitea/forgejo/gitlab/gogs 这类 fork 链时，主动在文档里 cross-mention 其他实现
- "选型组合表"（domain README 里那个"火山云 4C4G 内存预算"框）很受用，针对"用户场景明确"的 need 模式可以默认加入

## INDEX 自检
- 实际 entries: 5（piku / gitea / soft-serve / goproxy.cn / athens）
- INDEX.md 引用: 5
- ✅ 0 缺失 0 孤儿
