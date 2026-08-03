"""AVI v2 Episode 09: a small application harness around model/tool decisions."""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from typing import Callable


@dataclass
class Harness:
    allowed_tools: dict[str, Callable]
    run_log: list[dict] = field(default_factory=list)

    def execute_tool(self, name: str, **kwargs) -> dict:
        if name not in self.allowed_tools:
            event = {"tool": name, "status": "blocked", "arguments": kwargs}
            self.run_log.append(event)
            raise PermissionError(f"Tool is not registered or allowed: {name}")

        result = self.allowed_tools[name](**kwargs)
        event = {"tool": name, "status": "success", "arguments": kwargs, "result": result}
        self.run_log.append(event)
        return result

    def run(self, request: str) -> dict:
        # Episode 09 keeps the model decision deterministic so the harness boundary is visible.
        if "bgp" in request.lower():
            result = self.execute_tool("bgp_status", device="lab-r1")
        else:
            result = self.execute_tool("device_status", device="lab-r1")
        return {"request": request, "result": result, "run_log": self.run_log}


def main() -> None:
    tools = {
        "device_status": lambda device: {"device": device, "status": "up"},
        "bgp_status": lambda device: {"device": device, "peer": "10.0.0.2", "state": "Idle"},
    }
    harness = Harness(allowed_tools=tools)
    print(json.dumps(harness.run("Check BGP on lab-r1"), indent=2))

    try:
        harness.execute_tool("configure_device", device="lab-r1")
    except PermissionError as exc:
        print(f"\nBlocked by harness policy: {exc}")


if __name__ == "__main__":
    main()
