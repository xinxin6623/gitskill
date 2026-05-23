---
type: repo
repo: silverbulletmd/silverbullet
domain: misc
status: active
decision: harvest
discovered: 2026-05-22
last_reviewed: 2026-05-22
theme: personal-kb
intent_matched: "可编程的浏览器内 Markdown PKM（Lua 脚本驱动）"
signals:
  stars: 5290
  last_commit: 2026-05-22
  language: TypeScript
  license: MIT
url: https://github.com/silverbulletmd/silverbullet
absorption:
  harvested: false
  used: false
  used_in: []
---

# SilverBullet · 小白说明书

## 🧐 这是什么

**用 Lua 脚本可编程的浏览器内 Markdown 知识库平台**。5.3k 星，MIT。客户端 TypeScript + CodeMirror 6 + Preact，服务端 Go。可以 self-host 一份在自己 VPS / NAS / 本地，开网页就能编辑，自带双向链接 + 数据库式查询 + Tasks。

最大独特性：**Space Lua（自家 Lua 方言）让你能写脚本生成内容、定义自定义命令、做 widget**——本质上把"笔记"和"小型 web 应用"模糊了。

## 💡 解决什么问题

主流 PKM 的弱点：

- 客户端跨设备同步麻烦（Obsidian Sync 收费）
- 想动态生成内容（比如"汇总所有未完成 task"）要装插件且不灵活
- 想做自定义 UI 几乎不可能

SilverBullet **把 PKM 当成可编程平台**：你可以写 Lua 直接在某页面生成"今日 task 列表"、"近 30 天每周日报汇总"、"查询所有带 #book 标签的页面排序"。**笔记会变成你专属的小 Notion**。

## 🎯 谁该用 / 谁别用

**适合你如果：**
- 喜欢"工具适应我"不是"我适应工具"
- 接受 Lua（不难）
- 想 self-host 一份做团队 / 家庭共享 wiki

**别浪费时间如果：**
- 不愿意自部署
- 抗拒任何脚本语言
- 想要原生 app 体验（这是 PWA）

## 🚀 三分钟上手

```bash
# Docker（最快）
docker run -it -p 3000:3000 -v $PWD/space:/space \
  zefhemel/silverbullet

# 然后浏览器开 http://localhost:3000

# 或 Deno
deno run -A --unstable https://get.silverbullet.md
```

## 🔑 关键文件 / 关键概念

- **Space** — 你的笔记集合（一个文件夹）
- **Space Lua** — 嵌入 markdown 里的 Lua 代码块，运行时执行
- **Objects + Queries** — 把元数据当数据库查询
- **Tasks** — 跨页面的任务系统
- **plugs** — 第三方插件机制（plug-api 暴露 API）

## ⚠️ 踩坑提示

- self-host 安全要自己负责（默认无认证）
- Lua 是自家方言 Space Lua，不完全是标准 Lua
- 移动端是 PWA，体验略输原生

## 🤔 为什么这次推它给你

**给你 kb skill 的"未来形态"想象**。你现在 kb 是 CLI + markdown 文件，未来想要"在浏览器里直接维护、动态生成 dashboard 页面"——SilverBullet 就是这个方向的现成参考。**它的 Lua scripting 模式 + Objects/Queries 数据库式 metadata 查询**是值得学的两个核心想法。pattern 候选：`programmable-pkm`、`metadata-as-database-in-markdown`。

---
*由 /gitout 生成 · 2026-05-22 · theme: 个人知识库 / Markdown wiki*
