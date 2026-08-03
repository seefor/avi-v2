"""AVI v2 Episode 05: preserve per-device results while creating a fleet rollup."""

from __future__ import annotations

import json
from concurrent.futures import ThreadPoolExecutor, as_completed

DEVICES = {
    "lab-r1": {"status": "healthy", "evidence_id": "evt-101"},
    "lab-r2": {"status": "degraded", "evidence_id": "evt-102"},
    "lab-r3": {"status": "unreachable", "evidence_id": "evt-103"},
}


def observe(device: str) -> dict:
    result = DEVICES[device]
    if result["status"] == "unreachable":
        return {"device": device, **result, "error": "connection timeout"}
    return {"device": device, **result, "error": None}


def run_batch(devices: list[str], max_workers: int = 3) -> dict:
    per_device: list[dict] = []
    with ThreadPoolExecutor(max_workers=max_workers) as pool:
        futures = {pool.submit(observe, device): device for device in devices}
        for future in as_completed(futures):
            per_device.append(future.result())

    counts = {"healthy": 0, "degraded": 0, "unreachable": 0}
    for result in per_device:
        counts[result["status"]] += 1

    return {"requested": len(devices), "counts": counts, "devices": sorted(per_device, key=lambda x: x["device"])}


def main() -> None:
    print(json.dumps(run_batch(list(DEVICES)), indent=2))


if __name__ == "__main__":
    main()
