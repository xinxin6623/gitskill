---
type: repo
repo: aaPanel/aaPanel
domain: server-ops
status: active
discovered: 2026-05-23
last_reviewed: 2026-05-23
intent_matched: "单机/VPS 用的开源中文 Web 面板"
signals:
  stars: 2972
  last_commit: 2026-05-18
  language: JavaScript
  license: ""
url: https://github.com/aaPanel/aaPanel
absorption:
  harvested: false
  used: false
  used_in: []
---

# aaPanel · 小白说明书

## 🧐 这是什么
宝塔面板的国际版分支，同一套底层、英文优先 UI、走出海路线。中文叫"堡塔面板国际版"，老用户对 LNMP/LAMP 一键栈最熟。

## 💡 解决什么问题
- 你之前用过宝塔，对操作流程有肌肉记忆，但想要无强制账号绑定的版本
- 你需要"装个 PHP 网站环境"，aaPanel 这条路是阻力最小的
- 你内存只有 512M（VPS 低配），需要一个号称"60M 内存"就能跑的面板

## 🎯 谁该用 / 谁别用
**适合你如果：**
- 你建站需求强（WordPress / Discuz / Typecho / PHP 项目）
- 你需要超低内存占用（号称面板本体 60M）
- 你想要传统 LNMP 那套体验

**别浪费时间如果：**
- 你想要现代化 UI 和容器化思路（aaPanel UI 比较"古典"）
- 你介意 GitHub 仓库没标 LICENSE（核心代码 license 不明确）
- 你想要中文一等公民（aaPanel 是英文优先，中文版叫宝塔）

## 🚀 三分钟上手
```bash
URL=https://www.aapanel.com/script/install_6.0_en.sh && \
  curl -ksSO "$URL" && bash install_6.0_en.sh 66959f96
```
要求：Ubuntu 22+ / Debian 11+ / CentOS 9 / Rocky 8+，**必须干净系统**。

## 🔑 关键文件 / 关键概念
- 默认端口 8888（面板），22/21/80/443 业务
- `/www/wwwroot` — 网站根目录
- `/www/server/data` — MySQL 数据目录
- 配套 Docker 镜像 `aapanel/aapanel:lib`

## ⚠️ 踩坑提示
- 干净系统硬要求 — 装过 Apache/Nginx/MySQL 会拒绝
- GitHub 仓库本质是"宣传 + Docker 镜像"，主代码托管在自家，开源程度不如 1Panel/AcePanel
- 默认账号 `aapanel/aapanel123`，**装完立刻改**
- 中文版（宝塔）和国际版（aaPanel）有功能差异，文档别混看

## 🤔 为什么这次推它给你
**命中：** 单机场景（√）、轻量（√，强命中超低内存）、有中文社区（间接，通过宝塔生态）。
**Trade-off：** "开源自托管"命中度打折——仓库本身不是完整源码、license 缺失。但你勾了"轻量优先"，这条 60M 内存占用是榜单里最低的，适合你只有 1GB 内存 VPS 的场景。介意 license 就用 [[1Panel-dev__1Panel]]（GPL-3）或 [[acepanel__panel]]（BSD-3）。

---
*由 /gitout 生成 · 2026-05-23 · intent: "服务器搭建管理维护的项目"*
