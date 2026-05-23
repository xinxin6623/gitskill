---
type: repo
repo: LC044/WeChatMsg
domain: misc
status: active
decision: harvest
discovered: 2026-05-22
last_reviewed: 2026-05-22
theme: im-export
intent_matched: "中文场景微信聊天记录导出与年度报告生成"
signals:
  stars: 41464
  last_commit: 2026-05-22
  language: unknown
  license: unknown
url: https://github.com/LC044/WeChatMsg
absorption:
  harvested: false
  used: false
  used_in: []
---

# WeChatMsg (留痕) · 小白说明书

## 🧐 这是什么

**中文圈微信导出之王，41k 星**。把你 PC 微信里的所有聊天记录解密、提取，导出成 HTML / Word / Excel / 文本，还能生成"年度聊天报告"（跟谁聊得最多、什么时段、用什么词）。作者 LC044 写了一段相当有情怀的前言——核心信念是"**我的数据我做主**"，未来 AI 应该用你自己的数据养成你的专属 AI。

注意作者声明项目"很久没（也不会）更新了"，未来可能转方向。

## 💡 解决什么问题

微信占据你最多沟通的时间，但官方完全锁死：

- 没法导出
- 换手机就丢
- 想用聊天记录训练个人 AI 没数据源

WeChatMsg 给你**一键解密 + 解析 + 导出**完整链路。年度报告功能是 viral 卖点（每年春节朋友圈都有人晒）。

## 🎯 谁该用 / 谁别用

**适合你如果：**
- 你在做 weixinjilu，这就是直接同道（值得直接对比设计）
- 想做"个人 AI 训练数据"前置数据采集
- Windows PC 微信用户

**别浪费时间如果：**
- 只用 Mac 微信（支持有限）
- 法律 / 隐私顾虑强（数据全在本地但部分微信版本要绕过加密）
- 要长期维护版本（作者明示不更新了）

## 🚀 三分钟上手

```bash
# 见 https://memotrace.cn/ 下载发布版（有 GUI）

# 或源码
git clone https://github.com/LC044/WeChatMsg.git
cd WeChatMsg
pip install -r requirements.txt
python main.py
```

需要 PC 微信已登录且未退出。

## 🔑 关键文件 / 关键概念

- **留痕** — 项目正式名，意为"留下痕迹"
- **数据库解密** — 微信本地 SQLite 加密，工具拿到密钥后解
- **年度报告生成** — viral 功能，把数据可视化
- **TrailSnap** — 作者后续在做的 AI 相册项目，思路一脉相承

## ⚠️ 踩坑提示

- 微信版本更新经常打破解密路径
- **作者已明示停更**，未来选别的项目跟进或自己 fork
- 隐私敏感，导出文件别上传云

## 🤔 为什么这次推它给你

**weixinjilu 的直接竞品 / 参考**。你做"微信聊天记录导出"这个赛道，LC044/WeChatMsg 已经把社区资源拿走了，但**它已经停更**——这是你的机会窗口。**重点抄它的：年度报告生成（viral 卖点）、HTML 导出 layout、多格式同时输出**。但避免重复造 PC 解密轮子，可以做差异化（如 Mac 支持、Docker 部署，weixinjilu 已经领先）。

---
*由 /gitout 生成 · 2026-05-22 · theme: 聊天记录 / 个人数据遗产化*
