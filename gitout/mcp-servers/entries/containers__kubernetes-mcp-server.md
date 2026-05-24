---
type: repo
repo: containers/kubernetes-mcp-server
domain: mcp-servers
status: active
discovered: 2026-05-25
last_reviewed: 2026-05-25
intent_matched: "让 agent 直接操作 K8s 集群，不要包 kubectl"
signals:
  stars: 1615
  last_commit: 2026-05-21
  language: Go
  license: Apache-2.0
url: https://github.com/containers/kubernetes-mcp-server
absorption:
  harvested: false
  used: false
  used_in: []
---

# containers/kubernetes-mcp-server · 小白说明书

## 🧐 这是什么
Go 写的 Kubernetes/OpenShift MCP server，**直接走 Kubernetes API**——不是包 `kubectl` 或 `helm`，所以单二进制就能跑，不依赖 Node/Python/kubectl。覆盖通用 CRUD、Pod（list/get/logs/exec/run/top）、Namespace、Events、Helm（install/list/uninstall）、Tekton（pipeline/task），还支持 OpenTelemetry tracing。

## 💡 解决什么问题
- 你想让 Claude Code 帮你"看下 prod 命名空间下哪个 Pod 在 CrashLoopBackOff"，但又不想给 agent 直接 shell 跑 kubectl——这个 MCP server 把 K8s 操作变成结构化工具调用，可控、可审计。
- 多集群运维：一个 server 进程可以同时操作 kubeconfig 里所有 cluster。
- 想给团队搭一个"AI 运维助手"，需要可观测（OTEL）、可生产部署（单二进制 + 容器镜像）——这个在工程化上比 npm 类玩具 server 成熟很多。

## 🎯 谁该用 / 谁别用
**适合你如果：** 你有真正的 K8s 集群要管理；想给 AI 工作流加 K8s 工具；在意性能/部署形态（要原生二进制不要 Node 运行时）。
**别浪费时间如果：** 你只是 minikube 玩玩——直接 kubectl 就好，给 agent 加 K8s 工具是过度工程；你的需求是"AI 自己写 yaml 然后 apply"那种 vibes coding，安全风险太大别走这条路。

## 🚀 三分钟上手
```bash
# npx 最快
{
  "mcpServers": {
    "kubernetes": {
      "command": "npx",
      "args": ["-y", "kubernetes-mcp-server@latest"]
    }
  }
}

# 或者直接下载 release 二进制（Linux/macOS/Windows）
# 或者 pip install kubernetes-mcp-server
# 或者 docker pull quay.io/manusa/kubernetes_mcp_server
```

## 🔑 关键文件 / 关键概念
- `docs/getting-started-kubernetes.md` — **生产部署必看**：教你做专属 ServiceAccount + 只读 RBAC
- `docs/getting-started-claude-code.md` — Claude Code 接入指南
- `docs/OTEL.md` — OpenTelemetry tracing 配置（生产可观测必装）
- `/stats` HTTP 端点 — 实时调用统计

## ⚠️ 踩坑提示
- **默认走你当前 kubeconfig 的 context**——别在 prod context 下随便让 agent 试错，先用 dev context 或专属只读 SA。
- Helm install/uninstall 是真的写操作，权限给小点。
- 单二进制虽好，但跨平台时记得选对 arch（M 系列 Mac 选 darwin/arm64）。

## 🤔 为什么这次推它给你
你的意图是"高质量单功能 server"——DevOps 类必须有一个代表，K8s 是绝对刚需场景。这份在 K8s MCP 里属于**最工程化的**：Go 原生（不是 kubectl 包装）、有 OTEL、有 RBAC 文档、多种分发形式。命中 hard_constraints（开源 Apache-2.0），命中 soft preferences（含部署文档、生产可用）。trade-off：是 Go 不是 TS/Python（你 soft preference 提到这两个），但 K8s 场景下 Go 反而更合适，启动更快。

---
*由 /gitout 生成 · 2026-05-25 · intent: "MCP server 生态合集 — 给 agent 加工具能力"*
