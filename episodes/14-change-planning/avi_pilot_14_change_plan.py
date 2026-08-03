"""AVI v2 Episode 14: build and validate a reviewable change plan."""

from __future__ import annotations

import json
from pydantic import BaseModel, Field, model_validator


class ChangePlan(BaseModel):
    objective: str
    target: str
    evidence_refs: list[str] = Field(min_length=1)
    approval_ref: str
    proposed_commands: list[str] = Field(min_length=1)
    expected_diff: str
    prechecks: list[str] = Field(min_length=1)
    postchecks: list[str] = Field(min_length=1)
    rollback_commands: list[str] = Field(min_length=1)
    risks: list[str]
    execution_allowed: bool = False

    @model_validator(mode="after")
    def plan_stays_non_executable(self):
        if self.execution_allowed:
            raise ValueError("Episode 14 plans must remain non-executable")
        return self


def main() -> None:
    plan = ChangePlan(
        objective="Update a test-only interface description",
        target="lab-r1:GigabitEthernet1",
        evidence_refs=["evt-501", "evt-502"],
        approval_ref="approval-demo-001",
        proposed_commands=["interface GigabitEthernet1", "description AVI-LAB-TEST"],
        expected_diff="Interface description changes to AVI-LAB-TEST",
        prechecks=["Capture current interface description", "Confirm target is lab-r1"],
        postchecks=["Read interface description and compare expected value"],
        rollback_commands=["interface GigabitEthernet1", "description ORIGINAL-LAB-DESCRIPTION"],
        risks=["Incorrect target selection"],
    )
    print(plan.model_dump_json(indent=2))


if __name__ == "__main__":
    main()
