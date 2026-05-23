---
type: repo
repo: gradio-app/fastrtc
domain: misc
status: active
decision: harvest
discovered: 2026-05-22
last_reviewed: 2026-05-22
theme: voice-2
intent_matched: "实时语音/视频通信底座，Python 一函数变 WebRTC"
signals:
  stars: 4587
  last_commit: 2026-05-22
  language: JavaScript
  license: MIT
url: https://github.com/gradio-app/fastrtc
absorption:
  harvested: false
  used: false
  used_in: []
---

# FastRTC · 小白说明书

## 🧐 这是什么

Gradio 团队出的**"把 Python 函数变成 WebRTC 实时流"的库**。你只需要写个普通函数处理音频/视频，FastRTC 自动给你接好 WebRTC、自动检测语音停顿、自动 UI、还能给你一个临时电话号码让人真打过来。4.6k 星，MIT。

## 💡 解决什么问题

做实时语音应用最痛的不是 LLM，是**音视频管道**：

- WebRTC 协议复杂到劝退
- VAD（什么时候算说完）规则要自己写
- 想给 Demo 找人测要部署到公网

FastRTC 全部包好了。**最小例子 10 行 Python**就能让 Gemini / OpenAI realtime / Claude 跟人语音对话，还能 mount 到 FastAPI 当生产端点。

## 🎯 谁该用 / 谁别用

**适合你如果：**
- 想给 openclaw-voice-bot 加一层"网页打开就能说"的入口
- 不想跟 WebRTC 协议死磕
- 用 Gradio / FastAPI 做后端

**别浪费时间如果：**
- 已经有成熟 WebRTC 基建
- 必须用 LiveKit 那种企业级 SFU 架构
- 嫌 Gradio UI 太"研究气"

## 🚀 三分钟上手

```bash
pip install "fastrtc[vad,tts]"
```

```python
from fastrtc import Stream, ReplyOnPause

def handler(audio):
    # 你的 ASR + LLM + TTS 逻辑
    yield response_audio

stream = Stream(handler=ReplyOnPause(handler), modality="audio")
stream.ui.launch()  # 自动起 Gradio + WebRTC
# 或挂 FastAPI：stream.mount(app)
# 或来电：stream.fastphone()  # 给你一个临时号码！
```

## 🔑 关键文件 / 关键概念

- **ReplyOnPause** — 自动检测停顿触发回复，barge-in 友好
- **fastphone()** — 临时电话号码功能，测试神器
- **Stream.mount(app)** — 挂到 FastAPI 自动生成 WebRTC endpoint
- **Talk to Claude 示例** — HuggingFace 上有完整 demo

## ⚠️ 踩坑提示

- WebRTC 信令依赖网络条件，国内有时 NAT 穿越失败
- Gradio 5 之后 API 变过，老教程不一定能跑
- fastphone() 是免费 demo 接口，生产用要接 Twilio

## 🤔 为什么这次推它给你

**上轮搜索发现 caLLMe 是命令行 demo 级别，这次补一个生产级实时通信底座**。FastRTC 解决了你做 voice 项目"怎么从命令行升级到网页/电话入口"的最大障碍。**ReplyOnPause 的可打断设计、自动 WebRTC mount** 都可以直接抄。pattern 候选：`function-to-realtime-stream`。

---
*由 /gitout 生成 · 2026-05-22 · theme: 语音 pipeline 补充角度*
