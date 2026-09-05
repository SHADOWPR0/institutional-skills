# Banker Excel and PowerPoint Deliverable Standard

This standard governs native, editable Excel and PowerPoint output for banking,
underwriting, capital markets, diligence, transaction, and committee work.
`universal-banker` remains the domain owner for content, numbers, structure,
pricing, covenants, downside protection, distribution risk, and final judgment.

Use this reference when the deliverable is an Excel model, model audit, linked
deck, IC presentation, lender package, board deck, financing memo, CIM/pitch
support deck, covenant package, diligence appendix, or process update.

## Ownership and Tool Routing

- `universal-banker` owns banking logic, underwriting decision rights, model
  scope, assumptions, source discipline, and deliverable content.
- `visual-design-operating-system` owns hierarchy, page architecture, polish,
  typography, grids, anti-slop design review, and presentation scanability.
- `spreadsheet`, bundled Excel, and imported spreadsheet skills are execution
  support for `.xlsx`, `.csv`, formulas, formatting, charts, rendering, and
  workbook inspection. They do not own banking judgment.
- Bundled or imported PPTX skills are execution support for native `.pptx`
  creation/editing, OOXML inspection, thumbnails/contact sheets, and rendering.
  They do not own storyboard or financial conclusions.
- Figma and `figma-implement-design` are optional support only when a reusable
  visual component, brand system, geometry library, or comparison QA materially
  improves the output. Ordinary banker work must remain native and editable in
  Excel and PowerPoint without depending on Figma.
- Imported financial-modeling, financial-analyst, PPTX, and PPTX-generator
  packages are provenance/support libraries only. Distill techniques; do not create a new top-level skill or duplicate front door.

## Native Excel Model Standard

Every banker workbook must be useful to an analyst who opens the file later and
needs to audit, edit, print, and explain it.

Required structure:

- A visible cover or summary tab stating purpose, as-of date, units, sources,
  model owner, version, decision context, and global checks.
- Separate modules for inputs, assumptions, calculations, supporting schedules,
  scenarios/sensitivities, outputs, and checks. Single-tab statement layouts are
  acceptable when they improve traceability.
- Explicit source and assumption traceability at point of use. Raw hardcodes
  must have source labels or comments when the source matters.
- Left-to-right time-series logic with consistent periods, units, signs,
  formulas, and row/column placement.
- Native Excel formulas for derived values. No hidden assumptions, magic
  numbers inside formulas, or pasted static results where auditability matters.
- Bound ranges instead of whole-column references in generated formulas.
- Checks for balance sheet balance, cash/debt roll-forward integrity, covenant
  headroom, circularity, broken links, formula errors, stale source data,
  external links, and scenario consistency.
- Scenario and sensitivity outputs tied to the same assumption spine, not
  disconnected pasted tables.

Required formatting:

- Blue font for user-entered hardcodes, black for formulas, green for internal links, and red for external links or unavailable/problem inputs.
- Negatives in parentheses, zeros as dashes, multiples as `x`, units and periods
  in headers, and consistent decimal precision by row type.
- Top borders for direct sums and totals. Totals should tie directly to the
  visible rows above unless a separate schedule is explicitly referenced.
- Clean section headers, row indentation, hidden gridlines where appropriate,
  stable column widths, readable row heights, and a restrained alert color for
  checks.
- Schedules should use enough whitespace to scan; alternating blue/white rows
  are optional for dense schedules, not a house style.
- Print areas, page breaks, headers/footers, freeze panes, source footnotes,
  clean sheet names, and no stray default sheets.

Model coverage, when relevant:

- Three-statement operating model with working capital, debt, interest, tax,
  depreciation/amortization, cash flow, and balance checks.
- DCF with unlevered FCF, WACC/build-up assumptions, terminal value, equity
  bridge, sensitivity tables, and implied multiples.
- LBO with sources/uses, debt schedule, cash sweep, exit cases, IRR/MOIC,
  sponsor return attribution, and covenant or liquidity constraints.
- Merger/accretion model with purchase price, financing, synergies, transaction
  costs, pro forma ownership, EPS or FCF per share impact, and sensitivity.
- Trading and precedent comps with screen logic, normalization, calendarization,
  outlier treatment, multiple selection, and source labels.
- Debt/covenant model with leverage, coverage, baskets, headroom, cures,
  amortization, refinancing maturity wall, and stress cases.
- Waterfall or structured-finance model with priority of payments, triggers,
  reserves, advances, recoveries, timing, and loss allocation.
- Transaction, project, real-asset, or operating model with drivers that match
  the asset, borrower, sponsor, customer, geography, and legal structure.

Excel QA before delivery:

- Inspect key formulas, precedents/dependents, link types, circularity, and
  formula error scans.
- Render every sheet or representative print view when tooling permits; inspect
  the summary page, densest schedule, scenario/sensitivity page, and checks page.
