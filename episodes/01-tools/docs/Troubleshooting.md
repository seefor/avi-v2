# Episode 01 Troubleshooting — Tools

Start with basic connectivity before debugging AVI.

## Testbed Validation

Run:

```bash
pyats validate testbed testbed.yaml
```

If YAML validation fails, compare indentation and field names with `testbed.example.yaml`.

## Device Is Unreachable

Test network reachability and SSH manually:

```bash
ping <device-ip>
ssh <username>@<device-ip>
```

If manual SSH fails, fix network access before debugging pyATS.

## Authentication or Enable Failure

Check the local `credentials.default` and `credentials.enable` values. Do not copy real credentials into Git or screenshots.

## Wrong OS

Cisco IOS-XE devices should normally use:

```yaml
os: iosxe
```

A wrong OS can cause Unicon to use incorrect prompt and connection behavior.

## Prompt or Hostname Learning Problems

If login succeeds but pyATS cannot settle on the prompt:
- SSH manually and inspect the prompt.
- Check banners and unusual login messages.
- Confirm the device lands in the expected CLI mode.

## Approved Command Is Blocked

Check the command allowlist in the Episode 1 code. The command must match the application policy exactly.

## Unsafe Command Is Not Blocked

Stop the demo and review validation logic. The safety objective for this episode is rejection before device execution.

## Basic Recovery Order

```text
1. Validate YAML
2. Test IP reachability
3. Test manual SSH
4. Confirm OS and credentials
5. Run the AVI starter
6. Inspect the returned error
```

Do not weaken the allowlist just to make a demo pass.