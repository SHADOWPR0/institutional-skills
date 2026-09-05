# Design and Frontend Execution

Use this reference when the deliverable is an implemented interface or an
editable design-to-code/3D asset handoff. The design owner remains
`visual-design-operating-system`; prose belongs to `ethical-supersuader`, and
offer/channel/conversion judgment belongs to `growth-operating-system`.

## Choose the Work, Then the Tool

Read the current product, source files, design tokens, components, dependencies,
and user journey before choosing a stack. Keep an existing healthy framework.
For a small standalone artifact, native HTML/CSS/JS can be sufficient; React,
Next.js, Tailwind, and GSAP are capabilities, not mandatory dependencies.

| Request | Execution support | Required result |
| --- | --- | --- |
| React component or app | `react-best-practices`; existing component library | Semantic components, explicit state, measured bundle/network behavior |
| Next.js app | `nextjs`; project's installed-version documentation | Correct server/client boundary, protected secrets, loading/error/empty states, tested routes |
| Tailwind interface | `tailwind-patterns` or installed-version support | Existing tokens/breakpoints reused; no second style system |
| Animation | `gsap`, Figma motion support when relevant | Purposeful motion, lifecycle cleanup, reduced-motion alternative, no scroll trap |
| Screenshot reconstruction | `image-to-code`; Figma design context when available | Source-matched geometry/assets and a rendered comparison, not a plausible substitute |
| Responsive/accessibility work | `frontend-responsive-ui`, `accessibility`, `playwright` | Keyboard/focus/labels/errors, reflow, contrast and functional mobile states |
| Editable design system | Figma create/use/library/design-to-code tools | Components/variants, scoped variables, auto-layout, source node IDs and implementation mapping |
| Product/spatial/3D asset | Blender CLI or connected safe-mode MCP | Editable `.blend`, materials/lights/camera, original render and optimized delivery asset |

Find support packages through the global resolver/index by name and task. Load
only the relevant sections. Retained source packages are not competing owners,
and an installed connector does not prove a working account or executable.

## Source Adjudication

The following are source inputs, not unconditional style directives. Preserve
their originals and provenance; use the full inventory for current paths/hashes.

| Source | Useful contribution | Do not promote as a default |
| --- | --- | --- |
| `taste-skill` | Audience-first design; existing-system fit; audit before redesign | Arbitrary variance/motion scores or installing a new framework for appearance alone |
| `gpt-tasteskill` | Grid/spacing checks and coordinated motion | Random style selection, mandatory GSAP, mandatory animation, viewport-sized text |
| `soft-skill` | Consistent materials, legibility, hierarchy | One imposed visual style across banking, documents and product UI |
| `redesign-skill` | Interaction/state audit, focus visibility, truthful copy | Decorative backgrounds everywhere; invented metrics, randomized dates or fake authenticity |
| `image-to-code-skill` | Readable references, faithful imagery, section-level comparison | Mandatory generation when real assets or an editable design already exist |
| `minimalist-skill`, `brutalist-skill` | Optional art direction vocabulary | Style identity as a universal owner or mandatory palette |
| `brandkit`, `imagegen-frontend-web`, `imagegen-frontend-mobile`, `stitch-skill` | Medium-specific art direction and source handoffs | Paid generation, uploads, or new services without applicable authorization |
| `react-best-practices` | Waterfall/bundle analysis; small client boundaries | Refactoring working code merely to match a checklist |
| `nextjs` | App Router/server-client patterns | Force scaffolding over an existing project; assuming latest APIs fit the installed version |
| `tailwind-patterns` | Breakpoints, spacing and component structure | Copying decorative cards or version-specific syntax without project fit |
| `gsap` | Timelines, transform/opacity animation, matchMedia cleanup | Infinite motion or hiding required content until animation executes |
| `accessibility`, `frontend-responsive-ui` | Semantic controls, focus, labels, responsive media | Treating a checklist or a narrow browser run as full WCAG certification |

The inspected marketplace taste repository has an MIT license. Runtime-only
variants may have different provenance: confirm their individual license before
redistribution. Do not copy unlicensed source text or scripts. No vendor cache
edits or parallel top-level skill are required for this routing.

## Figma to Implementation

1. Verify account/file access with native tools. Use a new synthetic file for
   tests; do not overwrite a client file. Read the current Figma tool skills.
2. Inspect existing libraries, tokens, component mappings and fonts. Reuse
   the project's system. Create only the scoped missing components/variables.
3. Use auto-layout for related content, explicit variable scopes, named
   variants and editable text. Return node IDs. Inspect rendered bounds.
4. Fetch `get_design_context` before implementing a Figma node. Translate
   reference code into the existing stack: a visually correct `div` is not
   a keyboard-operable button. Preserve semantic intent and native behavior.
5. Use Code Connect only when account and repository support it. A local
   node-to-source mapping is useful but is not a published Code Connect map.
6. Compare fresh browser renders with source screenshots at the same size.
   Fix clipping, assets, hierarchy and state first. Record any font substitution
   or unsupported behavior; do not claim pixel identity without measuring it.

For a whole image-containing web screen, use the installed Figma capture plus
component reconstruction workflow. A component-only test proves that path at
component scope, not that an entire application was reconstructed.

## Blender Handoff

Use Blender for genuine 3D, not as a replacement for 2D layout. Check CLI and
MCP separately. A disconnected addon does not prevent isolated background CLI
work. Start with factory settings in a separate process and write only into
the authorized artifact directory. Preserve `.blend`, generation source,
materials, geometry, camera and lighting. Record Blender version and render
settings. Inspect the render before integrating it. Compress derived web assets
without discarding the original source. Never enable a remote asset/generation
provider merely because its addon is present.

## Deliverable Gate

- Exercise the primary task and every distinct state: success, invalid input,
  disabled/unavailable, empty/loading/error when the application has them.
- Use keyboard-only paths, visible focus, labels, logical order and readable
  status/error messages. Test narrow reflow and reduced motion. Run the
  project's automated accessibility tooling where available, plus manual review.
- Capture desktop, tablet and mobile screenshots after assets resolve. Check
  clipping/overlap, media framing, real content, actual interactions and requests.
- Record bundle/resource bytes, console errors and local timing. Do not label
  one local run as field Core Web Vitals or a sales/conversion improvement.
- Keep editable source and executable build/test commands. A screenshot alone
  does not prove editability; a source file alone does not prove good design.
- Report exact scope and exceptions. No unmeasured "10x" or universal quality
  claim. Avoid boilerplate review output when a short artifact receipt suffices.

## Recipient Regression Example

Create a synthetic product configurator in the recipient's own test directory. Keep the editable source, chosen tool versions, expected interactions and viewport checks with it. If 3D or Figma materially helps, use a recipient-owned synthetic asset or file and record its source-to-implementation mapping locally. Do not reuse another account's design IDs, private benchmark receipts or client assets. Compare keyboard behavior, reflow, reduced motion, clipping and actual artifact editability before promoting a change. This distribution includes guidance, not a preconnected Figma file or private regression corpus.

## Primary References

Accessed 2026-09-05:
- [W3C reflow guidance](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html):
  use 320 CSS px as one relevant reflow check, with legitimate two-dimensional
  content exceptions. This does not replace the rest of accessibility testing.
- [W3C interaction-animation guidance](https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions.html):
  nonessential interaction-triggered motion needs a disabling alternative.
- Installed official Figma `figma-use`, `figma-create-new-file`,
  `figma-generate-design`, `figma-generate-library`, and `figma-design-to-code`
  instructions govern the live connector API; resolve current versions rather
  than hardcoding a vendor-cache path into consumer projects.
