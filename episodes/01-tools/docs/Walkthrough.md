# Episode 01 Walkthrough — Can AI Safely Observe a Real Network?

This is the production-ready recording guide for AVI v2 Episode 1. Use it as the spine of the video. The goal is not to read it word-for-word; the goal is to remove guesswork about what to show, what to explain, and when to move between camera, slides, code, and terminal.

## YouTube Package

### Recommended title

**Can AI Safely Observe a Real Network? | Building AVI Ep. 1**

### Alternate titles

- **I Gave an AI Agent Access to a Cisco Switch — Safely | AVI Ep. 1**
- **Build Your First Safe AI Network Tool with pyATS | AVI Ep. 1**
- **Before AI Can Configure the Network, It Must Learn to Observe | AVI Ep. 1**

### Thumbnail direction

Keep the thumbnail simple. Do not show code.

Suggested visual:

```text
AI / AVI icon  ->  SAFETY GATE  ->  Cisco switch
                         |
                       BLOCKED
```

Suggested thumbnail text:

**CAN AI TOUCH THE NETWORK?**

Alternate:

**READ-ONLY FIRST**

### Core promise

By the end of the episode, the viewer will have a working pyATS-backed network tool that can run one approved read-only command against a Cat9k lab device while rejecting unsafe commands in application code.

### Target runtime

**25–35 minutes**

Do not stretch the episode to hit a target. If the lesson is complete in 27 minutes, stop.

---

# Recording Run of Show

## 0:00–0:45 — Cold Open / Hook

### Screen

Start on camera for the first sentence, then cut to a terminal showing the successful `show ip interface brief` result for two or three seconds. Do not explain the code yet.

### What to say

> "If we're going to build an AI network engineer, the first thing it needs is not a giant brain. It needs one boring tool that works. Today AVI gets one job: safely observe a real Cisco lab device with pyATS. And just as important, we're going to prove what happens when AVI asks for something it is not allowed to do."

Then:

> "This entire series is built around one idea: AVI has to earn the right to automate the network. Episode 1 starts with observation, not autonomy."

### Teaching point

- Reliable tools come before agent autonomy.
- A successful demo is only half the lesson; refusal behavior matters too.

### Editing note

Put a quick on-screen label over the successful terminal output:

```text
EPISODE 1
OBSERVE — DO NOT CHANGE
```

---

## 0:45–2:30 — Slide: The Trust Question

### Slide title

**Can AI Safely Observe a Real Network?**

### Slide content

```text
MODEL CAN REQUEST
       ↓
APPLICATION DECIDES
       ↓
TOOL EXECUTES
```

Bottom callout:

**The model never receives unrestricted SSH access.**

### What to say

> "The trust question for Episode 1 is simple: can the model request network data without receiving unrestricted SSH or shell access?"

> "That distinction matters. The model can ask for information. Python decides whether the device exists, whether the command is approved, and whether the request is allowed to reach pyATS."

> "I do not want safety to depend on asking the model nicely. I want the application to enforce the boundary."

### Teaching point

Prompts can describe policy. Code must enforce operational controls.

---

## 2:30–4:00 — Slide: AVI Flight Rules

### Slide title

**AVI Flight Rules — Episode 1**

### Show these five rules

1. Approved lab target only.
2. Approved read-only commands only.
3. Credentials stay outside the model.
4. No configuration mode or arbitrary shell.
5. Unsafe requests fail before execution.

### What to say

> "These aren't limitations I'm trying to work around. These are the first controls that make the system understandable."

> "AVI is read-only. It does not get the SSH password in a prompt. It cannot enter configuration mode. It cannot decide to invent another command. And if a request is outside the allowlist, we stop before touching the device."

### On-screen callout

**Trust = capability + boundaries + evidence**

Mention that Episode 2 adds stronger persistent evidence.

---

## 4:00–5:30 — Slide: Architecture

### Slide title

**AVI's First Flight**

### Architecture

```text
User
  ↓
AVI
  ↓
Tool Request
  ↓
Application Validation ───────→ BLOCKED
  ↓ approved
pyATS / Unicon
  ↓ SSH
Cat9k_AO_Sandbox
  ↓
show ip interface brief
  ↓
Result
```

