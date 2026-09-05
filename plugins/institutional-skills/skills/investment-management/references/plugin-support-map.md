# Curated Plugin Support Map

Use this file when `investment-management` needs polished public-equity, modeling, tracker, risk-report, or banking-adjacent artifact discipline from the bundled OpenAI curated plugins.

This file is a support map, not a new front door. `investment-management`
remains the decision owner for mandate, disclosure mode, objective mode, private
local corpus use, preserved model/risk provenance, sizing, risk governance,
quant/systematic work, and final investment judgment.

The former `investment-management-private`, `investment-management-public`, and
`investment-management-production-legacy` packages are consolidated inside
`investment-management/references/source-skill-index/legacy-packages/` as
provenance only. Do not route to them as active packages and do not let bundled
plugins replace the canonical local investment owner.

Global macro is not delegated to a bundled/vendor plugin. For macro regime
analysis, zero-based global macro rebuilds, thesis books, expression comparison,
price-aware entry states, paper-book recommendations, monthly checks, event
reviews, and locked-consumer favored macro themes, route through the canonical
`global-macro-theme-picker` child skill under `investment-management`. Plugins
may contribute public-equity, modeling, memo, deck, or data-artifact discipline
only after the canonical macro/investment route is selected.

## Source Plugin Roots

- Public Equity Investing: `{RECIPIENT_RESOURCE}`
- Investment Banking: `{RECIPIENT_RESOURCE}`

Do not edit plugin-cache files. Treat them as versioned upstream references that may change on app update. If a plugin file is missing or a version changes, continue with this skill's native workflow and note the missing support source.

## Operating Rule

1. Start in `investment-management`.
2. Set `PRIVATE_INTERNAL` or `PUBLIC_SAFE`.
3. Set `QUALITY_COMPOUNDING` or `OPPORTUNITY_CAPTURE`.
4. Decide the investment question, benchmark, horizon, constraints, and output.
5. If the question is global macro, load `global-macro-theme-picker` first and
   use plugins only for subordinate artifacts after the macro route is set.
6. Load only the plugin specialist file that improves the current deliverable.
7. Borrow workflow structure, output contracts, QC patterns, scripts, and source discipline. Do not hand off decision ownership unless the user explicitly asks for a plugin-native workflow.
8. Keep private local research and preserved model/risk provenance out of
   plugin-derived `PUBLIC_SAFE` deliverables.

## Public Equity Support Modules

Use these as support references for listed-equity workflows:

- `skills/public-equity-investing/SKILL.md`: router discipline, invocation boundaries, context preflight, and support-layer pattern.
- `skills/initiating-coverage/SKILL.md`: coverage report architecture, buy-side/sell-side mode handling, report contracts.
- `skills/long-short-pitch/SKILL.md`: variant perception, catalyst path, setup, risk/reward, and pitch packaging.
- `skills/portfolio-risk-management/SKILL.md`: position sizing, hedge design, integrated risk plan, basis-risk ledger, liquidity/exit posture, monitoring triggers.
- `skills/thesis-tracker/SKILL.md`: append-only thesis tracking, falsifiable pillars, KPI/catalyst/evidence ledger, company-thesis vs security-thesis distinction.
- `skills/earnings-preview/SKILL.md` and `skills/earnings-deep-dive/SKILL.md`: event prep, post-print update, guide/consensus/expectations analysis.
- `skills/equity-model-update/SKILL.md`: public company model refresh and estimate bridge discipline.
- `skills/catalyst-calendar/SKILL.md`: dated catalyst tracking and review cadence.
- `skills/event-driven-analyzer/SKILL.md`: event probability/payoff framing for equity-linked situations.
- `skills/economic-impact-report/SKILL.md`: macro/economic transmission into public-equity exposures.
- `skills/idea-generation/SKILL.md`: public-equity screen and idea list scaffolding.
- `skills/company-tearsheet/SKILL.md`: compact issuer snapshot structure.
- `skills/comps-valuation/SKILL.md`, `skills/dcf-model-builder/SKILL.md`, `skills/three-statement-model-builder/SKILL.md`, and `skills/scenario-sensitivity-generator/SKILL.md`: valuation/modeling architecture and QA scaffolds.
- `skills/financials-normalizer/SKILL.md`: source hierarchy, reported vs adjusted financials, and normalization evidence labels.
- `skills/model-audit-tieout/SKILL.md`: workbook and model review when the task is to audit existing financial models.
- `skills/deck-report-qc/SKILL.md`: first-pass circulation QC for public-equity decks or reports.

## Banking Support Modules For Investment Work

Use these when an investment-management task crosses into financing, private company valuation, deal process, or committee artifact work. If the task is primarily underwriting, capital markets, M&A, covenant design, securitization, or deal structuring, route the decision to `universal-banker`.

- `skills/investment-banking/SKILL.md`: banker router discipline and workflow routing playbook.
- `skills/memo-builder/SKILL.md`: client, committee, board, financing, process, and diligence memo structure.
- `skills/model-audit-tieout/SKILL.md`: model readiness, formula controls, source tie-out, issue logs.
- `skills/covenant-package-analyzer/SKILL.md`: finance-side covenant and headroom support.
- `skills/private-credit-underwriting/SKILL.md`: borrower-level credit workflow support.
- `skills/capital-markets-issuance/SKILL.md`: issuer financing, market window, instrument choice, investor targeting.
- `skills/cim-builder/SKILL.md` and `skills/cim-teardown/SKILL.md`: CIM architecture and diligence resilience.
- `skills/dcf-model-builder/SKILL.md`, `skills/lbo-model-build/SKILL.md`, `skills/merger-model-builder/SKILL.md`, `skills/three-statement-model-builder/SKILL.md`, and `skills/scenario-sensitivity-generator/SKILL.md`: model build standards and transaction analysis support.
- `skills/comps-valuation/SKILL.md`, `skills/financials-normalizer/SKILL.md`, and `skills/company-tearsheet/SKILL.md`: valuation and normalization support.
- `skills/ib-deck-qc/SKILL.md`: banking deck/report QC before circulation.

## Preferred Lift Targets

Lift ideas into local work only when they improve repeatability:

- append-only thesis logs
- point-of-use source/cell/range tie-outs
- model readiness labels
- artifact hierarchy: hero deliverable first, support artifacts second
- explicit stale-data and evidence-quality labels
- separate company thesis, security thesis, sizing, and action
- hedge-failure and size-down/no-hedge comparisons
- decision-grade vs screening-only posture labels
- documented handoff payloads for multi-agent work

Do not lift plugin material in a way that weakens this skill's benchmark discipline, disclosure separation, private corpus protection, or risk-first decision loop.
