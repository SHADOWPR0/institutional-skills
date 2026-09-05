# Context Budget And Retrieval

## Principle

The context window is an operating budget. Treat always-loaded instructions as fixed cost, skill bodies as variable cost, and reference files as on-demand inventory.

## Context Budget Audit

Classify every instruction source as:

- `ALWAYS`: needed in nearly every run and short enough to justify permanent exposure.
- `ROUTE`: needed only when a named skill or task lane triggers.
- `REFERENCE`: detailed material loaded only after the skill triggers.
- `ARCHIVE`: provenance, not active operating instructions.
- `REMOVE_FROM_ROUTE`: duplicate, stale, conflicting, or too broad for active use.

Audit questions:

- Does this instruction change behavior in the current task?
- Is the same rule already present in the system, global AGENTS file, or domain skill?
- Can this be moved from `SKILL.md` into `references/`?
- Can a script replace repeated generated code?
- Does the description over-trigger unrelated tasks?

## Iterative Retrieval Loop

Use staged retrieval when the answer depends on broad local context.

1. Dispatch.
   - Define the target artifact.
   - Name likely sources and false-positive sources.
   - Set a maximum retrieval depth.

2. Retrieve.
   - Search names, metadata, and headings first.
   - Open the smallest matching files.
   - Summarize findings before loading more.

3. Evaluate.
   - Identify what is known, missing, stale, or contradictory.
   - Decide whether another retrieval pass is worth its context cost.

4. Refine.
   - Narrow the query.
   - Load only the next best files.
   - Stop after three passes unless the user explicitly wants exhaustive inventory.

## Search-First Rule

Before creating a new abstraction, search for existing local patterns:

- `rg --files` for candidate files
- `rg` for symbols, phrases, and frontmatter names
- existing scripts before new scripts
- existing reference docs before new long-form instructions

Only build new material when reuse would be more confusing than creation.

## Parallel Lane Matrix

Use parallel lanes when work is independent and mergeable:

| Lane | Good For | Avoid When |
| --- | --- | --- |
| Discovery | inventory, source mapping, benchmark search | source set is tiny |
| Implementation | scoped file changes, scripts, templates | requirements are still unresolved |
| Evaluation | tests, audits, scorecards, diffs | no acceptance criteria exists |
| Governance | risks, permissions, kill switches | purely local trivial work |

Merge rule: one owner reconciles outputs into a single recommendation. Parallel agents do not each produce final strategy.

## Context Bloat Tripwires

Trigger a cleanup if:

- a `SKILL.md` exceeds 500 lines without a clear reason
- multiple skills have the same trigger phrase
- a support skill starts claiming domain ownership
- the same reference framework appears in three active skills
- global routing includes detailed operational doctrine better suited to a skill reference