### What to say

> "The most important box in this diagram is not the AI model. It's application validation. The model can request. The application decides."

> "pyATS gives us the network automation foundation. Unicon handles the device connection behavior underneath it. AVI never needs the raw SSH session itself."

### Transition

> "Let's build the smallest version of this that actually works."

---

# Build and Demo

## 5:30–7:00 — Repository Orientation

### Screen

Open the repository at:

```text
episodes/01-tools/
```

Show only the files viewers need for this episode:

```text
episodes/01-tools/
├── README.md
├── avi_pilot_01_tools.py
├── requirements.txt
├── testbed.example.yaml
└── docs/
```

### What to say

> "I'm intentionally keeping Episode 1 small. There is one Python starter, one pyATS testbed example, and the supporting documentation. We're not hiding a giant framework behind the demo."

### Teaching point

The viewer should be able to understand the entire network-access path in one sitting.

---

## 7:00–9:30 — Environment Setup

### Terminal

From the repository root:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
cd episodes/01-tools
cp testbed.example.yaml testbed.yaml
```

Windows PowerShell:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
cd episodes\01-tools
Copy-Item testbed.example.yaml testbed.yaml
```

### What to say

> "I keep the environment isolated because reproducibility matters when you're teaching, recording, or debugging someone else's lab."

> "The real `testbed.yaml` stays local. The example belongs in Git. Credentials do not."

### Optional terminal check

```bash
pyats validate testbed testbed.yaml
```

If available in the installed pyATS version, show the validation result briefly.

---

## 9:30–12:00 — Open `testbed.example.yaml`

### Screen

Open:

```text
episodes/01-tools/testbed.example.yaml
```

Highlight these exact fields:

```yaml
testbed:
  name: avi-v2-lab

devices:
  Cat9k_AO_Sandbox:
    os: iosxe
    type: router
    credentials:
      default:
        username: YOUR_USERNAME
        password: YOUR_PASSWORD
    connections:
      cli:
        protocol: ssh
        ip: 10.10.20.66
        port: 22
```

### What to say

> "Think of the pyATS testbed as AVI's network map. It describes what device exists and how pyATS reaches it."

Explain:

- `Cat9k_AO_Sandbox` is the device name the Python code requests.
- `os: iosxe` tells pyATS/Unicon which platform behavior to use.
- `credentials.default` is local connection data and should never be committed with real values.
- `connections.cli` defines SSH connectivity.

### Important clarification

> "The important separation here is that the model doesn't need these credentials. The tool does. Those are two very different things."

---

## 12:00–14:00 — Open the Python Starter: Constants and Allowlist

### Screen

Open:

```text
episodes/01-tools/avi_pilot_01_tools.py
```

Start at:

```python
TESTBED_FILE = "testbed.yaml"
DEFAULT_DEVICE = "Cat9k_AO_Sandbox"
DEFAULT_COMMAND = "show ip interface brief"
ALLOWED_COMMANDS = {"show ip interface brief", "show version"}
```

### What to say

> "This is the first real safety boundary. We are not allowing arbitrary CLI. Episode 1 has two approved commands, and our default mission uses only `show ip interface brief`."

> "An allowlist is deliberately boring. That's why I like it. The behavior is explicit, testable, and easy to review."

### Teaching point

Do not use a weak check such as `command.startswith("show")` for a safety-sensitive boundary. Exact approved operations are easier to reason about.

---

## 14:00–16:00 — Function 1: `validate_command()`

### Screen

Highlight:

```python
def validate_command(command: str) -> None:
    if command not in ALLOWED_COMMANDS:
        raise ValueError(f"Command is not approved for Episode 01: {command}")
```

### What to say

> "This little function is more important than it looks. Before we load a testbed or connect to anything, we validate the requested command."

> "If AVI asks for something outside this set, Python raises an error. The refusal is deterministic. It isn't up to the language model to decide whether it should behave."

### On-screen callout

**POLICY BEFORE CONNECTION**

---

## 16:00–20:00 — Function 2: `run_show_command()`

### Screen

Walk through the function in five chunks. Do not read every line.

### Chunk A — Validate first

