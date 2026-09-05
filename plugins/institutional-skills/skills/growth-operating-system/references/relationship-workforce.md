# Relationship Workforce Acceptance

Growth owns account research, qualification, offer, channel, pipeline priorities,
and campaign learning. Ethical Supersuader owns the message brief, prose,
selection, and draft receipt. Universal Banker owns financing facts, credit,
lender routing, capital structure, and transaction claims. Relationship OS owns
canonical identity, factual dossiers, relationship provenance, suppression,
eligibility, touch history, and committed outcomes.

Use these functions within the existing workforce. Do not create another CRM,
campaign worker, scheduler, top-level skill, or identity graph.

## Recipient CRM Authority

Bind the recipient's actual CRM owner and schema through bindings.json. The included validator supports the documented relationship_update.v1 subset only; other CRM schemas need an explicitly mapped adapter. No private parser or operational record is included. A structurally valid packet never proves a database commit. The owner validates, reconciles suppression and commits. Consumers stage only authorized source-backed deltas and await authenticated owner receipts.

## Evidence To Finished Work

1. Research accounts and prospects from primary professional evidence. Preserve
   source path, namespace, observed time, SHA-256, record key, and field pointer.
   Separate fact, inference, and unavailable. A website claim is not a verified
   mandate, contact permission, introduction, or funding commitment.
2. Reconcile identities against owner-issued canonical IDs and aliases. Exact
   alias keys are campaign + source namespace + source ID. Candidate dedupe may
   group repeated records for review; only Relationship OS merges identities.
   Similar names, confidential aliases, and LinkedIn mutuals do not resolve IDs.
3. Measure contact coverage with denominators and source-specific counts. Separate
   usable direct professional contacts, general-office channels, missing data,
   stale contacts, and contacts whose usability remains unverified. Zero means
   measured zero; unavailable means unknown. Property matches and listing events
   are not usable agent or owner contacts. Deduplicate before computing coverage.
4. Assess fit, professional relationship paths, qualification gaps, decision
   makers, offer, and channel. Keep fund-anchor and transaction offers separate.
   Preserve the current queue unless a nomination change is explicitly authorized.
   Ask Universal Banker to assess missing financing facts; do not infer approval,
   terms, table funding, savings, issuer authority, or a lender commitment.
5. Pass the source-backed growth brief to Ethical Supersuader using its current
   `references/high-hit-rate-marketing-prose.md` (not bundled; recipient resource required) and native draft-receipt contract.
   Load its required prose references, lint, and perform the skeptical rewrite.
   Use a useful-offer or permission CTA unless evidence supports a meeting ask.
   Missing eligibility permits internal analysis, not external draft staging.
   Do not put invented placeholder contacts into recipient-addressed copy.
   Preserve the sourced channel in the brief, draft and receipt: an email stays
   `email`, including a reply or follow-up. Use `other` only for a known channel
   outside the contract, not as a substitute for missing context.
6. Produce the pipeline disposition and next owner action for each record. Check
   current replies, opt-outs, meetings, prior drafts, and recent touches before
   selecting any follow-up. Add new value. A booked meeting or opt-out supersedes
   a no-reply chase. A user-reported send remains unverified until source evidence
   supports it; do not resend to resolve uncertainty.
7. Stage only source-backed relationship deltas using the native contract.
   `confirmed_owner` means interaction owner, not identity or introduction.
   `canonicalId=null` preserves unresolved identity. `taskGate` uses the native
   enums, not dates for new packets. Put due times in provenance/checkpoint fields.
   Supply a draft native packet for each campaign with supported relationship
   deltas, including mortgage-partnerships. If no delta is supported, state that reason rather
   than invent an update. Every case still needs a recovery checkpoint with
   completed work, pending owner action, source/artifact hashes and unchanged holds.
8. Feed observed results back to Growth by campaign, segment, temperature, message,
   and variant. Keep delivery, reply, qualified reply, meeting booking, acceptance,
   attendance, application, funding, and suppression separate. Draft outcomes stay
   null until owner evidence exists. Counts and small samples do not prove lift.

## Handoffs And Recovery

The main workforce adapter owns generic state storage and transitions. It must
represent these domain milestones without installing a second state engine here:

