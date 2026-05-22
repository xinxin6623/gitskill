# gitout · 项目搜索与吸收目录

> 由 `/gitout` skill 自动维护。本目录组织框架借鉴自 `radar-system-v1.2.md`。

## 目录结构

```
gitout/
├─ README.md                  # 本文件
├─ raw/{YYYY-MM-DD}/          # gh search 原始 JSON，只读审计痕迹
├─ <domain>/                  # 按 domain 分类（misc 是默认）
│   ├─ README.md              # 健康度面板
│   ├─ index.yaml             # 活跃 entry 索引（≤ 30）
│   ├─ entries/               # 每个 repo 一份小白说明书（≤ 1000 字）
│   ├─ snippets/              # 手动抓取的代码片段（可选）
│   └─ graveyard.md           # 淘汰项目反查
└─ snippets/                  # 公共片段池（未分域）
```

## 容量上限（沿用 v1.2 §5.3）

| 资源类型 | 单 domain 上限 |
| ---- | ----------- |
| active entries | 30 |
| snippets | 50 |

超上限自动进入 yellow / red 状态，需用 `/gitout prune` 整理。

## 使用入口

- `/gitout <关键词>` — 搜索并生成小白说明
- `/gitout list` — 列出已收纳
- `/gitout open <repo>` — 查看某条
- `/gitout prune` — 容量与陈旧检查

Skill 源码：`../skills/gitout/SKILL.md`
