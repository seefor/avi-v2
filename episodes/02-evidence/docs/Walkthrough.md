# Episode 02 Walkthrough — Evidence: The Black Box Recorder

## 1. Opening Hook

What to say:

"AVI touched the network in Episode 1. Now I want to answer a harder question: if AVI tells me a BGP neighbor was idle or an interface was down, can I prove exactly what tool event that statement came from?"

## 2. Trust Question

Can an engineer inspect the exact event behind a later AVI claim?

## 3. Architecture

```text
Tool Request -> Validation -> Execution -> Result
                    |             |
                    +-------------+-> Evidence Recorder -> JSONL
```

What to say:

"Evidence is not an optional debug log. It becomes part of AVI's control plane."

## 4. Run the Starter

From the repository root:

```bash
python episodes/02-evidence/avi_pilot_02_evidence.py
```

## 5. Build the Evidence Record

Walk through the fields:
- `run_id`
- `evidence_id`
- timestamp
- tool
- target
- arguments
- status
- duration
- summary
- error

Explain why `run_id` groups one investigation while `evidence_id` identifies one tool event.

## 6. Happy Path

Run a successful tool call and show the evidence record written to JSONL.

What to say:

"The terminal output is useful for us right now. The evidence ID is useful to every later layer because it gives us something stable to reference."

## 7. Record a Blocked Request

Trigger a policy rejection.

Show that the blocked request also leaves evidence.

Teaching point:
- Refusals are operationally important events.
- A black-box recorder should capture failures and policy blocks, not only successes.

## 8. Record a Failure

Use the starter's failed connection/error path.

Review the error field and duration.

What to say:

"We do not want a failed observation silently disappearing. Later AVI must be able to distinguish 'the interface is down' from 'I failed to observe the interface.'"

## 9. Talk About Redaction

Explain that evidence should be useful without dumping credentials, tokens, full secrets, or unnecessary sensitive payloads.

## 10. Review the JSONL

Open the evidence file and correlate terminal events to records.

Point out:
- immutable event-per-line format,
- unique IDs,
- status differences,
- compact summary vs raw sensitive data.

## 11. Break It on Purpose

Temporarily send an argument containing a fake secret/token-like field and demonstrate or explain the redaction rule.

## 12. What AVI Still Cannot Do

AVI has evidence, but the evidence is still raw observation. It does not yet have a normalized representation of interfaces, devices, or BGP state.

## 13. Homework

Ask viewers to:
1. Add a new evidence field such as caller or lab environment.
2. Run success, blocked, and failure cases.
3. Correlate all events with a shared `run_id`.
4. Verify no secret is written to the evidence file.

## 14. Next Flight

"In Episode 3 we stop treating CLI output as the final answer. AVI will turn observations into explicit network state objects that humans and later automation can reason over consistently."