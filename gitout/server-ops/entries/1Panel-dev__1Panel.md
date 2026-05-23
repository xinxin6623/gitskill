---
type: repo
repo: 1Panel-dev/1Panel
domain: server-ops
status: active
discovered: 2026-05-23
last_reviewed: 2026-05-23
intent_matched: "单机/VPS 用的开源中文 Web 面板"
signals:
  stars: 35545
  last_commit: 2026-05-22
  language: Go
  license: GPL-3.0
url: https://github.com/1Panel-dev/1Panel
absorption:
  harvested: false
  used: false
  used_in: []
---

# 1Panel · 小白说明书

## 🧐 这是什么
FIT2CLOUD（飞致云）出品的现代化 VPS 控制面板，Go 写、Web UI、165+ 应用商店一键装，是国内开源面板里目前最有名、生态最大、迭代最快的那个。已经做到 35k stars。

## 💡 解决什么问题
- 你想要"装 Nextcloud / Bitwarden / Umami 这种自托管应用，但不想自己写 docker-compose"
- 你想管理 Docker 容器但讨厌 Portainer 的英文界面和割裂体验
- 你想要"网站 + SSL + 反代 + 备份到 S3"开箱即用的国产宝塔替代

## 🎯 谁该用 / 谁别用
**适合你如果：**
- 你要在 VPS 上跑多个自托管应用 + 网站
- 你看重应用商店生态（165+ 一键装）
- 你想要中文社区支持 + 高频更新

**别浪费时间如果：**
- 你要纯粹的"轻量、不入侵系统"（1Panel 装得比较厚）
- 你拒绝 GPL（介意的话就用 BSD 系的 AcePanel）
- 你不需要 AI agent、应用商店这些花活儿，只想要 LNMP 基础栈

## 🚀 三分钟上手
```bash
bash -c "$(curl -sSL https://resource.1panel.pro/v2/quick_start.sh)"
```
要求：Linux VPS（Debian/Ubuntu/CentOS/Rocky），1GB RAM 起。

## 🔑 关键文件 / 关键概念
- App Store — 内置应用市场，开箱装 Nextcloud / Bitwarden / NocoBase 等
- 1pctl — 命令行工具，找回密码用 `1pctl user-info`
- OSS 免费，Pro 版从 $80/年（含多节点、WAF、防篡改），日常单机用 OSS 够了

## ⚠️ 踩坑提示
- 安装路径 `/opt/1panel`，比 AcePanel "重"得多
- Pro 功能引导比较多，介意的话别点
- AI agent 是新加的卖点，纯做服务器管理可以无视

## 🤔 为什么这次推它给你
**命中：** 单机场景（√）、中文优先（√，国产）、开源自托管（√，GPL-3）、生态成熟（强命中）。
**Trade-off：** 不算"极致轻量"——它什么都想做（网站、容器、AI、应用商店），所以装得厚。但你勾了"无硬约束看推荐"，1Panel 是这个赛道最稳的"工具齐全+中文好+持续维护"的选项，是你不知道选什么时的默认答案。如果你强调极简，就看 [[acepanel__panel]]。

---
*由 /gitout 生成 · 2026-05-23 · intent: "服务器搭建管理维护的项目"*
