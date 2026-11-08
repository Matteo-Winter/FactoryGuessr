#!/usr/bin/env python3
"""Prepare a panorama job WITHOUT calling any external API or spending credits.

Usage:
    python3 scripts/generate_skybox.py gb-1840-textile-mill
    python3 scripts/generate_skybox.py gb-1840-textile-mill --output /tmp/job.json

Copy the printed prompt into a suitable 360 panorama generator.
"""
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("scene_id", help="Scene id from public/data/scenes.json")
    parser.add_argument("--output", type=Path, help="Optional destination for job JSON")
    args = parser.parse_args()
    data = json.loads((ROOT / "public/data/scenes.json").read_text(encoding="utf-8"))
    scenes = {item["id"]: item for item in data["scenes"]}
    if args.scene_id not in scenes:
        parser.error("Unknown scene ID. Choose from: " + ", ".join(scenes))
    scene = scenes[args.scene_id]
    job = {
        "scene_id": scene["id"],
        "prompt": scene["prompt_en"],
        "projection": "equirectangular",
        "aspect_ratio": "2:1",
        "target_resolution": "4096x2048",
        "output_path": str(Path("public") / scene["panorama_path"]),
        "served_url": "/" + scene["panorama_path"],
        "historic_label": scene["historical_status"],
        "status": "manual_generation_required",
        "notice": "No API call was made. Provider setup, cost and license must be verified separately.",
    }
    output = json.dumps(job, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(output, encoding="utf-8")
        print("Wrote generation job to:", args.output)
    else:
        print(output, end="")

if __name__ == "__main__":
    main()
