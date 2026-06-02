---
type: repo
repo: goproxy/goproxy.cn
domain: git-self-host
status: active
discovered: 2026-05-26
last_reviewed: 2026-05-26
intent_matched: "国内 Go 依赖代理（可直接用 / 可自建）"
signals:
  stars: 7080
  last_commit: 2025-08-20
  language: HTML
  license: MIT
url: https://github.com/goproxy/goproxy.cn
absorption:
  harvested: false
  used: false
  used_in: []
---

# goproxy.cn · 小白说明书

## 🧐 这是什么

国内最大的 Go module 公共代理（七牛云赞助运维），同时也是这个公共服务的**源码 + 自部署文档**。它把全球的 Go module 缓存到国内 CDN，你 `go get` 不再需要翻墙。本仓库主要是宣传站 + 自建指引，真正的代理引擎在它的姐妹仓 `goproxy/goproxy`。

## 💡 解决什么问题

- `go mod tidy` 卡在 `golang.org/x/...` 拉不下来——直接用 goproxy.cn 立刻好
- 公司禁止依赖公共代理，但又想要国内速度——按它的指引在你的服务器自部署一份
- 想做内部 Go 模块私服 + 外部公共依赖缓存合一

## 🎯 谁该用 / 谁别用

**适合你如果：**
- 任何在国内写 Go 的人（直接用 `https://goproxy.cn` 就行，不需要自建）
- 想在火山云自建一份团队私有代理，又懒得从零开始撸代码
- 想看一个"在国内规模化跑 Go 代理"的工程参考

**别浪费时间如果：**
- 你不写 Go（这玩意只管 Go module，npm/pip/maven 找别的）
- 你只是个人开发者，公共 goproxy.cn 永久免费足够，不需要自建

## 🚀 三分钟上手

**直接用公共服务（推荐）：**

```bash
go env -w GOPROXY=https://goproxy.cn,direct
go env -w GOSUMDB=sum.golang.google.cn
go mod tidy   # 瞬间起飞
```

**自建（基于姐妹仓 goproxy/goproxy）：**

```bash
go install github.com/goproxy/goproxy/cmd/goproxy@latest
goproxy server --address :8080 --cache-dir /var/goproxy
# 团队改 GOPROXY=http://your-server:8080,direct
```

## 🔑 关键文件 / 关键概念

- **GOPROXY 环境变量** — Go 1.13+ 内置支持代理协议，配置一行搞定，不用改代码
- **`,direct` 兜底** — 代理找不到的私有模块走直连，不会被坑
- **GOSUMDB** — 校验数据库也要换国内镜像，否则 `go mod` 还是会卡

## ⚠️ 踩坑提示

- **公共 goproxy.cn 不缓存私有仓库**——你公司私有 Go 模块要么走 `GOPRIVATE`，要么自建
- **磁盘消耗**：自建后缓存会持续增长，火山云 4C4G 标配磁盘可能不大，注意挂数据盘 + 定期清理
- 别在 GOSUMDB 上偷懒关掉——它防供应链投毒，关掉等于裸奔

## 🤔 为什么这次推它给你

1. **命中 intent.what：** 你说"国内环境拉取相关依赖"——Go 生态里这就是标准答案，几乎全国 Go 开发者都在用。
2. **命中 soft pref：** 既能直接用公共服务（零成本），也能自建（如果你公司有私服需求），灵活度满分。
3. **没命中的 trade-off：** 只解决 **Go 一种语言**的依赖——如果你还要 npm/pip/Maven 国内镜像，那是另外一套（npm 用淘宝 npmmirror，pip 用清华源，Maven 用阿里云）。

---
*由 /gitout 生成 · 2026-05-26 · intent: "搜索git仓库自建相关项目，国内拉依赖+管理个人网站，4C4G 火山云"*
