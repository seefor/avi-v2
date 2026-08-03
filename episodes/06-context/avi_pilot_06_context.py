"""AVI v2 Episode 06: select relevant context instead of dumping everything."""

from __future__ import annotations

import json
from datetime import datetime, timedelta, timezone


def assemble_context(question: str, observations: list[dict], device: str, max_age_minutes: int = 15) -> dict:
    now = datetime.now(timezone.utc)
    included, excluded = [], []

    for item in observations:
        observed_at = datetime.fromisoformat(item["observed_at"])
        age = now - observed_at
        reason = None

        if item.get("device") != device:
            reason = "unrelated device"
        elif age > timedelta(minutes=max_age_minutes):
            reason = "stale observation"
        elif item.get("sensitive"):
            reason = "sensitive context"

        if reason:
            excluded.append({"item": item["id"], "reason": reason})
        else:
            included.append(item)

    return {
        "question": question,
        "device": device,
        "included": included,
        "excluded": excluded,
        "policy": {"max_age_minutes": max_age_minutes},
    }


def main() -> None:
    now = datetime.now(timezone.utc)
    observations = [
        {"id": "obs-1", "device": "lab-r1", "kind": "bgp", "value": "Idle", "observed_at": now.isoformat()},
        {"id": "obs-2", "device": "lab-r2", "kind": "interface", "value": "down", "observed_at": now.isoformat()},
        {"id": "obs-3", "device": "lab-r1", "kind": "old-log", "value": "...", "observed_at": (now - timedelta(hours=2)).isoformat()},
    ]
    context = assemble_context("Why is BGP unstable on lab-r1?", observations, "lab-r1")
    print(json.dumps(context, indent=2))


if __name__ == "__main__":
    main()
