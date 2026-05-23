# py-xiaozhi

<p align="center" class="trendshift">
  <a href="https://trendshift.io/repositories/14130" target="_blank">
    <img src="https://trendshift.io/api/badge/repositories/14130" alt="Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/>
  </a>
</p>
<p align="center">
  <a href="https://github.com/huangjunsen0406/py-xiaozhi/releases/latest">
    <img src="https://img.shields.io/github/v/release/huangjunsen0406/py-xiaozhi?style=flat-square&logo=github&color=blue" alt="Release"/>
  </a>
  <a href="https://opensource.org/licenses/MIT">
    <img src="https://img.shields.io/badge/License-MIT-green.svg?style=flat-square" alt="License: MIT"/>
  </a>
  <a href="https://github.com/huangjunsen0406/py-xiaozhi/stargazers">
    <img src="https://img.shields.io/github/stars/huangjunsen0406/py-xiaozhi?style=flat-square&logo=github" alt="Stars"/>
  </a>
  <a href="https://github.com/huangjunsen0406/py-xiaozhi/releases/latest">
    <img src="https://img.shields.io/github/downloads/huangjunsen0406/py-xiaozhi/total?style=flat-square&logo=github&color=52c41a1&maxAge=86400" alt="Download"/>
  </a>
  <a href="https://gitee.com/huang-jun-sen/py-xiaozhi">
    <img src="https://img.shields.io/badge/Gitee-FF5722?style=flat-square&logo=gitee" alt="Gitee"/>
  </a>
  <a href="https://huangjunsen0406.github.io/py-xiaozhi/guide/00_%E6%96%87%E6%A1%A3%E7%9B%AE%E5%BD%95.html">
    <img alt="Usage Docs" src="https://img.shields.io/badge/Usage Docs-View-blue?labelColor=2d2d2d" />
  </a>
  <a href="https://atomgit.com/huangjunsen0406/py-xiaozhi">
    <img src="./assets/AtomGit.svg" alt="AtomGit" height="20"/>
  </a>
</p>

English | [简体中文](README.zh.md)

## About

py-xiaozhi is a lightweight, cross-platform multi-modal AI interaction framework built on Python's async architecture. It supports real-time voice streaming, vision-language tasks, and IoT device control. Deployable across Windows, macOS, Linux desktops, and ARM embedded platforms (Raspberry Pi, Horizon Robotics RDK, Jetson Nano), it bridges the gap between Large Language Models and physical hardware — out of the box.

> Evolved from the [xiaozhi-esp32](https://github.com/78/xiaozhi-esp32) firmware project. Officially adopted by [D-Robotics (xiaozhi-in-rdk)](https://github.com/D-Robotics/xiaozhi-in-rdk) as an upstream dependency.

## Related Projects

- [xiaozhi-desktop](https://xiaozhi.junsen.online) — Electron desktop client with AEC echo cancellation, Live2D, floating window modes, and Windows / macOS installers

## Demo

- [Bilibili Demo Video](https://www.bilibili.com/video/BV1HmPjeSED2/#reply255921347937)

![Image](./documents/docs/guide/images/系统界面.png)

## Key Features

- **Real-time Voice AI** — Opus codec with auto frame detection (RFC 6716 TOC parsing), async streaming, sub-20ms latency
- **Multi-modal Vision** — Camera capture + vision-language model integration for image understanding and scene perception
- **MCP Tool Ecosystem** — Modular JSON-RPC 2.0 tool server: music player, camera, screenshot, app management, weather, volume control
- **Cross-platform Deployment** — Windows 10+ / macOS 10.15+ / Linux (x86_64 & ARM), optimized for Raspberry Pi and edge boards
- **Multiple UI Modes** — PySide6 + QML GUI / CLI / GPIO, adapting to desktop, headless server, and embedded environments
- **Offline Wake Word** — Sherpa-ONNX based on-device keyword spotting with custom wake word support
- **IoT & Embodied AI Ready** — GPIO interface for robotics control, hardware actuation, and sensor integration
- **WebSocket / MQTT** — Dual protocol communication with WSS/TLS encrypted transmission and auto-reconnection
- **Plugin Architecture** — Event-driven async design, clean dependency injection, extensible plugin system

## System Requirements

### Basic Requirements

- **Python Version**: 3.9 - 3.12
- **Operating System**: Windows 10+, macOS 10.15+, Linux
- **Audio Devices**: Microphone and speaker devices
- **Network Connection**: Stable internet connection (for AI services and online features)

### Recommended Configuration

- **Memory**: At least 4GB RAM (8GB+ recommended)
- **Processor**: Modern CPU with AVX instruction set support
- **Storage**: At least 2GB available disk space (for model files and cache)
- **Audio**: Audio devices supporting 16kHz sampling rate

### Optional Feature Requirements

- **Voice Wake-up**: Requires downloading Sherpa-ONNX speech recognition models
- **Camera Features**: Requires camera device and OpenCV support

## Read This First

- Carefully read [项目文档](https://huangjunsen0406.github.io/py-xiaozhi/) for startup tutorials and file descriptions
- The main branch has the latest code; manually reinstall pip dependencies after each update to ensure you have new dependencies

[Zero to Xiaozhi Client (Video Tutorial)](https://www.bilibili.com/video/BV1dWQhYEEmq/?vd_source=2065ec11f7577e7107a55bbdc3d12fce)

## Technical Architecture

### Core Architecture Design

- **Event-Driven Architecture**: Based on asyncio asynchronous event loop, supporting high-concurrency processing
- **Layered Design**: Clear separation of application layer, protocol layer, and UI layer
- **Dependency Injection**: Component lifecycle managed via bootstrap container
- **Plugin System**: Audio, UI, MCP tools and other components loaded via plugin system

### Key Technical Components

- **Audio Processing**: Opus codec, real-time resampling
- **Speech Recognition**: Sherpa-ONNX offline models, wake word recognition
- **Protocol Communication**: WebSocket/MQTT dual protocol support, encrypted transmission, auto-reconnection
- **Configuration System**: Hierarchical configuration, dot notation access, dynamic updates

### Performance Optimization

- **Async First**: Full system asynchronous architecture, avoiding blocking operations
- **Memory Management**: Smart caching, garbage collection
- **Audio Optimization**: 5ms low-latency processing, queue management, streaming transmission
- **Conc