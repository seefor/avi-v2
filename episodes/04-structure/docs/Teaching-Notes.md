# Episode 04 Teaching Notes — Structure

## Why Structure Matters

Agents often generate output that is syntactically valid but operationally wrong. A schema creates a deterministic boundary between free-form reasoning and machine-consumable data.

## Schema Validation Does Not Prove Truth

A perfectly valid object can still describe an incorrect observation. Validation answers: "Does this data obey the contract?" Evidence and later verification answer different questions.

## Pydantic-Style Models

Typed models are useful because they make required fields, enums, nullability, nested objects, and validation errors explicit. They also make the code self-documenting for learners.

## Logical Constraints

Some invalid states pass type checks. Examples:
- established peers > total peers,
- end time before start time,
- success status with a required error field populated,
- evidence reference missing from a claimed observation.

## Versioning

Schema versioning matters when multiple clients or later episodes reuse an output contract. It gives the system a way to evolve without silently changing meaning.

## Key Phrase

"Structured output is not trustworthy because it is JSON. It is trustworthy only to the extent that we validate the contract and preserve evidence behind it."

## Key Takeaway

Validation should fail closed. Bad structure should stop the workflow rather than get repaired by guesswork downstream.