# Episode 13 Teaching Notes — Human Approval

## Human-in-the-Loop Is More Than a Button

A useful approval record must answer:
- who approved,
- what exact action,
- against what exact target,
- why,
- based on which evidence,
- for how long the decision remains valid.

## Approval Binding

The approval should be bound to a stable request identity or canonical packet so changing the target/action invalidates the decision.

## Expiration

Approvals can become unsafe when the network state changes. A time limit forces the system to re-evaluate old decisions instead of treating permission as permanent.

## Approval Does Not Prove Technical Correctness

A person can approve a bad plan. This is why AVI still needs Episode 14: deterministic plan validation, prechecks, postchecks, and rollback.

## Rejection Is a First-Class Outcome

Rejected, expired, invalid, and mismatched approvals should all stop the workflow with explicit reasons.

## Key Teaching Phrase

"Human approval is authorization, not validation."

## Key Takeaway

A human-in-the-loop control becomes meaningful when permission is explicit, scoped, attributable, and time-bound.