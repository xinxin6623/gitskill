---
type: repo
repo: seslabSJU/tinyIoT
domain: iot-platform
status: active
discovered: 2026-05-23
last_reviewed: 2026-05-23
intent_matched: "极致轻量、架构清晰的 IoT 平台（学习用）"
signals:
  stars: 9
  last_commit: 2026-05-12
  language: C
  license: BSD-3-Clause
url: https://github.com/seslabSJU/tinyIoT
absorption:
  harvested: false
  used: false
  used_in: []
---

# tinyIoT · 小白说明书

## 🧐 这是什么
韩国世宗大学 SES Lab 出的 **oneM2M 标准轻量 IoT 服务层平台**，纯 C 写的 CSE（Common Services Entity）。整个项目用 `config.h` 一个头文件配置全局，依赖是 SQLite/PostgreSQL + cJSON + pico HTTP + wolfMQTT。配套 Vue dashboard。这是这一组里**唯一真正"代码量能完整读完"的**项目。

## 💡 解决什么问题
- 你想看清"一个 IoT 平台的核心抽象（设备/资源/订阅/权限）到底是什么"——它把 oneM2M 一比一实现给你看
- 你在做嵌入式 IoT 网关/边缘端，需要一个能塞进 ARM Linux 小盒子的 CSE 实现
- 你要学习/研究 oneM2M 标准（学术场景）

## 🎯 谁该用 / 谁别用
**适合你如果：**
- 你愿意接受小众标准（oneM2M）的概念入门成本
- 你想读"几千行 C 代码就跑起来一个 IoT 服务层"的实现
- 你做边缘网关、嵌入式 IoT 研究项目

**别浪费时间如果：**
- 你要"开箱即用"的产品级平台（这是研究项目，不是 [[kerwincui__FastBee]]）
- 你不想学 oneM2M 那套 cseBase/AE/CNT/CIN/SUB 资源模型
- 你需要手机 App / 现成应用商店

## 🚀 三分钟上手
```bash
git clone --recursive https://github.com/seslabSJU/tinyIoT.git
cd tinyIoT/source/server
# 编辑 config.h 设置 IP/Port，启用 ENABLE_MQTT
make
./server
```
默认 `127.0.0.1:3000`。

## 🔑 关键文件 / 关键概念
- `source/server/config.h` — 全局配置入口（IP/端口/协议/数据库），改这一个文件能配整套
- `source/server/` — CSE 主体实现
- oneM2M 核心资源：cseBase / ACP（访问控制）/ AE（应用实体）/ CNT（容器）/ CIN（内容实例）/ SUB（订阅）
- IN-CSE / MN-CSE — 基础架构节点 vs 中间节点，分别对应"云平台"和"边缘网关"

## ⚠️ 踩坑提示
- 学术研究项目，stars 才 9，社区小到几乎没有（出问题只能自己读代码）
- 协议绑定目前只有 HTTP + MQTT，**CoAP/Websocket 还在 TODO**
- Announcement（资源公告）目前只支持单向
- README 拼写错误若干（"Portabilit"），不影响代码质量

## 🤔 为什么这次推它给你
**命中：** 轻量（强命中，纯 C + 几个小型依赖）、架构清晰（强命中，单 config.h 配置 + 资源模型边界极清）、近期活跃 2026-05（√）、代码量能读完（**最强命中**，是这组里唯一真正几千行级别的）。
**Trade-off：** 功能完备性最低——你说"前端管理 UI、手机端等基础功能需要"，tinyIoT 只有 Vue dashboard 没有手机端，规则引擎也是 oneM2M 的订阅/通知范式而非"if-then-else 编辑器"。**这条不是给你直接用的，是给你"想搞懂一个 IoT 平台到底由什么构成"的最佳教材**。和 [[kerwincui__FastBee]] 配对食用：FastBee 看产品形态，tinyIoT 看底层抽象。

---
*由 /gitout 生成 · 2026-05-23 · intent: "搜索物联网平台，轻量，容易修改，架构清晰，近期项目"*
