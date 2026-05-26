---
type: repo
repo: jetlinks/jetlinks-community
domain: iot-platform
status: active
discovered: 2026-05-23
last_reviewed: 2026-05-23
intent_matched: "架构最清晰的企业级 IoT 平台（参考向）"
signals:
  stars: 6496
  last_commit: 2026-04-18
  language: Java
  license: Apache-2.0
url: https://github.com/jetlinks/jetlinks-community
absorption:
  harvested: false
  used: false
  used_in: []
---

# JetLinks · 小白说明书

## 🧐 这是什么
国内 hsweb 团队做的"企业级"开源 IoT 平台，基于 **Spring Boot 3.x + WebFlux + Netty + Vert.x + Project Reactor 全响应式技术栈**。架构上是这组项目里**模块切分最规整**的——13 个 components + 7 个 managers + standalone 启动模块，标准的"组件 + 业务 + 启动"三层骨架。

## 💡 解决什么问题
- 你想看"一个企业级响应式 IoT 平台到底怎么切模块"——JetLinks 的目录结构本身就是教科书
- 你要做产品而非毕设，需要规则引擎、网关、协议适配、数据可视化等都到位
- 你能驾驭 Reactor / WebFlux 那套异步范式

## 🎯 谁该用 / 谁别用
**适合你如果：**
- 你做企业级 IoT 项目，需要高并发设备接入
- 你团队熟 Spring 全家桶 + 能学响应式编程
- 你看重 Apache-2.0 协议，介意 AGPL

**别浪费时间如果：**
- 你想"代码能读完"（JetLinks 是这组里最重的，违反你列的硬约束）
- 你不熟响应式编程（WebFlux/Reactor 学习曲线陡）
- 你只是想做个智能家居 Demo（杀鸡用牛刀）

## 🚀 三分钟上手
```bash
git clone https://github.com/jetlinks/jetlinks-community.git
cd jetlinks-community/docker/run-all
docker-compose up -d
# 访问 http://localhost:8848
```
最小依赖：Java 17 + Redis + TimescaleDB（号称"无需大量中间件"，但确实需要这三个）。

## 🔑 关键文件 / 关键概念
- `jetlinks-components/` — 公共组件（13 个：gateway/network/protocol/rule-engine/timeseries 等）
- `jetlinks-manager/` — 业务管理（7 个：device/network/notify/rule-engine 等）
- `jetlinks-standalone/` — 启动模块
- `simulator/` — 设备模拟器（学习用很有价值）
- 物模型 + 规则引擎 + 协议解析三大核心

## ⚠️ 踩坑提示
- **代码量大**，第一次读不要试图通读，先看 `device-manager` 单模块
- 响应式代码到处是 `Mono` / `Flux`，没有响应式基础会很懵
- 企业版功能藏起来了（社区版能用的功能比商业页面少）
- 中文文档主要在 jetlinks.cn，QQ 群是社区主战场（不是 GitHub Issues）

## 🤔 为什么这次推它给你
**命中：** 架构清晰（**最强命中**，模块切分是这组里最规范的）、近期活跃 2026-04（√）、完整 MQTT+设备+规则+UI 栈（√）、Apache-2.0 商用友好（√）。
**Trade-off：** **违反你的"代码量要能读完"硬约束**——所以列在第 4 位，作为"想看清企业级架构长什么样"的参考。**如果你目标是上手用 → [[kerwincui__FastBee]]；想学架构 → JetLinks 看目录树就行，不必通读**。

---
*由 /gitout 生成 · 2026-05-23 · intent: "搜索物联网平台，轻量，容易修改，架构清晰，近期项目"*
