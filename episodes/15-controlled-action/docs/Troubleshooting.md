# Episode 15 Troubleshooting — Controlled Action

## Starter Changes a Real Device

Stop. The default Episode 15 starter should use in-memory/simulated lab state. Do not replace it with a live write backend until all controls are deliberately reviewed for a designated lab.

## Execution Runs After Failed Precheck

Treat this as a control failure. The executor must require every gate to pass before calling the write backend.

## Approval and Plan Do Not Match

Compare exact target, action class, plan/packet identity, and expiration. Require a new approval if scope changed.

## Postcheck Passes Without Observing State

A successful function return is not enough. Postcheck should independently inspect the resulting state.

## Rollback Runs but State Is Still Wrong

Run rollback verification and mark the workflow escalated/failed. Do not report rollback success only because the rollback command returned.

## Evidence Chain Has Gaps

Every stage should create or reference evidence. Inspect finding, approval, plan, preflight, snapshot, execution, postcheck, and rollback records.

## Target Mismatch Is Not Blocking

Move exact target validation into preflight immediately before execution as well as earlier plan/approval checks.

## Debugging Order

```text
1. Confirm backend is simulated/lab-only
2. Validate plan
3. Validate approval
4. Compare exact target/action
5. Run prechecks
6. Capture snapshot
7. Execute narrow action
8. Observe postcheck
9. Roll back on failure
10. Verify rollback
11. Inspect final evidence chain
```

Never bypass a failed gate simply to complete the demo.