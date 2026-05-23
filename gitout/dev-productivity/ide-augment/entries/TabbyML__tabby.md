---
type: repo
repo: TabbyML/tabby
domain: dev-productivity/ide-augment
status: active
discovered: 2026-05-23
last_reviewed: 2026-05-23
intent_matched: "自托管 Copilot：Rust server + 多 IDE 客户端，跑在自己 GPU 上"
signals:
  stars: 33541
  last_commit: 2026-03-02
  language: Rust
  license: NOASSERTION
url: https://github.com/TabbyML/tabby
absorption:
  harvested: false
  used: false
  used_in: []
---

# Tabby · 小白说明书

## 🧐 这是什么
一个 Rust 写的自托管 AI 编码助手 server，给 VSCode / IntelliJ / Vim 提供代码补全和 chat。一台机器跑起来，全公司的 IDE 都接它，不用把代码发给 OpenAI。

## 💡 解决什么问题
- 你公司不让代码外传，但你又想用 AI 补全
- 你有一台带 GPU 的服务器（甚至消费级 GPU 就行），想跑公司内部的 Copilot
- 你想要"代码补全 + chat + 仓库索引"一站式，不想自己拼 ollama + 插件

## 🎯 谁该用 / 谁别用
**适合你如果：** 想搭团队级私有 Copilot；研究 LSP / 补全 server 工程实现（Rust）；需要 OpenAPI 接口接入自家 Cloud IDE
**别浪费时间如果：** 个人开发者只想要补全（直接 ollama + continue 插件即可）；没有 GPU 机器（CPU 跑慢到不可用）

## 🚀 三分钟上手
```bash
# Docker（最简单）
docker run -it --gpus all -p 8080:8080 \
  -v $HOME/.tabby:/data \
  tabbyml/tabby serve --model StarCoder-1B --device cuda

# 然后在 VSCode 装 "Tabby" 扩展，endpoint 填 http://localhost:8080
```

## 🔑 关键文件 / 关键概念
- `crates/tabby/` — 主 server，Rust 工程结构非常清晰
- `crates/llama-cpp-server/` — 推理后端封装
- `clients/vscode/`、`clients/intellij/`、`clients/vim/` — 各 IDE 客户端，看完知道怎么对接 LSP 风格的补全协议
- `ee/` — 企业版（团队管理、SSO），普通用 OSS 部分就够
- "Answer Engine"概念 — 把仓库知识做成可问答的索引

## ⚠️ 踩坑提示
- License 是 NOASSERTION（实际为 Apache-2.0 + 企业模块另算），商用前看清 `ee/` 目录
- 模型显存吃得不少，1B 模型起步约 4GB，跑 7B 要 16GB
- 最近一次 push 是 2026-03，相对没那么活跃；但有姐妹项目 [pochi](https://github.com/TabbyML/pochi) 在迭代

## 🤔 为什么这次推它给你
你说"工程参考"——Tabby 是少数把 LLM 推理 server + 多 IDE 客户端 + 索引系统全做在一个 monorepo 里的开源项目，Rust 代码组织值得抄。trade-off：项目重心在往 agent / pochi 转，纯补全这条线进展慢了一点。

---
*由 /gitout 生成 · 2026-05-23 · intent: "个人提效工具，skill ide codeing harness 工程"*
