---
name: technical-analysis
description: CMT-curriculum-aligned technical analysis across trend, momentum, chart patterns, candlesticks, volatility, volume, breadth, relative strength, market profile, point-and-figure, cycles, Elliott/Fibonacci, intermarket, and market structure. Use for chart analysis, technical trade research, TA pattern interpretation, multi-timeframe market diagnosis, technical analyst agents, and causal walk-forward replay. Routes capital decisions through investment-management and distinguishes doctrine from tested edge.
---

Public distribution: resolve `{SKILLS_ROOT}` to this plugin's `skills/` directory. Recipient bindings and tool availability are explicit; read [portability](../../PORTABILITY.md). No host, CRM, sending, or trading access is implied.

# Technical Analysis

## Quick Reference

### What It Does

Provides a professional technical-analysis operating system: broad CMT-style doctrine, explicit causal interpretation, multi-timeframe synthesis, evidence grading, trade-scenario construction, and replay-ready agent packets. It incorporates the local `ta_vol_reflexivity` study without turning its daily research candidates into unsupported intraday rules.

### Entrypoints

- CMT, technical analyst, chart analyst, or market technician requests.
- Trend, momentum, mean-reversion, volatility, breadth, volume, relative-strength, or intermarket analysis.
- Chart patterns, candlesticks, point-and-figure, Ichimoku, market/volume profile, Elliott Wave, Fibonacci, cycles, or sentiment/positioning.
- Technical-analysis feature research, signal validation, causal replay, or agentic trading simulations.

### Inputs / Outputs

- Inputs: instrument, venue, as-of timestamp, data cutoff, timeframe stack, OHLCV or verified market snapshot, costs, and decision objective.
- Outputs: structured technical state, competing continuation/reversal cases, candidate levels or brackets, evidence grade, risks, invalidation, and a typed replay packet when requested.

### Dependencies / Tooling

- `investment-management` remains decision owner for trading, sizing, portfolio, and capital judgment.
- `ai-ml-research-lab` owns walk-forward design, leakage controls, agent evaluation, and model risk.
- `agent-ops-control-plane` owns bounded agent roles, handoffs, ledgers, and runtime controls.
- Deterministic market data and arithmetic outrank agent prose.

### Test Command(s)

From this skill directory, run the portable consumer suite:

```bash
python3 -B -m unittest discover -s ../../../../tests
```

### Invariants

- Never call a pattern or indicator profitable without instrument-, horizon-, execution-, and regime-specific evidence.
- Never use future bars to confirm a historical signal.
- A close-confirmed event is first executable on the next admissible observation unless an explicit executable quote proves otherwise.
- Separate observed facts, technical interpretation, empirical evidence, assumptions, and action.
- Raw agent prose cannot authorize a trade or bypass deterministic risk controls.

## Purpose And Ownership

This is the canonical support skill for professional technical analysis. It supersedes generic indicator-only analysis for serious TA work, but it does not replace `investment-management` and does not claim that the agent holds a CMT charter.

Use the smallest relevant reference:

- Broad doctrine or unfamiliar technique: [body of knowledge](references/body-of-knowledge.md).
- Exact pattern/indicator definitions: [pattern and indicator catalog](references/pattern-and-indicator-catalog.md).
- Claims of edge or strategy testing: [evidence and walk-forward](references/evidence-and-walk-forward.md).
- Feature causality or composed technical events: [evidence and walk-forward](references/evidence-and-walk-forward.md), including the differential-prefix audit and typed-event contract.
- Local empirical findings: [TA-vol-reflexivity study](references/ta-vol-reflexivity-study.md).
- private-execution-system Arena or another agent: [agent and replay contract](references/agent-and-replay-contract.md).
- Databento-backed technical features or replay: `{SKILLS_ROOT}/_library/docs/DATABENTO_MARKET_DATA_ML_OPERATING_CONTRACT.md` (not bundled; recipient resource required).
- Exact Databento TA, OHLCV, order-book, breadth, symbology, and replay examples: `{SKILLS_ROOT}/_library/docs/DATABENTO_OFFICIAL_DOCS_AND_EXAMPLES_CATALOG.md` (not bundled; recipient resource required).
- Provenance: [source map](references/source-map.md).

## Analysis Modes

Choose one mode before analysis:

- `DESCRIPTIVE_TA`: identify market structure and conditional scenarios; make no expectancy claim.
- `RESEARCH_TA`: formalize a causal signal and evaluate it against baselines, costs, and walk-forward evidence.
- `AGENT_REPLAY`: consume a frozen as-of snapshot and emit one typed proposal for deterministic historical or forward-paper scoring.
- `LIVE_SHADOW`: current-data proposal with zero execution authority; log the unresolved decision for later outcome scoring.

Default to `DESCRIPTIVE_TA` unless the user explicitly requests research, replay, or shadow operation.

## Source Hierarchy

1. Timestamped source data, exchange calendar, instrument specification, and executable quotes.
2. Frozen detector formulas, experiment contracts, manifests, and result artifacts.
3. CMT doctrine and established technical-analysis references.
4. Agent interpretation, chart narrative, and discretionary labels.

When these conflict, the higher source wins.

## Core Workflow

### 1. Freeze The Decision Context

Record instrument, venue, as-of timestamp, data cutoff, session state, horizon, timeframes, adjustment method, and whether the output is descriptive, research, replay, or shadow.

