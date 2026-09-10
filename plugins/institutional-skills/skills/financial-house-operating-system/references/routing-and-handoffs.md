# Routing and Handoffs

## Master Decision Owners

`investment-management` owns:

- investment research
- public/private portfolio decisions
- trading, sizing, risk budgets, regime, market making
- quant, AI finance, technical-analysis-supported market decisions
- venture capital, growth equity, follow-ons, reserves, secondaries, and founder/platform value creation

`universal-banker` owns:

- credit
- underwriting
- lender routing
- capital markets
- securitization
- deal structure
- M&A and corporate advisory
- venture debt, structured facilities, covenants, lender packages, and transaction process for venture-backed companies

## Business Growth Owners

`growth-operating-system` owns:

- market intelligence
- ICP and segmentation
- offer and positioning
- sales and CRM
- lead generation and funnel/CRO
- referral, partnership, and lifecycle growth

`ethical-supersuader` owns:

- persuasive writing
- email and pitch quality
- investor/deal prose
- voice, brevity, and anti-generic style

## Support Owners

- `ai-ml-research-lab`: model/eval/research method support.
- `technical-analysis`: technical evidence only; no capital decision.
- `visual-design-operating-system`: presentation and design.
- `agent-ops-control-plane`: multi-agent orchestration, tests, context budgets,
  runtime governance, and receipts.
- `corporate-counsel`, `tax-strategy`, `trust-officer`, and
  `financial-planner`: support within professional boundaries.

## Cross-Functional Handoff Patterns

### Routine Office Work

Use existing employees, not a separate office-manager skill. The Chief of Staff
coordinates cross-domain work; Operations handles records. These workflows are
capabilities in the same registry and org graph, not competing skill front doors.

| Request | Existing employee and owner | Required result |
|---|---|---|
| Financing follow-up coordination | Growth + Communications; Universal Banker for financing facts | Reconcile prior touches, requested documents, owner and next step; draft only when requested. Keep quoted terms, oral reports and assumptions separate. |
| Meeting follow-up capture | Operations / Records; add the relationship owner only for actual relationship updates | Extract sourced decisions, actions, owners, due dates and unresolved questions. Use unavailable for absent dates/owners, not invented commitments. |
| Lead intake | Growth; Universal Banker only for credit/borrower analysis; relationship system owns identity and eligibility | Preserve source, resolve aliases through the existing relationship system, stage the intake and missing-data list. A lead is not marketing consent or an approved borrower. |
| Deal package staging | Deal Diligence under Universal Banker | Inventory versions and missing items, reconcile discrepancies, retain originals, enforce teaser/full-package and recipient boundaries. No implied approval or submission. |
| Event design package | Product / Design under Visual Design Operating System | Apply the cross-medium brief, preserve source photos and accepted masters, produce only requested formats, inspect every exported page/frame. No vendor booking or sharing by inference. |

For relationship changes, use the existing `relationship_update.v1` handoff;
only its owner receipt establishes committed state. For other records, use the
owning project's current task/action store. Do not create a parallel CRM, meeting
database, folder hierarchy or recurring worker. Load prose, documents, slides,
image/video or other execution support only when the requested output needs it.

Computer History suggestions nominate reusable patterns; they are not installed
skills, user instructions, proof of completion or authority to act. Read only
relevant available evidence through supported history tools. Keep raw history,
personal content and source pointers private and at source. On the existing
Skill Intelligence cycle, match an observed pattern to this registry first,
patch a demonstrated routing/reference gap, test it, and publish through the
normal release process. A redundant suggestion needs no package or notification.
Do not change observation settings to suppress suggestions. A host UI card can
remain visible even after its workflow is covered; do not claim it was hidden.

Use existing authenticated connectors or CLI routes for repository operations.
A browser's private-repository sign-in page does not invalidate an authorized
MCP or Git session. Do not start another login, extract credentials, or change
auth configuration when the task can use a working authorized route. Report a
real authorization failure to the existing system owner. Preserve the task's
model selection; this graph is model-neutral.

### Domain Handoffs

Investment thesis to external memo:

1. `investment-management` owns the thesis.
2. `portfolio_construction_risk` tests portfolio fit.
3. `ethical-supersuader` drafts the memo.
4. `visual-design-operating-system` formats if a deck/report is needed.

Venture or growth-equity deal:

1. `investment-management` owns the VC/growth investment memo, reserve decision,
   platform plan, and portfolio fit.
2. `growth-operating-system` supports GTM, ICP, pricing, funnel, partnership,
   and customer evidence.
3. `ai-ml-research-lab` supports technical/model diligence for AI, ML, data, and
   infrastructure companies.
4. `universal-banker` owns venture debt, M&A, covenants, lender routing, and
   transaction structuring when those issues appear.

Deal financing:

1. `universal-banker` owns structure and credit view.
2. `deal_underwriting_diligence` builds the diligence packet.
3. `capital_markets_lender_routing` ranks lenders and requirements.
4. `ethical-supersuader` drafts outreach, but no send without approval.

Growth launch:

1. `growth-operating-system` owns market, offer, funnel, and metrics.
2. `ethical-supersuader` writes copy.
3. `visual-design-operating-system` shapes assets.
4. `ai-ml-research-lab` supports causal measurement if needed.

Firm-wide mission:

1. `financial-house-operating-system` assigns the mission owner and pod.
2. Domain owners produce decisions.
3. `agent-ops-control-plane` manages runtime and receipt.
4. Chief of Staff reconciles the final packet for the principal.
