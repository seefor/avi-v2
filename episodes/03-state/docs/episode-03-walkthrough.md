# Episode 03 Walkthrough — State

## Video Title
AVI #3 — State: Can AVI Turn pyATS Output Into Usable Network State?

## Hook
Network engineers can read a wall of CLI output. Agents and automation need something more explicit.

## Talking Points
- raw output is evidence, not yet a reusable state model
- state needs source, timestamp, and device identity
- missing data should stay missing
- normalization should not quietly turn observation into judgment

## Demo Flow
1. Show raw pyATS/CLI output.
2. Show the normalizer.
3. Produce an `InterfaceState` object.
4. Trace the state object back to its evidence ID.
5. Feed malformed or incomplete input and show explicit null/unknown handling.

## Failure Scenario
Remove a field or alter the CLI shape. Show that the normalizer reports incomplete state instead of filling the gap with a guess.

## Close
AVI can now represent what the network reported. Episode 4 decides whether those state objects are valid enough for another system to trust.
