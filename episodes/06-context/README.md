# Episode 06 — Context

## What information should AVI actually see?

AVI now has tools, evidence, structured state, and multiple-device observations. The next problem is not collecting more data. It is selecting the right data for the current decision.

## What AVI Gains

- explicit context objects
- source labels and observation age
- context selection rules
- stale-data handling
- token/context budgets
- inclusion and exclusion policies

## Trust Question

Can AVI receive enough information to reason usefully without burying the decision in stale, irrelevant, duplicated, or sensitive context?

## Architecture

```text
Question
  + current evidence
  + selected topology
  + relevant state
  + prior tool results
        -> Context Assembler
              -> curated context
                    -> prompt/model
```

## Build Goals

Create a context policy that decides:

- which sources are eligible,
- how old an observation may be,
- which devices are relevant,
- what history is retained,
- what must never be included,
- when missing context should be explicit.

Example policy:

```yaml
include:
  - current_tool_results
  - selected_topology
  - active_incident_summary
exclude:
  - credentials
  - unrelated_configs
  - stale_observations
max_age_minutes: 15
max_context_tokens: 12000
```

## Demo

Ask the same troubleshooting question three ways:

1. with almost no operational context,
2. with an excessive data dump,
3. with selected relevant context.

Compare usefulness and traceability.

## Safety Boundary

Context assembly can improve reasoning, but it cannot turn missing evidence into truth. If a required source is unavailable, AVI must say so.

## Next

Episode 7 adds intended state so AVI can compare what the network is doing with what it is supposed to be doing.
