---
type: repo
repo: eduardogoncalves/mlx-coder
domain: local-llm-runtime
status: active
discovered: 2026-05-25
last_reviewed: 2026-05-25
intent_matched: "Swift 原生、in-process MLX coding agent"
signals:
  stars: 8
  last_commit: 2026-05-22
  language: Swift
  license: unknown
url: https://github.com/eduardogoncalves/mlx-coder
absorption:
  harvested: false
  used: false
  used_in: []
---

# mlx-coder · 小白说明书

## 🧐 这是什么
一个 Swift 写的终端编码 agent，**模型直接在 agent 进程内加载**（不起 HTTP server、不调外部 API），等于"Cursor / Claude Code 的本地纯 MLX 版"。

## 💡 解决什么问题
- "跑本地 coding agent 要同时开 llama.cpp server + Node.js agent 两个进程，内存全被吃光" → mlx-coder 一个进程搞定，省下的内存全给模型权重和长上下文
- "想要 macOS 原生沙箱 + 审批 + 权限控制的 agent" → 集成 seatbelt sandbox + per-tool policy + audit log
- "本地 agent 但又想要 MCP / LSP 这套工具协议" → 内置 MCP（HTTP + stdio）+ LSP 安全 rename

## 🎯 谁该用 / 谁别用
**适合你如果：** 已经熟 Claude Code / Codex CLI 想要个纯本地原生替代；macOS 15+、Apple Silicon；想要"agent + 推理同进程"的极简架构；关心权限沙箱
**别浪费时间如果：** macOS < 15；要跨平台；要 GUI（这是纯 CLI）；模型管理要 Ollama 那种 pull/push 体验

## 🚀 三分钟上手
```bash
git clone https://github.com/eduardogoncalves/mlx-coder.git
cd mlx-coder
xcodebuild -scheme MLXCoder -configuration Release \
  -destination 'platform=macOS' -derivedDataPath .build/xcode
sudo cp .build/xcode/Build/Products/Release/MLXCoder /usr/local/bin/mlx-coder
sudo cp -R .build/xcode/Build/Products/Release/mlx-swift_Cmlx.bundle /usr/local/bin/
mlx-coder chat            # 默认模型 ~/models/Qwen/Qwen3.5-9B-4bit
```

## 🔑 关键文件 / 关键概念
- `chat` / `run` / `list-tools` / `show-audit` / `doctor` — 5 个核心子命令
- `mlx-swift_Cmlx.bundle` — Metal shader 包，必须和二进制同目录（关键坑）
- 任务 profile + 隔离工作目录 + delegated-input 校验 — 多任务并行不互相污染
- 默认模型路径：`~/models/Qwen/Qwen3.5-9B-4bit`

## ⚠️ 踩坑提示
- **必须用 `xcodebuild`，不能用 `swift build`** —— swift build 编不出 Metal shader，运行时直接 `Failed to load the default metallib` 崩
- bundle 没拷过去会出同样错
- 要求 macOS 15+ / Swift 6.3.1 / Xcode 16.4+，老系统直接放弃
- 8 star、license 不明，半生产环境用就好

## 🤔 为什么这次推它给你
**核心命中**：你 soft preference "Swift 或 MLX 原生" + "单文件可执行"，mlx-coder 是 in-process Swift agent，构建出来确实是个 `mlx-coder` 单二进制（虽然要拖个 bundle）。
**反共识维度**：主流 coding agent（Cursor / Claude Code / Codex）全是"agent + 远端模型 server"两层架构，mlx-coder 把这俩塞一个进程，反共识到极致。
**Trade-off**：构建坑多（必须 Xcode）；模型管理简陋（要自己 HF 下到固定路径）；如果只想用不想折腾，先看上面 Kevlar / mio。

---
*由 /gitout 生成 · 2026-05-25 · intent: "Mac/桌面本地跑 LLM 推理的轻量运行时"*
