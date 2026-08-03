# Episode 05 — Scale

## What changes when AVI looks at multiple devices?

A single-device demo hides important operational problems. AVI now has to observe a small fleet while preserving individual evidence and handling partial failure.

## What AVI Gains

- inventory-driven target selection
- bounded concurrency
- per-device timeout handling
- partial success reporting
- per-device evidence preservation
- fleet rollups without hiding detail

## Trust Question

Can AVI summarize multiple devices without flattening away the evidence that explains each result?

## Architecture

```text
Inventory
   -> bounded batch runner
       -> device A -> evidence/state
       -> device B -> evidence/state
       -> device C -> timeout/error
   -> rollup summary + per-device detail
```

## Build Goals

The multi-device runner should:

- limit concurrency,
- isolate one device failure from others,
- preserve timestamps and evidence IDs,
- report completed, degraded, failed, and unreachable targets separately.

## Demo

Use a mixed result:

- one healthy device,
- one degraded device,
- one unreachable device.

The final result should make all three conditions visible.

## Safety Boundary

Scale does not justify broader permissions. The same read-only command and target policies still apply to every device.

## Next

Episode 6 asks a harder question: when AVI has more data available, what information should actually be placed in the model context?
