# Episode 09 — Harness

## Building controls around the model

AVI has accumulated several capabilities. This episode stops treating them as disconnected demos and places them behind one reusable agent harness.

## What AVI Gains

- centralized orchestration
- model selection and prompt construction
- context assembly
- tool registry and tool authorization
- evidence recording
- structured-output validation
- run state and error handling
- policy enforcement in code

## Trust Question

Can we explain exactly what the application controls independently of what the model suggests?

## Architecture

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

## Build Goals

Begin moving stable logic into `avi_core/` so later episodes import common components rather than copying scripts.

The harness should own:

- what tools exist,
- which caller can request them,
- what context is supplied,
- how outputs are validated,
- what gets recorded,
- when the workflow stops.

## Demo

Run one troubleshooting request through the harness and print the stages:

1. request accepted,
2. context selected,
3. model decision,
4. tool request validated,
5. tool executed,
6. evidence recorded,
7. response validated.

Then request a tool that policy does not allow and show the harness blocking it.

## Safety Boundary

The prompt may express rules, but the harness must enforce them. A policy that exists only in natural language is not enough for operational control.

## Next

Episode 10 gives the harness a bounded investigation loop and teaches AVI when another tool call is useful—and when it is not.
