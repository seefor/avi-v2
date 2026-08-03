# Episode 15 Teaching Notes — Controlled Action

## Why the First Write Action Should Be Boring

A narrow lab action lets us test control integrity without combining that test with unnecessary network risk. The educational objective is the gating and evidence chain, not a flashy configuration change.

## Exact Matching

Execution should require the same target, action, plan, and approval scope. Any material mutation should invalidate eligibility.

## Pre-Change Snapshot

A snapshot provides a known reference for:
- confirming assumptions,
- measuring the expected diff,
- constructing/verifying rollback.

## Postcheck Is the Definition of Success

A command returning successfully does not prove the intended operational state exists. AVI should re-observe the network and compare against explicit success criteria.

## Rollback Is a Workflow, Not a String

Rollback should have its own execution evidence and verification. A rollback command that runs but fails to restore state is not a successful recovery.

## Fail Closed

Examples that should stop execution:
- expired approval,
- target mismatch,
- unsupported action class,
- missing rollback,
- failed precheck,
- invalid plan,
- missing evidence linkage.

## Production Boundary

Moving from this simulator to a live backend requires additional operational controls such as identity, RBAC, secrets management, environment isolation, transaction/concurrency policy, maintenance windows, audit retention, and organization-specific change governance.

## Series Takeaway

The architecture—not model intelligence alone—is what earns progressively more capability.