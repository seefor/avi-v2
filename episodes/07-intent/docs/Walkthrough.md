# Episode 07 Walkthrough — NetBox vs. Live Network State

This is the production-ready recording guide for AVI v2 Episode 7.

## YouTube Package

Recommended title: **NetBox vs. Live Network State: What Should AI Trust? | AVI Ep. 7**

Alternates:
- **Source of Truth vs. Operational State for AI Agents | AVI Ep. 7**
- **Teach an AI Agent to Detect Network Drift | AVI Ep. 7**

Thumbnail text: **INTENT vs REALITY**

Core promise: compare intended state and observed state without treating either source as automatically correct.

Target runtime: **30–40 minutes**.

---

# Recording Run of Show

## 0:00–0:50 — Cold Open

> "A device can be up and still be wrong. NetBox can say what we intended and still be stale. Today AVI learns one of the most important ideas in network automation: intended state and observed state are different things."

Flash one `drift` result and one `unmanaged` result.

## 0:50–2:15 — Trust Question

Slide: **Can AVI Compare Intent and Operation Without Treating Either as Infallible?**

```text
INTENT ------------------+
                         +-> compare_intent() -> finding
OBSERVED ----------------+
```

> "The comparator should report the relationship between two sources. It should not silently decide which side gets to rewrite the other."

## 2:15–4:00 — Architecture

```text
NetBox-style intended state
          ↓
   compare_intent()
          ↑
pyATS-style observed state
          ↓
match / drift / unmanaged / unknown
```

Mention that this starter uses local dictionaries representing those sources so the episode focuses on comparison semantics.

## 4:00–5:30 — Starter Orientation

Open:

```text
episodes/07-intent/avi_pilot_07_intent.py
```

Run:

```bash
python episodes/07-intent/avi_pilot_07_intent.py
```

Focus on:
- `compare_intent()`
- `intended` fixture
- `observed` fixture
- the two demo calls in `main()`

## 5:30–10:00 — `compare_intent()` Missing-Source Rules

Start with:

```python
if intent is None:
    return {"status": "unmanaged", "intent": None, "observed": observed}
```

### What to say

> "No intent record does not mean the observed value is wrong. In this starter we call that `unmanaged`."

Then:

```python
if observed is None:
    return {"status": "unknown", "intent": intent, "observed": None}
```

> "And if intended state exists but we have no observation, AVI says `unknown`. Missing observation is not drift."

## 10:00–14:00 — Provenance and Comparison

Walk through:

```python
"intent_source": intent.get("source", "netbox"),
"intent_record_id": intent.get("record_id"),
"observed_source": observed.get("source", "pyats"),
"evidence_id": observed.get("evidence_id"),
```

Then:

```python
"expected": expected,
"observed": actual,
"status": "match" if expected == actual else "drift",
```

### Key line

> "A drift finding is useful because it preserves both sides: what we expected, what we observed, and where those values came from."

## 14:00–17:00 — Demo Case 1: Drift

The existing fixture intentionally uses:

```python
intended value = True
observed value = False
```

Run the starter and show the `drift` result.

### What to say

> "This is a review finding. It is not an instruction to enable the interface. We still do not know why the difference exists or which side is stale."

## 17:00–19:00 — Demo Case 2: Unmanaged

The existing second call is:

```python
compare_intent(None, observed)
```

Show `status: unmanaged`.

Explain why this is operationally different from drift.

## 19:00–22:00 — Break It on Purpose: Missing Observation

Temporarily add:

```python
print(json.dumps(compare_intent(intended, None), indent=2))
```

Run again and show:

```text
status: unknown
```

### What to say

> "AVI cannot compare what it hasn't observed. Unknown is more honest than manufacturing a drift conclusion."

Remove or keep the extra demo call deliberately after recording.

## 22:00–25:00 — Add a Match Case

Temporarily create:

```python
observed_match = {"field": "interface_enabled", "value": True, "source": "pyats", "evidence_id": "evt-202"}
```

Call:

```python
compare_intent(intended, observed_match)
```

Show `status: match`.

Now viewers have seen all four starter outcomes available from the current comparison logic:

- `match`
- `drift`
- `unmanaged`
- `unknown`

## 25:00–27:00 — What This Starter Does Not Yet Model

Be explicit:

- no live NetBox API call yet,
- no intent freshness/version conflict logic yet,
- no `stale` status in this starter,
- no remediation.

> "The architecture will eventually care about stale or ambiguous intent, but I don't want to pretend the Episode 7 starter already solves that."

## 27:00–29:00 — Safety Boundary

Slide:

```text
DRIFT != DEVICE IS WRONG
DRIFT != NETBOX IS RIGHT
DRIFT != PERMISSION TO CHANGE
```

> "AVI's job here is to make disagreement visible and traceable. Human and later reasoning layers decide what that disagreement means."

## 29:00–31:00 — What AVI Still Cannot Do

AVI can now compare intent and observation. It still cannot:

- retrieve runbooks or standards,
- cite operational knowledge,
- distinguish live evidence from retrieved guidance inside a reasoning workflow.

## 31:00–32:30 — Homework

1. Add a second comparison field.
2. Add a match case.
3. Add missing-observation behavior.
4. Add timestamps/version metadata to intended state.
5. Preserve intent record ID and observed evidence ID in every finding.

## 32:30–33:30 — Next Flight

```text
Observed State + Intended State
             +
      Operational Knowledge
             ↓
            RAG
```

> "Episode 8 gives AVI runbooks and operational knowledge through RAG. The challenge is making that guidance useful without confusing a document with live network truth."

---

# Recording Checklist

- [ ] Default drift and unmanaged cases run.
- [ ] Match and missing-observation demos are rehearsed.
- [ ] Do not claim the starter has live NetBox integration.
- [ ] Do not claim stale-intent detection is implemented yet.
- [ ] Reinforce that drift is a finding, not authorization.

# Suggested Chapters

```text
00:00 A device can be up and still be wrong
00:50 The intent trust question
02:15 Architecture
04:00 Episode 7 starter
05:30 Missing intent vs missing observation
10:00 Preserving provenance
14:00 Drift demo
17:00 Unmanaged state
19:00 Unknown observation demo
22:00 Match demo
25:00 What this starter does not model yet
27:00 Drift is not authorization
29:00 What AVI still cannot do
31:00 Homework
32:30 Episode 8 tease
```

## Series takeaway

> **Source of truth tells us intent. The network tells us operational state. A trustworthy system keeps those concepts separate.**
