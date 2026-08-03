"""AVI v2 Episode 08: tiny transparent retrieval demo for operational knowledge."""

from __future__ import annotations

import json
from pathlib import Path

CORPUS = Path("knowledge")


def tokenize(text: str) -> set[str]:
    return {token.strip(".,:;!?()[]").lower() for token in text.split() if len(token) > 2}


def retrieve(query: str, top_k: int = 3) -> list[dict]:
    query_terms = tokenize(query)
    results = []
    for path in CORPUS.glob("*.md"):
        text = path.read_text(encoding="utf-8")
        overlap = query_terms & tokenize(text)
        if not overlap:
            continue
        results.append({
            "source_id": path.stem,
            "title": text.splitlines()[0].lstrip("# ") if text.splitlines() else path.name,
            "path": str(path),
            "score": len(overlap),
            "matched_terms": sorted(overlap),
            "text": text,
        })
    return sorted(results, key=lambda item: item["score"], reverse=True)[:top_k]


def main() -> None:
    query = "BGP neighbor is Idle and receiving zero prefixes"
    results = retrieve(query)
    print(json.dumps(results, indent=2))
    if not results:
        print("No relevant operational knowledge found. Do not invent guidance.")


if __name__ == "__main__":
    main()
