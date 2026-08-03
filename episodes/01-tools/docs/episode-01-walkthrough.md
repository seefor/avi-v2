# Episode 01 Walkthrough — Tools

## Video Title
AVI #1 — Tools: Can an AI Safely Observe a Real Network?

## Hook
A chatbot can explain BGP. That does not mean it should be given a shell on your router. The first AVI problem is simpler: how do we let an AI ask for network state without giving the model direct device access?

## Talking Points
- the model is one component, not the executor
- pyATS is the network tool, not the AI
- the application owns credentials and command policy
- read-only observation is the first trust milestone

## Demo Flow
1. Show the lab testbed file with credentials excluded from Git.
2. Show the narrow Python tool wrapper.
3. Run the approved interface command.
4. Show the returned data.
5. Attempt a blocked command.
6. Point out that rejection occurs before execution.

## Camera Emphasis
Pause on the boundary between the model request and Python validation. That is the core lesson.

## Failure Scenario
Use an unapproved command or unreachable device and show a controlled error instead of an uncontrolled traceback or repeated retry.

## Close
AVI can now observe one device, but we still have a problem: if it later makes a claim, how do we prove exactly what it saw? Episode 2 adds evidence.
