---
type: repo
repo: nikholasnova/Kevlar
domain: local-llm-runtime
status: active
discovered: 2026-05-25
last_reviewed: 2026-05-25
intent_matched: "MLX 本地 server + Anthropic API 兼容"
signals:
  stars: 7
  last_commit: 2026-03-26
  language: Python
  license: unknown
url: https://github.com/nikholasnova/Kevlar
absorption:
  harvested: false
  used: false
  used_in: []
---

# Kevlar · 小白说明书

## 🧐 这是什么
一个**让 Claude Code 跑在本地 MLX 模型上的兼容层**。完整模仿 Anthropic Messages API（含 tool calling、SSE 流、thinking blocks、token counting），后端是你本地的 MLX 模型。

## 💡 解决什么问题
- "我喜欢 Claude Code 这个 CLI 但不想付 API 费 / 想离线用" → Kevlar 起两个本地 server，`ANTHROPIC_BASE_URL` 一指就完事
- "Claude Code 会偷偷发 Haiku 请求做 compaction / 探索 / 起标题，本地 server 模拟不全" → Kevlar 专门跑双 process：主模型 + Haiku 模型分流
- "其他本地 server 每轮都重新 prefill 整个 prompt，KV cache 完全没复用" → Kevlar 做 prompt normalization 稳定前缀，避免重复 prefill

## 🎯 谁该用 / 谁别用
**适合你如果：** 是 Claude Code 重度用户；有 64GB+ 统一内存（能同时塞主模型 + Haiku 模型）；想离线 / 想省 API 费；关心 KV cache 命中率
**别浪费时间如果：** 不用 Claude Code（这是专门针对它的兼容层）；只有 16-32GB 内存（主模型 + Haiku 两个跑不动）；要支持 OpenAI / Ollama 协议

## 🚀 三分钟上手
```bash
git clone https://github.com/nikholasnova/Kevlar.git
cd Kevlar && python3 -m venv .venv && source .venv/bin/activate
pip install -e .
kevlar                    # 一键启动双 server + 自动拉 Claude Code
# 或手动：
kevlar serve --haiku-port 8081
export ANTHROPIC_BASE_URL=http://localhost:8080
unset ANTHROPIC_API_KEY ANTHROPIC_AUTH_TOKEN
claude
```

## 🔑 关键文件 / 关键概念
- 双进程架构：主模型 (8080) + Haiku 模型 (8081)
- 为啥分两个：MLX 不能在同进程的不同线程并发推理（ml-explore/mlx#3078），所以拆进程
- `/v1/messages` + `/v1/messages/count_tokens` + `/v1/model/load|unload` — 核心 endpoint
- 自带 SwiftUI **菜单栏 app**：`make install` 装到 /Applications
- 默认模型：主 Qwen 3.5 122B-A10B 4-bit / Haiku Qwen3-8B 4-bit

## ⚠️ 踩坑提示
- 默认主模型 122B-A10B（MoE 总参 122B），至少 128GB 内存才推荐；中配 64GB 改成 Qwen3-Coder-Next-8bit
- 7 star、license 没写清楚
- 路由规则：模型名含 "haiku" 才走 Haiku 子进程，命名不能乱改
- Claude Code 升级可能打破兼容（API 是事实标准，没合同）

## 🤔 为什么这次推它给你
**核心命中**：你 soft preference 全部命中——MLX 原生（不是 llama.cpp 包装）、本地可跑、Mac 优先；同时正好接 Claude Code 这个你日常用的工具。
**反共识维度**：主流 OpenAI-compatible server 已经够多了，专做 Anthropic-compatible 的极少，Kevlar 把 Claude Code 那些"暗地里发的 Haiku 请求"都模拟了，这是其他 server 没做的细节。
**Trade-off**：硬件门槛高（双模型并存）；只服务 Claude Code 这一个用户场景；和 mio 一样是小作坊项目。

---
*由 /gitout 生成 · 2026-05-25 · intent: "Mac/桌面本地跑 LLM 推理的轻量运行时"*
