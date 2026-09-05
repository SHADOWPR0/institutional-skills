# HyperFrames Video Production

Use this reference when a visual-design task should become a deterministic video artifact instead of a loose prompt for generated video.

## What This Adds

HyperFrames is useful because it treats video as code: HTML/CSS layout, motion timelines, captions, overlays, media, and rendering are authored as a repeatable composition and exported to MP4. That is a different job from Sora-style generative video or manual NLE editing.

Good local fits:

- mortgage-partnerships product, trust, process, or borrower education clips.
- Short social videos from a landing page, offer, blog post, or deck.
- Founder/investor update videos with controlled typography and motion.
- Website-to-video, product launch, feature reveal, and demo-adjacent reels.
- Captioned existing clips and designed talking-head overlays.
- Motion graphics for stats, headlines, logos, lower-thirds, and deck inserts.

## Routing

Prefer a HyperFrames-style workflow when the user wants:

- a finished MP4 from a website, product URL, script, deck, article, or brief;
- controlled typography, captions, data callouts, lower-thirds, or overlays;
- reproducible brand motion rather than one-off generated footage;
- a video artifact that should be iterated, linted, previewed, and re-rendered.

Do not use it when the user needs:

- live capture of a browser session or camera feed;
- avatar/lip-sync/talking-head generation from nothing;
- true video editing of existing footage such as cutting, retiming, recoloring, reframing, reordering, or audio replacement;
- live data pulled at render time.

If the task is still about art direction only, stay in this skill and produce the brief/storyboard. If the task asks to actually render, use the local HyperFrames CLI/support only after confirming dependencies and target output path.

## Workflow Map

Choose by input and intent:

- Product, SaaS, company, offer, or site being promoted: product-launch video.
- General website/site tour/social clip from a URL: website-to-video.
- Topic, article, or notes with no product being marketed: faceless explainer.
- GitHub PR or code change: PR-to-video.
- Existing talking-head clip with readable subtitles: embedded captions.
- Existing clip with designed lower-thirds/cards/callouts: graphic overlays.
- Short, unnarrated design-led motion piece: motion graphics.
- Anything longer, unusual, or not captured above: general video composition.

Ask one clarifying question when the split matters, especially product promo vs neutral topic explainer or product launch vs general site showcase.

## Production Contract

For repeatable renders:

- Bake data, copy, assets, and values into the composition before render.
- Avoid clocks, randomness, network calls, and live data during render.
- Keep root dimensions explicit, usually 1920x1080 or 1080x1920.
- Give every timed visual a start, duration, and track/layer decision.
- Register timelines as seekable, paused animation state owned by the renderer.
- Keep media playback under the framework rather than uncontrolled browser playback.
- Validate with lint/preview/snapshots before handing off a final MP4.

For brand work, first build a compact video design system: palette, type, motion language, scene grammar, caption treatment, overlay treatment, and audio/narration register.

## mortgage-partnerships And Content Use

Use the growth skill for audience, funnel, offer, CTA, and campaign logic. Use this skill for the visual system and production quality.

High-ROI mortgage-partnerships patterns:

- "How it works" process clips.
- Trust/credibility explainers.
- Deal update or broker-partner recap videos.
- Short educational content from mortgage/real-estate topics.
- Repurposed deck/report sections as social clips.
- Existing founder/talking-head video with captions and financial/process callouts.

Do not let the video engine invent regulated claims, borrower promises, rate quotes, underwriting guarantees, or legal/compliance language. The content owner must provide or approve those claims.

## Quality Gate

Before delivery, verify:

- The video has one clear job and one audience.
- The first 2 seconds explain why to keep watching.
- Captions are readable on mobile.
- Text does not collide with safe areas, logos, or subjects.
- The motion supports comprehension instead of adding noise.
- Any numbers, claims, screenshots, or product details have source provenance.
- The final output is either a previewable project, a rendered MP4, or a clear next-step handoff.

## Provenance

Source reviewed: https://github.com/heygen-com/hyperframes

Observed commit: `3f3293da8693f71aae5bd867fcff70080aab2454`

License observed: Apache-2.0.

Local integration decision: use as a production-pattern source and optional execution engine; do not bulk-copy its full skill pack into the canonical local skill library without a separate dependency, asset, and CLI review.