- Reconcile summary outputs to model tabs and source documents.
- Confirm hidden rows/sheets, external links, macros, metadata, and named ranges
  are intentional.
- Keep existing user workbooks intact. If editing a supplied workbook, render
  first, preserve style, and use a versioned output unless in-place edit is
  explicitly authorized.

## Native PowerPoint Deck Standard

Every banker deck must be a decision document, not a decorated transcript.

Required storyboard modules, selected as needed:

- Executive summary and clear ask.
- Situation, context, mandate, and process status.
- Company, sponsor, collateral, industry, or borrower overview.
- Operating case, key drivers, financial summary, and diligence issues.
- Valuation, credit, capital structure, transaction structure, sources/uses,
  covenant or liquidity analysis, and sensitivity evidence.
- Risks, mitigants, downside case, process, recommendation, and appendix.

Required page architecture:

- One message per page. Use an action title that states the point.
- Page body must pair the claim with the proof object: chart, table, bridge,
  map, waterfall, timetable, cap table, covenant grid, sensitivity, or evidence
  excerpt.
- Use native PowerPoint text boxes, tables, shapes, charts, and linked or
  paste-special objects where possible. Do not ship screenshot slides unless the
  screenshot is itself source evidence.
- Use restrained typography, firm-like color, consistent margins, alignment,
  spacing, masters/layouts, page numbers, sources, footnotes, confidentiality
  marks, and appendix numbering.
- Reconcile every material number to Excel, source files, or an explicit
  assumption. Do not create fake charts or unsourced placeholders.
- Keep tables and charts legible at presentation size. Direct labels beat busy
  legends when space is tight.

Anti-slop rules:

- No decorative gradients, orbs, floating card grids, fake dashboard clutter,
  generic SaaS landing-page composition, gratuitous icons, stock-looking filler,
  or marketing-site layouts for banker work.
- No vague title pages, repeated title phrasing, unanchored logos, random accent
  colors, or pages that need a narrator to explain what they mean.
- No dense bullet walls when a table, bridge, timeline, or decision tree carries
  the work better.

PowerPoint QA before delivery:

- Render every slide to thumbnails/contact sheet; inspect for overflow,
  clipping, bad contrast, poor alignment, off-page objects, chart/table
  unreadability, and inconsistent layouts.
- Check native editability by confirming important text, charts, tables, and
  shapes are editable objects, not flattened images.
- Run source, footnote, page-number, confidentiality, stale-link, font, metadata,
  and Excel tie-out checks.
- Cross-check deck numbers against the workbook, memo, and cited sources. Flag
  unresolved differences before circulation.

## Accepted Source Intelligence

- Macabacus model-formatting guidance: accepted for banker formatting cues,
  whitespace discipline, semantic colors, alerts, aligned figures, bracketed
  negatives, dashes for zeroes, and top borders.
- Macabacus presentation guidance: accepted for template discipline,
  firm-approved styles, legal/disclosure slides, deck proofing, PowerPoint link
  hygiene, and dynamic agenda/master layout concepts.
- CFI Financial Modeling Guidelines: accepted for modular design, outputs-first
  model planning, layouts, printability, freezing panes, consistent labels,
  units, schedules, transparency, and circularity/error discipline.
- ICAEW Financial Modelling Code and FMI/ICAEW best-practice material:
  accepted for principles-based model purpose, structure, transparency,
  consistency, clarity, review, master checks, traceability, and avoiding
  unnecessary complexity.
- XLerate GitHub repository: accepted only as technique inspiration for
  formula tracing, horizontal consistency checks, smart fill boundaries,
  semantic auto-coloring, and format cycles; no code imported.
- Figma SDS and Code Connect repositories: accepted only for optional
  design-system/source-of-truth patterns when Figma is materially useful; not
  required for banker XLS/PPT execution.
- Anthropic financial-services repository: accepted only as high-level support
  pattern evidence for file-based financial workflow agents, model/deck QC,
  Excel audit, and human-signoff boundaries; no branding or code imported.

## Rejected or Not Imported

- Macabacus product implementation and proprietary shortcuts: not imported;
  distilled standards only.
- CFI/ICAEW copyrighted templates, figures, slide/workbook files, and exact
  text: not copied; used for standards synthesis only.
- XLerate source code, add-in package, and distribution artifacts: not imported;
  useful ideas already covered by workbook QA rules.
- Figma SDS/Code Connect source: not imported; optional Figma support already
  exists as separate skills.
- Anthropic/Claude financial-services plugins and branding: not imported;
  overlapping domain ownership stays with the principal's canonical skills.

## Deliverable Gate

Before returning an Excel or PowerPoint artifact, provide or internally verify:

- native editability
- source and assumption traceability
- formula/link/check scan
- visual render/contact sheet inspection
- model-to-deck number reconciliation
- unresolved issue list or clean pass
- versioned output path
