# Episode 03 Walkthrough — Raw CLI Is Not Network State

This is the production-ready recording guide for AVI v2 Episode 3.

## YouTube Package

Recommended title: **Raw CLI Is Not Network State | Building AVI Ep. 3**

Alternates:
- **Teach an AI Agent to Read Network State | AVI Ep. 3**
- **Turn pyATS Observations into Structured Network State | AVI Ep. 3**

Thumbnail text: **CLI ≠ STATE**

Core promise: normalize raw observations into explicit state objects while preserving source evidence.

Target runtime: **20–30 minutes**.

---

# Recording Run of Show

## 0:00–0:45 — Cold Open

> "A wall of CLI text is evidence, but it's a terrible interface for everything we want AVI to do next. Today we're teaching AVI the difference between raw observation and explicit network state."

Show the raw input dictionary, then the normalized JSON result.

## 0:45–2:00 — Trust Question

Slide: **Can AVI Describe Network State Without Guessing?**

```text
Raw Observation -> Normalizer -> Explicit State
                         |
                         +-> preserve evidence_id
```

> "I want AVI to normalize what it observed, but I do not want normalization to quietly become inference. Unknown data should stay unknown."

## 2:00–3:30 — Architecture

```text
pyATS / CLI
   -> raw evidence
      -> normalize_interface()
         -> InterfaceState
            -> human / agent context
```

## 3:30–5:00 — Starter Orientation

Open:

```text
episodes/03-state/avi_pilot_03_state.py
```

Run:

```bash
python episodes/03-state/avi_pilot_03_state.py
```

Focus on:
- `InterfaceState`
- `normalize_interface()`
- `main()`

## 5:00–9:00 — `InterfaceState`

Walk through the exact fields:

```python
class InterfaceState(BaseModel):
    device: str
    interface: str
    admin_status: str
    operational_status: str
    ip_address: str | None = None
    source: str
    evidence_id: str
    observed_at: str
```

Explain why `admin_status` and `operational_status` are separate.

Key line:

> "The schema is describing an observation, not deciding whether the interface is correct or healthy."

Point out `source`, `evidence_id`, and `observed_at` as provenance fields.

## 9:00–13:00 — `normalize_interface()`

Highlight:

```python
admin_status=raw.get("admin_status", "unknown")
operational_status=raw.get("oper_status", "unknown")
ip_address=raw.get("ip_address")
source=raw.get("source", "pyats")
```

> "Notice the difference between an explicit default like `unknown` and inventing a value. We are acknowledging missing information instead of pretending we observed it."

Then show:

```python
evidence_id=raw["evidence_id"]
```

> "The evidence reference survives normalization. That's how later state can remain traceable to the observation that created it."

## 13:00–16:00 — Happy-Path Demo

Run:

```bash
python episodes/03-state/avi_pilot_03_state.py
```

Point out the normalized field names and generated `observed_at` timestamp.

Explain that the starter uses a local fixture in `main()` so the lesson focuses on the normalization boundary rather than reconnecting to the lab.

## 16:00–19:00 — Break It on Purpose: Missing Data

Temporarily remove:

```python
"oper_status": "down",
"ip_address": "10.0.0.1",
```

Run again.

Show:
- `operational_status` becomes `unknown`,
- `ip_address` becomes `null`,
- AVI does not invent either value.

### What to say

> "Unknown is a valid operational answer. Guessing is not."

Restore the original fixture after the demo.

## 19:00–21:00 — Required vs Optional Evidence

Temporarily remove `evidence_id` and show that the current normalizer raises a key error because that field is required by this path.

Explain:

> "This is an early sign of why Episode 4 matters. Right now some structural expectations are implicit in Python access patterns. Next we make the contract formal and validate it deliberately."

## 21:00–22:30 — What AVI Still Cannot Do

AVI now has a normalized `InterfaceState`, but it still cannot:

- enforce allowed status vocabularies,
- validate richer logical relationships,
- guarantee every candidate object is structurally safe,
- scale observations across multiple devices.

## 22:30–24:00 — Homework

1. Add a second interface fixture.
2. Add a BGP-state model following the same provenance pattern.
3. Remove optional fields and confirm they remain explicit.
4. Preserve `evidence_id` for every state object.
5. Do not add decision logic about whether state is intended yet.

## 24:00–25:00 — Next Flight

```text
Episode 3:
Evidence -> Normalizer -> State

Episode 4:
Evidence -> Normalizer -> Candidate State -> Schema Validation
```

> "Episode 4 turns this convention into an enforceable contract. If AVI produces malformed or impossible structure, validation stops it before anything downstream trusts it."

---

# Recording Checklist

- [ ] Starter runs before recording.
- [ ] Missing-data demo is rehearsed.
- [ ] Original fixture is restored afterward.
- [ ] Explain `oper_status` -> `operational_status` mapping clearly.
- [ ] Do not imply normalization proves correctness or intent.

# Suggested Chapters

```text
00:00 Raw CLI is not network state
00:45 The trust question
02:00 State architecture
03:30 Episode 3 starter
05:00 InterfaceState explained
09:00 Building the normalizer
13:00 Normalized state demo
16:00 Missing data without guessing
19:00 Why formal validation comes next
21:00 What AVI still cannot do
22:30 Homework
24:00 Episode 4 tease
```

## Series takeaway

> **Evidence tells us what was collected. State gives that observation an explicit, consistent shape.**
