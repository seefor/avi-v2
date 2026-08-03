"""AVI v2 Episode 03: normalize observations into explicit network state."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pydantic import BaseModel


class InterfaceState(BaseModel):
    device: str
    interface: str
    admin_status: str
    operational_status: str
    ip_address: str | None = None
    source: str
    evidence_id: str
    observed_at: str


def normalize_interface(raw: dict) -> InterfaceState:
    return InterfaceState(
        device=raw["device"],
        interface=raw["interface"],
        admin_status=raw.get("admin_status", "unknown"),
        operational_status=raw.get("oper_status", "unknown"),
        ip_address=raw.get("ip_address"),
        source=raw.get("source", "pyats"),
        evidence_id=raw["evidence_id"],
        observed_at=raw.get("observed_at", datetime.now(timezone.utc).isoformat()),
    )


def main() -> None:
    raw = {
        "device": "lab-r1",
        "interface": "GigabitEthernet1",
        "admin_status": "up",
        "oper_status": "down",
        "ip_address": "10.0.0.1",
        "source": "pyats",
        "evidence_id": "evt-demo-001",
    }
    state = normalize_interface(raw)
    print(state.model_dump_json(indent=2))


if __name__ == "__main__":
    main()
