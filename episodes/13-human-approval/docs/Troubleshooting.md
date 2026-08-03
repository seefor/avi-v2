# Episode 13 Troubleshooting — Human Approval

## Approval Always Validates

Check that validation compares the exact action, target, packet identity, expiration, and decision—not only an `approved=true` field.

## Approval Is Immediately Expired

Inspect timezone handling and timestamp formats. Prefer UTC-aware timestamps.

## Wrong Target Reuse Is Accepted

Bind target identity into the approval request and validate it again before downstream planning/execution.

## Packet Changes After Approval

Use an immutable packet ID/hash or canonical representation. A modified packet should require a new decision.

## Rejection Has No Explanation

Store a rejection reason so the workflow and human reviewer know why progress stopped.

## Approver Identity Is Missing

Treat identity as required for a valid decision. A decision without attributable approval should not move forward.

## Debugging Order

```text
1. Print approval packet
2. Validate required fields
3. Print decision record
4. Compare target/action identity
5. Check expiration
6. Check approver + decision
7. Confirm execution is still disabled
```