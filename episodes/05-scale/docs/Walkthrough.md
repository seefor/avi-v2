# Episode 05 Walkthrough — Scale: From One Device to a Small Fleet

## 1. Opening Hook

What to say:

"One-device demos hide the hard part. Real network operations means some devices are healthy, some are degraded, and one of them will time out at exactly the wrong moment. Today AVI learns to observe several targets without hiding partial failure."

## 2. Trust Question

Can AVI summarize multiple devices without flattening away the evidence that explains each result?

## 3. Architecture

```text
Inventory
   -> bounded batch runner
       -> device A -> evidence/state
       -> device B -> evidence/state
       -> device C -> timeout/error
   -> rollup summary + per-device detail
```

## 4. Run the Starter

```bash
python episodes/05-scale/avi_pilot_05_scale.py
```

## 5. Explain Inventory-Driven Targeting

Show how targets come from an inventory/list rather than being embedded in the model prompt.

What to say:

"The model should not be able to invent a hostname and suddenly expand its own scope."

## 6. Explain Bounded Concurrency

Discuss why parallel observations are useful, but unlimited concurrency is not.

Cover:
- max workers/tasks,
- per-device timeout,
- resource protection,
- predictable blast radius.

## 7. Mixed-Result Demo

Use the intended three-device shape:
- one healthy,
- one degraded,
- one unreachable.

Show the per-device evidence/state first.

## 8. Fleet Rollup

Then show the summary.

What to say:

"A rollup should help me see the fleet. It should not erase the individual device facts."

## 9. Partial Failure

Highlight that one timeout does not make the entire batch a failure and does not get silently treated as a healthy result.

## 10. Break It on Purpose

Force one target to fail or exceed its timeout.

Confirm:
- other targets complete,
- failed target is explicit,
- evidence remains per target,
- the rollup reports incomplete/degraded state honestly.

## 11. Safety Boundary

Scale does not earn broader permissions. Every device still passes through the same target and read-only policies.

## 12. What AVI Still Cannot Do

AVI can collect much more information now. The new danger is dumping all of it into the model. Episode 6 introduces deliberate context selection.

## 13. Homework

1. Add a fourth simulated target.
2. Change the concurrency limit.
3. Force one timeout.
4. Verify the final rollup preserves every per-device result.

## 14. Next Flight

"More data is not automatically better context. In Episode 6 we decide what AVI should actually see for one operational question—and what should stay out."