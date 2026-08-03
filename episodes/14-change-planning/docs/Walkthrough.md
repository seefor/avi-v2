# Episode 14 Walkthrough — Recommendation Before Execution

This is the production-ready recording guide for AVI v2 Episode 14.

## YouTube Package

Recommended title: **Before AI Changes the Network, Make It Show You the Plan | AVI Ep. 14**

Alternates:
- **Build a Reviewable AI Network Change Plan | AVI Ep. 14**
- **AI Should Plan the Change Before It Executes Anything | AVI Ep. 14**

Thumbnail text: **SHOW ME THE PLAN**

Core promise: build a structured, reviewable, reversible change plan that remains explicitly non-executable.

Target runtime: **30–40 minutes**.

---

# Recording Run of Show

## 0:00–0:50 — Cold Open

> "Generating configuration commands is easy. Generating a change another engineer can review, validate, measure, and reverse is the engineering work. Today AVI learns to plan before it ever executes."

Flash the `ChangePlan` JSON and highlight `execution_allowed: false`.

## 0:50–2:15 — Trust Question

Slide: **Can Another Engineer Review Exactly What AVI Proposes Before Anything Runs?**

```text
Finding + Approval -> Change Plan -> Validation -> Review
                                      |
                                      +-> NO EXECUTION
```

## 2:15–4:00 — Architecture

```text
Verified finding
      +
Valid approval
      ↓
ChangePlan
      ↓
Pydantic validation
      ↓
Reviewable artifact
      ↓
execution_allowed = false
```

> "A plan is not execution. That separation is intentional."

## 4:00–5:30 — Starter Orientation

Open:

```text
episodes/14-change-planning/avi_pilot_14_change_plan.py
```

Run:

```bash
python episodes/14-change-planning/avi_pilot_14_change_plan.py
```

Focus on:
- `ChangePlan`
- field constraints
- `plan_stays_non_executable()`
- the narrow interface-description plan in `main()`

## 5:30–11:00 — Walk Through `ChangePlan`

Show the exact model:

```python
class ChangePlan(BaseModel):
    objective: str
    target: str
    evidence_refs: list[str] = Field(min_length=1)
    approval_ref: str
    proposed_commands: list[str] = Field(min_length=1)
    expected_diff: str
    prechecks: list[str] = Field(min_length=1)
    postchecks: list[str] = Field(min_length=1)
    rollback_commands: list[str] = Field(min_length=1)
    risks: list[str]
    execution_allowed: bool = False
```

Explain each group:

### Why
- `objective`
- `evidence_refs`
- `approval_ref`

### What
- `target`
- `proposed_commands`
- `expected_diff`

### Before
- `prechecks`

### After
- `postchecks`

### Recovery
- `rollback_commands`
- `risks`

### Control
- `execution_allowed`

### What to say

> "A network change is more than a command. The command is one small part of a reviewable change artifact."

## 11:00–14:00 — Non-Executable Validator

Highlight:

```python
@model_validator(mode="after")
def plan_stays_non_executable(self):
    if self.execution_allowed:
        raise ValueError("Episode 14 plans must remain non-executable")
```

### Key line

> "Even if someone tries to flip the flag, Episode 14 rejects the object. Planning and execution stay separated in code, not just in the narration."

## 14:00–18:00 — Happy-Path Plan

Walk through the real starter plan:

```text
Objective: test-only interface description
Target: lab-r1:GigabitEthernet1
Evidence: evt-501, evt-502
Approval: approval-demo-001
Commands: interface + description
Prechecks: capture current description + confirm lab-r1
Postcheck: read description and compare expected value
Rollback: restore ORIGINAL-LAB-DESCRIPTION
Risk: incorrect target selection
```

Run the starter and review the JSON as if it were a change ticket.

### What to say

> "This is the point where I want another network engineer to be able to say: I understand what will change, why, how we know it worked, and how to put it back."

## 18:00–21:00 — Prechecks and Postchecks

Explain the difference:

```text
PRECHECK = should we proceed?
POSTCHECK = did the expected result happen?
```

Show the exact starter fields.

> "A precheck protects our assumptions. A postcheck measures the outcome. They solve different problems."

## 21:00–23:00 — Expected Diff

Highlight:

```python
expected_diff="Interface description changes to AVI-LAB-TEST"
```

Explain that a stronger future plan could make expected state machine-verifiable rather than free text.

## 23:00–26:00 — Break It on Purpose: Remove Rollback

Temporarily change:

```python
rollback_commands=[]
```

Run again.

Pydantic should reject the plan because:

```python
Field(min_length=1)
```

### What to say

> "If we haven't decided how to recover before the change, this plan is not ready."

Restore the rollback list.

## 26:00–29:00 — Break It Again: Remove Postcheck

Temporarily change:

```python
postchecks=[]
```

Run again and show validation failure.

### What to say

> "A plan that cannot measure success is incomplete."

Restore the postcheck.

## 29:00–31:00 — Break It Again: Try to Enable Execution

Temporarily set:

```python
execution_allowed=True
```

Run again.

Expected custom validation failure:

```text
Episode 14 plans must remain non-executable
```

### What to say

> "We spent this entire episode planning. AVI still has not earned execution yet."

Restore `False`/default behavior.

## 31:00–33:00 — What This Starter Does Not Validate Yet

Be explicit:

- it requires an `approval_ref` but does not resolve and cryptographically/semantically verify the Episode 13 approval record,
- it does not parse or allowlist the command content yet,
- it does not execute prechecks,
- it does not run rollback,
- it only validates the plan artifact.

This is the bridge to Episode 15.

## 33:00–35:00 — What AVI Still Cannot Do

AVI now has the prerequisites for one controlled action, but execution still needs:

- exact plan/approval/target match,
- preflight checks,
- pre-change snapshot,
- bounded execution,
- post-change verification,
- evidence at every stage,
- rollback on failed success criteria.

## 35:00–36:30 — Homework

1. Add a second risk.
2. Add a platform field.
3. Remove rollback and confirm failure.
4. Remove postchecks and confirm failure.
5. Attempt `execution_allowed=True` and confirm rejection.
6. Make the expected diff more machine-verifiable.

## 36:30–37:30 — Next Flight

Show all previous layers converging:

```text
Evidence
State
Validation
Context
Intent
RAG
Harness
Loop
Verification
MCP
Approval
Plan
   ↓
CONTROLLED ACTION
```

### What to say

> "We have spent fourteen episodes refusing to give AVI write access. In Episode 15 we finally let it make one intentionally boring lab change—and prove every control around it."

End on that line.

---

# Recording Checklist

- [ ] Happy-path plan validates.
- [ ] Empty rollback failure is rehearsed and restored.
- [ ] Empty postcheck failure is rehearsed and restored.
- [ ] `execution_allowed=True` failure is rehearsed and restored.
- [ ] Do not imply approval linkage is fully validated by this starter.
- [ ] Do not imply any command executes in Episode 14.

# Suggested Chapters

```text
00:00 Configuration commands are the easy part
00:50 The change-plan trust question
02:15 Architecture
04:00 Episode 14 starter
05:30 The ChangePlan contract
11:00 Keep planning non-executable
14:00 Review the lab change plan
18:00 Prechecks vs postchecks
21:00 Expected diff
23:00 Missing rollback failure
26:00 Missing postcheck failure
29:00 Reject execution_allowed=True
31:00 What this starter does not validate yet
33:00 What AVI still cannot do
35:00 Homework
36:30 Episode 15 tease
```

## Series takeaway

> **A generated command is not a change plan. AVI must make the change reviewable before it ever makes it executable.**
