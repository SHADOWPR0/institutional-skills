# Curated Plugin Support Map

Use this file when `universal-banker` needs polished investment-banking, credit, capital-markets, model, covenant, process, memo, or deck artifact discipline from the bundled OpenAI curated plugins.

This file is a support map, not a replacement. `universal-banker` remains the decision owner for underwriting, structure, pricing, covenants, downside protection, distribution risk, specialist sub-agent orchestration, and final approve / reprice / restructure / decline judgment.

For native, editable Excel models and PowerPoint decks, load
`references/banker-xls-ppt-deliverable-standard.md` first. Use plugin and
imported package material only as execution or quality-control support; never
route around `universal-banker` for banking content or around
`visual-design-operating-system` for visual hierarchy and anti-slop review.

## Source Plugin Roots

- Investment Banking: `{RECIPIENT_RESOURCE}`
- Public Equity Investing: `{RECIPIENT_RESOURCE}`
- Bundled/imported Excel support: `{SKILLS_ROOT}/excel` (not bundled; recipient resource required), `{SKILLS_ROOT}/spreadsheets` (not bundled; recipient resource required)
- Bundled/imported PPTX support: `{SKILLS_ROOT}/imported-pptx-7142a2e9` (not bundled; recipient resource required), `{SKILLS_ROOT}/imported-pptx-generator-f0efb52a` (not bundled; recipient resource required)

Do not edit plugin-cache files. Treat them as versioned upstream references that may change on app update. If a plugin file is missing or a version changes, continue with this skill's native workflow and note the missing support source.

## Operating Rule

1. Start in `universal-banker`.
2. Define seat, mandate, instrument, capital structure, collateral, counterparties, and decision owner.
3. Route the deal vertical with `scripts/vertical_router.py` or `references/vertical-matrix.md`.
4. Use plugin modules only for artifact discipline, specialized checklists, deterministic scripts, and output packaging.
5. Keep the universal-banker risk standard intact: downside first, legal package, covenant bite, liquidation realism, distribution/funding risk, and failure triggers.
6. Do not treat plugin outputs as legal, tax, regulatory, brokerage, or final compliance advice.

## Investment Banking Support Modules

Use these as support references for transaction and financing workflows:

- `skills/investment-banking/SKILL.md`: banker router discipline, invocation boundaries, workflow routing, and artifact hierarchy.
- `skills/pitch-deck-builder/SKILL.md`: banking pitch page plans and draft slide content.
- `skills/memo-builder/SKILL.md`: client, committee, board, financing, process, and diligence memo structure.
- `skills/deal-process-tracker/SKILL.md`: process management, milestones, parties, diligence, and next actions.
- `skills/cim-builder/SKILL.md`: CIM architecture, equity story spine, diligence resilience, source/tie-out standards.
- `skills/cim-teardown/SKILL.md`: buyer/investor diligence critique and marketability issues.
- `skills/buyer-investor-list/SKILL.md`: buyer universe and investor targeting support.
- `skills/company-tearsheet/SKILL.md`: compact company snapshot.
- `skills/comps-valuation/SKILL.md`: trading/transaction comps scaffolding.
- `skills/dcf-model-builder/SKILL.md`, `skills/lbo-model-build/SKILL.md`, `skills/merger-model-builder/SKILL.md`, `skills/three-statement-model-builder/SKILL.md`, and `skills/scenario-sensitivity-generator/SKILL.md`: model build architecture, scenario planning, and transaction math support.
- `skills/financials-normalizer/SKILL.md`: reported vs adjusted financials, add-back discipline, KPI normalization, source labels.
- `skills/model-audit-tieout/SKILL.md`: formula controls, workbook hygiene, source tie-out, issue logs, decision-readiness labels.
- `skills/covenant-package-analyzer/SKILL.md`: finance-side credit agreement, covenant, basket, leakage, headroom, amendment, and waiver review support.
- `skills/private-credit-underwriting/SKILL.md`: borrower-level underwriting support for direct lending and private credit.
- `skills/distressed-recovery-waterfall/SKILL.md`: distressed recovery, priority, waterfall, and restructuring support.
- `skills/capital-markets-issuance/SKILL.md`: issuer-side financing strategy, market window, instrument choice, investor targeting, use of proceeds.
- `skills/ib-deck-qc/SKILL.md`: banking deck/report QC before circulation.
- `skills/meeting-prep/SKILL.md`: banker meeting preparation and question agenda support.

When using these modules for Excel or PowerPoint output, keep the final artifact
native and editable, reconcile deck numbers to the model, render workbook sheets
and deck thumbnails when tooling permits, and preserve source/footnote trails.

## Public Equity Support Modules

Use Public Equity Investing modules only when a banking task touches listed equity, public-company valuation, public comps, issuer/shareholder context, stock risk, or public-market read-through:

- `skills/public-equity-investing/SKILL.md`: listed-equity workflow routing and support-layer pattern.
- `skills/portfolio-risk-management/SKILL.md`: public equity position sizing, hedging, liquidity, and basis-risk support.
- `skills/thesis-tracker/SKILL.md`: public-company thesis status, catalysts, evidence ledger, and monitoring cadence.
- `skills/earnings-preview/SKILL.md`, `skills/earnings-deep-dive/SKILL.md`, and `skills/equity-model-update/SKILL.md`: public company estimate and event update support.
- `skills/initiating-coverage/SKILL.md`, `skills/long-short-pitch/SKILL.md`, and `skills/memo-builder/SKILL.md`: listed-company report and pitch scaffolding when a deal view needs public-market framing.
- `skills/deck-report-qc/SKILL.md`: public-equity deck/report QC when the deliverable is equity-market facing.

## Preferred Lift Targets

Lift ideas into local work only when they strengthen the deal desk:

- source universe and operative-document maps
- evidence labels and stale-data flags
- point-of-use model cell/range tie-outs
- adjusted EBITDA and add-back discipline
- covenant/headroom posture labels
- issue logs with severity, location, decision impact, owner, and recommended fix
- artifact hierarchy: IC memo, structure sheet, pricing sheet, distribution/exit plan, monitoring plan
- process trackers for diligence, bids, financing, approvals, and closing conditions
- deck/report QC before circulation
- native Excel model and PowerPoint deck QA gates from
  `references/banker-xls-ppt-deliverable-standard.md`

Do not lift plugin material in a way that weakens this skill's original underwriting voice, risk-first doctrine, broad asset-class coverage, or specialist lane orchestration.
