# personality-test · 性格 / 心理测试

> MBTI / 大五 / 九型等性格测试的开源实现（webapp、微信小程序、题库 API）。
> 用于个人挂站、社群活动、团建、自定义题库 SaaS 起点。

## 健康度（2026-05-24）

| 指标 | 值 |
|---|---|
| entries | 5 |
| 主流栈分布 | Python/Django × 1，JS/HTML 静态 × 1，TS 小程序 × 1，TS API × 1，Java/Vue/Taro 教学栈 × 1 |
| 全活跃（近 1 年有 commit） | 5/5 |
| 风险点 | 多数 repo 缺 license，商用前需逐个确认 |

## 速览

| ⭐ | repo | 一句话 | 场景 |
|---|---|---|---|
| ⭐ | [[personality-test/entries/liyupi__yudada|liyupi/yudada]] | 鱼皮 AI 答题平台教学项目（MBTI 是第一阶段，扩展性最强） | 想做通用答题平台 |
|   | [[personality-test/entries/zcw576020095__mbti-test|zcw576020095/mbti-test]] | Django MBTI 系统 + PDF 导出，最快可上线 | Python 用户挂站 |
|   | [[personality-test/entries/MskTmi__MBTI|MskTmi/MBTI]] | 纯静态 93 题中文版，5 分钟挂 Pages | 零部署体验 |
|   | [[personality-test/entries/SwapnilSoni1999__16personalities-api|SwapnilSoni1999/16personalities-api]] | 16personalities.com 非官方 API，只写前端 | 题库即用 |
|   | [[personality-test/entries/lilemy__mbti-mini|lilemy/mbti-mini]] | TypeScript 微信小程序参考实现 | 小程序起点 |

## ⭐ 首推：liyupi/yudada
本主题里**唯一覆盖"网页 + 小程序 + 通用题库扩展"**三件套的项目。星数虽不最高，但完整度和教学价值最高，能从 MBTI 起步做到任意自定义答题应用。

## 相关周边（未入选主表）
- [juncheong/MBTI-Test](https://github.com/juncheong/MBTI-Test) — React + Node + MySQL 全栈，2023 停更，学习参考用
- [suyadong-dev/MBTI-](https://github.com/suyadong-dev/MBTI-) — 中文 MBTI 小程序，过新过小

## 检索元信息
- 查询轮次：5 query（mbti test / personality quiz / 16personalities / mbti 小程序 / mbti react）
- 候选池：40 → 一轮 reject 后 7 → 二轮 reject 后 5 入选
- raw 归档：[../raw/2026-05-24/personality-test/](../raw/2026-05-24/personality-test/)

discarded_queries: []

> 反思 2026-05-24：最低效环节 = SKILL.md 里 `archivedAt` 写错（实际是 `isArchived`），5 个 query 全失败白跑一轮；下次改 = 已修 SKILL.md 同 PR 提交。