Reject stale, incomplete, timezone-ambiguous, split-corrupted, roll-corrupted, or future-contaminated inputs.

For Databento inputs, apply the canonical schema, symbology, sparse-OHLCV,
status/session, roll, MBP, event-order, caching, and historical/live parity
rules before interpreting any pattern or indicator.

### 2. Read Structure Before Indicators

Establish:

- primary and secondary trend;
- swing sequence and range boundaries;
- support, resistance, gaps, anchored references, and acceptance/rejection zones;
- volatility state and compression/expansion;
- volume, breadth, participation, and relative strength;
- regime and cross-asset context when available.

Indicators may summarize this state; they do not replace it.

### 3. Build Competing Cases

Always state at least:

- continuation case;
- reversal or failed-move case;
- neutral/indeterminate case;
- observations that would invalidate each case.

Do not stack correlated indicators as independent confirmation. RSI, stochastic, MACD, and moving-average slope may all encode overlapping transformations of the same price path.

### 4. Grade Evidence

- `A_VALIDATED`: executable, costed, leakage-safe walk-forward evidence with adequate samples and benchmark defeat.
- `B_RESEARCH_CANDIDATE`: causal OOS evidence survives primary screens but lacks product, regime, or forward-paper proof.
- `C_DESCRIPTIVE`: reproducible conditional behavior or in-sample finding; not a trading rule.
- `D_DOCTRINE`: practitioner interpretation without local empirical validation.
- `F_REJECTED`: failed causality, costs, baseline, stability, multiple-testing, or tradability.

The local study's two strict daily survivors are `B_RESEARCH_CANDIDATE`, not live rules. Its VIX inversion result is `C_DESCRIPTIVE`.

### 5. Construct The Output

For chart analysis, return:

- verified observations;
- timeframe-by-timeframe state;
- technical thesis and counter-thesis;
- relevant levels and why they matter;
- evidence grade and applicable empirical prior;
- costs/liquidity caveats;
- invalidation and next observation.

For a trading-agent proposal, emit the typed packet defined in [agent-and-replay-contract.md](references/agent-and-replay-contract.md). Arithmetic and admissibility are validated by `scripts/validate_analysis_packet.py`; a valid packet remains a proposal, not execution authority.

### 6. Install The Measurement Loop

Every recurring signal or agent decision records:

- frozen snapshot identity;
- prompt/skill/model versions;
- proposal and rejected alternatives;
- causal confirmation timestamp;
- entry convention, costs, and horizon;
- realized first passage or terminal outcome;
- benchmark-relative result;
- one bounded lesson that may be tested, not silently promoted.

## Research And Replay Rules

- Pre-register the universe, formulas, thresholds, action set, horizon, costs, split policy, and primary metric.
- Fit thresholds and select variants inside training folds only.
- Purge overlapping labels and embargo at least the maximum holding horizon.
- Compare against no-trade, unconditional drift, naive trend, naive reversal, and randomized-time controls.
- Apply next-observation execution, adverse gap-through, spread, fees, slippage, and product mechanics.
- Adjust for multiple testing across instruments, patterns, horizons, directions, filters, and costs.
- Report event counts, fold dispersion, break-even costs, concentration, and negative results.
- Historical agent replay should mask exact dates and absolute price levels when practical, disable internet/news retrieval, and freeze prompts, skills, model, tools, and sampling settings.
- Forward paper/shadow evidence outranks historical LLM replay because pretrained models may contain historical market information.
- Run the differential-prefix causality fixtures before promoting a new technical feature or event composition; a feature that changes at a frozen cutoff, other than declared warm-up tolerance, is future-dependent until proved otherwise.

## Agent Handoffs

Use one technical-analysis skill across roles; do not create separate momentum, reversal, pattern, or CMT skill copies.

Recommended bounded roles:

- Market-State Verifier: creates the causal snapshot and stale-data flags.
- Continuation Analyst: argues the strongest trend/momentum path.
- Reversal/Liquidity Analyst: argues the strongest exhaustion or failed-move path.
- Falsifier: attacks both proposals for leakage, duplication, weak geometry, and regime mismatch.
- Portfolio Manager: accepts one finite candidate or returns `FLAT`, subject to deterministic risk validation.
- Performance Analyst: resolves outcomes and updates the append-only ledger.

One claim, one rebuttal, one synthesis is the default debate budget.

## Guardrails

- No brokerage, exchange, Telegram, deployment, or capital action without separate explicit authority.
- No claims that a famous indicator works everywhere or that more confirmations imply more edge.
- No discretionary redrawing of historical patterns after outcomes are visible.
- No mixing index-level volatility findings with tradable futures, options, or ETP claims without product mechanics.
- No automatic skill or prompt mutation from a single winning or losing episode.
- No imported benchmark logic into a target strategy unless explicitly authorized and independently retested.
- Do not copy the 179 MB `ta_vol_reflexivity` corpus into this skill. Use the distilled annex and canonical source pointers.

## Related Skills

- `investment-management`: decision owner, risk, sizing, and capital governance.
- `ai-ml-research-lab`: leakage-safe experiment and agent evaluation.
- `agent-ops-control-plane`: agent orchestration, ledgers, and runtime controls.
- Legacy imported `stock-analyzer`: lightweight indicator utility only; this skill is the canonical professional TA route.
