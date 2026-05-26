# 飞书副本 · Gitea 自建 Git 仓库选型结论

## 元数据

- **推送时间**: 2026-05-26
- **飞书 URL**: https://ccn3ixoh82kp.feishu.cn/docx/J7NldnCe1oEgY6xJ1qNc4Ugnn6f
- **document_id**: J7NldnCe1oEgY6xJ1qNc4Ugnn6f
- **推送命令**: `lark-cli docs +create --api-version v2 --content '...'`
- **同步策略**: ❌ 不同步，本地是真相源（见 [followups/README.md](../../README.md)）

## 推送时使用的 XML 内容（一次性快照）

> 这份内容是 2026-05-26 推送飞书时的状态。**本地真相源是 [../decision.md](../decision.md)，如有出入以本地为准**。如需更新飞书，先改 decision.md，再用 `lark-cli docs +update --api-version v2` 推一次。

```xml
<title>Gitea 自建 Git 仓库选型结论 · 4C4G 火山云</title>

<callout emoji="🏁" background-color="light-green" border-color="green">
  <p><b>一句话结论：</b>装 <b>Gitea</b>，一个就够你用 3 年。MIT 协议干净、Go 单二进制优雅、有完整 REST API 让 Claude Code 顺畅维护、Packages 收纳 AI 时代杂七杂八的源码物料。</p>
</callout>

<h1>📌 你的核心诉求</h1>
<ul>
  <li>代码量轻，需求轻</li>
  <li>AI 时代要放杂七杂八的源码物料：依赖、项目源码、skills 源码</li>
  <li><b>没有版权和开源协议风险</b></li>
  <li>代码优雅、便于 agent 维护</li>
  <li>服务器：4 核 4G 火山云</li>
</ul>

<h1>⚖️ 三层维度对比</h1>
<h2>1. 协议风险维度（你新加的硬约束，最关键）</h2>
<!-- 表 1: License 对比表 -->

<h2>2. 代码优雅 + agent 友好维度</h2>
<!-- 表 2: agent 维护难度对比 -->

<h2>3. AI 时代多源码维度</h2>
<!-- ul: Packages / Mirror / Releases -->

<h1>🚀 直接抄的部署方案</h1>
<!-- pre lang=yaml: docker-compose.yml -->

<h1>🎯 最终选型</h1>
<!-- grid: 选 Gitea 理由 + 未来切换信号 -->
```

> 完整 XML 内容存在 git log 里（commit message 或 PR 描述）。本副本仅记录骨架结构，详情看本地 decision.md。

## 推送时遇到的坑

- 第一次带了 `--json` flag 报 `unknown flag: --json`（lark-cli 默认就是 JSON 输出，不需要也不支持这个 flag）
- 第二次去掉 `--json` 一把过

## 是否需要更新

| 触发条件 | 动作 |
|---|---|
| decision.md 关键决策变了 | 手动 `lark-cli docs +update` 推 |
| Gitea 版本升级 / 部署细节变了 | 手动推 |
| 只是补充信息 | 看 [followups/README.md](../../README.md)，可能不需要回推 |
