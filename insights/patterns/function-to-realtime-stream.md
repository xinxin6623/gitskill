---
type: pattern
name: function-to-realtime-stream
sources:
  - gitout/voice-pipeline/entries/gradio-app__fastrtc.md
  - gitout/voice-pipeline/entries/OpenMOSS__MOSS-TTS.md
status: draft
created: 2026-05-30
last_reviewed: 2026-05-30
---

# Function → Realtime Stream

## 问题

想把一个普通 Python 函数（处理音频/视频/文本）变成**实时流式接口**，但 WebRTC / 流协议复杂度高、VAD（语音停顿检测）规则要自己写、部署到公网麻烦。

## 上下文

语音/视频 AI 应用的瓶颈不在 LLM，在**音视频管道**——WebRTC 信令、NAT 穿越、流式输出管理。当你的核心逻辑只是一个 `input → process → output` 函数时，不值得从头搭建管道。

## 方案

把业务函数包装成**流式 handler**，由框架接管 WebRTC / VAD / UI 层：

```
def handler(input_stream):
    while True:
        chunk = receive()
        result = process(chunk)
        yield result

stream = Stream(handler=ReplyOnPause(handler), modality="audio")
stream.ui.launch()  # 自动 WebRTC
stream.mount(app)   # 或挂 FastAPI
```

关键设计点：
- **Handler as Generator**：函数用 `yield` 输出流式结果，框架自动管理缓冲区
- **ReplyOnPause**：自动 VAD，检测停顿触发回复，barge-in 友好
- **Mountable**：可挂到现有 Web 框架（FastAPI/Gradio），不锁技术栈

## 已知实例

- [[gitout/voice-pipeline/entries/gradio-app__fastrtc.md|FastRTC]] — 核心实现，Python 函数 → WebRTC 流，10 行搞定
- [[gitout/voice-pipeline/entries/OpenMOSS__MOSS-TTS.md|MOSS-TTS]] — 流式 TTS 输出，与 FastRTC 组合可做完整语音管道

## 变体 / 取舍

- **轻量级（FastRTC）**：Gradio 生态，10 行起，适合 Demo 和中等规模
- **企业级（LiveKit/Twilio）**：SFU 架构，适合需要录制/转码/多房间的场景
- **纯本地（speech-swift）**：Mac M 系列 in-process，不上云

## 相关模式

- [[insights/patterns/interruptible-streaming-pipeline.md]]（待创建）— 在流式管道中支持打断（barge-in）

---

*由 [[insights/INDEX.md]] 管理 · pattern 模板 v1*
