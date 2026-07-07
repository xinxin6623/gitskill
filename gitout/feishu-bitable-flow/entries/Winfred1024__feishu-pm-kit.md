---
type: repo
repo: Winfred1024/feishu-pm-kit
domain: feishu-bitable-flow
status: active
discovered: 2026-07-07
last_reviewed: 2026-07-07
intent_matched: "飞书 CLI + 多维表格自建业务流"
signals:
  stars: 24
  last_commit: 2026-05-25
  language: Python
  license: MIT
  url: https://github.com/Winfred1024/feishu-pm-kit
absorption:
  harvested: false
  used: false
  used_in: []
---

# feishu-pm-kit · 小白说明书

## 🧐 这是什么

把"Claude Code + lark-cli 飞书通道"产品化成的 **AI 项目经理 Agent + 项目管理系统部署套件**。一份共享引擎驱动多个团队实例,新团队加一份 config 跑一条 bootstrap 即上线。

## 💡 解决什么问题

- 想让 AI 当项目经理,但每次给不同团队配一遍飞书应用、机器人、CLAUDE.md 太重复
- 项目档案散在 markdown 里,团队看不到全局健康度
- 飞书多维表格台账和本地 markdown 源容易脱节

## 🎯 谁该用 / 谁别用

**适合你如果：**
- 多团队共用飞书,想给每个团队部署一个 AI 项目经理
- 项目档案以 markdown frontmatter 为源,想自动生成索引+健康看板+镜像到多维表格
- 用 Claude Code,接受 AI 在业务群里监听消息发日报

**别浪费时间如果：**
- 单团队轻量项目管理,飞书自带项目工具够了
- 不用 Claude Code(引擎强依赖它当 Agent 本体)
- 想要飞书原生多维表格深度双向同步(这里只单向镜像)

## 📜 协议风险

- **License：** MIT
- **商用 / 魔改 / 闭源：** ✅ 无风险
- **对外提供 SaaS / 给客户部署：** ✅ 无传染义务

## 🚀 三分钟上手

```bash
git clone https://github.com/Winfred1024/feishu-pm-kit.git
cd feishu-pm-kit
python3 -m venv .venv && ./.venv/bin/pip install -r requirements.txt
./.venv/bin/python -m pytest -q          # 22 passed
# 阶段0(手动):飞书后台建应用+授权+拉机器人进群+lark-cli config init
python3 -m engine.bootstrap --name team-alpha
cd instances/team-alpha && claude          # 启动 Claude Code 当项目经理
```

## 🔑 关键文件 / 关键概念

- `engine/bootstrap.py` — 一键部署:脚手架/拉成员/建表/渲染 CLAUDE.md
- `engine/gen_index.py` — 索引生成 + 四项治理校验(必填/公式一致性/新鲜度/命名编号)
- `engine/bitable_sync.py` — 项目台账单向同步到飞书多维表格
- `engine/feishu.py` — 飞书通道:poll/send/ws-start|stop|status
- **共享引擎 + 多实例配置** — `engine/` 零硬编码,团队差异全进 `instances/<名>/config.yaml`

## ⚠️ 踩坑提示

- `lark-cli config init` 必须先跑,多实例用 `--profile` 隔离凭据
- 多维表格同步是**单向**(本地 markdown → 飞书),别在飞书侧改数据期望回流
- WebSocket 健康检查依赖 `health.py` 自动重启,别手动 kill 进程

## 🤔 为什么这次推它给你

1. **命中 intent.what：** lark-cli + 多维表格 + Claude Code 自建业务流(项目管理),产品化的多实例部署模式
2. **命中 soft pref：** 中文 README、有设计文档(spec/plan/部署清单)、22 测试通过、四项治理校验是独立设计点
3. **没命中的 trade-off：** 强绑定 Claude Code 当 Agent 本体,换其他 agent 框架需重写;多维表格只单向镜像不做双向

---
*由 /gitout 生成 · 2026-07-07 · intent: "飞书 cli+多维表格 自建业务流 近3个月活跃"*
