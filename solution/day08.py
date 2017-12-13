import unittest
from input_utilities.inputfilepath import get_input_file_path


class TestDay08(unittest.TestCase):
    def test_empty_fails(self):
        self.assertFalse(True, 'empty test')