# Episode 06 Troubleshooting — Context

## Relevant Source Is Missing

Inspect the context-selection rules before blaming the model. Confirm the source is eligible, within the freshness window, and associated with the selected device/question.

## Stale Data Is Still Included

Check timestamp parsing, timezone handling, and the `max_age` comparison. Use UTC or consistently timezone-aware timestamps.

## Context Is Too Large

Look for duplicate state, full raw outputs when summaries would suffice, unrelated devices, and repeated historical events.

## Sensitive Fields Appear

Move redaction/exclusion before prompt construction. Do not rely on the model to ignore credentials that were already inserted.

## Same Question Produces Very Different Context

Print the inclusion/exclusion decision for each source so you can audit the assembler deterministically.

## Missing Context Gets Replaced by a Guess

Add an explicit missing-source marker and require the response path to preserve uncertainty.

## Debugging Order

```text
1. Print candidate sources
2. Print eligibility decisions
3. Check freshness
4. Check relevance/device scope
5. Check exclusions/redaction
6. Check final context size
```