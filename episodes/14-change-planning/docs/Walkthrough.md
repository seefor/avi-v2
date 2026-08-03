# Episode 14 Walkthrough — Change Planning: Recommendation Before Execution

## 1. Opening Hook

What to say:

"Generating a configuration command is easy. Building a change another engineer can review, validate, reverse, and measure is the hard part. Today AVI learns to plan before it ever executes."

## 2. Trust Question

Can another engineer see exactly what AVI proposes, why, how success will be measured, and how the change will be reversed before anything runs?

## 3. Architecture

```text
Verified finding + valid approval
        -> change planner
            -> plan validation
                -> reviewable change packet
                    -> execution remains disabled
```

## 4. Run the Starter

```bash
python episodes/14-change-planning/avi_pilot_14_change_plan.py
```

## 5. Walk Through the Change Plan

Explain:
- objective,
- target,
- evidence references,
- approval reference,
- proposed commands/actions,
- expected diff,
- prechecks,
- postchecks,
- rollback commands,
- risks,
- `execution_allowed: false`.

## 6. Build One Narrow Lab Plan

Use a harmless example such as changing a lab interface description.

What to say:

"The plan is an artifact for review. It is not execution."

## 7. Prechecks

Explain what must be true before the proposed change is even eligible to run.

Examples:
- exact target/platform,
- current state matches assumptions,
- approval is valid,
- action class is permitted.

## 8. Expected Diff

Show what should change and, equally important, what should not change.

## 9. Postchecks

Define objective success criteria that can be observed after execution.

## 10. Rollback

Show rollback instructions existing before any write action begins.

## 11. Break It — Remove Rollback

Delete/empty rollback and run plan validation.

Confirm the plan fails.

## 12. Break It — Remove Postcheck

Show that a plan without verification cannot move forward.

## 13. Safety Boundary

A valid plan still does not execute in Episode 14.

## 14. What AVI Still Cannot Do

AVI has finally assembled the prerequisites for one controlled lab action. Execution is still gated behind preflight, exact approval/plan matching, evidence, post-validation, and rollback.

## 15. Homework

1. Add a second risk note.
2. Add a precheck that can deliberately fail.
3. Remove rollback and verify rejection.
4. Confirm the plan references the exact approval and evidence.

## 16. Next Flight

"We spent fourteen episodes refusing to give AVI write access. In Episode 15 we let it make one intentionally boring lab change—and prove every control around it."