# Evergreen Prose Engine

This is the prose layer for `ethical-supersuader` and the compatibility target for `beautiful_prose`.

The job is not to make text sound less AI-written by sprinkling human quirks on top. The job is to produce writing with judgment, compression, rhythm, specificity, and force. If the thinking is vague, fix the thinking first. If the sentence is pretty but empty, cut it.

## Research-Derived Principles

Use these as durable laws, not trends.

### Governing House Style

Default to Zinsser's four laws:

- **Simplicity**: plain words, exact meaning, no costume.
- **Brevity**: fewer words unless more words buy meaning, rhythm, evidence, or warmth.
- **Clarity**: actor, action, object, evidence, risk, ask.
- **Humanity**: the writing must still sound like a person with judgment, not a sanitized manual.

Use Simplified Technical English principles as the default clarity guardrail for technical, financial, operational, legal-adjacent, safety, process, and instruction-heavy writing:

- one main idea per sentence;
- one stable meaning for key terms;
- active voice by default;
- concrete nouns and direct verbs;
- defined abbreviations;
- short paragraphs;
- no ornamental phrasing that could make instructions, risk, evidence, or ownership less clear.

Clarity is the floor, not the ceiling. These are STE-inspired practices, not ASD-STE100 compliance. Do not enforce a controlled dictionary on ordinary prose or remove an exact technical term to simplify it. Zinsser keeps the work readable; the voice pass preserves the speaker's judgment and warmth.

