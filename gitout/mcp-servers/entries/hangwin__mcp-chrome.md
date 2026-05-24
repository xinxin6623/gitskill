---
type: repo
repo: hangwin/mcp-chrome
domain: mcp-servers
status: active
discovered: 2026-05-25
last_reviewed: 2026-05-25
intent_matched: "让 agent 操作浏览器，但用我已登录的真实 Chrome"
signals:
  stars: 11707
  last_commit: 2026-01-06
  language: TypeScript
  license: MIT
url: https://github.com/hangwin/mcp-chrome
absorption:
  harvested: false
  used: false
  used_in: []
---

# hangwin/mcp-chrome · 小白说明书

## 🧐 这是什么
一个 **基于 Chrome 扩展** 的 MCP server，把你日常用的 Chrome 直接变成 agent 可以操作的工具：不是另起一个 Playwright/Puppeteer 进程，而是接管你已经开着、已经登录的那个浏览器。20+ 工具：截图、网络监控、点击、书签、历史、跨标签上下文，还内置向量数据库做"语义搜索浏览历史"。

## 💡 解决什么问题
- 让 agent 帮你"看下我刚才在公司后台填到一半的那个表单"——Playwright 类做不到，因为它启动的是全新会话；这个直接用你已登录的 Chrome。
- 在本地高频做"截图当前页 / 抓 console / 看 network"调试，不想每次都重新登录测试账号。
- 想做"翻一下我过去一周看过的资料，找跟 X 相关的"——内置 SIMD-加速的本地向量数据库就是干这个的。

## 🎯 谁该用 / 谁别用
**适合你如果：** 频繁让 agent 跟你的真实浏览器交互；在意隐私（纯本地，无云端）；想要"打开 Claude → 让它操作我手头浏览器"的体验。
**别浪费时间如果：** 你的场景是无头爬虫 / CI 里跑测试（这种用 Playwright 类 MCP 更合适，比如官方 archived 的 puppeteer 或 microsoft/playwright-mcp）；不想装 Chrome 扩展。

## 🚀 三分钟上手
```bash
# 1. 装桥接（native messaging）
npm install -g mcp-chrome-bridge

# 2. 从 release 下载 Chrome 扩展，chrome://extensions 开发者模式加载

# 3. MCP 客户端配置（streamable HTTP，推荐）
{
  "mcpServers": {
    "chrome-mcp-server": {
      "type": "streamableHttp",
      "url": "http://127.0.0.1:12306/mcp"
    }
  }
}
```

## 🔑 关键文件 / 关键概念
- **mcp-chrome-bridge** — npm 全局包，跑 native messaging 桥
- **Chrome 扩展本体** — 从 release 下载，手动 load unpacked
- `docs/VisualEditor.md` — 给 Claude Code / Codex 的可视化编辑器
- 内置 **WebAssembly SIMD 向量库** — 跨 tab 语义搜索的底座

## ⚠️ 踩坑提示
- pnpm v7+ 默认禁 postinstall，要么 `pnpm config set enable-pre-post-scripts true`，要么手动 `mcp-chrome-bridge register`。
- 把你日常 Chrome 交给 agent = agent 拿到你**所有登录态**，权限非常大，别给不信任的 prompt 自动执行权。
- "early stages, 密集开发"——README 自承稳定性还在迭代，做关键自动化前测一下。

## 🤔 为什么这次推它给你
你的意图里"浏览器自动化"是高频场景，这份选项的差异化在于**用真实已登录浏览器**——这是 Playwright/Puppeteer 类 MCP 永远做不到的事。命中 hard_constraints（开源 MIT、TypeScript），命中 soft preferences（单功能强、含完整部署文档）。trade-off：得手动装扩展和桥接，不像 npx 一行那么轻；但换来的隐私 + 登录态复用值这点麻烦。

---
*由 /gitout 生成 · 2026-05-25 · intent: "MCP server 生态合集 — 给 agent 加工具能力"*
