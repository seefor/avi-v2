"""AVI v2 Episode 11: verify claims against explicit evidence requirements."""

from __future__ import annotations

import json


def verify_claim(claim: str, required_kinds: set[str], evidence: list[dict]) -> dict:
    available = {item["kind"] for item in evidence}
    missing = sorted(required_kinds - available)
    supporting = [item["evidence_id"] for item in evidence if item["kind"] in required_kinds]

    if missing:
        return {
            "claim": claim,
            "status": "unresolved",
            "confidence": "low",
            "evidence_refs": supporting,
            "limitations": [f"Missing evidence kinds: {', '.join(missing)}"],
        }

    return {
        "claim": claim,
        "status": "supported",
        "confidence": "medium",
        "evidence_refs": supporting,
        "limitations": [],
    }


def main() -> None:
    claim = "BGP instability is related to interface reachability"
    bgp_only = [{"kind": "bgp", "evidence_id": "evt-301", "state": "Idle"}]
    print(json.dumps(verify_claim(claim, {"bgp", "interface"}, bgp_only), indent=2))

    complete = bgp_only + [{"kind": "interface", "evidence_id": "evt-302", "state": "down"}]
    print("\nWith additional evidence:")
    print(json.dumps(verify_claim(claim, {"bgp", "interface"}, complete), indent=2))


if __name__ == "__main__":
    main()
