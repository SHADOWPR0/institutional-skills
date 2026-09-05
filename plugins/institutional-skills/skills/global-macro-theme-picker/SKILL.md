---
name: global-macro-theme-picker
description: "Vendor-neutral investment-management subskill for global macro research workflows: quarterly zero-based world rebuilds, thesis cards, expression comparison, price-aware entry states, paper portfolio recommendations, monthly evidence checks, event reviews, and sanitized locked-consumer theme handoffs. Research and paper recommendations only; no live trading or autonomous execution."
---

Public distribution: resolve `{SKILLS_ROOT}` to this plugin's `skills/` directory. Recipient bindings and tool availability are explicit; read [portability](../../PORTABILITY.md). No host, CRM, sending, or trading access is implied.

# Global Macro Theme Picker

## Quick Reference

### What It Does

Runs a full global macro research process from a broad cross-asset information
set. It separates theme validity, price attractiveness, timing, expression
quality, and paper portfolio fit before producing an auditable recommendation
for human approval.

### Entrypoints

- favored global macro themes
- macro regime or cross-asset theme scan
- quarterly zero-based macro rebuild
- monthly macro evidence check
- event-driven macro review
- paper global macro book recommendation
- expression comparison and entry-state review
- core-book themes versus independent model additions
- Locked consumer theme handoff packet

### Inputs / Outputs

- Inputs: as-of timestamp, evidence cutoff, source manifest, world-state data,
  candidate imbalances, current or watch-list theses, expression universe,
  risk limits, and data availability map.
- Outputs: world-state table, candidate imbalances, thesis cards, expression
  comparison, critic memo, proposed paper book, risk/stress report, monthly
  evidence update, event review, or sanitized theme handoff.

### Dependencies / Tooling

`investment-management` is the domain and capital-decision owner. This package
may compare instruments, build paper recommendations, and compute proposed risk
reports, but it cannot place orders, alter live portfolios, infer approval, or
override the parent skill. Use primary sources, causal as-of data, and
`scripts/validate_theme_packet.py` before publication.

### Test Command(s)

From this skill directory, run the portable consumer suite:

```bash
python3 -B -m unittest discover -s ../../../../tests
```

### Invariants

- The output is research or paper recommendation only and grants no execution
  authority.
- Every portfolio change remains `PROPOSED` until the principal explicitly approves it.
- Every theme must reference the same market-state snapshot.
- Unsupported data is `UNAVAILABLE`; it is never guessed or silently inferred.
- Theme-handoff packets contain no securities, tickers, weights, sizing, orders,
  or execution instructions.
- Rates-spread paper positions require DV01 normalization. FX paper positions
  require native notional, USD notional, margin, and 5/10/15 percent stress loss.

## Ownership And Routing

This is a reusable child of `investment-management`, not a second investment
front door. It can produce global macro research and paper recommendations for
the parent owner to review. Route actual capital allocation, mandate override,
brokerage/execution, live portfolio mutation, and final investment decisions
back to `investment-management`.

Load `references/global-macro-theme-framework.md` for the complete operating
contract, ranking method, expression selection, paper-book construction,
conflict hierarchy, output schema, cadence, examples, and theme handoff.
The sanitized verbatim source specification is preserved at
`references/authoritative-global-macro-agent-spec.md`; use it as the default
macro process source when this package and the framework reference differ.

## Required Workflow

1. Freeze the information set.
   - Record `as_of`, `evidence_cutoff`, retrieval timestamps, and unavailable or
     stale sources.
   - Historical runs may not see later releases or revisions.

2. Build one shared market-state snapshot.
   - Resolve liquidity, inflation, policy, and business-cycle states first.
   - Give the snapshot an immutable `snapshot_id`.
   - Keep facts, estimates, assumptions, and interpretation distinct.

3. Scan the full macro surface.
   - Rates and curves; FX; commodities; country and regional equities; credit;
     reserve assets; and structural, fiscal, geopolitical, and capex themes.

4. Generate candidate imbalances from zero.
   - Quarterly rebuilds do not inspect the existing book until the zero-based
     candidate book is complete.
   - Generate 8 to 15 candidate imbalances, promote no more than eight thesis
     cards, and normally carry no more than five independent active theses.
   - Compare core-book ideas and independent model additions without anchoring.

5. Require a causal thesis card.
   - State the imbalance, decision maker, likely response, transmission path,
     asset-class impact, thesis, catalyst window, evidence, strongest bear case,
     invalidation, crowding, market structure, and data gaps.
   - Separately label `THESIS`, `VALUATION_OR_PRICE`, `TIMING`, and
     `PORTFOLIO_ACTION`.

6. Reconcile, rank, and compare expressions.
   - A theme that contradicts the shared snapshot is rejected or explicitly
     labeled `CONDITIONAL`; never create a second private regime view to save it.
   - Compare at least three expressions when feasible on causal purity,
     valuation, liquidity, carry, convexity, governance, currency exposure,
     path dependency, implementation cost, and thesis-neutral downside.
   - A valid thesis at a bad price is `WAIT_PRICE`, not an automatic position.

7. Run adversarial checks.
   - Test stale evidence, circular logic, consensus masquerading as variant
     insight, duplicated drivers, missing transmission, hidden contradictions,
     crowding, and unsupported data.

8. Construct paper recommendation if requested.
   - Size by risk contribution and independent thesis exposure, not ticker
     count or raw dollars.
   - Report cash, gross/net notional, volatility, one-day 99 percent VaR,
     expected shortfall, theme and factor risk, eight or more stress scenarios,
     liquidity, gap risk, and approval status.

9. Publish and validate.
   - Use full paper-book packets for macro PM work.
   - Use sanitized theme-handoff packets for locked downstream consumers.
   - Run the packet validator. Validation failure blocks publication.

## Output Contract

Return:

- shared market-state snapshot and freshness
- ranked themes or thesis cards with `CORE_BOOK` or `MODEL_ADDITION` origin
- thesis, causal chain, variant view, and state reconciliation
- catalysts and timing
- evidence quality and source status
- strongest bear case and falsifiable invalidation
- crowding and positioning
- market structure
- expression comparison, price/valuation state, and entry state when running
  full macro research
- proposed paper book, risk contribution, stress loss, and human approval status
  when running full paper-book mode
- data gaps and explicit `UNAVAILABLE` fields
- conflict-resolution record
- next daily, monthly, and quarterly review dates

Do not return live orders or imply execution. Theme-handoff mode must not return a model
portfolio, individual security, allocation, weight, size, entry, target, stop,
order, or execution plan.

## Self-Check

Before publishing, answer yes to all:

- Is one snapshot ID used everywhere?
- Are liquidity, inflation, policy, and business-cycle states explicit?
- Does every theme have a complete causal chain and transmission mechanism?
- Are core themes and model additions independently generated and labeled?
- Are contradictory themes rejected or conditional?
- Are missing values marked `UNAVAILABLE` rather than inferred?
- Are evidence timestamps causal and sources resolvable?
- On quarterly rebuilds, was the existing book hidden until the zero-based book
  was complete?
- Does each promoted thesis separate thesis state, price, timing, and action?
- Were at least three expressions compared when feasible?
- If a paper book is present, are risk contributions, DV01/FX stress rules,
  scenario stresses, liquidity/gap flags, and approval state explicit?
- If this is a theme handoff, are measurement proxies and security-level fields
  absent from the published packet?
- Does the validator pass?
