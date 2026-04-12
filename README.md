# Web PPT Builder

Turn a fixed outline into a web-first presentation that feels like PPT, but ships as a static website.

This repo is built around:

- `Slidev` for the presentation runtime
- theme presets for fast visual direction
- explicit intake for branding, images, and deck mode
- `dist/` output that can be uploaded to Cloudflare Pages
- optional PDF export for offline sharing

## Who This Is For

Use this when:

- your content outline is already mostly fixed
- you want a presentation-style website, not a `.pptx`
- you need something visually stronger than a memo
- you still want a repeatable workflow instead of one-off prompting

## Core Idea

Before generating anything, decide the deck mode:

- `content-dense` = 内容详实型
  A deck people can read on their own and still understand fully.
- `design-led` = 设计优先型
  A deck that supports live narration with stronger visuals and less text.

Then decide:

- theme preset
- brand system
- image sourcing plan
- deployment mode

## Repo Structure

```text
Web PPT Builder/
├── SKILL.md
├── README.md
├── deck.config.example.json
├── agents/openai.yaml
├── scripts/
│   ├── scaffold_deck.py
│   └── generate_image_prompts.py
├── references/
│   ├── deck-modes.md
│   ├── intake-template.md
│   ├── image-workflow.md
│   ├── theme-presets.md
│   ├── content-rules.md
│   └── deployment.md
└── assets/starter/
```

## Quick Start

1. Copy [deck.config.example.json](./deck.config.example.json) into your working folder and fill it.
2. Generate a deck project:

```bash
python3 scripts/scaffold_deck.py \
  --output "/absolute/path/to/my-deck" \
  --config "/absolute/path/to/deck.config.json"
```

3. If images are still missing, generate a collaboration pack:

```bash
python3 scripts/generate_image_prompts.py \
  --config "/absolute/path/to/deck.config.json"
```

This will generate:

- `image-prompts.generated.md`
- `image-manifest.generated.json`

Both files tell the user exactly which filenames should exist locally.

4. Run the generated deck:

```bash
cd "/absolute/path/to/my-deck"
pnpm install
pnpm dev
pnpm build
pnpm export:pdf
```

## Cloudflare Pages

The primary deployment target is Cloudflare Pages.

Simplest path:

1. run `pnpm build`
2. upload the generated `dist/` folder to Cloudflare Pages

If you want auto-deploys from GitHub instead, connect the repo to Cloudflare Pages and build the same output there.

## Image Workflow

This repo assumes image work is collaborative, not fully automatic.

Default local asset rule:

- do not rely on chat uploads
- place images in `public/media/`
- use the exact generated filenames
- let the AI match images by filename instead of free-form conversation memory

Use the intake and image workflow docs to separate:

- what the user must upload
- what can be AI-generated
- what can be AI-edited

Default rule:

- real people, real products, real proof -> user provides
- concept visuals, section art, abstract support imagery -> AI can generate
- cleanup, crop, background extension, aspect ratio adaptation -> AI can edit

## Status

This is an opinionated starter for web-first decks.
It is intentionally not optimized for exporting editable PowerPoint files.
