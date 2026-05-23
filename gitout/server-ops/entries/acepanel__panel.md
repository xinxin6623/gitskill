---
type: repo
repo: acepanel/panel
domain: server-ops
status: active
discovered: 2026-05-23
last_reviewed: 2026-05-23
intent_matched: "单机/VPS 用的轻量中文 Web 面板"
signals:
  stars: 2776
  last_commit: 2026-05-22
  language: Go
  license: BSD-3-Clause
url: https://github.com/acepanel/panel
absorption:
  harvested: false
  used: false
  used_in: []
---

# AcePanel · 小白说明书

## 🧐 这是什么
原"耗子面板"升级品牌后的开源 Linux 服务器管理面板，Go 写的单文件二进制，主打"装上能跑、卸了无痕"。中国独立开发者作品，文档默认中文。

## 💡 解决什么问题
- 你买了台 VPS，想装 Nginx + MySQL + PHP + Let's Encrypt 但不想背一堆 `apt install` 和配置文件路径
- 你试过宝塔但讨厌它强绑账号、强制弹广告、闭源核心
- 你想要一个"我哪天不爽了能直接 kill 掉、原生服务照常跑"的面板

## 🎯 谁该用 / 谁别用
**适合你如果：**
- 你想要中文界面 + 国内开发者维护节奏
- 你跑 1-2 台 VPS / 家用 ARM 主机（amd64/arm64 都支持）
- 你介意系统被面板"侵入式改造"

**别浪费时间如果：**
- 你要管 10+ 台服务器（用 Ansible 更对路）
- 你需要 Docker 容器可视化一站式（这块 1Panel 更强）
- 你装在已有生产环境上（要求干净系统）

## 🚀 三分钟上手
```bash
bash <(curl -sSLm 10 https://dl.acepanel.net/helper.sh)
```

## 🔑 关键文件 / 关键概念
- 单文件二进制 — 卸载只需停进程删目录，不留垃圾
- 离线模式 — 装完可以把面板进程关掉，已部署的网站照常跑
- 兼容架构：`amd64` / `arm64`

## ⚠️ 踩坑提示
- 仅支持干净系统，已装过 Apache/Nginx/MySQL 会冲突
- 2.x（耗子面板）升级到 3.0（AcePanel）需走迁移流程，老用户注意
- 商业赞助多为国内云服务商，文档外链偶尔会带推广

## 🤔 为什么这次推它给你
**命中：** 单机场景（√）、中文优先（√）、轻量（Go 单文件，强命中）、依赖少（√）、开源自托管（BSD-3）。
**Trade-off：** 比 1Panel 小众（2.7k vs 35k stars），生态没那么繁荣；但你说"无硬约束看推荐"+"轻量优先"，这条比 1Panel 更纯粹地命中你的偏好——1Panel 现在主推 AI agent，反而背离"轻量"。

---
*由 /gitout 生成 · 2026-05-23 · intent: "服务器搭建管理维护的项目"*
