---
type: repo
repo: kerwincui/FastBee
domain: iot-platform
status: active
discovered: 2026-05-23
last_reviewed: 2026-05-23
intent_matched: "轻量易改的完整 IoT 平台（含 MQTT+设备+规则+UI+App）"
signals:
  stars: 2173
  last_commit: 2026-04-16
  language: Java
  license: AGPL-3.0
url: https://github.com/kerwincui/FastBee
absorption:
  harvested: false
  used: false
  used_in: []
---

# FastBee · 小白说明书

## 🧐 这是什么
国内开发者做的"轻量级全栈"开源物联网平台。基于若依（RuoYi）权限框架扩展，**Spring Boot 内置 Netty MQTT Broker**（不用单独装 EMQX），前端 Vue + ElementUI，移动端 uniapp（小程序/Android/iOS/H5 一套出），硬件 SDK 包括 ESP32/ESP8266/树莓派。是国内 IoT 平台里**"小而全"代表作**。

## 💡 解决什么问题
- 你想要"MQTT+设备+规则+UI+App"全套但又不想拼一堆中间件（EMQX+InfluxDB+Grafana+前后端各搞一摊）
- 你在做毕设/中小型项目，需要一个能改、能跑、能演示的现成底子
- 你需要现成的手机端（小程序 + App），不想从零搭

## 🎯 谁该用 / 谁别用
**适合你如果：**
- 你的项目要覆盖：设备接入、物模型、规则脚本、用户权限、视频接入、APP
- 你接受 Java/Spring Boot 技术栈
- 你需要中文文档 + 国内硬件生态（合宙/ESP-IDF/Arduino 示例齐）

**别浪费时间如果：**
- 你拒绝 Java（这就是 Java 全家桶）
- 你做商业项目（AGPL-3 + 商业版要授权，开源版仅个人学习）
- 你只需要 MQTT broker（用 Mosquitto/NanoMQ 即可）

## 🚀 三分钟上手
```bash
sudo wget -c https://hub.fastbee.cn/resource/install.sh && bash ./install.sh
```
脚本里选"开源版本"。默认账号 `admin/admin123`。

## 🔑 关键文件 / 关键概念
- `spring-boot/` — 后端源码（含 Netty MQTT Broker）
- `vue/` — Web 控制台
- 移动端、SDK 分别在外部 gitee 仓库（fastbee-app / fastbee-sdk）
- 时序数据库支持 TDengine / IoTDB / InfluxDB
- 物模型 = 属性 + 功能 + 事件三件套（行业标准范式）

## ⚠️ 踩坑提示
- **AGPL-3.0** —— 商用必须开源衍生品，否则要买商业版
- 移动端代码不在主仓库，要跨仓库克隆（gitee）
- 开源版"暂仅支持 MQTT 协议"，TCP/CoAP 在商业版
- 文档大部分在 `fastbee.cn/doc/` 而非 GitHub

## 🤔 为什么这次推它给你
**命中：** 完整 MQTT+设备+规则+UI+App（强命中你列的"基础功能需要"）、中文（√）、近期活跃 2026-04（√）、架构按"服务端/Web/移动端/硬件 SDK"四块切分，**模块边界清晰、可读**（√）。
**Trade-off：** 比 [[seslabSJU__tinyIoT]] 重，比 [[jetlinks__jetlinks-community]] 轻——是"代码能读完"和"功能完整度"的黄金折中。AGPL 协议是最大限制，介意的话看 [[IoTSharp__IoTSharp]]（Apache-2.0）。

---
*由 /gitout 生成 · 2026-05-23 · intent: "搜索物联网平台，轻量，容易修改，架构清晰，近期项目"*
