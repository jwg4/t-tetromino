import unittest

from fill_blocks import make_frame_class

class TestFrame(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.Frame = make_frame_class(4)

    def test_constructor(self):
        f = self.Frame(1, 2, 3, 4)
        self.assertIsNotNone(f)
