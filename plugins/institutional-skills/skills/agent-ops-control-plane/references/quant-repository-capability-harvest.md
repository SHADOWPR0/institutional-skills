# Quant Repository Capability Harvest

Use this reference before adopting ideas from an external quant, trading,
agent, connector, or research repository. It creates a bounded evidence record;
it does not create a new owner, routing front door, permanent clone, or
permission to execute external code.

## Harvest Record

Record: objective; domain owner; exact repository and target system; full commit
SHA and review date; license; dependency/data/API provenance; maintenance and
activity signal; claimed capability versus demonstrated capability; source/test
review budget; and a cost proxy.

Review untrusted code only in a disposable `/tmp` checkout. No external code
execution is permitted during intake. Declare the number of agents and
rechecks before starting, then record cleanup proof for every temporary clone.

## Tactic Record

For each candidate tactic, record source files/lines reviewed, independent
problem statement, evidence grade, benchmark, ablation, effort, expected
impact, license/contamination boundary, and `ADOPT`, `ADAPT`, `HOLD`, or
`REJECT` decision. README claims are orientation only; they cannot satisfy a
demonstrated-evidence requirement. GPL or unlicensed code cannot be direct-code
`ADOPT` material for proprietary systems.

Protected local paths remain read-only during intake. Compare any independently
specified local implementation against the incumbent under the same data,
costs, and acceptance criteria before promotion.

## Adapter Evidence Annex

For adapters, record the official API version and as-of date, least-privilege
authentication scope, precision, fees, product types, and event ordering for
place, acknowledge, fill, cancel, and status. Test websocket recovery and REST
reconciliation; duplicate intent after restart; rate-limit, outage, and stale
data injection; and explicitly report `SUPPORTED`, `UNSUPPORTED`, or
`UNVERIFIED` per capability.

No credentials, orders, or live capital actions are allowed without manual
approval from the domain owner. Adapter evidence is not strategy evidence.

## Deterministic Gate

A valid harvest record has a full SHA, review date, license, bounded budget,
no intake execution, protected-path read-only proof, temporary cleanup proof,
and tactic-level source/test/benchmark/ablation/effort/impact fields. It must
reject README-only evidence and direct proprietary adoption from GPL or
unlicensed code. Adapter records additionally require API/version/as-of,
least-privilege proof, event ordering, recovery/reconciliation tests, chaos
tests, S/U/U capability output, and manual approval before credentials or
orders.
