# AVI v2 Series Architecture

AVI v2 treats the language model as one component inside a controlled network automation system.

```text
User / Operator
      |
      v
+------------------------------+
|          AVI Harness         |
|                              |
|  Policy / Permissions        |
|  Context Assembly            |
|  Prompt Construction         |
|  Model Call                  |
|  Tool Registry               |
|  Evidence Recorder           |
|  Validation                  |
|  Loop Controller             |
|  Verification                |
|  Approval Gate               |
+---------------+--------------+
                |
                v
        Approved Network Tools
                |
        +-------+--------+
        |                |
      pyATS            MCP
        |                |
        +-------+--------+
                |
         Network / Lab Data

Supporting context sources:
- NetBox or another source of intended state
- runbooks and operational documentation
- recent tool evidence
- topology and inventory
- change records or incident context when available
```

## Engineering Layers

### 1. Tools
The model never receives a shell. The application exposes narrow tools with known inputs and outputs.

### 2. Evidence
Every tool invocation receives an evidence ID and records the request, target, timing, status, result summary, and error state.

### 3. State
Raw device data becomes explicit network state objects before reasoning depends on it.

### 4. Structure
Schemas and deterministic validation decide whether a candidate result is safe for downstream use.

### 5. Scale
Multi-device work preserves per-device evidence and handles partial failure instead of collapsing everything into one success/failure result.

### 6. Context
The context layer selects relevant evidence for the current question rather than dumping every available artifact into the model.

### 7. Intent
Intended state and observed state are represented separately. AVI reports drift; it does not assume either source is automatically correct.

### 8. Knowledge
RAG adds runbooks and operational knowledge with source identity and citations. Retrieval augments context; it does not replace live state.

### 9. Harness
The harness owns orchestration. The prompt can state policy, but code enforces tool permissions, limits, validation, and approval rules.

### 10. Loops
Investigation is bounded by iteration, tool-call, runtime, duplicate-call, and progress limits.

### 11. Verification
AVI separates observations from hypotheses and requires evidence references before presenting a claim as supported.

### 12. MCP
MCP exposes reusable contracts around the same safe tools. Protocol reuse does not weaken the validation boundary.

### 13. Approval
Approval is a structured record tied to an exact target, action, evidence set, risk, and expiration.

### 14. Change Planning
AVI creates a reviewable change plan before execution: objective, target, commands, expected diff, prechecks, postchecks, risks, and rollback.

### 15. Controlled Action
The first action is narrow, lab-only, pre-approved, reversible, and automatically followed by verification.

## Separation of Responsibility

- **Model:** language understanding and reasoning over supplied context.
- **Harness:** orchestration and workflow state.
- **Tool layer:** execution and input/output validation.
- **Context layer:** selection and labeling of information.
- **Evidence layer:** traceability.
- **Verification layer:** claim-to-evidence checks.
- **Authorization/approval layer:** access and human control.
- **Network engineer:** operational ownership and final accountability.

## Trust Progression

AVI should never gain a capability simply because it is technically possible. Each episode must prove the previous layer works under both a happy path and a failure path before the next layer is introduced.
