# Episode 06 Walkthrough — What Should AVI Actually See?

This is the production-ready recording guide for AVI v2 Episode 6.

## YouTube Package

Recommended title: **What Context Should an AI Network Agent Actually See? | AVI Ep. 6**

Alternates:
- **Context Engineering for Network Operations | AVI Ep. 6**
- **More Data Can Make Your AI Agent Worse | AVI Ep. 6**

Thumbnail text: **MORE DATA ≠ BETTER**

Core promise: build a context assembler that includes relevant, current observations while excluding unrelated, stale, or sensitive data.

Target runtime: **25–35 minutes**.

---

# Recording Run of Show

## 0:00–0:45 — Cold Open

> "AVI can collect more data now, and that creates a new problem. If I dump every device, every old observation, and every note into the prompt, I haven't built context engineering. I've built noise."

Show the final `included` and `excluded` arrays.

## 0:45–2:00 — Trust Question

Slide: **Can AVI Get Enough Context Without Getting Everything?**

```text
Question + Observations -> Context Policy -> Included / Excluded
```

> "The goal is not the smallest prompt. It's the smallest sufficient operational context."

## 2:00–3:30 — Architecture

```text
Question
   + observations
        -> assemble_context()
             |- include relevant/current
             `- exclude unrelated/stale/sensitive
                    -> curated context
```

## 3:30–5:00 — Starter Orientation

Open:

```text
episodes/06-context/avi_pilot_06_context.py
```

Run:

```bash
python episodes/06-context/avi_pilot_06_context.py
```

Focus on:
- `assemble_context()`
- the `observations` fixture in `main()`

## 5:00–10:00 — `assemble_context()`

Walk through the exact filters in order:

```python
if item.get("device") != device:
    reason = "unrelated device"
elif age > timedelta(minutes=max_age_minutes):
    reason = "stale observation"
elif item.get("sensitive"):
    reason = "sensitive context"
```

### What to say

> "This is policy in code. We're making the inclusion decision inspectable instead of hoping the model ignores irrelevant information."

Point out that excluded items retain a reason:

```python
excluded.append({"item": item["id"], "reason": reason})
```

> "Exclusion is part of the evidence. I want to know not only what AVI saw, but why something was intentionally left out."

## 10:00–13:00 — Explain the Fixture

Show:

- `obs-1`: current BGP state on `lab-r1`
- `obs-2`: current state on the wrong device
- `obs-3`: two-hour-old data for the correct device

Explain the default policy:

```python
max_age_minutes: int = 15
```

## 13:00–16:00 — Happy-Path Demo

Run the starter.

Read the result in this order:

1. question,
2. selected device,
3. included context,
4. excluded context and reasons,
5. policy.

Show that only `obs-1` is included.

## 16:00–19:00 — Break It on Purpose: Sensitive Context

Temporarily add:

```python
{"id": "obs-4", "device": "lab-r1", "kind": "config", "value": "secret-like-data", "observed_at": now.isoformat(), "sensitive": True}
```

Run again.

Show that `obs-4` appears under `excluded` with:

```text
sensitive context
```

Restore the fixture afterward.

## 19:00–21:00 — Staleness Experiment

Temporarily call:

```python
assemble_context(..., max_age_minutes=180)
```

Show that the previously stale `obs-3` becomes eligible.

### Teaching point

> "Freshness is policy, not a universal constant. Fifteen minutes might make sense for one operational decision and be wrong for another."

Restore the default policy afterward.

## 21:00–23:00 — What This Starter Does Not Do Yet

Be explicit:

- no model call is required,
- no token counting is implemented yet,
- no topology expansion is implemented yet,
- the starter demonstrates deterministic inclusion/exclusion policy.

> "Before optimizing tokens, I want the source-selection rules to be understandable."

## 23:00–24:30 — What AVI Still Cannot Do

AVI can curate observed context, but it still does not know what the network is supposed to look like.

It cannot yet:

- compare observation with intent,
- label drift,
- distinguish missing intent from operational mismatch.

## 24:30–26:00 — Homework

1. Add a `kind` allowlist.
2. Make `max_age_minutes` configurable by context type.
3. Add a sensitive observation and verify exclusion.
4. Print exclusion reasons for every rejected item.
5. Do not silently drop missing sources.

## 26:00–27:00 — Next Flight

```text
Observed State -> Context
                    +
                  Intent
                    ↓
             Drift Comparison
```

> "Episode 7 adds the other half of the operational picture: intended state. We'll compare NetBox-style intent with live observed state without assuming either source is automatically correct."

---

# Recording Checklist

- [ ] Default starter output includes only `obs-1`.
- [ ] Sensitive-context failure demo is rehearsed.
- [ ] Staleness experiment is restored afterward.
- [ ] Do not claim token budgets are implemented in this starter.
- [ ] Explain inclusion and exclusion as deterministic application policy.

# Suggested Chapters

```text
00:00 More data is not better context
00:45 The context trust question
02:00 Context architecture
03:30 Episode 6 starter
05:00 Building context policy
10:00 The observation fixture
13:00 Curated context demo
16:00 Excluding sensitive context
19:00 Staleness policy
21:00 What this starter does not do yet
23:00 What AVI still cannot do
24:30 Homework
26:00 Episode 7 tease
```

## Series takeaway

> **The context window is not a junk drawer. The application should decide what the model needs for this decision.**
