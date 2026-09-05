# Runtime Governance And Cost

## Runtime Contract

Every long-running or multi-agent workflow should define:

- owner
- objective
- workspace
- allowed tools
- forbidden actions
- runtime budget
- cost budget
- external side effects
- observability
- stop condition
- escalation path

If a workflow can spend money, contact people, trade, deploy, delete, overwrite, or publish, it needs an explicit kill switch.

## Model And Tool Routing

Route by task complexity:

- low-cost deterministic tools for search, parsing, counting, formatting, and validation
- lightweight models for classification, extraction, and drafting
- stronger reasoning models for high-ambiguity synthesis, planning, and failure diagnosis
- specialist tools for source-of-truth systems, databases, calendars, mail, deployments, and spreadsheets

Track quality per dollar and quality per minute. The most expensive path is justified only when it changes the decision quality.

## Cost Controls

Use:

- bounded retrieval depth
- max attempt count
- deterministic prechecks
- batchable tool calls
- cached source summaries
- explicit stop conditions
- no-op detection before expensive work

Report:

- total attempts
- time spent
- external calls made
- failed calls
- cost proxy when available
- remaining uncertainty

## Kill Switches

Stop or escalate when:

- source hierarchy conflicts
- data freshness is unacceptable
- secrets or private data could leak
- regulated action is requested without compliance checks
- campaign, trade, or deployment risk exceeds the allowed loss budget
- agents disagree on a material fact
- repeated retries are not improving output quality
- the user changes scope mid-run

## Incident Review

For failed runs:

1. State what happened.
2. Identify the broken assumption.
3. Separate model error, tool error, source error, and instruction error.
4. Patch the smallest responsible layer.
5. Retest.
6. Promote, iterate, or retire.

Do not hide failed experiments. A clean failure record is part of production hardening.
