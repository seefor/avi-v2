# Episode 13 — Human Approval

## When AVI needs permission

AVI can observe, investigate, verify, and recommend. This episode adds a structured human approval boundary before any risky action is eligible for execution.

## What AVI Gains

- approval-request model
- approval decision record
- exact target/action binding
- evidence references
- risk and impact fields
- expiration checks
- approver identity
- rejection and invalidation paths

## Trust Question

Can AVI prove that a human approved this exact action against this exact target for this exact reason?

## Architecture

```text
Verified recommendation
      -> approval packet
          -> human decision
              -> approval record
                   | approved and valid
                   v
              eligible for planning
```

## Build Goals

An approval packet should include:

- requested action
- target device/object
- reason
- supporting evidence IDs
- expected impact
- risk level
- proposed command or action class
- validation expectation
- rollback expectation
- expiration

An approval record should bind the decision to the exact packet. A generic “approved” flag is not enough.

## Demo

Show four cases:

1. incomplete request rejected,
2. expired approval rejected,
3. approval for the wrong target rejected,
4. valid approval recorded.

Execution remains disabled in this episode.

## Safety Boundary

Human approval does not mean the proposed change is technically correct. It only proves that an authorized person accepted a specific request. Change planning and validation still come next.

## Next

Episode 14 turns a verified recommendation and valid approval into a reviewable change plan with prechecks, postchecks, and rollback.
