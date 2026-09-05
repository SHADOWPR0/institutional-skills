# Evidence And Walk-Forward Contract

This contract turns a technical idea into a falsifiable experiment. It applies to indicator rules, chart patterns, learned features, discretionary analyst packets, and LLM-agent replay.

## 1. Freeze The Claim

Before seeing evaluation outcomes, record:

- economic hypothesis and expected failure mode;
- point-in-time universe and product mapping;
- input schema, timezone, session calendar, and corporate-action/roll treatment;
- exact formula, parameters, thresholds, confirmation lag, and version hash;
- action space, entry, target/stop or exit horizon, and tie-breaking rule;
- transaction costs, spread, fees, slippage, gap-through, tick rounding, and liquidity exclusions;
- development interval, fold boundaries, embargo, primary metric, and minimum sample requirement;
- all variants that count toward the research family.

Do not choose a nearby pattern, threshold, cost, or horizon after observing its test result and then present it as predeclared.

## 2. Enforce Point-In-Time Causality

Each field has both an event time and an availability time. The decision may use only information whose availability time is at or before the frozen cutoff.

Common traps:

- centered rolling windows;
- right-side pivots timestamped at the pivot rather than at confirmation;
- revised macro, constituent, or fundamental data;
- session highs/lows before the session is complete;
- continuous-futures rolls or back-adjustments computed with future data;
- features fit or normalized on the entire sample;
- target/stop order inferred from an OHLC bar that touched both;
- agents retrieving news, dates, or historical outcomes during replay.

Close-confirmed bar signals execute on the next admissible bar/quote. If price gaps through the intended level, use the adverse executable price, not the theoretical signal level.

## 3. Use Development-Only Nested Walk-Forward

Use expanding or rolling folds that respect time:

1. outer training window;
2. inner validation used for features, thresholds, models, and hyperparameters;
3. purged outer test window used once for fold scoring;
4. embargo at least as long as the maximum label/holding horizon;
5. final locked OOS held outside the discovery process.

Overlapping events and labels share future returns. Purge them or use cluster-aware uncertainty. Never randomly shuffle market observations as the primary validation.

All preprocessing—imputation, scaling, winsorization, feature selection, calibration, and class balancing—fits inside each training fold.

## 4. Score Economics, Not Classification Alone

Report at minimum:

- eligible observations, proposals, accepted trades, and exposure;
- gross and net expectancy in points, returns, and R where meaningful;
- win rate, average win/loss, payoff ratio, and break-even win rate;
- median, dispersion, confidence interval, and fold-by-fold results;
- maximum drawdown and loss concentration;
- performance by instrument, session, direction, volatility, trend, and liquidity regime;
- break-even transaction cost and sensitivity to worse fills;
- calibration and decision-curve or utility behavior for probabilistic systems.

Accuracy can rise while trading expectancy falls. A rare-event classifier can look strong by staying flat. Execution rate is therefore a diagnostic, not a target to maximize blindly.

## 5. Use Honest Comparators

Every proposal should face the comparators that explain the least-complex alternative:

- always flat;
- unconditional asset drift at the same timestamps/horizon;
- same-symbol randomized timestamps matched for session and exposure;
- naive trend and naive reversal rules;
- a simple regularized linear model for learned systems;
- the incumbent strategy under identical costs and fills.

A benchmark may be read as an economic hurdle. Do not copy its mechanics into a challenger unless explicitly authorized and counted as a separate hypothesis.

## 6. Control Research Multiplicity

The family includes every inspected combination of pattern, direction, instrument, horizon, filter, threshold, model, feature packet, cost, and regime. Preserve failures.

Use a declared correction such as Benjamini-Hochberg for a discovery family, plus walk-forward stability and economic-materiality gates. A small p-value does not rescue tiny expectancy, concentration, or weak break-even costs.

Report the full tested count, not only survivors. White's Reality Check, Hansen's SPA, deflated Sharpe, or probabilistic Sharpe can supplement—not replace—clean design when selection pressure is high.

## 7. Evidence Grades

- `A_VALIDATED`: executable causal implementation; nested walk-forward and locked OOS; survives realistic costs, comparators, multiplicity, stability, and sample gates; operational parity proven.
- `B_RESEARCH_CANDIDATE`: causal OOS/walk-forward research result that survives primary screens but lacks one or more product, regime, sample, forward-paper, or operational proofs.
- `C_DESCRIPTIVE`: reproducible association or diagnostic behavior with no tradable claim.
- `D_DOCTRINE`: practitioner framework or untested interpretation.
- `F_REJECTED`: failed causality, economics, baseline, multiplicity, stability, or tradability.

Only a separately governed capital owner may decide that grade A evidence is deployable.

