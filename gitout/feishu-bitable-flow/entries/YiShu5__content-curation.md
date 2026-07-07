---
type: repo
repo: YiShu5/content-curation
domain: feishu-bitable-flow
status: active
discovered: 2026-07-07
last_reviewed: 2026-07-07
intent_matched: "飞书 CLI + 多维表格自建业务流"
signals:
  stars: 123
  last_commit: 2026-06-29
  language: Python
  license: MIT
  url: https://github.com/YiShu5/content-curation
absorption:
  harvested: false
  used: false
  used_in: []
---

# content-curation (NoiseFilter) · 小白说明书

## 🧐 这是什么

多源内容(YouTube/Bilibili/小宇宙)自动抓取 → AI 深度改写 → 归档 + 飞书多维表格同步 + 博客展示的全链路内容策展系统,一条命令 5 分钟获取一小时播客精华。

## 💡 解决什么问题

- 每天优质内容太多看不完,收藏了等于没看
- 想做内容策展/知识库,但抓取+转录+摘要+归档各环节断开
- 摘要质量参差,简单总结没深度,想要金句+核心观点+1500字解读

## 🎯 谁该用 / 谁别用

**适合你如果：**
- 想从 YouTube/B站/小宇宙批量提炼知识资产
- 已用飞书多维表格做内容管理
- 想要一个开箱即用的"降噪风"博客站展示策展内容

**别浪费时间如果：**
- 不做内容策展,业务流模型对不上
- 飞书应用没开 `bitable:app` + `drive:drive` 权限
- 不想配 BibiGPT API Token(转录主力,免费兜底有限)

## 📜 协议风险

- **License：** MIT
- **商用 / 魔改 / 闭源：** ✅ 无风险
- **对外提供 SaaS / 给客户部署：** ✅ 无传染义务

## 🚀 三分钟上手

```bash
git clone https://github.com/YiShu5/content-curation.git
cd content-curation
pip install -r requirements.txt && npm install
cp config/.env.example config/.env  # 填 BibiGPT/OpenAI/飞书凭证
# 编辑 config/sources.yaml 配订阅源
./run.sh url "https://www.youtube.com/watch?v=xxx"  # 单条
./run.sh all                                         # 批量+飞书同步
```

## 🔑 关键文件 / 关键概念

- `scripts/fetch.py` — yt-dlp 元数据 + BibiGPT 转录 + 封面下载
- `scripts/rewrite.js` — DeepSeek/OpenAI 结构化 JSON(金句/观点/摘要)
- `scripts/sync-feishu.js` — 飞书多维表格同步 + 封面上传
- `scripts/sync-feishu-doc.js` — 飞书文档长文阅读视图
- `blog/app.py` — Flask 博客,直接读多维表格数据
- **评分体系** — AI 相关性 40 + 故事性 30 + 加分项 30 = 总分 100,分必读/强烈推荐/推荐/一般/可跳过

## ⚠️ 踩坑提示

- 多维表格字段类型要严格按 README 表建(AI相关性/故事性/加分项是数字字段,评级是单选)
- BibiGPT 免费额度有限,大批量抓取需付费 Token
- `sync-doc` 需额外开 `docx:document` 权限,只做多维表格可跳过

## 🤔 为什么这次推它给你

1. **命中 intent.what：** 飞书多维表格做内容策展业务流,fetch→rewrite→sync 三段式全链路自建
2. **命中 soft pref：** 中文 README、完整字段说明表、内置博客展示站、AI 提示词可自定义
3. **没命中的 trade-off：** 用飞书原生 API 而非 lark-cli(用户问的是"飞书 CLI"),但多维表格业务流完整度足以入选

---
*由 /gitout 生成 · 2026-07-07 · intent: "飞书 cli+多维表格 自建业务流 近3个月活跃"*
