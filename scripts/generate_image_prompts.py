#!/usr/bin/env python3
"""
Generate a markdown image collaboration pack plus a JSON manifest from a deck config file.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


def load_config(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def list_or_empty(config: dict, key: str) -> list:
    value = config.get(key, [])
    return value if isinstance(value, list) else []


def infer_slot_base(purpose: str, category: str) -> str:
    p = purpose.lower()
    keyword_map = [
        (("ceo", "founder", "创始人", "总裁"), "founder-portrait"),
        (("presenter", "speaker", "headshot", "portrait", "演讲者", "讲者", "头像"), "presenter-headshot"),
        (("cover", "hero", "封面", "主视觉", "概念图"), "cover-hero"),
        (("team", "团队"), "team-photo"),
        (("office", "办公室"), "office-photo"),
        (("factory", "工厂"), "factory-photo"),
        (("event", "conference", "活动", "峰会"), "event-photo"),
        (("product screenshot", "ui screenshot", "dashboard", "截图", "界面"), "product-ui-screen"),
        (("product", "产品"), "product-hero"),
        (("certificate", "award", "资质", "证书", "奖项"), "proof-certificate"),
        (("customer logo", "partner logo", "logo", "客户logo", "合作方logo"), "proof-logo-strip"),
        (("media", "press", "报道", "媒体"), "proof-media-mention"),
        (("chart", "report", "graph", "图表", "报告"), "proof-chart"),
    ]
    for keywords, base in keyword_map:
        if any(k in p for k in keywords):
            return base

    category_defaults = {
        "core_people_images": "people-asset",
        "company_images": "company-asset",
        "product_images": "product-asset",
        "proof_images": "proof-asset",
        "image_gaps": "missing-asset",
    }
    return category_defaults.get(category, "asset")


def build_records(config: dict) -> list[dict]:
    counters: dict[str, int] = {}
    records: list[dict] = []
    image_source_dir = config.get("image_source_dir", "public/media").strip() or "public/media"

    category_modes = {
        "core_people_images": "required-real",
        "company_images": "required-real",
        "product_images": "required-real",
        "proof_images": "required-real",
        "image_gaps": "missing",
    }

    for category in ("core_people_images", "company_images", "product_images", "proof_images", "image_gaps"):
        for item in list_or_empty(config, category):
            if not isinstance(item, str) or not item.strip():
                continue
            purpose = item.strip()
            base = infer_slot_base(purpose, category)
            counters[base] = counters.get(base, 0) + 1
            index = counters[base]
            filename = f"{index:02d}-{base}.png"
            records.append(
                {
                    "category": category,
                    "purpose": purpose,
                    "slot": f"{base}-{index:02d}",
                    "filename": filename,
                    "target_path": f"{image_source_dir}/{filename}",
                    "source_mode": category_modes[category],
                }
            )
    return records


def render_prompt_block(filename: str, purpose: str, style_hint: str, target_path: str) -> str:
    return "\n".join(
        [
            f"### {filename}",
            "",
            f"- purpose: {purpose}",
            f"- target_path: {target_path}",
            "- composition: 16:9, clean slide-friendly framing, obvious focal point, uncluttered background",
            f"- style: {style_hint}",
            "- brand cues: use the deck palette where appropriate, but keep the image realistic and presentation-friendly",
            "- constraints: no watermark, no random text, no distorted hands, no broken UI, no extra limbs",
            "- aspect_ratio: 16:9",
            "",
            "Prompt:",
            f"> {purpose}。16:9 presentation visual, {style_hint}, clean composition, strong focal point, uncluttered background, no text, no watermark.",
            "",
        ]
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate markdown prompts and filenames for deck images.")
    parser.add_argument("--config", required=True, help="Path to deck.config.json")
    parser.add_argument("--output", help="Optional output markdown file path")
    args = parser.parse_args()

    config_path = Path(args.config).expanduser().resolve()
    config = load_config(config_path)
    output_path = Path(args.output).expanduser().resolve() if args.output else config_path.with_name("image-prompts.generated.md")
    manifest_path = output_path.with_name("image-manifest.generated.json")

    deck_title = config.get("deck_title", "Untitled Deck")
    deck_mode = config.get("deck_mode", "content-dense")
    style_hint = config.get("ai_image_style_hint", "clean editorial, realistic, web-first")
    image_source_dir = config.get("image_source_dir", "public/media").strip() or "public/media"
    records = build_records(config)

    lines = [
        "# Image Collaboration Pack",
        "",
        f"- deck_title: {deck_title}",
        f"- deck_mode: {deck_mode}",
        f"- local_image_dir: {image_source_dir}",
        f"- ai_generation_allowed: {config.get('ai_generation_allowed', True)}",
        f"- ai_editing_allowed: {config.get('ai_editing_allowed', True)}",
        "",
        "## Local Asset Rule",
        "",
        "- Do not send images in chat by default.",
        f"- Put all deck images into the local folder `{image_source_dir}/`.",
        "- Use the exact filenames below so the workflow can match them deterministically.",
        "",
        "## Asset Filename Map",
        "",
    ]

    if records:
        for record in records:
            lines.append(
                f"- `{record['filename']}`"
                f" | {record['source_mode']}"
                f" | {record['purpose']}"
            )
    else:
        lines.append("- No image records were derived from the config.")

    lines.extend(["", "## Must Upload", ""])
    must_upload = [r for r in records if r["source_mode"] == "required-real"]
    if must_upload:
        for record in must_upload:
            lines.append(f"- `{record['filename']}` -> {record['purpose']}")
    else:
        lines.append("- No explicit must-upload items were derived.")

    lines.extend(["", "## Missing Images That Need Decisions", ""])
    gaps = [r for r in records if r["category"] == "image_gaps"]
    if gaps:
        for record in gaps:
            lines.append(f"- `{record['filename']}` -> {record['purpose']}")
    else:
        lines.append("- No image gaps listed.")

    lines.extend(["", "## AI Prompt Drafts", ""])
    if gaps:
        for record in gaps:
            lines.append(
                render_prompt_block(
                    record["filename"],
                    record["purpose"],
                    style_hint,
                    record["target_path"],
                )
            )
    else:
        lines.append("No image gaps were provided, so no AI prompts were generated.")

    output_path.write_text("\n".join(lines).strip() + "\n", encoding="utf-8")
    manifest_path.write_text(
        json.dumps(
            {
                "deck_title": deck_title,
                "deck_mode": deck_mode,
                "local_image_dir": image_source_dir,
                "assets": records,
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    print(
        json.dumps(
            {
                "output_path": str(output_path),
                "manifest_path": str(manifest_path),
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
