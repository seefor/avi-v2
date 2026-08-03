# Episode 07 Walkthrough — Intent: NetBox vs. Live Network State

## 1. Opening Hook

What to say:

"A device can be up and still be wrong. NetBox can say what we intended and still be stale. Today AVI learns one of the most important ideas in network automation: intended state and observed state are different things."

## 2. Trust Question

Can AVI compare intent and live operation without treating either source as infallible?

## 3. Architecture

```text
NetBox / intent source -----------+
                                  |
                                  v
                           Intent Comparator -> drift finding
                                  ^
                                  |
pyATS / observed state -----------+
```

## 4. Run the Starter

```bash
python episodes/07-intent/avi_pilot_07_intent.py
```

## 5. Explain Intent vs. Observation

What to say:

"NetBox tells us what we believe should exist. pyATS tells us what the device is doing right now. Neither automatically wins. AVI needs to preserve both sources and report the comparison."

## 6. Walk Through the Comparison Record

Show fields for:
- intent source and record identity,
- observed source and timestamp,
- comparison field,
- expected value,
- observed value,
- status,
- evidence references.

## 7. Demo Case 1 — Match

Show intended and observed state agreeing.

## 8. Demo Case 2 — Drift

Change one observed value and produce a drift finding.

What to say:

"Drift is a finding for review. It is not permission to configure the device."

## 9. Demo Case 3 — Missing Intent

Remove the intended-state record.

Show `unmanaged`, `unknown`, or equivalent rather than assuming a desired value.

## 10. Demo Case 4 — Stale/Ambiguous Intent

Mark the source stale or conflicting and show the comparator preserve that uncertainty.

## 11. Break It on Purpose

Make NetBox and observed state disagree on a field with poor source quality. Explain why AVI should not blindly "fix" the network to match NetBox.

## 12. Safety Boundary

The comparator creates a review artifact. It does not create an automatic remediation request.

## 13. What AVI Still Cannot Do

AVI can identify drift, but it does not yet know the operational runbooks and troubleshooting knowledge engineers use to decide what to inspect next.

## 14. Homework

1. Add a second comparison field.
2. Create a missing-intent case.
3. Add source version/date metadata.
4. Make sure every drift result retains both intent and observed provenance.

## 15. Next Flight

"Episode 8 adds RAG so AVI can retrieve runbooks and standards while keeping that knowledge separate from live network truth."