# Episode 09 Teaching Notes — Harness

## The Model Is Not the Agent

A production agent is the model plus application controls: tools, context, state, policy, evidence, validation, retries, stop conditions, and identity/authorization.

This distinction is central to the AVI series.

## Prompt Rules vs. Enforced Rules

Natural-language instructions help shape model behavior but should not be the only control for operational permissions. The harness should independently validate target, tool, arguments, and workflow state.

## Tool Registry

A registry can centralize:
- tool name/description,
- typed input contract,
- allowed targets/actions,
- evidence behavior,
- authorization requirements.

## Run State

The harness needs an explicit representation of the current request, selected context, tool events, validation results, and terminal status. That becomes even more important once Episode 10 introduces iteration.

## Why Move Logic to `avi_core`

The goal is one evolving assistant rather than 15 disconnected demos. Stable implementations should progressively move into shared code while each episode remains understandable.

## Key Takeaway

Trust comes from controls around the model that are visible, testable, and deterministic where possible.