# Episode 08 Teaching Notes — RAG

## RAG Adds Knowledge, Not Live Truth

Operational documents explain procedures, standards, known issues, and escalation paths. They are not observations of the current device.

Keep these categories separate:
- observed network evidence,
- intended state,
- retrieved operational knowledge.

## Why Metadata Must Survive Chunking

A chunk without source identity is difficult to audit. Preserve document title, section, version/date, and a stable source ID so the final response can cite the original guidance.

## Retrieval Failure Is Important

If no relevant document exists, AVI should say that. The absence of retrieval should not cause the model to synthesize an imaginary runbook.

## Stale Documentation

RAG systems can confidently retrieve outdated procedures. Version/date metadata and corpus curation are part of operational safety.

## Retrieval Score Is Not Authority

A high similarity score means the text resembles the query. It does not prove the document is current, authoritative, or applicable to the observed device.

## Useful Teaching Phrase

"RAG tells AVI what our documentation says. pyATS tells AVI what the network says. Those are different evidence classes."

## Key Takeaway

RAG becomes trustworthy when retrieval is cited, source-aware, freshness-aware, and allowed to return no answer.