# Episode 13 Walkthrough — Human Approval

## Video Title
AVI #13 — Human Approval: When AVI Needs Permission

## Hook
A prompt that says “ask before making changes” is not an approval system. AVI needs a real record that binds a human decision to one exact action and target.

## Talking Points
- approval is an application control
- approval needs scope, evidence, target, and expiration
- a yes/no button without context is weak control
- approval does not replace technical validation

## Demo Flow
1. Start from a verified recommendation.
2. Generate the approval packet.
3. Reject an incomplete packet.
4. Record a valid approval.
5. Change the target and show the approval becoming invalid.
6. Expire the approval and show it failing closed.

## Failure Scenario
Reuse an approval for a different device or command. The system should reject it deterministically.

## Close
AVI can now request permission, but permission alone is not enough to safely execute anything. Episode 14 builds the complete change plan before execution is even considered.
