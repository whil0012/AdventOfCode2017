import unittest
from input_utilities.inputfilepath import get_input_file_path


class TestDay11(unittest.TestCase):
    def test_empt_test_fails(self):
        self.assertEquals(False, True, 'empty test')


def main():
    file_path = get_input_file_path('day11.txt')
    with open(file_path, 'r') as input_file:
        input_text = input_file.read()
    print('inputText: ', input_text)


if __name__ == '__main__':
    main()