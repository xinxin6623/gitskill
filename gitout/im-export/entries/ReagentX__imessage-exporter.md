---
type: repo
repo: ReagentX/imessage-exporter
domain: misc
status: active
decision: harvest
discovered: 2026-05-22
last_reviewed: 2026-05-22
theme: im-export
intent_matched: "iMessage 完整导出（Rust + 跨平台 + 工程化标杆）"
signals:
  stars: 5226
  last_commit: 2026-05-22
  language: Rust
  license: GPL-3.0
url: https://github.com/ReagentX/imessage-exporter
absorption:
  harvested: false
  used: false
  used_in: []
---

# imessage-exporter · 小白说明书

## 🧐 这是什么

**用 Rust 写的 iMessage 数据库导出器**，号称是 iMessage 数据**最完整最准确**的开源解析器。截至 macOS Tahoe 26.4 + iOS 26.4 的所有特性都支持：iMessage / RCS / SMS / MMS、回复线程、富文本、附件、表情贴纸、Apple Pay、Tapback、URL 预览、手写消息、编辑过的消息……一个都不少。

可作为 CLI binary 或 Rust library 用，跨 macOS / Linux / Windows。

## 💡 解决什么问题

iMessage 是 Apple 用户最重要的通信方式之一，但：

- Apple 完全没给导出选项
- 换平台（Android / Windows）就丢历史
- 法律 / 合规需要的聊天记录（仲裁、举证）拿不到
- 想给个人 AI 喂数据需要结构化原始信息

imessage-exporter 把 macOS 上 chat.db 完整解析出来，导出 txt 或 html。html 模式漂亮，附件原样保留。

## 🎯 谁该用 / 谁别用

**适合你如果：**
- Apple 生态用户想完整掌握自己的通信数据
- 想做"iMessage as AI 训练数据"
- 学 Rust 解析二进制格式（typedstream / plist）的范本

**别浪费时间如果：**
- 不用 iMessage
- 嫌 Rust 安装麻烦
- GPL-3.0 协议你商用不接受

## 🚀 三分钟上手

```bash
# Homebrew
brew install imessage-exporter

# 或 cargo
cargo install imessage-exporter

# 跑（默认导出到 ~/imessage_export）
imessage-exporter -f html -c full

# 跑诊断
imessage-exporter --diagnostics
```

## 🔑 关键文件 / 关键概念

- **imessage-database** crate — 独立 lib，可以单独引入做自定义工具
- **typedstream 格式** — Apple 自家二进制格式，作者反向工程了
- **plist payload_data** — 附件元数据，作者用 Xplist 配合
- **`-c full`** — 包括所有附件，磁盘空间要留够

## ⚠️ 踩坑提示

- 需要 macOS Full Disk Access（在系统设置里给终端权限）
- GPL-3.0：你 fork 改也得开源
- iOS 备份格式不同，要先用 iMazing 之类提取 chat.db

## 🤔 为什么这次推它给你

**Mac 用户做"个人数据遗产化"的最佳工具，也是 weixinjilu 的对照范本**。它的 Rust 工程质量极高（lib + binary 分离、跨平台、覆盖 iMessage 所有特性），**目录组织、CLI 设计、HTML 模板**都是值得抄的范本。你做 weixinjilu 想升级到 Rust 或者支持 iMessage 的话直接参考这个。pattern 候选：`lib-and-binary-dual-crate`、`incremental-export-with-diagnostics`。

---
*由 /gitout 生成 · 2026-05-22 · theme: 聊天记录 / 个人数据遗产化*
