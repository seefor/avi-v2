# Episode 08 Troubleshooting — RAG

## No Documents Are Retrieved

Run the episode from `episodes/08-rag` so relative knowledge-folder paths resolve correctly.

```bash
cd episodes/08-rag
python avi_pilot_08_rag.py
```

## Wrong Document Is Ranked First

Inspect chunk size, query terms, and corpus overlap. A tiny demo corpus can produce misleading similarity when several documents reuse the same networking vocabulary.

## Citation Loses Source Information

Check ingestion metadata. Source ID/title/section must be attached before chunking and preserved through retrieval.

## Old Runbook Is Used

Add and inspect document version/date. Retrieval similarity alone should not hide staleness.

## No-Result Query Still Produces Advice

Separate retrieval output from model fallback. Require an explicit no-result path when the corpus has no relevant source.

## Relative File Path Error

Confirm the working directory and knowledge-folder path. Prefer paths resolved relative to the script in production-quality code.

## Debugging Order

```text
1. Confirm files load
2. Inspect chunks + metadata
3. Run retrieval only
4. Inspect ranked sources
5. Verify citations
6. Add reasoning after retrieval works
```