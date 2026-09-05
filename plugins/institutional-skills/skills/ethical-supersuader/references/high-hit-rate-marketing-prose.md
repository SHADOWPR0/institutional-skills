# High-Hit-Rate Marketing Prose

Use this reference for Relationship OS, capital-partnerships, mortgage-partnerships, investor, founder, deal, landing-page, email, InMail, X/social, and follow-up copy.

The objective is a qualified positive response or useful next step. Opens and raw engagement are weak signals. Trust, relevance, proof, and a low-friction ask do the work.

## Ownership

- `growth-operating-system` owns audience, segment, offer, positioning, channel, campaign economics, measurement, and stop rules.
- `ethical-supersuader` owns prose, variants, proof discipline, voice, CTA phrasing, skeptical editing, and copy selection.
- Relationship OS owns canonical identity, relationship provenance, consent, suppression, touch history, reply state, and outcome state.
- Channel skills provide execution capability only after explicit authority. They do not own message strategy or prose.

This skill drafts. It does not send, activate campaigns, mutate contacts, clear suppressions, or infer consent.

## Message Brief

Build this compact brief from available context before drafting:

```yaml
recipient_segment: ""
relationship_temperature: cold | known | warm | active
verified_professional_signals:
  - fact_id: ""
    fact: ""
    source: ""
    observed_at: ""
role_and_seniority: ""
decision_altitude: company | department | team | individual
campaign_objective: ""
message_job: ""
offer_or_mechanism: ""
proof:
  - claim: ""
    source: ""
likely_objection:
  statement: ""
  status: fact | inference
channel: email | inmail | x | landing_page | other
cta: ""
compliance_and_suppression_state: cleared | blocked | unknown | not_applicable
prior_touches_and_replies: []
approved_voice: "the principal voice unless another voice is supplied"
```

One campaign objective. One job for the message. If a required fact is unavailable, write `unavailable`. Do not fill the gap with a guess.

Keep the brief internal unless a draft artifact or user request requires it. A routine reply does not need a visible form. Preserve the stated channel through the brief, draft, and receipt: an email remains `email`, including a referral or follow-up. Use `other` only for an actual unlisted medium. Unknown or blocked eligibility stays unchanged; drafting is never clearance to send.

## Signal Rules

Good personalization uses verified professional context:

- a stated company priority;
- a role change or operating mandate;
- a sourced transaction, product, hiring, financing, regulatory, or market event;
- a real prior exchange, introduction, mutual relationship, or response;
- a work product, public statement, or professional interest relevant to the offer.

Reject:

- generic praise;
- alma mater trivia with no business relevance;
- protected traits;
- wealth proxies;
- neighborhood, home value, family, health, religion, politics, or private-life inference;
- invented commonality;
- psychological profiling;
- a proposed introduction treated as a verified relationship;
- a role stereotype stated as fact.

The buyer lens may infer a professional priority from role and company evidence. Label it `inference`. Do not present it as known.

Keep attributed claims at the source's strength. A document gap does not establish a delay, lost revenue, or buyer frustration. A diligence question does not establish decision readiness. Use the verified fact; do not add a consequence or advance the relationship stage to sharpen the pitch.

## Decision Altitude

Match the value claim to the reader's level:

- Company: strategy, timing, revenue, cost, risk, capital, or competitive position.
- Department: mandate, use case, budget, operating constraint, or cross-functional result.
- Team: workflow, throughput, error rate, conversion, capacity, or handoff.
- Individual: work outcome, time, quality, control, learning, or career-relevant result.

Do not pitch tactics to an executive or abstract strategy to an individual contributor unless the context supports it.

## Internal Review Sequence

Run this sequence in one pass unless a high-volume or high-stakes task justifies separate agents.

1. Signal researcher
   - Extract only source-backed recipient, company, and relationship facts.
   - Attach source IDs and dates.
2. Buyer lens
   - State the likely professional priority and objection.
   - Label inference and name the evidence behind it.
3. Copy chief
   - Privately draft two or three materially different variants for marketing or outreach, then return one finished answer by default.
   - Show multiple variants only for a requested choice or a defined campaign experiment.
   - When comparing variants, change one major variable at a time: angle, proof order, CTA, or length.
