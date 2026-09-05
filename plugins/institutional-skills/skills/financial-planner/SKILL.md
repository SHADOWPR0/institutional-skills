---
name: financial-planner
description: Comprehensive financial planning operating system across cash flow, risk management, investments, taxes, retirement, estate basics, education planning, and client-behavior coaching. Use for household and small-business planning workflows, policy design, and plan monitoring.
---

Public distribution: resolve `{SKILLS_ROOT}` to this plugin's `skills/` directory. Recipient bindings and tool availability are explicit; read [portability](../../PORTABILITY.md). No host, CRM, sending, or trading access is implied.

# Financial Planner

## Quick Reference

### What It Does
- Comprehensive financial planning operating system across cash flow, risk management, investments, taxes, retirement, estate basics, education planning, and client-behavior coaching. Use for household and small-business planning workflows, policy design, and plan monitoring.

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

Use this skill to run end-to-end financial planning engagements with disciplined assumptions, documented recommendations, and ongoing monitoring.

## Trigger Conditions

Use when a request involves:

- client discovery and goals-based planning
- cash-flow and balance-sheet planning
- debt strategy and liquidity buffer design
- insurance/risk protection analysis
- investment policy and portfolio fit analysis
- tax-aware planning decisions
- retirement income and decumulation strategy
- estate and beneficiary coordination planning

## Planning Doctrine

- goals first, products second
- stress-test assumptions before recommendation
- tax and liquidity awareness in every decision
- align behavior plan to client risk capacity and risk tolerance
- convert advice into measurable implementation tasks

## Workflow

1. Discovery and data quality check.
2. Baseline diagnostics (cash flow, net worth, risk gaps).
3. Goal hierarchy and constraints mapping.
4. Strategy design across planning domains.
5. Prioritized action roadmap with owners and deadlines.
6. Monitoring cadence with trigger-based plan updates.

## Sub-Agent Lanes

- Client Discovery and Data Quality Lead
- Cash Flow and Debt Planning Lead
- Insurance and Risk Protection Lead
- Investment Planning Lead
- Tax Planning Coordination Lead
- Retirement Planning Lead
- Estate and Beneficiary Coordination Lead
- Behavioral Coaching and Implementation Lead

## Output Contract

- planning snapshot (current state)
- strategy memo by domain
- 90-day implementation plan
- annual review and trigger framework

## Boundaries

- This skill supports analysis and planning workflow; regulated legal/tax/investment advice must be finalized by licensed professionals where required.

## References

- `references/cfp-competency-map.md`
- `references/client-discovery-framework.md`
- `references/cash-flow-and-balance-sheet-planning.md`
- `references/debt-and-liquidity-planning.md`
- `references/insurance-planning.md`
- `references/investment-planning.md`
- `references/tax-planning-coordination.md`
- `references/retirement-planning.md`
- `references/estate-and-beneficiary-planning.md`
- `references/planning-formulas-and-ratios.md`
- `references/behavioral-coaching-and-governance.md`
- `references/plan-documentation-templates.md`