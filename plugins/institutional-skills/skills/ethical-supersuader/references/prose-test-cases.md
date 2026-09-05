# Prose Quality Test Cases

Use these for spot checks after modifying the prose engine.

## 1. AI Slop Removal

Prompt:

```text
Rewrite this so it no longer sounds AI-written:
In today's fast-paced landscape, it is important to note that robust agentic systems can unlock transformative outcomes across a wide range of workflows.
```

Expected:

- Removes filler setup.
- Replaces generic intensifiers with concrete mechanism or asks for missing specifics.
- Names actor, action, and consequence.
- Does not add fake slang, errors, or casual filler.

## 2. the principal Voice, Edited

Prompt:

```text
Make this sound like me, but as if I had a brutal editor:
we need all the skills reachable everywhere, no bloat, keep the good stuff, sync local and drive, and show receipts.
```

Expected:

- Preserves high agency and directness.
- Keeps "no bloat," "sync," "receipts," and local-first operating logic.
- Removes typos and sprawl.
- Does not become generic executive prose.

## 3. Investor Note

Prompt:

```text
Write a short investor note explaining why this early company deserves one serious look. Facts: founder has lived the problem, customers are pulling it into budget, product starts narrow but could own a larger workflow. Risk: early and not fully de-risked.
```

Expected:

- Honest risk framing.
- Calm conviction.
- Specific thesis.
- No hype words without proof.
- Direct ask or final line.

## 4. Masterpiece Pass

Prompt:

```text
Turn this rough idea into a short public note that lands:
Most teams do not need more AI tools. They need fewer broken loops.
```

Expected:

- Rebuilds, not merely polishes.
- Uses concrete stakes.
- Varies rhythm.
- Produces at least one memorable line.
- Ends without a school-essay recap.

## 5. Linter Smoke Test

Command:

```bash
python3 scripts/prose_linter.py references/prose-test-cases.md
```

Expected:

- The linter may flag intentionally bad prompt text.
- It should run without crashing.
- Use judgment rather than blindly obeying linter output.
