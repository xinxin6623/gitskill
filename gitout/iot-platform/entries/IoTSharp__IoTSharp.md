---
type: repo
repo: IoTSharp/IoTSharp
domain: iot-platform
status: active
discovered: 2026-05-23
last_reviewed: 2026-05-23
intent_matched: "架构清晰、活跃的中型 IoT 平台"
signals:
  stars: 1329
  last_commit: 2026-05-20
  language: C#
  license: Apache-2.0
url: https://github.com/IoTSharp/IoTSharp
absorption:
  harvested: false
  used: false
  used_in: []
---

# IoTSharp · 小白说明书

## 🧐 这是什么
基于 ASP.NET Core 10 的开源工业 IoT 平台，前端 Vue 3。理念是"ThingsBoard 的 .NET 重写版"，**rule chain（规则链）+ 多租户 + 时序存储** 一应俱全，但代码量远小于 ThingsBoard。Apache-2.0，商用友好。

## 💡 解决什么问题
- 你想要 ThingsBoard 那套规则链/物模型设计，但代码量打骨折
- 你的栈是 .NET，需要一个能直接吃 NuGet 的 IoT 平台
- 你要部署灵活：Docker / Windows 服务 / Linux 服务 / Docker Desktop 扩展都行

## 🎯 谁该用 / 谁别用
**适合你如果：**
- 你接受 .NET（C# / ASP.NET Core）
- 你看重 Apache 协议（无 copyleft 烦恼）
- 你想要"工业级"概念建模（telemetry/attributes/alarms/products/assets/tenants）

**别浪费时间如果：**
- 你纯小白只想要"点点鼠标控制 LED"（IoTSharp 概念偏多）
- 你拒绝 .NET 生态
- 你做的是消费级智能家居（IoTSharp 偏工业 / B 端语义）

## 🚀 三分钟上手
```bash
docker run -d -p 18080:18080 --name iotsharp maikebing/iotsharp:latest
```
或参考官方安装器：<https://iotsharp.net/docs/getting-started/installation-options>

## 🔑 关键文件 / 关键概念
- `IoTSharp/` — 主 ASP.NET Core 应用
- `ClientApp/` — Vue 3 前端控制台
- `IoTSharp.SDKs/` — 多端 SDK（HTTP / MQTT / RT-Thread 包等）
- `IoTSharp.Installer.Windows/` — Windows 安装器
- Rule Chain（规则链）—— 核心抽象，类似 ThingsBoard 的 rule node

## ⚠️ 踩坑提示
- README 最近加了 OpenClaw（AI 助手）路线，主线代码不受影响但 README 显得"AI 味重"
- 前端默认端口 `27915`，不是常见的 8080
- 文档分散在 `iotsharp.net/docs/` 站点，GitHub 上的 README 信息密度偏低
- 不要装最新 main 的 .NET 10 依赖，跟 .NET 8 LTS 项目混用要注意

## 🤔 为什么这次推它给你
**命中：** 架构清晰（√，明确的 Connectivity/Domain/Data/Integration/Delivery 五层）、近期活跃 2026-05（强命中）、中型代码量（√，比 [[jetlinks__jetlinks-community]] 小一档）、MQTT+设备+规则+UI 完整（√）。
**Trade-off：** 中文文档不如 [[kerwincui__FastBee]]，没现成手机端 App。但架构上比 FastBee 更"工业范式"——如果你的学习目标是"看清一个 IoT 平台该怎么切层"，IoTSharp 的层次比 FastBee 更标准。

---
*由 /gitout 生成 · 2026-05-23 · intent: "搜索物联网平台，轻量，容易修改，架构清晰，近期项目"*
