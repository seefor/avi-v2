"""AVI v2 Episode 10: bounded investigation loop with duplicate-call detection."""

from __future__ import annotations

import json
import time


class LoopController:
    def __init__(self, max_iterations: int = 5, max_runtime_seconds: int = 10):
        self.max_iterations = max_iterations
        self.max_runtime_seconds = max_runtime_seconds
        self.calls: list[tuple[str, tuple]] = []

    def run(self) -> dict:
        started = time.monotonic()
        history = []

        for iteration in range(1, self.max_iterations + 1):
            if time.monotonic() - started > self.max_runtime_seconds:
                return {"status": "stopped", "reason": "runtime_limit", "history": history}

            # Deterministic teaching sequence: first BGP, then reachability.
            call = ("bgp_status", ("lab-r1",)) if iteration == 1 else ("reachability", ("10.0.0.2",))

            if call in self.calls:
                return {"status": "escalated", "reason": "duplicate_call_no_progress", "history": history}

            self.calls.append(call)
            result = self.execute(*call)
            history.append({"iteration": iteration, "tool": call[0], "result": result})

            if result.get("enough_evidence"):
                return {"status": "complete", "reason": "enough_evidence", "history": history}

        return {"status": "escalated", "reason": "iteration_limit", "history": history}

    @staticmethod
    def execute(tool: str, args: tuple) -> dict:
        if tool == "bgp_status":
            return {"state": "Idle", "enough_evidence": False}
        if tool == "reachability":
            return {"reachable": False, "enough_evidence": True}
        return {"enough_evidence": False}


def main() -> None:
    print(json.dumps(LoopController().run(), indent=2))


if __name__ == "__main__":
    main()
