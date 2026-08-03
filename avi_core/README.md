# avi_core

`avi_core` is the reusable application layer that grows across the AVI v2 series.

Early episodes may keep code local so each concept is easy to see. As capabilities stabilize, shared logic should move here instead of being copied into later episodes.

Planned modules:

```text
avi_core/
├── agent.py
├── configuration.py
├── approvals/
├── changes/
├── context/
├── evidence/
├── execution/
├── guardrails/
├── intent/
├── knowledge/
├── loops/
├── models/
├── state/
├── tools/
└── verification/
```

## Design Rule

The language model is not the application. The application owns tool execution, evidence, context selection, validation, loop limits, verification, approval checks, and change controls.

## Implementation Strategy

Do not create abstractions before an episode needs them. Each module should appear when the series introduces the corresponding engineering problem, then later episodes should import and reuse it.
