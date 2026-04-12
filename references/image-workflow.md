# Image Workflow

Use this before locking the slide structure.

## Goal

Make image handling explicit.
Do not leave photo sourcing, AI generation, and image editing to the very end.

## Local Folder Rule

Default local folder:

- `public/media/`

Do not rely on chat uploads or conversational memory for image matching.
Generate exact filenames first, then ask the user to place all images into the local folder using those names.

That includes:

- real photos
- AI-generated images
- AI-edited variants

The matching rule should be filename-first, not “the user said this was the CEO image in chat”.

## 1. Classify Each Needed Image

For each slide, assign one of these:

- `required-real`
- `real-preferred`
- `ai-acceptable`
- `ai-edit-only`
- `no-image-needed`

## 2. What Usually Requires Real Images

These should be user-supplied whenever possible:

- founder / CEO / executive portraits
- team photos
- office / factory / event photos
- real product photos
- UI screenshots from the actual product
- certifications, awards, press proof
- partner logos and customer logos

Reason:

- these slides carry trust
- fake-looking visuals weaken the deck immediately

## 3. What Can Usually Be AI-Generated

These are safe candidates for generation:

- concept illustrations
- abstract hero backgrounds
- metaphoric scenes
- section-break visuals
- generic cover images when no product or person needs to be shown
- mood-setting support visuals

Use generation when the image is helping explain an idea rather than proving a claim.

## 4. What Is Best Solved By AI Editing

Prefer editing a real user-provided image when the source exists but needs cleanup:

- background removal
- aspect ratio adaptation
- light retouching
- color and lighting cleanup
- extending image edges for a wider slide crop
- converting mixed-style product photos into a more consistent set

Do not AI-edit identity-sensitive faces so heavily that they no longer look real.

## 5. Minimum Image Checklist By Deck Type

### Company Intro

- logo
- founder / CEO photo
- one company or team image
- one product or service visual
- optional office / factory / milestone proof

### Founder / Personal Deck

- profile headshot
- optional working scene photo
- optional speaking / media / social proof screenshots

### Product Deck

- product hero image
- 2 to 5 supporting product shots or screenshots
- comparison or before/after visuals

### Proposal / Pitch

- logo
- one credibility image
- one product / workflow image
- one outcome or proof visual

## 6. Prompting Pattern For AI Images

When images are missing, produce prompts in this structure:

- `purpose`: what this image is doing on the slide
- `composition`: camera angle, framing, background simplicity
- `style`: clean, editorial, realistic, technical, premium, etc.
- `brand cues`: key colors or materials
- `constraints`: no text, no watermark, no extra hands, no distorted UI
- `aspect_ratio`: usually `16:9`, `4:3`, or wide crop for slide use

## 7. Human Collaboration Rule

If any slide depends on a real person, real product, or real proof that the user has not yet supplied:

1. mark the slide as blocked by missing assets
2. list the exact requested files
3. if acceptable, provide an AI prompt as a temporary fallback
4. clearly label fallback images as synthetic placeholders

## 8. Suggested Output For Missing Images

When the user has not supplied enough assets, output a list like:

- `must upload`
  - CEO portrait
  - product hero image
  - dashboard screenshot
- `can generate`
  - opening concept image
  - section divider artwork
- `can edit`
  - crop and clean current founder photo
  - extend product image background to 16:9

## 9. Naming Rule

For every needed image, output:

- `purpose`
- `source_mode`
- `filename`
- `target_path`

Example:

- purpose: founder portrait
- source_mode: required-real
- filename: `01-founder-portrait.png`
- target_path: `public/media/01-founder-portrait.png`
