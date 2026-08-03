# Episode 10 Walkthrough — Loops

## Video Title
AVI #10 — Loops: Teaching AVI When to Investigate Further

## Hook
Calling tools repeatedly is not an investigation strategy. AVI needs to know whether the next step is adding evidence or just repeating failure.

## Talking Points
- agent loops are application code
- iteration and time limits are required
- duplicate-call detection prevents fake progress
- escalation is a valid successful outcome

## Demo Flow
1. Run a two-tool investigation that reaches enough evidence.
2. Trigger a failed tool call.
3. Let the model request the same arguments again.
4. Show duplicate detection.
5. Select a different evidence source or escalate.
6. Review iteration history and stopping reason.

## Failure Scenario
Construct a loop that never produces new evidence and show the controller terminating it predictably.

## Close
A controlled loop tells AVI when to stop gathering. Episode 11 asks the harder question: does the evidence actually support the conclusion AVI wants to return?
