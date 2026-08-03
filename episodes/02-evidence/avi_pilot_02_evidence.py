"""AVI v2 Episode 02: durable evidence records for tool activity."""

from __future__ import annotations

import json
import time
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable

EVIDENCE_FILE = Path("avi_evidence.jsonl")


def record_event(*, tool: str, target: str, arguments: dict[str, Any], status: str,
                 duration_ms: int, summary: dict[str, Any] | None = None,
                 error: str | None = None) -> dict[str, Any]:
    event = {
        "run_id": str(uuid.uuid4()),
        "evidence_id": f"evt-{uuid.uuid4()}",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "tool": tool,
        "target": target,
        "arguments": arguments,
        "status": status,
        "duration_ms": duration_ms,
        "summary": summary or {},
        "error": error,
    }
    with EVIDENCE_FILE.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(event) + "\n")
    return event


def observed_tool(target: str, tool: Callable[[], dict[str, Any]]) -> dict[str, Any]:
    started = time.perf_counter()
    try:
        result = tool()
        duration = int((time.perf_counter() - started) * 1000)
        event = record_event(tool="demo_status", target=target, arguments={}, status="success",
                             duration_ms=duration, summary=result)
        return {"result": result, "evidence": event}
    except Exception as exc:
        duration = int((time.perf_counter() - started) * 1000)
        record_event(tool="demo_status", target=target, arguments={}, status="failure",
                     duration_ms=duration, error=str(exc))
        raise


def main() -> None:
    payload = observed_tool("lab-r1", lambda: {"reachable": True, "role": "edge"})
    print(json.dumps(payload, indent=2))
    print(f"Evidence appended to {EVIDENCE_FILE}")


if __name__ == "__main__":
    main()
