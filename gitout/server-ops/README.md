# server-ops · 服务器搭建/管理/维护

## 健康度
- entries: 10 / 30
- last_updated: 2026-05-26
- focus: Web 控制面板 + 轻量 PaaS + 反向代理（单机/VPS 场景）

## 当前条目

### 🖥️ VPS 管理面板
| Repo | 一句话 | Stars |
|------|--------|-------|
| [acepanel/panel](entries/acepanel__panel.md) | Go 单文件、低侵入、中文优先（耗子面板继任者） | 2.7k |
| [1Panel-dev/1Panel](entries/1Panel-dev__1Panel.md) | 国产现代化 VPS 面板，应用商店 + Docker 一体化 | 35k |
| [IceWhaleTech/CasaOS](entries/IceWhaleTech__CasaOS.md) | 家用"个人云"面板，NAS / 小主机最佳搭档 | 33k |
| [aaPanel/aaPanel](entries/aaPanel__aaPanel.md) | 宝塔国际版，超低内存占用、PHP 建站老熟人 | 2.9k |
| [webmin/webmin](entries/webmin__webmin.md) | 28 年祖师爷，传统 Linux 服务（DNS/邮件）管理 | 5.7k |

### 🚀 轻量 PaaS / 多站部署（适合 Claude Code 操作）
| Repo | 一句话 | Stars | CC 友好度 |
|------|--------|-------|-----------|
| [dokku/dokku](entries/dokku__dokku.md) | 100% CLI 的 mini-Heroku，git push 就部署 | 32k | 极高 |
| [Dokploy/dokploy](entries/Dokploy__dokploy.md) | 现代 PaaS，CLI + API + Traefik 自动路由 | 34k | 高 |
| [coollabsio/coolify](entries/coollabsio__coolify.md) | 最火自托管 PaaS，280+ 一键模板 | 56k | 中高 |
| [caprover/caprover](entries/caprover__caprover.md) | Docker+Nginx PaaS，600+ 一键应用 | 15k | 中 |
| [NginxProxyManager/nginx-proxy-manager](entries/NginxProxyManager__nginx-proxy-manager.md) | 最流行的反代 GUI，自动 SSL | 33k | 低 |

## 选型建议（快速决策）

### 面板类
- 不知道选啥 → **1Panel**
- 要极致轻量 + 中文 → **AcePanel**
- 家用 NAS / 小主机 → **CasaOS**
- 1GB VPS 建 PHP 站 → **aaPanel**
- 要管邮件/DNS 等传统服务 → **Webmin**

### 多站部署类（一台 VPS 跑 2-3 个小站）
- 100% Claude Code 操作、最轻量 → **Dokku**
- 想要 Web UI + CLI 两手抓、Docker Compose 原生 → **Dokploy**
- 功能最全、不差内存 → **Coolify**
- 想要应用商店式体验 → **CapRover**
- 只需要反代层、自己管 Docker → **Nginx Proxy Manager**（但不适合 Claude Code）
