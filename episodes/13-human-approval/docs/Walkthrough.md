# Episode 13 Walkthrough — Human Approval Is More Than a Yes/No Button

This is the production-ready recording guide for AVI v2 Episode 13.

## YouTube Package

Recommended title: **Human Approval for AI Agents: Scope It or It Doesn't Count | AVI Ep. 13**

Alternates:
- **Build a Real Human-in-the-Loop Approval Gate | AVI Ep. 13**
- **Don't Give AI Generic Approval — Bind It to the Exact Change | AVI Ep. 13**

Thumbnail text: **APPROVED FOR WHAT?**

Core promise: create an approval request and decision record bound to an exact target, exact action, evidence, approver, and expiration.

Target runtime: **25–35 minutes**.

---

# Recording Run of Show

## 0:00–0:50 — Cold Open

> "AVI can observe, investigate, verify, and recommend. That still does not mean it gets to act. Today we're adding human approval—but a generic `approved = true` is not enough."

Flash the valid approval, then the wrong-target rejection.

## 0:50–2:15 — Trust Question

Slide: **Did a Human Approve This Exact Action on This Exact Target?**

```text
Recommendation -> Approval Request -> Human Decision -> Bound Approval
```

> "Approval is not a blanket permission. It should be scoped, attributable, and temporary."

## 2:15–4:00 — Architecture

```text
Verified recommendation
        ↓
create_request()
        ↓
approval packet
        ↓
approve()
        ↓
approval record
        ↓
validate_approval()
        ↓
eligible for planning
```

Stress that Episode 13 does not execute anything.

## 4:00–5:30 — Starter Orientation

Open:

```text
episodes/13-human-approval/avi_pilot_13_approval.py
```

Run:

```bash
python episodes/13-human-approval/avi_pilot_13_approval.py
```

Focus on:
- `create_request()`
- `approve()`
- `validate_approval()`
- built-in wrong-target rejection in `main()`

## 5:30–9:00 — `create_request()`

Show:

```python
{
    "approval_request_id": f"apr-{uuid4()}",
    "target": target,
    "action": action,
    "evidence_refs": evidence_refs,
    "risk": "low",
    "expected_impact": "lab-only metadata change",
    "expires_at": ...,
}
```

### What to say

> "The person approving needs enough context to understand what is being requested. The request has an identity, exact target, exact action, evidence, risk, impact, and a time window."

Be explicit that the starter's request model is intentionally small; richer packets can later include reason, prechecks, rollback expectations, and proposed command details.

## 9:00–12:00 — `approve()`

Highlight:

```python
"request_id": request["approval_request_id"],
"target": request["target"],
"action": request["action"],
"approver": approver,
"decision": "approved",
"expires_at": request["expires_at"],
```

### Key line

> "The decision record copies the target and action because I want the approval to remain bound to what the human actually reviewed."

## 12:00–16:00 — `validate_approval()`

Walk through all three controls.

Decision:

```python
if approval["decision"] != "approved":
    raise PermissionError("Request is not approved")
```

Scope:

```python
if approval["target"] != target or approval["action"] != action:
    raise PermissionError("Approval scope does not match target/action")
```

Expiration:

```python
if datetime.fromisoformat(approval["expires_at"]) <= datetime.now(timezone.utc):
    raise PermissionError("Approval has expired")
```

### What to say

> "Approval has to survive three questions: was it approved, does it match what we're trying to do now, and is it still valid?"

## 16:00–19:00 — Happy-Path Demo

Run the starter.

Show:

- request ID,
- target `lab-r1`,
- action `set_test_description`,
- evidence `evt-401`,
- approver `network-engineer`,
- expiration,
- valid decision.

### What to say

> "This approval only makes the request eligible for the next stage. There is still no execution path here."

## 19:00–22:00 — Built-In Failure: Wrong Target

The starter already validates the same approval against:

```python
target="lab-r2"
```

Show:

```text
Controlled rejection: Approval scope does not match target/action
```

### Key line

> "Approval is not transferable permission. An approval for lab-r1 does not become permission for lab-r2."

## 22:00–25:00 — Break It on Purpose: Wrong Action

Temporarily validate with:

```python
action="shutdown_interface"
```

while keeping `target="lab-r1"`.

Run again and show the same scope mismatch.

Restore the original action afterward.

## 25:00–28:00 — Break It Again: Expired Approval

For the demo, make a copy of the approval and set:

```python
expired["expires_at"] = (datetime.now(timezone.utc) - timedelta(minutes=1)).isoformat()
```

Call `validate_approval()` and show:

```text
Approval has expired
```

Do not permanently change the default 30-minute expiration.

## 28:00–30:00 — What Approval Does Not Prove

Slide:

```text
APPROVED != TECHNICALLY CORRECT
APPROVED != REVERSIBLE
APPROVED != SAFE TO EXECUTE NOW
```

> "Human approval proves authorization for this scoped request. It doesn't replace change engineering."

## 30:00–32:00 — What AVI Still Cannot Do

AVI can prove permission exists, but it still cannot produce a complete, reviewable change packet with:

- prechecks,
- proposed actions,
- expected diff,
- postchecks,
- risks,
- rollback.

## 32:00–33:30 — Homework

1. Create an expired approval and verify rejection.
2. Attempt wrong-target reuse.
3. Attempt wrong-action reuse.
4. Add an explicit rejection decision path.
5. Add a reason field to the approval request.

## 33:30–34:30 — Next Flight

```text
Verified Finding + Valid Approval
              ↓
         Change Plan
              ↓
prechecks / diff / postchecks / rollback
```

> "Episode 14 turns permission into something another network engineer can actually review: a complete change plan. And even then, execution stays disabled."

---

# Recording Checklist

- [ ] Valid approval path runs.
- [ ] Wrong-target rejection is visible.
- [ ] Wrong-action demo is rehearsed and restored.
- [ ] Expired-approval demo is rehearsed.
- [ ] Do not imply approval authorizes immediate execution.
- [ ] Keep the exact target/action binding central to the lesson.

# Suggested Chapters

```text
00:00 Approval is more than yes/no
00:50 The approval trust question
02:15 Architecture
04:00 Episode 13 starter
05:30 Building the approval request
09:00 Recording the human decision
12:00 Validating approval
16:00 Happy-path approval
19:00 Wrong-target rejection
22:00 Wrong-action rejection
25:00 Expired approval
28:00 What approval does not prove
30:00 What AVI still cannot do
32:00 Homework
33:30 Episode 14 tease
```

## Series takeaway

> **Permission should be bound to the exact action, exact target, exact approval record, and a valid time window.**
