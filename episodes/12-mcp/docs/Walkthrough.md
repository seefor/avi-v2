# Episode 12 Walkthrough — MCP: Reusable Network Tools

## 1. Opening Hook

What to say:

"AVI has safe network tools already. Today we make those tools reusable through MCP. But there is one thing I want to make clear before we write a line of code: MCP is a protocol boundary, not a safety system."

## 2. Trust Question

Can we reuse AVI's tools across clients without weakening the policies that made them trustworthy?

## 3. Architecture

```text
AVI / MCP client
      -> MCP server
          -> safe tool wrappers
              -> avi_core tool implementation
                  -> network backend
```

## 4. Start the MCP Server

```bash
cd episodes/12-mcp
python mcp_server.py
```

Use an MCP-capable client or inspector to discover the available tools.

## 5. Explain the Contract

Walk through tool definitions such as:
- `device_status`
- `bgp_status`

Explain:
- name and description,
- typed inputs,
- approved target validation,
- structured output,
- predictable errors,
- evidence event.

## 6. Discover Tools

From the client/inspector, list the server's available tools.

What to say:

"Discovery is useful, but discoverable does not mean unrestricted."

## 7. Happy-Path Tool Call

Call one approved read-only tool for an approved lab target.

Show:
- structured result,
- evidence/log entry,
- reuse of the same internal capability.

## 8. Invalid Target Demo

Pass an unapproved device name.

Confirm the server/tool layer rejects it deterministically.

## 9. Invalid Argument Demo

Send a malformed or unsupported argument and inspect the error contract.

## 10. Explain Reuse

What to say:

"MCP lets another client speak to the capability. I do not want to copy-paste the network implementation into every client. The safe behavior still belongs in the shared tool layer."

## 11. Break It on Purpose

Describe or demonstrate what would be unsafe: exposing a generic `run_any_cli_command` tool simply because MCP makes it easy to publish.

## 12. Safety Boundary

MCP does not replace authorization, validation, evidence, target scope, or tool design.

## 13. What AVI Still Cannot Do

AVI can recommend and verify, and clients can reuse its tools, but any risky action still requires explicit human permission.

## 14. Homework

1. Inspect all published tool schemas.
2. Add one safe read-only tool.
3. Test an invalid target.
4. Confirm every MCP invocation creates evidence.

## 15. Next Flight

"Episode 13 creates a real human approval artifact. Not a generic yes/no flag—a decision bound to an exact action, exact target, evidence, risk, and expiration."