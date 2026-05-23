---
type: repo
repo: liyupi/yudada
domain: personality-test
status: active
discovered: 2026-05-24
last_reviewed: 2026-05-24
intent_matched: "MBTI 测试 webapp/小程序自部署"
signals:
  stars: 385
  last_commit: 2025-04-19
  language: Java
  license: MIT
url: https://github.com/liyupi/yudada
absorption:
  harvested: false
  used: false
  used_in: []
---

# 鱼答答 yudada · 小白说明书

## 🧐 这是什么
鱼皮老师的"AI 答题应用平台"教学项目，**MBTI 只是它的第一阶段**——后面会一路升级成可创建任意题库的通用 SaaS。Vue 3 + Spring Boot + Taro 小程序，全套都给你。

## 💡 解决什么问题
- 想做个 MBTI 测试小程序，但不知道完整该长啥样
- 想自己搭一个**通用答题平台**（不止 MBTI，还能塞九型、霍兰德、自定义题库）
- 想顺手学下"评分算法 + AI 总结回答"怎么落地

## 🎯 谁该用 / 谁别用
**适合你如果：** 想把 MBTI 当起点，做一个能上线的多题型测试平台；不介意 Java 全家桶；想要 Taro 小程序示例。

**别浪费时间如果：** 你只想要一个**今晚就能跑**的 MBTI 测试页面（这是教学项目，4 阶段渐进式，分支多）；不想碰 Spring Boot + Redis + RxJava 这一坨。

## 🚀 三分钟上手
项目分阶段，仓库里有多个分支对应 4 阶段。最快路径：

```bash
git clone https://github.com/liyupi/yudada.git
cd yudada
# 看 README 选 stage1（MBTI 小程序）还是 stage4（完整平台）
# stage1：Taro 小程序，cd 子目录跑 npm install && npm run dev:weapp
# stage4：后端 Spring Boot + 前端 Vue 3，看子目录 README
```

## 🔑 关键文件 / 关键概念
- `README.md` — 四阶段路径图，先读这个
- `yudada-frontend/` — Vue 3 后台
- `yudada-mini/` — Taro 写的小程序（含 MBTI 题）
- `yudada-backend/` — Spring Boot + ChatGLM AI 集成

## ⚠️ 踩坑提示
- 是付费课程的开源代码，README 满是引流链接，**别被吓到，代码本身能跑**
- 真要上线得自己接 ChatGLM API key，不然 AI 评分段挂掉
- Spring Boot + Redis + 分库分表配置不少，本地起一遍准备装 10 个东西

## 🤔 为什么这次推它给你

1. **命中 intent.what：** 包含 MBTI 性格测试小程序的**从零完整实现**（Taro 微信小程序），还能扩展成"任意题型答题应用"——比单纯 MBTI repo 更耐用。
2. **命中 soft pref：** 全中文 README + 中文题库 + 小程序场景齐全，三个软偏好全中。
3. **没命中的 trade-off：** 你说"现在比较流行的"，这个是**重型教学项目**不是"打开即用 demo"——想 3 分钟看结果它不合适，要的是周末开干的人。

---
*由 /gitout 生成 · 2026-05-24 · intent: "mbit 测试 app 或程序或网页端或小程序，现在比较流行的"*
