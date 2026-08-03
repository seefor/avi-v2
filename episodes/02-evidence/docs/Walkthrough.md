# Episode 02 Walkthrough — How Do We Prove What AVI Actually Saw?

This is the production-ready recording guide for AVI v2 Episode 2.

## YouTube Package

### Recommended title

**How Do We Prove What an AI Agent Actually Saw? | Building AVI Ep. 2**

Alternate titles:
- **Build a Black Box Recorder for Your AI Agent | AVI Ep. 2**
- **AI Agent Logs Are Not Enough — Build Evidence | AVI Ep. 2**

Thumbnail text:

**PROVE WHAT IT SAW**

Core promise: turn transient tool activity into durable, referenceable evidence records.

Target runtime: **20–30 minutes**.

---

# Recording Run of Show

## 0:00–0:45 — Cold Open

### What to say

> "AVI touched the network safely in Episode 1. But if AVI later tells me an interface was down, I don't want to trust the sentence. I want to inspect the event behind it. Today we're building AVI's black box recorder."

Quickly show one `avi_evidence.jsonl` record.

## 0:45–2:00 — Trust Question

Slide title: **Can I Inspect the Exact Event Behind a Claim?**

Show:

```text
Tool Call -> Result -> Evidence ID -> Later Claim
```

What to say:

> "Evidence is not just debug output. It gives later layers something stable to point back to."

## 2:00–3:30 — Architecture

```text
Tool Request -> Execution -> Result
                    |
                    v
             Evidence Recorder
                    |
                    v
            avi_evidence.jsonl
```

Explain that Episode 2 records success and failure. Policy-block evidence is the direction of the architecture, while this starter specifically demonstrates successful and exception paths.

## 3:30–5:00 — Repository and Starter

Open:

```text
episodes/02-evidence/avi_pilot_02_evidence.py
```

Run from the repository root:

```bash
python episodes/02-evidence/avi_pilot_02_evidence.py
```

Tell viewers the starter has three important pieces:

- `record_event()`
- `observed_tool()`
- `main()`

## 5:00–9:00 — `record_event()`

Highlight:

```python
EVIDENCE_FILE = Path("avi_evidence.jsonl")
```

Then walk through the event fields:

```text
run_id
evidence_id
timestamp
tool
target
arguments
status
duration_ms
summary
error
```

### What to say

> "`evidence_id` identifies this specific tool event. The current starter also generates a `run_id` here. As AVI matures, a real investigation should create one run ID and pass it across multiple evidence events."

Call that out clearly so the video matches the actual code.

Explain JSON Lines:

> "One event per line is deliberately simple. It's easy to append, inspect, stream, and process later."

## 9:00–13:00 — `observed_tool()`

Walk through:

```python
started = time.perf_counter()
```

Then the success path:

```python
result = tool()
...
record_event(... status="success", summary=result)
```

Then the exception path:

```python
except Exception as exc:
    ...
    record_event(... status="failure", error=str(exc))
    raise
```

### Key line

> "A failed observation is not the same thing as observing a failed network state. AVI has to preserve that distinction."

## 13:00–16:00 — Happy-Path Demo

Run:

```bash
python episodes/02-evidence/avi_pilot_02_evidence.py
```

Then open the evidence file from the repository root:

```bash
cat avi_evidence.jsonl
```

PowerShell:

```powershell
Get-Content avi_evidence.jsonl
```

Point out the generated `evidence_id`, status, duration, summary, and timestamp.

## 16:00–19:00 — Break It on Purpose

Temporarily change the lambda in `main()` from:

```python
lambda: {"reachable": True, "role": "edge"}
```

to a small function/lambda that raises an exception, for example:

```python
lambda: (_ for _ in ()).throw(RuntimeError("simulated connection failure"))
```

Run the starter again.

Show that:

- the script raises the exception,
- a failure evidence record is still appended,
- `error` is populated,
- `duration_ms` is still captured.

Restore the happy-path lambda after the demo.

### What to say

> "This is why the recorder wraps the tool call. Failure still leaves a trail."

## 19:00–21:00 — Evidence Hygiene

Explain that logging everything is not automatically safe.

Show the `arguments` and `summary` fields and say:

> "Before this becomes a production pattern, we need redaction and data-minimization rules. Credentials, tokens, or sensitive payloads should not be blindly copied into evidence."

Do not claim the current starter already performs redaction; identify it as a hardening step.

## 21:00–23:00 — What AVI Still Cannot Do

Slide title: **What AVI Has NOT Earned Yet**

AVI can now create evidence records, but it still cannot:

- turn raw observations into consistent network state,
- enforce richer schemas across those state objects,
- correlate multiple devices,
- verify later claims against evidence.

## 23:00–24:30 — Homework

1. Pass a shared `run_id` into multiple events.
2. Add a `caller` or `environment` field.
3. Run success and failure cases.
4. Add a redaction helper for sensitive argument names.
5. Confirm every event receives a unique `evidence_id`.

## 24:30–25:30 — Next Flight

Show architecture growth:

```text
Episode 2:
Tool -> Evidence Record

Episode 3:
Tool -> Evidence Record -> Normalizer -> Network State
```

### What to say

> "Evidence tells us what happened. In Episode 3, AVI learns to turn those observations into explicit network state without losing the evidence behind them."

---

# Recording Checklist

- [ ] Delete or archive old `avi_evidence.jsonl` before recording if you want a clean demo.
- [ ] Happy path runs successfully.
- [ ] Failure path has been rehearsed.
- [ ] No real secrets are included in test arguments.
- [ ] Terminal font is readable.
- [ ] Failure demo is restored before committing code.

# Suggested Chapters

```text
00:00 Why AVI needs evidence
00:45 The trust question
02:00 Black box architecture
03:30 Episode 2 starter
05:00 Building the evidence record
09:00 Wrapping tool execution
13:00 Successful evidence event
16:00 Recording a failed tool call
19:00 Evidence hygiene and redaction
21:00 What AVI still cannot do
23:00 Homework
24:30 Episode 3 tease
```

## Series takeaway

> **If AVI makes a claim later, we should be able to ask: which evidence event supports it?**
