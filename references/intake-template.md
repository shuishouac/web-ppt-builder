# Intake Template

Collect this before generating the deck.

## 1. Deck Basics

- `deck_title`:
- `deck_subtitle`:
- `deck_mode`:
  - `content-dense`
  - `design-led`
- `deck_type`:
  - `company`
  - `personal`
  - `product`
  - `training`
  - `proposal`
- `audience`:
- `goal`:
- `cta`:

## 2. Source Content

- `source_format`:
  - outline
  - article
  - memo
  - notes
  - script
- `source_path`:
- `must_keep_points`:
- `must_remove_points`:

## 3. Brand Identity

- `organization_name`:
- `presenter_name`:
- `presenter_role`:
- `logo_path`:
- `headshot_path`:
- `show_logo`: `true | false`
- `show_headshot`: `true | false`

## 4. Image Assets

- `image_source_dir`:
  - default: `public/media`
- `core_people_images`:
  - founder / CEO photo
  - leadership photos
  - speaker portrait
- `company_images`:
  - office
  - team
  - factory
  - events
- `product_images`:
  - product cutout
  - product lifestyle
  - UI screenshots
  - comparison screenshots
- `proof_images`:
  - certificates
  - customer logos
  - media mentions
  - charts / reports / screenshots
- `image_gaps`:
  - what is missing and still needs to be sourced
- `ai_generation_allowed`: `true | false`
- `ai_editing_allowed`: `true | false`
- `ai_image_style_hint`:
- `image_notes`:

## 5. Visual System

- `theme_preset`:
  - `editorial-light`
  - `product-grid`
  - `midnight-stage`
  - `warm-story`
- `primary_color`:
- `secondary_color`:
- `accent_color`:
- `surface_color`:
- `text_color`:
- `muted_color`:
- `font_hint`:

## 6. Voice And Constraints

- `tone`:
  - sharp
  - professional
  - premium
  - technical
  - warm
- `copy_rules`:
- `forbidden_words`:
- `language`:

## 7. Delivery

- `needs_pdf`: `true | false`
- `deployment_mode`:
  - `cloudflare-direct-upload`
  - `cloudflare-git`
  - `local-only`
- `base_path`:
  - use `/` for root deployment
  - use `/sub-path/` for sub-route deployments

## Minimum Viable Intake

If the user gives very little information, infer only these defaults:

- `deck_mode`: `content-dense`
- `theme_preset`: `editorial-light`
- `show_logo`: `false`
- `show_headshot`: `false`
- `ai_generation_allowed`: `true`
- `ai_editing_allowed`: `true`
- `needs_pdf`: `false`
- `deployment_mode`: `cloudflare-direct-upload`
- `base_path`: `/`

Then explicitly note what was inferred.