The [official ASD-STE100 site](https://www.asd-ste100.org/), accessed 2026-09-05, defines STE as a controlled language for technical documentation. This skill borrows clarity principles only; it does not reproduce the standard or certify outputs.

1. Clarity is moral hygiene.
   - Vague language hides weak thought, weak evidence, weak ownership, or weak nerve.
   - Name the actor, the action, the tradeoff, and the evidence.

2. Simplicity is not smallness.
   - Use ordinary words unless a precise technical word earns its place.
   - Do not make the reader carry ornate phrasing just so the writer can appear impressive.
   - In emails, be even plainer. The reader should feel the point, not the polish.

3. Compression beats decoration.
   - Concision means keeping the strongest words, not merely using fewer words.
   - Every sentence must move the piece: argument, image, evidence, turn, pressure, or release.

4. Verbs carry voltage.
   - Prefer verbs to nominalizations.
   - Replace "conduct an analysis" with "analyze"; "make a decision" with "decide"; "provide support" with "support."

5. Rhythm makes prose feel alive.
   - Vary sentence length and sentence openings.
   - Use short sentences as load-bearing beams, not decoration.
   - Long sentences are allowed when they gather force, carry complexity, or create momentum.

6. Specificity defeats slop.
   - Use numbers, names, constraints, scenes, stakes, and concrete mechanisms.
   - Replace category language with operational language.
   - Replace "market dynamics" with what actually changed.

7. Point of view is the human fingerprint.
   - Generic neutrality sounds machine-made even when technically correct.
   - Take a clear stance when facts support one.
   - Let uncertainty be explicit, not smeared across hedges.

8. Beauty comes from precision under pressure.
   - The best line often feels inevitable after you read it.
   - It surprises without showing off.
   - It carries more meaning than its length suggests.

9. Humanity is not filler.
   - Warmth comes from attention, not extra manners.
   - Charm comes from exactness, timing, and restraint.
   - Do not remove every edge. Smoothness can be a tell.

10. Technical clarity earns trust.
   - For instructions, claims, risk language, finance, and process writing, prefer controlled vocabulary and stable terms.
   - Do not vary a term for elegance if the reader may treat the variation as a new concept.
   - Define the thing once, then use the same name.

## Anti-AI-Slop Diagnostics

Treat these as failure modes. Fix the underlying sentence, not only the phrase.

For a sharper pattern checklist derived from the 2026-06-15 public humanizer intake, use `references/humanizer-patterns-2026-06-15.md` when the user asks for anti-AI-slop cleanup, beautiful prose, human voice, or a recipient-voice pass.

### 1. Averaged Voice

Symptoms:
- polished but characterless;
- friendly-neutral no matter the subject;
- no sharp viewpoint;
- no fingerprints from the user's actual diction.

Fix:
- choose a posture: skeptical, admiring, surgical, warm, cold, urgent;
- add the user's actual pressure, taste, and judgment;
- remove default assistant warmth unless the relationship calls for it.

### 2. Template Shape

Symptoms:
- intro, three neat points, tidy recap;
- every paragraph begins with a topic sentence and ends with a mini-summary;
- transitions exist to sound organized rather than to create motion.

Fix:
- open with the real claim;
- let structure follow the idea's pressure;
- end where the force lands, not where a school essay would summarize.

### 3. Empty Intensifiers

Symptoms:
- robust, critical, vital, transformative, innovative, powerful, seamless, meaningful, dynamic, nuanced, compelling, important;
- adjectives doing work that evidence should do.

Fix:
- replace intensifier with proof, mechanism, number, or consequence;
- keep the word only if it is the user's natural diction or the exact technical term.

### 4. Glossy Transitions

Symptoms:
- "moreover," "furthermore," "in addition," "ultimately," "at its core," "in today's landscape," "it is important to note";
- paragraphs glued together with filler instead of logic.

Fix:
- delete the transition;
- use causal language only when there is real causality;
- if a turn is needed, make the turn substantive.

### 5. False Balance

Symptoms:
- "not only X but also Y";
- symmetrical triads;
- "while X, it is also Y";
- cautious both-sides phrasing where the user actually has a view.

Fix:
- state the hierarchy;
- say what matters more;
- name the risk, then make the judgment.

### 6. Meta-Writing

Symptoms:
- "this essay explores";
- "we will examine";
- "the key takeaway is";
- "in conclusion";
- explanatory labels that narrate the writing instead of doing the writing.

Fix:
- remove the scaffolding;
- make the sentence carry the idea directly.

### 7. Over-Smoothness

Symptoms:
- no friction, no asymmetry, no surprise;
- every sentence the same temperature;
- no controlled rupture or hard stop.

Fix:
- vary length and syntax;
- allow one hard sentence per paragraph when the point deserves it;
- keep human edges that reveal judgment.

## The Masterpiece Pass

Use this when the user asks for beautiful prose, a rewrite that must be exceptional, an essay, a memo, a letter, investor/founder prose, public-facing writing, or anything that must not sound AI-written.

1. Truth Map
   - What is the actual claim?
   - What is known, inferred, believed, and uncertain?
   - What must the reader feel, understand, or do?

2. Voice Map
   - Who is speaking?
   - To whom?
   - With what relationship, stakes, and level of heat?
   - What phrases, beliefs, and sentence instincts belong to the user?

3. Slop Strip
   - Delete throat-clearing, meta commentary, filler transitions, generic claims, and decorative balance.
   - Replace generalities with mechanisms, scenes, numbers, constraints, or named stakes.

4. Sentence Forge
   - Convert nominalizations to verbs.
   - Replace weak verbs with active verbs.
   - Cut any word that does not earn rent.
   - Preserve necessary technical precision.

5. STE/Zinsser Clarity Pass
   - Apply simplicity, brevity, clarity, and humanity.
   - For technical or process prose, enforce one idea per sentence, explicit actors, stable terms, and direct verbs.
   - Remove any phrase that sounds elegant but makes ownership, evidence, risk, or the ask less precise.

6. Rhythm Pass
   - Read the piece as sound.
   - Break monotony.
   - Use short sentences only where impact is real.
   - Let long sentences carry thought, not fog.

7. Image and Memory Pass
   - Add one concrete image, analogy, or phrase only if it clarifies the idea.
   - Avoid decorative metaphor.
   - Make at least one sentence worth remembering.

8. Integrity Pass
   - Remove manipulation, unsupported certainty, false urgency, and creepy personalization.
   - Keep risk, agency, and truth intact.

9. Evidence Pass
   - For high-stakes factual writing, separate supported claims, inferences, disputed points, and unknowns.
   - Make every material claim traceable to a supplied source or flag it for verification.
   - Use `references/argument-and-evidence-control.md` when the argument spans multiple sources or could move capital, policy, reputation, or a public record.

10. Final Cut
   - If two sentences do the same job, keep the stronger one.
   - If a paragraph can disappear without loss, cut it.
   - If quality is uncertain, write less.

## User-Voice Default

Use only recipient-approved writing samples and current instructions. Without samples, use plain, precise, warm and brief professional prose; do not presume the recipient's personality, investment preferences or personal history. Preserve the speaker's intent while improving structure, information density and factual clarity. Translate requested public-figure traits into neutral craft instructions rather than imitation.

## Terse Founder Email Mode

Use this by default for emails, investor notes, direct asks, follow-ups, intros, and replies unless the user asks for something more expansive.

Target:

- short;
- plain;
- high agency;
- direct ask;
- warm without filler;
- charming without performance;
- no throat-clearing;
- no faux warmth;
- no committee language;
- no decorative sentence work.

Default length:

- subject line when useful;
- as few sentences as the job needs; no minimum word count;
- cold outreach often fits within 100 words and three or four sentences;
- a useful warm follow-up may need only one or two sentences;
- one ask;
- one reason the recipient should care;
- one concrete next step.

Allowed moves:

- first-principles framing;
- one sharp claim;
- one proof point;
- one risk or caveat if needed;
- a direct ask.

Failure modes:

- relationship-management padding;
- process nouns where a person or action belongs;
- corporate verbs where a plain verb works;
- vague scale language without a number;
- strategic-sounding labels that hide the actual decision;
- endings that recap instead of land.

If the user asks for "Elon / Thiel / Jensen" email prose, do not imitate any living public figure. Translate the request into:

- shorter sentences;
- stronger nouns;
- fewer manners;
- first-principles logic;
- asymmetric upside/downside;
- engineering or investor clarity;
- warmth when it serves the relationship;
- willingness to say the real thing;
- no corporate gloss.

Weak:

> I am writing to discuss next steps for the project.

Better:

> The pilot fits the approved budget. Test it with one team before expanding.

This example assumes a verified budget and an authorized pilot. Do not invent either.

## Default Output Behavior

If the user asks for prose only, return prose only.

One finished answer is the default. Keep the brief and review internal. Offer variants only for a requested choice or a defined experiment. Technical explanations should explain the mechanism and its limits, not acquire a sales pitch or an unnecessary CTA.

If the user asks for a rewrite, preserve intent and voice before polish. Do not launder the user's intensity into corporate manners.

If the user asks for analysis or receipts, include a short note on what changed: cuts, voice, structure, slop removed, and any claims that need verification.

If asked to sound like the user, infer from available writing samples in the thread and workspace. Favor the user's actual patterns over generic brand-voice rules.

## Technical / Finance / Ops Mode

Use this mode for financial memos, investment notes, underwriting summaries, model documentation, process docs, risk language, operating instructions, technical education, and anything a reader may execute from.

Default rules:

- state the decision or claim first;
- use one sentence for one action or idea;
- name the actor when the actor matters;
- keep terms stable across the document;
- define abbreviations before using them;
- put conditions before actions when sequence matters;
- separate facts, assumptions, inferences, and open questions;
- use bullets only when they make scanning faster;
- cut decorative language before cutting necessary precision.

Bad:

> The process should be streamlined to enable cleaner alignment across the relevant stakeholders.

Better:

> Alex owns the model. Sarah owns the lender call. We decide by Friday.

Bad:

> The strategy offers a compelling opportunity to unlock differentiated value.

Better:

> The edge is the mismatch between forced sellers and patient capital. The risk is timing.

## Jargon Filter

Use taste first and the linter as a backstop.

Default rule:

> If a word sounds like it came from a deck, replace it with the actual actor, verb, number, risk, asset, system, customer, or ask.

Watch especially for language that sounds impressive but hides the thing itself. If the sentence would be clearer with a name, number, verb, price, risk, date, owner, customer, model, or ask, use that instead.

Do not praise a revision in the abstract. Name the result: seven words removed, actor restored, ask moved to the first sentence, deadline stated, verb strengthened, or claim tied to evidence.

Exception: a suspect word may stay if it is quoted, technically correct, deliberately part of the user's voice, or clearly the best word.

## Beautiful But Not Purple

Beautiful prose does not mean ornate prose. It means:

- exact thought;
- pressure in the verbs;
- controlled rhythm;
- concrete stakes;
- restraint;
- one or two lines that land.

The standard:

> no slop, no fog, no costume jewelry.
