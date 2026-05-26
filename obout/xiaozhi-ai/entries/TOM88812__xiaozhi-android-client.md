---
type: repo
repo: TOM88812/xiaozhi-android-client
domain: xiaozhi-ai
status: active
discovered: 2026-05-23
last_reviewed: 2026-05-23
intent_matched: "xiaozhi 同类型 — 移动端 (Flutter iOS/Android)"
signals:
  stars: 1477
  last_commit: 2026-03-24
  language: Dart
  license: Apache-2.0
url: https://github.com/TOM88812/xiaozhi-android-client
absorption:
  harvested: false
  used: false
  used_in: []
---

# xiaozhi-android-client · 小白说明书

## 🧐 这是什么
Flutter 写的 xiaozhi 移动端客户端，iOS 和 Android 双平台通吃，还支持 Dify 流式对话和回音消除。

## 💡 解决什么问题
- 没带 ESP32 盒子出门也想用 xiaozhi
- 想直接在手机上接自建的 xiaozhi 服务器
- 想要一个跨平台的对话 App 模板

## 🎯 谁该用 / 谁别用
**适合你如果：**
- 想做 xiaozhi 的移动端入口
- 熟悉 Flutter / 想抄一份现成 AEC 实现
- 已经部署了 xiaozhi-server 想给手机端开通访问

**别浪费时间如果：**
- 你是纯硬件党，根本不需要手机端
- 只用 iOS native，不想碰 Flutter
- 想要原生 Kotlin/Swift（这是 Flutter 单源码）

## 🚀 三分钟上手
```bash
git clone https://github.com/TOM88812/xiaozhi-android-client
cd xiaozhi-android-client
flutter pub get
flutter run             # 跑设备/模拟器
# 进 App 后填后端地址即可
```

## 🔑 关键文件 / 关键概念
- Flutter 单源码 → iOS + Android 双端
- 支持 Dify 流式对话
- iOS/安卓回音消除（AEC）已实现

## ⚠️ 踩坑提示
- iOS 真机调试需要 Apple 开发者证书
- 最后一次大更新是三月，比固件/server 更新慢
- 文档 Wiki 在 wiki.lhht.cc，部分链接需翻墙

## 🤔 为什么这次推它给你
xiaozhi 同类型生态里少数同时覆盖 iOS+Android 的客户端，1.5k 星、Apache-2.0 商用更友好、社区维护中。trade-off：最近 2 个月更新略慢，不如固件/Python server 那么频繁，但功能已经够全。

---
*由 /gitout 生成 · 2026-05-23 · intent: "搜一组关于 xiaozhi ai 相关的同类型项目"*
