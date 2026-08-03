# Episode 03 Walkthrough — State: Teaching AVI to Read the Network

## 1. Opening Hook

What to say:

"A wall of CLI text is evidence, but it is a poor interface for everything we want to build next. Today AVI learns the difference between raw output and explicit network state."

## 2. Trust Question

Can AVI describe the observed network consistently without inventing missing fields or losing the source evidence?

## 3. Architecture

```text
pyATS / CLI
    -> raw evidence
        -> normalizer
            -> state object
                -> human / agent context
```

## 4. Run the Starter

```bash
python episodes/03-state/avi_pilot_03_state.py
```

## 5. Explain Raw Evidence vs. State

What to say:

"Evidence tells me what was collected. State is our explicit interpretation of that observation. I want to keep both because later I need to know where every state field came from."

## 6. Walk Through `InterfaceState`

Explain fields such as:
- device
- interface
- admin status
- operational status
- IP address
- source
- observed timestamp
- evidence ID

Show why normalized field names are easier for downstream code than parsing CLI every time.

## 7. Happy-Path Demo

Parse one interface observation and print the normalized object.

Point out that the evidence ID survives normalization.

## 8. Missing Data Demo

Use an observation with a missing address or unknown field.

What to say:

"Unknown is a valid operational state for AVI. Guessing is not."

Show an explicit `null`, `unknown`, or equivalent representation rather than fabricating a value.

## 9. Add Device and BGP State

Explain how the same pattern can represent device health and BGP neighbors while keeping separate models for different operational concepts.

## 10. Break It on Purpose

Feed the normalizer unexpected raw input and show the failure or incomplete-state behavior.

Teaching point:
- A normalizer should not silently invent defaults that change the meaning of the observation.

## 11. Review the Evidence Link

Trace one normalized field back to the underlying evidence event.

## 12. What AVI Still Cannot Do

AVI now has normalized state, but a Python dictionary or object can still be malformed. It needs formal schemas, allowed values, and deterministic validation.

## 13. Homework

1. Add a second interface fixture.
2. Add one BGP neighbor state.
3. Include a missing field and preserve it explicitly.
4. Confirm every state object retains its evidence reference.

## 14. Next Flight

"Episode 4 makes the state contract enforceable. If AVI produces malformed or invented structure, validation will stop the workflow instead of letting bad data move downstream."