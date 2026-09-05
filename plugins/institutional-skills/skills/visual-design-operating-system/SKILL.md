---
name: visual-design-operating-system
description: Canonical cross-medium visual design, art direction, design taste, brand expression, house document systems, UI/UX polish, Figma-quality mockups, deck design, document and letter layout, report/dashboard aesthetics, social/content creative, image/video direction, and "make this look better" skill. Use when the user asks for an expert designer, Figma-level design, visual polish, a stronger look, design themes, brand systems, house-style document output, product UI, UX, decks, PDFs, letters, posts, images, videos, or any artifact that needs to be visualized.
---

Public distribution: resolve `{SKILLS_ROOT}` to this plugin's `skills/` directory. Recipient bindings and tool availability are explicit; read [portability](../../PORTABILITY.md). No host, CRM, sending, or trading access is implied.

# Visual Design Operating System

## Quick Reference

### What It Does
- Acts as the canonical design front door for visual quality across mediums: UI, UX, decks, documents, letters, reports, dashboards, landing pages, social/content assets, images, video, brand systems, and design critique.
- Translates loose asks like "make this look better", "be an expert designer", "Figma-quality", "less AI", "stronger deck", or "polish the UI" into a medium-specific design workflow.
- Routes execution to existing skills and tools instead of creating a duplicate design stack.

### Entrypoints
- Read this SKILL.md first.
- Use `references/recipient-document-system.md` whenever the user asks for a
  house document, branded research PDF, investment memo, family-office report,
  recipient organization letter, or an explicitly named house brand variant.
- Use `references/cross-medium-design-brief.md` when the visual direction is underspecified.
- Use `references/medium-playbooks.md` to choose the correct medium workflow.
- Use `references/interface-detail-and-reconstruction.md` for UI audits, screenshot-to-interface work, responsive reconstruction, interaction polish, and evidence-backed visual iteration.
- Use `references/design-frontend-execution.md` for frontend implementation,
  React/Next.js, Tailwind, motion, accessibility, Figma-to-code, and editable
  Blender asset pipelines. It maps retained specialist sources to this owner
  and requires working interactions, source editability, and rendered evidence.
- Use `references/hyperframes-video-production.md` when a video request should become a deterministic HTML/CSS/motion composition rendered to MP4, especially for product, website, mortgage-partnerships, deck, content, caption, or overlay workflows.
- Use `references/blender-figma-routing.md` for pitch decks, 3D, motion,
  cinematic scenes, compositing, product visualization, VFX, or any request
  where the choice between Figma and Blender matters.
- Use `references/quality-gates.md` before delivery.
- Use `references/source-map.md` for provenance and watchlist references.

### Inputs / Outputs
- Inputs: user request, target artifact, current brand/source material, audience, medium, constraints, files, screenshots, design URLs, repo conventions, and any existing visual system.
- Outputs: design direction, artifact changes, medium-specific visual system, critique, Figma/image/video prompt, deck/report layout, UI implementation guidance, or QA findings.

### Dependencies / Tooling
- Support skills: `figma`, `figma-implement-design`, local safe-mode Blender
  MCP, `imagegen`, `sora`, HyperFrames-style video production when installed or
  explicitly selected, `ethical-supersuader`, `growth-operating-system`,
  `screenshot`, `playwright`, `spreadsheet`, and relevant
  document/presentation tools.
- Use the Figma MCP/plugin when the user provides Figma links or asks for Figma implementation.
- Use image/video generation tools only when the artifact actually needs generated media.
- For branded house documents, start from
  `assets/research-platform-dfh-document-template.html` (not bundled; recipient resource required), use
  `assets/research-platform-dfh-document.css` (not bundled; recipient resource required), render with
  `scripts/render_document_pdf.py`, and run
  `scripts/audit_document_output.py --final` (not bundled; recipient resource required) before delivery.

### Test Command(s)

From this skill directory, run the portable consumer suite:

```bash
python3 -B -m unittest discover -s ../../../../tests
```

### Invariants
- Do not hardcode a permanent the principal-specific aesthetic into this skill.
- Derive visual direction from the user's ask, the artifact's job, the audience, the medium, and any existing brand/source system.
- Keep this as the design router and taste layer; do not fork growth, prose, Figma, image, video, or presentation ownership.
- Do not bulk-import external skill packs without license/provenance review.
- Prefer one high-quality design system per artifact over many style presets.

## Purpose

This skill exists so visual work compounds instead of scattering across one-off prompts. It is not a fixed brand style. It is a design operating layer that decides what kind of designer is needed, what constraints matter, which existing skill/tool should execute, and what quality bar must be met before shipping.

Use it whenever the deliverable has a visible surface.

## Ownership

