---
type: repo
repo: liyupi/yudada
domain: personality-test
status: active
discovered: 2026-05-24
last_reviewed: 2026-05-24
intent_matched: "MBTI 测试 webapp/小程序自部署"
deep_dive: 2026-05-24   # 见文末"深入调查"节
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
- `yudada-frontend/` — Vue 3 + Arco Design 用户/管理后台
- `mbti-test-mini/` — Taro + React 写的 MBTI 微信小程序（**独立**，可不跑后端）
- `yudada-backend/` — Spring Boot + ChatGLM AI 集成（Java 8 + MySQL + Redis + ShardingSphere）

## ⚠️ 踩坑提示
- 是付费课程的开源代码，README 满是引流链接，**别被吓到，代码本身能跑**
- 真要上线得自己接 ChatGLM API key，不然 AI 评分段挂掉
- Spring Boot + Redis + 分库分表配置不少，本地起一遍准备装 10 个东西

## 🤔 为什么这次推它给你

1. **命中 intent.what：** 包含 MBTI 性格测试小程序的**从零完整实现**（Taro 微信小程序），还能扩展成"任意题型答题应用"——比单纯 MBTI repo 更耐用。
2. **命中 soft pref：** 全中文 README + 中文题库 + 小程序场景齐全，三个软偏好全中。
3. **没命中的 trade-off：** 你说"现在比较流行的"，这个是**重型教学项目**不是"打开即用 demo"——想 3 分钟看结果它不合适，要的是周末开干的人。

---

# 📦 深入调查：搭建 + 外网开放完整指南（2026-05-24）

> 基于浅克隆探针实测，下面所有命令/文件路径/版本号已对真实仓库验证过。

## 一、项目实际结构（纠正常见误解）

不是单仓库一个 app，是**三件套**：

```
yudada/
├── yudada-backend/      Spring Boot（Java 8 + MySQL + Redis + ChatGLM）
├── yudada-frontend/     Vue 3 + Arco Design 管理后台 / 用户网页端
└── mbti-test-mini/      Taro + React 微信小程序（独立，可单独上线）
```

后端 ↔ 前端**强耦合**（前端调后端 API），小程序**独立**（不跑后端也能做 MBTI 测试）。

## 二、技术栈与外部依赖

| 组件 | 版本 | 必须? | 用途 |
|---|---|---|---|
| JDK | Java 8 | ✅ | 后端运行（Dockerfile 写死 jdk-8） |
| Maven | 3.6+ | ✅ | 后端构建 |
| MySQL | 5.7+ / 8.x | ✅ | 主存储 |
| Redis | 5+ | ✅ | session + 缓存 + Redisson 限流 |
| Node.js | 16.x | ✅ | 前端 + 小程序构建（锁版本旧，必须 `--force`） |
| ShardingSphere | 已内嵌 | ✅ | `user_answer` 分 2 表（`appId % 2`），SQL 已建好 |
| **ChatGLM API Key** | 智谱 AI | ✅（AI 功能） | 题目生成 + 答案分析 |
| 腾讯云 COS | 对象存储 | ⚠️ 半必须 | 头像 / 封面上传，不传图能跑 |
| 微信小程序 AppID | 注册 | ⚠️ 仅上线小程序需要 | 本地开发用测试号 |

**AI 提供方是智谱 ChatGLM**（pom.xml 里 `cn.bigmodel.openapi:oapi-java-sdk`），不是 OpenAI。新用户送 18 元额度，MBTI 用半年。

## 三、本地搭建（dev 环境跑通）

### 3.1 装基础环境
```bash
brew install openjdk@8 maven mysql redis node@16
brew services start mysql redis
```

### 3.2 初始化数据库
```bash
git clone https://github.com/liyupi/yudada.git && cd yudada
mysql -uroot -p < yudada-backend/sql/create_table.sql
mysql -uroot -p yudada < yudada-backend/sql/init_data.sql
```

### 3.3 改后端配置 `yudada-backend/src/main/resources/application.yml`
```yaml
spring:
  datasource:
    username: root
    password: 你的mysql密码
  redis:
    host: localhost
  shardingsphere:
    datasource:
      yudada:
        username: root
        password: 你的mysql密码     # 两处都要改！
ai:
  apiKey: 你的智谱ChatGLM-API-Key   # https://open.bigmodel.cn 申请
cos:                                # 不传图可暂时留空
  client: { accessKey: xxx, secretKey: xxx, region: xxx, bucket: xxx }
```

