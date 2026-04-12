#!/usr/bin/env python3
"""
Scaffold a branded Slidev deck from the starter project.
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
from pathlib import Path


PRESETS = {
    "editorial-light": {
        "primary_color": "#1f2937",
        "secondary_color": "#e5e7eb",
        "accent_color": "#c2410c",
        "surface_color": "#fffaf2",
        "text_color": "#111827",
        "muted_color": "#6b7280",
    },
    "product-grid": {
        "primary_color": "#0f172a",
        "secondary_color": "#dbeafe",
        "accent_color": "#2563eb",
        "surface_color": "#f8fbff",
        "text_color": "#0f172a",
        "muted_color": "#64748b",
    },
    "midnight-stage": {
        "primary_color": "#e2e8f0",
        "secondary_color": "#1e293b",
        "accent_color": "#22c55e",
        "surface_color": "#020617",
        "text_color": "#e2e8f0",
        "muted_color": "#94a3b8",
    },
    "warm-story": {
        "primary_color": "#4c1d06",
        "secondary_color": "#f5e6da",
        "accent_color": "#b45309",
        "surface_color": "#fff7ed",
        "text_color": "#431407",
        "muted_color": "#9a6b52",
    },
}

MODE_LABELS = {
    "content-dense": "内容详实型",
    "design-led": "设计优先型",
}


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", value.strip().lower()).strip("-")
    return slug or "web-ppt-deck"


def load_config(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def write_mode_template(output_dir: Path, mode: str) -> None:
    template_name = {
        "content-dense": "slides-content-dense.md",
        "design-led": "slides-design-led.md",
    }.get(mode, "slides-content-dense.md")
    templates_dir = output_dir / "templates"
    selected_template = templates_dir / template_name
    destination = output_dir / "slides.md"
    shutil.copy2(selected_template, destination)
    shutil.rmtree(templates_dir, ignore_errors=True)


def replace_tokens(root: Path, tokens: dict[str, str]) -> None:
    text_extensions = {".md", ".vue", ".css", ".json"}
    for file_path in root.rglob("*"):
        if not file_path.is_file() or file_path.suffix not in text_extensions:
            continue
        content = file_path.read_text(encoding="utf-8")
        for key, value in tokens.items():
            content = content.replace(key, value)
        file_path.write_text(content, encoding="utf-8")


def bool_literal(value: bool) -> str:
    return "true" if value else "false"


def copy_brand_asset(source: str | None, target_dir: Path, target_name: str) -> str:
    if not source:
        return ""
    source_path = Path(source).expanduser().resolve()
    if not source_path.exists():
        return ""
    target_dir.mkdir(parents=True, exist_ok=True)
    suffix = source_path.suffix.lower() or ".png"
    destination = target_dir / f"{target_name}{suffix}"
    shutil.copy2(source_path, destination)
    return f"/branding/{destination.name}"


def main() -> None:
    parser = argparse.ArgumentParser(description="Create a Slidev deck project from the bundled starter.")
    parser.add_argument("--output", required=True, help="Output directory for the new deck project.")
    parser.add_argument("--config", required=True, help="Path to a JSON config file.")
    args = parser.parse_args()

    script_dir = Path(__file__).resolve().parent
    skill_root = script_dir.parent
    starter_dir = skill_root / "assets" / "starter"
    output_dir = Path(args.output).expanduser().resolve()
    config_path = Path(args.config).expanduser().resolve()

    if output_dir.exists() and any(output_dir.iterdir()):
        raise SystemExit(f"Output directory is not empty: {output_dir}")
    output_dir.mkdir(parents=True, exist_ok=True)

    config = load_config(config_path)
    deck_mode = config.get("deck_mode", "content-dense")
    if deck_mode not in MODE_LABELS:
        valid = ", ".join(sorted(MODE_LABELS))
        raise SystemExit(f"Unknown deck_mode '{deck_mode}'. Valid values: {valid}")

    preset_name = config.get("theme_preset", "editorial-light")
    if preset_name not in PRESETS:
        valid = ", ".join(sorted(PRESETS))
        raise SystemExit(f"Unknown theme_preset '{preset_name}'. Valid values: {valid}")

    palette = PRESETS[preset_name].copy()
    for key in palette:
        if config.get(key):
            palette[key] = config[key]

    shutil.copytree(starter_dir, output_dir, dirs_exist_ok=True)
    write_mode_template(output_dir, deck_mode)

    branding_dir = output_dir / "public" / "branding"
    logo_src = copy_brand_asset(config.get("logo_path"), branding_dir, "logo")
    headshot_src = copy_brand_asset(config.get("headshot_path"), branding_dir, "headshot")

    title = config.get("deck_title", "Web PPT Deck")
    subtitle = config.get("deck_subtitle", "Built with Slidev")
    presenter_name = config.get("presenter_name", "")
    presenter_role = config.get("presenter_role", "")
    organization_name = config.get("organization_name", "")
    export_filename = slugify(config.get("export_filename", title))

    tokens = {
        "__DECK_TITLE__": title,
        "__DECK_SUBTITLE__": subtitle,
        "__PRESENTER_NAME__": presenter_name,
        "__PRESENTER_ROLE__": presenter_role,
        "__ORGANIZATION_NAME__": organization_name,
        "__LOGO_SRC__": logo_src,
        "__HEADSHOT_SRC__": headshot_src,
        "__SHOW_LOGO__": bool_literal(bool(config.get("show_logo") and logo_src)),
        "__SHOW_HEADSHOT__": bool_literal(bool(config.get("show_headshot") and headshot_src)),
        "__PRIMARY_COLOR__": palette["primary_color"],
        "__SECONDARY_COLOR__": palette["secondary_color"],
        "__ACCENT_COLOR__": palette["accent_color"],
        "__SURFACE_COLOR__": palette["surface_color"],
        "__TEXT_COLOR__": palette["text_color"],
        "__MUTED_COLOR__": palette["muted_color"],
        "__DECK_MODE__": deck_mode,
        "__DECK_MODE_LABEL__": MODE_LABELS[deck_mode],
        "__EXPORT_FILENAME__": export_filename,
        "__BASE_PATH__": config.get("base_path", "/"),
    }
    replace_tokens(output_dir, tokens)

    summary = {
        "output_dir": str(output_dir),
        "deck_mode": deck_mode,
        "theme_preset": preset_name,
        "logo_copied": bool(logo_src),
        "headshot_copied": bool(headshot_src),
        "next_steps": [
            "cd <output_dir>",
            "pnpm install",
            "pnpm dev",
            "pnpm build",
        ],
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
