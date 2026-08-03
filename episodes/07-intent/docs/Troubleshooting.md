# Episode 07 Troubleshooting — Intent

## Everything Shows as Drift

Check field normalization first. Intent and observed sources may use different interface names, capitalization, status vocabularies, or data types.

## NetBox Record Is Not Found

Verify the lookup key: device name, interface ID, prefix, or other identifier. A naming mismatch is not the same as "no intent exists."

## Stale Intent Is Treated as Current

Preserve the source update/version timestamp and apply the stale-data policy before comparison.

## Missing Intent Produces a Fake Expected Value

Do not fill absent intent with defaults unless the policy explicitly defines them. Report unmanaged/unknown instead.

## Observed Evidence ID Is Missing

Trace the state object back to Episode 3/4 and ensure provenance survives into the comparison record.

## Comparison Uses Strings for Everything

Normalize types before comparing. Boolean, numeric, prefix, and enum values should not rely only on text equality.

## Debugging Order

```text
1. Print intent record
2. Print observed state
3. Normalize identifiers/types
4. Check freshness
5. Compare one field at a time
6. Inspect final provenance/status
```