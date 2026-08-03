# Episode 09 Troubleshooting — Harness

## Tool Exists but Harness Cannot Find It

Check registration name, import path, and initialization order. Print the tool registry before the model/request path runs.

## Unauthorized Tool Executes

Stop and inspect authorization placement. Policy validation must occur before tool invocation, not after the result returns.

## Context Is Missing

Trace the request through the context-assembly stage and print the selected sources before prompt construction.

## Validation Is Skipped on Error Paths

Make sure every terminal path sets run status and records evidence. Exceptions should not bypass the harness lifecycle.

## Episode Code and `avi_core` Drift Apart

Keep one source of truth for shared behavior. Import stable components rather than copying and modifying duplicate functions.

## Model Output Controls Execution Directly

Insert a deterministic translation/validation step between model suggestion and application tool invocation.

## Debugging Order

```text
1. Print request/run state
2. Print tool registry
3. Print selected context
4. Inspect model decision
5. Inspect policy validation
6. Inspect tool result/evidence
7. Inspect final validation
```