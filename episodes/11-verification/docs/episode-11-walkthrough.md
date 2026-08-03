# Episode 11 Walkthrough — Verification

## Video Title
AVI #11 — Verification: How AVI Knows Whether Its Hypothesis Is Supported

## Hook
A model can give you a convincing root cause with weak evidence. AVI should be able to say, “that is plausible, but I cannot prove it yet.”

## Talking Points
- observation is not inference
- inference is not verified finding
- confidence should come from evidence quality
- unsupported claims should be visible, not polished away

## Demo Flow
1. Gather a degraded BGP observation.
2. Let AVI propose an interface-related hypothesis.
3. Run verification with insufficient interface evidence.
4. Show the claim marked unsupported/unresolved.
5. Add relevant interface evidence.
6. Rerun and show the claim becoming supported with evidence references.

## Failure Scenario
Have the model use confident language unsupported by tools. The verifier should downgrade the claim regardless of wording.

## Close
AVI can now investigate and defend its conclusions. Episode 12 makes the safe tool layer reusable through MCP without changing the underlying trust model.
