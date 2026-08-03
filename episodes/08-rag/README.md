# Episode 08 — RAG

## Giving AVI runbooks and operational knowledge

Live network state answers what is happening. RAG helps AVI retrieve the operational knowledge that explains what engineers normally check next.

## What AVI Gains

- document ingestion
- chunking with document identity
- retrieval over runbooks and standards
- source citations
- document date/version metadata
- no-result handling

## Trust Question

Can AVI use operational knowledge without confusing retrieved guidance with live network state?

## Architecture

```text
Runbooks / standards / incident notes
            -> ingestion
            -> retrieval
            -> cited knowledge context
                          +
                 current network state
                          -> AVI reasoning
```

## Build Goals

Start with a small realistic corpus:

- BGP troubleshooting runbook
- interface troubleshooting guide
- change validation checklist
- escalation procedure
- known-issue note

Every retrieval result should retain:

- source ID
- document title
- section
- relevance score
- retrieved text
- document version/date

## Demo

Ask a BGP troubleshooting question. Combine current pyATS evidence with a cited runbook section and show that AVI distinguishes:

- what the device reports,
- what the runbook recommends,
- what remains unknown.

Then ask a question with no relevant document and show a controlled no-result response.

## Safety Boundary

RAG is a context source, not a source of live truth. A retrieved document cannot override observed state or authorize a change.

## Next

Episode 9 brings these separate layers under a reusable agent harness that enforces policy around the model.
