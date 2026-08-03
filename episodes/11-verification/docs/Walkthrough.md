# Episode 11 Walkthrough — How Does AVI Know a Finding Is Actually Supported?

This is the production-ready recording guide for AVI v2 Episode 11.

## YouTube Package

Recommended title: **How Does an AI Agent Know Its Conclusion Is Supported? | AVI Ep. 11**

Alternates:
- **Stop AI Agents from Turning Guesses into Findings | AVI Ep. 11**
- **Verify AI Network Troubleshooting Claims with Evidence | AVI Ep. 11**

Thumbnail text: **PROVE THE FINDING**

Core promise: separate plausible hypotheses from evidence-supported findings with explicit evidence requirements and limitations.

Target runtime: **25–35 minutes**.

---

# Recording Run of Show

## 0:00–0:50 — Cold Open

> "AVI can investigate now, but an investigation can still end with a story that sounds right. Today we're going to make AVI prove the relationship between a claim and the evidence before we call that claim a finding."

Flash the first `unresolved` result and the second `supported` result.

## 0:50–2:15 — Trust Question

Slide: **Can AVI Distinguish a Plausible Explanation from a Supported Conclusion?**

```text
Evidence -> Claim -> Verification Rule -> Supported / Unresolved
```

> "Confidence should come from evidence quality and coverage, not from how confident the language sounds."

## 2:15–4:00 — Four Layers to Explain

Slide:

```text
OBSERVATION  = recorded fact
INFERENCE    = interpretation
HYPOTHESIS   = explanation to test
FINDING      = claim supported by required evidence
```

Make clear that the Episode 11 starter focuses on the last transition: candidate claim -> evidence requirement -> verification result.

## 4:00–5:30 — Starter Orientation

Open:

```text
episodes/11-verification/avi_pilot_11_verification.py
```

Run:

```bash
python episodes/11-verification/avi_pilot_11_verification.py
```

Focus on:
- `verify_claim()`
- `required_kinds`
- `bgp_only`
- `complete`

## 5:30–10:00 — `verify_claim()` Evidence Coverage

Show:

```python
available = {item["kind"] for item in evidence}
missing = sorted(required_kinds - available)
```

### What to say

> "The verifier is asking a deterministic question: which evidence categories does this claim require, and which of those categories are actually present?"

Then:

```python
supporting = [item["evidence_id"] for item in evidence if item["kind"] in required_kinds]
```

> "The final record doesn't just say supported. It carries the evidence references that earned that status."

## 10:00–13:00 — Unresolved Path

Highlight:

```python
if missing:
    return {
        "status": "unresolved",
        "confidence": "low",
        "evidence_refs": supporting,
        "limitations": [f"Missing evidence kinds: {', '.join(missing)}"],
    }
```

### Key line

> "Missing evidence becomes a limitation, not an invitation to fill in the blank."

## 13:00–16:00 — Supported Path

Show:

```python
return {
    "status": "supported",
    "confidence": "medium",
    "evidence_refs": supporting,
    "limitations": [],
}
```

Be explicit:

> "Medium confidence is hardcoded for this teaching starter. A production confidence model would need stronger rules around source quality, recency, corroboration, and contradictions."

## 16:00–19:00 — Demo 1: BGP Evidence Only

The claim is:

```text
BGP instability is related to interface reachability
```

Required kinds:

```python
{"bgp", "interface"}
```

First evidence set:

```python
bgp_only = [{"kind": "bgp", "evidence_id": "evt-301", "state": "Idle"}]
```

Run and show:

```text
status: unresolved
confidence: low
limitations: Missing evidence kinds: interface
```

## 19:00–22:00 — Demo 2: Add Interface Evidence

Show:

```python
complete = bgp_only + [{"kind": "interface", "evidence_id": "evt-302", "state": "down"}]
```

Run again.

Show:

```text
status: supported
confidence: medium
evidence_refs: evt-301, evt-302
```

### What to say

> "The status changed because the evidence changed. We didn't rewrite the prompt to sound more convincing."

## 22:00–25:00 — Break It on Purpose: Wrong Evidence Kind

Temporarily replace the interface evidence with:

```python
{"kind": "cpu", "evidence_id": "evt-302", "state": "high"}
```

Run again.

Show the claim returns to `unresolved` because the required `interface` evidence is still missing.

Restore the original fixture afterward.

### What to say

> "Having more evidence isn't the same thing as having evidence relevant to this claim."

## 25:00–27:00 — What This Verifier Does Not Prove

Be explicit:

- it verifies presence of required evidence kinds,
- it does not deeply inspect whether each evidence value logically proves causation,
- it does not detect contradictory evidence yet,
- `supported` here means the configured evidence requirements are satisfied.

This distinction is important for credibility.

## 27:00–29:00 — What AVI Still Cannot Do

AVI now has internal tool and verification patterns, but those tool contracts are still application-specific.

Next AVI needs:

- reusable tool exposure,
- typed protocol contracts,
- consistent behavior across clients,
- the same safety controls preserved across that boundary.

## 29:00–30:30 — Homework

1. Add a third required evidence kind.
2. Add irrelevant evidence and confirm it does not satisfy the claim.
3. Add contradiction handling.
4. Add evidence recency/source-quality rules.
5. Preserve limitations in every unresolved result.

## 30:30–31:30 — Next Flight

```text
AVI Safe Tools
      ↓
     MCP
      ↓
Multiple Clients
```

> "Episode 12 exposes AVI's narrow tools through MCP. The lesson isn't that MCP makes the tools safe. The lesson is how to preserve the controls when the tools become reusable."

---

# Recording Checklist

- [ ] Default unresolved and supported paths both run.
- [ ] Wrong-evidence-kind demo is rehearsed and restored.
- [ ] Do not overstate `supported` as causal certainty.
- [ ] Explain hardcoded confidence honestly.
- [ ] Keep evidence IDs visible on screen.

# Suggested Chapters

```text
00:00 A plausible story is not a finding
00:50 The verification trust question
02:15 Observation vs hypothesis vs finding
04:00 Episode 11 starter
05:30 Required evidence coverage
10:00 Unresolved claims
13:00 Supported claims
16:00 Missing interface evidence demo
19:00 Add supporting evidence
22:00 Wrong evidence kind demo
25:00 What this verifier does not prove
27:00 What AVI still cannot do
29:00 Homework
30:30 Episode 12 tease
```

## Series takeaway

> **A claim should earn its status from evidence, not from model confidence or persuasive language.**
