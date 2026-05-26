---
type: repo
repo: SwapnilSoni1999/16personalities-api
domain: personality-test
status: active
discovered: 2026-05-24
last_reviewed: 2026-05-24
intent_matched: "MBTI 题库 API，前端只管 UI"
signals:
  stars: 54
  last_commit: 2025-03-11
  language: TypeScript
  license: unknown
url: https://github.com/SwapnilSoni1999/16personalities-api
absorption:
  harvested: false
  used: false
  used_in: []
---

# 16personalities-api · 小白说明书

## 🧐 这是什么
**16personalities.com 官网的非官方 API 镜像**。一个 GET 拿全套题目、一个 POST 提交答案拿性格类型 + 详细描述。题目和判分逻辑都是它管，你只写前端。

## 💡 解决什么问题
- 想做一个**视觉风格自定义**的 MBTI 测试，但不想自己整理 100 道题 + 写计分逻辑
- 想要 16personalities 那套"NT/NF/SJ/SP + 含描述/动画"的完整结果数据
- 后端从零做？算了，调个免费 API 完事

## 🎯 谁该用 / 谁别用
**适合你如果：** 你强在前端（React Native / Flutter / 小程序），后端能省则省；接受第三方服务有挂掉的风险；只是个人项目或非商业 demo。

**别浪费时间如果：** 你的 app 要上架商店（**非官方 API + 镜像官网内容 = 法律灰区**）；要做完全离线版本；服务正式上线后稳定性要求高。

## 🚀 三分钟上手
```bash
# 不用 clone，直接调
curl https://16personalities-api.com/api/personality/questions

# 提交答案
curl -X POST https://16personalities-api.com/api/personality \
  -H "Content-Type: application/json" \
  -d '{"answers":[{"id":"...","value":3}],"gender":"Male"}'
```
答案值范围 -3 到 +3（强烈不同意到强烈同意）。

## 🔑 关键文件 / 关键概念
- README — 两个 endpoint 文档（GET questions / POST personality）
- 返回字段含 `fullCode`（如 ISTP-A）、`niceName`、`traits[]` 五维分数
- 不需要 API key、不需要鉴权

## ⚠️ 踩坑提示
- **官方随时可能封 API**，别拿它做正式产品的核心依赖
- 题目和结果是英文，要中文得自己翻译映射
- 没 license 标注，**严格说就是个爬虫镜像**，使用风险自负

## 🤔 为什么这次推它给你

1. **命中 intent.what：** 让你"做 MBTI 测试程序"这事**前端工作量减半**——拿来即用的题库 + 计分 + 16 型描述。
2. **命中 soft pref：** 维护到 2025 年，TypeScript 写的，整合到现代前端栈零摩擦。
3. **没命中的 trade-off：** **非官方 + 英文** 两个大坑——中文界面要自己翻译，商用要做好被切断的预案。

---
*由 /gitout 生成 · 2026-05-24 · intent: "mbit 测试 app 或程序或网页端或小程序，现在比较流行的"*
