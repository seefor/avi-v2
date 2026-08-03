# Episode 04 — Structure

## Why agent output must be validated

AVI now has state objects. This episode makes those objects safe for downstream use by adding schemas and deterministic validation.

## What AVI Gains

- Pydantic-style schemas
- required fields and allowed values
- explicit null handling
- schema versioning
- controlled validation failures
- JSON fixtures for success and failure cases

## Trust Question

Can another system consume AVI output without first reading it like a human?

## Architecture

```text
candidate state -> schema validation -> valid object
                            |
                            +-> controlled failure
```

## Build Goals

Validate:

- parseability
- required keys
- data types
- allowed values
- evidence references
- logical constraints
- missing or unknown values

Example logical rule: established BGP peers cannot exceed total peers.

## Demo

Show three results:

1. valid structured output,
2. missing required field,
3. unsupported or invented value.

Only the first moves forward.

## Safety Boundary

A schema proves that data has the expected shape. It does not prove that the underlying observation is true or that the model's conclusion is correct.

## Next

Episode 5 takes validated observations across multiple devices without losing per-device evidence.
