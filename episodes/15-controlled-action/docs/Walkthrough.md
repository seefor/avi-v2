# Episode 15 Walkthrough — AVI Earns the Right to Make One Network Change

This is the production-ready recording guide for AVI v2 Episode 15 and the finale of the first full AVI v2 journey.

## YouTube Package

### Recommended title

**We Finally Let the AI Change the Network | Building AVI Ep. 15**

### Alternate titles

- **After 14 Episodes, AVI Finally Gets Write Access — Safely | Ep. 15**
- **Can an AI Agent Safely Make a Network Change? | AVI Finale**
- **From Read-Only to Controlled Action: AVI Earns Write Access | Ep. 15**

### Thumbnail direction

Show the full journey converging on one guarded write action:

```text
14 CONTROL LAYERS
      ↓
  ONE CHANGE
```

Suggested thumbnail text:

**IT FINALLY GETS WRITE ACCESS**

Alternate:

**ONE CONTROLLED CHANGE**

### Core promise

AVI will execute one narrow, reversible, lab-only simulated change only after preflight passes, and it will automatically roll back when the postcheck fails.

### Target runtime

**40–55 minutes**

This is the one episode where a longer runtime is justified because it closes the entire trust arc.

---

# Recording Run of Show

## 0:00–1:00 — Cold Open

### Screen

Start on camera.

### What to say

> "We spent fourteen episodes refusing to let AVI configure the network. That was intentional. Today AVI finally gets one write capability—but only after every previous control has earned its place."

Then cut quickly to the final two statuses from the starter:

```text
status: success
```

and:

```text
status: rolled_back
reason: postcheck_failed
```

Then return to camera:

> "The first action is going to be boring, narrow, reversible, and lab-only. That's exactly the point."

### Hook takeaway

The episode is about proving the control system, not proving that Python can change configuration.

---

## 1:00–3:00 — Slide: The Final Trust Question

### Slide title

**Has AVI Earned the Right to Act?**

### Show

```text
Can AVI execute the exact approved plan
on the exact target,
measure the result,
and roll back if success criteria fail?
```

### What to say

> "A command completing without an exception is not enough. Success means we executed the intended action, on the intended target, and independently observed the expected result afterward."

---

## 3:00–6:00 — Slide: The Full AVI Journey

Show the complete progression:

```text
Tool -> Evidence -> State -> Structure -> Scale -> Context -> Intent -> Knowledge
     -> Harness -> Loop -> Verification -> Reuse -> Approval -> Plan -> Action
```

Walk through it quickly in four arcs.

### Arc 1 — Observe safely

```text
Tool -> Evidence -> State -> Structure
```

### Arc 2 — Understand the environment

```text
Scale -> Context -> Intent -> Knowledge
```

### Arc 3 — Behave like an agent safely

```text
Harness -> Loop -> Verification -> Reuse
```

### Arc 4 — Earn permission to act

```text
Approval -> Plan -> Action
```

### What to say

> "AVI did not become trustworthy because the model got smarter. It earned capability because the system around the model became more observable, structured, bounded, verifiable, and controllable."

---

## 6:00–8:30 — Slide: Episode 15 Architecture

```text
Plan + Approval
      ↓
   preflight()
      ↓
pre-change snapshot
      ↓
   execute()
      ↓
   postcheck
      |
      |- pass -> success
      |
      `- fail -> rollback -> rolled_back
```

### Important clarification

The Episode 15 starter is an **in-memory lab simulator**. It does not configure a real router.

### What to say

> "I want the control chain to be testable before I attach it to a real write backend. A fresh clone of this repo should never be one command away from changing production infrastructure."

---

# Build and Code Walkthrough

## 8:30–10:00 — Repository Orientation

Open:

```text
episodes/15-controlled-action/
```

Show:

```text
avi_pilot_15_controlled_action.py
README.md
docs/
```

Run from the repository root:

```bash
python episodes/15-controlled-action/avi_pilot_15_controlled_action.py
```

Before running it live, explain the code first.

---

## 10:00–12:00 — In-Memory Lab State

Highlight:

```python
LAB_STATE = {
    "lab-r1": {
        "GigabitEthernet1": {"description": "ORIGINAL-LAB-DESCRIPTION"}
    }
}
```

### What to say

> "This dictionary is our lab device for Episode 15. We're proving state transition, post-validation, and rollback without creating a live configuration backend."

> "Once these controls are well understood, a future backend can replace this state store—but the default should remain safe."

---

## 12:00–16:00 — `preflight()`

Show the function:

```python
def preflight(plan: dict, approval: dict) -> None:
```

Walk through each check.

### Check 1 — Exact target match

```python
if plan["target"] != approval["target"]:
    raise PermissionError("Plan and approval target do not match")
