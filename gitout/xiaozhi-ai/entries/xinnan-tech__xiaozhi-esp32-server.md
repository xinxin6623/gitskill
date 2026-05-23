---
type: repo
repo: xinnan-tech/xiaozhi-esp32-server
domain: xiaozhi-ai
status: active
discovered: 2026-05-23
last_reviewed: 2026-05-23
intent_matched: "xiaozhi 同类型 — Python/Vue 全栈后端"
signals:
  stars: 9612
  last_commit: 2026-05-20
  language: JavaScript
  license: MIT
url: https://github.com/xinnan-tech/xiaozhi-esp32-server
absorption:
  harvested: false
  used: false
  used_in: []
---

# xiaozhi-esp32-server · 小白说明书

## 🧐 这是什么
社区里最火的 xiaozhi 自建后端，Python + Java + Vue 三件套，让你不用依赖虾哥官方服务器也能跑全套对话流程。

## 💡 解决什么问题
- 不想让自己的 AI 盒子流量都过别人服务器（隐私 / 稳定性）
- 想加自定义角色、声纹识别、私有知识库
- 想跑 MQTT+UDP 或 Websocket，两种协议自由切换

## 🎯 谁该用 / 谁别用
**适合你如果：**
- 已经有一台 xiaozhi-esp32 硬件，想自建后端
- Python 栈舒服，能 Docker compose 跑起来
- 想做企业内网部署 / 多设备管理

**别浪费时间如果：**
- 只想随便玩玩——直接连官方服务器更省事
- 想要 Java 企业级框架（看 server-java 那条）
- 服务器资源吃紧（ASR + LLM + TTS 流水线吃内存）

## 🚀 三分钟上手
```bash
git clone https://github.com/xinnan-tech/xiaozhi-esp32-server
cd xiaozhi-esp32-server
docker compose up -d
# 然后在 xiaozhi-esp32 固件里改后端 URL 指向你的 IP
```

## 🔑 关键文件 / 关键概念
- `main/xiaozhi-server/` — Python 核心服务，跑 ASR/LLM/TTS 编排
- `main/manager-api/` — Java 管理后端
- `main/manager-web/` — Vue 管理界面
- `docs/FAQ.md` — 常见坑文档，先看这个

## ⚠️ 踩坑提示
- 三个组件要一起跑，单跑 Python server 没管理界面
- 默认对接的 ASR/TTS 供应商有几家是收费的，看清配置文件
- 多语言文档（英/越/德/葡）齐全，但 issue 区主要是中文

## 🤔 为什么这次推它给你
xiaozhi 生态里事实标准的自建后端，9.6k 星社区最大，中文文档齐全、活跃维护。命中你的"开源 + 端侧接 LLM"。trade-off：组件多、部署稍重，如果你只想要 Python 单文件 server，看 py-xiaozhi 那条。

---
*由 /gitout 生成 · 2026-05-23 · intent: "搜一组关于 xiaozhi ai 相关的同类型项目"*
