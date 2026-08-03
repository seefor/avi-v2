# Episode 14 Teaching Notes — Change Planning

## A Command Is Not a Change Plan

A production-quality plan describes the full lifecycle:
- why the change is needed,
- exact target and scope,
- assumptions/prechecks,
- proposed delta,
- expected impact,
- validation criteria,
- rollback,
- supporting evidence and approval.

## Expected Diff

The plan should make the intended delta explicit. This improves review and later verification because the system knows what success should look like.

## Prechecks and Postchecks

Prechecks validate assumptions before execution. Postchecks prove whether the expected state was achieved afterward. Both should be machine-observable when possible.

## Rollback Before Execution

Rollback should be known before the change begins. Designing rollback after a failed change is too late.

## Approval Linkage

The plan must remain inside the scope that was approved. If the plan changes action or target, it should require a new approval decision.

## Deterministic Validation

Plan validation should reject missing rollback, missing postchecks, unsupported commands/action classes, wrong targets, and invalid approval linkage.

## Key Takeaway

AVI earns the right to execute only after the proposed action becomes a complete, reviewable, bounded, and reversible engineering artifact.