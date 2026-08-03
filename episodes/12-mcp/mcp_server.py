"""AVI v2 Episode 12: expose narrow read-only network tools through MCP."""

from __future__ import annotations

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("avi-v2-network-tools")

ALLOWED_DEVICES = {"lab-r1", "lab-r2"}


def validate_device(device: str) -> None:
    if device not in ALLOWED_DEVICES:
        raise ValueError(f"Device is not approved: {device}")


@mcp.tool()
def device_status(device: str) -> dict:
    """Return read-only demo device status for an approved AVI lab device."""
    validate_device(device)
    return {"device": device, "status": "up", "source": "avi-demo"}


@mcp.tool()
def bgp_status(device: str) -> dict:
    """Return read-only demo BGP status for an approved AVI lab device."""
    validate_device(device)
    state = "Idle" if device == "lab-r2" else "Established"
    return {
        "device": device,
        "neighbors": [{"ip": "10.0.0.2", "state": state}],
        "source": "avi-demo",
    }


if __name__ == "__main__":
    mcp.run()
