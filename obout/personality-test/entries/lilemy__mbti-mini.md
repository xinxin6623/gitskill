---
type: repo
repo: lilemy/mbti-mini
domain: personality-test
status: watch
discovered: 2026-05-24
last_reviewed: 2026-05-24
intent_matched: "MBTI 微信小程序参考实现"
signals:
  stars: 1
  last_commit: 2024-06-11
  language: TypeScript
  license: unknown
url: https://github.com/lilemy/mbti-mini
absorption:
  harvested: false
  used: false
  used_in: []
---

# lilemy/mbti-mini · 小白说明书

## 🧐 这是什么
一个 **TypeScript 写的微信小程序版 MBTI 测试**。star 少（1 个），但 2024 年的代码、TS 写法，比那些 2018 年的 jQuery 残骸看着舒服。**你想要小程序参考，这是少数能直接看的代码之一**。

## 💡 解决什么问题
- 想做个 MBTI 微信小程序，但找不到现代化（TS + 原生小程序）的参考
- 不想看鱼皮 [[liyupi__yudada]] 那种重型教学项目，只想要"最小可跑"的小程序
- 想学习小程序 Page 生命周期 + 题目分页交互怎么写

## 🎯 谁该用 / 谁别用
**适合你如果：** 你想做个人小程序练手，需要"能跑、能改"的代码基线；你看得懂 TypeScript + 微信小程序原生 API。

**别浪费时间如果：** 你期待精美 UI 或完整产品（这是练习项目，star=1）；你要 Taro/uni-app 跨端，不是原生小程序；你要中文社区维护活跃的项目。

## 🚀 三分钟上手
```bash
git clone https://github.com/lilemy/mbti-mini.git
# 用微信开发者工具打开项目目录
# AppID 用"测试号"即可，不需要注册小程序账号
# 点编译，模拟器就能跑
```

## 🔑 关键文件 / 关键概念
- `pages/` — 小程序页面（题目页、结果页）
- `utils/` — MBTI 计分工具函数
- TypeScript 配置直接复用作者的 `tsconfig.json`

## ⚠️ 踩坑提示
- star 极低 + 2024-06 后没动，可能有 bug 没人修
- 没 license，**只能学习不能商用**
- README 几乎是空的，全靠看代码

## 🤔 为什么这次推它给你

1. **命中 intent.what：** 你明确提到"小程序"场景，这是**现代代码风格（TS + 2024）的微信小程序 MBTI 参考**，候选池里独一份。
2. **命中 soft pref：** 命中"小程序"这个软偏好；代码量少（你说不想要重的）。
3. **没命中的 trade-off：** **流行度严重不符**（你说"现在比较流行的"，这个 star=1）——它是给你拿来当**起点改**的，不是用来"装上立刻用"。

---
*由 /gitout 生成 · 2026-05-24 · intent: "mbit 测试 app 或程序或网页端或小程序，现在比较流行的"*
