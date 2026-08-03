# Episode 02 Troubleshooting — Evidence

## Evidence File Is Not Created

Confirm the script has write permission in the current directory and that the configured path exists.

Run the episode from the repository root as documented:

```bash
python episodes/02-evidence/avi_pilot_02_evidence.py
```

## JSONL Cannot Be Parsed

Each line must be one complete JSON object. Avoid pretty-printing multi-line objects into a JSONL file.

Quick check:

```bash
python -m json.tool <first-record.json>
```

Or parse each line with a short Python loop.

## Duplicate Evidence IDs

Evidence IDs should be generated per event. If IDs repeat, confirm a new UUID/identifier is created inside the event-recording path rather than once at module import.

## Duration Is Wrong

Use a monotonic timer for elapsed duration and wall-clock time for timestamps. Do not subtract local-time strings.

## Secrets Appear in Evidence

Stop and fix redaction before continuing. Check nested arguments as well as top-level fields.

## Blocked Calls Are Missing

Make sure recording happens around validation and execution, not only after successful tool return.

## Failure Looks Like Network State

A failed observation should use a failure status/error field. Do not create a state summary that implies the device itself is down unless evidence supports that claim.