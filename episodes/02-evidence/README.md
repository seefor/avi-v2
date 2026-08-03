# Episode 02 — Evidence

## How do we prove what the agent actually saw?

AVI can observe a device. Now every observation must leave an evidence trail.

## What AVI Gains

- evidence IDs and run IDs
- persistent JSONL records
- timestamps and duration
- tool name, target, arguments, status, and error details
- result summaries suitable for later verification
- basic redaction rules

## Trust Question

If AVI later says an interface was down or a BGP peer was idle, can an engineer inspect the exact tool event behind that claim?

## Architecture

```text
Tool Request -> Validation -> Execution -> Result
                    |             |
                    +-------------+-> Evidence Recorder -> JSONL
```

## Build Goals

Create a reusable evidence recorder that stores one immutable record per tool event. Separate raw sensitive data from the compact evidence summary passed to later layers.

Suggested record fields:

```json
{
  "run_id": "uuid",
  "evidence_id": "evt-uuid",
  "timestamp": "ISO-8601",
  "tool": "get_interface_status",
  "target": "lab-r1",
  "arguments": {},
  "status": "success",
  "duration_ms": 412,
  "summary": {},
  "error": null
}
```

## Demo

- successful tool call creates evidence
- blocked request creates evidence
- failed connection creates evidence
- review the JSONL file and correlate it to terminal output

## Safety Boundary

Evidence must not leak credentials, tokens, or secrets. Logging is part of the control plane, not a reason to record everything blindly.

## AVI Still Cannot

Evidence is still raw observation. AVI does not yet have a normalized model of network state.

## Next

Episode 3 turns pyATS observations into explicit state objects that humans and later automation can reason over consistently.
