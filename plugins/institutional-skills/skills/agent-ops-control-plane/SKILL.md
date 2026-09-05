---
name: agent-ops-control-plane
description: Vendor-neutral support skill for agent operations, orchestration, context budgeting, iterative retrieval, eval harnesses, agent benchmarking, continuous learning, model/cost routing, runtime governance, safety gates, kill switches, and recursive decision ledgers across all canonical skills. Use when improving all skills, running agent swarms, auditing context bloat, benchmarking agents, creating pass/fail evals, building feedback loops, or operating long-running agents.
---

Public distribution: resolve `{SKILLS_ROOT}` to this plugin's `skills/` directory. Recipient bindings and tool availability are explicit; read [portability](../../PORTABILITY.md). No host, CRM, sending, or trading access is implied.

# Agent Ops Control Plane

## Quick Reference

### What It Does

Provides the reusable operating layer for agent orchestration, context budgets, iterative retrieval, evals, memory promotion, runtime governance, cost routing, and safe multi-agent handoffs.

### Entrypoints

- agent swarms or handoffs
- context bloat or retrieval plans
- skill-library upgrades
- eval harnesses and agent benchmarks
- durable memory promotion
- long-running agent governance

### Inputs / Outputs

- Inputs: objective, domain owner, source paths, constraints, allowed tools, forbidden actions, budget, acceptance criteria.
- Outputs: operating plan, handoff contract, eval plan, monitoring metrics, kill switch, promotion or rollback rule.

### Dependencies / Tooling

Use local files, `rg`, deterministic tests, repo-native commands, and the references in this package. Domain skills remain decision owners.

### Test Command(s)

From this skill directory, run the portable consumer suite:

```bash
python3 -B -m unittest discover -s ../../../../tests
```

### Invariants

- Do not expose secrets or private account details in logs, memory, evals, or handoffs.
- Do not let an eval alone authorize capital, legal, security, outreach, or deployment actions.
- Do not create hidden autonomous actions.
- Keep global rules lean and push specialized detail into references.

## Role

Use this as the reusable operating layer for agent systems. It is a support skill, not a domain decision owner.

Domain owners stay in charge:

- `investment-management` owns capital allocation, portfolio, trading, and investment-risk judgment.
- `universal-banker` owns banking, underwriting, deal structuring, and capital-markets judgment.
- `growth-operating-system` owns growth, marketing, sales, CRM, funnel, and campaign judgment.
- `ethical-supersuader` owns prose, persuasion, and voice quality.
- `ai-ml-research-lab` owns AI/ML/RL method design and model evaluation.

This skill improves how those skills are routed, budgeted, tested, coordinated, monitored, and recursively upgraded.

## When To Use

Use when the user asks for:

- agent swarms, multi-agent workflows, workstream splits, or handoffs
- context budget, context bloat, retrieval plans, or skill-library compression
- pass/fail evals, benchmark harnesses, pass@k, regression tests, or agent scorecards
- continuous learning, memory promotion, playbook updates, or skill self-improvement
- model routing, cost budgets, runtime metrics, long-running agents, kill switches, or incident reviews
- optimization of all skills, global agent infrastructure, or cross-skill orchestration

## Default Workflow

1. Classify the operating problem.
   - `CONTEXT_BUDGET`: loaded instructions are too large, redundant, or poorly routed.
   - `ITERATIVE_RETRIEVAL`: the agent needs staged discovery instead of one-shot context loading.
   - `ORCHESTRATION`: multiple agents or lanes need clear ownership and handoffs.
   - `EVAL_HARNESS`: behavior needs objective or rubric-based measurement.
   - `CONTINUOUS_LEARNING`: high-signal lessons need scoped memory and promotion gates.
   - `RUNTIME_GOVERNANCE`: long-running work needs observability, costs, permissions, and kill switches.
   - `DECISION_LEDGER`: repeated rollouts need hypothesis, outcome, and patch history.

