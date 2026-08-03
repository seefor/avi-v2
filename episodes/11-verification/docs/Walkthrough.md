# Episode 11 Walkthrough — Verification: Prove the Finding

## 1. Opening Hook

What to say:

"AVI can investigate now, but an investigation can still end with a story that sounds right. Today we separate what AVI observed from what it thinks happened—and only call something a finding when the evidence actually supports it."

## 2. Trust Question

Can AVI distinguish a plausible explanation from a conclusion supported by available evidence?

## 3. Architecture

```text
Evidence -> Candidate claims -> Verification rules ->
             supported / unsupported / unresolved
```

## 4. Run the Starter

```bash
python episodes/11-verification/avi_pilot_11_verification.py
```

## 5. Define the Four Layers

Explain:
- observation: a recorded fact from a source/tool,
- inference: a reasoned interpretation,
- hypothesis: an explanation to test,
- verified finding: a claim that meets the evidence rule.

What to say:

"Confidence should come from evidence quality, not from how confident the model sounds."

## 6. Walk Through the Verification Record

Show:
- claim,
- status,
- evidence references,
- confidence,
- limitations.

## 7. Unsupported Hypothesis Demo

Start with a plausible claim such as BGP instability being caused by interface loss, but omit the required supporting interface evidence.

Show the verifier downgrade or reject the claim.

## 8. Add Supporting Evidence

Add the missing evidence source and rerun verification.

Show how the status/confidence changes because the evidence changed—not because the prompt became more persuasive.

## 9. Unresolved Questions

Show how AVI reports missing evidence and recommends the next safe check instead of filling the gap.

## 10. Break It on Purpose

Give a candidate claim an evidence ID that does not exist or does not support the claim.

Confirm verification fails.

## 11. Safety Boundary

Verification is not certainty. It is a documented relationship between claims, evidence, and known limitations.

## 12. What AVI Still Cannot Do

AVI has safe internal tools, but those contracts are still tied to this application. Episode 12 makes them reusable through MCP without weakening the controls.

## 13. Homework

1. Add one unsupported claim.
2. Add a second evidence source.
3. Add a limitation field.
4. Verify that confidence cannot increase without stronger evidence.

## 14. Next Flight

"Episode 12 exposes AVI's narrow network tools through MCP. The important lesson is that MCP makes tools reusable—it does not make them safe automatically."