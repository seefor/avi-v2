# Episode 09 Walkthrough — The Model Is Not the Agent

This is the production-ready recording guide for AVI v2 Episode 9.

## YouTube Package

Recommended title: **The LLM Is Not the Agent — Build the Harness Around It | AVI Ep. 9**

Alternates:
- **Build an Agent Harness for Network Operations | AVI Ep. 9**
- **How to Put Real Controls Around an AI Agent | AVI Ep. 9**

Thumbnail text: **THE MODEL ISN'T THE AGENT**

Core promise: centralize tool authorization, run state, and deterministic orchestration behind an application harness.

Target runtime: **30–40 minutes**.

---

# Recording Run of Show

## 0:00–0:50 — Cold Open

> "At this point AVI has tools, evidence, state, validation, context, intent, and RAG. But if those are just disconnected demo scripts, we still don't have an agent architecture. Today the model stops being the center of the diagram."

Flash the `Harness` dataclass and the blocked `configure_device` result.

## 0:50–2:15 — Trust Question

Slide: **What Does the Application Control Independently of the Model?**

```text
MODEL SUGGESTS
      ↓
HARNESS DECIDES
      ↓
TOOLS EXECUTE
```

> "The model is one component. The agent is the controlled system around it."

## 2:15–4:00 — Architecture

```text
User
  ↓
Harness
  |- allowed tools
  |- run log
  |- deterministic decision path
  |- tool execution boundary
  `- policy block
```

Explain that the full AVI architecture will also own context, evidence, validation, and model calls. The Episode 9 starter intentionally keeps the decision deterministic so the harness boundary is visible.

## 4:00–5:30 — Starter Orientation

Open:

```text
episodes/09-harness/avi_pilot_09_harness.py
```

Run:

```bash
python episodes/09-harness/avi_pilot_09_harness.py
```

Focus on:
- `Harness`
- `execute_tool()`
- `run()`
- tool registry in `main()`

## 5:30–8:30 — The Tool Registry

Show:

```python
tools = {
    "device_status": lambda device: {"device": device, "status": "up"},
    "bgp_status": lambda device: {"device": device, "peer": "10.0.0.2", "state": "Idle"},
}
```

### What to say

> "AVI doesn't receive arbitrary Python functions. The application creates an explicit registry of capabilities that exist for this run."

> "A tool registry gives us a place to attach contracts, permissions, schemas, and evidence later."

## 8:30–13:00 — `execute_tool()`

Start with the block path:

```python
if name not in self.allowed_tools:
    event = {"tool": name, "status": "blocked", "arguments": kwargs}
    self.run_log.append(event)
    raise PermissionError(...)
```

### Key line

> "The prompt can remind the model about policy. The harness enforces policy."

Then show the success path:

```python
result = self.allowed_tools[name](**kwargs)
event = {"tool": name, "status": "success", "arguments": kwargs, "result": result}
self.run_log.append(event)
```

Explain that the run log is intentionally simple here and is not yet the durable Episode 2 evidence recorder.

## 13:00–16:30 — `run()`

Highlight:

```python
if "bgp" in request.lower():
    result = self.execute_tool("bgp_status", device="lab-r1")
else:
    result = self.execute_tool("device_status", device="lab-r1")
```

### What to say

> "There is no LLM making this decision in the starter. That is intentional. I want the orchestration boundary to be obvious before we make the decision source probabilistic."

Explain what changes later:

```text
Today: deterministic request routing
Later: model proposes a tool request
Always: harness validates the request
```

## 16:30–20:00 — Happy-Path Demo

Run:

```bash
python episodes/09-harness/avi_pilot_09_harness.py
```

Review the first result:

- incoming request,
- selected `bgp_status` tool,
- arguments,
- result,
- `run_log` event.

## 20:00–23:00 — Built-In Blocked Tool Demo

The starter already calls:

```python
harness.execute_tool("configure_device", device="lab-r1")
```

Show the output:

```text
Blocked by harness policy: Tool is not registered or allowed: configure_device
```

Then point back to `run_log` behavior in `execute_tool()`.

### What to say

> "This is the control I want to preserve even when a model is eventually choosing tools. The model should not be able to create a capability by naming it."

## 23:00–25:30 — Break It on Purpose: Different Request

Change the request from:

```text
Check BGP on lab-r1
```

to:

```text
Check device health on lab-r1
```

Run again and show deterministic selection of `device_status`.

Restore the original request afterward if desired.

## 25:30–28:00 — Architecture Gap: What Moves into `avi_core`

Show the `avi_core/` directory and explain the direction:

- stable tool contracts,
- evidence recorder,
- context assembler,
- validation models,
- policy,
- harness/run state.

Do not imply those components have all been migrated already.

## 28:00–30:00 — What AVI Still Cannot Do

AVI can orchestrate one deterministic pass, but it still cannot:

- investigate across multiple iterations,
- detect duplicate tool calls,
- recognize lack of progress,
- stop a looping investigation safely.

## 30:00–31:30 — Homework

1. Add one harmless tool to `allowed_tools`.
2. Call an unregistered tool and verify it cannot execute.
3. Add a simple target allowlist.
4. Add a unique run ID to the harness run log.
5. Keep the policy check inside `execute_tool()`.

## 31:30–32:30 — Next Flight

```text
Harness -> One Pass
             ↓
Harness -> Gather -> Reason -> Act -> Verify -> Stop/Continue
```

> "Episode 10 gives AVI a loop. The interesting part isn't letting it run again. The interesting part is proving that another iteration is making progress."

---

# Recording Checklist

- [ ] BGP request selects `bgp_status`.
- [ ] `configure_device` is blocked.
- [ ] Alternate request selects `device_status`.
- [ ] Do not claim the starter contains a real model call.
- [ ] Make the distinction between `run_log` and durable evidence clear.

# Suggested Chapters

```text
00:00 The model is not the agent
00:50 The harness trust question
02:15 Architecture
04:00 Episode 9 starter
05:30 Tool registry
08:30 Enforcing tool policy
13:00 Deterministic orchestration
16:30 Happy-path harness run
20:00 Blocking configure_device
23:00 Alternate request demo
25:30 Moving stable components into avi_core
28:00 What AVI still cannot do
30:00 Homework
31:30 Episode 10 tease
```

## Series takeaway

> **The model can suggest behavior. The harness owns capability, policy, and execution.**
