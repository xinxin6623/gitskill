# git-self-host · 自建 Git 仓库 / 依赖代理

> 在自己的 VPS 上跑代码托管 + 国内依赖镜像 + git push 部署网站。
> 目标场景：**4C4G 级别国内云服务器**（火山云、阿里云、腾讯云），单人或小团队。

## 健康度

| 指标 | 值 |
|---|---|
| entries | 5 |
| 最近扫描 | 2026-05-26 |
| 主要语言 | Go (4) / Python (1) |
| 全部 active | ✅ |

## 速览表

| ⭐ | 项目 | 用一句话 | 内存占用 |
|---|---|---|---|
| ⭐ | [piku/piku](./entries/piku__piku.md) | `git push` 一键部署网站，最小 PaaS | 极低 |
| ⭐ | [go-gitea/gitea](./entries/go-gitea__gitea.md) | 自托管 Git 平台事实标准，带 mirror | 中（200MB+） |
| | [charmbracelet/soft-serve](./entries/charmbracelet__soft-serve.md) | 单二进制 SSH-only Git server | 极低 |
| ⭐ | [goproxy/goproxy.cn](./entries/goproxy__goproxy.cn.md) | 国内 Go 依赖代理（公共服务） | N/A |
| | [gomods/athens](./entries/gomods__athens.md) | 企业级自建 Go module 代理 | 中 |

## 选型建议（针对你的需求：4C4G 火山云）

**你的两个核心诉求拆开看：**

1. **国内拉依赖** → 看你写什么语言
   - Go：直接用 `goproxy.cn`，要私服上 Athens 或 Gitea Packages
   - 任意语言 + 想统一管控：**Gitea 开 mirror**，把上游 GitHub 仓库镜像下来
   - npm / pip / Maven：**Gitea Packages** 一站式（不在本 domain，但 Gitea entry 里提到了）

2. **git 管理个人网站** → 看你想要多重的工具
   - 极简：**soft-serve** + `post-receive` hook（自己写 rsync 脚本）
   - 体验顺滑：**piku** 一行 `git push` 自动起服务（强推）
   - 想要 Web UI + CI/CD：**Gitea + Actions**（杀鸡用牛刀但全套都有）

**推荐组合**（4C4G 火山云）：

```
火山云 4C4G
├── Gitea (Docker, ~400MB)     ← 代码托管 + GitHub mirror
├── piku (~50MB)               ← 网站 git push 部署
└── nginx (~30MB)              ← 反代 + 静态资源
   合计内存 < 1G，还能跑别的
```

## discarded_queries

```yaml
discarded_queries: []  # 本次 5 个 query 都有效返回
```

## 相关周边（未单列 entry）

- **gogs/gogs** ⭐47547 — Gitea 的上游，已被 Gitea 完全覆盖，新用户直接选 Gitea
- **Forgejo** — Gitea 的社区分叉，主仓在 Codeberg.org（不在 GitHub 上），治理上更社区导向，功能近似 Gitea
- **goproxy/goproxy** ⭐1486 — `goproxy.cn` 背后的代理引擎库，自建时配合使用

> 反思 2026-05-26：最低效环节 = README 抓取后还要手动 grep 过滤 buzzword（已在 SKILL Step 4 落地），下次跑同类主题时直接采用 `head -120` + grep 反 buzzword 的组合
