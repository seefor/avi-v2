# Episode 04 Walkthrough — Structure

## Video Title
AVI #4 — Structure: Why Agent Output Must Be Validated

## Hook
A model can return JSON that looks right and still be wrong enough to break the next step.

## Talking Points
- structured output is a contract
- model output is a candidate result
- code decides whether that candidate is acceptable
- validation failure should stop the workflow

## Demo Flow
1. Produce a valid state object.
2. Validate and serialize it.
3. Remove a required field.
4. Inject an unsupported value.
5. Show both failures stopping downstream execution.

## Failure Scenario
Use a model-generated payload with one subtle schema violation. The lesson is that readable is not the same as automation-safe.

## Close
AVI can now produce validated structured observations. Next we have to keep that discipline when one device becomes many.
