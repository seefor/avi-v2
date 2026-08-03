# Episode 10 Troubleshooting — Loops

## Loop Never Stops

Confirm limits are enforced by the controller before each new iteration/tool call. Do not rely on the prompt to remember the limits.

## Duplicate Detection Misses Repeated Calls

Normalize arguments before comparison. Ordering, whitespace, or equivalent defaults can make identical calls appear different.

## Loop Stops Too Early

Inspect the "enough evidence" rule. Make sure one successful tool event is not automatically treated as proof of the full hypothesis.

## Runtime Limit Is Inaccurate

Use a monotonic clock for elapsed execution time.

## Failure Causes Immediate Crash

Convert tool exceptions into structured failed events so the controller can decide whether to change strategy or escalate.

## Final Result Has No Stop Reason

Make termination reason a required field in run state/final output.

## Debugging Order

```text
1. Print iteration state
2. Print prior tool calls
3. Check normalized duplicate key
4. Check progress decision
5. Check limits
6. Check final termination reason
```