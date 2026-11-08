#!/usr/bin/env python3
"""Inspect candidate equirectangular 360 panoramas. Never grants image approval.

Usage:
    python3 scripts/check_panorama.py public/assets/panoramas/*.jpg
    python3 scripts/check_panorama.py <image> --json

Requires: Pillow and NumPy (python3 -m pip install pillow numpy).
All diagnostics are heuristics. An actual 360 image still needs visual inspection.
"""
import argparse
import json
from pathlib import Path
import sys

import numpy as np
from PIL import Image, UnidentifiedImageError


def analyze(path: Path) -> dict:
    with Image.open(path) as image:
        width, height = image.size
        rgb = np.asarray(image.convert("RGB"), dtype=np.float32)

    # Exclude extreme rows where equirectangular poles degenerate.
    margin = max(1, round(height * 0.05))
    middle = rgb[margin : height - margin] if margin * 2 < height else rgb
    seam_delta = float(np.abs(middle[:, 0] - middle[:, -1]).mean())
    adjacent = np.abs(middle[:, 1:] - middle[:, :-1])
    ordinary_delta = float(adjacent.mean())
    seam_ratio = seam_delta / ordinary_delta if ordinary_delta else None

    # At latitude +/-90 degrees, every longitude corresponds to the same
    # geometric point. Top and bottom scanline variation is useful but not
    # sufficient evidence of correct pole projection.
    def pole_spread(row: np.ndarray) -> float:
        return float(np.abs(row - row.mean(axis=0, keepdims=True)).mean())

    out = {
        "file": str(path),
        "width": width,
        "height": height,
        "aspect_ratio_2_to_1": width == 2 * height,
        "min_4k": width >= 4096 and height >= 2048,
        "seam_mean_rgb_delta": round(seam_delta, 3),
        "ordinary_neighbor_mean_rgb_delta": round(ordinary_delta, 3),
        "seam_vs_neighbor_ratio": round(seam_ratio, 3) if seam_ratio is not None else None,
        "top_row_mean_deviation": round(pole_spread(rgb[0]), 3),
        "bottom_row_mean_deviation": round(pole_spread(rgb[-1]), 3),
        "manual_qa_required": True,
        "approved": False,
    }
    out["warnings"] = []
    if not out["aspect_ratio_2_to_1"]:
        out["warnings"].append("NOT_2_TO_1")
    if not out["min_4k"]:
        out["warnings"].append("BELOW_4K")
    # Low-contrast continuous panoramas may show a high ratio due to rounding;
    # the absolute difference threshold reduces this false-positive mode.
    if seam_ratio is not None and seam_ratio >= 1.5 and seam_delta >= 8.0:
        out["warnings"].append("SEAM_COLOR_DISCONTINUITY")
    if out["top_row_mean_deviation"] > 10 or out["bottom_row_mean_deviation"] > 10:
        out["warnings"].append("POLE_ROW_VARIATION")
    return out


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("images", nargs="+", type=Path)
    parser.add_argument("--json", action="store_true", help="Print a JSON array")
    args = parser.parse_args()
    results = []
    for path in args.images:
        try:
            results.append(analyze(path))
        except (OSError, ValueError, UnidentifiedImageError) as exc:
            results.append({"file": str(path), "error": str(exc), "approved": False})
    if args.json:
        print(json.dumps(results, ensure_ascii=False, indent=2))
    else:
        for result in results:
            print(f"{result['file']}")
            if "error" in result:
                print(f"  ERROR: {result['error']}")
            else:
                print(f"  {result['width']}x{result['height']} | seam/normal {result['seam_vs_neighbor_ratio']} | pole rows {result['top_row_mean_deviation']}/{result['bottom_row_mean_deviation']} | warnings: {','.join(result['warnings']) or 'none'}")
                print("  NOT APPROVED: human check of seam, poles, historical accuracy and rights is required")
    return 1 if any("error" in result for result in results) else 0


if __name__ == "__main__":
    sys.exit(main())
