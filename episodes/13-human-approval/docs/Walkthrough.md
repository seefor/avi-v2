# Episode 13 Walkthrough — Human Approval: Permission With Scope

## 1. Opening Hook

What to say:

"AVI can observe, investigate, verify, and recommend. That still does not mean it gets to act. Today we build the human approval boundary—but a generic 'approved' boolean is not enough."

## 2. Trust Question

Can AVI prove that a human approved this exact action, on this exact target, for this exact reason, within a valid time window?

## 3. Architecture

```text
Verified recommendation
      -> approval packet
          -> human decision
              -> approval record
                   | approved and valid
                   v
              eligible for planning
```

## 4. Run the Starter

```bash
python episodes/13-human-approval/avi_pilot_13_approval.py
```

## 5. Walk Through the Approval Packet

Show:
- requested action,
- target,
- reason,
- evidence IDs,
- expected impact,
- risk,
- proposed action class,
- validation expectation,
- rollback expectation,
- expiration.

What to say:

"The human needs enough information to understand what they are approving."

## 6. Approval Decision Record

Explain approver identity, decision time, packet reference/hash/ID, expiration, and exact binding to target/action.

## 7. Demo Case 1 — Incomplete Request

Remove a required field and show the request is rejected before approval can be valid.

## 8. Demo Case 2 — Expired Approval

Use an expired record and show validation reject it.

## 9. Demo Case 3 — Wrong Target

Approve an action for device A, then attempt to use that approval for device B.

What to say:

"Approval is not transferable permission."

## 10. Demo Case 4 — Valid Approval

Show a complete packet and valid decision record.

Emphasize that execution remains disabled.

## 11. Break It on Purpose

Change the requested command/action after the approval is recorded. Show that the approval no longer matches.

## 12. Safety Boundary

Human approval proves authorization for a specific request. It does not prove the change is technically correct or safe to execute.

## 13. What AVI Still Cannot Do

AVI has permission to move forward conceptually, but it does not yet have a complete, reviewable, reversible change plan.

## 14. Homework

1. Add a short expiration.
2. Test wrong-target reuse.
3. Test action mutation after approval.
4. Add an explicit rejection reason.

## 15. Next Flight

"Episode 14 takes the verified recommendation and valid approval and turns them into something another network engineer can actually review: a change plan with prechecks, expected diff, postchecks, risks, and rollback."