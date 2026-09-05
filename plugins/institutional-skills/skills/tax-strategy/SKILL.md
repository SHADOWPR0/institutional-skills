---
name: tax-strategy
description: Tax strategy and operations workflow for internal finance teams and downstream user planning support across direct tax, indirect tax, entity-level planning, transaction tax impacts, and tax governance controls.
---

Public distribution: resolve `{SKILLS_ROOT}` to this plugin's `skills/` directory. Recipient bindings and tool availability are explicit; read [portability](../../PORTABILITY.md). No host, CRM, sending, or trading access is implied.

# Tax Strategy

## Quick Reference

### What It Does
- Tax strategy and operations workflow for internal finance teams and downstream user planning support across direct tax, indirect tax, entity-level planning, transaction tax impacts, and tax governance controls.

### Entrypoints
- Follow the workflow in this SKILL.md.

### Inputs / Outputs
- Inputs: Task request plus any files/resources referenced by this skill.
- Outputs: Concrete artifacts or decisions produced by running this skill workflow.

### Dependencies / Tooling
- none beyond workspace defaults

### Test Command(s)

From this skill directory, run the portable consumer suite:

```bash
python3 -B -m unittest discover -s ../../../../tests
```

### Invariants
- Keep existing behavior and command interfaces backward compatible.
- Do not remove or rename scripts/references without a compatibility shim.
- Prefer mechanical edits; avoid stylistic rewrites.

## Overview

Use this skill to run tax-aware decision support with operational discipline, documentation, and escalation to licensed tax professionals for final treatment.

## Modes

- Internal mode
  - finance/tax operations, close-cycle support, planning scenarios, audit readiness.
- Downstream user mode
  - educational planning support, structured tax-impact comparisons, and action checklists.

## Trigger Conditions

Use when a request involves:

- tax-impact analysis for investments, transactions, or distributions
- entity-level tax planning and filing-cycle coordination
- indirect tax obligations and nexus checkpoints
- cross-border or multi-jurisdiction coordination issues
- audit or controversy readiness workflows
- tax control design and documentation quality

## Doctrine

- document assumptions and data sources
- separate tax facts from interpretive judgments
- optimize after compliance baseline is secured
- escalate uncertain positions before execution

## Workflow

1. Classify request (internal vs downstream mode).
2. Gather facts and data quality checks.
3. Route tax lanes (direct, indirect, international, controversy, controls).
4. Build scenario comparisons and sensitivity ranges.
5. Produce recommendation + compliance checklist + escalation notes.
6. Log outcomes and maintain tax assumption registry.

## Sub-Agent Lanes

- Direct Tax Planning Lead
- Indirect Tax and Nexus Lead
- International Tax Coordination Lead
- Transaction Tax Impact Lead
- Tax Controversy and Audit Lead
- Tax Data and Controls Lead

## Output Contract

- tax issue summary and scope
- scenario analysis table (base/upside/downside)
- recommended path with controls and deadlines
- escalation list for licensed tax review

## Boundaries

- This skill is tax workflow support, not a substitute for licensed tax advice.
- Final filing positions and legal interpretations require qualified professionals.

## References

- `references/tax-ops-lifecycle.md`
- `references/direct-tax-planning-framework.md`
- `references/indirect-tax-and-nexus-framework.md`
- `references/international-tax-coordination.md`
- `references/transaction-tax-impact.md`
- `references/tax-controversy-and-audit-response.md`
- `references/tax-data-controls-and-governance.md`
- `references/tax-formulas-and-metrics.md`
- `references/aba-training-placeholder.md`