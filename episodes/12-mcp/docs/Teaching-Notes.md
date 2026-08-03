# Episode 12 Teaching Notes — MCP

## MCP Solves Reuse and Discovery

Model Context Protocol provides a standard way for clients to discover and call tools/resources. It does not automatically determine whether those tools are operationally safe.

## Keep Safety Below the Protocol Boundary

The safest pattern is for MCP wrappers to call already-safe application tools. Authorization, target validation, structured output, evidence recording, and narrow command scope should not disappear when the tool is exposed through MCP.

## Typed Tool Contracts

Typed inputs improve predictability and let clients understand required fields before invocation. Structured outputs make downstream handling easier and reduce parsing ambiguity.

## Error Contracts

A reusable tool should distinguish:
- invalid input,
- unauthorized target/action,
- backend failure,
- timeout,
- successful observation.

## Reuse Without Duplication

If `avi_core` already knows how to obtain BGP state safely, the MCP server should wrap that implementation rather than create a second independent path to the network.

## Key Teaching Phrase

"MCP makes capability portable. The safety properties still come from the capability we chose to expose and the controls underneath it."

## Key Takeaway

Reusable agent tools should preserve the same contracts and boundaries no matter which client calls them.