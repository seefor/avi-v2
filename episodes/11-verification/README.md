# Episode 11 — Verification

## How AVI knows whether its hypothesis is supported

AVI can investigate. This episode makes the final answer prove its relationship to the evidence.

## What AVI Gains

- claim-to-evidence checks
- explicit observation, inference, hypothesis, and verified-finding labels
- confidence based on evidence quality rather than model tone
- unresolved-question reporting
- evidence references in final findings

## Trust Question

Can AVI distinguish a plausible explanation from a conclusion actually supported by the available data?

## Architecture

```text
Evidence -> Candidate claims -> Verification rules ->
             supported / unsupported / unresolved
```

## Build Goals

A verification record should contain:

```json
{
  "claim": "The BGP instability is related to interface loss",
  "status": "supported",
  "evidence_refs": ["evt-102", "evt-108"],
  "confidence": "medium",
  "limitations": ["No historical change data was available"]
}
```

Final responses should separate:

- observations
- hypotheses
- supported findings
- unsupported claims
- missing evidence
- recommended next checks

## Demo

Give AVI a plausible initial hypothesis, then show that the verifier downgrades or rejects it when the required evidence is absent. Add a second evidence source and rerun verification.

## Safety Boundary

Verification is not certainty. Confidence must reflect available evidence and limitations, not how persuasive the language model sounds.

## Next

Episode 12 packages the safe tool capabilities behind MCP so the same contracts can be reused by more than one client.
