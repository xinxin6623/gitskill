---
type: repo
repo: foambubble/foam
domain: misc
status: active
decision: harvest
discovered: 2026-05-22
last_reviewed: 2026-05-22
theme: personal-kb
intent_matched: "VSCode 内嵌的 Markdown wiki（与你 kb skill 工作流最贴合）"
signals:
  stars: 17149
  last_commit: 2026-05-22
  language: TypeScript
  license: Other
url: https://github.com/foambubble/foam
absorption:
  harvested: false
  used: false
  used_in: []
---

# Foam · 小白说明书

## 🧐 这是什么

**直接装在 VSCode 里的个人知识库扩展**，17k 星。基于 VSCode + GitHub 两件套——笔记是 Markdown 文件、双向链接靠 VSCode 自动补全、图谱视图就是个 VSCode panel。同名文件支持不同目录（用最短唯一标识符）、文件改名时链接自动同步。

不是独立 app，是**"把 VSCode 变成 Obsidian"**的扩展集合。

## 💡 解决什么问题

你已经在 VSCode 里写代码 + 写笔记 + 写文档（CLAUDE.md 之类）了：

- 切到 Obsidian 写笔记打断心流
- 笔记和代码分两个 app 不方便
- 用 git 同步笔记最舒服，已有的工作流就是这个

Foam 让你**完全不切换工具**——VSCode 里就能享受双向链接、图谱、链接自动补全、placeholder（未来要写的页面）追踪。

## 🎯 谁该用 / 谁别用

**适合你如果：**
- VSCode 重度用户（你正是）
- 用 git 管笔记
- 想 publish 笔记到 GitHub Pages（Foam 集成了 publish 工具）

**别浪费时间如果：**
- 不用 VSCode
- 想要 outliner 而不是文档式笔记
- 想要移动端（VSCode 移动支持有限）

## 🚀 三分钟上手

```bash
# 在 VSCode 里
# Marketplace 搜 "Foam" 装扩展（foam.foam-vscode）

# 或开个新仓库当 foam-template
git clone https://github.com/foambubble/foam-template.git mynotes
code mynotes
```

然后在 .md 文件里打 `[[` 自动补全已有笔记，写一个不存在的会创建 placeholder。

## 🔑 关键文件 / 关键概念

- **VSCode extension** — 主体形式
- **placeholder** — 你引用了还没创建的页面，foam 会追踪
- **Daily notes** — 类似 Logseq 的日报功能
- **graph view** — 在 VSCode panel 里看双向链接图
- **publish to GitHub Pages** — 集成 Jekyll / 11ty 等

## ⚠️ 踩坑提示

- 是社区项目，活跃度比作者爆肝时低
- License 是 "Other"（实际是 MIT，但 GitHub 解析问题）
- 同名文件多了，placeholder 解析偶尔抽风

## 🤔 为什么这次推它给你

**你 kb skill 的工作流可以直接基于 Foam 增强**。kb 现在是命令行调用，但你写笔记肯定在编辑器里——**让 Foam 处理 VSCode 内的双链 + 图谱 + 自动补全，kb skill 专注做"LLM 辅助 + 自动整理 + lint"**，两者职责分清。pattern 候选：`pkm-as-editor-extension`、`graph-view-on-markdown-folder`。

---
*由 /gitout 生成 · 2026-05-22 · theme: 个人知识库 / Markdown wiki*
