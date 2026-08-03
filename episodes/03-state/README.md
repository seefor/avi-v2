# Episode 03 — State

## Can AVI turn pyATS output into usable network state?

Raw command output is evidence, but later reasoning needs explicit state.

## What AVI Gains

- normalized device, interface, and BGP state objects
- source and observation timestamps
- clear distinction between raw evidence and interpreted state
- predictable field names across observations

## Trust Question

Can AVI describe what the network is doing without inventing fields or hiding the source observation?

## Architecture

```text
pyATS / CLI
    -> raw evidence
        -> normalizer
            -> state object
                -> human / agent context
```

## Build Goals

Introduce typed state models such as:

```text
InterfaceState
- device
- interface
- admin_status
- operational_status
- ip_address
- source
- observed_at
- evidence_id
```

Do the same for device health and BGP neighbor state.

## Demo

- parse one interface observation
- normalize it into a state object
- preserve the source evidence ID
- show missing values explicitly rather than guessing

## Safety Boundary

Normalization describes observed state. It does not decide whether that state is correct, intended, or the root cause of an incident.

## AVI Still Cannot

State objects can still be malformed or inconsistent. Episode 4 adds formal schemas and validation rules.
