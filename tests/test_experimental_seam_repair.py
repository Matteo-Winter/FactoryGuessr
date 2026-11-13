"""Tests for the experimental gradient-domain seam repair."""
import importlib.util
import math
from pathlib import Path
import tempfile
import unittest

import numpy as np
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]


def load(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / "scripts" / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


sr = load("experimental_seam_repair")
ev = load("export_panorama_views")

W, H = 1024, 512


def textured_sphere(seed=0):
    """Continuous, seam-free test panorama with texture (periodic in longitude)."""
    lon = ((np.arange(W) + 0.5) / W - 0.5) * 2 * math.pi
    lat = (0.5 - (np.arange(H) + 0.5) / H) * math.pi
    lon, lat = np.meshgrid(lon, lat)
    base = 120 + 50 * np.sin(3 * lon) * np.cos(lat) + 30 * np.sin(5 * lat)
    tex = 12 * np.sin(40 * lon + 7 * lat) + 8 * np.cos(31 * lat)
    img = np.stack([base + tex, base * 0.9 + tex, base * 0.7 - tex], -1)
    return np.clip(img, 0, 255).astype(np.uint8)


def with_seam_offset(img, offset=(35, -20, 25), width=200):
    """Simulate a typical AI seam: one side of the border has a colour cast."""
    bad = img.astype(np.int16)
    ramp = np.linspace(1, 0, width)[None, :, None]
    bad[:, :width] += (np.array(offset)[None, None, :] * ramp).astype(np.int16)
    return np.clip(bad, 0, 255).astype(np.uint8)


def edge_step(img):
    a = img.astype(float)
    return np.abs(a[:, 0] - a[:, -1]).mean()


class SeamRepairTests(unittest.TestCase):
    def test_colour_step_at_seam_is_removed(self):
        bad = with_seam_offset(textured_sphere())
        fixed, _ = sr.repair(bad, band=64)
        self.assertGreater(edge_step(bad), 15)
        self.assertLess(edge_step(fixed), edge_step(textured_sphere()) + 2)
        self.assertLess(ev.seam_view_diagnostics(fixed)["seam_vs_ordinary_ratio"], 1.5)

    def test_only_the_band_changes(self):
        bad = with_seam_offset(textured_sphere())
        band = 48
        fixed, _ = sr.repair(bad, band=band)
        np.testing.assert_array_equal(fixed[:, band:-band], bad[:, band:-band])

    def test_seamless_image_is_left_almost_unchanged(self):
        good = textured_sphere()
        fixed, _ = sr.repair(good, band=64)
        self.assertLessEqual(np.abs(fixed.astype(int) - good.astype(int)).max(), 3)

    def test_rejects_non_2to1_and_bad_band(self):
        with self.assertRaises(ValueError):
            sr.repair(np.zeros((100, 300, 3), np.uint8))
        with self.assertRaises(ValueError):
            sr.repair(textured_sphere(), band=4)

    def test_cli_writes_same_size_png(self):
        with tempfile.TemporaryDirectory() as tmp:
            src, dst = Path(tmp) / "in.png", Path(tmp) / "out.png"
            Image.fromarray(with_seam_offset(textured_sphere())).save(src)
            self.assertEqual(sr.main([str(src), str(dst), "--band", "32"]), 0)
            with Image.open(dst) as im:
                self.assertEqual(im.size, (W, H))


if __name__ == "__main__":
    unittest.main()