## 8. Agent Replay Protocol

LLM replay is testable, but historical evaluation has a special contamination risk: a pretrained model may recognize dates, prices, famous events, or text-derived outcomes.

Freeze before replay:

- model and exact version;
- system/developer/user prompts and skill hashes;
- tool allowlist, with internet and historical search disabled;
- sampling settings and seed set;
- finite action menu and deterministic candidate generator;
- risk, cost, fill, and outcome resolver versions;
- all scoring metrics and termination rules.

At each heartbeat:

1. construct a point-in-time snapshot using only data available at cutoff;
2. replace date and absolute-price identifiers with stable masked equivalents when they are not economically necessary;
3. give every role the same immutable snapshot ID and candidate menu;
4. require typed proposals and bounded rationales;
5. let a falsifier challenge admissibility and unsupported claims;
6. allow the portfolio role to choose one candidate or `FLAT`;
7. validate geometry, staleness, risk, and costs deterministically;
8. resolve the outcome from later tape without showing it to the agents;
9. append proposals, rejections, selection, and outcome to an immutable ledger.

Run multiple declared seeds and compare:

- each analyst alone;
- the full desk;
- a deterministic simple policy;
- random selection from the same valid menu;
- always flat.

Treat forward paper/shadow operation as the strongest initial evidence. Historical replay alone cannot prove absence of foundation-model contamination.

## 9. Learning Without Prompt Drift

Do not let an agent rewrite its skill or prompt after each outcome. First collect 60–90 sessions or a preregistered minimum number of independent decisions.

If outcomes justify adaptation, begin with a small contextual bandit that chooses among frozen analyst policies or weights their proposals using predeclared market-state features. Evaluate it walk-forward against the frozen equal-weight desk. Direct reinforcement learning of a large language model against sparse PnL is a later research program, not the starting point.

## 10. Promotion Packet

A promotion packet contains:

- immutable hypothesis and configuration hashes;
- data lineage and forbidden-data audit;
- fold-level and aggregate economics;
- all attempted variants and multiplicity treatment;
- benchmark parity proof for costs/fills;
- failure regimes, concentration, and sensitivity;
- reproducible command and artifact hashes;
- explicit `PROMOTE`, `ITERATE`, or `KILL` routing.

No prose summary may contradict the machine-readable ledger.

## 11. Differential-Prefix Causality Audit

Use this audit before assigning more than `C_DESCRIPTIVE` evidence to a
feature, detector, or event rule. It is a regression check, not proof of edge.

1. Compute the feature and signal on each truncated history ending at cutoff `t`.
2. Compute it again on the full history, then retain values at or before the same cutoff.
3. Compare the two outputs at every shared timestamp.
4. Treat any material difference as future dependence unless it is a declared, bounded warm-up or numerical-tolerance effect.
5. Run deliberately leaky controls. The audit is not credible if it cannot reject known leaks.

Record formula parameters, bar/session convention, warm-up length, numerical
tolerance, first availability time, and every untriggered path. A detector
that did not trigger in the sample is not validated merely because it did not
fail.

Required regression fixtures:

- causal trailing moving average: stable at every eligible cutoff;
- centered moving average: rejected as future-dependent;
- right-side pivot stamped at pivot time: rejected until restamped at its confirmation time;
- session high claimed before the session closes: rejected or made unavailable until the declared completion event;
- fair-value-gap confirmation: availability is the confirmation bar, not the first bar in the visual pattern;
- composed entry plus regime gate: test the gate's incremental lift against entry-only and randomized-gate controls. Zero incremental lift is not a promotion result.

The concept is compatible with public lookahead-analysis practice. No external
detector code is imported; formulas and tests remain local, transparent, and
independently specified.

## 12. Typed Event Composition

Represent every technical event as a typed definition before testing it. The
minimum record is:

- `event_id` and falsifiable hypothesis;
- formula and frozen parameters;
- `event_time` and `first_available_at`;
- one role per component: `entry`, `zone`, `context`, `timing`, or `exit`;
- finite persistence and lookback windows;
- explicit `AND`/`OR` composition;
- family count and multiplicity treatment;
- entry-only, randomized-gate, and component-removal ablations.

Do not turn a visual stack into a causal claim by naming it a setup. A
right-side confirmation, completed-session statistic, or later gap fill may
be useful context, but it cannot be used at the earlier visual timestamp. A
multi-component event must show that each added component improves the
predeclared economic objective beyond the entry-only and randomized controls.

An event with missing availability times, infinite persistence, unbounded
lookback, undeclared family size, or missing ablations remains `C_DESCRIPTIVE`
or below. Costed OOS evidence is required for any higher grade.
