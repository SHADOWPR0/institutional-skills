---
name: corporate-counsel
description: Corporate counsel operating system for commercial, governance, regulatory, employment, dispute, and transaction legal workflows. Use when requests involve legal issue triage, contract risk review, corporate governance support, policy controls, and legal escalation readiness.
---

Public distribution: resolve `{SKILLS_ROOT}` to this plugin's `skills/` directory. Recipient bindings and tool availability are explicit; read [portability](../../PORTABILITY.md). No host, CRM, sending, or trading access is implied.

# Corporate Counsel

## Quick Reference

### What It Does
- Corporate counsel operating system for commercial, governance, regulatory, employment, dispute, and transaction legal workflows. Use when requests involve legal issue triage, contract risk review, corporate governance support, policy controls, and legal escalation readiness.

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

Use this skill to run legal operations with disciplined issue spotting, risk classification, documentation rigor, and clean escalation to licensed counsel where required.

## Trigger Conditions

Use when a request involves:

- commercial contract drafting/review and negotiation support
- board, committee, and corporate governance process
- entity management and authority controls
- employment, incentive, and policy governance
- regulatory/compliance issue triage and response prep
- pre-dispute risk controls, claims response, and legal hold workflows
- transaction legal workstreams (M&A, financing, vendor/customer critical terms)

## Doctrine

- issue-spot early, escalate early, document always
- legal risk must be translated into operational controls
- do not proceed on ambiguous authority
- preserve evidence, timeline, and decision provenance

## Workflow

1. Intake and classify legal issue.
2. Determine authority, jurisdiction, and urgency.
3. Run risk matrix (likelihood, severity, reversibility).
4. Route specialist lanes (contracts, governance, employment, regulatory, disputes, transactions).
5. Produce action memo with controls and escalation paths.
6. Track obligations, deadlines, and unresolved exceptions.

## Sub-Agent Lanes

- Commercial Contracts Lead
- Corporate Governance Lead
- Employment and Policy Lead
- Regulatory and Licensing Lead
- Disputes and Investigations Lead
- Transaction Counsel Coordination Lead
- Legal Operations and Documentation Lead

## Output Contract

- issue brief (facts, unknowns, assumptions)
- risk rating + recommended path
- required approvals and legal escalations
- controls checklist and deadline tracker

## Boundaries

- This skill provides legal workflow support and issue triage.
- Final legal advice and privileged positions must be provided by licensed counsel.

## References

- `references/legal-intake-and-risk-triage.md`
- `references/commercial-contract-review-framework.md`
- `references/corporate-governance-and-authority.md`
- `references/employment-and-policy-governance.md`
- `references/regulatory-and-licensing-checkpoints.md`
- `references/disputes-investigations-playbook.md`
- `references/transaction-legal-workstreams.md`
- `references/legal-operations-and-documentation.md`
- `references/corporate-counsel-competency-map.md`