# Episode 15 — Controlled Action

## Earning the right to make a network change

AVI reaches its first write capability only after tools, evidence, state, validation, context, intent, knowledge, harness controls, bounded loops, verification, MCP reuse, human approval, and change planning are already in place.

The first action should be intentionally boring.

## What AVI Gains

- preflight validation
- exact plan/approval/target matching
- pre-change snapshot
- tightly scoped execution
- post-change validation
- evidence for every stage
- automatic rollback path
- final execution report

## Trust Question

Can AVI make one narrow lab change and prove that the exact approved plan was executed, validated, and reversed if success criteria were not met?

## Architecture

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

## First Action Scope

Use only a designated lab or sandbox target. Good first actions include:

- update a harmless lab interface description,
- enable a specifically designated lab interface,
- modify a test-only banner or loopback description.

Do not begin with arbitrary configuration execution, routing policy changes, session resets, or production targets.

## Build Goals

Execution should require all of the following:

1. valid structured plan,
2. non-expired approval tied to the same plan,
3. exact target match,
4. permitted action class,
5. pre-change snapshot,
6. passing prechecks,
7. evidence recording before and after execution,
8. passing postchecks,
9. rollback instructions ready before the change begins.

## Demo

Run two scenarios:

### Successful path
- preflight passes,
- narrow change executes,
- postcheck confirms expected state,
- final report references all evidence.

### Failed postcheck path
- change executes,
- expected state is not observed,
- AVI triggers the predefined rollback,
- rollback is verified,
- result escalates to the engineer.

## Safety Boundary

This is not autonomous production networking. It is a controlled lab demonstration of the engineering controls required before any write capability should exist.

## Series Takeaway

AVI did not become trustworthy because the model got smarter. It earned capability because the surrounding system became more observable, structured, bounded, verifiable, and controllable.

```text
Tool -> Evidence -> State -> Structure -> Scale -> Context -> Intent -> Knowledge
     -> Harness -> Loop -> Verification -> Reuse -> Approval -> Plan -> Action
```

That is the AVI v2 journey.
