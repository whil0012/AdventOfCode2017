import unittest
import os


class TestDay04(unittest.TestCase):
    def test_empty_test_fails(self):
        self.assertFalse(True, "empty test")