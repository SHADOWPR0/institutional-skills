# Financial House Org Chart

This chart is the reusable agent workforce model for the principal's private financial
house. It is a routing graph, not a personnel fantasy. Use the smallest useful
team.

## Canonical Capability Registry

`references/capability-registry.json` owns capability and execution-profile
metadata. The router imports its 14 profiles through `execution_roles`; the
profile IDs and `Role` fields remain stable for workforce-runtime consumers.
The org descriptions below explain mandates. They do not create extra agents.

The registry retains the source contracts for 38 investment desk families,
11 sectors, 10 regions, 19 investment roles, and 20 banker specialists. Each
capability names its owner, execution profile, skills, references, tools,
deliverable, and routing keywords. Desk subfunctions, sector coverage, regional
coverage, and banker lane fields remain attached under `details`.

`resource_ownership` maps all 51 canonical packages from the institutional
manifest. Both financial masters have enumerated resource paths, including
scripts, formulas, playbooks, tests, and preserved archives: 114 resources in
`investment-management` and 34 in `universal-banker`. Availability does not
load these resources into every packet. Archived packages remain provenance;
their active replacements own decisions.

| Execution profile | Functions carried by the profile |
|---|---|
| `chief_of_staff` | mandate, staffing, cross-domain reconciliation |
| `cio` | investment judgment, discretionary desks, research synthesis |
| `systematic_research_pm` | causal research, data engineering, systematic desks |
| `portfolio_risk` | sizing, portfolio construction, central risk, attribution |
| `market_structure` | macro research or technical evidence, selected separately |
| `venture_platform` | venture, growth equity, reserves, founder platform |
| `credit_committee` | credit judgment, treasury, insurance, enterprise risk |
| `deal_diligence` | underwriting, M&A/LBO, models, fiduciary/legal/tax support |
| `capital_markets` | capital routes, issuance, distribution, syndication |
| `growth` | qualified demand, CRM, referrals, partnership execution packets |
| `communications` | writing, source-bounded claims, prose review |
| `product_design` | software, product, design, artifact verification |
| `ai_validation` | AI/ML methods, leakage, calibration, evaluation |
| `ops_security` | records, controls, security, operational evidence |

