# Interface Detail And Reconstruction

Use this reference for web and product UI audits, screenshot-to-interface work, redesigns, responsive repair, and final interaction polish.

## Choose The Mode

- `AUDIT`: inspect and score an existing interface without changing source.
- `DIRECTION`: turn a loose request into an approved visual system and acceptance tests.
- `RECONSTRUCT`: implement a supplied screenshot, mockup, or generated concept as real UI.
- `POLISH`: improve hierarchy, typography, surfaces, states, motion, and responsiveness without changing the product model.

Do not turn these modes into separate global skills. This skill remains the owner.

## Evidence-Backed Audit

1. Identify the framework, style system, component library, fonts, tokens, and current breakpoints.
2. Start the app with its existing command. Record build failures as prerequisites, not visual findings.
3. Capture fresh screenshots at 375, 768, 1024, and 1440 CSS pixels, or project-specific equivalents.
4. Check horizontal overflow, clipped text, contrast, focus visibility, touch targets, missing states, and unstable dimensions.
5. Read the source behind each suspected problem. Every finding needs a screenshot observation or file-and-line anchor.
6. Rank changes by user impact: task failure, comprehension, hierarchy, responsive integrity, interaction, then decoration.

Avoid vague verdicts. Replace "feels generic" with an observable fact such as: every section uses the same centered heading, equal card row, and identical radius, so no section has a distinct job or hierarchy.

## Visual Direction Contract

Before a broad redesign, define:

- identity: one sentence tying the visual character to the product, audience, and stakes;
- hierarchy: what the eye should see first, second, and third;
- color roles: background, surface, text, muted text, accent, state colors, and verified contrast pairs;
- typography: families, fixed type tokens, line heights, weight budget, wrapping rules, and fallback behavior;
- spacing and density: base spacing unit, section rhythm, container width, and compact versus expansive regions;
- surfaces: radius relationships, border use, shadow logic, texture, and elevation levels;
- imagery and icons: subject rules, crop behavior, stroke/fill consistency, and rights constraints;
- motion: purpose, duration bands, easing, interruption behavior, and reduced-motion fallback;
- signature treatment: one subject-specific visual or interaction that earns attention;
- acceptance checks: three to seven facts that can be verified from screenshots, DOM inspection, or tests.

Use explicit user approval before replacing a mature brand system or performing a broad visual rewrite.

## Screenshot-To-Interface Reconstruction

### 1. Inspect Before Coding

Extract what is visible and mark what is uncertain:

- exact text where legible;
- page frame, content width, outer padding, and section order;
- grid, alignment, dominant regions, and continuation below the first viewport;
- type roles, sizes, line heights, weights, and wraps;
- color roles, borders, shadows, radii, imagery, and icon treatment;
- controls, states, likely interactions, and responsive failure points;
- dense or spatial systems whose labels, paths, or anchors must scale together.

Do not invent details that the source already answers. Do not claim exactness where the image is ambiguous.

### 2. Build Real UI

- Reuse the project's existing components, tokens, and dependencies where suitable.
- Build structure with HTML, CSS, and existing primitives. Never use the reference screenshot as the page background.
- Keep responsive content in real layout systems. Reserve absolute positioning for intentional decoration or a coherent scaled coordinate plane.
- Use one coordinate model for connected diagrams, labels, markers, and paths so anchors do not drift.
- Preserve accessible semantics, keyboard use, focus states, and readable fallbacks.

### 3. Compare In The Right Order

After each meaningful pass, capture a new screenshot and compare:

1. page frame and background;
2. major regions and their proportions;
3. primary message, line breaks, and action placement;
4. primary image, chart, diagram, or product surface;
5. repeated modules and internal rhythm;
6. controls, states, and trust details;
7. decoration and microdetails.

Fix one major mismatch category at a time when possible. Structural changes can invalidate surface polish, so structure comes first.

## Interface Details That Compound

### Geometry And Surfaces

- For nested rounded surfaces, derive the outer radius from the inner radius plus the surrounding inset. Eyeball the result and correct optically.
- Keep a small, named radius system. Do not apply one radius to every object.
- Use borders when they clarify separation. Use restrained layered shadows when depth matters. Do not stack both by reflex.
- Align adjacent titles, values, controls, and actions across repeated modules.

### Typography And Data

- Keep body copy readable and constrain line length.
- Use balanced or pretty wrapping only when it improves real text; inspect the result at every target width.
- Use tabular figures for tables, prices, counters, timestamps, and changing metrics when alignment helps comparison.
- Keep letter spacing at zero unless an existing design system requires otherwise.
- Do not scale type continuously with viewport width. Use stable tokens and deliberate breakpoint changes only when required.

### Interaction

- Make the visible control and its hit area distinct: a small icon can sit inside a larger invisible target.
- Provide hover, focus-visible, active, disabled, loading, empty, error, and success states when the workflow can reach them.
- Prefer transitions for interruptible state changes. Use keyframes for staged, finite sequences.
- Animate transform and opacity where possible. Avoid layout-triggering animation of top, left, width, or height.
- Remove `transition: all`; name the properties that should move.
- Honor `prefers-reduced-motion` and keep motion subordinate to comprehension.

### Responsive Behavior

- Use the project's existing breakpoints before inventing new ones.
- Start from the smallest supported width and add space deliberately.
- Stack or simplify dense modules before labels, controls, or geometry overlap.
- Preserve the primary task and action on mobile; collapse secondary context without making it undiscoverable.
- Verify real content, longest labels, zero states, error states, and large numbers. Placeholder-perfect layouts are not proof.

## Exit Evidence

Before declaring the interface done, provide or retain:

- passing build and relevant lint, typecheck, or tests;
- fresh screenshots at target widths;
- no unintended overflow or overlap;
- a short list of corrected structural mismatches;
- any acceptance check that remains unmet;
- source and license notes for external assets or adapted patterns.

## Provenance

This reference distills portable, MIT-licensed process ideas from Unslop, Make Interfaces Feel Better, and Taste Skill, inspected on 2026-07-16. Exact repositories, commits, and use boundaries are recorded in `source-map.md`.
