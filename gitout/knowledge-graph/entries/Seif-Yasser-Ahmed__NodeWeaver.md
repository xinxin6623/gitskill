---
type: repo
repo: Seif-Yasser-Ahmed/NodeWeaver
domain: knowledge-graph
status: active
discovered: 2026-05-25
last_reviewed: 2026-05-25
intent_matched: "把长 PDF / markdown 文档抽成 Obsidian 兼容的知识图谱文件夹，agent 驱动"
signals:
  stars: 0
  last_commit: 2026-05-22
  language: Python
  license: MIT
url: https://github.com/Seif-Yasser-Ahmed/NodeWeaver
absorption:
  harvested: false
  used: false
  used_in: []
---

# NodeWeaver · 小白说明书

## 🧐 这是什么
"agent 把大 PDF 啃成 Obsidian 知识图谱"的 pipeline。不是 Obsidian 插件——是个独立 Python 工具，输出一坨带 `[[wikilink]]` 的 markdown 文件，你拖进 Obsidian 就能直接看图。查询时不靠向量相似度，而是物理遍历 wikilink 拉上下文。

## 💡 解决什么问题
- 普通 RAG 切 500 token 块塞向量库 → 多跳问题答不了
- 想要"图能给人看"——黑盒向量数据库无法肉眼检查 AI 到底建了啥
- 想要可溯源的答案，告诉你"我读了哪几个 .md 文件得出这结论"
- 笔记数据要永远是 plain text，不能锁在某个 SaaS 里

## 🎯 谁该用 / 谁别用
**适合你如果：**
- 你已经是 Obsidian 用户，想让 AI 帮你把 PDF 资料自动织进 vault
- 觉得"向量相似度黑盒"不可信，想要确定性的图遍历推理
- 愿意付 GPT-4o-mini 抽取费用（map 阶段），高质量 reasoning 用 Claude

**别浪费时间如果：**
- 想要纯本地（默认配 OpenAI/Anthropic API，要改成 Ollama 得自己折腾 LiteLLM）
- 不用 Obsidian，也不喜欢 markdown 双链
- 只想要个 GUI，这是纯 CLI

## 🚀 三分钟上手
```bash
git clone https://github.com/Seif-Yasser-Ahmed/NodeWeaver
cd NodeWeaver
pip install -r requirements.txt
cp .env.example .env  # 填 OPENAI_API_KEY 和/或 ANTHROPIC_API_KEY

# 把 PDF 扔进 data/raw/
python src/runner.py ingest manual.pdf

# 用 Obsidian 打开 data/vault/ 看建好的图

# 多跳查询
python src/runner.py query "认证模块如何与数据库约束交互？"
```

## 🔑 关键文件 / 关键概念
- `src/ingestion/vault_builder.py` — Map-Reduce：chunk 抽 entity → merge 去重 → 写带 wikilink 的 md
- `src/inference/query_engine.py` — 从查询命中的入口节点递归遍历 `[[link]]`，深度可控
- `src/llm/client.py` — LiteLLM 包装，理论上可切任意 provider
- 双模型架构：ingestion 用便宜小模型（gpt-4o-mini）批量抽，inference 用 Claude/GPT-4 推理

## ⚠️ 踩坑提示
- 默认要 OpenAI + Anthropic 两个 key，改成单 provider / Ollama 要动 .env
- "图就是 markdown 文件夹"听着浪漫，但**百万 token 级别**会产生上千个 md，文件系统会卡
- Obsidian 兼容只是输出格式兼容，**没有 Obsidian 插件**——是离线生成的
- 0 stars 新项目，issue 没人回

## 🤔 为什么这次推它给你
你说"大量 markdown 笔记或聊天历史，想自动找概念关系，输出可交互图谱"——NodeWeaver 把这个倒过来了：**先 PDF 进、自动织成 markdown 图谱出**。它精准命中你的 anti-pattern 边界：**不是** Obsidian 双链插件（不靠你手动写链接），而是 LLM agent 主动抽 entity/relation 后生成 wikilink，本质还是 KG 抽取 + 用 markdown 当存储格式。配上 Obsidian 自带的图视图，你立刻就有"可交互可视化"。Trade-off：0 stars + 默认云 API。

---
*由 /gitout 生成 · 2026-05-25 · intent: "从非结构化文本自动抽取实体关系、构建可视化知识图谱"*
