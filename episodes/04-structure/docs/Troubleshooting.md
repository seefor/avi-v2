# Episode 04 Troubleshooting — Structure

## Valid Fixture Fails

Read the full validation error. Check field names, required fields, enum values, and nested object shape before changing the schema.

## Invalid Fixture Passes

Confirm the rule actually exists in the validator. Type checks alone will not catch cross-field logical errors.

## `null` Handling Is Confusing

Separate "field absent" from "field present but unknown" where that distinction matters. Define optionality deliberately.

## Enum Value Rejected

Compare the normalized state vocabulary from Episode 3 with the schema's allowed values. Fix the mismatch at the contract boundary instead of accepting arbitrary strings.

## JSON Parse Error

Validate syntax before schema rules. A parser failure and a schema failure are different categories and should be reported separately.

## Evidence Reference Missing

Treat provenance as a required field for observations that will be used later. Do not auto-generate a fake evidence ID during validation.

## Debugging Order

```text
1. Parse JSON/data
2. Check required keys
3. Check types
4. Check enum values
5. Check evidence references
6. Check logical constraints
```