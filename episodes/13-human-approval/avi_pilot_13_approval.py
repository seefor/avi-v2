"""AVI v2 Episode 13: bind human approval to an exact action and target."""

from __future__ import annotations

import json
from datetime import datetime, timedelta, timezone
from uuid import uuid4


def create_request(target: str, action: str, evidence_refs: list[str]) -> dict:
    return {
        "approval_request_id": f"apr-{uuid4()}",
        "target": target,
        "action": action,
        "evidence_refs": evidence_refs,
        "risk": "low",
        "expected_impact": "lab-only metadata change",
        "expires_at": (datetime.now(timezone.utc) + timedelta(minutes=30)).isoformat(),
    }


def approve(request: dict, approver: str) -> dict:
    return {
        "approval_id": f"approval-{uuid4()}",
        "request_id": request["approval_request_id"],
        "target": request["target"],
        "action": request["action"],
        "approver": approver,
        "decision": "approved",
        "expires_at": request["expires_at"],
    }


def validate_approval(approval: dict, *, target: str, action: str) -> None:
    if approval["decision"] != "approved":
        raise PermissionError("Request is not approved")
    if approval["target"] != target or approval["action"] != action:
        raise PermissionError("Approval scope does not match target/action")
    if datetime.fromisoformat(approval["expires_at"]) <= datetime.now(timezone.utc):
        raise PermissionError("Approval has expired")


def main() -> None:
    request = create_request("lab-r1", "set_test_description", ["evt-401"])
    approval = approve(request, "network-engineer")
    validate_approval(approval, target="lab-r1", action="set_test_description")
    print(json.dumps({"request": request, "approval": approval}, indent=2))

    try:
        validate_approval(approval, target="lab-r2", action="set_test_description")
    except PermissionError as exc:
        print(f"\nControlled rejection: {exc}")


if __name__ == "__main__":
    main()
