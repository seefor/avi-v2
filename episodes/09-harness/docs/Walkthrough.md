# Episode 09 Walkthrough — Harness: Controls Around the Model

## 1. Opening Hook

What to say:

"At this point AVI has tools, evidence, state, validation, context, intent, and RAG. If all of that lives in disconnected demo scripts, we still do not have an agent architecture. Today we build the harness that controls how those pieces work together."

## 2. Trust Question

Can we explain exactly what the application controls independently of what the model suggests?

## 3. Architecture

```text
User
  -> AVI Harness
      |- policy / permissions
      |- context assembly
      |- prompt construction
      |- model
      |- approved tools
      |- evidence
      |- validation
      `- run state
```

## 4. Run the Starter

```bash
python episodes/09-harness/avi_pilot_09_harness.py
```

## 5. Reframe the Agent

What to say:

"The model is one component. The agent is the controlled system around the model."

Explain what the harness owns:
- available tools,
- caller permissions,
- context selection,
- prompt construction,
- evidence recording,
- output validation,
- stop conditions.

## 6. Walk One Request Through the Harness

Show each stage:
1. request accepted,
2. context selected,
3. model decision,
4. tool request validated,
5. tool executed,
6. evidence recorded,
7. response validated.

Pause at each stage and identify which parts are deterministic application logic.

## 7. Tool Registry

Explain why tools should be registered with names/contracts/policies rather than exposed as arbitrary functions.

## 8. Policy Block Demo

Request a tool or target the current policy does not allow.

What to say:

"The prompt can remind the model about policy. The harness enforces it."

Show the blocked result and evidence.

## 9. Error Path

Trigger a validation/tool error and show how run state captures the failure without skipping controls.

## 10. Begin `avi_core`

Explain the architectural shift from episode-specific copied code toward reusable stable components.

## 11. What AVI Still Cannot Do

AVI can orchestrate one pass, but a troubleshooting investigation may require more than one observation. It still needs a bounded loop.

## 12. Homework

1. Add one harmless tool to the registry.
2. Add a caller/tool authorization rule.
3. Log every harness stage.
4. Confirm an unauthorized tool cannot execute even if the model requests it.

## 13. Next Flight

"Episode 10 teaches AVI how to investigate further without getting stuck in an endless agent loop."