2. Pick the domain owner before picking agents.
   - If a real-world decision has financial, legal, operational, or reputational consequences, the relevant domain skill owns the recommendation.
   - This skill owns the agent process around that recommendation.

3. Load only the needed reference.
   - Context and retrieval: `references/context-budget-and-retrieval.md`
   - Evals, benchmarks, and ledgers: `references/evals-benchmarks-and-ledgers.md`
   - Continuous learning and memory: `references/continuous-learning-and-memory.md`
   - Runtime governance and cost: `references/runtime-governance-and-cost.md`
   - Bounded review swarms and work packets: `references/review-swarms-and-work-packets.md`
   - Databento acquisition, batch/retry, live recovery, cursor/deduplication,
     immutable cache, and GCS continuity:
     `{SKILLS_ROOT}/_library/docs/DATABENTO_MARKET_DATA_ML_OPERATING_CONTRACT.md` (not bundled; recipient resource required)
   - Exact Databento API, schema, release, and example routing:
     `{SKILLS_ROOT}/_library/docs/DATABENTO_OFFICIAL_DOCS_AND_EXAMPLES_CATALOG.md` (not bundled; recipient resource required)
   - Source provenance: `references/source-map.md`
   - External repo intake decisions: `references/external-skill-intake-2026-06-15.md`, `references/external-repo-intake-2026-06-15.md`, and `references/codex-marketplace-intake-2026-07-16.md`
   - Quant repository capability harvests and adapter evidence: `references/quant-repository-capability-harvest.md`

4. Produce an operating plan.
   - objective
   - domain owner
   - agent lanes
   - context budget
   - retrieval policy
   - eval harness
   - monitoring metrics
   - kill switch
   - audit trail
   - promotion or rollback rule

5. Run the smallest useful loop first.
   - Search and reuse before building.
   - Prefer deterministic checks before model judges.
   - Promote learned behavior only after evidence.
   - Keep global rules lean; put specialized detail in references.

## Non-Negotiables

- Do not expose secrets, credentials, personal contact data, or private account details in memory, logs, eval datasets, or agent handoffs.
- Do not let an eval score authorize a capital, legal, security, outreach, or deployment action by itself.
- Do not globally promote a project-specific lesson until it has repeated evidence and clear boundaries.
- Do not overload a thread with every available skill. Load the smallest useful skill set.
- Do not create hidden autonomous actions. Make owner, scope, and forbidden actions explicit.
- Do not overwrite user work. Use file reservations or explicit scope notes when multiple agents touch files.
- Databento jobs and live sessions must be idempotent and resumable: preserve
  request/job identity, never resubmit merely because polling failed, ledger
  reconnect or slow-reader gaps, and keep downstream decisions `FLAT` until
  continuity is proven.

## Handoff Contract

Every agent handoff should include:

- objective
- domain owner
- assigned workstream
- source paths
- allowed tools
- forbidden actions
- expected output
- acceptance criteria
- budget
- deadline or review point
- kill switch

## Output Patterns

Agent swarm plan:

- Domain owner
- Workstreams
- Context budget
- Source hierarchy
- Handoff contract
- Eval plan
- Monitoring and kill switches

Skill upgrade plan:

- Current trigger surface
- Redundancy and context-bloat risks
- Reusable references
- Router changes
- Eval harness
- Memory-promotion rule
- Sync/deployment steps

Incident or failed-run review:

- Intended objective
- Actual outcome
- Failure mode
- Broken assumption
- Cost/time spent
- Patch
- Retest
- Promote / iterate / retire

## Scripts

- `scripts/agent_ops_audit.py` (not bundled; recipient resource required): audit local skill packages for frontmatter, duplicate skill names, large `SKILL.md` files, and context-bloat candidates.
- `scripts/validate_quant_repository_harvest.py`: fail-closed validation for external quant-repository and adapter evaluation records.