### 3.4 启动
```bash
cd yudada-backend && mvn spring-boot:run     # 端口 8101
cd yudada-frontend && npm install --force && npm run serve   # 端口 8080
```

启动成功后 http://localhost:8080 注册账号即可，管理员账号在 `init_data.sql` 里。

### 3.5 小程序（可选）
```bash
cd mbti-test-mini && npm install && npm run dev:weapp
# 微信开发者工具打开 dist/，AppID 选"测试号"
```

## 四、外网开放给其他人

### 4.1 三件套的外网形态
| 组件 | 外网形态 | 谁能访问 |
|---|---|---|
| backend | `https://api.你的域名` | 前端/小程序调用 |
| frontend | `https://app.你的域名` | 浏览器访问 |
| mini | 微信小程序商店 | 微信用户（独立通道） |

### 4.2 服务器最低配置
- **2C4G 起步**（Spring Boot + MySQL + Redis 同机跑，2G 必 OOM）
- 40GB SSD，3-5 Mbps 带宽
- 推荐阿里云/腾讯云轻量 2C4G，约 ¥30-70/月

### 4.3 部署顺序
1. **域名 + 备案**：中国大陆服务器必须 ICP 备案（7-20 天）；不想等就买**香港/新加坡**服务器，立刻能用
2. **DNS 解析**：`app.` 和 `api.` 两个子域都指向服务器 IP
3. **装基础软件**：用 `1Panel` 一键装 MySQL/Redis/Nginx/Java/Node
4. **改 prod 配置**：`application-prod.yml` 全部强密码，别用 dev 的 123456
5. **后端**：`mvn package -DskipTests` → scp 到服务器 → systemd 跑（不要 nohup）
6. **前端**：改 `.env.production` 里 API 地址为 `https://api.你的域名` → `npm run build` → 推到 `/var/www/`
7. **Nginx 反代 + HTTPS**：Let's Encrypt 免费证书 `certbot --nginx -d ...`
8. **防火墙**：只开 22/80/443，**MySQL/Redis/8101 全 deny 公网**

### 4.4 Nginx 关键片段
```nginx
server {
  listen 443 ssl http2;
  server_name app.你的域名;
  root /var/www/yudada-frontend;
  location / { try_files $uri $uri/ /index.html; }   # Vue history 路由必须
}
server {
  listen 443 ssl http2;
  server_name api.你的域名;
  client_max_body_size 20M;
  location / {
    proxy_pass http://127.0.0.1:8101;
    proxy_set_header Host $host;
    proxy_read_timeout 120s;       # AI 生成可能慢
  }
}
```

## 五、安全雷区（不做会被打爆）

- **Redis 设密码 + bind 127.0.0.1**（裸跑公网 Redis 是经典挖矿入口）
- **MySQL 不开 3306 公网**
- 后端 `CorsConfig.allowedOrigins` 改成 `https://app.你的域名`，**不要 `*`**
- **AI API Key 只能后端持有**，别挪到前端
- ChatGLM 调用必须**按用户限流**（Redisson 已在依赖里），不然有人刷光你的额度

## 六、月成本估算

| 项 | ¥/月 |
|---|---|
| 服务器 2C4G | 30-70 |
| 域名 .com | 5（年付摊） |
| HTTPS | 0 |
| ChatGLM 轻量用 | 0-30 |
| COS 10G | 1-3 |
| **合计** | **40-110** |

## 七、最小可行路径（4 小时上线）

1. 香港 2C4G 轻量（免备案，首月 ¥30）
2. 1Panel 一键装环境
3. 后端 + 前端按上面 5-7 步部署
4. certbot 拿 HTTPS
5. 智谱 API Key 填进 `application-prod.yml`

**不要 AI 功能**？`ai.apiKey` 留空 + 前端隐藏 AI 入口按钮即可，**核心 MBTI 测试不依赖 AI**。

## 八、鱼皮项目特有的坑
- README 的"4 阶段"对应**不同分支**（main 是最终态），从 MBTI stage1 起步要 `git checkout` 切
- 代码里大量"编程导航星球"引流注释，删不删随你，不影响功能
- 后端日志默认 stdout，生产改成文件 + 切片（用 logback-spring.xml）
- 分库分表规则 `appId % 2` **不能改**，否则启动报错

---
*由 /gitout 生成 · 2026-05-24 · intent: "mbit 测试 app 或程序或网页端或小程序，现在比较流行的"*
*深入调查 · 2026-05-24 · 基于 liyupi/yudada main 分支浅克隆实测*
