---
type: repo
repo: IceWhaleTech/CasaOS
domain: server-ops
status: active
discovered: 2026-05-23
last_reviewed: 2026-05-23
intent_matched: "单机/家用主机的轻量 Web 面板"
signals:
  stars: 33871
  last_commit: 2025-08-06
  language: Go
  license: Apache-2.0
url: https://github.com/IceWhaleTech/CasaOS
absorption:
  harvested: false
  used: false
  used_in: []
---

# CasaOS · 小白说明书

## 🧐 这是什么
冰山科技（IceWhale，ZimaBoard/ZimaBlade 的厂商）做的"个人云"系统，定位介于"服务器面板"和"NAS 操作系统"之间。UI 走家用美学路线——大图标、卡片式应用，像 iPad。

## 💡 解决什么问题
- 你有一台 J4125 / N100 小主机 / 树莓派 / 旧笔记本，想做家庭 NAS + 自托管中心
- 你不喜欢 1Panel 那种"运维感"很重的界面，想要更"消费级"的体验
- 你想给家人/不懂技术的人也能用的家庭服务器入口

## 🎯 谁该用 / 谁别用
**适合你如果：**
- 你的场景偏家用/NAS（媒体库、文件分享、家庭自动化）
- 你看重 UI 美观度 > 运维专业度
- 你打算装在 ZimaBoard / 小主机 / 玩客云上

**别浪费时间如果：**
- 你的核心需求是建站（Nginx/SSL/MySQL 管理）—— CasaOS 这方面薄
- 你需要精细的 cron、防火墙、用户权限管理
- 你跑生产业务（CasaOS 定位是"个人云"不是"生产面板"）

## 🚀 三分钟上手
```bash
curl -fsSL https://get.casaos.io | sudo bash
```
默认监听 80 端口，浏览器打开 `http://<server-ip>` 即可。

## 🔑 关键文件 / 关键概念
- 应用商店（含第三方仓库：BigBear、LinuxServer 等数百个 Docker app）
- Files App — 类 Finder 的网页文件管理器，可挂 SMB / NFS
- 走 Docker Compose 跑应用，没有侵入式系统改动

## ⚠️ 踩坑提示
- 主仓库 2025-08 后更新放缓（生态 repo 仍活跃），关注节奏放心使用但别期待激进新功能
- UI 是中文的，但部分应用商店内的 app 描述是英文
- 想要"网站托管面板"那种深度功能，CasaOS 不是答案

## 🤔 为什么这次推它给你
**命中：** 单机场景（√，强命中家用）、轻量（√）、自托管（√）、依赖少（√，纯 Docker）。
**Trade-off：** 中文文档不如 1Panel/AcePanel 全。"建站运维"维度它弱，但如果你的"服务器"其实是家里那台小主机，CasaOS 比 [[1Panel-dev__1Panel]] 用起来更舒服——它不假装自己是数据中心。

---
*由 /gitout 生成 · 2026-05-23 · intent: "服务器搭建管理维护的项目"*
