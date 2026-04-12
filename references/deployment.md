# Deployment Notes

## Local Workflow

Inside a generated deck project:

```bash
pnpm install
pnpm dev
pnpm build
pnpm export:pdf
```

Use `pnpm preview` or `npx vite preview` to check the built site.

## GitHub Sharing

If this deck or starter is going into GitHub:

1. keep the config example in repo
2. avoid committing private logos or headshots unless intended
3. commit the starter and references
4. do not commit generated `dist/` unless you intentionally use GitHub Pages or a static branch workflow
5. keep project-specific deck outputs in separate example folders when sharing demos

## Cloudflare Pages

### Direct Upload

Use this when the user wants the simplest manual deployment.

Flow:

1. build the deck
2. take the generated `dist/` folder
3. upload that folder to Cloudflare Pages

Best for:

- one-off public sharing
- quick demos
- non-technical publishing

Tradeoff:

- do not choose this if the user wants automatic GitHub-triggered deploys for the same project later

### Git Integration

Use this when the deck lives in a GitHub repo and should auto-deploy.

Best for:

- ongoing iteration
- versioned public decks
- open-source repos with automatic previews

## Base Path

Use `/` when hosting at the project root.

Use a slash-wrapped sub-path like `/talks/my-deck/` when the deck is hosted below a sub-route.

When using a sub-path, build with:

```bash
pnpm build -- --base /talks/my-deck/
```

## PDF

Keep PDF as optional.
The web deck is the primary deliverable.
