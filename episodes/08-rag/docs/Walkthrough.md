# Episode 08 Walkthrough — RAG: Giving AVI Operational Knowledge

## 1. Opening Hook

What to say:

"Live state tells AVI what the network is doing. It does not tell AVI how our team normally troubleshoots that condition. Today we give AVI runbooks and operational knowledge—but we keep retrieved guidance separate from live truth."

## 2. Trust Question

Can AVI use runbooks without confusing documentation with current network evidence?

## 3. Architecture

```text
Runbooks / standards / incident notes
            -> ingestion
            -> retrieval
            -> cited knowledge context
                          +
                 current network state
                          -> AVI reasoning
```

## 4. Run the Starter

```bash
cd episodes/08-rag
python avi_pilot_08_rag.py
```

## 5. Show the Knowledge Corpus

Walk through the sample documents, especially the BGP troubleshooting runbook.

Explain document identity, section, version/date, and why those metadata must survive chunking.

## 6. Explain Chunking and Retrieval

What to say:

"A useful RAG result is not just a paragraph. It needs to tell AVI and the engineer where that paragraph came from."

Show fields such as:
- source ID,
- title,
- section,
- relevance score,
- text,
- version/date.

## 7. Happy-Path BGP Demo

Ask the BGP troubleshooting question.

Combine:
- current pyATS/network evidence,
- one or more cited runbook sections.

Then separate the response into:
1. what the device reports,
2. what the runbook recommends,
3. what remains unknown.

## 8. Source Citation Review

Open the cited document and verify that the retrieved section really supports the recommendation.

## 9. No-Result Demo

Ask a question that is not covered by the local corpus.

What to say:

"No relevant document is a valid result. AVI should not turn retrieval failure into invented policy."

## 10. Break It on Purpose

Add an old or conflicting runbook note and discuss how document date/version should affect trust.

## 11. Safety Boundary

A runbook can recommend a check. It cannot override current state, grant permission, or authorize a change.

## 12. What AVI Still Cannot Do

The capabilities now exist as separate layers. Episode 9 brings them behind one controlled harness.

## 13. Homework

1. Add an interface troubleshooting guide.
2. Add document metadata.
3. Ask one covered and one uncovered question.
4. Verify citations manually.

## 14. Next Flight

"In Episode 9 the LLM stops being the center of the architecture. We build a harness around it that owns tools, context, policy, evidence, validation, and run state."