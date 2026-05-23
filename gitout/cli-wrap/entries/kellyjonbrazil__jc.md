---
type: repo
repo: kellyjonbrazil/jc
domain: misc
status: active
decision: harvest
discovered: 2026-05-22
last_reviewed: 2026-05-22
theme: cli-agent
intent_matched: "把 GUI 软件包装成 Agent 可读输出（CLI-Anything 同道）"
signals:
  stars: 8615
  last_commit: 2026-05-22
  language: Python
  license: MIT
url: https://github.com/kellyjonbrazil/jc
absorption:
  harvested: false
  used: false
  used_in: []
---

# jc (JSON Convert) · 小白说明书

## 🧐 这是什么

一个**"把任何 Unix 命令的输出转成 JSON"的解析器集合**。已经支持 150+ 个命令（`ls` / `ps` / `dig` / `ifconfig` / `route` / ... 全在内）。你输入 `dig example.com | jc --dig`，它给你结构化 JSON，下一步直接 `jq` 取字段。也支持当 Python 库用。8.6k 星，MIT。

作者 Kelly Brazil 写了一篇博客叫 **Bringing the Unix Philosophy to the 21st Century**——21 世纪 Unix 哲学就该是 JSON 化 + 流水线。

## 💡 解决什么问题

Unix 工具的输出对 LLM 是噩梦：

- `ls -la` 输出对齐用空格，没法稳定切字段
- `ifconfig` 在不同系统格式不一样
- 让 LLM 解析自由文本既不稳又费 token

jc 直接给每个常用命令配一个 parser，**把输出转成稳定的 JSON schema**。Agent 调用 `jc dig example.com` 拿到的就是结构化数据，可以直接 `data[0]['answer'][0]['data']` 取 IP。

## 🎯 谁该用 / 谁别用

**适合你如果：**
- 在做 CLI-Anything 这种"GUI 包 CLI 给 Agent"的工作
- 想给 Agent 喂 Unix 工具输出但担心格式不稳
- 想搞 shell 自动化，需要结构化数据流

**别浪费时间如果：**
- 你的命令输出 jc 不支持（先查 parser 列表）
- 只需要单个命令的 JSON 输出，命令本身有 `--json` 选项就够了
- 对 JSON 过敏，喜欢纯文本

## 🚀 三分钟上手

```bash
pip install jc       # 或 brew install jc

# 管道用法
dig example.com | jc --dig | jq '.[].answer[].data'

# magic 语法，更短
jc dig example.com | jq '.[].answer[].data'

# Python 库用法
import jc, subprocess
out = subprocess.check_output(['dig', 'example.com'], text=True)
data = jc.parse('dig', out)
```

## 🔑 关键文件 / 关键概念

- **150+ parsers** — 详见 README 的 Parsers 表，每个 parser 有独立 schema 文档
- **流式 parser** — `--lsblk-s` 这类，处理大输出
- **`-r` raw 模式** — 不做 int/float 转换，保留原始字符串
- **Ansible filter plugin** — 已被 community.general 收录

## ⚠️ 踩坑提示

- 不同 OS 的 `ifconfig` 输出格式略不同，parser 可能失败 → 切 `ip addr` 试试
- parser 维护是社区驱动，新命令支持靠贡献
- "magic 语法"（`jc dig ...`）跟管道结果一样，但对 sudo 包了一层要小心

## 🤔 为什么这次推它给你

**CLI-Anything 的直接亲戚**。你们都在做"把工具输出标准化给 Agent"，jc 的 **150 parser 组织结构 + schema 文档化 + 流式处理** 是现成的最佳实践。可以直接参考它怎么管理 150 个独立 parser 不乱、怎么版本化 schema。pattern 候选：`output-normalization-via-parser-registry`。

---
*由 /gitout 生成 · 2026-05-22 · theme: CLI 包装 / Agent 工具化*
