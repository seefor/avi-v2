# Episode 15 Walkthrough — Controlled Action: Earning the Right to Change the Network

## 1. Opening Hook

What to say:

"We spent fourteen episodes refusing to let AVI configure the network. That was intentional. Today AVI finally gets one write capability—but only after every previous control passes. The first action is going to be boring, narrow, reversible, and lab-only."

## 2. Trust Question

Can AVI execute the exact approved plan on the exact lab target, prove the result, and roll back if the success criteria are not met?

## 3. Full Architecture

```text
Verified finding
   -> valid approval
      -> validated change plan
         -> preflight
            -> pre-change snapshot
               -> controlled execution
                  -> postchecks
                     |- pass -> evidence + complete
                     `- fail -> rollback -> verify rollback -> escalate
```

Take time to remind viewers that every box exists because of an earlier episode.

## 4. Run the Starter

```bash
python episodes/15-controlled-action/avi_pilot_15_controlled_action.py
```

Explain that the starter uses in-memory lab state by default. That is intentional.

## 5. Define the First Action Scope

Use only a harmless designated lab action such as:
- interface description update,
- specifically designated lab interface enable,
- test-only banner/loopback description.

What to say:

"The goal is to prove the control system, not to prove AVI can type a dangerous command."

## 6. Preflight

Walk through each required gate:
1. valid structured plan,
2. valid non-expired approval,
3. exact target match,
4. permitted action class,
5. pre-change snapshot,
6. passing prechecks,
7. evidence recorder ready,
8. rollback ready.

If any gate fails, stop.

## 7. Pre-Change Snapshot

Show the state before execution and explain why it matters for both verification and rollback.

## 8. Successful Path Demo

Run the controlled action.

Show:
- execution evidence,
- postcheck,
- expected state observed,
- final report with evidence references.

What to say:

"Success is not 'the command returned without an exception.' Success is that the expected state was independently observed after the change."

## 9. Failed Postcheck Demo

Run the failure scenario where the change executes but the expected state is not observed.

Show:
- postcheck failure,
- predefined rollback,
- rollback verification,
- escalation/final failed status.

## 10. Review the Evidence Chain

Trace the final report through:
- finding evidence,
- approval,
- plan,
- preflight,
- snapshot,
- execution,
- postcheck,
- rollback if applicable.

## 11. Break It on Purpose

Demonstrate one blocked preflight case such as expired approval, target mismatch, or missing rollback.

Confirm no execution happens.

## 12. Safety Boundary

This episode is not autonomous production networking. It is a lab demonstration of the controls required before any write capability should exist.

## 13. Series Review

Show:

```text
Tool -> Evidence -> State -> Structure -> Scale -> Context -> Intent -> Knowledge
     -> Harness -> Loop -> Verification -> Reuse -> Approval -> Plan -> Action
```

What to say:

"AVI did not become trustworthy because the model got smarter. AVI earned capability because the system around the model became more observable, structured, bounded, verifiable, and controllable."

## 14. Homework / Build Forward

Ask viewers to:
1. Keep the write backend simulated until they understand every gate.
2. Add another harmless lab action class.
3. Add a failing precheck.
4. Add a postcheck failure and verify rollback.
5. Never broaden the system to arbitrary configuration execution.

## 15. Final Series Close

"This was the first full AVI v2 journey. We started by asking whether AI could safely observe a network. We ended by asking whether it had earned the right to make one bounded change. That gap between observation and action is where the real engineering lives."