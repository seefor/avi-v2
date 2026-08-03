# Episode 03 Troubleshooting — State

## Parser Returns No Interfaces

Confirm the fixture or tool output matches the parser expectations. Print the raw evidence before debugging the normalizer.

## Status Values Look Inconsistent

Normalize platform-specific spellings into a controlled vocabulary, but do not collapse distinct concepts such as administratively down vs operationally down.

## Missing Field Raises an Unexpected Exception

Decide whether the field is required at this layer. If the source legitimately omits it, represent the field explicitly as unknown/null and let Episode 4 enforce the formal schema.

## Evidence ID Disappears

Check the mapping step. Provenance fields should be copied into every state object created from that evidence event.

## Timestamp Looks Stale

Record observation time when the network data is collected, not when the normalized object is later printed.

## Raw CLI Changes

If a vendor or lab output format changes, update the parser/normalizer fixture rather than adding guesses. Prefer a structured parser where available.

## Debugging Order

```text
1. Print raw evidence
2. Confirm parser input shape
3. Inspect field mapping
4. Check controlled status values
5. Verify timestamps and evidence IDs
6. Print normalized state
```