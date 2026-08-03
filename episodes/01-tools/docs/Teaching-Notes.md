# Episode 01 Teaching Notes — Tools

## Core Lesson

An LLM can reason about network observations, but it does not know the current state of a router unless the application gives it a tool that can collect that state. The tool boundary is where operational control begins.

## pyATS and Unicon

A pyATS testbed describes devices, operating systems, credentials, and connection methods. Unicon is the connection layer pyATS uses for CLI devices. A useful beginner explanation is:

> pyATS gives AVI the device model; Unicon handles the live CLI session.

This keeps SSH mechanics out of the agent logic.

## Why Read-Only Comes First

Read-only access gives us a low-risk environment for proving the mechanics that will matter later: target validation, command policy, timeouts, connection handling, structured results, and clean disconnects.

The goal is not to make AVI impressive in Episode 1. The goal is to make the first capability understandable and repeatable.

## Model Permission vs. Application Permission

A prompt can tell a model not to run configuration commands, but prompts are not enforcement. The Python application must independently decide:
- whether the tool exists,
- whether the target is approved,
- whether the operation is permitted,
- whether credentials can be used,
- when the request must stop.

Use the phrase: "The model can request. The application authorizes."

## Why Small Tools Matter

Small tools are easier to test, document, secure, and reuse. A narrow `get_interface_status` capability is safer than giving the model a generic function that executes arbitrary CLI.

## Optional Deep-Dive Questions

- What changes if there are ten devices instead of one?
- Should a `show` prefix automatically make a command safe?
- Where should secrets live in a production deployment?
- How would authorization differ between a lab and production?

## Key Takeaway

AVI does not earn trust because the model sounds careful. It earns trust because the surrounding application puts hard boundaries around what the model can do.