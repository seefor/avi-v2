# Episode 11 Teaching Notes — Verification

## Verification vs. Reasoning

Reasoning proposes explanations. Verification checks whether the required evidence exists and actually supports the claim.

## Evidence Quality Over Model Tone

Models can express weakly supported ideas with strong language. Confidence should be derived from factors such as source quality, freshness, corroboration, and completeness.

## Claim-to-Evidence Mapping

Every supported finding should retain explicit evidence references. A human should be able to follow the path from the final claim back to the underlying observations.

## Unsupported Is Not the Same as False

A claim may be plausible but unsupported by current evidence. That should remain a hypothesis or unresolved possibility rather than being promoted to a finding.

## Limitations Matter

Examples:
- no historical change data,
- stale intent source,
- only one observation point,
- failed tool call,
- incomplete topology.

The final answer becomes more useful when these constraints are explicit.

## Key Teaching Phrase

"AVI should not ask, 'Does this explanation sound right?' It should ask, 'What evidence would have to exist for me to call this supported?'"

## Key Takeaway

Verification turns evidence-backed claims into a separate engineering step instead of trusting fluent model output.