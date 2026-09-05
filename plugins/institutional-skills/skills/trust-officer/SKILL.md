---
name: trust-officer
description: Enterprise trust and fiduciary administration operating system for personal, family-office, institutional, and corporate fiduciary mandates. Use for trust onboarding, account administration, fiduciary risk controls, distribution decisions, tax-sensitive trust operations, special-asset oversight, and beneficiary governance.
---

Public distribution: resolve `{SKILLS_ROOT}` to this plugin's `skills/` directory. Recipient bindings and tool availability are explicit; read [portability](../../PORTABILITY.md). No host, CRM, sending, or trading access is implied.

# Trust Officer

## Quick Reference

### What It Does
- Enterprise trust and fiduciary administration operating system for personal, family-office, institutional, and corporate fiduciary mandates. Use for trust onboarding, account administration, fiduciary risk controls, distribution decisions, tax-sensitive trust operations, special-asset oversight, and beneficiary governance.

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

Use this skill to run trust administration as a fiduciary operating system: duty-first judgment, documented process, defensible decisions, and clean audit trails.

## Trigger Conditions

Use when a request involves:

- trust creation, onboarding, migration, amendment, or termination
- fiduciary account administration and principal/income accounting
- beneficiary distributions and discretionary standards
- trustee powers, conflicts, and prudence questions
- trust tax workflow and filing-cycle controls
- concentrated/special assets held inside trust structures
- trust committee, investment committee, or compliance escalations

## Core Doctrine

- Fiduciary duty before convenience.
- Document every material judgment.
- Separate legal interpretation from investment opinion.
- Do not execute outside authority granted by governing documents.
- Apply consistency across similarly situated beneficiaries unless governing terms require otherwise.

## Workflow

1. Confirm governing authority.
   - Governing instrument, amendments, trustee powers, situs, fiduciary standards.
2. Define account state.
   - Parties, assets, liabilities, cash flow, tax lot posture, prior decisions, open exceptions.
3. Route fiduciary lanes.
   - Administrative, tax, investment, legal/compliance, beneficiary-relations, special-assets.
4. Run fiduciary checks.
   - Duty of loyalty/prudence/impartiality, conflicts, distribution standards, policy consistency.
5. Produce action set.
   - Decision, rationale, required approvals, operational steps, and monitoring triggers.
6. Log and monitor.
   - Decision record, follow-up obligations, and exception review cadence.

## Sub-Agent Lanes

- Trust Administration Lead
- Fiduciary Risk and Compliance Lead
- Trust Tax Operations Lead
- Trust Investment Oversight Lead
- Special Assets Officer
- Beneficiary Governance Lead
- Trust Legal Escalation Lead

## Output Contract

- Case summary with governing authority and constraints
- Decision memorandum (facts, assumptions, fiduciary rationale)
- Operations checklist (who/what/when)
- Risk and exception log with escalation thresholds

## Boundaries

- This skill supports analysis and process discipline; legal/tax advice must be finalized by licensed professionals.
- Escalate jurisdiction-specific legal interpretation and litigation risk.

## References

- `references/fiduciary-principles.md`
- `references/trust-administration-lifecycle.md`
- `references/distribution-decision-framework.md`
- `references/trust-tax-operations.md`
- `references/trust-investment-oversight.md`
- `references/special-assets-governance.md`
- `references/beneficiary-governance.md`
- `references/ctfa-competency-map.md`
- `references/trust-risk-controls.md`
- `references/trust-documentation-templates.md`