---
type: repo
repo: cragiclin-cmyk/lark-jobpilot-skill
domain: feishu-bitable-flow
status: active
discovered: 2026-07-07
last_reviewed: 2026-07-07
intent_matched: "飞书 CLI + 多维表格自建业务流"
signals:
  stars: 9
  last_commit: 2026-04-19
  language: JavaScript
  license: MIT
  url: https://github.com/cragiclin-cmyk/lark-jobpilot-skill
absorption:
  harvested: false
  used: false
  used_in: []
---

# lark-jobpilot-skill · 小白说明书

## 🧐 这是什么

Chrome 插件 + Node.js CLI 组合,从招聘网站(Boss 直聘等)一键提取 JD,经 Coze AI 工作流解析岗位要求与能力模型,自动写入飞书多维表格,建立个人求职 CRM。

## 💡 解决什么问题

- 投递太多岗位,记不清哪家公司什么职位,信息散在各招聘 App
- JD 太长抓不住重点,面试前不知从何准备
- 想对比不同岗位要求,没统一视图

## 🎯 谁该用 / 谁别用

**适合你如果：**
- 正在找工作,用 Boss 直聘等已适配站点
- 已装 lark-cli 且有多维表格
- 想用 AI 自动生成面试准备清单 + 简历匹配度分析

**别浪费时间如果：**
- 不求职,业务流模型对不上
- 用的是 lark-cli 不支持的招聘站(未适配网站只能手动划选文本)
- 不想配 Coze 平台账号(AI 解析强依赖它)

## 📜 协议风险

- **License：** MIT(README 声明)
- **商用 / 魔改 / 闭源：** ✅ 无风险
- **对外提供 SaaS / 给客户部署：** ✅ 无传染义务

## 🚀 三分钟上手

```bash
git clone https://github.com/cragiclin-cmyk/lark-jobpilot-skill.git
cd lark-jobpilot-skill
npm install && npm run build
node dist/coze-parser.js --init        # 初始化 ~/.jobpilot/config.json
# 填 Coze API Token + Workflow ID
# Chrome 加载 chrome-extension 文件夹
node dist/coze-parser.js "岗位描述..." --save --create-base  # 解析并自动建表
```

## 🔑 关键文件 / 关键概念

- `chrome-extension/` — 浏览器插件,自动/手动提取 JD 文本到剪贴板
- `dist/coze-parser.js` — CLI 入口,JD 解析 + 多维表格写入
- `~/.jobpilot/config.json` — Coze Token + Workflow ID + 飞书配置(不入 Git)
- **Coze Workflow** — AI 解析后端,返回结构化能力雷达图 + 备考清单 + 匹配度

## ⚠️ 踩坑提示

- `lark-cli auth login` 必须先跑,否则写入多维表格会 401
- Coze Workflow ID 要自己在 Coze 平台建工作流,不是开箱即用
- 已有表格用 `--base-token <Token> --table-id <TableID>`,首次用 `--create-base` 自动建

## 🤔 为什么这次推它给你

1. **命中 intent.what：** lark-cli + 飞书多维表格自建业务流(求职 CRM),Chrome 插件 + CLI + AI 三段式完整业务流
2. **命中 soft pref：** 中文 README、详细 FAQ、多维度字段说明表、配置文件安全提示
3. **没命中的 trade-off：** AI 解析强绑 Coze 平台(非 OpenAI/DeepSeek 通用接口),Chrome 插件只适配部分招聘站

---
*由 /gitout 生成 · 2026-07-07 · intent: "飞书 cli+多维表格 自建业务流 近3个月活跃"*
