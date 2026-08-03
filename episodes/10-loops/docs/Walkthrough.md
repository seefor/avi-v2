# Episode 10 Walkthrough — Let the Agent Investigate Without Letting It Loop Forever

This is the production-ready recording guide for AVI v2 Episode 10.

## YouTube Package

Recommended title: **How to Build Safe Agent Loops for Network Troubleshooting | AVI Ep. 10**

Alternates:
- **Teach an AI Agent When to Stop Investigating | AVI Ep. 10**
- **Bounded Agent Loops: Gather, Check, Stop | AVI Ep. 10**

Thumbnail text: **WHEN SHOULD IT STOP?**

Core promise: let AVI perform multiple investigation steps while enforcing iteration, runtime, duplicate-call, and progress boundaries.

Target runtime: **30–40 minutes**.

---

# Recording Run of Show

## 0:00–0:50 — Cold Open

> "A useful network agent may need more than one observation. The dangerous part isn't giving it another tool call. The dangerous part is letting it keep calling tools without making progress."

Flash the successful two-step history and the `duplicate_call_no_progress` reason you will demo later.

## 0:50–2:15 — Trust Question

Slide: **Can AVI Continue an Investigation Without Repeating the Same Failed Idea Forever?**

```text
Gather -> Reason -> Act -> Verify
   ^                    |
   |                    v
Continue <--- Progress? ---> Stop / Escalate
```

## 2:15–4:00 — Architecture

Explain that the model may eventually influence which check comes next, but the loop controller owns how many times the application can run and why it stops.

> "The model does not get to decide how long the application runs."

## 4:00–5:30 — Starter Orientation

Open:

```text
episodes/10-loops/avi_pilot_10_loops.py
```

Run:

```bash
python episodes/10-loops/avi_pilot_10_loops.py
```

Focus on:
- `LoopController.__init__()`
- `LoopController.run()`
- `execute()`
- `main()`

## 5:30–8:00 — Hard Limits

Show:

```python
def __init__(self, max_iterations: int = 5, max_runtime_seconds: int = 10):
```

and:

```python
self.calls: list[tuple[str, tuple]] = []
```

Explain:
- iteration ceiling,
- runtime ceiling,
- call history for duplicate detection.

Be explicit that this starter does not yet have a separate `max_tool_calls` setting; one tool call occurs per iteration in the teaching sequence.

## 8:00–13:00 — `run()` Control Flow

Walk through the loop:

```python
for iteration in range(1, self.max_iterations + 1):
```

Runtime check:

```python
if time.monotonic() - started > self.max_runtime_seconds:
    return {"status": "stopped", "reason": "runtime_limit", ...}
```

Deterministic teaching sequence:

```python
call = ("bgp_status", ("lab-r1",)) if iteration == 1 else ("reachability", ("10.0.0.2",))
```

### What to say

> "Again, the starter keeps tool selection deterministic so we can inspect the control mechanics. The loop policy matters whether the next tool came from hardcoded logic or a model suggestion."

## 13:00–16:00 — Duplicate Detection

Highlight:

```python
if call in self.calls:
    return {"status": "escalated", "reason": "duplicate_call_no_progress", "history": history}
```

### What to say

> "Same tool, same arguments, no new condition: that's a strong signal that the investigation is not progressing."

## 16:00–19:00 — `execute()` and Enough Evidence

Show:

```python
if tool == "bgp_status":
    return {"state": "Idle", "enough_evidence": False}
if tool == "reachability":
    return {"reachable": False, "enough_evidence": True}
```

Explain the teaching sequence:

1. BGP Idle is observed.
2. That alone is not enough evidence.
3. Reachability check fails.
4. The fixture declares enough evidence for this demo.

Then:

```python
if result.get("enough_evidence"):
    return {"status": "complete", "reason": "enough_evidence", ...}
```

## 19:00–22:00 — Happy-Path Two-Step Demo

Run the starter.

Review:
- iteration 1 `bgp_status`,
- iteration 2 `reachability`,
- final `complete`,
- `reason: enough_evidence`,
- history retained.

### What to say

> "A loop should finish because a defined condition was met, not because the model got tired of calling tools."

## 22:00–25:00 — Break It on Purpose: Duplicate Call

Temporarily change the call-selection line so every iteration requests the same call:

```python
call = ("bgp_status", ("lab-r1",))
```

Run again.

Expected final result on the second iteration:

```text
status: escalated
reason: duplicate_call_no_progress
```

### What to say

> "This is the loop behavior I care about. AVI notices that repeating the same observation is not progress and exits instead of spinning forever."

Restore the original deterministic sequence afterward.

## 25:00–27:00 — Break It Again: Iteration Limit

Temporarily change the BGP result to never provide enough evidence and instantiate:

```python
LoopController(max_iterations=1)
```

Show:

```text
reason: iteration_limit
```

Restore the starter after recording.

## 27:00–29:00 — Runtime Limit Discussion

Explain why `time.monotonic()` is used for elapsed runtime measurement.

Do not force a long sleep into the final recording unless you want to demonstrate it. Show the code path and explain the control.

## 29:00–31:00 — What Progress Really Means

Slide:

```text
NEW TOOL CALL != PROGRESS
MORE TOKENS != PROGRESS
MORE ITERATIONS != PROGRESS

PROGRESS = new useful evidence or reduced uncertainty
```

Explain that the current starter uses simple duplicate detection and `enough_evidence`; later systems can make progress detection richer.

## 31:00–33:00 — What AVI Still Cannot Do

AVI can stop an investigation, but it still cannot prove that its final explanation is supported by evidence.

It needs to separate:

- observation,
- inference,
- hypothesis,
- supported finding,
- unresolved question.

## 33:00–34:30 — Homework

1. Change `max_iterations`.
2. Trigger `duplicate_call_no_progress`.
3. Add another explicit stopping reason.
4. Add a tool-call counter separate from iteration count.
5. Preserve the full history for every stop condition.

## 34:30–35:30 — Next Flight

```text
Investigation History
        ↓
Candidate Claim
        ↓
Verification Rules
        ↓
Supported / Unsupported / Unresolved
```

> "Episode 11 asks the question that agents often skip: just because AVI has a plausible explanation, does the evidence actually support it?"

---

# Recording Checklist

- [ ] Default two-step run ends with `enough_evidence`.
- [ ] Duplicate-call edit is rehearsed and restored.
- [ ] Iteration-limit edit is rehearsed and restored.
- [ ] Do not claim model-driven tool selection is implemented here.
- [ ] Explain current progress logic as intentionally simple.

# Suggested Chapters

```text
00:00 Why agent loops are risky
00:50 The loop trust question
02:15 Architecture
04:00 Episode 10 starter
05:30 Hard limits
08:00 Loop control flow
13:00 Duplicate detection
16:00 Enough evidence
19:00 Two-step investigation
22:00 Duplicate-call failure demo
25:00 Iteration-limit demo
27:00 Runtime limits
29:00 What counts as progress
31:00 What AVI still cannot do
33:00 Homework
34:30 Episode 11 tease
```

## Series takeaway

> **A bounded unresolved result is safer than an agent that keeps calling tools without making progress.**
