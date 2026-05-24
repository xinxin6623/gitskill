> **This project is no longer maintained.**
>
> causantic is archived as of May 2026. Claude Code's native memory has since matured and covers the same ground for most use cases. The code remains available for reference but will not receive updates, fixes, or support.

# Causantic

[![npm version](https://img.shields.io/npm/v/causantic)](https://www.npmjs.com/package/causantic)
[![CI](https://github.com/Entrolution/causantic/actions/workflows/ci.yml/badge.svg)](https://github.com/Entrolution/causantic/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Node.js](https://img.shields.io/badge/node-%3E%3D20-brightgreen)](https://nodejs.org)
[![Claude Code](https://img.shields.io/badge/Claude_Code-%3E%3D5.1-blueviolet)](https://docs.anthropic.com/en/docs/claude-code)
[![TypeScript](https://img.shields.io/badge/TypeScript-native-blue)](https://www.typescriptlang.org/)

**Long-term memory for Claude Code — local-first, graph-augmented, self-benchmarking.**

No cloud. No data leaves your machine. Runs entirely on your hardware with optional per-chunk encryption. An optional Anthropic API key enables cluster topic labeling via Haiku — all core retrieval works without it.

<p align="center">
<strong>Long-term episodic memory for Claude Code</strong><br/>
<sub>Local-first · Keyword-first retrieval · Causal chain walking · Structural repo map</sub>
</p>

## Quick Start

```bash
# Install
npm install causantic

# Initialize (creates dirs, configures MCP, offers to import sessions)
npx causantic init

# Query memory
npx causantic recall "authentication flow"

# Launch the dashboard
npx causantic dashboard
```

## Who Is This For?

Developers using Claude Code who want their AI assistant to **remember across sessions**. When you switch projects, return after a weekend, or need context from three sessions ago, Causantic retrieves the right history automatically.

## Why Causantic?

Most AI memory systems use vector embeddings for similarity search. Causantic takes a different approach — **keyword-first (BM25) retrieval** as the default, a **causal graph** that tracks _relationships_ between memory chunks, a **structural repo map** for code orientation, and **session state capture** for instant resumption. Vector search and HDBSCAN clustering are available as optional enrichment.

|                                      | Vector Search Only | Causantic                                         |
| ------------------------------------ | ------------------ | ------------------------------------------------- |
| **Finds lexically relevant content** | No                 | Yes (BM25 keyword search — default)               |
| **Finds similar content**            | Yes                | Yes (optional vector enrichment)                  |
| **Finds related context**            | No                 | Yes (causal edges)                                |
| **Structural code orientation**      | No                 | Yes (repo map — definitions, references, ranking) |
| **Session continuity**               | No                 | Yes (session state capture + briefing mode)        |
| **Temporal awareness**               | Wall-clock decay   | Episodic chain walking                            |
| **Context augmentation**             | 1×                 | **2.46×** (chain walking adds episodic narrative) |
| **Handles project switches**         | Breaks continuity  | Preserves causality                               |
| **Bidirectional queries**            | Forward only       | Backward + Forward                                |

### How It Compares

| System        |  Local-First  |  Temporal Decay   |  Graph Structure   | Structural Map | Self-Benchmarking |
| ------------- | :-----------: | :---------------: | :----------------: | :------------: | :---------------: |
| **Causantic** |    **Yes**    | **Chain walking** |  **Causal graph**  |   **Yes**      |      **Yes**      |
| Mem0          |  No (Cloud)   |       None        |    Paid add-on     |      No        |        No         |
| Cognee        | Self-hostable |       None        | Triplet extraction |      No        |        No         |
| Letta/MemGPT  | Self-hostable |   Summarization   |        None        |      No        |        No         |
| Zep           |  Enterprise   |    Bi-temporal    |    Temporal KG     |      No        |        No         |
| GraphRAG      | Self-hostable |   Static corpus   |    Hierarchical    |      No        |        No         |

See [Landscape Analysis](docs/research/approach/landscape-analysis.md) for detailed per-system analysis.

## Key Differentiators

**1. Local-First with Encryption**
All data stays on your machine. Optional per-chunk encryption (ChaCha20-Poly1305) with keys stored in your system keychain. No cloud dependency.

**2. Keyword-First Retrieval**
BM25 keyword search (FTS5) is the default retrieval method — fast, precise, and excellent for function names, error codes, and specific terms. Vector search is available as optional enrichment for semantic similarity. Both can fuse via Reciprocal Rank Fusion (RRF) when hybrid mode is enabled.

**3. Structural Repo Map**
Codebase analysis extracts definitions, references, and cross-file relationships. Produces a compact structural summary (~1K tokens) ranked by importance. Gives Claude Code instant orientation without reading individual files. **22 languages**: 12 via tree-sitter (TS, JS, Python, Java, C, C++, Rust, Go, Ruby, C#, PHP, Bash) and 10 via regex fallback (Scala, Kotlin, Swift, Haskell, Lua, Dart, Zig, Elixir, Perl, R).

**4. Session Continuity**
Structured session state capture (files touched, errors, outcomes, tasks, LLM summary) enables instant resumption. The `reconstruct` tool's briefing mode combines session state with the repo map for a complete startup context.

**5. Causal Graph with Multi-Path Chain Walking**
Chunks are connected in a sequential linked list — intra-turn chunks chained sequentially, inter-turn edges linking last→first, cross-session edges bridging sessions. The `recall` tool walks this graph backward to reconstruct episodic narratives (augmented with session summaries); `predict` walks forward. Multi-path DFS explores alternatives and selects the best chain by median cosine similarity.

**6. Self-Benchmarking Suite**
Measure how well your memory system is working with built-in benchmarks. Health, retrieval quality, chain quality, and latency — scored and tracked over time with specific tuning recommendations.

## Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                     Claude Code Session                          │
└─────────────────────────────┬───────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                      Hook System                                 │
│  ┌──────────────┐  ┌──────────────┐  ┌─────────────┐            │
│  │session-start │  │ session-end  │  │ pre-compact │            │
│  └──────────────┘  └──────────────┘  └─────────────┘            │
│  ┌──────────────────────┐                                        │
│  │ claudemd-generator   │                                        │
│  └──────────────────────┘                                        │
└─────────────────────────────┬───────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                    Ingestion Pipeline                            │
│  ┌──────────┐  ┌──────────┐  ┌────────────┐  ┌──────────────┐   │
│  │  Parser  │→ │ Chunker  │→ │ Edge       │→ │ Session      │   │
│  │          │  │          │  │ Creator    │  │ State        │   │
│  └──────────┘  └──────────┘  └────────────┘  └──────────────┘   │
│  ┌──────────────┐  (optional: embedding when embeddingEager=true)│
│ 
