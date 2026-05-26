---
type: repo
repo: gomods/athens
domain: git-self-host
status: active
discovered: 2026-05-26
last_reviewed: 2026-05-26
intent_matched: "企业级自建 Go module 代理 + 缓存"
signals:
  stars: 4763
  last_commit: 2026-05-15
  language: Go
  license: MIT
url: https://github.com/gomods/athens
absorption:
  harvested: false
  used: false
  used_in: []
---

# Athens · 小白说明书

## 🧐 这是什么

CNCF 沙箱项目，Go module 的**代理 + 私服 + 缓存**三合一。和 goproxy.cn 定位不同：goproxy.cn 是"我们运维好的公共代理你直接用"，Athens 是"你自己跑一份，企业级配置全有"。支持多种存储后端（本地、S3、MinIO、GCS、Azure Blob）。

## 💡 解决什么问题

- 公司禁止依赖外部公共代理（合规/审计），又要国内速度——Athens 自建一份完事
- 想要"上游 module 缓存 + 私有 module 私服"一个东西全搞定
- 多团队/多项目要统一 Go 依赖来源，方便做漏洞扫描和版本审计

## 🎯 谁该用 / 谁别用

**适合你如果：**
- 你或你团队是中重度 Go 开发，公共代理满足不了合规
- 服务器配置不差（Athens 比裸 goproxy 重些，4G 跑得动但要看并发）
- 想用对象存储做后端（火山云有 TOS 对象存储，S3 兼容，配 Athens 很顺）

**别浪费时间如果：**
- 个人开发 + 不在乎合规 → 直接用 goproxy.cn 别折腾
- 不写 Go → 走开
- 服务器内存 < 2G → 跑得起但比较吃力

## 🚀 三分钟上手

```bash
# Docker 起一个，本地磁盘做存储
docker run -d \
  --name athens \
  -p 3000:3000 \
  -v $(pwd)/athens-storage:/var/lib/athens \
  -e ATHENS_DISK_STORAGE_ROOT=/var/lib/athens \
  -e ATHENS_STORAGE_TYPE=disk \
  gomods/athens:latest

# 客户端
go env -w GOPROXY=http://your-server:3000,direct
go mod tidy
```

## 🔑 关键文件 / 关键概念

- `config.toml` — Athens 的核心配置，存储类型、上游代理、过滤规则都在这
- **Storage Backend** — disk / s3 / gcs / azureblob / mongo 任选，火山云 TOS 选 s3 即可（兼容 S3 协议）
- **Filter** — 通过 `filter.conf` 控制哪些 module 可以代理、哪些必须走私服，做合规审计的关键
- **`GONOSUMCHECK`** — Athens 自己当 sum 校验源，配置不当容易引发 sum mismatch

## ⚠️ 踩坑提示

- **首次使用 module 时会 stall**：Athens 同步上游需要时间，第一次拉某个 module 偶尔会超时，重试或预热即可
- **磁盘膨胀很快**：Go 生态依赖密集，几个月就能堆几十 G——一定要挂数据盘 + 定期清理
- **国内访问上游**：Athens 自己也需要能访问 proxy.golang.org，建议把 Athens 的 `GlobalEndpoint` 设成 `goproxy.cn` 做二级代理
- 跟 `GOPRIVATE` 配合：私有仓库别走 Athens，否则会卡到怀疑人生

## 🤔 为什么这次推它给你

1. **命中 intent.what：** 你说"国内环境拉依赖"——goproxy.cn 是消费端方案，Athens 是企业端方案，两者互补；如果你以后想"团队/公司维度统一管控"，goproxy.cn 不够用，Athens 才是出路。
2. **命中 soft pref：** CNCF 沙箱、活跃维护、Docker 一行起、支持对象存储后端，正好对接火山云 TOS。
3. **没命中的 trade-off：** Athens 比 goproxy 重得多，**个人玩纯属杀鸡用牛刀**——你如果只想"自己 go get 别卡"，goproxy.cn 直接用就行，Athens 留给"想搭团队私服时"再回来看。

---
*由 /gitout 生成 · 2026-05-26 · intent: "搜索git仓库自建相关项目，国内拉依赖+管理个人网站，4C4G 火山云"*
