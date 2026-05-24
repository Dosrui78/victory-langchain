# 🚀 Victory LangChain: 从入门到实战的开源教程

[![Python Version](https://img.shields.io/badge/python-3.13+-blue.svg)](https://www.python.org/)
[![LangChain Version](https://img.shields.io/badge/LangChain-v0.3+-green.svg)](https://github.com/langchain-ai/langchain)
[![Package Manager](https://img.shields.io/badge/manager-uv-orange.svg)](https://github.com/astral-sh/uv)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> 这是一个旨在帮助开发者快速掌握 LangChain 框架的开源教程。无论你是 AI 开发新手，还是想要查漏补缺的资深开发者，这里都有你需要的实战干货。

---

## 🌟 教程简介

`Victory LangChain` 是我在复习 LangChain 框架时顺手整理的一份实战指南。LangChain 目前正处于高速发展阶段，版本迭代非常快。本教程将紧跟社区步伐，使用现代化的开发工具和最新的 API 实践。

### 核心前提
- **语言平台**: Python 3.13+
- **框架版本**: 基于 LangChain v0.3.x (持续更新中)
- **大模型**: 默认使用 OpenAI 系列模型 (支持自定义 Provider)
- **包管理**: 全面采用现代化的 **uv** 进行依赖管理

---

## 🛠️ 环境配置 & uv 使用指南

本项目使用 [uv](https://github.com/astral-sh/uv) 进行依赖管理。`uv` 是由 Astral 开发的极速 Python 包管理器，性能远超 pip。

### 1. 安装 uv
如果你还没有安装 `uv`，可以通过以下命令快速安装：

```powershell
# Windows (PowerShell)
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 2. 初始化环境
克隆项目后，在根目录下运行以下命令来同步环境：

```bash
# 同步依赖并创建虚拟环境 (.venv)
uv sync
```

### 3. 常用 uv 命令
在本教程的开发过程中，你可能会用到以下命令：

- **运行脚本**: `uv run main.py` (自动在虚拟环境中执行)
- **添加依赖**: `uv add langchain-openai`
- **移除依赖**: `uv remove some-package`
- **查看依赖树**: `uv tree`

---

## 📚 教程大纲 (Roadmap)

本教程分为以下几个阶段，带你由浅入深：

| 章节 | 主题 | 核心内容 |
| :--- | :--- | :--- |
| 🟢 第一阶段 | **基础入门** | Model, Prompt, Output Parsers |
| 🟡 第二阶段 | **核心组件** | Chains (LCEL), Memory, Document Loaders |
| 🔴 第三阶段 | **进阶应用** | RAG (检索增强), Vector Stores, Embeddings |
| 🟣 第四阶段 | **智能体** | Agents, Tools, LangGraph 简介 |
| 🚀 第五阶段 | **项目部署** | LangServe, Streamlit 集成 |

---

## ⚙️ 快速开始

1. **设置 API Key**:
   在根目录下创建 `.env` 文件，并添加你的 OpenAI API 密钥：
   ```env
   OPENAI_API_KEY=your_sk_key_here
   OPENAI_BASE_URL=https://api.openai.com/v1  # 可选，如果使用代理
   ```

2. **运行第一个示例**:
   ```bash
   uv run main.py
   ```

---

## 🤝 参与贡献

欢迎通过 Issue 提交你的建议，或者直接发起 Pull Request！

1. Fork 本项目
2. 创建你的特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交你的更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 发起 PR

---

## 📄 开源协议

本项目采用 [MIT License](LICENSE) 开源。

---

<p align="center">
  <i>如果这个教程对你有帮助，请点一个 ⭐ 鼓励一下吧！</i>
</p>
