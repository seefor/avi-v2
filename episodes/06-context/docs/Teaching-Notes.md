# Episode 06 Teaching Notes — Context

## Context Engineering for Network Operations

A model does not need every fact the organization owns. It needs the right evidence, state, topology, and recent history for the current task.

## Relevance, Freshness, and Sensitivity

A practical context policy should ask:
- Is the source relevant to this question?
- Is the observation recent enough?
- Is the source authoritative for the claim being considered?
- Does this information contain secrets or unnecessary sensitive data?
- Does it fit within a predictable context budget?

## Missing Context Must Be Visible

If the current BGP state was never collected, AVI should not hide that gap behind a polished explanation. Missing context is an operational fact.

## Context Is Not Memory

Context is the working set selected for one decision. Long-term memory, evidence retention, and source-of-truth data may feed context, but they are different concepts.

## Why Token Budgets Matter

A token budget is not only a cost control. It forces prioritization and reduces the temptation to solve uncertainty by dumping more data into the prompt.

## Optional Analogy

A network engineer troubleshooting one branch outage does not open every configuration in the company. They gather the topology, current state, recent changes, and procedures relevant to that branch.

## Key Takeaway

Better agents are often built by improving the information boundary around the model, not by asking the model to reason over everything.