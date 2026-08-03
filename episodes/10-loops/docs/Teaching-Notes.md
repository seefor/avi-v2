# Episode 10 Teaching Notes — Loops

## Agentic Does Not Mean Unbounded

An agent loop is useful when the system needs to gather information iteratively. Operational safety requires hard application limits independent of model preference.

## Progress Is the Important Signal

A new iteration should add something:
- new evidence,
- a materially different hypothesis,
- a different approved tool/argument,
- closure on an unresolved question.

Repeating the same failed call is not progress.

## Duplicate Detection

Track tool name plus normalized arguments. This lets the controller recognize an identical request even if the model phrases the explanation differently.

## Termination Reasons Matter

Useful reasons include:
- sufficient evidence,
- max iterations,
- max runtime,
- duplicate request,
- tool unavailable,
- authorization block,
- unresolved/escalated.

Explicit stop reasons make loops auditable.

## Escalation Is a Successful Safety Outcome

The loop does not need to solve every incident. Recognizing insufficient evidence and handing the case to an engineer is often the correct result.

## Key Takeaway

A trustworthy agent loop is a bounded state machine with evidence and progress checks—not an open-ended conversation with tools.