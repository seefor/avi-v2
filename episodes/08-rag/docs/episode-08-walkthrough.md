# Episode 08 Walkthrough — RAG

## Video Title
AVI #8 — RAG: Giving AVI Runbooks and Operational Knowledge

## Hook
pyATS can tell AVI that a BGP peer is idle. It cannot tell AVI how your team normally investigates that condition. That is where retrieval becomes useful.

## Talking Points
- RAG is one context-engineering technique
- live state and retrieved guidance are different source types
- citations make retrieved knowledge reviewable
- no relevant result is better than invented guidance

## Demo Flow
1. Show the small runbook corpus.
2. Ingest and retrieve a BGP troubleshooting section.
3. Collect current BGP state.
4. Build one context object containing both sources.
5. Produce a response that cites the runbook and references live evidence separately.
6. Ask an unsupported question and show no-result handling.

## Failure Scenario
Retrieve an outdated or weakly relevant document and show why source/version metadata and relevance thresholds matter.

## Close
AVI now has tools, state, intent, and knowledge. Episode 9 turns those parts into an actual harness so the model operates inside enforceable system controls.