| Milestone | Required evidence | Resume behavior |
| --- | --- | --- |
| research_ready | Dossier with source hashes and unresolved facts | Reuse unchanged evidence; refresh only stale inputs |
| qualification_ready | Fit, identity/contact distinctions, holds, owner action | Do not infer permission from a favorable score |
| prose_ready | Growth brief, reviewed internal draft or specific draft hold | Preserve message/variant IDs and draft state |
| packet_staged | Native packet, run ID, exact artifact hash, aliases | Reuse immutable staged packet |
| awaiting_owner_receipt | Notification status and pending owner task | Reconcile existing receipt before retrying notification |
| partially_committed | Owner receipt with per-alias pending nominations | Track committed and pending aliases separately |
| graph_committed | Trusted owner receipt for all intended aliases | Keep unresolved identity and suppressions intact |
| outcome_reconciled | Owner-backed event IDs and timestamps | Deduplicate feedback; never count a draft as a send |

Persist the last completed handoff, pending operation, campaign/alias keys, raw
source and artifact hashes, `schemaVersion`, stable `runId`, packet hash,
message/variant IDs, event cursor, owner task, receipt path/hash, unresolved
facts, suppression snapshot, and exact next action. Save before an operation
whose response could be lost. Interruption must not rerun completed research,
create another worker, choose a new run ID, resend, or mark a missing receipt as
success. Changed packet content under an existing run ID is a conflict, not a
retry: native idempotency is keyed by `schemaVersion + runId`, not packet hash.
Keep the original artifact; changed facts need a separately reviewed delta.

Recheck receipt provenance against the owner task and the same staged artifact.
The API returns `{receipt: {...}}` with `schema_version`, `run_id`, `observed_at`,
`audit_id`, `source_record_ids`, counts, per-alias `results`, `idempotent`, and
four zero external-action counters. Results may be `relationship_updated`,
`identity_pending_relationship_updated`, or `awaiting_campaign_nomination`.
An identity-pending relationship update can be committed without resolving the
identity. Pending nominations are not committed updates. Compare suppression
against the prior trusted owner snapshot; a receipt cannot clear an existing hold.
An acknowledgement, valid packet, audit-looking ID, or passing local validator
does not prove a live commit. The validator cannot authenticate its input receipt.

## Executable Acceptance

Use the distribution's synthetic consumer suite for installation, artifact, ratio, assignment and recovery checks. Native CRM parser integration is recipient-specific and is not exercised by the portable demo. For real workflow testing, provide raw synthetic facts to a fresh agent and retain expected invariants separately. Require actual dossiers, briefs, drafts or explicit holds, packets and checkpoints, not just summaries.

From the skill directory, run:

```bash
python3 -B -m unittest discover -s ../../../../tests -v
python3 -B scripts/validate_relationship_handoff.py /path/to/packet.json --schema-path /path/to/recipient-crm/lib/relationship-updates.ts
python3 -B scripts/validate_relationship_handoff.py /path/to/packet.json --schema-path /path/to/recipient-crm/lib/relationship-updates.ts --owner-receipt /path/to/receipt.json
```

Native mode requires Node with TypeScript type stripping (tested on Node 25).
It imports only the pure parser and its local date helper, never the live API.
Choose only a trusted owner-controlled parser path. No hard-coded machine path
is required by the validator. Tests use `RELATIONSHIP_SCHEMA_PATH` to enable
native integration; without it they explicitly skip those tests.

For a portable offline check, explicitly use `--allow-minimal` without a schema
path. The built-in fallback accepts a conservative modern authoring subset:
it does not emulate native coercion, truncation, or legacy date normalization.
It reports `minimal_contract_only`, not canonical schema validation. A supplied
parser failure never falls back silently. `--schema-path` selects the actual
owner's pure TypeScript contract, not a JSON Schema substitute. No second schema
or third-party Python dependency is maintained here. Neither mode grants owner
or send authority.

Exit 0 means structural checks passed, 1 means rejected, and 2 means invalid CLI
usage. Output is a small JSON receipt without raw private values. Every success
reports `owner_authenticity_verified=false` and `graph_commit_verified=false`.
`receipt_state=complete` means internally consistent input, not live DB verification.
