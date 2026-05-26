---
type: repo
repo: 78/xiaozhi-esp32
domain: xiaozhi-ai
status: active
discovered: 2026-05-23
last_reviewed: 2026-05-23
intent_matched: "xiaozhi 同类型 — 原版固件基准"
signals:
  stars: 26685
  last_commit: 2026-05-22
  language: C++
  license: MIT
url: https://github.com/78/xiaozhi-esp32
absorption:
  harvested: false
  used: false
  used_in: []
---

# xiaozhi-esp32 · 小白说明书

## 🧐 这是什么
虾哥（作者 78）的 ESP32 AI 语音盒子原版固件，基于 MCP 协议跑 LLM 对话，是整个 xiaozhi 生态的"祖师爷"。

## 💡 解决什么问题
- 想自己造一个能说话的 AI 小盒子，但不知道从哪开始
- 想让一块几十块钱的 ESP32 接上 Qwen / DeepSeek 这种大模型
- 想跑离线唤醒词 + 流式 ASR + LLM + TTS 全链路

## 🎯 谁该用 / 谁别用
**适合你如果：**
- 想 DIY 一个 AI 对话硬件，且 ESP32 + ESP-IDF 不陌生
- 想用 MCP 协议把语音助手当万能控制器
- 不介意做点焊接 / 刷固件的活

**别浪费时间如果：**
- 想要"插电即用"的成品（这只是固件源码）
- 不想自己搭后端服务（要配合 xiaozhi-esp32-server 之类）
- 只会写 Web，没有嵌入式基础

## 🚀 三分钟上手
```bash
git clone https://github.com/78/xiaozhi-esp32
cd xiaozhi-esp32
# 装 ESP-IDF v5.4+，然后
idf.py set-target esp32s3
idf.py menuconfig    # 配置 board / wifi / 后端 URL
idf.py build flash monitor
```

## 🔑 关键文件 / 关键概念
- `main/` — 固件核心，包含 ASR/TTS 流水线
- `partitions/v2/` — v2 分区表，跟 v1 不兼容，OTA 升级不了
- `docs/websocket.md`、MCP 协议 — 后端通信两种方式
- ESP-SR — 乐鑫的离线唤醒库

## ⚠️ 踩坑提示
- **v1 → v2 不能 OTA**，必须重新刷固件，v1 维护到 2026-02
- 默认对接虾哥的官方后端服务；想自建后端必须配合服务端项目（见下面几条）
- ESP32-S3 与普通 ESP32 引脚/性能差距大，看清自己买的是哪款再 flash

## 🤔 为什么这次推它给你
你说"xiaozhi ai 相关同类型"——这就是源头，所有衍生项目都绕不开它。26.6k 星、近 30 天还在更新、MIT license 干净，且明确符合你说的"AI 语音对话硬件 + LLM"硬约束。trade-off：纯固件，没有后端就跑不起来，所以下面几个服务端实现是必备搭档。

---
*由 /gitout 生成 · 2026-05-23 · intent: "搜一组关于 xiaozhi ai 相关的同类型项目"*
