# local-llm-runtime · Mac 本地 LLM 推理运行时

## 健康度
- entries: 5
- last_updated: 2026-05-25
- focus: Apple Silicon 本地跑 7B-30B 模型的反共识/原生方案；不收 Ollama 本体与 cloud API 包装

## 当前条目
| Repo | ⭐ Stars | 一句话 |
|------|---------|--------|
| ⭐ [mozilla-ai/llamafile](entries/mozilla-ai__llamafile.md) | 24505 | 把模型权重 + 推理代码塞进一个可执行文件，下载即跑、零安装、跨 OS |
| [ml-explore/mlx-swift-lm](entries/ml-explore__mlx-swift-lm.md) | 523 | Apple 官方 Swift LLM 库，把 mlx-lm 那套搬进 Xcode 嵌进 app |
| [Ruler-Dev/mio](entries/Ruler-Dev__mio.md) | 4 | DFlash 投机解码 + PolarQuant KV 压缩，默认开起来的极致 MLX 引擎 |
| [eduardogoncalves/mlx-coder](entries/eduardogoncalves__mlx-coder.md) | 8 | Swift 写的 in-process coding agent，agent 和 MLX 推理同一个进程 |
| [nikholasnova/Kevlar](entries/nikholasnova__Kevlar.md) | 7 | 让 Claude Code 跑在你本地 MLX 模型上的 Anthropic API 兼容层 |

## ⭐ 首推说明
**llamafile** 在五条入选里独一档：唯一星数级生态、Mozilla 长期维护、最契合"单文件可执行"这条 soft preference。其余四条都是各自方向的硬核反共识选择，按你的硬件和使用场景挑：
- 64GB+ Mac、Claude Code 重度用户 → **Kevlar**
- 32-64GB Mac、想试投机解码新论文 → **mio**
- 做 macOS / iOS app 嵌 LLM → **mlx-swift-lm**
- 想用纯本地 coding agent、能容忍 Xcode 构建坑 → **mlx-coder**
