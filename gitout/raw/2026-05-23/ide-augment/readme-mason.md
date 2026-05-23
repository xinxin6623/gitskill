![Linux](https://img.shields.io/badge/Linux-%23.svg?logo=linux&color=FCC624&logoColor=black)
![macOS](https://img.shields.io/badge/macOS-%23.svg?logo=apple&color=000000&logoColor=white)
![Windows](https://img.shields.io/badge/Windows-%23.svg?logo=windows&color=0078D6&logoColor=white)
[![GitHub CI](https://github.com/mason-org/mason.nvim/workflows/Tests/badge.svg)](https://github.com/mason-org/mason.nvim/actions?query=workflow%3ATests+branch%3Amain+event%3Apush)
[![Sponsors](https://img.shields.io/github/sponsors/williamboman)](https://github.com/sponsors/williamboman)

<h1>
    <img src="https://user-images.githubusercontent.com/6705160/177613416-0c0354d2-f431-40d8-87f0-21310f0bba0e.png" alt="mason.nvim" />
</h1>

<p align="center">
    Portable package manager for Neovim that runs everywhere Neovim runs.<br />
    Easily install and manage LSP servers, DAP servers, linters, and formatters.<br />
</p>
<p align="center">
    <code>:help mason.nvim</code>
</p>
<p align="center">
    <sup>Latest version: v2.3.0</sup> <!-- x-release-please-version -->
</p>

## Table of Contents

-   [Introduction](#introduction)
-   [Installation & Usage](#installation--usage)
    - [Recommended setup for `lazy.nvim`](#recommended-setup-for-lazynvim)
-   [Requirements](#requirements)
-   [Commands](#commands)
-   [Registries](#registries)
-   [Screenshots](#screenshots)
-   [Firewall (socket.dev)](#firewall-socketdev)
-   [Configuration](#configuration)

## Introduction

> [`:h mason-introduction`][help-mason-introduction]

`mason.nvim` is a Neovim plugin that allows you to easily manage external editor tooling such as LSP servers, DAP servers,
linters, and formatters through a single interface. It runs everywhere Neovim runs (across Linux, macOS, Windows, etc.),
with only a small set of [external requirements](#requirements) needed.

Packages are installed in Neovim's data directory ([`:h standard-path`][help-standard-path]) by default. Executables are
linked to a single `bin/` directory, which `mason.nvim` will add to Neovim's PATH during setup, allowing seamless access
from Neovim builtins (LSP client, shell, terminal, etc.) as well as other 3rd party plugins.

For a list of all available packages, see <https://mason-registry.dev/registry/list>.

## Installation & Usage

> [`:h mason-quickstart`][help-mason-quickstart]

Install using your plugin manager of choice. **Setup is required**:

```lua
require("mason").setup()
```

`mason.nvim` is optimized to load as little as possible during setup. Lazy-loading the plugin, or somehow deferring the
setup, is not recommended.

Refer to the [Configuration](#configuration) section for information about which settings are available.

### Recommended setup for `lazy.nvim`

The following is the recommended setup when using `lazy.nvim`. It will set up the plugin for you, meaning **you don't have
to call `require("mason").setup()` yourself**.

```lua
{
    "mason-org/mason.nvim",
    opts = {}
}
```

## Requirements

> [`:h mason-requirements`][help-mason-requirements]

`mason.nvim` relaxes the minimum requirements by attempting multiple different utilities (for example, `wget`,
`curl`, and `Invoke-WebRequest` are all perfect substitutes).
