---
type: repo
repo: starbaser/ccproxy
domain: dev-productivity/claude-workflow
status: active
discovered: 2026-05-23
last_reviewed: 2026-05-23
intent_matched: "在网络层 hook Claude Code 请求，按规则 route 到不同模型（OpenAI/Gemini/Perplexity）"
signals:
  stars: 400
  last_commit: 2026-05-17
  language: Python
  license: NOASSERTION
url: https://github.com/starbaser/ccproxy
absorption:
  harvested: false
  used: false
  used_in: []
---

# ccproxy · 小白说明书

## 🧐 这是什么
一个挂在 Claude Code 和 Anthropic API 之间的本地代理。Claude Code 以为自己在跟标准 API 说话，实际请求被 ccproxy 截获，按你写的规则路由：大 context 给 Gemini 2M，WebSearch 给 Perplexity，普通编码继续走 Claude 订阅，全程无感切换。v2 prerelease 更猛——直接走网络层 TLS 拦截，任意 LLM client 都能挂。

## 💡 解决什么问题
- 你订阅了 Claude 但偶尔想要 Gemini 的 2M 长 context，又不想换 IDE
- WebSearch 烧 Claude token，但 Perplexity 又便宜又强，没法分流
- Claude Code 本身不支持 model routing，你想做"按 token 数选模型"
- 想看一个**真正的 hook 中间层架构**长啥样（不是 Claude Code 里那种 hook，是网络代理 hook）

## 🎯 谁该用 / 谁别用
**适合你如果：**
- 你同时有 Claude / Gemini / OpenAI / Perplexity 账号，想统一在 Claude Code 里调度
- 你想学"如何用 LiteLLM 做多模型代理 + 规则引擎"
- 你愿意为省 token 折腾一下本地代理

**别浪费时间如果：**
- 你只有 Claude 一个 provider，没必要绕一层
- 你部署在团队/生产环境（这是个人代理，不是企业网关）
- 你受不了配置 YAML（ccproxy.yaml + config.yaml 两套）

## 🚀 三分钟上手
```bash
uv tool install claude-ccproxy --with 'litellm[proxy]'
ccproxy install              # 生成 ~/.ccproxy/{ccproxy,config}.yaml
ccproxy start --detach       # 起代理服务
ccproxy run claude           # 或 export ANTHROPIC_BASE_URL=http://localhost:4000
```

## 🔑 关键文件 / 关键概念
- `~/.ccproxy/ccproxy.yaml` — hook 链 + 路由规则（`TokenCountRule` / `MatchToolRule` / `MatchModelRule` / `ThinkingRule`）
- `~/.ccproxy/config.yaml` — 标准 LiteLLM proxy config，定义各个 provider
- **hook pipeline** — `rule_evaluator` → `model_router` → `forward_oauth` → `extract_session_id`，每个 hook 都是可插拔的 Python 模块
- **OAuth 自动注入** — 用你 `~/.claude/.credentials.json` 里的 token，不用手填 API key
- **v2 dev 分支** — 整个换成 rootless WireGuard namespace + TLS 网络层拦截 + DAG hook 引擎，已脱离 Claude Code

## ⚠️ 踩坑提示
- License 是 NOASSERTION，商业用前看一下作者意图
- LiteLLM 必须跟 ccproxy 装在同一 venv，否则 hook 加载不到（README 反复强调）
- v1 走 LiteLLM proxy，v2 走网络层——两套架构差很远，**别混着读文档**
- 路由规则按顺序匹配第一个命中，写规则时把强约束放前面（thinking / 大 token）

## 🤔 为什么这次推它给你
你要"harness 工程"。Claude Code 内置的 hook 是会话层（PreToolUse / PostToolUse），ccproxy 是**网络层** hook——同一个 hook 概念在不同抽象层的实现，是看"中间件设计"的极好样本。**hook pipeline + 规则引擎 + OAuth 转发**三件套放一起很值得抄。trade-off：v1 v2 架构断代，长期跟得跟主分支。

---
*由 /gitout 生成 · 2026-05-23 · intent: "个人提效工具，skill ide codeing harness 工程"*