```

### What to say

> "The approved target and the planned target must be identical. We do not transfer approval from one object to another."

### Check 2 — Approved decision

```python
if approval.get("decision") != "approved":
    raise PermissionError("Action is not approved")
```

### Check 3 — Rollback must exist

```python
if not plan.get("rollback_description"):
    raise ValueError("Rollback is required before execution")
```

### Key line

> "Rollback is not something we invent after a failed change. It has to exist before execution begins."

### Accuracy note

Explain that this starter demonstrates three focused preflight gates. The full architecture from Episodes 13–14 can later add expiration, approval IDs, action classes, evidence linkage, and richer plan validation.

---

## 16:00–21:00 — `execute()` Part 1: Snapshot Before Change

Highlight:

```python
preflight(plan, approval)
device, interface = plan["target"].split(":", 1)
before = deepcopy(LAB_STATE[device][interface])
```

### What to say

> "Before AVI changes anything, it captures what existed before. That gives us a baseline for both reporting and recovery."

Explain why `deepcopy()` matters in this in-memory example: the `before` snapshot must not mutate when the lab state changes.

Then show the write:

```python
LAB_STATE[device][interface]["description"] = plan["new_description"]
```

### What to say

> "This is the first actual state-changing line in the entire AVI v2 series."

Pause there for emphasis.

---

## 21:00–24:00 — `execute()` Part 2: Postcheck

Show:

```python
observed = LAB_STATE[device][interface]["description"]
postcheck_ok = observed == plan["new_description"] and not force_postcheck_failure
```

### What to say

> "Success isn't that the assignment executed. Success is that we independently read the resulting state and it matches the expected value."

Explain `force_postcheck_failure` as a deterministic teaching switch used to prove rollback behavior.

---

## 24:00–28:00 — `execute()` Part 3: Rollback

Highlight:

```python
if not postcheck_ok:
    LAB_STATE[device][interface]["description"] = plan["rollback_description"]
```

Then the returned result:

```python
{
    "status": "rolled_back",
    "before": before,
    "attempted": plan["new_description"],
    "after": deepcopy(LAB_STATE[device][interface]),
    "reason": "postcheck_failed",
}
```

### What to say

> "AVI doesn't keep going and hope for the best. The predefined recovery path restores the known value and reports that the attempted change did not meet the success criteria."

### Important accuracy note

The starter restores the rollback value and returns the post-rollback state. A future hardened backend should also have an explicit rollback verification step against the real target.

---

## 28:00–30:00 — The Plan and Approval Fixtures

Show:

```python
plan = {
    "target": "lab-r1:GigabitEthernet1",
    "new_description": "AVI-LAB-TEST",
    "rollback_description": "ORIGINAL-LAB-DESCRIPTION",
}
```

and:

```python
approval = {"target": plan["target"], "decision": "approved"}
```

### What to say

> "The Episode 15 starter intentionally keeps these objects small so we can see the execution mechanics. In the full design, this plan comes from Episode 14 and the approval comes from Episode 13."

Do not pretend the starter automatically imports those previous episode files.

---

# Live Demo

## 30:00–34:00 — Successful Controlled Path

Run:

```bash
python episodes/15-controlled-action/avi_pilot_15_controlled_action.py
```

Focus first on:

```text
Successful controlled path:
```

Review:

```json
{
  "status": "success",
  "before": {
    "description": "ORIGINAL-LAB-DESCRIPTION"
  },
  "after": {
    "description": "AVI-LAB-TEST"
  }
}
```

### What to say

> "The state changed, the expected value was observed, and the result contains both the before and after state."

> "Again, this is simulated. The point is the control sequence."

---

## 34:00–38:00 — Failed Postcheck and Automatic Rollback

The starter resets the state to the known baseline and then calls:

```python
execute(plan, approval, force_postcheck_failure=True)
```

Show:

```text
Failed postcheck path:
```

Review:

```text
status: rolled_back
attempted: AVI-LAB-TEST
after.description: ORIGINAL-LAB-DESCRIPTION
reason: postcheck_failed
```

### What to say

> "This is the demo that closes the series for me. AVI made the change, the success criteria failed, and the system followed the recovery path instead of declaring victory because the write itself succeeded."

---

## 38:00–41:00 — Break It on Purpose: Target Mismatch

Temporarily create:

```python
bad_approval = {"target": "lab-r2:GigabitEthernet1", "decision": "approved"}
```

Call:

```python
execute(plan, bad_approval)
```

Expected failure:

```text
PermissionError: Plan and approval target do not match
```

### What to say

> "Notice the order. The mismatch is rejected in `preflight()` before the state-changing line can execute."

Restore the normal approval afterward.

---

## 41:00–43:00 — Break It Again: Missing Rollback

Temporarily copy the plan and remove or blank:

```python
rollback_description
```

Call `execute()`.

Expected failure:

```text
ValueError: Rollback is required before execution
```

### What to say

> "No rollback, no write. That's a rule I want the application to enforce, not a checklist item we hope someone remembers."

---

## 43:00–45:00 — Break It Again: Unapproved Decision

Use:

```python
rejected = {"target": plan["target"], "decision": "rejected"}
```

Expected failure:

```text
PermissionError: Action is not approved
```

Restore the starter fixtures afterward.

---

# Final Series Teaching

## 45:00–47:00 — What Episode 15 Proves

Slide title:

**What AVI Earned**

Show:

- exact target match before action,
- approved decision required,
- rollback required before action,
- pre-change snapshot,
- controlled state change,
- postcheck,
- rollback path,
- final result.

### What to say

> "AVI earned one write capability because we kept the action narrow enough that every part of the path could be inspected and tested."

---

## 47:00–49:00 — What Episode 15 Does NOT Prove

Slide title:

**What This Is Not**

Show:

```text
NOT autonomous production networking
NOT arbitrary CLI execution
NOT blanket write access
NOT proof every change is safe
NOT a reason to remove human control
```

### What to say

> "This is an educational lab simulator. Connecting the design to a real write backend would require the controls from the entire series to be hardened for that environment."

---

## 49:00–51:00 — Series Review

Show the complete journey again:

```text
Tool -> Evidence -> State -> Structure -> Scale -> Context -> Intent -> Knowledge
     -> Harness -> Loop -> Verification -> Reuse -> Approval -> Plan -> Action
