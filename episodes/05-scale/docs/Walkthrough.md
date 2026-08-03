# Episode 05 Walkthrough — What Changes When AVI Looks at Multiple Devices?

This is the production-ready recording guide for AVI v2 Episode 5.

## YouTube Package

Recommended title: **What Changes When an AI Agent Watches Multiple Network Devices? | AVI Ep. 5**

Alternates:
- **Scale a Network AI Agent Without Hiding Failures | AVI Ep. 5**
- **From One Router to a Fleet: Bounded AI Observation | AVI Ep. 5**

Thumbnail text: **ONE DEVICE IS EASY**

Core promise: observe several targets concurrently while preserving per-device status, evidence, and partial failures.

Target runtime: **25–35 minutes**.

---

# Recording Run of Show

## 0:00–0:45 — Cold Open

> "One-device demos hide the hard part. In a real network, one device is healthy, one is degraded, and one times out at exactly the wrong moment. Today AVI has to look at all three without pretending the fleet is either all good or all bad."

Flash the final JSON counts:

```json
{"healthy": 1, "degraded": 1, "unreachable": 1}
```

## 0:45–2:00 — Trust Question

Slide: **Can AVI Summarize a Fleet Without Erasing Per-Device Truth?**

```text
Inventory
   -> bounded runner
       -> lab-r1
       -> lab-r2
       -> lab-r3
   -> rollup + detail
```

## 2:00–3:30 — Safety Boundary

> "Scale does not earn AVI broader permissions. We are changing how many approved targets we observe, not what AVI is allowed to do to them."

Call out bounded concurrency as a control rather than a performance trick.

## 3:30–5:00 — Starter Orientation

Open:

```text
episodes/05-scale/avi_pilot_05_scale.py
```

Run:

```bash
python episodes/05-scale/avi_pilot_05_scale.py
```

Focus on:
- `DEVICES`
- `observe()`
- `run_batch()`
- `main()`

## 5:00–8:00 — Inventory Fixture

Show:

```python
DEVICES = {
    "lab-r1": {"status": "healthy", "evidence_id": "evt-101"},
    "lab-r2": {"status": "degraded", "evidence_id": "evt-102"},
    "lab-r3": {"status": "unreachable", "evidence_id": "evt-103"},
}
```

Explain that this episode uses simulated device results so the lesson stays focused on fleet coordination.

> "The important pattern is that target scope comes from an inventory, not from the model inventing hostnames."

## 8:00–11:00 — `observe()`

Highlight:

```python
def observe(device: str) -> dict:
    result = DEVICES[device]
    if result["status"] == "unreachable":
        return {"device": device, **result, "error": "connection timeout"}
    return {"device": device, **result, "error": None}
```

Key point:

> "Unreachable is represented explicitly. We do not convert 'I couldn't observe it' into 'healthy,' and we do not crash the whole fleet summary."

## 11:00–16:00 — `run_batch()` and Bounded Concurrency

Show:

```python
with ThreadPoolExecutor(max_workers=max_workers) as pool:
```

Explain:
- bounded worker count,
- futures per device,
- `as_completed()` means results can finish in any order,
- sorting restores a predictable output order.

Then show:

```python
counts = {"healthy": 0, "degraded": 0, "unreachable": 0}
```

and the final return object containing both counts and full device detail.

### What to say

> "A rollup should help me see the fleet. It should never replace the individual device facts that explain the rollup."

## 16:00–19:00 — Happy-Path Mixed Fleet Demo

Run:

```bash
python episodes/05-scale/avi_pilot_05_scale.py
```

Read the output in this order:

1. requested device count,
2. fleet counts,
3. per-device details,
4. evidence IDs,
5. explicit error on `lab-r3`.

## 19:00–22:00 — Break It on Purpose

Temporarily add a fourth device:

```python
"lab-r4": {"status": "unreachable", "evidence_id": "evt-104"},
```

Run again.

Show that:
- other results still appear,
- unreachable count increases,
- each target remains visible.

Restore the fixture afterward.

Optional experiment: run with `max_workers=1` inside `main()` to explain the difference between concurrency and correctness.

## 22:00–24:00 — What the Starter Does Not Yet Simulate

Be explicit:

> "This starter labels an unreachable device instead of waiting on a real network timeout. In a hardened implementation, per-device connection timeout handling belongs inside the actual tool execution path."

This keeps the walkthrough aligned with the code.

## 24:00–25:30 — What AVI Still Cannot Do

AVI can now produce more data than before. It still cannot decide:

- which device results matter to the current question,
- how old observations may be,
- what context should be excluded,
- how much information the model should receive.

## 25:30–27:00 — Homework

1. Add a fourth target.
2. Change `max_workers` and compare output behavior.
3. Add a new `status` category and update the rollup deliberately.
4. Preserve evidence IDs for every target.
5. Do not flatten per-device details into counts only.

## 27:00–28:00 — Next Flight

```text
Episode 5:
Many Observations
      ↓
Episode 6:
Context Selection
```

> "AVI can collect more information now. The next problem is deciding what it should actually see. Episode 6 is context engineering for network operations."

---

# Recording Checklist

- [ ] Mixed fleet output is clean and readable.
- [ ] Fourth-device failure demo is rehearsed.
- [ ] Fixture restored after recording.
- [ ] Clearly state this starter simulates status instead of making live multi-device calls.
- [ ] Explain bounded concurrency as an operational control.

# Suggested Chapters

```text
00:00 Why one-device demos are easy
00:45 The fleet trust question
02:00 Scale without broader permissions
03:30 Episode 5 starter
05:00 Inventory-driven targeting
08:00 Per-device observation
11:00 Bounded concurrency
16:00 Mixed fleet demo
19:00 Partial failure demo
22:00 What this starter simulates
24:00 What AVI still cannot do
25:30 Homework
27:00 Episode 6 tease
```

## Series takeaway

> **Fleet summaries should reduce cognitive load without erasing the evidence underneath them.**
