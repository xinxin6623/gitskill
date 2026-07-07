---
type: repo
repo: peachgreenti/lark-cli-skill-auto-quotation
domain: feishu-bitable-flow
status: active
discovered: 2026-07-07
last_reviewed: 2026-07-07
intent_matched: "飞书 CLI + 多维表格自建业务流"
signals:
  stars: 11
  last_commit: 2026-04-19
  language: Python
  license: MIT
  url: https://github.com/peachgreenti/lark-cli-skill-auto-quotation
absorption:
  harvested: false
  used: false
  used_in: []
---

# lark-cli-skill-auto-quotation · 小白说明书

## 🧐 这是什么

一个基于 `lark-cli` + 飞书多维表格 + AI 的**外贸询价全自动处理系统**。监听邮箱 → AI 提取报价需求 → 写入多维表格触发报价流程 → 生成云文档报价单 → 人工群内确认 → 自动回复客户邮件。

## 💡 解决什么问题

- 外贸询价邮件散落在邮箱,人工逐封拆解 PDF 附件、手抄产品型号到报价表,一个询盘折腾半小时
- 报价单生成、邮件回复分属不同工具,来回切换丢上下文
- 团队多人协作时,谁在处理哪条询盘全靠口头同步

## 🎯 谁该用 / 谁别用

**适合你如果：**
- 外贸/跨境团队,每天收到中英文询价邮件
- 已用飞书多维表格做报价管理,想接自动化
- 装了 lark-cli 且机器人已入群

**别浪费时间如果：**
- 不做外贸(B2B 询价场景),业务模型对不上
- 没有飞书企业版或多维表格 AI 字段捷径(核心流程依赖它)
- 想找通用邮件自动化,n8n/Make 更合适

## 📜 协议风险

- **License：** MIT
- **商用 / 魔改 / 闭源：** ✅ 无风险
- **对外提供 SaaS / 给客户部署：** ✅ 无传染义务

## 🚀 三分钟上手

```bash
git clone https://github.com/peachgreenti/lark-cli-skill-auto-quotation.git
cd lark-cli-skill-auto-quotation
pip install -r requirements.txt
cp .env.example .env       # 填 IMAP/SMTP/AI Key
cp config.yaml.example config.yaml  # 填多维表格 app_token/table_id
python3 main.py            # 监听模式
python3 main.py --test 20260419090  # 跳过邮件,直接测单条
```

## 🔑 关键文件 / 关键概念

- `main.py` — 主入口,IMAP 监听循环 + 10 步流程编排
- `base_writer.py` — 飞书多维表格操作(创建记录/上传附件/轮询报价结果)
- `quotation_generator.py` — 报价单云文档 + PDF 生成
- `config.yaml` — 三张表(询盘需求/报价明细/客户管理)的 table_id 与字段 ID 映射
- **AI 字段捷径** — 多维表格内配的 AI 自动从询盘需求生成报价明细,是流程关键节点

## ⚠️ 踩坑提示

- 首次启动会**跳过所有历史未读邮件**,只处理启动后新到的——别拿旧邮件测试,用 `--test` 跳过
- 多维表格必须**先配 AI 字段捷径**,否则报价明细不会自动生成
- 真实发件人优先取 `X-Sender`/`Return-Path` 头,直接 reply 可能被 SPF 挡

## 🤔 为什么这次推它给你

1. **命中 intent.what：** 典型的"飞书 CLI + 多维表格自建业务流",lark-cli 串起邮件→多维表格→云文档→群通知→邮件回复全链路
2. **命中 soft pref：** 中文 README、具体业务流(外贸报价)而非纯 API 包装,代码结构清晰按流程步骤分文件
3. **没命中的 trade-off：** 场景垂直(只做外贸询价),不是通用业务流框架,想改造成其他业务需重写流程编排

---
*由 /gitout 生成 · 2026-07-07 · intent: "飞书 cli+多维表格 自建业务流 近3个月活跃"*
