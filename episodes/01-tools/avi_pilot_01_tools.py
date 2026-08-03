"""AVI v2 Episode 01: one approved read-only pyATS tool."""

from __future__ import annotations

from pathlib import Path

from pyats.topology import loader

TESTBED_FILE = "testbed.yaml"
DEFAULT_DEVICE = "Cat9k_AO_Sandbox"
DEFAULT_COMMAND = "show ip interface brief"
ALLOWED_COMMANDS = {"show ip interface brief", "show version"}


def validate_command(command: str) -> None:
    if command not in ALLOWED_COMMANDS:
        raise ValueError(f"Command is not approved for Episode 01: {command}")


def run_show_command(device_name: str, command: str) -> dict:
    validate_command(command)
    path = Path(TESTBED_FILE)
    if not path.exists():
        raise FileNotFoundError(
            "Copy testbed.example.yaml to testbed.yaml and add your local lab credentials."
        )

    testbed = loader.load(str(path))
    if device_name not in testbed.devices:
        raise ValueError(f"Unknown device: {device_name}")

    device = testbed.devices[device_name]
    try:
        device.connect(
            via="cli",
            log_stdout=False,
            learn_hostname=True,
            init_exec_commands=[],
            init_config_commands=[],
            connection_timeout=15,
        )
        output = device.execute(command)
        return {
            "device": device_name,
            "command": command,
            "status": "success",
            "output": output,
        }
    finally:
        if getattr(device, "connected", False):
            device.disconnect()


def main() -> None:
    print("AVI v2 — Episode 01: Tools")
    result = run_show_command(DEFAULT_DEVICE, DEFAULT_COMMAND)
    print(result["output"])


if __name__ == "__main__":
    main()
