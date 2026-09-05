# Continuous Learning And Memory

## Micro-Pattern Format

Store learned behavior as small, scoped micro-patterns:

- trigger
- context boundary
- behavior
- evidence
- counterexample
- confidence
- source path or task id
- owner
- review date

Prefer one precise lesson over a broad slogan.

## Scope Levels

- `THREAD`: useful in the current conversation only.
- `PROJECT`: useful inside one repo, client, account, or mandate.
- `DOMAIN`: useful across one canonical skill.
- `GLOBAL`: useful across nearly all work.

Most lessons should start as project or domain scope. Global promotion is rare.

## Promotion Gates

Promote a lesson when:

- it has repeated evidence
- it reduces errors or cost
- it has clear boundaries
- it does not conflict with a higher-priority instruction
- it can be written compactly
- it has an owner for future correction

Retire a lesson when it becomes stale, causes false positives, or has better replacement logic.

## Memory Hygiene

- Never store secrets.
- Do not store sensitive personal details unless the user explicitly asks and the storage location is appropriate.
- Record source paths rather than duplicating large private text.
- Mark stale assumptions with dates.
- Separate facts, preferences, and inferred habits.

## Persistent Memory Pattern

Use this pattern when adapting ideas from memory systems such as `claude-mem` into the local recipient organization stack.

- Capture compact session summaries, not raw transcript dumps.
- Attach source ids, file paths, dates, and confidence.
- Store memories by scope: private, project, domain, global.
- Retrieve progressively. Load the smallest memory slice that can answer the current question.
- Keep private exclusions and sensitive-context boundaries explicit.
- Preserve human-readable summaries alongside machine-readable indexes.
- Prefer recipient organization domain files and canonical skill references over hidden background workers.
- Require an owner and review date for anything promoted to durable memory.

Do not install a memory hook, worker, vector index, or background daemon unless the owner, data boundary, rollback path, and kill switch are written down first.

## Skill Self-Improvement Loop

1. Capture repeated friction.
2. Verify it is not a one-off.
3. Find the smallest skill, reference, or script change.
4. Add an eval or audit check if measurable.
5. Sync the canonical source and mirrors.
6. Record what changed and why.

## CASS / Knowledge Graph Use

When a memory or knowledge system is available:

- write only high-signal lessons
- include source references
- tag by domain skill
- keep owner and review cadence visible
- avoid dumping entire transcripts

Memory should make future work sharper, not heavier.
