---
type: repo
repo: huangjunsen0406/py-xiaozhi
domain: xiaozhi-ai
status: active
discovered: 2026-05-23
last_reviewed: 2026-05-23
intent_matched: "xiaozhi 同类型 — 无硬件纯 Python 客户端"
signals:
  stars: 3324
  last_commit: 2026-05-18
  language: Python
  license: MIT
url: https://github.com/huangjunsen0406/py-xiaozhi
absorption:
  harvested: false
  used: false
  used_in: []
---

# py-xiaozhi · 小白说明书

## 🧐 这是什么
Python 版的 xiaozhi 客户端 —— 没买 ESP32 板子也能在电脑上体验完整 xiaozhi AI 对话流程。

## 💡 解决什么问题
- 想先用电脑试一试 xiaozhi 体验，再决定要不要买硬件
- 不想焊电路，但想跑 AI 语音助手
- 想在 PC 上做 xiaozhi 协议的开发调试

## 🎯 谁该用 / 谁别用
**适合你如果：**
- Python 玩家，想"不买硬件先玩起来"
- 想拿它当参考实现来学 xiaozhi 通信协议
- 想在 Mac/Windows/Linux 桌面跑一个 AI 桌宠

**别浪费时间如果：**
- 你已经买了 ESP32，那直接刷原版固件更对
- 想要移动端体验（用 android-client）
- 想做企业部署（这是个人/桌面级项目）

## 🚀 三分钟上手
```bash
git clone https://github.com/huangjunsen0406/py-xiaozhi
cd py-xiaozhi
pip install -r requirements.txt
python main.py
# 也可以直接下 Release 的打包版本，免环境
```

## 🔑 关键文件 / 关键概念
- `main.py` — 客户端入口
- 文档站：huangjunsen0406.github.io/py-xiaozhi
- 配置文件里改后端地址 / 唤醒词

## ⚠️ 踩坑提示
- Windows 下麦克风权限要单独开
- 不同操作系统打包方式略有差异，看 Release 页对应平台版本
- 跟原版固件功能不是 100% 对齐，部分 MCP 工具调用受限

## 🤔 为什么这次推它给你
覆盖了"想体验 xiaozhi 但还没买硬件"的最大群体。MIT 协议、近 30 天活跃、3.3k 星且持续涨。trade-off：本质是客户端不是服务端，要配合一个 xiaozhi-server 才能完整运转，但作为入门快速试水极合适。

---
*由 /gitout 生成 · 2026-05-23 · intent: "搜一组关于 xiaozhi ai 相关的同类型项目"*
