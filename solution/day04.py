import unittest
import os


class TestDay04(unittest.TestCase):
    def test_is_valid_passphrase_whenNoDuplicateWords_returnsTrue(self):
        actual = is_valid_passphrase('aa bb cc')
        self.assertTrue(actual)

    def test_is_valid_passphrase_whenDuplicateWords_returnsFalse(self):
        actual = is_valid_passphrase('aa bb cc aa dd')
        self.assertFalse(actual)

    def test_is_valid_passphrase_whenOneWordIsSubstringOfAnother_returnsTrue(self):
        actual = is_valid_passphrase('aa bb cc aaa dd')
        self.assertTrue(actual)


def is_valid_passphrase(passphrase):
    word_list = passphrase.split(' ')
    word_list_counts = [word_list.count(x) for x in word_list]
    return max(word_list_counts) < 2


def main():
    valid_passphrase_count = 0
    filepath = os.path.join('..', 'input', 'day04.txt')
    with open(filepath, 'r') as input_file:
        for line in input_file:
            if is_valid_passphrase(line.strip()):
                valid_passphrase_count += 1
    print('valid passphrase count: ', valid_passphrase_count)


if __name__ == '__main__':
    main()
