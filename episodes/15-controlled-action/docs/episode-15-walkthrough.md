# Episode 15 Walkthrough — Controlled Action

## Video Title
AVI #15 — Controlled Action: Earning the Right to Make a Network Change

## Hook
This is the first time in the series AVI is allowed to change anything—and the interesting part is not the command. The interesting part is everything that has to be true before and after that command runs.

## Talking Points
- the first write capability should be narrow and reversible
- approval, plan, and target must match exactly
- prechecks and snapshots happen before execution
- postchecks decide whether the change actually succeeded
- rollback is part of the plan, not something invented after failure

## Demo Flow — Success
1. Review the verified finding.
2. Review the valid approval.
3. Review the exact change plan.
4. Run preflight and prechecks.
5. Capture the pre-change snapshot.
6. Execute the designated lab-only action.
7. Run postchecks.
8. Review the evidence chain and final report.

## Demo Flow — Failed Postcheck
1. Use a controlled test that makes the success condition fail.
2. Show post-validation rejecting the outcome.
3. Trigger the predefined rollback.
4. Verify the rollback.
5. Show the final state as rolled back and escalated.

## Camera Emphasis
The configuration command should be the least interesting part of the video. Spend the time on the evidence, plan, approval, preflight, verification, and rollback controls around it.

## Close
AVI did not earn a write capability because the LLM became more autonomous. It earned it because we built a system around the model that can be inspected, constrained, verified, and stopped.

That is the difference between an AI demo and an operational engineering pattern.
