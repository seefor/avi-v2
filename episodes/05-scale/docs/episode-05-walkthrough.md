# Episode 05 Walkthrough — Scale

## Video Title
AVI #5 — Scale: What Changes When AVI Looks at Multiple Devices?

## Hook
Running the same command on ten devices is easy. Preserving evidence, failures, timing, and meaning across ten devices is the real problem.

## Talking Points
- one failed device should not erase successful observations
- concurrency needs limits
- fleet summaries must keep drill-down evidence
- partial failure is a normal network condition

## Demo Flow
1. Load a small inventory.
2. Run bounded observations.
3. Show one healthy, one degraded, and one unreachable target.
4. Review the rollup.
5. Drill back into individual evidence records.

## Failure Scenario
Force one device timeout and prove the overall run completes with an explicit partial-failure result.

## Close
AVI can now collect more information than we should necessarily send to a model. Episode 6 introduces context engineering: selecting the right information for the current decision.