4. Skeptical editor
   - Reject generic personalization, seller jargon, unsupported proof, premature meeting asks, excess length, AI cadence, and vague value.
5. Selection note
   - Select the strongest draft internally; do not append review narration to ordinary copy.
   - For an actual experiment, name the hypothesis and segment in the campaign receipt or requested selection note.

Do not spawn role-play agents for ordinary drafting. These are stable review functions, not celebrity personas.

Run the prose linter on the final copy, then make one silent judgment-based rewrite. Lint detects some weak patterns; it cannot establish sincerity, accuracy, voice quality, or higher response rates. Preserve useful technical terms and record justified warnings in benchmark or review receipts, not in the recipient's message.

## Channel Contracts

### Cold Email

Strong default, not universal law:

- often 100 words or fewer;
- often three or four sentences;
- subject usually four plain words or fewer;
- one message job;
- one relevant professional signal;
- buyer language, not seller vocabulary;
- one low-friction CTA;
- fully scannable on a phone.

Break the length default only when proof, regulation, relationship context, or a complex offer needs more room. Cut first. Keep only what improves comprehension or response quality.

Ask for interest, permission, or acceptance of a useful offer before defaulting to a calendar request. A meeting ask is valid when the relationship is warm, intent is evident, or the meeting itself is the natural next step.

### Warm or Relationship Email

- Use the actual relationship and prior exchange.
- Continue the existing conversation rather than restarting a sales script.
- Keep nuance or proof that the relationship needs, even if the note runs longer.
- State the ask directly.
- Never use warmth to hide pressure.

### InMail

- Lead with a professional signal or real commonality.
- Show relevance to the person and organization.
- Give one brief value statement.
- Make the response easy.
- Treat profile views, company follows, activity, and role changes as research or timing inputs, not as personal familiarity.

### X and Social

- One idea per post.
- Write in the platform's natural rhythm.
- Use a real claim, observation, proof point, question, or point of view.
- No engagement bait, fake controversy, invented virality, or thread padding.
- X API and platform skills are execution capabilities. They do not replace this prose owner and do not authorize posting.

### Follow-Up

- Add a new fact, proof point, useful artifact, changed condition, or angle.
- A short bump is usually one or two sentences.
- Do not send empty `checking in` or `circling back` copy.
- If there is no new value, wait or send one brief close-the-loop note.
- Respect cadence, consent, suppression, and any explicit no.

### Landing Page

- One audience and one conversion job per page.
- Put the plain promise and mechanism before supporting detail.
- Place proof beside the claim it supports.
- Match the CTA to visitor intent and decision stage.
- Make the page scannable on mobile.
- Remove fake urgency, unsupported logos, invented testimonials, and generic superlatives.
- `growth-operating-system` owns offer, funnel, test, and metric. This skill owns the words.

## Variant Discipline

Variants must differ in one important way. Examples:

- business problem versus timing signal;
- quantified proof versus useful artifact;
- permission CTA versus interest CTA;
- terse executive frame versus slightly fuller operating frame.

Keep the recipient, offer, and segment constant. Otherwise the test cannot tell which change mattered.

Do not claim causality from a few sends. Compare variants within like segments and similar relationship temperatures. Record confounders such as sender, list quality, timing, prior contact, and offer changes.

## Message Draft Receipt

For Relationship OS or measured campaign drafts, return this compact record beside the copy:

```json
{
  "schema": "message_draft_receipt.v1",
  "message_id": "",
  "variant_id": "",
  "campaign": "",
  "channel": "",
  "segment": "",
  "relationship_temperature": "",
  "source_fact_ids": [],
  "provenance": [],
  "angle": "",
  "proof_used": [],
  "cta_type": "interest|permission|useful_offer|reply|meeting|other",
  "word_count": 0,
  "sentence_count": 0,
  "selection_hypothesis": "",
  "compliance_and_suppression_state": "",
  "outcomes": {
    "delivered": null,
    "reply": null,
    "positive_reply": null,
    "qualified_reply": null,
    "meeting_booked": null,
    "unsubscribe_or_suppression": null,
    "timestamp": null
  }
}
```

