"""Synthetic regression tests for the diagnostic script, no real image approval."""
import importlib.util
from pathlib import Path
import tempfile
import unittest

import numpy as np
from PIL import Image

MODULE = Path(__file__).resolve().parents[1] / 'scripts' / 'check_panorama.py'
spec = importlib.util.spec_from_file_location('check_panorama', MODULE)
qa = importlib.util.module_from_spec(spec)
spec.loader.exec_module(qa)


class PanoramaQaTests(unittest.TestCase):
    def test_clean_periodic_image_not_approved_automatically(self):
        w, h = 1024, 512
        lon = np.arange(w, dtype=np.float64)[None, :] / w * 2 * np.pi
        lat = np.arange(h, dtype=np.float64)[:, None] / (h - 1) * np.pi
        amplitude = np.sin(lat)
        red = 120 + 50 * amplitude * np.cos(lon)
        green = 110 + 40 * amplitude * np.sin(lon)
        blue = np.broadcast_to(130 + 30 * np.cos(lat), (h, w))
        rgb = np.stack([red, green, blue], axis=-1).astype(np.uint8)
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / 'synthetic.png'
            Image.fromarray(rgb).save(path)
            result = qa.analyze(path)
            self.assertTrue(result['aspect_ratio_2_to_1'])
            self.assertFalse(result['min_4k'])
            self.assertFalse(result['approved'])
            self.assertTrue(result['manual_qa_required'])
            self.assertNotIn('SEAM_COLOR_DISCONTINUITY', result['warnings'])

    def test_unmatched_edges_are_flagged(self):
        rgb = np.full((512, 1024, 3), 100, dtype=np.uint8)
        for x in range(1024):
            rgb[:, x, :] = 80 + (x // 64) * 6
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / 'bad.jpg'
            Image.fromarray(rgb).save(path)
            result = qa.analyze(path)
            self.assertGreater(result['seam_vs_neighbor_ratio'], 1.5)
            self.assertIn('SEAM_COLOR_DISCONTINUITY', result['warnings'])

    def test_bad_ratio_is_flagged(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / 'flat.png'
            Image.new('RGB', (800, 600)).save(path)
            result = qa.analyze(path)
            self.assertIn('NOT_2_TO_1', result['warnings'])


if __name__ == '__main__':
    unittest.main()
