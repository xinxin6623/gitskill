# decisions.md — 人工 override 累计记录

每次 /gitout 跑完后，如果对结果有异议（该 reject 的没 reject、排序不对、漏推了好项目），
记录在此。积累足够 override → 提炼进 `rubrics/*.md`。

> 这是 Rubric-as-Interface 的反馈入口：改 rubric 是治本，改 entry 是治标。
> 改 rubric 时 `git commit -m "rubric: <which> <change>"`，演化历史就是系统的"学习曲线"。

## 格式

```
### YYYY-MM-DD · <domain> · <owner/repo 或 "整体排序">
- **LLM 决策**: reject | 入选 | 排第 N
- **我的决策**: reject | 入选 | 该排第 N
- **理由**: 一段话，说清楚为什么 LLM 错了
- **是否已改 rubric**: yes（指向 commit）/ no（待积累）
```

---

<!-- override 记录从此处往下追加 -->
