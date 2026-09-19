---
name: expert_mcp_architect
description: Triggers whenever Antigravity modifies or creates MCP tools, IPC logic, Zod schemas, or the Node.js WebSocket server layer.
---

# MCP Architecture Protocol (FAANG Standards)

You are tasked with generating elite, highly scalable Model Context Protocol (MCP) server code. The client requires zero-bottleneck communication between the LLM agent and the browser environment. Treat the MCP layer as a mission-critical router.

## 1. The Control/Data-Plane Split (Zero Memory Leaks)
JSON-RPC (via stdio) is incredibly inefficient for massive payloads. Extracting a 64MB DOM from LinkedIn will crash the Node server, lock the Event Loop, and OOM the LLM context window.
*   **Data Plane Isolation:** If a tool extracts a massive payload (e.g., >5MB), **DO NOT return it as a raw string inside the CallToolResult response**. You must write the payload to a local file cache (e.g., `data/snapshots/snapshot-123.html.gz`).
*   **Control Plane Descriptors:** Return a URI descriptor to the LLM agent: `{ "status": "success", "file_uri": "file:///path/to/snapshot-123.html.gz" }`. The agent will read this file locally using file-system tools.

## 2. Anti-Hallucination Schemas (Strict Types)
LLMs frequently hallucinate tool arguments if schemas rely on text descriptions (e.g., `"value is required if action is type"`).
*   **Zod Discriminated Unions:** You MUST use `z.discriminatedUnion` for any tool that has conditional branches (like `browser_act`). The schema must physically reject invalid combinations before hitting the tool execution layer.
*   **Strict String Typing:** Use `.min(1)` for required strings to prevent empty `""` passes. Use `.regex()` if the string expects a specific format.
*   **Descriptions as Code:** Keep Zod descriptions concise. Focus on *what* the field does, not *how* to bypass it.

## 3. Backpressure & Streaming Resilience
When the agent issues rapid commands or requests massive DOM updates, the WebSocket server can become overwhelmed.
*   **Asynchronous IPC:** Ensure `wsService.broadcast()` uses robust `async/await` patterns with timeouts. 
*   **Polling Limits:** When a Tool polls the Database waiting for an extension response (e.g., `pollCapture`), implement a strict timeout loop (e.g., max 15 seconds) to prevent infinite loops if the extension is disabled.
*   **Connection Dropping:** If the extension disconnects mid-poll, the service must detect the closed WebSocket and immediately reject the Promise, rather than waiting for the timeout.

## 4. Tool-to-Service Handoff (Domain Driven Design)
Files in `mcp-server/src/tools/` act exclusively as routing layers.
*   **The Controller Rule:** They must validate the Zod input, log the intent, and instantly call a method on a Domain Service (e.g., `BrowserService.executeAction()`).
*   **No SQL:** Never write raw logic or SQLite queries in the Tool file. 
*   **Error Masking:** Tools should catch deep internal service errors and translate them into clean, LLM-friendly error messages (e.g., translating a `SQLITE_BUSY` into `System is currently processing a large DOM, please retry in 2 seconds`).
