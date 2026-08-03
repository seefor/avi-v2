# Episode 12 Walkthrough — Reuse AVI's Network Tools with MCP Without Weakening Safety

This is the production-ready recording guide for AVI v2 Episode 12.

## YouTube Package

Recommended title: **Build an MCP Server for Network Automation | Building AVI Ep. 12**

Alternates:
- **Give AI Agents Reusable Network Tools with MCP | AVI Ep. 12**
- **MCP Makes Tools Reusable — Not Automatically Safe | AVI Ep. 12**

Thumbnail text: **MCP ≠ SAFETY**

Core promise: expose narrow read-only AVI tools through MCP while preserving deterministic target validation.

Target runtime: **35–45 minutes**.

---

# Recording Run of Show

## 0:00–0:50 — Cold Open

> "AVI already has narrow network capabilities. Today we're making them reusable through MCP. But before we start, I want one thing clear: MCP is a protocol boundary. It is not a safety system."

Flash the two published tools and then the invalid-device rejection.

## 0:50–2:15 — Trust Question

Slide: **Can We Reuse AVI's Tools Without Weakening the Controls That Made Them Trustworthy?**

```text
Client -> MCP -> Safe Tool -> Validation -> Result
```

## 2:15–4:00 — Architecture

```text
MCP Client
   ↓
FastMCP Server
   |- device_status()
   `- bgp_status()
          ↓
   validate_device()
          ↓
      demo backend
```

Explain that the longer-term architecture can reuse shared `avi_core` capabilities. The Episode 12 starter currently returns demo data directly from the MCP tool functions.

## 4:00–5:30 — Starter Orientation

Open:

```text
episodes/12-mcp/mcp_server.py
```

Run from the episode directory:

```bash
cd episodes/12-mcp
python mcp_server.py
```

Use the MCP client or inspector you already use for demos to discover and call the server.

Focus on:
- `FastMCP("avi-v2-network-tools")`
- `ALLOWED_DEVICES`
- `validate_device()`
- `device_status()`
- `bgp_status()`

## 5:30–8:00 — Server and Target Scope

Highlight:

```python
mcp = FastMCP("avi-v2-network-tools")
ALLOWED_DEVICES = {"lab-r1", "lab-r2"}
```

### What to say

> "The protocol can expose capabilities to multiple clients. Scope still belongs to the application. In this episode only two demo device names are approved."

## 8:00–10:00 — `validate_device()`

Show:

```python
def validate_device(device: str) -> None:
    if device not in ALLOWED_DEVICES:
        raise ValueError(f"Device is not approved: {device}")
```

### Key line

> "A client can discover a tool. That does not mean the client gets to expand the tool's target scope."

## 10:00–13:00 — `device_status()`

Show:

```python
@mcp.tool()
def device_status(device: str) -> dict:
    validate_device(device)
    return {"device": device, "status": "up", "source": "avi-demo"}
```

Explain:
- discoverable tool contract,
- typed `device` input,
- deterministic validation,
- structured result.

Be explicit that this returns demo data rather than a live network call.

## 13:00–16:00 — `bgp_status()`

Show:

```python
@mcp.tool()
def bgp_status(device: str) -> dict:
    validate_device(device)
    state = "Idle" if device == "lab-r2" else "Established"
```

Explain how the same tool contract can produce different structured states for approved targets.

## 16:00–20:00 — Start and Discover the Server

Start:

```bash
python mcp_server.py
```

From your MCP-capable client/inspector, list tools.

Show:

- `device_status`
- `bgp_status`
- tool descriptions,
- input schema.

### What to say

> "Discovery is useful because clients no longer need hardcoded knowledge of every tool. But discoverable still does not mean unrestricted."

## 20:00–23:00 — Happy-Path Tool Call

Call:

```text
device_status(device="lab-r1")
```

Then call:

```text
bgp_status(device="lab-r2")
```

Show the structured outputs and explain the `source: avi-demo` field.

## 23:00–26:00 — Break It on Purpose: Invalid Device

Call either tool with:

```text
device="prod-core-01"
```

or another name outside `ALLOWED_DEVICES`.

Expected error:

```text
Device is not approved: prod-core-01
```

### What to say

> "This is the important demo. The MCP client can request a target. The server-side application still decides whether that target is in scope."

## 26:00–28:00 — Invalid Argument Demo

Use the client/inspector to omit the required `device` argument or pass an incompatible input shape.

Show the protocol/tool validation error.

Explain the difference between:

- protocol/input validation,
- AVI's application-level target validation.

## 28:00–30:00 — What Not to Publish

Slide:

```text
BAD MCP TOOL:
run_any_cli_command(device, command)

BETTER:
device_status(device)
bgp_status(device)
```

> "MCP makes publishing a generic capability easy. That doesn't make the capability a good idea. Narrow tools are easier to authorize, validate, test, and audit."

## 30:00–32:00 — Evidence Gap in This Starter

Be explicit:

> "The broader AVI architecture requires evidence for MCP invocations, but this small Episode 12 server does not yet wire the Episode 2 evidence recorder into these tool functions. That is a hardening step, not something I'm going to pretend is already here."

This distinction keeps the video aligned with the code.

## 32:00–34:00 — What AVI Still Cannot Do

AVI's read-only capabilities can now be reused by MCP clients. AVI still cannot safely move toward risky action without:

- a specific human approval artifact,
- exact action and target binding,
- expiration,
- risk and evidence context.

## 34:00–35:30 — Homework

1. Inspect both MCP tool schemas.
2. Add one narrow read-only tool.
3. Test an unapproved target.
4. Add evidence recording around MCP invocations.
5. Do not publish a generic arbitrary CLI tool.

## 35:30–36:30 — Next Flight

```text
Verified Recommendation
        ↓
Human Approval Packet
        ↓
Bound Decision Record
```

> "Episode 13 gives AVI something it has not had yet: permission. But we're not using a generic approved flag. We're going to bind approval to an exact action, exact target, evidence, and expiration."

---

# Recording Checklist

- [ ] MCP server starts successfully.
- [ ] Client/inspector can discover both tools.
- [ ] `lab-r1`/`lab-r2` calls succeed.
- [ ] Unapproved-device call is rehearsed.
- [ ] Do not claim live network calls are implemented in the starter.
- [ ] Do not claim evidence recording is already wired into MCP.

# Suggested Chapters

```text
00:00 MCP is not a safety system
00:50 The reuse trust question
02:15 MCP architecture
04:00 Episode 12 starter
05:30 Server and target scope
08:00 Device validation
10:00 device_status
13:00 bgp_status
16:00 Discover MCP tools
20:00 Happy-path tool calls
23:00 Reject an unapproved device
26:00 Invalid argument demo
28:00 What not to publish as an MCP tool
30:00 Evidence gap and hardening
32:00 What AVI still cannot do
34:00 Homework
35:30 Episode 13 tease
```

## Series takeaway

> **MCP makes capabilities reusable. Safety still comes from narrow tool design, validation, authorization, and evidence.**
