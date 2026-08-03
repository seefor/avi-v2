# Episode 02 Teaching Notes — Evidence

## Evidence vs. Logging

Traditional logs often answer, "What did the application print?" AVI evidence should answer, "What operational event occurred, against which target, with what result, and what identifier can later claims reference?"

That makes evidence a first-class data model rather than a pile of strings.

## Why JSONL

JSON Lines is intentionally boring and useful for an educational build:
- one event per line,
- append-friendly,
- human-readable,
- easy to parse with Python or `jq`,
- easy to replace later with a database or event store.

## Run ID vs. Evidence ID

Use a run ID for the full investigation and an evidence ID for each individual event. Later a verified finding may reference multiple evidence IDs from one run.

## Failure Is Evidence

A timeout or policy rejection is not proof of network state. It is proof that an attempted observation failed or was blocked. This distinction prevents AVI from converting missing data into a false operational conclusion.

## Redaction

The recorder must be selective. Useful metadata can include tool, target, timing, normalized arguments, outcome, and summary. Secrets, credentials, tokens, and unnecessary raw payloads should be excluded or redacted.

## Optional Analogy

Treat the evidence recorder like a flight data recorder. Its value is not that it makes the plane fly. Its value is that later we can reconstruct what the system actually did.

## Key Takeaway

If AVI cannot point back to evidence, later explanations are difficult to audit, verify, or trust.