#!/usr/bin/env python3
"""EXPERIMENTAL local, cost-free repair of the +/-180 deg seam of an equirectangular panorama.

Method (gradient-domain / Poisson-style, no AI model, no network):
1. Roll the image by half its width so the left/right border lies in the centre.
2. Measure the colour step across the seam for every row and channel, minus the
   natural gradient expected from the neighbouring columns.
3. Spread a correction of +-step/2 into both sides as a harmonic (Laplace) field
   inside a band of +-BAND pixels: exact at the seam, zero at the band edge.
   High-frequency parts of the step decay within a few pixels, slow colour and
   brightness offsets are spread across the whole band. Edges and texture inside
   the band are kept (the correction is smooth); outside the band nothing changes.
4. Roll back. The output is the same size as the input.

What this can NOT do: it does not invent or move content. Shapes that differ on
both sides (cloud outlines, a cut object) stay visibly mismatched. Always check
the before/after views by eye; a lower metric alone is not an approval.

Usage:
  python3 scripts/experimental_seam_repair.py IN.jpg OUT.png [--band 160]
"""
import argparse
import json
import sys
from pathlib import Path

import numpy as np
from PIL import Image
from scipy.fft import dct, idct


def seam_step(rolled, c):
    """Per-row, per-channel discontinuity between columns c-1 and c (float)."""
    a = rolled.astype(np.float64)
    l0, l1 = a[:, c - 1], a[:, c - 2]
    r0, r1 = a[:, c], a[:, c + 1]
    natural = ((l0 - l1) + (r1 - r0)) / 2  # step expected from the local gradient
    return (r0 - l0) - natural  # shape (H, 3)


def harmonic_ramp(step_half, band):
    """Laplace solution on a strip of width `band`: value step_half(y) at s=0, 0 at s=band.

    Neumann (reflecting) boundary at top/bottom, solved per DCT mode along y.
    Returns array (band, H, C); index s = distance from the seam (0 = seam column).
    """
    h = step_half.shape[0]
    coef = dct(step_half, type=2, axis=0, norm="ortho")  # (H, C)
    k = np.arange(h)[:, None]
    lam = np.pi * k / h  # continuous eigenvalue per mode (pixel units)
    s = np.arange(band)[:, None, None]
    with np.errstate(over="ignore", invalid="ignore"):
        # sinh(lam*(band-s))/sinh(lam*band), written stably as exp differences
        prof = (np.exp(-lam * s) - np.exp(-lam * (2 * band - s))) / (1 - np.exp(-2 * lam * band))
    prof[:, 0, :] = (band - s[:, 0, :]) / band  # mode 0: linear ramp
    prof = np.nan_to_num(prof)
    return idct(prof * coef[None], type=2, axis=1, norm="ortho")


def repair(equi, band=160):
    h, w, _ = equi.shape
    if w != 2 * h:
        raise ValueError(f"expected 2:1 equirectangular image, got {w}x{h}")
    if not 8 <= band <= w // 4:
        raise ValueError("band must be between 8 and width/4")
    rolled = np.roll(equi, w // 2, axis=1).astype(np.float64)
    c = w // 2
    half = seam_step(rolled, c) / 2
    ramp = harmonic_ramp(half, band)  # (band, H, C)
    # left side (columns c-1, c-2, ...) is raised by +half, right side lowered by -half
    rolled[:, c - band : c] += ramp[::-1].transpose(1, 0, 2)
    rolled[:, c : c + band] -= ramp.transpose(1, 0, 2)
    out = np.clip(np.rint(rolled), 0, 255).astype(np.uint8)
    return np.roll(out, -(w // 2), axis=1), {
        "method": "roll + harmonic gradient-domain seam correction + roll back",
        "band_px_each_side": band,
        "changed_columns": [w - band, w - 1, 0, band - 1],
        "mean_abs_seam_step_before": round(float(np.abs(2 * half).mean()), 3),
    }


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("src")
    p.add_argument("dst")
    p.add_argument("--band", type=int, default=160, help="pixels changed on each side of the seam")
    a = p.parse_args(argv)
    try:
        with Image.open(a.src) as im:
            equi = np.asarray(im.convert("RGB"))
    except OSError as e:
        print(f"cannot read {a.src}: {e}", file=sys.stderr)
        return 1
    out, info = repair(equi, a.band)
    untouched = np.ones(equi.shape[1], bool)
    untouched[: a.band] = untouched[-a.band :] = False
    info["outside_band_identical"] = bool((out[:, untouched] == equi[:, untouched]).all())
    info["approved"] = False
    Path(a.dst).parent.mkdir(parents=True, exist_ok=True)
    Image.fromarray(out).save(a.dst)
    print(json.dumps(info, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
