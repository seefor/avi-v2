"""AVI v2 Episode 04: validate structured network observations."""

from __future__ import annotations

from typing import Literal
from pydantic import BaseModel, Field, ValidationError, model_validator


class BGPNeighbor(BaseModel):
    ip: str
    state: Literal["Established", "Idle", "Active", "Connect", "unknown"]
    prefixes: int = Field(ge=0)


class BGPSummary(BaseModel):
    schema_version: str = "1.0"
    device: str
    total_peers: int = Field(ge=0)
    established_peers: int = Field(ge=0)
    neighbors: list[BGPNeighbor]
    evidence_id: str

    @model_validator(mode="after")
    def established_not_greater_than_total(self):
        if self.established_peers > self.total_peers:
            raise ValueError("established_peers cannot exceed total_peers")
        return self


def main() -> None:
    valid = {
        "device": "lab-r1",
        "total_peers": 2,
        "established_peers": 1,
        "neighbors": [
            {"ip": "10.0.0.2", "state": "Established", "prefixes": 42},
            {"ip": "10.0.0.3", "state": "Idle", "prefixes": 0},
        ],
        "evidence_id": "evt-demo-002",
    }
    print(BGPSummary.model_validate(valid).model_dump_json(indent=2))

    invalid = {**valid, "established_peers": 3}
    try:
        BGPSummary.model_validate(invalid)
    except ValidationError as exc:
        print("\nControlled validation failure:\n", exc)


if __name__ == "__main__":
    main()