Drafting fills message metadata. CRM fills outcome fields. `null` means unknown, not false.

Store receipts beside draft artifacts when the workflow supports that. Do not append them to recipient-facing copy. Use `selection_hypothesis: null` when no experiment is planned. Counts describe the body only, excluding the subject, signature, receipt, and review notes; record the counting method for measured tests.

Treat opens as optional and weak because privacy systems distort them. Optimize for qualified positive replies and booked next steps. Delivery, reply, meeting, and suppression states must remain distinct.

## Final Gate

Reject or revise if any answer is yes:

- Could this personalization apply to almost anyone?
- Is any important claim unsupported?
- Does seller jargon replace the buyer's problem?
- Is the ask larger than the relationship or intent supports?
- Does the follow-up add nothing?
- Does the copy sound assembled, flattering, invasive, or desperate?
- Does the message contain more than one job?
- Is any protected or private-life inference doing persuasive work?
- Is a draft, send, delivery, reply, meeting, or suppression state mislabeled?

## Research Basis

Distilled on 2026-08-28. The studies guide defaults, not universal rules. Local segment performance outranks pooled benchmarks when the local sample is comparable and large enough to be useful.

On 2026-09-05, rechecked the Gong guide and Lavender benchmark at their original URLs. Retained the bounded defaults below. These vendor observational samples do not establish causal lift from this skill or guarantee performance in another audience. No additional package installed; prior access dates for sources not revisited remain unchanged.

- [Gong cold-email guide, 85M+ emails](https://www.gong.io/files/gong-guide-how-to-master-cold-email-get-the-data-backed-guide-based-on-85-million-emails.pdf), accessed 2026-08-28. Accepted: buyer language, high-intent prioritization, business personalization, concise mobile defaults, useful-offer or interest CTAs, and short follow-ups.
- [LinkedIn InMail analysis of 2022 Sales Navigator messages](https://www.linkedin.com/business/sales/blog/prospecting/data-on-sending-inmails-higher-acceptance-rates), accessed 2026-08-28. Accepted: research the person and organization, then ground outreach in current professional context.
- [LinkedIn Deep Sales Playbook](https://business.linkedin.com/content/dam/me/business/en-us/amp/sales-solutions/images/deep-sales-playbook/pdf/LinkedIn-Deep-Sales-Playbook---EN.pdf), accessed 2026-08-28. Accepted: sourced relationship paths, relevance, trust, and transparency.
- [Lavender 2026 Cold Email Benchmark Report](https://lavender.ai/blog/the-cold-email-benchmark-report) and [five benchmark takeaways](https://lavender.ai/blog/5-takeaways-from-our-latest-cold-email-benchmark-report), accessed 2026-08-28. Accepted: segment by department, industry, and seniority; match value altitude; design for mobile; prefer local comparable benchmarks.
- [X official skill discovery documentation](https://docs.x.com/tools/skill-md), accessed 2026-08-28. Accepted only as evidence that API capability and prose ownership are separate. No X API package or send authority is imported.
- [xAI Grok Build context implementation](https://github.com/xai-org/grok-build/blob/main/crates/codegen/xai-grok-agent/src/prompt/context.rs), accessed 2026-08-28. Accepted: stable role and persona instructions belong in model context. Applied here as bounded review functions, without celebrity imitation.
- [judicael-s/Copywriting-skill](https://github.com/judicael-s/Copywriting-skill), MIT, accessed 2026-08-28. Accepted as pattern evidence for critique before rewrite, proof provenance, customer language, and human voice. No package installed.
- [inerrata/brief](https://github.com/inerrata/brief), MIT, accessed 2026-08-28. Accepted as pattern evidence for brief-first work, one job per asset, proof over claims, and evals. No package installed.
- [erron-ai/marketing-skills](https://github.com/erron-ai/marketing-skills), accessed 2026-08-28. Accepted only as non-copying pattern evidence for shared marketing context and channel routing. The reviewed checkout did not provide the license file referenced by its README, so no code or text was copied.
- Community persona libraries, direct-response gists, `agency-agents`, and ClawFlows were rejected for installation. Their useful abstraction is already represented by bounded role, deliverable, and eval contracts. Persona theater and parallel copywriting owners add noise.
