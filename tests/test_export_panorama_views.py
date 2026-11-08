"""Tests for the perspective view exporter: real spherical geometry, not 2D crops.

Positive fixture: an equirectangular image whose RGB value encodes the 3D view
direction (R,G,B = 128 + 120 * x,y,z). It is continuous on the whole sphere,
including the +/-180 seam and both poles, so every rendered pixel can be decoded
back into the direction it shows and checked independently of the exporter.
Negative fixtures: a hard left/right seam and a non-equirectangular pole.
"""
import importlib.util
import json
import math
from pathlib import Path
import tempfile
import unittest

import numpy as np
from PIL import Image

MODULE = Path(__file__).resolve().parents[1] / "scripts" / "export_panorama_views.py"
spec = importlib.util.spec_from_file_location("export_panorama_views", MODULE)
ev = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ev)

W, H = 1024, 512


def lonlat_grid(w=W, h=H):
    lon = ((np.arange(w) + 0.5) / w - 0.5) * 2 * math.pi
    lat = (0.5 - (np.arange(h) + 0.5) / h) * math.pi
    return np.meshgrid(lon, lat)


def direction_panorama():
    lon, lat = lonlat_grid()
    xyz = np.stack([np.cos(lat) * np.sin(lon), np.sin(lat), np.cos(lat) * np.cos(lon)], axis=-1)
    return np.clip(128 + 120 * xyz + 0.5, 0, 255).astype(np.uint8)


def decode(img):
    d = (img.astype(np.float64) - 128) / 120
    return d / np.linalg.norm(d, axis=-1, keepdims=True)


def unit(yaw, pitch):
    y, p = math.radians(yaw), math.radians(pitch)
    return np.array([math.cos(p) * math.sin(y), math.sin(p), math.cos(p) * math.cos(y)])


def angle_deg(a, b):
    return math.degrees(math.acos(float(np.clip(np.dot(a, b), -1, 1))))


class GeometryTests(unittest.TestCase):
    equi = direction_panorama()

    def render(self, yaw, pitch, hfov=90, size=257):
        return ev.render_view(self.equi, yaw, pitch, hfov, size, size)

    def test_view_centre_points_at_requested_direction(self):
        for yaw, pitch in [(0, 0), (90, 0), (180, 0), (-90, 0), (37, 22), (-140, -61), (0, 90), (0, -90)]:
            img, _ = self.render(yaw, pitch)
            c = decode(img)[128, 128]
            self.assertLess(angle_deg(c, unit(yaw, pitch)), 1.0, (yaw, pitch))

    def test_field_of_view_matches_hfov(self):
        for hfov in (40, 90, 120):
            img, _ = self.render(15, 30, hfov, size=401)
            d = decode(img)
            # pixel centres at the left/right edge are half a pixel inside the frame
            f = 200.5 / math.tan(math.radians(hfov) / 2)
            expected = 2 * math.degrees(math.atan(200.0 / f))
            self.assertAlmostEqual(angle_deg(d[200, 0], d[200, 400]), expected, delta=1.0)

    def test_rectilinear_rows_and_columns_are_great_circles(self):
        # Straight lines in a perspective image are planes through the eye.
        img, _ = self.render(60, 35, 100, size=301)
        d = decode(img)
        for line in (d[150, :], d[:, 150], d[40, :], d[:, 260]):
            _, s, _ = np.linalg.svd(line)
            self.assertLess(s[-1] / s[0], 0.01)

    def test_orientation_right_is_positive_yaw_up_is_positive_pitch(self):
        img, _ = self.render(0, 0)
        d = decode(img)
        lon = lambda v: math.degrees(math.atan2(v[0], v[2]))
        lat = lambda v: math.degrees(math.asin(v[1]))
        self.assertGreater(lon(d[128, 250]), 30)
        self.assertLess(lon(d[128, 6]), -30)
        self.assertGreater(lat(d[6, 128]), 30)
        self.assertLess(lat(d[250, 128]), -30)

    def test_continuous_sphere_shows_no_seam_or_pole_break(self):
        for yaw, pitch in [(180, 0), (0, 90), (0, -90), (180, 70)]:
            img, _ = self.render(yaw, pitch)
            step = np.abs(np.diff(img.astype(int), axis=1)).max()
            step_v = np.abs(np.diff(img.astype(int), axis=0)).max()
            self.assertLessEqual(max(step, step_v), 3, (yaw, pitch))
        diag = ev.seam_view_diagnostics(self.equi)
        self.assertLess(diag["seam_vs_ordinary_ratio"], 1.5)

    def test_seam_meridian_is_marked_only_where_visible(self):
        _, front = self.render(0, 0)
        _, back = self.render(180, 0)
        _, zenith = self.render(0, 90)
        self.assertFalse(front.any())
        self.assertTrue(back[:, 127:130].any(axis=1).all())  # vertical line through the centre
        self.assertTrue(zenith.any())  # meridian runs from the pole to the frame edge

    def test_marker_lands_where_an_independent_projection_predicts(self):
        equi = np.full((H, W, 3), 90, dtype=np.uint8)
        lon_m, lat_m = 30.0, 10.0
        x = int((lon_m / 360 + 0.5) * W)
        y = int((0.5 - lat_m / 180) * H)
        equi[y - 2 : y + 3, x - 2 : x + 3] = (255, 0, 0)
        size, hfov = 401, 90
        img, _ = ev.render_view(equi, 0, 0, hfov, size, size)
        ys, xs = np.where((img[..., 0] > 200) & (img[..., 1] < 80))
        f = (size / 2) / math.tan(math.radians(hfov / 2))
        d = unit(lon_m, lat_m)
        expect_x = size / 2 + f * d[0] / d[2] - 0.5
        expect_y = size / 2 - f * d[1] / d[2] - 0.5
        self.assertAlmostEqual(xs.mean(), expect_x, delta=2.5)
        self.assertAlmostEqual(ys.mean(), expect_y, delta=2.5)

    def test_bilinear_filtering_wraps_across_the_seam(self):
        # Zoomed far into the seam, one source pixel spans many output pixels.
        # Interpolation must blend the last column into the first one smoothly;
        # clamping at the image edge would produce an artificial step.
        equi = np.full((H, W, 3), 40, dtype=np.uint8)
        equi[:, -1] = 210
        img, _ = ev.render_view(equi, 180, 0, 2, 256, 9)
        row = img[4, :, 0].astype(int)
        self.assertGreater(row.max() - row.min(), 100)  # both edge columns are visible
        self.assertLessEqual(np.abs(np.diff(row)).max(), 12)

    def test_invalid_hfov_rejected(self):
        with self.assertRaises(ValueError):
            ev.view_rays(0, 0, 180, 10, 10)


