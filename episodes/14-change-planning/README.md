# Episode 14 — Change Planning

## Recommendation before execution

Generating configuration is easy. Generating a reviewable, bounded, reversible change plan is the engineering work AVI needs before it can ever act.

## What AVI Gains

- structured change-plan model
- proposed commands/actions
- expected diff
- prechecks
- postchecks
- risk notes
- rollback plan
- approval reference
- deterministic plan validation

## Trust Question

Can another engineer review exactly what AVI proposes, why it proposes it, how success will be measured, and how the change will be reversed before anything executes?

## Architecture

```text
Verified finding + valid approval
        -> change planner
            -> plan validation
                -> reviewable change packet
                    -> execution remains disabled
```

## Build Goals

A change plan should include:

```yaml
change_plan:
  objective:
  target:
  evidence_refs: []
  approval_ref:
  proposed_commands: []
  expected_diff:
  prechecks: []
  postchecks: []
  rollback_commands: []
  risks: []
  execution_allowed: false
```

Validate:

- target platform and device
- permitted action class
- exact approval linkage
- required evidence
- rollback presence
- post-change verification
- command shape/allowlist

## Demo

Generate a plan for one narrow lab change. Review it like a change ticket. Then deliberately remove the rollback or postcheck and show plan validation failing.

## Safety Boundary

This episode does not execute the plan. A valid plan is an artifact that can be reviewed; it is not authorization to bypass the controlled-action gate.

## Next

Episode 15 puts every previous layer together and executes one tightly bounded, reversible lab action with preflight, approval, evidence, post-validation, and rollback.
