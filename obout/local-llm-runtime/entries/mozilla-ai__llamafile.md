---
type: repo
repo: mozilla-ai/llamafile
domain: local-llm-runtime
status: active
discovered: 2026-05-25
last_reviewed: 2026-05-25
intent_matched: "单文件可执行的本地 LLM 运行时"
signals:
  stars: 24505
  last_commit: 2026-05-24
  language: C++
  license: Apache-2.0
url: https://github.com/mozilla-ai/llamafile
absorption:
  harvested: false
  used: false
  used_in: []
---

# llamafile · 小白说明书

## 🧐 这是什么
一个把 LLM 权重 + llama.cpp 推理代码 + 所有 OS 适配，**全部塞进一个可执行文件**的项目。Mozilla 出品，下载即跑，零安装。

## 💡 解决什么问题
- "我下了一个 7B 模型，但每次都要装 Python、装 torch、装一堆依赖才能跑" → 用 llamafile 你就 `chmod +x && ./xxx.llamafile` 一行命令
- "想把本地 LLM 打包给同事用、给客户演示" → 一个 4GB 单文件，发邮件丢 U 盘都行
- "Mac、Windows、Linux 切来切去都要重新编译" → llamafile 用 Cosmopolitan Libc 实现真·一个二进制跑 6 个 OS

## 🎯 谁该用 / 谁别用
**适合你如果：** 想把 LLM 当成一个可分发的命令行工具；不想搞 Python / Docker 环境；要给非技术朋友演示本地 LLM；M 系列 Mac 直接用 Metal 加速
**别浪费时间如果：** 要做生产级高并发推理 server；要深度定制采样/量化策略；只想要纯 Swift / 纯 MLX 原生方案

## 🚀 三分钟上手
```bash
# 下一个小模型 (Mozilla 官方打包)
curl -LO https://huggingface.co/mozilla-ai/llamafile_0.10/resolve/main/Qwen3.5-0.8B-Q8_0.llamafile
chmod +x Qwen3.5-0.8B-Q8_0.llamafile
./Qwen3.5-0.8B-Q8_0.llamafile  # 自动开 web UI，浏览器访问 localhost:8080
```

## 🔑 关键文件 / 关键概念
- `Cosmopolitan Libc` — 让一个二进制在 macOS / Linux / Windows / BSD 都能跑的"黑魔法"
- `whisperfile` — 配套的单文件 Whisper 语音转文字
- `Qwen3.5-*.llamafile` — Mozilla 在 HuggingFace 预打包的开箱即用模型

## ⚠️ 踩坑提示
- macOS 首次启动会被 Gatekeeper 拦，需要 `xattr -d com.apple.quarantine xxx.llamafile`
- 单文件 > 4GB 时，Windows / 老 macOS 文件系统可能直接拒绝执行（用 external weights 模式绕过）
- v0.10 换了新构建系统，部分老用法和 v0.9 不兼容，注意看 release notes

## 🤔 为什么这次推它给你
**核心命中**：你的 soft preference 第一条就是"单文件可执行"，llamafile 就是这个理念的旗舰实现。
**反共识维度**：在 Ollama 主导的"server + CLI"范式之外，llamafile 走的是"LLM as a binary"路线——更适合分发、演示、嵌入老旧环境。
**Trade-off**：性能上不一定打得过纯 MLX 原生方案（用的是 llama.cpp + Metal，不是 MLX），如果你追求 Apple Silicon 极致吞吐，下面 mio / mlx-swift-lm 更适合。

---
*由 /gitout 生成 · 2026-05-25 · intent: "Mac/桌面本地跑 LLM 推理的轻量运行时"*
