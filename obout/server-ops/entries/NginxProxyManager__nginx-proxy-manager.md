---
type: repo
repo: NginxProxyManager/nginx-proxy-manager
domain: server-ops
status: active
discovered: 2026-05-26
last_reviewed: 2026-05-26
intent_matched: "多站点反向代理 + 自动 SSL 管理界面"
signals:
  stars: 32935
  last_commit: 2026-05-26
  language: TypeScript
  license: MIT
url: https://github.com/NginxProxyManager/nginx-proxy-manager
absorption:
  harvested: false
  used: false
  used_in: []
---

# Nginx Proxy Manager · 小白说明书

## 🧐 这是什么
给 Nginx 反向代理套了个"傻瓜式 Web UI"——你在网页上填个域名、选个目标端口，它帮你生成 Nginx 配置 + 自动申请 Let's Encrypt 证书。不是 PaaS，只管"流量怎么转发"这一层。

## 💡 解决什么问题
- 你在一台 VPS 上手动跑了几个 Docker 容器（博客在 3000 端口、API 在 8080 端口），需要按域名分流
- 你不想手写 Nginx 配置和 certbot 命令
- 你想要一个清晰的界面看到所有域名 → 服务的映射关系

## 🎯 谁该用 / 谁别用
**适合你如果：**
- 你已经会用 Docker 部署应用，只需要"最后一公里"的反代 + SSL
- 你想要最简单的方案——NPM 只做一件事：转发流量
- 你不介意偶尔从浏览器操作

**别浪费时间如果：**
- 你想要完整的部署/构建/CI 流程（那是 PaaS 该做的事）
- 你想 100% 用 CLI 操作（NPM 基本只有 Web UI，没有官方 CLI/API）
- 你想把部署操作完全交给 Claude Code 自动化

## 🚀 三分钟上手
```yaml
# docker-compose.yml
services:
  npm:
    image: jc21/nginx-proxy-manager:latest
    restart: unless-stopped
    ports:
      - '80:80'
      - '81:81'    # 管理界面
      - '443:443'
    volumes:
      - ./data:/data
      - ./letsencrypt:/etc/letsencrypt
```
```bash
docker compose up -d
# 访问 http://your-vps:81
# 默认账号：admin@example.com / changeme
```

## 🔑 关键文件 / 关键概念
- Proxy Host — 一条"域名 → 内部地址:端口"的转发规则
- SSL Certificate — 自动申请 Let's Encrypt，也支持导入自有证书
- Access List — 给特定路径加 Basic Auth 保护
- Stream — TCP/UDP 端口转发（非 HTTP 流量）

## ⚠️ 踩坑提示
- 纯 GUI 操作，**没有官方 CLI/API**——Claude Code 无法直接管理（这是最大短板）
- 社区有第三方 API wrapper（Erreur32/nginx-proxy-manager-Bash-API）但非官方
- 和 PaaS 工具互斥——如果你用了 Coolify/Dokploy（它们自带 Traefik），不需要再装 NPM

## 🤔 为什么这次推它给你
**Claude Code 友好度：低。** 这是唯一一个基本不适合 Claude Code 操作的入选项。推它的原因是：如果你选择"自己用 Docker Compose 管理容器 + 只需要一个反代层"的轻量路线，NPM 是这个细分领域最主流的工具（33k stars），学习成本极低。但如果 Claude Code 自动化是硬需求，建议用 Dokku/Dokploy 的内置路由代替它。

---
*由 /gitout 生成 · 2026-05-26 · intent: "一台 VPS 部署多个小网站，适合 Claude Code 操作"*
