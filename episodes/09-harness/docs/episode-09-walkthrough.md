# Episode 09 Walkthrough — Harness

## Video Title
AVI #9 — Harness: Building Controls Around the Model

## Hook
At this point AVI has prompts, network tools, evidence, state, context, intent, and RAG. If those pieces are just glued together around an LLM call, we still do not have a system I would trust.

## Talking Points
- the harness is the application around the model
- prompt policy and enforced policy are different things
- the model reasons; code controls execution
- stable capabilities should move into reusable `avi_core` modules

## Demo Flow
1. Show the harness architecture.
2. Submit one troubleshooting request.
3. Trace context selection and prompt construction.
4. Show the model requesting a tool.
5. Show policy validation before execution.
6. Review the evidence and validated response.
7. Request a blocked capability and show policy rejection.

## Failure Scenario
Have the model request a tool that is not registered or permitted. The harness should reject it deterministically.

## Close
Now AVI is more than a set of scripts. Episode 10 gives that harness a controlled investigation loop, including progress detection and hard stop conditions.
