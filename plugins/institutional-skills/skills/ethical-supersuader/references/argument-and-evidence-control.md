# Argument And Evidence Control

Use this reference for investment memos, banking materials, research papers, technical reports, public claims, rebuttals, diligence notes, and any draft where polished prose could hide weak evidence.

Do not use the full protocol for ordinary short emails. Match rigor to stakes.

## Core Model

```text
intent -> audience -> claim -> evidence -> boundary -> objection -> decision or ask
```

Writing quality cannot repair a broken argument. Build the argument first, then apply the evergreen prose engine.

## Source Boundary

Before drafting or reviewing, identify:

- canonical source files;
- allowed external sources;
- source date or version where it matters;
- prior drafts and notes that are context but not evidence;
- missing sources needed to support material claims;
- confidential facts that must not appear in the output.

Do not treat prior chat, model memory, generated summaries, or unlisted local notes as evidence. They may identify a question; they cannot prove the answer.

## Claim States

Label material claims internally as:

- `SUPPORTED`: a source directly supports the claim at the stated scope;
- `INFERRED`: the claim follows from evidence plus an explicit reasoning step;
- `CONTESTED`: credible sources or interpretations disagree;
- `UNSUPPORTED`: no adequate source is present;
- `OUT_OF_SCOPE`: the available packet cannot answer it.

Never promote background, methodology, workflow, or adjacent-domain evidence into direct empirical, causal, deployment, or outcome proof.

## Argument Spine

For a substantial draft, answer:

1. What decision, belief, or action should this writing support?
2. What is the main claim in one sentence?
3. What evidence carries the claim?
4. What is inferred rather than observed?
5. What boundary or limitation prevents overclaiming?
6. What is the strongest good-faith objection?
7. What changes if the objection is right?
8. What should the reader do next?

If any link is missing, name the gap. Do not bridge it with eloquence.

## Optional Claim Ledger

Use a compact ledger when the draft has many sources or material consequences:

| ID | Claim | State | Source anchor | Reasoning | Boundary | Draft location |
| --- | --- | --- | --- | --- | --- | --- |

Keep the ledger local unless the user asks to see it. The final prose should read naturally, not like a compliance form.

## Paragraph Logic Pass

Each paragraph should do one main job:

- state a claim;
- supply evidence;
- explain mechanism;
- qualify a boundary;
- answer an objection;
- move to a decision or ask.

Flag paragraphs that repeat a prior point, change subject without a real logical turn, cite evidence that does not fit the claim, or end with a summary that adds nothing.

Use transitions only when they name a true relation: cause, contrast, sequence, condition, or consequence.

## Adversarial Self-Review

Run a final independent pass that asks:

- Which sentence would a skeptical expert attack first?
- Which number, date, causal verb, superlative, or forecast needs a source?
- Does the draft confuse correlation, mechanism, and causation?
- Does a narrow sample support a broad conclusion?
- Is contrary evidence missing or dismissed too easily?
- Does the recommendation survive the strongest reasonable objection?
- Are uncertainty and downside stated in proportion to the evidence?

Separate findings into `supported by sources`, `requires verification`, and `reviewer-risk inference`.

## Output Rule

- Preserve the user's point of view when evidence supports it.
- Use citations or source notes in the requested format.
- Flag unsupported claims instead of quietly weakening them into fog.
- Keep caveats near the claim they qualify.
- State the decision or ask plainly.
- After the argument passes, apply the evergreen prose engine for compression, rhythm, voice, and force.

## Provenance

This reference distills portable, MIT-licensed argument-governance, evidence-review, logic-review, and clean-room self-review patterns from `yha9806/academic-writing-toolkit`, inspected at commit `cd7fbb5bd7dd1e9af3c9079e85a6af8e1c1b8ab0` on 2026-07-16. It does not install the upstream plugin or create competing writing skills.