```

Then say:

> "Episode 1 asked whether AI could safely observe a network. Episode 15 asks whether it has earned the right to make one bounded change. Everything between those two questions is the engineering."

Then:

> "The model did not earn write access because it became more intelligent. AVI earned capability because the system around it became more trustworthy."

---

## 51:00–52:30 — Homework / Build Forward

Ask viewers to:

1. Keep the write backend simulated until they understand every gate.
2. Add a failing preflight condition.
3. Add an explicit rollback-verification result.
4. Add richer Episode 13 approval validation to `preflight()`.
5. Add a validated Episode 14 plan object instead of the small dictionary.
6. Add one other harmless lab-only action class.
7. Never replace this with arbitrary configuration execution.

---

## 52:30–53:30 — Final Close

### What to say

> "AVI started with one boring pyATS tool. It ended with one boring controlled change. That's not an accident. Good network agents are not built by giving a model more power as quickly as possible. They're built by earning the right to automate the network."

End there.

Do not add a long promotional outro after the final line.

---

# Recording Checklist

Before recording:

- [ ] Default starter produces both `success` and `rolled_back` paths.
- [ ] Lab state starts as `ORIGINAL-LAB-DESCRIPTION`.
- [ ] Target-mismatch demo is rehearsed.
- [ ] Missing-rollback demo is rehearsed.
- [ ] Rejected-approval demo is rehearsed.
- [ ] Any temporary demo edits are restored.
- [ ] Clearly state the backend is in-memory simulation.
- [ ] Do not claim the starter validates approval expiration or full Episode 14 schema linkage.
- [ ] Do not show or suggest a production write target.
- [ ] Terminal output clearly shows before/after state.

---

# Suggested Chapter Markers

Adjust after editing.

```text
00:00 After 14 episodes, AVI finally gets write access
01:00 The final trust question
03:00 The complete AVI journey
06:00 Controlled-action architecture
08:30 Episode 15 starter
10:00 In-memory lab state
12:00 Preflight gates
16:00 Pre-change snapshot and first write
21:00 Postcheck
24:00 Rollback path
28:00 Plan and approval fixtures
30:00 Successful controlled action
34:00 Failed postcheck and rollback
38:00 Block a target mismatch
41:00 Block execution without rollback
43:00 Block an unapproved action
45:00 What Episode 15 proves
47:00 What this is not
49:00 The AVI v2 journey
51:00 Build-forward homework
52:30 Final series close
```

---

# Production Notes

## Let the first write line breathe

When you reach:

```python
LAB_STATE[device][interface]["description"] = plan["new_description"]
```

pause for a moment.

You have spent fourteen episodes building toward the first state-changing line. Use that narrative weight.

## The rollback demo is the climax

The successful path is necessary.

The failed-postcheck path is the stronger demonstration because it proves AVI's definition of success is not merely "the write executed."

## Keep the finale grounded

Do not turn the last episode into a claim that autonomous networking is solved.

The strongest closing message is the opposite: the path from observation to action requires deliberate engineering layers around the model.

## Series north star

> **AVI has to earn the right to automate the network.**
