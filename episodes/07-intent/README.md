# Episode 07 — Intent

## NetBox vs. live network state

AVI can now observe the network and assemble relevant context. This episode adds intended state so AVI can compare what the network is doing with what it is supposed to be doing.

## What AVI Gains

- an intent-provider abstraction
- NetBox-backed intended state
- explicit observed-vs-intended comparisons
- drift findings with source identity
- missing-intent and ambiguous-intent handling

## Trust Question

Can AVI compare intent and operation without treating either source as infallible?

## Architecture

```text
NetBox / intent source -----------+
                                  |
                                  v
                           Intent Comparator -> drift finding
                                  ^
                                  |
pyATS / observed state -----------+
```

## Build Goals

Represent intended and observed state separately. A comparison result should retain:

- intent source
- intent record identity/version when available
- observed source and timestamp
- comparison field
- expected value
- observed value
- status: match, drift, unknown, unmanaged, or stale
- evidence references

## Demo

Show four cases:

1. observed state matches intent,
2. operational drift,
3. no intended-state record,
4. stale or ambiguous intended state.

## Safety Boundary

A drift finding is a review artifact, not an automatic change request. AVI does not assume the device is wrong simply because NetBox differs.

## Next

Episode 8 adds operational knowledge through RAG so AVI can retrieve the runbooks and standards that help explain what engineers normally check next.
