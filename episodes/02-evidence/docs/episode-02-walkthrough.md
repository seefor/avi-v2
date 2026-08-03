# Episode 02 Walkthrough — Evidence

## Video Title
AVI #2 — Evidence: How Do We Prove What the Agent Actually Saw?

## Hook
An AI answer is only as useful as the evidence behind it. If AVI says a peer was down, I want to know which tool ran, against which device, what came back, and whether the call actually succeeded.

## Talking Points
- observability comes before autonomy
- tool results need durable identity
- success, rejection, and failure all matter
- logs must be useful without becoming a secret dump

## Demo Flow
1. Run the same read-only tool from Episode 1.
2. Open the evidence JSONL record.
3. Trace run ID and evidence ID.
4. Trigger a blocked command and inspect the evidence.
5. Trigger a connection failure and compare records.

## Failure Scenario
Show why a terminal print statement is not enough: rerun the workflow and demonstrate that durable evidence is what allows later replay and verification.

## Close
We can now prove what AVI saw. Next we need to stop treating network output as a blob of text and turn it into explicit operational state.
