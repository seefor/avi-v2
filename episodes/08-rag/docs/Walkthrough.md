# Episode 08 Walkthrough — Give AVI Runbooks Without Confusing Guidance with Truth

This is the production-ready recording guide for AVI v2 Episode 8.

## YouTube Package

Recommended title: **Build RAG for Network Operations Without Losing Source Trust | AVI Ep. 8**

Alternates:
- **Give Your AI Network Agent Runbooks with RAG | AVI Ep. 8**
- **RAG for Network Troubleshooting: Evidence vs. Guidance | AVI Ep. 8**

Thumbnail text: **RUNBOOKS + LIVE STATE**

Core promise: retrieve relevant operational knowledge with source identity while keeping documents separate from live network evidence.

Target runtime: **35–45 minutes**.

---

# Recording Run of Show

## 0:00–0:50 — Cold Open

> "Live network state tells AVI what is happening. It does not tell AVI how our team normally troubleshoots that condition. Today we give AVI runbooks—but we're going to be very careful not to confuse a document with live network truth."

Quickly show the BGP query and one retrieved source.

## 0:50–2:15 — Trust Question

Slide: **Can AVI Use Runbooks Without Treating Them as Live Evidence?**

```text
LIVE STATE = what is happening
RUNBOOK = what engineers normally check
```

> "Those two sources are both useful, but they answer different questions."

## 2:15–4:00 — Architecture

```text
knowledge/*.md
      ↓
   retrieve()
      ↓
source + score + matched terms + text
      ↓
operational knowledge context
      +
current network evidence
```

Explain that this starter intentionally uses transparent lexical retrieval rather than embeddings so viewers can see exactly why a document matched.

## 4:00–5:30 — Run Location Matters

Episode 8 uses a relative knowledge path:

```python
CORPUS = Path("knowledge")
```

So run it from the episode directory:

```bash
cd episodes/08-rag
python avi_pilot_08_rag.py
```

### What to say

> "This is one of those little details that matters when someone follows the video later. The corpus path is relative to the current working directory."

## 5:30–8:00 — Show the Knowledge Folder

Open:

```text
episodes/08-rag/knowledge/
```

Show the sample BGP troubleshooting runbook.

Explain why a real corpus should preserve:

- source identity,
- title,
- section/chunk identity,
- document date/version,
- retrieved text.

Be explicit that the current starter retrieves whole Markdown files and does not yet implement production chunking/version metadata.

## 8:00–11:00 — `tokenize()`

Open:

```text
episodes/08-rag/avi_pilot_08_rag.py
```

Highlight:

```python
def tokenize(text: str) -> set[str]:
    return {token.strip(".,:;!?()[]").lower() for token in text.split() if len(token) > 2}
```

### What to say

> "This is deliberately unsophisticated. We're normalizing words into a set so we can build a retrieval path that is easy to explain and debug."

> "The point of Episode 8 is the retrieval contract and source trust—not pretending this tiny tokenizer is the final search engine."

## 11:00–17:00 — `retrieve()`

Walk through the function in chunks.

### Query terms

```python
query_terms = tokenize(query)
```

### Corpus scan

```python
for path in CORPUS.glob("*.md"):
```

### Overlap

```python
overlap = query_terms & tokenize(text)
if not overlap:
    continue
```

### Result contract

```python
{
    "source_id": path.stem,
    "title": ...,
    "path": str(path),
    "score": len(overlap),
    "matched_terms": sorted(overlap),
    "text": text,
}
```

### Ranking

```python
return sorted(results, key=lambda item: item["score"], reverse=True)[:top_k]
```

### Teaching point

> "What I like about this starter is that I can inspect why a source ranked: the matched terms are right there. Later, a vector database can improve semantic retrieval, but source identity and traceability still need to survive."

## 17:00–21:00 — Happy-Path BGP Demo

The starter asks:

```text
BGP neighbor is Idle and receiving zero prefixes
```

Run:

```bash
python avi_pilot_08_rag.py
```

Review:

1. `source_id`,
2. title,
3. score,
4. matched terms,
5. source path,
6. retrieved text.

### What to say

> "A strong final AVI response would keep three sections separate: what the network reports, what the runbook recommends, and what we still don't know."

Do not imply the current starter already calls an LLM or combines live state. It demonstrates retrieval only.

## 21:00–24:00 — Verify the Citation Manually

Open the returned Markdown file and find the terms that caused the match.

### What to say

> "This is a habit I want throughout the series. Don't just trust the retrieval result because it has a score. Open the source and verify it."

## 24:00–27:00 — Break It on Purpose: No-Result Query

Temporarily change:

```python
query = "wireless controller certificate renewal process"
```

or another topic not present in the corpus.

Run again.

Expected message:

```text
No relevant operational knowledge found. Do not invent guidance.
```

### What to say

> "No result is a valid result. Retrieval failure should not become invented company policy."

Restore the original BGP query afterward.

## 27:00–30:00 — Break Retrieval Quality on Purpose

Use a vague query containing generic terms likely to overlap weakly with multiple documents.

Explain:

- lexical overlap is not semantic understanding,
- longer documents may win by term count,
- production retrieval needs better chunking/ranking/evaluation.

This is a teaching demo, not a bug fix.

## 30:00–32:00 — Safety Boundary

Slide:

```text
RUNBOOK CAN:
recommend checks
provide procedures
explain escalation

RUNBOOK CANNOT:
prove current state
override evidence
authorize a change
```

> "RAG is a context source, not a control plane."

## 32:00–34:00 — What AVI Still Cannot Do

AVI now has tools, evidence, state, context, intent, and retrieval—but these are still largely separate episode components.

AVI still needs:

- centralized orchestration,
- model/tool policy,
- unified run state,
- consistent validation and evidence handling.

## 34:00–35:30 — Homework

1. Add a second operational runbook.
2. Ask one covered and one uncovered question.
3. Add basic document date/version metadata.
4. Change `top_k` and inspect ranking.
5. Verify every result manually against its source.

## 35:30–36:30 — Next Flight

```text
Tools + Evidence + State + Context + Intent + RAG
                         ↓
                     AVI Harness
```

> "Episode 9 is where the architecture starts feeling like a real application. We're putting the model, tools, context, policy, evidence, validation, and run state behind one controlled harness."

---

# Recording Checklist

- [ ] Run Episode 8 from `episodes/08-rag`.
- [ ] BGP query returns at least one sample document.
- [ ] No-result query is rehearsed.
- [ ] Original query is restored afterward.
- [ ] Do not claim embeddings/vector search are implemented.
- [ ] Do not claim live pyATS state is combined by this starter.
- [ ] Manually open the cited source on screen.

# Suggested Chapters

```text
00:00 Live state is not operational knowledge
00:50 The RAG trust question
02:15 Architecture
04:00 Run location and corpus path
05:30 The knowledge corpus
08:00 Transparent tokenization
11:00 Building retrieval
17:00 BGP retrieval demo
21:00 Verify the source
24:00 No-result demo
27:00 Where simple retrieval breaks
30:00 RAG safety boundary
32:00 What AVI still cannot do
34:00 Homework
35:30 Episode 9 tease
```

## Series takeaway

> **Retrieved guidance can help AVI decide what to inspect next, but it is never a substitute for current network evidence.**
