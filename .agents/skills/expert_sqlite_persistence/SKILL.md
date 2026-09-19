---
name: expert_sqlite_persistence
description: Triggers whenever Antigravity modifies database logic, SQLite schemas, migrations, or the CaptureService layer.
---

# SQLite Persistence Protocol (FAANG Standards)

You are tasked with generating elite, high-throughput Database architecture. The system relies on SQLite to handle massive concurrent telemetry blasts from the Chrome Extension.

## 1. The WAL Mandate
Under heavy load, standard SQLite encounters `SQLITE_BUSY` (Database is locked) exceptions when multiple reads/writes happen simultaneously (e.g., the extension flooding the MCP server with DOM deltas while the LLM agent is querying profiles).
*   **The Mandate:** SQLite MUST be initialized with `PRAGMA journal_mode = WAL;` (Write-Ahead Logging) and `PRAGMA synchronous = NORMAL;`.
*   **Connection Pooling:** Ensure the SQLite connection is treated as a singleton service to prevent file lock contention.

## 2. Transaction Atomicity
Complex operations (e.g., scoring a profile and saving a field map, or bulk-updating posting statuses) require multiple SQL insertions.
*   **The Mandate:** If an operation requires multiple inserts/updates, wrap them in a `db.transaction()`. If one step fails, the entire transaction MUST roll back cleanly to prevent orphaned data.
*   Never use raw `db.run()` for multi-step logic.

## 3. Repository Pattern Isolation
Never leak raw SQL strings into the MCP Tool definitions or WebSocket IPC routers.
*   **The Mandate:** All DB logic must be contained within `mcp-server/src/services/` or a dedicated `repositories/` layer. 
*   The presentation/tool layer must only call high-level semantic methods (e.g., `CaptureService.logRequest()`).
*   Always use parameterized queries (`?`) to prevent SQL injection vulnerabilities, even for internal telemetry.

## 4. Non-Blocking Migrations
When adding new columns (e.g., a new `site_id` field) to an active production database, naive schema drops will destroy data.
*   **The Mandate:** Use graceful `ALTER TABLE ADD COLUMN` statements wrapped in `try/catch` blocks. If a column already exists, the migration should silently succeed rather than crashing the active MCP server boot cycle.
*   Always test schema integrity upon server start using `PRAGMA table_info()`.
