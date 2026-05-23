---
type: repo
repo: dendronhq/dendron
domain: misc
status: watch
decision: watch
discovered: 2026-05-22
last_reviewed: 2026-05-22
theme: personal-kb
intent_matched: "层级化（hierarchical）笔记组织（命名空间式 PKM）"
signals:
  stars: 7401
  last_commit: 2026-05-21
  language: TypeScript
  license: Apache-2.0
url: https://github.com/dendronhq/dendron
absorption:
  harvested: false
  used: false
  used_in: []
---

# Dendron · 小白说明书

## 🧐 这是什么

**专门为开发者设计的"层级命名空间"式 PKM 工具**，7.4k 星。文件名直接是层级路径，比如 `project.openclaw.architecture.md`、`project.openclaw.security.md`——靠点分隔体现层次。VSCode 扩展，markdown 文件，本地优先。

**重要：作者已宣布只维护不开发**（`maintenance only, active development has ceased`），但理念仍然值得学。

## 💡 解决什么问题

Logseq / Foam / Obsidian 都靠"标签 + 链接"建立结构，但当笔记上万条后：

- 找东西全靠搜索 + 滚屏
- 层级关系不清晰
- 没有"按住命名空间收起整个分支"的体验

Dendron 借鉴 **Unix 文件系统的命名空间思想**——把笔记按层级命名，VSCode 边栏自然形成树。引用 Vannevar Bush 1945 那句关于"信息工具"的名言作 motivation。

## 🎯 谁该用 / 谁别用

**适合你如果：**
- 你笔记体系强烈层级（如 `project.X.Y.Z`）
- 喜欢"目录树即知识结构"
- 想学一种已存档但有思想的 PKM 范式

**别浪费时间如果：**
- 项目已停止开发，不能依赖未来更新
- 你的知识结构网状不强层级
- 看重活跃社区

## 🚀 三分钟上手

```bash
# VSCode Marketplace 装 "Dendron"
# 或直接装相关插件包

# 笔记文件命名约定：
# my.project.alpha.md
# my.project.beta.md
# 自动形成 my.project 父节点
```

## 🔑 关键文件 / 关键概念

- **dot-separated naming** — `a.b.c.md` 就是核心
- **schema 系统** — 给某个 namespace 定义模板和必填字段
- **lookup 命令** — VSCode 内快速定位/创建
- **publish** — 自己的发布管线（类似 Quartz 思路）

## ⚠️ 踩坑提示

- **已停止开发**，重大 bug 不会修
- 文件名长，跨工具兼容性差（其他 PKM 工具不懂层级语义）
- 切换到 Obsidian / Logseq 后这些点分隔文件名会很尴尬

## 🤔 为什么这次推它给你

**学思想不学工具**。Dendron 已经停了，但**它的"命名空间作为一等公民"**这个想法对你 kb / mem 项目结构有借鉴价值。你 `~/knowledge/concepts/` 下的文件可以借鉴这个命名法：`voice-pipeline.barge-in.md`、`voice-pipeline.streaming.md`，**让命名本身承担一部分结构责任**。pattern 候选：`namespace-as-filename`、`hierarchical-pkm`。

---
*由 /gitout 生成 · 2026-05-22 · theme: 个人知识库 / Markdown wiki*
