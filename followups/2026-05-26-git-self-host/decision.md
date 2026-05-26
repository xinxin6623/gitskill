# decision · Gitea 自建 Git 仓库选型结论

> 这份文档脱离上下文也能读懂。和飞书推送版本同源。

## 一句话结论

**装 Gitea，一个就够你用 3 年。** MIT 协议干净 + Go 单二进制优雅 + 完整 REST API 让 Claude Code 顺畅维护 + Packages 收纳 AI 时代杂七杂八的源码物料。

## 场景

- 服务器：4 核 4G 火山云
- 用途：放代码、放 AI 时代的依赖 / 项目源码 / skills 源码、偶尔 push 部署网站
- 硬约束：没有版权和开源协议风险、代码优雅、便于 agent 维护

## 三层维度对比

### 1. 协议风险

| 项目 | License | 评估 |
|---|---|---|
| **Gitea** | **MIT** | ✅ 最干净，商用/魔改/闭源都没事 |
| soft-serve | MIT | ✅ 同样干净 |
| piku | MIT | ✅ 干净 |
| Forgejo | GPL-3.0 | ⚠️ 魔改后对外提供服务可能触发开源义务 |
| GitLab CE | MIT + EE 部分专有 | ⚠️ 边界不清，企业版条款复杂 |
| Gogs | MIT | ✅ 但已被 Gitea 超越，不推 |

→ **Forgejo / GitLab 出局。Gitea / soft-serve / piku 三个 MIT 都安全。**

### 2. 代码优雅 + agent 友好

| 项目 | 代码可读性 | agent 维护难度 |
|---|---|---|
| **Gitea** | Go 单仓库，模块清晰，文档齐 | ✅ Claude Code 改 app.ini / 写 webhook 脚本都顺 |
| soft-serve | Go 但很薄，无 Web API | ❌ agent 维护要靠 SSH 命令，没 REST API 别扭 |
| piku | Python 单文件 ~2000 行 | ⚠️ 极简但"一切都在一个文件里"，扩展靠 hack |

→ **Gitea 有完整 REST API + Webhook + Actions**，agent 自动化场景全是一句 curl 的事。

### 3. AI 时代多源码

| 能力 | Gitea | soft-serve | piku |
|---|---|---|---|
| Packages（npm/PyPI/Container/Generic）| ✅ | ❌ | ❌ |
| Mirror 上游仓库 | ✅ | ❌ | ❌ |
| Releases 发版 | ✅ | ❌ | ❌ |

→ **piku 和 soft-serve 只是 Git server，不是"代码物料中心"。**

## 部署方案

```yaml
# ~/gitea/docker-compose.yml
services:
  gitea:
    image: gitea/gitea:1.22  # 锁版本，agent 升级前先评估
    container_name: gitea
    environment:
      - USER_UID=1000
      - USER_GID=1000
      - GITEA__server__DOMAIN=git.your-domain.com
      - GITEA__server__ROOT_URL=https://git.your-domain.com/
      - GITEA__server__SSH_PORT=2222
      - GITEA__service__DISABLE_REGISTRATION=true   # 个人用，关掉注册
    volumes:
      - ./data:/data
      - /etc/timezone:/etc/timezone:ro
      - /etc/localtime:/etc/localtime:ro
    ports:
      - "3000:3000"
      - "2222:22"
    restart: always
```

## 为什么不顺手装 piku

需求里没有"复杂应用部署"，只是放代码 + 偶尔发个站。**Gitea Actions + 一个 5 行 workflow**（rsync 到 nginx 目录）就能干 piku 的活，不用再起一个进程。

## 未来切换信号

等到某天觉得"Gitea 200MB 内存舍不得"，再切 soft-serve。那天大概率不会到来。

## 后续动作

- [ ] 火山云服务器装 Docker
- [ ] 跑 docker-compose up
- [ ] 走完安装向导，关闭公开注册
- [ ] 试一次 Mirror（拉个 GitHub 上的 skill 仓库进来）
- [ ] 试一次 Packages（push 一个 npm tarball 或 Generic 文件）
- [ ] 写一份 Gitea Actions workflow 自动部署个人站
