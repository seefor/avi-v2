# Episode 01 Walkthrough — Tools: First Safe Observation

Use this as the camera-ready spine for the episode. Keep the delivery conversational and show the terminal whenever possible.

## 1. Opening Hook

What to say:

"If we're going to build an AI network engineer, the first thing it needs is not more autonomy. It needs one boring tool that works. Today AVI gets one job: safely observe a real lab device with pyATS and prove that application code—not the model—controls what it is allowed to do."

Teaching point:
- Reliable tools come before agent autonomy.
- The first trust question is whether the model can request data without getting unrestricted device access.

## 2. Flight Rules

What to say:

"AVI is read-only. It does not get credentials. It cannot enter configuration mode. It cannot run arbitrary commands. Python validates the target and command before pyATS ever touches the device."

Rules:
1. Approved lab target only.
2. Approved read-only commands only.
3. Credentials stay in the local testbed.
4. No direct shell or SSH access for the model.
5. A blocked request must fail before execution.

## 3. Architecture

```text
User -> AVI -> tool request -> application validation -> pyATS -> lab device
                                      |
                                      +-> blocked if unsafe
```

What to say:

"The important part of this diagram is the validation boundary. The model can ask. The application decides."

## 4. Project Setup

From the repository root:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cd episodes/01-tools
cp testbed.example.yaml testbed.yaml
```

Edit `testbed.yaml` with the lab SSH details. Do not commit it.

## 5. Explain the pyATS Testbed

Show:
- device name
- `os: iosxe`
- credentials
- `connections.cli`

What to say:

"The testbed is AVI's network map. It keeps inventory and credentials outside the Python behavior so the code can stay focused on the tool contract."

## 6. Build the Tool Boundary

Open `avi_pilot_01_tools.py` and explain the functions responsible for:
- loading the testbed,
- validating the device,
- checking the command allowlist,
- connecting with pyATS,
- returning the result,
- disconnecting cleanly.

Emphasize that the safety rule is enforced in code, not only in the prompt.

## 7. Happy-Path Demo

Run:

```bash
python avi_pilot_01_tools.py
```

Use `show ip interface brief` as the approved observation.

What to say:

"AVI is not deciding anything yet. It is collecting one fact through one approved path."

## 8. Break It on Purpose

Change the request to a non-allowlisted or configuration-style command.

What to say:

"This is the demo I care about. A trustworthy system should not only show what it can do. It should show what it refuses to do."

Confirm the request is rejected before the device is touched.

## 9. Review the Result

Show the returned structure and point out:
- target,
- requested operation,
- success or failure,
- result/error.

Explain that Episode 1 proves the tool boundary, but does not yet give AVI a persistent black-box recorder.

## 10. What AVI Still Cannot Do

AVI cannot:
- persist evidence reliably,
- normalize network state,
- observe a fleet,
- decide whether an observation supports a hypothesis,
- make a change.

## 11. Homework

Ask viewers to:
1. Point the testbed at their own lab device.
2. Add one additional safe `show` command to the allowlist.
3. Attempt an unsafe command and confirm it is blocked.
4. Do not add configuration mode.

## 12. Next Flight

What to say:

"AVI can touch the network safely, but right now the observation disappears when the terminal scrolls away. In Episode 2 we build the Black Box Recorder so every tool event leaves evidence we can inspect later."