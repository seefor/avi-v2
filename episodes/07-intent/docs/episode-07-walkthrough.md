# Episode 07 Walkthrough — Intent

## Video Title
AVI #7 — Intent: NetBox vs. Live Network State

## Hook
A source of truth tells us what we intended. The device tells us what is actually happening. AVI needs both, and it needs to know they are not the same thing.

## Talking Points
- intended state and operational state are separate evidence sources
- drift is a finding, not automatically a fault
- source identity and freshness matter
- missing intent is different from bad intent

## Demo Flow
1. Pull intended interface or BGP data from NetBox.
2. Pull current observed state through AVI.
3. Compare one matching item.
4. Show one drift case.
5. Show a missing intent record.
6. Show stale/ambiguous intent handling.

## Failure Scenario
Use an outdated NetBox value and demonstrate why AVI must label source age instead of blindly recommending a change.

## Close
AVI now knows what the network is doing and what we intended. Episode 8 adds another source of context: operational knowledge from runbooks and troubleshooting documentation.
