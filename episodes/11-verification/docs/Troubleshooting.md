# Episode 11 Troubleshooting — Verification

## Everything Is Marked Supported

Inspect the verification rules. A claim should require specific evidence conditions rather than only the presence of any evidence ID.

## Evidence ID Cannot Be Resolved

Confirm the evidence store/fixture contains the referenced event and that IDs are copied exactly through state and reasoning layers.

## Confidence Is Always High

Tie confidence to measurable evidence properties. Do not accept model-generated confidence as the only input.

## Unsupported Claim Is Treated as False

Preserve a separate unsupported/unresolved status unless evidence directly contradicts the claim.

## Limitations Are Empty

Add deterministic checks for missing evidence classes, stale sources, or incomplete observations.

## Verification Changes When Wording Changes

Normalize the claim or use explicit verification criteria so small prose differences do not bypass the rule.

## Debugging Order

```text
1. Print candidate claim
2. Resolve each evidence reference
3. Check required evidence classes
4. Check source quality/freshness
5. Apply support rule
6. Print limitations + final status
```