# Episode 03 Teaching Notes — State

## Observation Is Not Intent

This episode describes what the network appears to be doing. It does not decide whether the state is correct or desired. That distinction becomes important when NetBox enters in Episode 7.

## Why Normalize

Network platforms expose similar concepts with different text formats. Normalization creates stable internal names so later logic can ask for `operational_status` instead of re-parsing vendor output at every layer.

## Preserve Provenance

Every normalized object should retain:
- where the observation came from,
- when it was observed,
- which evidence event supports it.

Without provenance, state becomes detached from its source.

## Unknown Is Better Than Invented

If an IP address, admin status, or BGP field is missing, the system should represent that absence explicitly. A model or parser that fills gaps with plausible values creates false certainty.

## Parsing Options

For a production system, structured pyATS/Genie parsers are preferable when available. For educational fixtures, deterministic parsing is acceptable as long as the limitations are explicit.

## Optional Analogy

Raw CLI is a photograph. Normalized state is the labeled inventory created from that photograph. Keep the photograph because later somebody may challenge the label.

## Key Takeaway

A useful agent needs a stable operational data model before it needs more reasoning.