---
type: repo
repo: OpenHands/OpenHands
domain: dev-productivity/ai-coding-agent
status: active
discovered: 2026-05-23
last_reviewed: 2026-05-23
intent_matched: "学术派 SWE-Bench 77.6 分的开源 AI 工程师，全套 SDK + CLI + GUI + 沙箱"
signals:
  stars: 74593
  last_commit: 2026-05-23
  language: Python
  license: MIT
url: https://github.com/OpenHands/OpenHands
absorption:
  harvested: false
  used: false
  used_in: []
---

# OpenHands · 小白说明书

## 🧐 这是什么
学术界拿来刷 SWE-Bench 跑分的开源 AI 软件工程师本体，从 SDK、CLI、本地 GUI 到企业版一整套，目标是"派一个 Devin 出来给你打工"。

## 💡 解决什么问题
- 你想跑一个**自主**完成 issue → 代码 → PR 的 agent，而不只是辅助你打字
- 你想要一个能**隔离在 Docker / K8s 沙箱**里跑命令的 agent，不让它把你本机搞砸
- 你想要一个**有论文背书、SWE-Bench 77.6 分**的工业级实现可以照抄架构

## 🎯 谁该用 / 谁别用
**适合你如果：**
- 想研究 agent loop 工程实现（runtime / event stream / action-observation 这一套很值得读）
- 需要跑批量自主任务（比如同时让 100 个 agent 修 100 个 bug）
- 想自建企业内部 Devin

**别浪费时间如果：**
- 你只想要"我打字它补全"，OpenHands 太重
- 你不喜欢 Docker，因为隔离运行时是它的核心卖点
- 你已经在 Claude Code 里用得很顺手，OpenHands 的差异在"全自动 + 沙箱"而不是 IDE 体验

## 🚀 三分钟上手
```bash
# Docker 模式（推荐，沙箱安全）
docker pull docker.all-hands.dev/all-hands-ai/openhands:latest
docker run -it --pull=always \
    -e SANDBOX_RUNTIME_CONTAINER_IMAGE=docker.all-hands.dev/all-hands-ai/runtime:latest \
    -v /var/run/docker.sock:/var/run/docker.sock \
    -p 3000:3000 \
    --name openhands \
    docker.all-hands.dev/all-hands-ai/openhands:latest

# 或者纯 SDK 写代码
pip install openhands-sdk
```

## 🔑 关键文件 / 关键概念
- `openhands/controller/` — agent 主循环，event stream 架构
- `openhands/runtime/` — 沙箱运行时抽象（Docker / Modal / Remote）
- `openhands/agenthub/` — 不同 agent 策略（CodeActAgent 是主力）
- 配套 repo `OpenHands/software-agent-sdk` — 想嵌入自己代码就读这个

## ⚠️ 踩坑提示
- 初次跑会拉好几个 Docker 镜像，几个 G，国内网络注意代理
- 默认 GUI 很重（React + REST + 沙箱容器），轻量用 CLI 或 SDK 就够
- enterprise/ 目录是源码可见但**非 MIT**，商用前看清楚 license

## 🤔 为什么这次推它给你
你已经在用 Claude Code（一个**与你协作**的 harness）。OpenHands 是另一个极端——**派出去就别管了**的全自动 agent。它的 event stream + runtime 沙箱架构是目前开源圈里被学术界、benchmark 引用最多的工程参考实现，读架构比读 Claude Code（闭源）值得。trade-off 是部署比 Claude Code 重 10 倍。

---
*由 /gitout 生成 · 2026-05-23 · intent: "个人提效工具，skill ide codeing harness 工程"*
