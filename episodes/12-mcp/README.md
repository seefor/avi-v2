# Episode 12 — MCP

## Giving AVI reusable network tools

AVI already has safe network tools. MCP lets those contracts be reused by more than one client without duplicating the tool implementation.

## What AVI Gains

- MCP server
- discoverable tool contracts
- typed inputs and structured outputs
- consistent error behavior
- reusable access to existing `avi_core` tools
- evidence for MCP invocations

## Trust Question

Can we make AVI's tools reusable without weakening the safety checks that made them trustworthy?

## Architecture

```text
AVI / MCP client
      -> MCP server
          -> safe tool wrappers
              -> avi_core tool implementation
                  -> network backend
```

## Build Goals

Expose narrow tools such as:

- device status
- interface status
- BGP status
- topology lookup
- approved read-only show operation

Each MCP tool should define:

- clear name and description
- typed inputs
- target validation
- structured output
- predictable error contract
- evidence event for invocation

## Demo

1. start the MCP server,
2. list tools from a client,
3. call a read-only network tool,
4. inspect structured output and evidence,
5. send an invalid target or argument and show deterministic rejection.

## Safety Boundary

MCP is a protocol boundary, not a safety feature by itself. Narrow tools, validation, authorization, and evidence remain application responsibilities.

## Next

Episode 13 introduces human approval before AVI can move from observation and recommendation toward any risky action.
