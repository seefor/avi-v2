# Episode 12 Walkthrough — MCP

## Video Title
AVI #12 — MCP: Giving AVI Reusable Network Tools

## Hook
The same safe BGP or interface tool should not have to be rewritten for every AI client. MCP gives us a reusable contract—but it does not make unsafe tools safe.

## Talking Points
- MCP separates tool provider from tool consumer
- the business logic remains in `avi_core`
- tool safety stays in validation and policy
- every client invocation should still leave evidence

## Demo Flow
1. Start the MCP server.
2. Discover AVI network tools from a client.
3. Call a safe status tool.
4. Inspect typed structured output.
5. Trace the MCP call to an AVI evidence record.
6. Send an invalid target or input and show rejection.

## Failure Scenario
Attempt to call a tool or argument outside the defined contract. Show that reuse does not bypass policy.

## Close
AVI's tools are now reusable. Episode 13 adds a different boundary: before risky actions can even be considered, AVI must produce a complete approval request tied to evidence and an exact target.
