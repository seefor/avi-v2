# Episode 04 Walkthrough — Structure: Validate Before You Trust

## 1. Opening Hook

What to say:

"JSON that looks right is not the same thing as data that is safe for another system to consume. Today AVI gets a contract: required fields, allowed values, logical rules, and a controlled failure path."

## 2. Trust Question

Can another system consume AVI output without a human first reading every field?

## 3. Architecture

```text
candidate state -> schema validation -> valid object
                            |
                            +-> controlled failure
```

## 4. Run the Starter

```bash
python episodes/04-structure/avi_pilot_04_structure.py
```

## 5. Explain the Schema

Walk through:
- required fields,
- types,
- enum/allowed values,
- null handling,
- evidence references,
- schema version.

What to say:

"The schema is the contract between AVI and everything downstream."

## 6. Valid Case

Show a state object that passes validation.

Explain that passing validation means the object has the expected shape and rules—not that the observation itself is necessarily true.

## 7. Missing Required Field

Remove a required field and rerun validation.

Show the controlled error and confirm downstream processing stops.

## 8. Invented or Unsupported Value

Use a status value outside the allowed vocabulary.

What to say:

"This is exactly the kind of plausible-looking output we want to reject."

## 9. Logical Validation

Demonstrate a cross-field rule such as established BGP peers not exceeding total peers.

Teaching point:
- Type validation is necessary but insufficient.
- Operational logic can enforce relationships between fields.

## 10. Break It on Purpose

Feed malformed JSON or an impossible state combination.

Show that failure is explicit and inspectable.

## 11. What AVI Still Cannot Do

AVI can validate one state object, but the next challenge is operating across several devices while preserving evidence and handling partial failures.

## 12. Homework

1. Add one new allowed state value deliberately.
2. Add a fixture that should fail.
3. Add a logical validation rule.
4. Make sure a failed object cannot move downstream.

## 13. Next Flight

"Episode 5 leaves the comfort of one device. AVI will observe a small fleet with bounded concurrency and prove that one broken target does not erase the results from the others."