Routine office work is part of these employees, not a new package: Growth owns
lead intake and follow-up coordination, Operations captures meeting actions,
Deal Diligence stages transaction packages, and Product / Design produces event
design. See [the workflow contracts](routing-and-handoffs.md#routine-office-work).
The Chief of Staff coordinates only when the request spans decision domains.

Each execution profile retains the prior institutional roster's skill and tool
coverage in `skills`, `tools`, and `source_contracts`. `default_skills` defines
the smaller starting stack used by the router. Fiduciary, counsel, tax, and
planning functions remain available through `deal_diligence`; they do not
create a third financial master.

The financial decision owners remain `investment-management` and
`universal-banker`. Sector and regional lenses enrich the selected owner's
packet. A mortgage lead list can need banker evidence without needing the
whole underwriting and capital-markets team.

## Route Packets

`build_route(context)` preserves the existing output keys and adds
`capability_ids`, `capabilities`, `resource_refs`, and `external_handoffs`.
Every returned role references a registry profile and its selected functions.
Use `capability_ids` in the input for an explicit function selection; unknown
IDs fail rather than silently selecting another function.

Natural-language classification uses word boundaries for every keyword length.
It reads request fields, not forbidden actions, source paths, budgets, or model
metadata. Numerical financial models route to banking, while explicit AI/ML
methods route to model validation. Macro and technical packets load their
respective child skill without loading the other by default.

Routes report `planned_not_invoked`. The workforce runtime owns invocation,
receipt validation, owner acceptance, and observed outcomes.

## Relationship OS Handoff

Ordinary CRM and lead-generation requests use `growth` and `communications`.
Finance evidence adds `credit_committee` when required; transaction execution
planning can also require `deal_diligence` or `capital_markets`.

recipient-crm remains the external identity, suppression, provenance,
eligibility, and factual-dossier owner. The registry stores its existing owner
task and `relationship_update.v1` handoff contract. Consumer work stages the
packet with source paths, hashes, timestamps, aliases, and field provenance.
Only the external owner's receipt establishes committed state. No route creates
a second CRM skill, clears suppression, grants eligibility, or sends outreach.

## Routing Evidence

`tests/test_capability_routing.py --receipt` (not bundled; recipient resource required) returns the captured original
outputs and freshly computed routes for 20 raw requests. Exact staffing matches
in this regression matrix improved from 3/20 to 20/20; selected profile
assignments fell from 61 to 39. These are deterministic routing results, not
agent-invocation or task-quality scores.

The tests compare the registry against the masters' actual desk tables,
investment role contracts, banker lane definitions, and resource inventories.
They also exercise every capability ID, profile references, macro/TA separation,
CRM ownership, financial models, sector/region lenses, software, and writing.

## Command Chain

the principal -> Chief of Staff / Control Plane -> decision owner -> specialist pod ->
validated handoff -> receipt.

## Executive Control

### Chief of Staff / Control Plane

- Skill stack: `financial-house-operating-system`, `agent-ops-control-plane`.
- Mandate: translate the principal's objective into a bounded mission, assign the
  decision owner, staff specialists, manage handoffs, and stop when the
  deliverable is complete.
- Decision rights: routing, staffing, budget, acceptance contract.
- No authority: capital allocation, credit approval, external commitments.

## Buy-Side Investment Office

### CIO / Investment Committee

- Skill stack: `investment-management`.
- Mandate: own capital allocation, portfolio, market, trading, sizing, and
  investment-risk decisions.
- Output: source-backed decision memo with risk limits, benchmark, invalidation,
  and action boundary.

### Systematic Research PM

- Skill stack: `investment-management`, `ai-ml-research-lab`.
- Mandate: design causal research, test models, maintain reproducibility, and
  separate research from production.
- Output: research packet with data lineage, net economics, folds, tests, and
  promote/iterate/kill state.

### Portfolio Construction and Risk

- Skill stack: `investment-management`.
- Mandate: size risk, test factor/correlation/liquidity exposure, and define
  rollback triggers.
- Output: risk budget, concentration map, stress result, and review trigger.

### Macro Themes and Market Structure

- Skill stack: `global-macro-theme-picker`, `technical-analysis`,
  `investment-management`.
- Mandate: produce theme-level and market-structure evidence. No independent
  allocation authority.
- Output: evidence packet or unavailable-data flag.

### Venture Capital / Growth Equity Platform

- Skill stack: `investment-management`, `growth-operating-system`,
  `ai-ml-research-lab`, `ethical-supersuader`; add `universal-banker` only for
  debt, M&A, covenants, lender routing, or deal-structure work.
- Mandate: own venture investing, growth-equity diligence, founder/platform
  support, portfolio reserves, follow-on logic, secondaries, and company-building
  value creation.
- Output: VC investment memo, follow-on/reserve decision, platform support plan,
  or `BANKER_HANDOFF` when financing or transaction structure controls the
  decision.

## Universal Banking and Capital Markets

### Universal Banker / Credit Committee

- Skill stack: `universal-banker`.
- Mandate: own credit, underwriting, banking, lender routing, capital markets,
  and deal-structure decisions.
- Output: approve, reprice, restructure, decline, or request-evidence memo.

### Deal Underwriting and Diligence

- Skill stack: `universal-banker`, `corporate-counsel`, `spreadsheet`, `pdf`.
- Mandate: test borrower, collateral, structure, sponsor, docs, and downside
  recovery.
- Output: diligence findings, scenario table, exceptions, and conditions
  precedent.

### Capital Markets / Lender Routing

- Skill stack: `universal-banker`, `ethical-supersuader`.
- Mandate: match structure to capital providers, process strategy, distribution
  risk, and lender-facing drafts.
- Output: ranked route, economics, required package, and draft-only outreach.

### M&A / Strategic Alternatives

- Skill stack: `universal-banker`, `investment-management`.
- Mandate: valuation, buyer/seller logic, synergy realism, financing risk, and
  process control.
- Output: transaction view, valuation range, process map, and risk controls.

## Growth and Revenue

### Market Intelligence

- Skill stack: `growth-operating-system`.
- Mandate: ICP, segmentation, customer evidence, competitor map, pain and
  objection library.
- Output: opportunity map and demand-quality assessment.

### Offer and Positioning

- Skill stack: `growth-operating-system`, `ethical-supersuader`.
- Mandate: offer design, pricing psychology, risk reversal, differentiation,
  and message-market fit.
- Output: offer ladder, positioning map, and testable promise.

### Sales / Partnerships / CRM

- Skill stack: `growth-operating-system`, `ethical-supersuader`.
- Mandate: qualified pipeline, outreach, referral systems, partnership routes,
  CRM hygiene, and conversion process.
- Output: target list, outreach drafts, qualification path, follow-up logic,
  economics, and no-send boundary.

### Funnel / CRO / Growth Analytics

- Skill stack: `growth-operating-system`, `ai-ml-research-lab`.
- Mandate: CAC, LTV, conversion, cohort behavior, attribution skepticism,
  experiment design, and kill rules.
- Output: funnel map, experiment, metric contract, and review trigger.

## Communications

### Persuasive Writing / Communications

- Skill stack: `ethical-supersuader`.
- Mandate: concise, human, high-density prose in the principal's voice for emails,
  memos, pitches, public copy, investor/deal materials, and positioning.
- Output: sendable draft or publication-ready copy, with claims supported.

## Product / Engineering / Design

### Product / Engineering / Design

- Skill stack: `visual-design-operating-system`, `ai-ml-research-lab`,
  deployment and browser skills as needed.
- Mandate: build, validate, present, and deploy software, dashboards, reports,
  sites, and visual artifacts.
- Output: tested artifact, QA receipt, and deployment status if authorized.

## Data / AI / Model Validation

### Data / AI / Model Validation

- Skill stack: `ai-ml-research-lab`, `agent-ops-control-plane`.
- Mandate: model quality, leakage control, evals, benchmark fixtures,
  calibration, model cards, RL/simulation support, and production boundaries.
- Output: model card, benchmark result, failure modes, and recommendation to
  the domain owner.

## Operations / Security / Records

### Operations / Security / Records

- Skill stack: `agent-ops-control-plane`, security, docs, and records skills.
- Mandate: controls, secrets boundary, audit trail, logs, receipts, access,
  incident review, and durable memory promotion.
- Output: control record, issue list, receipt, or escalation.

## Staffing Rule

Use one owner and one to three specialists for most missions. Larger pods are
reserved for missions that genuinely span investing, banking, growth, product,
and operations.
