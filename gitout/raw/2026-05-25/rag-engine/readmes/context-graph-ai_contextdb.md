<p align="center">
  <img src="assets/banner.svg" alt="contextdb" width="800">
</p>

[![CI](https://github.com/context-graph-ai/contextdb/actions/workflows/ci.yml/badge.svg)](https://github.com/context-graph-ai/contextdb/actions/workflows/ci.yml)
[![Crates.io](https://img.shields.io/crates/v/contextdb-engine)](https://crates.io/crates/contextdb-engine)
[![License](https://img.shields.io/badge/license-Apache--2.0-blue)](LICENSE)
[![docs.rs](https://docs.rs/contextdb-engine/badge.svg)](https://docs.rs/contextdb-engine)

# contextdb

An embedded database for agentic memory systems. Relational storage, graph traversal, and vector similarity search under unified MVCC transactions — in a single file, in a single process. Every agent, device, or service runs its own contextdb. They sync bidirectionally through a central server over WebSocket — knowledge learned by one becomes available to all, with per-table conflict resolution. No port forwarding, no VPN — WebSocket traverses NAT out of the box.

If you're building agent memory today, you're probably stitching together SQLite for state, a vector database for embeddings, and application code for graph traversal. contextdb replaces all three — and adds **enforceable policy constraints** (state machines, DAG enforcement, cascading propagation) that the database guarantees, not application code.

```
contextdb> UPDATE decisions SET status = 'draft' WHERE id = '550e8400...';
Error: invalid state transition: active -> draft
```

No triggers. No application-side validation. The database enforces it.

**Familiar conventions, nothing new to learn:** PostgreSQL-compatible SQL, [pgvector](https://github.com/pgvector/pgvector) syntax for vector search (`<=>`), and [SQL/PGQ](https://www.iso.org/standard/76120.html)-style `GRAPH_TABLE ... MATCH` for graph queries — the subset that matters for bounded traversal, not the full standard.

**Language support:** contextdb is a Rust library and CLI today. Python and TypeScript bindings are on the roadmap — contributions welcome.

**Website:** [contextdb.tech](https://contextdb.tech) · **Docs:** [contextdb.tech/docs](https://contextdb.tech/docs/)

See [Why contextdb?](docs/why-contextdb.md) for the full problem statement, or jump to [Getting Started](docs/getting-started.md) to try it in 2 minutes.

## Why Not SQLite + Extensions?

| Capability | SQLite + extensions | contextdb |
|---|---|---|
| Vector search | sqlite-vec (separate extension, no unified transactions with relational data) | Built-in, auto-HNSW at 1K vectors, pre-filtered search, same MVCC transaction as rows |
| Graph traversal | Recursive CTEs (unbounded, no cycle detection) | SQL/PGQ with bounded BFS, DAG enforcement, typed edges |
| State machines | CHECK constraints + triggers (bypassable) | `STATE MACHINE` in DDL, enforced by the database engine |
| Atomic cross-model updates | Application-level coordination | Single MVCC transaction across relational + graph + vector |
| Sync | Build your own | Bidirectional collaborative sync — each database syncs changesets with conflict resolution, not WAL pages |
| Immutable tables | Not enforceable (triggers are bypassable) | `IMMUTABLE` keyword, enforced by the database engine |
| Cascading invalidation | Application code | `PROPAGATE` in DDL — state changes cascade along edges and FKs |

## Use It As a Library

contextdb is an embedded database. The primary interface is the Rust API:

```rust
use contextdb_engine::Database;
use std::collections::HashMap;
use std::sync::Arc;

let db = Database::open(std::path::Path::new("./my.db"))?;
// or: Database::open_memory() for ephemeral

let params = HashMap::new();

db.execute(
    "CREATE TABLE observations (
       id UUID PRIMARY KEY,
       data JSON,
       embedding VECTOR(384)
     ) IMMUTABLE",
    &params,
)?;

// Insert with parameters
let mut params = HashMap::new();
params.insert("id".into(), Value::Uuid(uuid::Uuid::new_v4()));
params.insert("data".into(), Value::Json(serde_json::json!({"type": "sensor"})));
params.insert("embedding".into(), Value::Vector(vec![0.1; 384]));

db.execute(
    "INSERT INTO observations (id, data, embedding) VALUES ($id, $data, $embedding)",
    &params,
)?;

// Vector similarity search
let mut query_params = HashMap::new();
query_params.insert("query".into(), Value::Vector(vec![0.1; 384]));

let result = db.execute(
    "SELECT id, data FROM observations ORDER BY embedding <=> $query LIMIT 10",
    &query_params,
)?;

// Graph traversal
let result = db.execute(
    "SELECT target_id FROM GRAPH_TABLE(
       edges MATCH (a)-[:DEPENDS_ON]->{1,3}(b)
       WHERE a.id = $start
       COLUMNS (b.id AS target_id)
     )",
    &params,
)?;

// Subscribe to commits
let rx = db.subscribe();
// rx is a std::sync::mpsc::Receiver<CommitEvent>
```

### One Query, Three Subsystems

Find semantically similar observations within a graph neighborhood, filtered by relational predicates — a query that would take ~40 lines of Python across SQLite, ChromaDB, and a hand-rolled BFS:

```sql
WITH neighborhood AS (
  SELECT b_id FROM GRAPH_TABLE(
    edges MATCH (start)-[:RELATES_TO]->{1,3}(related)
    WHERE start.id = $entity_id
    COLUMNS (related.id AS b_id)
  )
),
candidates AS (
  SELECT o.id, o.data, o.embedding
  FROM observations o
  INNER JOIN neighborhood n ON o.entity_id = n.b_id
  WHERE o.observation_type = 'config_change'
)
SELECT id, data FROM candidates
ORDER BY embedding <=> $query_embedding
LIMIT 5
```

One query. One transaction. One process.

Add to your `Cargo.toml`:

```toml
[dependencies]
contextdb-engine = "1.0.0"
contextdb-core = "1.0.0"
```

## Install

```bash
# Install the CLI
cargo install contextdb-cli

# Or run the server (no clone needed)
curl -O https://raw.githubusercontent.com/context-graph-ai/contextdb/main/docker-compose.yml
curl -O https://raw.githubusercontent.com/context-graph-ai/contextdb/main/nats.conf
docker compose up
```

## Or Explore With the CLI

```bash
cargo build --release -p contextdb-cli
./target/release/contextdb-cli :memory:
```

```
contextdb> CREATE TABLE decisions (id UUID PRIMARY KEY, status TEXT NOT NULL)
           STATE MACHINE (status: draft -> [active, rejected], active -> [superseded]);
ok (rows_affected=0)

contextdb> INSERT INTO decisions VALUES ('550e8400-e29b-41d4-a716-446655440000', 'draft');
ok (rows_affected=1)

contextdb> UPDATE decisions SET status = 'active' WHERE id = '550e8400-e29b-41d4-a716-446655440000';
ok (rows_affected=1)

contextdb> UPDATE decisions SET status = 'draft' WHERE id = '550e8400-e29b-41d4-a716-446655440000';
Error: invalid state transition: active -> draft

contextdb> .schema decisions
CREATE TABLE decisions (
  id UUID NOT NULL PRIMARY KEY,
  status TEXT NOT NULL
)
STATE MACHINE (status: active -> [superseded], draft -> [active, rejected])
```

### Two-Vector Walkthrough

```sql
CREATE TABLE evidence (id UUID PRIMARY KEY, vector_text VECTOR(4), vector_vision VECTOR(8));
INSERT INTO evidence (id, vector_text, vector_vision) VALUES
  ('11111111-1111-1111-1111-111111111111', [1,0,0,0], [0,1,0,0,0,0,0,0]);
SHOW VECTOR_INDEXES;
SELECT id FROM evidence ORDER BY vector_text <=> '[1,0,0,0]' LIMIT 1;
```

Each `VECTOR(N)` column is its own index, keyed by `(table, column)`. Use
`VECTOR(N) WITH (quantization = 'F32'|'SQ8'|'SQ4')` to choose the per-column
storage footprint; omitted quantization defaults to `F32`.

### Upgrading From 0.3.x

Opening a legacy vector store without the named-index format marker returns
`LegacyVectorStoreDetected`. For teams upgrading from 0.3.x, recovery is
explicit: sync from a peer already on the named-index storage format, or
recreate the schema and reimport the data.

## What It Does

**Relational (PostgreSQL-compatible SQL)** — SELECT, INSERT, UPDATE, DELETE, JOINs (INNER/LEFT), CTEs, upsert (`ON CONFLICT DO UPDATE`), DISTINCT, LIMIT, IN with subqueries, LIKE, BETWEEN, parameter binding (`$name`).

**Graph (SQL/PGQ-style)** — `GRAPH_TABLE(... MATCH ...)` following SQL/PGQ conventions for 