This skill owns:

- visual taste and art direction
- UI/UX polish and critique
- cross-medium design consistency
- design briefs and design direction
- brand expression and design-system judgment
- deck, report, dashboard, document, letter, and content layout judgment
- generated image/video art direction
- anti-generic and anti-AI-slop visual review

This skill does not replace:

- `growth-operating-system` for offer, funnel, audience, conversion, and campaign metrics
- `ethical-supersuader` for sentence-level prose, voice, persuasion ethics, and beautiful writing
- `figma` for Figma MCP fetch, screenshot, variables, asset, and implementation mechanics
- `imagegen` for final image generation/editing
- `sora` for final video generation/remix
- `investment-management`, `universal-banker`, or other domain skills for business judgment

## Routing

Use this decision order:

1. If the request is mostly about visual quality, design, UI/UX, art direction, deck look, report layout, social creative, or generated media, this skill is decision owner.
2. If the request is mostly about growth or conversion, use `growth-operating-system` as decision owner and this skill as the visual layer.
3. If the request is mostly about prose quality, use `ethical-supersuader` as decision owner and this skill for layout/format/presentation.
4. If the request starts from a Figma URL, use `figma` for source extraction and this skill for design judgment.
5. If the request starts from an image/video asset, use `imagegen` or `sora` for execution and this skill for direction and critique.
6. Pitch decks, UI, 2D layouts, typography, storyboards, and brand systems
   default to Figma or document/presentation tools. Use Blender only for
   original 3D, spatial, motion, VFX, compositing, or rendered assets that are
   then placed into the deck or design.
7. If the request needs a finished, repeatable MP4 from a website, product brief, PR, article, existing talking-head clip, caption layer, or designed overlay, read `references/hyperframes-video-production.md` before choosing generated video or ad hoc editing.
8. If the request names a house document brand, use the house document reference
   and assets in this package. Do not infer the document system from unrelated
   application-theme or code repositories.
9. Keep academic submissions in conventional venue-appropriate LaTeX unless the
   user explicitly asks for a branded edition. House styling may be used for a
   companion article or internal edition, not silently imposed on the academic
   manuscript.

## Workflow

1. Classify the medium.
   - UI/product, deck, document/letter, dashboard/report, landing page, social/content, brand system, image, video, or critique.
2. Find the source of truth.
   - Existing brand, current product UI, Figma file, deck template, prior post, client material, investment memo style, or user-provided preference.
3. Define the design job.
   - What must the artifact make easier to understand, believe, decide, buy, remember, or act on?
4. Select the visual register.
   - Choose a direction based on audience, stakes, density, medium, and context. Avoid defaulting to a fashionable style.
5. Execute through the right support skill/tool.
   - Build the artifact, prompt generated media, revise a deck, implement UI, or create a critique.
6. Run the quality gate.
   - Use `references/quality-gates.md` before returning final work.
   - For implemented UI, compare fresh screenshots at representative mobile, tablet, laptop, and desktop widths. Fix structural mismatches before decorative ones.
   - For branded house PDFs, inspect the first page, the densest table or chart
     page, and the final page. The output audit must pass with no local URLs,
     browser chrome, internal status labels, font drift, or broken page
     geometry.
7. Capture reusable learning.
   - If a visual pattern should recur, write it as an artifact-specific note or design-system source, not as a global hardcoded preference in this skill.

## Design Principles

- The artifact's job comes before decoration.
- Taste is constraint selection: audience, medium, brand, density, stakes, time, and available assets.
- Strong design removes friction before it adds style.
- Visual hierarchy should make the next action obvious.
- Typography, spacing, color, imagery, and motion must work together; none should carry the whole design alone.
- Generic polish is not enough. Give each artifact one clear visual point of view.
- A beautiful artifact that weakens truth, readability, accessibility, or decision quality fails.

## Quality Standards

Before delivery, verify:

- The hierarchy is clear within five seconds.
- The strongest content is visually dominant.
- The medium's constraints are respected.
- Text fits its containers across likely viewport/page sizes.
- Color, contrast, spacing, and typography are coherent.
- Images or media support the actual subject instead of acting as filler.
- Repeated elements share a system.
- The result avoids generic AI tells unless the user explicitly asks for that style.
- Accessibility and legibility are not sacrificed for aesthetics.
- The final artifact can be used by a human without explanation text inside the UI.

## References

- `references/recipient-document-system.md`
- `references/cross-medium-design-brief.md`
- `references/blender-figma-routing.md`
- `references/hyperframes-video-production.md`
- `references/interface-detail-and-reconstruction.md`
- `references/design-frontend-execution.md`
- `references/medium-playbooks.md`
- `references/quality-gates.md`
- `references/source-map.md`