class NegativeFixtureTests(unittest.TestCase):
    def test_hard_seam_is_visible_and_measured(self):
        lon, _ = lonlat_grid()
        ramp = (40 + (lon + math.pi) / (2 * math.pi) * 170).astype(np.uint8)  # dark at -180, bright at +180
        equi = np.repeat(ramp[..., None], 3, axis=2)
        img, mask = ev.render_view(equi, 180, 0, 40, 256, 256)
        cols = np.where(mask.any(axis=0))[0]
        c = cols.min()
        # bilinear filtering spreads the step over ~2 pixels, so compare a few pixels apart
        jump = np.abs(img[:, c + 4].astype(int) - img[:, c - 3].astype(int)).mean()
        self.assertGreater(jump, 140)
        self.assertGreater(ev.seam_view_diagnostics(equi)["seam_vs_ordinary_ratio"], 10)

    def test_non_equirectangular_pole_breaks_up_in_zenith_view(self):
        good = direction_panorama()
        bad = good.copy()
        # Ordinary vertical stripes in the top rows, as in a stretched wide-angle
        # picture: on the sphere they all converge in the zenith.
        stripes = ((np.arange(W) // 32) % 2 * 200 + 25).astype(np.uint8)
        bad[:40] = stripes[None, :, None]

        def centre_spread(equi):
            img, _ = ev.render_view(equi, 0, 90, 90, 256, 256)
            return img[118:138, 118:138].astype(float).std(axis=(0, 1)).mean()

        self.assertLess(centre_spread(good), 8)  # smooth direction gradient only
        self.assertGreater(centre_spread(bad), 60)


class CliTests(unittest.TestCase):
    def test_export_writes_views_sheet_and_unapproved_manifest(self):
        with tempfile.TemporaryDirectory() as tmp:
            src = Path(tmp) / "synthetic.png"
            Image.fromarray(direction_panorama()).save(src)
            out = Path(tmp) / "out"
            code = ev.main([str(src), "--out", str(out), "--size", "128", "--view=-45,20,60"])
            self.assertEqual(code, 0)
            manifest = json.loads((out / "manifest.json").read_text(encoding="utf-8"))
            self.assertFalse(manifest["approved"])
            self.assertTrue(manifest["manual_qa_required"])
            self.assertEqual(len(manifest["views"]), len(ev.DEFAULT_VIEWS) + 1)
            for v in manifest["views"]:
                with Image.open(out / v["file"]) as im:
                    self.assertEqual(im.size, (128, 128))
            seam_views = {v["file"] for v in manifest["views"] if v["contains_seam"]}
            self.assertIn("03_seam_yaw180.png", seam_views)
            self.assertNotIn("01_front_yaw000.png", seam_views)
            self.assertTrue((out / "contact_sheet.jpg").exists())

    def test_unreadable_file_returns_error_code(self):
        with tempfile.TemporaryDirectory() as tmp:
            bad = Path(tmp) / "broken.jpg"
            bad.write_bytes(b"not an image")
            self.assertEqual(ev.main([str(bad), "--out", str(Path(tmp) / "o"), "--no-sheet"]), 1)


if __name__ == "__main__":
    unittest.main()
