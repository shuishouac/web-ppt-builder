---
name: web-ppt-builder
description: Build web-based slide decks that feel like PPT but ship as static websites using Slidev. Use when the user already has a content outline or near-final copy and wants a branded presentation-style webpage, optional PDF export, theme selection, logo/headshot handling, and Cloudflare Pages deployment-ready output.
---

# Web PPT Builder

## Overview

Turn a fixed outline into a presentation-style website instead of a `.pptx` file.
Default stack:

- `Slidev` for the deck runtime
- local theme presets for fast style switching
- built-in click animations and transitions for reliable motion
- `slidev build` output for static hosting
- optional PDF export for offline sharing

Do not default to exporting `.pptx`.
The primary deliverable is an interactive web deck that can be uploaded to Cloudflare Pages or any static host.

## Workflow

### 1. Collect Intake First

Before generating slides, read [references/intake-template.md](references/intake-template.md) and fill the minimum required fields.

Do not skip branding inputs when the deck is tied to a company, founder, or creator brand.

Minimum required inputs:

- deck topic
- target audience
- outcome of the deck
- existing outline or source content
- deck mode
- preferred theme preset
- deployment intent

Strongly recommended inputs:

- company or personal brand name
- logo path
- presenter headshot path
- image asset list
- primary / secondary / accent colors
- typography or copy constraints
- CTA and contact details

### 2. Choose Deck Mode Before Theme

Read [references/deck-modes.md](references/deck-modes.md).

Do not treat this as a cosmetic preference.
The deck mode changes:

- slide density
- writing style
- image needs
- animation usage
- whether the deck should stand alone without a live presenter

Default modes:

- `content-dense` -> 内容详实型
- `design-led` -> 设计优先型

If the user does not choose, ask which of these they want:

- a deck that can be read on its own with most information inside the slides
- a deck that is visually stronger, lighter on text, and depends more on live narration

### 3. Choose Theme Before Writing Slides

Read [references/theme-presets.md](references/theme-presets.md).

Pick one preset first.
Do not write the whole deck and only then think about style.

Default rule:

- business / investor / internal brief -> `editorial-light`
- product launch / demo / modern SaaS -> `product-grid`
- premium / dark / keynote / founder talk -> `midnight-stage`
- personal story / creator / educational narrative -> `warm-story`

### 4. Scaffold The Deck Project

Use the bundled starter project in `assets/starter/`.

When the user wants a runnable local project, run:

```bash
python3 scripts/scaffold_deck.py \
  --output "/abs/path/to/new-deck" \
  --config "/abs/path/to/deck.config.json"
```

The script copies the starter project, applies a theme preset, injects branding tokens, and optionally copies the logo/headshot into `public/branding/`.

Use JSON for config to avoid extra runtime dependencies.

### 5. Plan Images Before Writing Final Slides

Read [references/image-workflow.md](references/image-workflow.md).

Do not treat images as a late decoration pass.
Decide slide-by-slide whether each image must be:

- user-supplied
- AI-generated
- AI-edited from a user-supplied original
- replaced by a non-photo layout such as cards, numbers, diagrams, or quotes

By default, coordinate images through a local folder, not chat attachments.
Use exact filenames so another local AI agent can match assets deterministically.

Default rule:

- real people, real executives, real offices, real products, certifications, factories, customers, event photos -> user-supplied first
- conceptual scenes, metaphors, abstract backgrounds, generic hero art, visual fillers -> AI-generated is acceptable
- cleanup, crop, background removal, lighting correction, aspect-ratio adaptation -> AI edit is acceptable if the base image is real

If the deck depends on credibility, prefer real images over synthetic ones.

When the user has missing images and still wants to move forward, generate a collaboration pack:

```bash
python3 scripts/generate_image_prompts.py \
  --config "/abs/path/to/deck.config.json"
```

This produces a markdown file with:

- must-upload items
- current image gaps
- draft AI prompts for placeholder or conceptual visuals
- exact local filenames and target paths

The default local image folder is `public/media/`.
Users should place real photos, generated images, and edited results there using the exact emitted filenames.

### 6. Write Slides For Web Delivery, Not For Printed Pages

Read [references/content-rules.md](references/content-rules.md).

Core rules:

- one idea per slide
- short headlines
- avoid dense bullet walls
- use contrast, cards, stats, split layouts, and visual rhythm
- optimize for browser viewing first
- preserve a clear CTA or next step

Prefer:

- `DeckCover` for the opening
- `SectionBreak` between major sections
- short click-reveal sequences for layered explanation

Avoid:

- dumping a memo onto slides
- long paragraphs
- fake cinematic motion
- overusing code or charts if the audience is non-technical

### 7. Motion Policy

Default to Slidev's built-in animation system.

Use:

- per-slide `transition`
- `v-click`
- `v-clicks`
- `v-after`

Do not add external motion libraries by default.

Reason:

- built-in motion is simpler to maintain
- built-in motion exports more reliably
- external motion libraries add complexity without improving most explainers

Only add external animation tooling if the user explicitly asks for one of these:

- advanced scene choreography
- scroll-linked effects
- 3D transforms
- product-demo-grade motion beyond ordinary deck behavior

### 8. Build, Preview, Deploy

Read [references/deployment.md](references/deployment.md).

Primary commands inside a generated deck project:

```bash
pnpm install
pnpm dev
pnpm build
pnpm export:pdf
```

Primary deployment target:

- upload `dist/` to Cloudflare Pages

If the user wants simple manual deployment, prefer Direct Upload.
If the user wants automatic deploys from GitHub, prefer Git integration instead of Direct Upload.

### 9. Output Expectations

For a normal request, produce:

1. a filled intake config or clearly inferred config
2. a generated Slidev project
3. a deck-specific `slides.md`
4. image plan with missing asset list
5. theme + branding applied
6. build instructions
7. deployment instructions for Cloudflare Pages

If the user also wants offline sharing, include PDF export instructions.

## Resources

### `scripts/`

- `scaffold_deck.py`: copies the starter, injects theme tokens, copies branding assets
- `generate_image_prompts.py`: turns missing asset notes into a human-AI image sourcing pack

### `references/`

- `intake-template.md`: what to collect before deck generation
- `deck-modes.md`: how to choose between dense and design-led decks
- `image-workflow.md`: what images to request, generate, or edit
- `theme-presets.md`: preset selection guide
- `content-rules.md`: deck writing rules
- `deployment.md`: local preview, build, PDF export, Cloudflare delivery

### `assets/`

- `starter/`: base Slidev project with reusable components and theme hooks
