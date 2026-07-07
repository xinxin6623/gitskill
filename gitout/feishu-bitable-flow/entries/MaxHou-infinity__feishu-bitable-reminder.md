---
type: repo
repo: MaxHou-infinity/feishu-bitable-reminder
domain: feishu-bitable-flow
status: active
discovered: 2026-07-07
last_reviewed: 2026-07-07
intent_matched: "飞书 CLI + 多维表格自建业务流"
signals:
  stars: 1
  last_commit: 2026-06-17
  language: Shell
  license: MIT
  url: https://github.com/MaxHou-infinity/feishu-bitable-reminder
absorption:
  harvested: false
  used: false
  used_in: []
---

# feishu-bitable-reminder · 小白说明书

## 🧐 这是什么

飞书多维表格「自动催办官」——扫一遍多维表里的负责人 + DDL 缺口,3 分钟生成带记录编号的提醒消息,经人工确认后由 lark-cli 发到个人或群聊。

## 💡 解决什么问题

- L1 目标表/招聘看板/入职进度表里,谁还没填 DDL 全靠人工翻
- 催办消息写起来重复,语气难统一,容易漏人
- 批量催办发错人发错群,社死

## 🎯 谁该用 / 谁别用

**适合你如果：**
- 用飞书多维表格做目标/招聘/入职进度追踪
- 已装 lark-cli 且机器人入群
- 想要场景化催办模板 + 安全的草稿确认流程

**别浪费时间如果：**
- 没有飞书多维表格(本 skill 只读多维表 + 发消息,核心依赖它)
- 想自动发送不发草稿(安全边界强制人工确认)
- 团队超 10 人需批量催办(超 10 个目标强制先列名单确认)

## 📜 协议风险

- **License：** MIT
- **商用 / 魔改 / 闭源：** ✅ 无风险
- **对外提供 SaaS / 给客户部署：** ✅ 无传染义务

## 🚀 三分钟上手

```bash
# 一键环境验证
bash ~/.hermes/skills/productivity/feishu-bitable-reminder/scripts/check-lark-cli-ready.sh
# 首次配置团队联系人
cp references/team-contacts.yaml.example references/team-contacts.yaml
# 编辑填入真实 open_id 和 app_token
# 对话中说:"扫一遍 L1 目标表 tblqQqYDTzDL1Eho,告诉我谁还没填"
```

## 🔑 关键文件 / 关键概念

- `SKILL.md` — Agent 加载的完整规范
- `scripts/check-lark-cli-ready.sh` — 6 步环境验证
- `references/reminder-templates.md` — 3 套催办话术模板(A/B/C 自动选)
- `references/pitfalls-cheatsheet.md` — 17 条 lark-cli 坑点速查
- `references/team-contacts.yaml` — 真人 open_id 档案(gitignored)
- **安全边界** — 不自动发送/不修改记录/不跨表引用/超 10 人强制确认

## ⚠️ 踩坑提示

- `+record-list` 必须 `--format json`,否则拿到 markdown 无法解析
- `+record-create` 不存在,用 `+record-upsert`
- 新表默认字段不可删除,直接 `+field-create` 新的
- 金额敏感场景(薪酬表)走子流程 `salary-supplement-table-workflow.md`

## 🤔 为什么这次推它给你

1. **命中 intent.what：** lark-cli + 多维表格自建业务流(催办),端到端"看到缺口→自动催办"场景化
2. **命中 soft pref：** 中文 README、17 条坑点速查、3 套模板、8 条测试样例、安全边界清晰
3. **没命中的 trade-off：** stars 低(1 颗)、场景单一(只做催办)、依赖 Hermes skill 目录结构

---
*由 /gitout 生成 · 2026-07-07 · intent: "飞书 cli+多维表格 自建业务流 近3个月活跃"*