```python
validate_command(command)
```

What to say:

> "First, policy. No network access yet."

### Chunk B — Require local testbed

```python
path = Path(TESTBED_FILE)
if not path.exists():
    raise FileNotFoundError(...)
```

What to say:

> "If the local testbed doesn't exist, fail clearly rather than guessing where credentials or inventory might come from."

### Chunk C — Validate device target

```python
testbed = loader.load(str(path))
if device_name not in testbed.devices:
    raise ValueError(f"Unknown device: {device_name}")
```

What to say:

> "The command isn't the only boundary. AVI also doesn't get to invent device targets. The requested device must exist in the approved testbed."

### Chunk D — Connect and execute

```python
device.connect(
    via="cli",
    log_stdout=False,
    learn_hostname=True,
    init_exec_commands=[],
    init_config_commands=[],
    connection_timeout=15,
)
output = device.execute(command)
```

What to say:

> "pyATS loads the device model, and Unicon handles the CLI connection behavior. `connection_timeout=15` keeps a bad connection from hanging forever."

Point out:

```python
init_config_commands=[]
```

Then say:

> "Notice that we're not doing initialization work in configuration mode. Episode 1 is observation only."

### Chunk E — Structured result and cleanup

```python
return {
    "device": device_name,
    "command": command,
    "status": "success",
    "output": output,
}
```

and:

```python
finally:
    if getattr(device, "connected", False):
        device.disconnect()
```

### What to say

> "The tool returns a small structured result instead of leaking connection objects up into the rest of the application. And whether execution succeeds or fails, the `finally` block gives us a clean disconnect path."

### Teaching point

Network access should live behind a small, reviewable tool contract.

---

## 20:00–21:00 — Function 3: `main()`

### Screen

Highlight:

```python
def main() -> None:
    print("AVI v2 — Episode 01: Tools")
    result = run_show_command(DEFAULT_DEVICE, DEFAULT_COMMAND)
    print(result["output"])
```

### What to say

> "This is intentionally not a chatbot yet. There isn't even an LLM required for the first flight. We're proving the tool path before we add reasoning on top of it."

### Key teaching line

> "An LLM can understand networking concepts, but it does not know the current state of your router unless a tool collects that state."

---

## 21:00–24:00 — Happy-Path Demo

### Terminal

Make sure you are in:

```text
episodes/01-tools
```

Run:

```bash
python avi_pilot_01_tools.py
```

### What viewers should see

The actual device output from:

```text
show ip interface brief
```

### What to say before pressing Enter

> "At this point, there is one approved device and one approved default operation. Let's see whether that boring path actually works."

### What to say after the result

> "AVI didn't make a network decision here. It collected an observation through a controlled tool. That's enough for Episode 1."

Point out that the terminal output is raw network evidence, not yet normalized state. Episode 3 handles that distinction explicitly.

---

## 24:00–27:00 — Break It on Purpose

This is a required part of the episode, not an optional blooper.

### Preferred failure demo

Temporarily change:

```python
DEFAULT_COMMAND = "configure terminal"
```

Do not add it to `ALLOWED_COMMANDS`.

Run:

```bash
python avi_pilot_01_tools.py
```

### Expected behavior

Python should raise:

```text
ValueError: Command is not approved for Episode 01: configure terminal
```

### What to say

> "This is actually the demo I care about more. A trustworthy system should show what it refuses to do, not just what it can do."

> "Notice where the failure happens. `validate_command()` runs before we load the testbed and before we create the device connection. The unsafe request never reaches the Cat9k."

### Restore the starter

Change:

```python
DEFAULT_COMMAND = "show ip interface brief"
```

before continuing or committing any code.

### Optional second blocked demo

Use an unknown target by temporarily changing:

```python
DEFAULT_DEVICE = "not-a-real-device"
```

This demonstrates that target validation is separate from command validation.

Do this only if runtime allows; the command rejection is the primary failure demo.

---

## 27:00–29:00 — Evidence Review

### Slide / terminal split

Show the result shape from the tool:

```python
{
    "device": device_name,
    "command": command,
    "status": "success",
    "output": output,
}
```

### What to say

