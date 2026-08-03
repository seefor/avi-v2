# Episode 10 — Loops

## Teaching AVI when to investigate further

A useful agent may need more than one observation. The challenge is not allowing a loop; it is controlling whether another iteration is actually making progress.

## What AVI Gains

- explicit loop controller
- iteration and tool-call limits
- runtime limits
- duplicate-call detection
- progress detection
- termination reasons
- escalation when evidence remains insufficient

## Trust Question

Can AVI continue an investigation without retrying the same failed idea forever?

## Architecture

```text
Goal -> Gather -> Reason -> Act -> Verify -> Enough evidence?
                                          | yes -> Finish
                                          ` no  -> Progress check -> Continue / Escalate
```

## Build Goals

Track for every run:

- iteration number
- current hypothesis
- missing evidence
- previous tool calls and arguments
- elapsed time
- repeated failures
- stopping reason

Example policy:

```yaml
max_iterations: 5
max_tool_calls: 8
max_runtime_seconds: 90
duplicate_call_limit: 1
unresolved_action: escalate
```

## Demo

1. run a successful two-step investigation,
2. create a failed tool call,
3. have the model request the same call again,
4. detect the duplicate,
5. change strategy or escalate,
6. print the final stopping reason.

## Safety Boundary

More iterations do not equal better reasoning. A bounded unresolved result is safer than an agent that keeps calling tools without progress.

## Next

Episode 11 verifies the claims AVI makes after the loop and separates observations from hypotheses and supported findings.
