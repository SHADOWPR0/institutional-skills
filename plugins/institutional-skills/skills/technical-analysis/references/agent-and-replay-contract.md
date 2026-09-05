# Technical Analyst Agent And Replay Contract

Use this contract to stage a small analyst desk without multiplying skill packages. Every role invokes the same canonical `technical-analysis` skill; `investment-management` owns portfolio judgment, `ai-ml-research-lab` owns evaluation, and `agent-ops-control-plane` owns orchestration.

## Desk Roles

| Role | Allowed work | Required output | Forbidden work |
| --- | --- | --- | --- |
| Market-State Verifier | Freeze and verify the causal snapshot, calendar, session, staleness, roll, and candidate menu | Verified facts and admissibility flags | Directional persuasion or candidate selection |
| Continuation Analyst | Argue the strongest trend/momentum/acceptance path | One candidate ID or `FLAT`, evidence, invalidation | Inventing prices or editing candidates |
| Reversal/Liquidity Analyst | Argue the strongest exhaustion, rejection, failed-auction, or mean-reversion path | One candidate ID or `FLAT`, evidence, invalidation | Claiming order-book facts absent from the packet |
| Falsifier | Attack both cases for leakage, duplication, weak evidence, bad geometry, or regime mismatch | Veto flags and concise rebuttal | Creating a replacement trade thesis |
| Portfolio Manager | Select one admitted candidate or `FLAT` | Final typed proposal and reason codes | Overriding deterministic risk or sizing capital |
| Performance Analyst | Resolve later first passage/terminal outcome and comparator results | Append-only outcome record | Altering historical proposals or prompts |

Default debate budget: one proposal per directional analyst, one rebuttal by the falsifier, one synthesis by the manager.

## Finite Action Menu

Agents do not invent arbitrary brackets. A deterministic generator produces 6–12 or another preregistered bounded number of valid candidates from causal market structure. Each candidate contains:

```json
{
  "candidate_id": "c07",
  "side": "LONG",
  "entry": 20000.0,
  "target": 20020.0,
  "stop": 19990.0,
  "tick_size": 0.25,
  "entry_type": "market_or_declared_limit",
  "ttl_minutes": 60,
  "source_levels": ["session_vwap", "prior_high"],
  "cost_points": 1.0
}
```

The only valid final actions are one menu candidate or `FLAT`. Deterministic code validates tick rounding, side geometry, staleness, TTL, costs, duplicate exposure, session admission, and risk status.

## Immutable Snapshot

Every role receives the same packet:

- `snapshot_id` and content hash;
- instrument, venue, synthetic clock label, horizon, and session phase;
- data cutoff and maximum source-availability timestamp;
- verified multi-timeframe OHLCV/structure features;
- exact data coverage and stale/missing flags;
- finite candidate menu;
- prompt, model, skill, and tool versions;
- no future bars, outcome fields, exact historical date, or unnecessary absolute identifiers.

If the verifier fails, every analyst must return `FLAT` and the heartbeat remains in the ledger.

## Proposal Packet

The canonical JSON packet validated by `scripts/validate_analysis_packet.py` contains:

```json
{
  "schema_version": "1.0",
  "mode": "AGENT_REPLAY",
  "as_of": "2026-01-01T15:00:00Z",
  "data_cutoff": "2026-01-01T15:00:00Z",
  "instrument": "NQ",
  "venue": "GLBX",
  "horizon_minutes": 60,
  "snapshot_id": "sha256:...",
  "skill_version": "technical-analysis@1",
  "model_id": "frozen-model-version",
  "role": "portfolio_manager",
  "verified_observations": ["Snapshot passed the causal availability audit."],
  "timeframe_state": {"decision_horizon": "indeterminate"},
  "candidate_set_id": "sha256:...",
  "decision": "FLAT",
  "selected_candidate_id": null,
  "entry": null,
  "target": null,
  "stop": null,
  "tick_size": 0.25,
  "ttl_minutes": 60,
  "evidence_grade": "D_DOCTRINE",
  "confidence": 0.0,
  "continuation_case": "No admitted continuation candidate cleared the portfolio gate.",
  "reversal_case": "No admitted reversal candidate cleared the portfolio gate.",
  "invalidation_conditions": ["Any material snapshot or candidate-set change requires a new packet."],
  "stale_data": false,
  "lookahead_audit": {
    "passed": true,
    "future_data_used": false,
    "signal_confirmed_at": "2026-01-01T15:00:00Z"
  },
  "costs": {
    "round_trip_points": 1.0,
    "slippage_model": "next-admissible-observation with adverse gap-through",
    "adverse_gap_through": true
  },
  "risk_status": "PASS",
  "execution_authority": false
}
```

Confidence is a self-report unless separately calibrated; it is never position size.

## Replay Sequence

```text
freeze snapshot -> verify -> independent analyst proposals -> falsify
-> portfolio select/FLAT -> deterministic validate -> later tape resolve
-> append outcome -> score desk and comparators
```

The outcome resolver uses first-touch event data when available. If only bars exist and target and stop are both touched, apply the preregistered conservative ambiguity rule. Costs and adverse gap-through are identical for agents and benchmarks.

## No-Sprawl Registry

The desk may reference but must not copy:

- `{SKILLS_ROOT}/technical-analysis`
- `{SKILLS_ROOT}/investment-management`
- `{SKILLS_ROOT}/ai-ml-research-lab`
- `{SKILLS_ROOT}/agent-ops-control-plane`

Role prompts are configuration, not new skills. Research data remains in its owning data tree. Arena-specific outputs belong in one isolated project directory with an index, immutable run IDs, and retention rules; never vendor the skill folders into it.

## Staging Gate

Skills-only staging is complete when:

- all canonical skills resolve from the global Codex exposure root;
- each role has a one-sentence objective, input schema, output schema, and forbidden actions;
- the finite candidate and proposal contracts validate;
- the causal replay protocol and contamination audit are frozen;
- no data pull, model training, cloud deployment, Telegram message, broker connection, or production mutation has occurred.

The terminal status is `STAGED — NO IMPLEMENTATION`.