> "Episode 1 gives us enough information to understand the tool result, but it does not yet give us the black-box recorder I want for a real agent workflow."

> "If AVI later says an interface was down, I want to know exactly which tool ran, against which target, when it ran, how long it took, whether it failed, and which evidence record supports the claim."

### Transition

> "That's the job of Episode 2."

---

## 29:00–30:30 — What AVI Still Cannot Do

### Slide title

**What AVI Has NOT Earned Yet**

### Show

AVI still cannot:

- persist evidence with evidence IDs and run IDs,
- normalize raw output into network state,
- observe multiple devices safely,
- choose the right context,
- compare observed state with intended state,
- retrieve runbooks,
- investigate in a loop,
- verify a hypothesis,
- make any network change.

### What to say

> "I want this slide in every episode. AVI gets one new capability at a time, and we're going to be explicit about what it still cannot do."

> "The point isn't to make AVI powerful as fast as possible. The point is to make each new capability understandable enough that we can trust the next one."

---

## 30:30–32:00 — Homework

### Slide title

**Your Flight Assignment**

Ask viewers to:

1. Point `testbed.yaml` at their own IOS-XE lab device.
2. Run the default `show ip interface brief` operation.
3. Add one additional explicitly approved read-only command.
4. Attempt one unsafe command and confirm it is rejected before connection.
5. Do **not** add configuration mode yet.

### What to say

> "That last one is intentional. Don't race ahead and give AVI write access. The next few episodes are about earning trust before we earn power."

---

## 32:00–33:00 — Episode 2 Tease

### Slide

Show the architecture growing.

Episode 1:

```text
Request -> Validation -> pyATS -> Device -> Result
```

Episode 2:

```text
Request -> Validation -> pyATS -> Device -> Result
                  \____________________________/
                                ↓
                         Evidence Recorder
                                ↓
                              JSONL
```

### What to say

> "AVI can now touch the network through one safe path, but right now the observation disappears when the terminal scrolls away. In Episode 2 we're building the Black Box Recorder. Every tool invocation—successful, blocked, or failed—will leave evidence behind."

End there. Do not add a long outro.

---

# Recording Checklist

Before recording, verify all of these:

- [ ] Real `testbed.yaml` exists locally and is ignored by Git.
- [ ] Cat9k sandbox is reachable.
- [ ] Manual SSH works if the lab requires troubleshooting.
- [ ] `pyats validate testbed testbed.yaml` passes, if available.
- [ ] `python avi_pilot_01_tools.py` succeeds once before recording.
- [ ] `DEFAULT_COMMAND` is restored to `show ip interface brief`.
- [ ] `ALLOWED_COMMANDS` contains only the intended Episode 1 commands.
- [ ] Terminal font is large enough for YouTube.
- [ ] Credentials are not visible in the editor, terminal history, or screen recording.
- [ ] Browser tabs and notifications are cleaned up.
- [ ] The blocked-command demo has been rehearsed.

---

# Suggested Chapter Markers

Adjust these after editing to match the final timestamps.

```text
00:00 Why AVI starts read-only
00:45 The Episode 1 trust question
02:30 AVI flight rules
04:00 Architecture
05:30 Repository walkthrough
07:00 Environment setup
09:30 pyATS testbed explained
12:00 The command allowlist
14:00 Enforcing policy in Python
16:00 Building the pyATS tool
21:00 First live network observation
24:00 Blocking an unsafe command
27:00 What counts as evidence
29:00 What AVI still cannot do
30:30 Homework
32:00 Episode 2: The Black Box Recorder
```

---

# Production Notes

## What to keep on camera

Use camera primarily for:

- the opening hook,
- the trust/safety framing,
- the wrap-up.

Move quickly to slides, editor, and terminal for the technical teaching.

## What not to over-explain

Do not turn Episode 1 into a complete pyATS course. Explain only enough pyATS and Unicon to understand AVI's tool path. The series is about engineering the assistant, not teaching every feature of the automation library.

## The sentence to repeat throughout the series

> **"The model can request. The application decides."**

That line captures the Episode 1 trust boundary and can become recurring language as AVI gains more capability.

## Series north star

> **AVI has to earn the right to automate the network.**
