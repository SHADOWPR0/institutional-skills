# Review Swarms And Work Packets

Use this reference for broad code review, bug hunts, large but separable refactors, and independent verification. Do not spawn multiple agents when one focused pass is cheaper and sufficient.

## When A Review Swarm Is Worth It

Use independent reviewers when at least two of these are true:

- the change crosses modules or ownership boundaries;
- failure could affect money, security, privacy, production, or stored data;
- the diff is too large for one reliable pass;
- the work needs distinct expertise;
- the first reviewer could anchor later judgment;
- reproducible evidence matters more than speed.

Keep the swarm small. Three orthogonal reviewers usually beat ten overlapping ones.

## Work Packet

Every delegated packet must include:

```text
Objective:
Domain owner:
Scope:
Owned files:
Read-only context:
Must-read sources:
Allowed tools:
Forbidden actions:
Required commands:
Evidence format:
Output path or return contract:
Acceptance tests:
Stop conditions:
Budget or review point:
```

No agent receives implicit authority to edit outside `Owned files`. Reviewers are read-only unless the packet says otherwise.

## Orthogonal Review Roles

Choose only the roles the change needs:

- `CORRECTNESS`: behavioral bugs, edge cases, state transitions, data loss.
- `SECURITY_PRIVACY`: trust boundaries, secret exposure, injection, permissions, unsafe defaults.
- `TESTS`: missing coverage, weak assertions, false-positive tests, untested failure paths.
- `SIMPLIFICATION`: unnecessary complexity in the touched diff, dead branches, duplicated logic.
- `PERFORMANCE`: measured hotspots, blocking work, query or rendering regressions.
- `DOMAIN`: finance, banking, ML, growth, or other domain-specific contract failures.
- `REPRODUCTION`: reproduce a suspected bug and preserve exact steps, inputs, output, and environment.

Agents should not all review "everything." Give each a separate failure model.

## Finding Contract

Every finding must contain:

- severity;
- file and line or artifact anchor;
- observed behavior;
- expected behavior;
- reproduction or reasoning chain;
- user or system impact;
- smallest viable correction;
- confidence and what would falsify it.

Reject style preferences presented as bugs. Reject unsupported findings. Merge duplicates before presenting results.

## Coordinator Pass

The coordinator:

1. validates each finding against source or reproduction evidence;
2. deduplicates findings by root cause, not wording;
3. resolves conflicts or marks them unresolved;
4. orders verified findings by severity and impact;
5. assigns corrections to non-overlapping file owners;
6. runs the full verification suite after integration;
7. records what was intentionally left unchanged.

## Simplification Boundary

Simplification reviewers inspect the touched behavior and immediate dependencies. They must not use a review as permission for unrelated refactors, dependency swaps, style migrations, or repository cleanup.

## Provenance

This reference distills MIT-licensed work-packet, batch-refactor, bug-hunt, simplification, and review-swarm patterns from `Dimillian/Skills`, inspected at commit `05ba982bfeb0d77d3c97d4542b0ee15034d05f84` on 2026-07-16. It preserves the local control plane as the sole orchestration owner.
