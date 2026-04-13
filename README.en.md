# Web PPT Builder

[中文 README](./README.md)

Turn a mostly finalized outline into a presentation-style website instead of a `.pptx` file.

This repo is built to:

- generate web-based decks with `Slidev`
- support two modes: `content-dense` and `design-led`
- make branding, images, themes, and deployment explicit
- produce static output ready for `Cloudflare Pages`
- optionally export `PDF` for offline sharing

## Who This Is For

Use this if:

- your content structure is already mostly settled
- you do not want to handcraft PowerPoint layouts
- you want a presentation-style website, not an editable `.pptx`
- you want a reusable local-AI workflow instead of one-off prompting

## Core Idea

Before generating the deck, choose the mode:

- `content-dense`
  A deck that should still make sense if the audience only reads it.
- `design-led`
  A deck that supports live narration with less text and stronger visuals.

Then choose:

- a theme preset
- brand inputs
- an image collaboration plan
- a deployment path

## Repo Structure

```text
Web PPT Builder/
├── SKILL.md
├── README.md
├── README.en.md
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

1. Copy [deck.config.example.json](./deck.config.example.json) into your working folder and fill it as `deck.config.json`
2. Generate a deck project:

```bash
python3 scripts/scaffold_deck.py \
  --output "/absolute/path/to/my-deck" \
  --config "/absolute/path/to/deck.config.json"
```

3. If images are still missing, generate an image collaboration pack:

```bash
python3 scripts/generate_image_prompts.py \
  --config "/absolute/path/to/deck.config.json"
```

This generates:

- `image-prompts.generated.md`
- `image-manifest.generated.json`

Those files tell the user:

- which images are missing
- which filenames to use
- where those files should live locally
- which assets must be real
- which assets can be AI-generated

4. Run the generated deck:

```bash
cd "/absolute/path/to/my-deck"
pnpm install
pnpm dev
pnpm build
pnpm export:pdf
```

## Image Workflow

This repo assumes image collaboration happens through local files, not chat uploads.

Default rule:

- do not rely on chat-uploaded images
- keep images in `public/media/`
- use exact generated filenames
- let later AI steps match images by filename, not conversational memory

By default:

- real people, real products, and real proof should come from the user
- concept art, section visuals, and atmospheric support visuals can be AI-generated
- cutouts, outpainting, aspect-ratio adaptation, and style cleanup can be AI-edited

## Cloudflare Pages

The default deployment target is Cloudflare Pages.

Simplest workflow:

1. run `pnpm build`
2. upload the generated `dist/` folder to Cloudflare Pages

You can also connect the repo to Cloudflare Pages for Git-based auto deployment.

## Current Positioning

This is a web-first presentation starter.
It is not designed around exporting editable PowerPoint files.
