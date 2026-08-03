# Episode 01 — Tools

## Can an AI safely observe a real network?

AVI begins with one narrow capability: observe a real lab device through an approved pyATS-backed tool.

## What AVI Gains

- connection to one approved lab device
- one read-only command path
- a narrow Python tool boundary
- timeout and connection-failure handling
- command allowlisting

## Trust Question

Can the model request network data without receiving unrestricted SSH or shell access?

## Architecture

```text
User -> AVI -> tool request -> application validation -> pyATS -> lab device
                                      |
                                      +-> blocked if unsafe
```

The model can request information. Python decides whether the tool exists, whether the target is allowed, and whether the command is read-only.

## Build Goals

Create a small pyATS tool wrapper that:

1. loads local testbed configuration,
2. validates the target device,
3. permits only approved `show` operations,
4. connects with a timeout,
5. returns a structured result,
6. never exposes credentials to the model.

## Demo

Happy path: run `show ip interface brief` against the lab device and return the result.

Blocked path: attempt a configuration or non-allowlisted command and show that application code rejects it before the device is touched.

## Safety Boundary

- read-only only
- one approved device or sandbox inventory
- no configuration mode
- no arbitrary shell
- credentials remain outside prompts and source control

## Evidence to Review

At this stage, basic console output is enough to prove the tool boundary. Episode 2 turns that into a persistent evidence record.

## AVI Still Cannot

- remember evidence reliably
- normalize network state
- observe multiple devices
- decide whether a result supports a hypothesis
- make changes

## Next

Episode 2 adds the Black Box Recorder: every tool invocation must leave evidence.
