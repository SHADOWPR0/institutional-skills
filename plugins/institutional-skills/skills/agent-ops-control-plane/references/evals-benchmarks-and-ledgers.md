# Evals, Benchmarks, And Ledgers

## Lightweight Engineering Gates

Use these gates when a task has ambiguity, code changes, cross-system risk, or durable skill impact. They adapt the useful parts of public engineering-methodology skill packs without importing their global mandates.

- Brainstorm first when the requested outcome is unclear, high-leverage, or easy to overbuild.
- Write a small plan before nontrivial edits: target files, expected behavior, tests, and rollback.
- Use test-first development when changing behavior and a focused test can be written cheaply.
- Keep implementation scoped to the smallest patch that satisfies the plan.
- Run a review pass after the change: regressions, missing tests, hidden side effects, path risk, and user-owned files.
- Finish with evidence: commands run, files changed, known gaps, and what was intentionally not changed.

These gates are not theater. Skip or compress them for tiny tasks where they add no value, and tighten them for protected systems, automations, money flows, outreach, or production code.

## Eval-Driven Agent Development

Build the eval before claiming improvement.

Minimum eval spec:

- target behavior
- task set
- baseline
- scoring method
- pass threshold
- failure taxonomy
- cost and latency capture
- regression guard
- owner approval for promotion

Use deterministic checks first. Add model-graded rubrics only when judgment is genuinely required.

## Eval Types

- `CAPABILITY`: Can the agent perform the intended task?
- `REGRESSION`: Did the new skill preserve old behavior?
- `ROUTING`: Did the correct domain owner and support skills trigger?
- `SAFETY`: Did the agent avoid forbidden actions and unsafe claims?
- `COST`: Did the workflow improve quality per unit cost/time?
- `ROBUSTNESS`: Does performance hold across adversarial, stale, missing, or noisy inputs?

## Pass@K And Success-Per-Cost

For agent workflows where multiple attempts are allowed, report:

- pass@1
- pass@k
- best-of-k cost
- median latency
- failure cluster
- marginal gain from additional attempts

Do not let pass@k hide a weak first attempt. A robust production agent should improve both first-pass quality and recovery quality.

## Worktree-Isolated Benchmarking

For code or skill refactors, isolate competing variants:

1. Create a clean branch or worktree per variant.
2. Apply only the intended change.
3. Run identical evals.
4. Compare quality, regressions, cost, and maintenance burden.
5. Promote only the smallest variant that wins out of sample.

## Recursive Decision Ledger

Use a ledger for repeated rollouts, trading systems, campaigns, automations, or skill upgrades.

Ledger fields:

- date
- hypothesis
- change
- owner
- task class
- baseline
- expected improvement
- observed result
- failures
- patch
- retest result
- promote / iterate / retire

The ledger should reward compounding process improvements and expose repeated mistakes quickly.

## Agent Scorecard

For recurring agents, track:

- task volume
- first-pass acceptance rate
- correction rate
- blocked rate
- unsafe-action avoidance
- false-positive escalations
- cost per accepted output
- latency to useful answer
- memory quality
- owner satisfaction notes

Promote to always-on only when the agent has sustained utility, low false-positive overhead, and clear ownership.
