# Episode 10 Walkthrough — Loops: Investigate Without Spinning Forever

## 1. Opening Hook

What to say:

"A useful network agent may need more than one tool call. The problem is not giving AVI a loop. The problem is teaching AVI when another loop is actually making progress—and when it needs to stop."

## 2. Trust Question

Can AVI continue an investigation without repeating the same failed idea forever?

## 3. Architecture

```text
Goal -> Gather -> Reason -> Act -> Verify -> Enough evidence?
                                          | yes -> Finish
                                          ` no  -> Progress check -> Continue / Escalate
```

## 4. Run the Starter

```bash
python episodes/10-loops/avi_pilot_10_loops.py
```

## 5. Explain the Loop State

Walk through:
- iteration number,
- current hypothesis,
- missing evidence,
- previous tool calls/arguments,
- elapsed time,
- failures,
- stopping reason.

## 6. Explain Hard Limits

Show the policy:
- max iterations,
- max tool calls,
- max runtime,
- duplicate-call limit,
- unresolved action.

What to say:

"The model does not get to decide how long the application runs."

## 7. Successful Two-Step Investigation

Run a scenario where the first observation reveals a second useful check, then AVI stops after enough evidence is collected.

## 8. Duplicate Call Demo

Cause a tool call to fail and have the next step request the same call with the same arguments.

Show duplicate detection.

## 9. Progress Detection

Explain the difference between:
- new evidence,
- changed hypothesis,
- repeated observation,
- repeated failure.

## 10. Escalation Demo

When evidence remains insufficient, stop with a clear unresolved/escalated result.

What to say:

"A bounded unresolved result is better than fake certainty and better than an agent that keeps hammering the same tool."

## 11. Break It on Purpose

Lower the iteration limit and show a clean stop reason.

## 12. What AVI Still Cannot Do

A loop can gather observations and propose a conclusion, but AVI still needs a separate verification step that asks whether the final claim is actually supported.

## 13. Homework

1. Change `max_iterations`.
2. Trigger duplicate detection.
3. Add one new termination reason.
4. Verify every stop produces an explicit final status.

## 14. Next Flight

"Episode 11 separates observations, hypotheses, and supported findings so AVI cannot turn a plausible story into a verified conclusion just because it sounds convincing."