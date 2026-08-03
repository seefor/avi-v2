# Episode 06 Walkthrough — Context

## Video Title
AVI #6 — Context: What Information Should AVI Actually See?

## Hook
A bigger context window does not mean a better architecture. AVI now has enough data that choosing what not to send becomes part of the engineering.

## Talking Points
- prompt engineering asks how to instruct the model
- context engineering asks what information the model needs
- freshness, relevance, and source identity matter
- more tokens can mean more noise

## Demo Flow
1. Ask a network question with almost no context.
2. Ask it again with a large unfiltered data dump.
3. Run the context assembler.
4. Ask with curated current evidence.
5. Print which sources were included, excluded, or considered stale.

## Failure Scenario
Mark an important observation stale or unavailable and show AVI reporting the missing evidence rather than quietly using it.

## Close
AVI now sees selected operational state. In Episode 7 we add a different kind of context: intended state from NetBox, and we keep it separate from what the devices report.
