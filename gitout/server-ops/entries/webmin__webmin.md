---
type: repo
repo: webmin/webmin
domain: server-ops
status: active
discovered: 2026-05-23
last_reviewed: 2026-05-23
intent_matched: "单机/VPS 用的开源 Web 面板（老牌备选）"
signals:
  stars: 5742
  last_commit: 2026-05-23
  language: Perl
  license: BSD-3-Clause
url: https://github.com/webmin/webmin
url: https://github.com/webmin/webmin
absorption:
  harvested: false
  used: false
  used_in: []
---

# Webmin · 小白说明书

## 🧐 这是什么
1997 年就有的"祖师爷"级 Unix/Linux Web 管理面板，Perl 写的，全球年装 100 万次。它不是来取悦你的——是给系统管理员用了 28 年的工业用品。BSD 许可证、116 个标准模块、上百个第三方模块。

## 💡 解决什么问题
- 你要管的是"传统 Linux 服务"（BIND DNS、Apache、Postfix、Sendmail、Samba、CUPS……）
- 你需要细到"改某个配置文件某一行"的权限，国产面板抽象层把你挡在外面
- 你介意被国产面板锁定，要一个"无论哪台 Linux 都能装"的瑞士军刀

## 🎯 谁该用 / 谁别用
**适合你如果：**
- 你的需求是经典 Linux 系统管理（DNS / 邮件服务器 / 用户配额 / 磁盘 RAID）
- 你能接受英文界面（中文支持有但翻译不全）
- 你看重"28 年没死、还在更新"的稳定性

**别浪费时间如果：**
- 你要的是"一键装 WordPress / Nextcloud" —— Webmin 不是这个路子
- 你想要现代 UI（默认皮肤偏老派，需要装 authentic-theme）
- 你不想看 Perl 错误（虽然你不需要改它，但 stack trace 会出现）

## 🚀 三分钟上手
```bash
# Debian / Ubuntu
curl -O https://raw.githubusercontent.com/webmin/webmin/master/webmin-setup-repo.sh
sh webmin-setup-repo.sh
apt install webmin
```
访问 `https://<server-ip>:10000`。

## 🔑 关键文件 / 关键概念
- 116 个内置模块，几乎覆盖所有传统 Linux 服务
- Virtualmin — 在 Webmin 上层的虚拟主机管理（多站点托管场景）
- Usermin — 给普通用户的子集面板
- authentic-theme — 现代化主题，强烈建议装

## ⚠️ 踩坑提示
- 默认 10000 端口，TLS 自签证书，第一次进会有证书警告
- 中文支持不完整，部分模块仍是英文
- UI 风格"工程化"，对小白不友好（这是这次推荐里最不轻量但最专业的）

## 🤔 为什么这次推它给你
**命中：** 单机场景（√）、开源自托管（√，BSD-3，老资格）、依赖少（√，Perl + 标准库即可）。
**Trade-off：** 中文优先维度严重未命中——但作为"备选答案"列出它有意义：如果你发现国产面板都太"产品化"、限制太多，或者你管的是邮件服务器、DNS 这类传统服务，Webmin 是少数还在更新且功能深度顶天的开源面板。考虑它就别考虑 [[1Panel-dev__1Panel]]，俩理念完全不同。

---
*由 /gitout 生成 · 2026-05-23 · intent: "服务器搭建管理维护的项目"*
