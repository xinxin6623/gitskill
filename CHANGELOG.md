# gitskill · CHANGELOG

> 每次动了什么记一条。详细记录写在各自模块目录下（如 `gitout/retros/`），根目录 CHANGELOG 是**强标签化的检索索引**。
>
> **本项目下若有子项目**（子目录里也有 AGENTS/INDEX/CHANGELOG 三件套）：本 CHANGELOG **只记录跨多个子项目的同时操作**；单一子项目操作记在该子项目自己的 CHANGELOG 里。详见 [`docs/trio-protocol.md`](./docs/trio-protocol.md) §5 子项目嵌套（max-depth = 3）。

## 格式规范（严格）

```
## YYYY-MM-DD #<type> scope:<name> [#<extra-tag>...] - <一句话主题>

- Why: <一句话动机，不复述 what>
- 详见: <path 或 commit hash>
```

**硬约束**：
- 日期必须 ISO 格式 `YYYY-MM-DD`
- 类型标签必须以 `#` 开头，从下面字典选一个为主标签
- 作用域必须 `scope:<name>` 形式，name 用 kebab-case；多模块改动用多个 `scope:`
- Why 一行不超过 80 字符
- **不贴 diff、不复述 what**——那些进 commit 或模块自己的文档

## 类型标签字典

| 标签 | 含义 |
|---|---|
| `#feat` | 新功能 |
| `#fix` | bug 修复 |
| `#refactor` | 重构（无行为变化） |
| `#perf` | 性能优化 |
| `#docs` | 文档变更 |
| `#test` | 测试相关 |
| `#chore` | 构建/依赖/工具链/初始化 |
| `#archive` | 归档/弃用 |
| `#breaking` | 破坏性变更（叠加） |
| `#deprecated` | 标记弃用（叠加） |
| `#wip` | 进行中（叠加） |

## 检索示例

```bash
grep -E "^## .* #feat .* scope:gitout" CHANGELOG.md   # gitout 模块新功能
grep "#breaking" CHANGELOG.md                          # 所有破坏性变更
grep "^## 2026-06" CHANGELOG.md                        # 2026 年 6 月所有动作
```

---

## 2026-06-08 #chore scope:trio - 三件套 standard-v2 落地

- Why: 把项目规则从单文件 CLAUDE.md 升级为 trio 标准（AGENTS/INDEX/CHANGELOG + docs/trio-protocol.md），让 agent / skill 能用 frontmatter 自动识别
- 详见: AGENTS.md / INDEX.md / docs/trio-protocol.md；CLAUDE.md 已 git mv 为 AGENTS.md 并建相对软链回 CLAUDE.md

<!-- 新条目加在这里上方，保持最新在最上 -->
