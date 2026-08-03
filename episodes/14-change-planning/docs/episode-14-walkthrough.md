# Episode 14 Walkthrough — Change Planning

## Video Title
AVI #14 — Change Planning: Recommendation Before Execution

## Hook
The dangerous shortcut is going from “I think this should change” straight to “run these commands.” AVI needs a complete plan that another engineer can review first.

## Talking Points
- configuration generation is not change control
- every plan needs prechecks, expected outcome, postchecks, and rollback
- approval must reference the exact plan scope
- validation should reject incomplete plans

## Demo Flow
1. Start from a verified finding and valid approval.
2. Generate the proposed change plan.
3. Review commands, expected diff, prechecks, postchecks, and rollback.
4. Remove a rollback step and run plan validation.
5. Restore it and show the plan passing validation.
6. Confirm `execution_allowed` is still false.

## Failure Scenario
Produce a plan with a target mismatch or missing postcheck and show the workflow stopping before any execution path exists.

## Close
AVI can now create a reviewable plan. In Episode 15 we put every layer together for one deliberately boring, reversible lab action—and we prove rollback works when post-validation fails.
