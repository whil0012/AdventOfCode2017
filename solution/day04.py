import unittest
import os
import itertools


class TestDay04(unittest.TestCase):
    def test_passphrase_does_not_have_duplicate_words_whenNoDuplicateWords_returnsTrue(self):
        actual = passphrase_does_not_have_duplicate_words(['aa', 'bb', 'cc'])
        self.assertTrue(actual)

    def test_passphrase_does_not_have_duplicate_words_whenDuplicateWords_returnsFalse(self):
        actual = passphrase_does_not_have_duplicate_words(['aa', 'bb', 'cc', 'aa', 'dd'])
        self.assertFalse(actual)

    def test_passphrase_does_not_have_duplicate_words_whenOneWordIsSubstringOfAnother_returnsTrue(self):
        actual = passphrase_does_not_have_duplicate_words(['aa', 'bb', 'cc', 'aaa', 'dd'])
        self.assertTrue(actual)

    def test_are_anagrams_whenNotAnagrams_returnsFalse(self):
        actual = are_anagrams('abcde', 'abcd')
        self.assertFalse(actual)

    def test_are_anagrams_whenAreAnagrams_returnsTrue(self):
        actual = are_anagrams('abcde', 'ecbad')
        self.assertTrue(actual)

    def test_has_anagrams_whenNoAnagrams_returnsFalse(self):
        actual = has_anagrams(['abcde', 'fghij'])
        self.assertFalse(actual)

    def test_has_anagrams_whenHasAnagrams_returnsTrue(self):
        actual = has_anagrams(['abcde', 'xyz', 'ecdab'])
        self.assertTrue(actual)

    def test_has_anagrams_whenHasAnagramsNextToEachOther_returnsTrue(self):
        actual = has_anagrams(['abcde', 'ecdab', 'xyz'])
        self.assertTrue(actual)


def passphrase_does_not_have_duplicate_words(word_list):
    word_list_counts = [word_list.count(x) for x in word_list]
    return max(word_list_counts) < 2


def are_anagrams(word1, word2):
    permutations = itertools.permutations(word1)
    anagrams_list = [''.join(x) for x in permutations]
    return word2 in anagrams_list


def has_anagrams(word_list):
    for i in range(len(word_list)):
        word1 = word_list[i]
        for j in range(i + 1, len(word_list)):
            word2 = word_list[j]
            if are_anagrams(word1, word2):
                return True
    return False


def main():
    valid_passphrase_count = 0
    valid_no_anagrams_count = 0
    filepath = os.path.join('..', 'input', 'day04.txt')
    with open(filepath, 'r') as input_file:
        for line in input_file:
            word_list = line.strip().split(' ')
            if passphrase_does_not_have_duplicate_words(word_list):
                valid_passphrase_count += 1
                if not has_anagrams(word_list):
                    valid_no_anagrams_count += 1
    print('valid passphrase count: ', valid_passphrase_count)
    print('valid no anagrams count: ', valid_no_anagrams_count)


if __name__ == '__main__':
    main()
