# Episode 06 Walkthrough — Context: What Should AVI Actually See?

## 1. Opening Hook

What to say:

"AVI can collect more data now. That creates a new problem: if I dump every interface, every device, every old observation, and every note into the prompt, I have not built context engineering. I have built noise."

## 2. Trust Question

Can AVI receive enough information to reason usefully without burying the decision in stale, irrelevant, duplicated, or sensitive data?

## 3. Architecture

```text
Question
  + current evidence
  + selected topology
  + relevant state
  + prior tool results
        -> Context Assembler
              -> curated context
                    -> model
```

## 4. Run the Starter

```bash
python episodes/06-context/avi_pilot_06_context.py
```

## 5. Explain Context as a Product

What to say:

"The context window is not a junk drawer. The application should deliberately decide what the model needs for this decision."

Walk through the policy ideas:
- eligible sources,
- observation age,
- relevant devices,
- retained history,
- excluded sensitive data,
- token/context budget.

## 6. Demo 1 — Too Little Context

Ask the troubleshooting question with almost no operational context.

Show what the model/application cannot know and label missing evidence explicitly.

## 7. Demo 2 — Too Much Context

Pass a noisy bundle with irrelevant devices, duplicate observations, and stale state.

Discuss how more tokens can reduce clarity and traceability.

## 8. Demo 3 — Curated Context

Assemble only the sources relevant to the question.

Show source labels and observation age.

What to say:

"The goal is not the smallest prompt. The goal is the smallest sufficient operational context."

## 9. Stale Data Demo

Change an observation timestamp so it exceeds the allowed age.

Show the assembler excluding or labeling it stale.

## 10. Break It on Purpose

Remove a required source entirely.

Confirm AVI reports missing context instead of substituting a plausible answer.

## 11. Safety Boundary

Context selection can improve reasoning, but it cannot create truth. Missing evidence remains missing.

## 12. What AVI Still Cannot Do

AVI now sees relevant observed state, but it still does not know what the network is supposed to look like.

## 13. Homework

1. Add an explicit `max_age_minutes` rule.
2. Add one excluded source type.
3. Compare broad vs curated context.
4. Print which sources were included and why.

## 14. Next Flight

"Episode 7 adds intent. We are going to put NetBox on one side, live pyATS state on the other, and teach AVI to report drift without assuming either source is automatically correct."