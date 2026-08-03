"""AVI v2 Episode 07: compare intended state with observed state."""

from __future__ import annotations

import json


def compare_intent(intent: dict | None, observed: dict | None) -> dict:
    if intent is None:
        return {"status": "unmanaged", "intent": None, "observed": observed}
    if observed is None:
        return {"status": "unknown", "intent": intent, "observed": None}

    expected = intent.get("value")
    actual = observed.get("value")
    return {
        "field": intent.get("field"),
        "intent_source": intent.get("source", "netbox"),
        "intent_record_id": intent.get("record_id"),
        "observed_source": observed.get("source", "pyats"),
        "evidence_id": observed.get("evidence_id"),
        "expected": expected,
        "observed": actual,
        "status": "match" if expected == actual else "drift",
    }


def main() -> None:
    intended = {"field": "interface_enabled", "value": True, "source": "netbox", "record_id": 417}
    observed = {"field": "interface_enabled", "value": False, "source": "pyats", "evidence_id": "evt-201"}
    print(json.dumps(compare_intent(intended, observed), indent=2))
    print(json.dumps(compare_intent(None, observed), indent=2))


if __name__ == "__main__":
    main()
