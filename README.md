# AVI v2

**Building an AI Network Engineer One Layer at a Time**

AVI v2 is a build-in-public network AI assistant project for network engineers who want to understand how a trustworthy agent is engineered around real network operations.

AVI does not begin with autonomy. It begins with observation, evidence, validation, and control.

> Good agents are built on boring tools that work.

## Why AVI v2 Exists

The first AVI repository proved the value of building capability gradually. AVI v2 turns that idea into a complete 15-episode architecture that follows one assistant from safe read-only observation through evidence, context, intent, RAG, controlled agent loops, verification, reusable MCP tools, human approval, change planning, and finally one tightly bounded lab action.

The series is designed as a continuation of the ideas in **Building AI Agents for Network Operations**. The book teaches the patterns. AVI v2 keeps building one assistant and shows what those patterns look like when they are assembled into a larger operational system.

## North Star

AVI is not about giving AI control of the network as quickly as possible.

AVI is about **earning the right to automate the network**.

Each episode must answer four questions:

1. What new capability did AVI gain?
2. What evidence can an engineer inspect?
3. What safety boundary still exists?
4. What must be true before AVI earns the next capability?

## The 15-Episode Roadmap

| # | Layer | Episode | What AVI Learns |
|---|---|---|---|
| 1 | Tools | Can an AI safely observe a real network? | Use one approved pyATS-based read-only tool without giving the model direct device access. |
| 2 | Evidence | How do we prove what the agent actually saw? | Record tool calls, inputs, timing, status, summaries, failures, and evidence IDs. |
| 3 | State | Can AVI turn pyATS output into usable network state? | Normalize raw network observations into explicit interface, device, and BGP state. |
| 4 | Structure | Why agent output must be validated | Validate schemas, required fields, allowed values, missing data, and malformed output. |
| 5 | Scale | What changes when AVI looks at multiple devices? | Observe multiple devices with bounded concurrency while preserving per-device evidence. |
| 6 | Context | What information should AVI actually see? | Assemble only the relevant operational context for the current decision. |
| 7 | Intent | NetBox vs. live network state | Compare intended state from a source of truth with observed state from the network. |
| 8 | RAG | Giving AVI runbooks and operational knowledge | Retrieve relevant runbooks and operational documents with source citations. |
| 9 | Harness | Building controls around the model | Put context, prompts, tools, policy, validation, evidence, and model calls behind one controlled harness. |
| 10 | Loops | Teaching AVI when to investigate further | Run bounded gather-reason-act-verify loops with progress detection and explicit stop conditions. |
| 11 | Verification | How AVI knows whether its hypothesis is supported | Separate observations, hypotheses, supported findings, uncertainty, and unresolved questions. |
| 12 | MCP | Giving AVI reusable network tools | Expose the same narrow network capabilities through reusable MCP contracts. |
| 13 | Human Approval | When AVI needs permission | Create complete approval packets and enforce decision, scope, target, and expiration checks. |
| 14 | Change Planning | Recommendation before execution | Produce reviewable change plans with prechecks, diffs, postchecks, risks, and rollback. |
| 15 | Controlled Action | Earning the right to make a network change | Execute one tightly bounded lab change only after all previous controls pass. |

## Learning Progression

```text
Tool
  -> Evidence
  -> State
  -> Structure
  -> Scale
  -> Context
  -> Intent
  -> Knowledge
  -> Harness
  -> Loop
  -> Verification
  -> Reuse
  -> Approval
  -> Plan
  -> Action
```

The order matters. AVI does not get more power simply because the model can ask for it. AVI gains capability only after the previous layer is observable, testable, and reviewable.

## Repository Layout

```text
avi-v2/
├── README.md
├── .gitignore
├── requirements.txt
├── docs/
│   ├── SERIES_ARCHITECTURE.md
│   └── CONTENT_WORKFLOW.md
├── avi_core/
│   └── README.md
└── episodes/
    ├── 01-tools/
    ├── 02-evidence/
    ├── 03-state/
    ├── 04-structure/
    ├── 05-scale/
    ├── 06-context/
    ├── 07-intent/
    ├── 08-rag/
    ├── 09-harness/
    ├── 10-loops/
    ├── 11-verification/
    ├── 12-mcp/
    ├── 13-human-approval/
    ├── 14-change-planning/
    └── 15-controlled-action/
```

Each episode contains:

- `README.md` — the technical lesson, scope, safety boundary, demo, and build goals
- `docs/episode-NN-walkthrough.md` — camera-ready teaching and demo flow for YouTube

As the implementation grows, reusable code moves into `avi_core/` instead of being copied between episodes.

## Series Rules

1. Read-only first.
2. The model never receives device credentials.
3. The model does not directly execute arbitrary commands.
4. Every tool invocation leaves evidence.
5. Structured output is validated before downstream use.
6. Current observed state and intended state remain separate concepts.
7. Retrieved documents must retain source identity.
8. Agent loops have hard iteration, time, and duplicate-call limits.
9. Final claims must point back to evidence.
10. MCP makes tools reusable, not automatically safe.
11. Risky actions require explicit human approval.
12. Approval does not replace change planning.
13. Controlled execution requires prechecks and postchecks.
14. Failed validation stops the workflow.
15. The first write action remains narrow, reversible, and lab-only.

## Relationship to the Book

The book progresses from LLM fundamentals and prompts through structured output, memory, tool calling, troubleshooting, MCP, and production-readiness patterns.

AVI v2 starts from that foundation and keeps going with one evolving assistant:

```text
BOOK
Learn the patterns
        ↓
AVI v2
Build the assistant layer by layer
        ↓
Future Platform Direction
Engineer a larger operational system
```

## Recommended Video Format

Every episode should use the same teaching rhythm:

1. Operational problem
2. Trust question
3. Architecture
4. Build
5. Successful demonstration
6. Failure or blocked demonstration
7. Evidence review
8. What AVI still cannot do
9. Next layer

That keeps the series focused on engineering decisions rather than disconnected code demos.

## Safety

AVI v2 is an educational lab project. Do not point early episode code at production systems. Do not commit credentials, tokens, running configurations, or private operational data.

The controlled-action episode must remain limited to a designated lab or sandbox target with an explicitly reversible change.

## Status

The complete 15-episode series architecture and teaching walkthroughs are being built in this repository. Implementation will grow episode by episode so the code reflects the same trust-first progression as the videos.
