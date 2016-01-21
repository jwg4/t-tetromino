import unittest

from fill_blocks import make_frame_class

class TestFrame(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.Frame = make_frame_class(4)

    def test_constructor(self):
        f = self.Frame(1, 2, 3, 4)
        self.assertIsNotNone(f)
        expected = "(1, 2, 3, 4)"
        self.assertEqual(str(f), expected)

    def test_hash(self):
        f = self.Frame(1, 2, 3, 4)
        expected = hash((0, 1, 2, 3))
        self.assertEqual(hash(f), expected)

    def test_set_intersection(self):
        f = self.Frame(1, 2, 3, 4)
        g = self.Frame(0, 1, 2, 3)
        self.assertEqual(len(set([f]) & set([g])), 1)

    def test_generate_new_frames(self):
        f = self.Frame(0, 0, 0, 1)
        new_frames = f.generate_new_frames()
        # Two ways to place a T-tetromino on a 
        # board of width four with one sq in the 
        # 4th column:
        # |....|  |..x.|
        # |.x..|  |..xx|
        # |xxxo|  |..xo|
        #  ----    ----
        self.assertEqual(len(new_frames), 2)

    def test_a_gap_on_the_left_is_not_valid(self):
        f = self.Frame(0, 3, 0, 0)
        self.assertFalse(f._is_valid())

    def test_a_gap_on_the_right_is_not_valid(self):
        f = self.Frame(2, 3, 2, 0)
        self.assertFalse(f._is_valid())
