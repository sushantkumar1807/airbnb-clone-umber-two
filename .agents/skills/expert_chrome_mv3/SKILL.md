---
name: expert_chrome_mv3
description: Triggers whenever Antigravity touches Chrome Extension files (content scripts, background scripts, DOM extractors, Event APIs).
---

# Chrome MV3 Extension Protocol (FAANG Standards)

You are tasked with generating elite, highly resilient Chrome MV3 extension code. Modern SPAs and MV3 constraints are highly hostile to naive automation. Treat the DOM as a hostile, constantly shifting environment.

## 1. Hardware-Level Synthesis (The PointerEvent Trap)
Raw `element.click()` or standard `MouseEvent` dispatches are ignored by React 17+ and Vue SyntheticEvent pools.
*   **The Mandate:** All automated clicks must synthesize the hardware sequence:
    1. `pointerover`
    2. `pointerenter`
    3. `pointerdown` (isPrimary: true)
    4. `mousedown`
    5. `pointerup`
    6. `mouseup`
    7. `.click()`
*   **Draft.js/Lexical Trap:** For text inputs, generic `Event('input')` is not enough. You must dispatch native `InputEvent` with correct `data` payloads. Never force `element.value = x` on a controlled React component.

## 2. Deep Shadow Penetration
`document.querySelectorAll` is completely blind to modern Web Components.
*   **The Mandate:** When generating interactive maps or extracting the DOM, you MUST use recursive `walkDOM` logic that strictly checks for `element.shadowRoot` and pierces it.
*   **Element Tracking:** Ensure that injected `data-mcp-id` attributes are unique across all shadow boundaries.

## 3. IPC Memory Leaks & V8 Crashes
Extension IPC (`chrome.runtime.sendMessage`) is highly volatile during massive DOM extraction.
*   **The Mandate:** Never leave a Promise unhandled on fire-and-forget telemetry. If you do not expect a response from a massive DOM delta payload, aggressively check and catch `chrome.runtime.lastError`.
*   Failing to do this will trigger "Message port closed" Unhandled Promise Rejections which will crash the V8 Engine during high-throughput DOM mutation events.

## 4. The 5-Minute Death Lifecycle
The background script (`background.ts`) is an ephemeral Service Worker in Manifest V3. It is aggressively terminated by Chrome after 5 minutes of inactivity.
*   **The Mandate:** Do not store critical state (like active socket IDs or ongoing extraction tasks) in memory variables. Sync all critical state to `chrome.storage.local`. Upon Service Worker boot, re-hydrate state seamlessly.
*   **Keep-Alive Hacks:** If a stream requires >5 minutes (e.g., continuous DOM recording), you must implement a keep-alive ping mechanism.

## 5. Cross-Origin Strategies (FAANG Sandbox)
Content Scripts injected into the Main World cannot interact with elements inside cross-origin iframes (e.g., Stripe, OAuth popups).
*   **The Mandate:** Recognize when an element is inside a restricted iframe. Instead of crashing, gracefully log the boundary limit, or implement proxy injection techniques via `chrome.debugger` APIs if explicitly requested by the user. Do not attempt `iframe.contentDocument` on a CORS-locked frame.
