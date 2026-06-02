# insights · 成长型知识库

> 给"个人吸收和创造"一个家。在 gitout/（发现）和 followups/（决策）之外，这里是**沉淀、消化、自研**的场所。
> 最后更新：2026-05-30

---

## 四类内容

| 目录 | 内容 | 创建时机 | 容量上限 | 反向链接 |
|------|------|---------|----------|----------|
| [[insights/patterns/INDEX.md|patterns/]] | 跨 2+ repo 提炼的抽象模式 | 发现重复模式时 | ≤ 20 | → 关联 ≥2 个 gitout entry |
| [[insights/learning/INDEX.md|learning/]] | 个人学习笔记 | 学新东西时 | 无上限 | → 关联相关 gitout entry |
| [[insights/synthesis/INDEX.md|synthesis/]] | 跨 3+ domain 横向对比/洞见 | 季度/月度整理 | 无上限 | → 关联多个 domain |
| [[insights/projects/INDEX.md|projects/]] | 自有项目文档 | 新建项目时 | 无上限 | gitout entry → used_in 指向这里 |

---

## 目录结构

```
insights/
├── INDEX.md                # 本文件，主入口
├── index.yaml              # 机器可读索引
├── _templates/             # 新建时复制使用的模板
│   ├── pattern.md
│   ├── learning.md
│   ├── synthesis.md
│   └── project.md
├── patterns/               # 跨项目抽象模式
│   ├── INDEX.md
│   └── <kebab-pattern-name>.md
├── learning/               # 个人学习笔记
│   ├── INDEX.md
│   └── <YYYY-MM-DD>-<topic>.md
├── synthesis/              # 跨域综合洞见
│   ├── INDEX.md
│   └── <topic>.md
└── projects/               # 自有项目
    ├── INDEX.md
    └── <kebab-project-name>/
        └── README.md
```

---

## 与 gitout/ 的关系规则

- `absorption.used_in` → 指向 `insights/projects/<name>`
- `absorption.harvested` → 指向 `insights/patterns/<name>`
- insights 文档**必须**反向链接回 `gitout/` 的源 entry
- patterns 必须关联 ≥2 个 source repo

详细约束见 [[CLAUDE.md#2ter]]#。
