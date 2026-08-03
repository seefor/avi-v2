# Episode 04 Walkthrough — Validate Before You Trust Agent Output

This is the production-ready recording guide for AVI v2 Episode 4.

## YouTube Package

Recommended title: **Validate Before You Trust AI Agent Output | Building AVI Ep. 4**

Alternates:
- **JSON Is Not a Contract — Validate Your AI Agent | AVI Ep. 4**
- **Use Pydantic to Stop Bad Agent Output | AVI Ep. 4**

Thumbnail text: **VALIDATE IT**

Core promise: convert plausible-looking structured output into an enforceable contract with deterministic failures.

Target runtime: **20–30 minutes**.

---

# Recording Run of Show

## 0:00–0:45 — Cold Open

> "JSON that looks right is not the same thing as data another system should trust. Today AVI gets a real contract: required fields, allowed values, field constraints, and logical validation."

Flash the valid BGP object, then the controlled validation failure.

## 0:45–2:00 — Trust Question

Slide: **Can Another System Consume AVI Output Without Reading It Like a Human?**

```text
Candidate State -> Validation -> Valid Object
                        |
                        +-> STOP
```

## 2:00–3:30 — Architecture

Explain that validation checks structure and rules; it does not prove the observation itself is true.

> "A schema can tell us the object is well formed. It cannot tell us the router actually reported this state. That still comes from evidence."

## 3:30–5:00 — Starter Orientation

Open:

```text
episodes/04-structure/avi_pilot_04_structure.py
```

Run:

```bash
python episodes/04-structure/avi_pilot_04_structure.py
```

Focus on:
- `BGPNeighbor`
- `BGPSummary`
- `established_not_greater_than_total()`
- `main()`

## 5:00–8:00 — `BGPNeighbor`

Highlight:

```python
class BGPNeighbor(BaseModel):
    ip: str
    state: Literal["Established", "Idle", "Active", "Connect", "unknown"]
    prefixes: int = Field(ge=0)
```

Explain:
- required `ip`,
- allowed state vocabulary,
- non-negative prefix count.

Key line:

> "This is how we stop a plausible but unsupported status string from silently moving downstream."

## 8:00–12:00 — `BGPSummary`

Walk through:

```python
schema_version: str = "1.0"
device: str
total_peers: int = Field(ge=0)
established_peers: int = Field(ge=0)
neighbors: list[BGPNeighbor]
evidence_id: str
```

Explain why `schema_version` matters once multiple tools and clients depend on the object.

Then highlight the model validator:

```python
@model_validator(mode="after")
def established_not_greater_than_total(self):
    if self.established_peers > self.total_peers:
        raise ValueError("established_peers cannot exceed total_peers")
```

> "Types are not enough. Sometimes the invalid condition is the relationship between two perfectly valid integers."

## 12:00–15:00 — Happy-Path Demo

Run the starter and show the valid JSON.

Point out:
- default schema version,
- nested neighbor validation,
- evidence reference,
- deterministic shape.

## 15:00–18:00 — Built-In Failure Demo

The starter already creates:

```python
invalid = {**valid, "established_peers": 3}
```

with `total_peers` still equal to 2.

Run it and show the controlled `ValidationError`.

### What to say

> "This is exactly what I want. Bad state doesn't get fixed, guessed at, or quietly passed through. It stops."

## 18:00–21:00 — Break It Again: Unsupported Value

Temporarily change a neighbor state from:

```python
"Idle"
```

to:

```python
"Broken"
```

Run again and show the `Literal` validation failure.

Restore the valid fixture afterward.

## 21:00–22:30 — What Validation Does Not Prove

Slide:

```text
VALID SHAPE != TRUE OBSERVATION
VALID SHAPE != CORRECT INTENT
VALID SHAPE != SAFE CHANGE
```

> "Validation is one control in a chain. It does not replace evidence, context, verification, or approval."

## 22:30–24:00 — What AVI Still Cannot Do

AVI can validate one structured observation, but it still cannot:

- safely summarize a fleet,
- preserve partial-failure detail across devices,
- choose which information belongs in model context.

## 24:00–25:30 — Homework

1. Add a new valid BGP state intentionally.
2. Create one unsupported-state fixture.
3. Add a logical rule comparing neighbor count with `total_peers`.
4. Confirm failures stop before downstream use.

## 25:30–26:30 — Next Flight

```text
Validated State -> One Device
             ↓
Episode 5: Bounded Multi-Device Observation
```

> "Episode 5 leaves the comfort of one device. AVI will observe a small fleet without letting one unreachable target erase or distort everything else."

---

# Recording Checklist

- [ ] Valid and invalid starter paths both run.
- [ ] Unsupported-value demo is rehearsed.
- [ ] Fixture is restored after recording.
- [ ] Make clear that Pydantic validates contracts, not truth.

# Suggested Chapters

```text
00:00 JSON is not a contract
00:45 The trust question
02:00 Validation architecture
03:30 Episode 4 starter
05:00 BGPNeighbor schema
08:00 BGPSummary schema
12:00 Valid structured output
15:00 Logical validation failure
18:00 Rejecting invented values
21:00 What validation does not prove
22:30 What AVI still cannot do
24:00 Homework
25:30 Episode 5 tease
```

## Series takeaway

> **If another system is going to trust AVI's output, the contract must be enforceable in code.**
