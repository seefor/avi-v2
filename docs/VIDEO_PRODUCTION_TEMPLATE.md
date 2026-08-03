# AVI v2 Video Production Template

Use this template when upgrading an episode walkthrough from teaching notes into a recording-ready YouTube plan.

The technical topic changes from episode to episode. The production rhythm should remain recognizable so viewers feel AVI growing one capability at a time.

## YouTube Package

Every episode walkthrough should begin with:

- recommended YouTube title,
- two or three alternate titles,
- thumbnail direction,
- short thumbnail text,
- core viewer promise,
- target runtime range.

Title the video around the engineering problem first. Keep `AVI Ep. N` as series branding rather than making the episode number the main title.

Example:

```text
Can AI Safely Observe a Real Network? | Building AVI Ep. 1
```

not:

```text
AVI v2 Episode 1 — Tools
```

## Standard Recording Rhythm

### 1. Cold Open

Target: 30–60 seconds.

Start with the operational problem or the most interesting result. Avoid a long channel introduction.

Answer:

- Why should a network engineer care?
- What will AVI gain today?
- What are we deliberately refusing to give AVI yet?

### 2. Trust Question

Every episode must state one explicit trust question.

Examples:

- Can the model request data without unrestricted SSH?
- Can an engineer prove which observation supports a claim?
- Can another system safely consume AVI's structured output?
- Can AVI investigate without looping forever?
- Can AVI prove a human approved this exact action?

### 3. Flight Rules / Safety Boundary

Show what remains prohibited.

Do not present safety only as prompt text. Identify which control is enforced by application logic, schema validation, policy, approval records, or execution gates.

### 4. Architecture

Show the architecture for the current episode.

Then show how it changed from the previous episode.

The series should visually grow like this:

```text
Tool -> Evidence -> State -> Structure -> Scale -> Context -> Intent -> Knowledge
     -> Harness -> Loop -> Verification -> Reuse -> Approval -> Plan -> Action
```

### 5. Repository Orientation

Show only the files relevant to today's lesson.

Avoid scrolling through the entire repository.

Tell viewers which files they will touch before opening the editor.

### 6. Environment / Inputs

Show exact commands and input files required for reproduction.

Examples:

- virtual environment,
- testbed,
- inventory,
- fixtures,
- runbook corpus,
- context policy,
- MCP server,
- approval packet,
- change plan.

### 7. Code Walkthrough

Use the actual function/class names in the episode starter.

Do not read every line.

Organize the code into logical chunks:

```text
Input -> Policy -> Execution -> Validation -> Evidence -> Output
```

When applicable, explicitly identify which parts are model behavior and which parts are deterministic application controls.

### 8. Happy-Path Demo

Run the actual episode starter.

Before pressing Enter, state what should happen.

After the output appears, explain what the result proves—and what it does not prove.

### 9. Break It on Purpose

Required in every episode.

Demonstrate one controlled failure or rejection that reinforces the episode's trust question.

Examples by layer:

```text
Tools          unsafe command
Evidence       failed/blocked call still recorded
State          missing field remains unknown
Structure      malformed object rejected
Scale          unreachable device does not hide fleet results
Context        stale/irrelevant context excluded
Intent         missing or stale intended state
RAG            no relevant source found
Harness        unauthorized tool request blocked
Loops          duplicate/no-progress loop stopped
Verification   plausible unsupported claim rejected
MCP            invalid target/argument rejected
Approval       expired/wrong-target approval rejected
Planning       missing rollback/postcheck rejected
Action         failed postcheck triggers rollback
```

Use the recurring line when appropriate:

> "A trustworthy system should show what it refuses to do, not just what it can do."

### 10. Evidence Review

Show the evidence artifact produced by the current layer.

Ask:

- What can an engineer inspect?
- Can a later claim point back to this evidence?
- What remains transient or incomplete?

### 11. What AVI Still Cannot Do

Required slide in every episode.

Keep it concrete.

AVI gets capability only after the previous layer becomes observable, testable, and reviewable.

### 12. Homework

Give three to five small modifications viewers can make safely.

Homework should reinforce the current layer, not jump ahead to future permissions.

### 13. Next Flight

Show the architecture gaining exactly one new layer.

Tease the trust question for the next episode.

End quickly. Avoid a long outro.

## Standard Walkthrough Metadata

Each production-ready `Walkthrough.md` should contain:

```text
YouTube Package
Target Runtime
Recording Run of Show
Exact Terminal Commands
Exact Files to Open
Exact Functions/Classes to Explain
Happy-Path Demo
Intentional Failure Demo
Evidence Review
What AVI Still Cannot Do
Homework
Next Flight
Recording Checklist
Suggested Chapter Markers
Production Notes
```

## Production Style

Camera works best for:

- hook,
- framing/trust question,
- major takeaway,
- wrap-up.

Editor and terminal should carry most of the technical teaching.

Slides should explain architecture, boundaries, and mental models—not reproduce paragraphs from the walkthrough.

## Recurring Series Language

Use these phrases consistently when they fit naturally:

> **AVI has to earn the right to automate the network.**

> **The model can request. The application decides.**

> **Good agents are built on boring tools that work.**

Do not force all three into every episode. The first is the series north star; the others should appear where the lesson supports them.

## Runtime Guidance

Do not force every video to one hour.

Typical ranges:

- focused control/validation episode: 20–30 minutes,
- substantial architecture/tool episode: 25–40 minutes,
- RAG/MCP/agent-loop episodes: 30–45 minutes,
- controlled-action finale: 40–60 minutes.

Stop when the lesson is complete.
