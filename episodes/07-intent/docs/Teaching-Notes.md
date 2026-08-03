# Episode 07 Teaching Notes — Intent

## Source of Truth Does Not Mean Source of Current State

A source of truth normally represents intended or authoritative inventory/configuration data. The live device represents observed operational state. Those are related but not interchangeable.

## Why Drift Needs Provenance

A useful finding should tell the engineer:
- what was expected,
- what was observed,
- where each value came from,
- when each source was last updated/observed,
- whether the comparison is reliable enough to act on.

## Do Not Automatically Favor NetBox

NetBox may be wrong, stale, incomplete, or not authoritative for a particular field. The live device may also contain unauthorized drift. The comparator should reveal disagreement rather than decide the remediation by assumption.

## Useful Status Vocabulary

Possible states:
- `match`
- `drift`
- `unknown`
- `unmanaged`
- `stale`

The exact names matter less than keeping uncertainty explicit.

## Connection to Automation Design

This is where intent-based automation begins to become safer. A later workflow can reason over a drift artifact instead of comparing strings ad hoc.

## Key Takeaway

Network automation should preserve the difference between what we intended and what is actually happening.