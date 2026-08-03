# AVI v2 Content Workflow

Each technical episode should produce one coherent content package rather than separate code, video, and blog ideas.

## Episode Content Package

Every episode should answer:

1. What operational problem are we solving?
2. What trust question does the new capability introduce?
3. What changed in the AVI architecture?
4. What code is new?
5. What does the successful path look like?
6. What does the blocked or failed path look like?
7. What evidence can an engineer review?
8. What can AVI still not do?
9. What does the next episode add?

## YouTube Flow

Recommended episode structure:

### Hook
Start with the operational problem, not with code.

### Architecture
Show where this layer sits around the model.

### Build
Walk through only the code that matters to the new capability.

### Demo: expected path
Show the capability working.

### Demo: failure or safety boundary
Show a timeout, malformed response, blocked tool, missing context, unsupported claim, expired approval, or failed postcheck depending on the episode.

### Evidence review
Inspect what AVI recorded and why that matters.

### Boundary
State exactly what AVI still cannot do.

### Next layer
Preview the next episode as the next trust problem, not simply another feature.

## Blog Flow

Blogs should go deeper on the engineering principle behind an episode instead of transcribing the video.

Suggested structure:

- operational problem
- engineering concept
- NetOps example
- architecture or flow
- failure modes
- implementation choices
- where AVI applies the concept
- what to validate before production

## Repository Flow

The repository is the implementation source. Videos should reference reproducible commands and files from the matching episode folder. Reusable logic should progressively move into `avi_core/` rather than being copied between episodes.

## Content Spine

```text
Book concepts
    -> Blog explains the architecture
        -> AVI repo implements it
            -> YouTube demonstrates it
                -> Later episodes build on the evidence
```

The recurring question for the entire series is:

> How do we build an AI network assistant that we can actually trust?
