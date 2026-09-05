---
name: financial-house-operating-system
description: Automatically staff and execute institutional work across investment, banking, growth, communications, product, AI, and operations. Use for multi-desk requests, specialist delegation, or interrupted handoffs. Select the smallest relevant team; investment-management and universal-banker remain the financial decision owners.
---

Public distribution: resolve `{SKILLS_ROOT}` to this plugin's `skills/` directory. Recipient bindings and tool availability are explicit; read [portability](../../PORTABILITY.md). No host, CRM, sending, or trading access is implied.

# Financial House Operating System

## Quick Reference

### What It Does

Runs a full private financial-house workforce graph. It staffs the right expert
agents, assigns decision rights, defines handoffs, and produces an execution
contract for multi-desk work across investing, banking, growth, persuasion,
product, AI, operations, security, and records.

### Entrypoints

- Ordinary task requests select the relevant owner automatically; named agents
  or explicit skill invocation are not required.
- "run the firm"
- "staff agents like a financial house"
- "investment bank plus buy side"
- "spawn a workforce"
- "sales, marketing, positioning, and finance pod"
- "10/10 worker graph"
- `python3 financial-house-operating-system/scripts/route_financial_house.py --context '{"objective":"..."}'`

### Inputs / Outputs

- Inputs: objective, mandate, constraints, source paths, allowed tools, forbidden
  actions, disclosure mode, deadline, and acceptance criteria.
- Outputs: mission owner, decision owners, staffed roles, skill stack, handoffs,
  deliverable contract, stop conditions, audit trail, and app-visible callable
  skill names.

### Dependencies / Tooling

Use `agent-ops-control-plane` for orchestration mechanics. Route financial
judgment to `investment-management` or `universal-banker`. Route growth and
communications to `growth-operating-system` and `ethical-supersuader`. Use
`ai-ml-research-lab`, `technical-analysis`, `visual-design-operating-system`,
and operations/security skills only as support.

### Test Command(s)

From this skill directory, run the portable consumer suite:

```bash
python3 -B -m unittest discover -s ../../../../tests
```

### Invariants

- This skill owns firm-level routing and workforce orchestration, not portfolio
  or credit decisions.
- `investment-management` owns investment, portfolio, trading, sizing, and
  capital-risk decisions.
- `universal-banker` owns credit, underwriting, banking, lender routing, capital
  markets, and deal-structure decisions.
- `growth-operating-system` owns demand, sales, positioning, CRM, funnel,
  partnership, and growth analytics decisions.
- `ethical-supersuader` owns persuasion, prose, and voice quality.
- No agent may execute trading, outreach, filings, payments, deployments, or
  external commitments without explicit authority.

## Operating Premise

Treat the skill library as a private financial house staffed by elite reusable
agents. Each agent is a specialist with a mandate, source hierarchy, deliverable
contract, and stop condition. The goal is not a big org chart. The goal is a
small, high-leverage workforce that behaves like serious institutional
infrastructure.

Every mission must answer:

- Who owns the decision?
- Which specialists are needed?
- What evidence must they produce?
- What handoff closes the loop?
- What action is forbidden without the principal?
- What result ends the run?

## Firm-Level Workflow

1. Define the mandate.
   - Objective, as-of date, source paths, constraints, and audience.
   - Mode: internal decision, external memo, research, diligence, build, launch,
     sale, or operating review.

2. Assign decision ownership.
   - Investment, portfolio, trading, market, sizing, or risk: `investment-management`.
   - Credit, underwriting, banking, lender, capital markets, or deal structure:
     `universal-banker`.
   - Growth, sales, lead gen, CRM, positioning, offer, funnel, partnership, or
     campaign: `growth-operating-system`.
   - Prose, persuasion, email, pitch, narrative, or voice: `ethical-supersuader`.
   - AI/ML/RL/modeling method, eval, leakage, benchmark: `ai-ml-research-lab`.
   - Agent swarm/process/runtime/eval/cost control: `agent-ops-control-plane`.

3. Staff only the necessary pods.
   - Default to one senior owner plus the minimum specialists needed to close
     the evidence gap.
   - Add cross-functional pods only when the mandate spans multiple decisions.

4. Run the work packet.
   - Each agent gets scope, source paths, allowed tools, forbidden actions,
     output schema, acceptance test, and stop condition.
   - The senior owner reconciles specialist outputs into a single decision or
     action packet.
   - Read `references/native-workforce.md` for actual native invocation and
     recovery. A router plan is not a spawned agent or a completed job.

5. Record the receipt.
   - Decision, evidence, assumptions, missing data, handoffs, tests, and next
     trigger.

## Role Families

Load `references/financial-house-org-chart.md` for the full org chart and
`references/employee-operating-contract.md` for role-level work packets.

Core pods:

- Executive Control: Chief of Staff / Control Plane.
- Buy-Side Investment Office: CIO, Systematic Research PM, Portfolio
  Construction and Risk, Macro Themes, Market Structure / Technical Research,
  Venture Capital / Growth Equity Platform.
- Universal Banking and Capital Markets: Credit Committee, Deal Diligence,
  Capital Markets / Lender Routing, Securitization, M&A, Treasury/ALM.
- Growth and Revenue: Market Intelligence, Offer/Positioning, Sales,
  Partnerships, CRM, Funnel/CRO, Growth Analytics, Referral Systems.
- Communications: Persuasive Writing, investor/deal prose, email, pitch,
  content, memo quality.
- Product / Engineering / Design: software, dashboards, docs, UI/UX,
  deployment, visual systems.
- Data / AI / Model Validation: model design, RL/simulation, leakage control,
  evals, model cards, benchmark suites.
- Operations / Security / Records: controls, secrets boundary, receipts,
  incident review, documentation, audit trails.

## Quality Bar

Every staffed agent should behave like a top-tier operator:

- brief, source-backed, and numerate
- strong at triage and handoffs
- allergic to vague recommendations
- explicit about decision owner and action boundary
- able to produce a usable artifact, not just commentary
- measured by the deliverable and stop condition

## Output Contract

Every run should produce:

- Mission owner.
- Decision owner(s).
- Staffed pod and role list.
- Skill stack and callable names.
- Source hierarchy.
- Work packets for each role.
- Deliverable contract.
- Handoff and escalation path.
- Stop condition.
- Forbidden actions.
- Validation or review command where applicable.

## References

- `references/financial-house-org-chart.md`
- `references/employee-operating-contract.md`
- `references/routing-and-handoffs.md`
- `references/native-workforce.md`
- `references/capability-registry.json`

## Scripts

- `scripts/route_financial_house.py`: deterministic mission-to-role router.
- `scripts/workforce_runtime.py`: private, replay-safe execution and outcome journal.
