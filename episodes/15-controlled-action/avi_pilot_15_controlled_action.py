"""AVI v2 Episode 15: controlled-action simulator with prechecks, postchecks, and rollback.

This starter intentionally uses an in-memory lab device. Replace the backend only after
reviewing the Episode 15 safety boundary. It must never default to production execution.
"""

from __future__ import annotations

import json
from copy import deepcopy

LAB_STATE = {
    "lab-r1": {
        "GigabitEthernet1": {"description": "ORIGINAL-LAB-DESCRIPTION"}
    }
}


def preflight(plan: dict, approval: dict) -> None:
    if plan["target"] != approval["target"]:
        raise PermissionError("Plan and approval target do not match")
    if approval.get("decision") != "approved":
        raise PermissionError("Action is not approved")
    if not plan.get("rollback_description"):
        raise ValueError("Rollback is required before execution")


def execute(plan: dict, approval: dict, *, force_postcheck_failure: bool = False) -> dict:
    preflight(plan, approval)
    device, interface = plan["target"].split(":", 1)
    before = deepcopy(LAB_STATE[device][interface])

    LAB_STATE[device][interface]["description"] = plan["new_description"]
    observed = LAB_STATE[device][interface]["description"]
    postcheck_ok = observed == plan["new_description"] and not force_postcheck_failure

    if not postcheck_ok:
        LAB_STATE[device][interface]["description"] = plan["rollback_description"]
        return {
            "status": "rolled_back",
            "before": before,
            "attempted": plan["new_description"],
            "after": deepcopy(LAB_STATE[device][interface]),
            "reason": "postcheck_failed",
        }

    return {
        "status": "success",
        "before": before,
        "after": deepcopy(LAB_STATE[device][interface]),
    }


def main() -> None:
    plan = {
        "target": "lab-r1:GigabitEthernet1",
        "new_description": "AVI-LAB-TEST",
        "rollback_description": "ORIGINAL-LAB-DESCRIPTION",
    }
    approval = {"target": plan["target"], "decision": "approved"}

    print("Successful controlled path:")
    print(json.dumps(execute(plan, approval), indent=2))

    # Reset the lab state so the rollback scenario begins from the same known baseline.
    LAB_STATE["lab-r1"]["GigabitEthernet1"]["description"] = "ORIGINAL-LAB-DESCRIPTION"
    print("\nFailed postcheck path:")
    print(json.dumps(execute(plan, approval, force_postcheck_failure=True), indent=2))


if __name__ == "__main__":
    main()
