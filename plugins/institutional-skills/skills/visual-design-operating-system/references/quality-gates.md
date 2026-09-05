# Quality Gates

Run the relevant gate before presenting visual work as done.

## Universal Gate

- Purpose: the artifact's job is obvious.
- Hierarchy: the eye lands on the right thing first.
- Readability: text size, line length, contrast, and spacing are humane.
- Consistency: repeated elements use the same visual grammar.
- Specificity: imagery, icons, charts, and language fit the actual subject.
- Accessibility: color contrast, focus/interaction states, and touch targets are reasonable for the medium.
- Restraint: no unnecessary decoration, filler imagery, or generic AI flourish.
- Truth: visual emphasis does not exaggerate evidence, claims, or certainty.

## UI Gate

- Fresh screenshots were inspected at 375, 768, 1024, and 1440 CSS pixels, or the closest project-specific viewports.
- Layouts do not overlap, clip, or create unintended horizontal overflow.
- Buttons, inputs, menus, cards, tables, nav, and modals have stable dimensions.
- Loading, empty, error, hover/focus, selected, disabled, and success states are handled when relevant.
- Controls use familiar patterns and icons where possible.
- Interactive targets are large enough to use; compact icons may render small but keep a roughly 44 by 44 CSS pixel hit area on touch surfaces.
- Nested surfaces use coherent radii, padding, borders, and shadows; depth is deliberate rather than uniform.
- Numeric data uses aligned figures when comparison matters.
- Motion is interruptible, uses transform or opacity where possible, and honors reduced-motion preferences.
- Text does not require user instructions inside the UI to understand the workflow.
- The build and the repo's closest lint, typecheck, or test command pass when implementation changed.

## Reference Reconstruction Gate

- The source screenshot or mockup was decomposed into hierarchy, grid, typography, color, imagery, surfaces, states, and responsive behavior before implementation.
- The interface is real, accessible UI. A screenshot was not embedded as the page background.
- Visible text, assets, and interaction states are preserved when legible and appropriate.
- Comparison proceeds in this order: frame, major regions, primary message, primary visual system, repeated modules, controls, then decoration.
- One major mismatch category is corrected per iteration when possible, followed by a fresh screenshot.
- Relationship geometry, labels, and anchors remain attached when the viewport changes.

## Deck Gate

- Each slide has one dominant claim.
- Supporting visuals prove or clarify the claim.
- Titles, charts, labels, and source notes are legible at presentation size.
- The deck has a clear opening, flow, and closing ask.
- Appendix material is separated from decision-critical pages.

## Document / Letter Gate

- The recipient can scan the document and know why it matters.
- Page breaks and table widths are clean.
- Formality matches the audience and stakes.
- Visual emphasis helps the argument instead of creating noise.
- Signature, contact, attachments, citations, and next steps are easy to find.

## Report / Dashboard Gate

- Metrics define units, windows, and denominators.
- Initial sort/order makes the data easier to interpret.
- Charts answer a real question and tables support review.
- Alerts and exceptions are visually distinct from background context.
- The first screen/page makes the recommended action clear.

## Generated Media Gate

- The prompt specifies subject, medium, composition, lighting/style, aspect ratio, and usage context.
- Any text inside the image/video is minimized or handled separately when reliability matters.
- The result is not just mood; it contributes to comprehension, persuasion, inspection, or memory.
- Source assets, rights, and likeness constraints are respected.
