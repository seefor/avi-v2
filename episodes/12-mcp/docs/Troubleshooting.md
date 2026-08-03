# Episode 12 Troubleshooting — MCP

## Client Cannot See the Server

Confirm the server process is running and that the MCP client configuration points to the correct command/transport.

## Tools Are Not Listed

Check server startup errors and tool registration names. Validate the server independently before debugging the client.

## Tool Call Returns Invalid Target

Episode 12 intentionally exposes demo data for approved lab device names only. Use one of the configured allowed targets or update the lab allowlist deliberately.

## Input Validation Error

Compare the client payload with the published tool schema. Do not loosen the schema simply to accept malformed input.

## MCP Tool Bypasses Evidence

Make the MCP wrapper call the same safe internal tool path used elsewhere. Avoid a shortcut implementation that returns data without recording the invocation.

## Duplicate Implementations Drift

If the MCP server and AVI app contain separate business logic, move the stable capability into `avi_core` and import it from both places.

## Debugging Order

```text
1. Start server directly
2. Confirm no startup error
3. List tools
4. Inspect tool schema
5. Call approved target
6. Call invalid target
7. Inspect evidence/error behavior
```