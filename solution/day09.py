import unittest
from input_utilities.inputfilepath import get_input_file_path


class TestDay09(unittest.TestCase):
    def test_score_groups_whenOneGroup_returns1(self):
        actual = score_groups('{}')
        self.assertEquals(actual, 1)

    def test_score_groups_whenTwoGroupsNotNested_returns2(self):
        actual = score_groups('{}{}')
        self.assertEquals(actual, 2)

    def test_score_groups_whenTwoGroupsOneNested_returns3(self):
        actual = score_groups('{{}}')
        self.assertEquals(actual, 3)

    def test_score_groups_whenThreeGroupsNestedAtOneLevel_returns5(self):
        actual = score_groups('{{}{}}')
        self.assertEquals(actual, 5)

    def test_score_groups_whenOneGroupNestedIsInGarbage_returns1(self):
        actual = score_groups('{<{}>}')
        self.assertEquals(actual, 1)

    def test_score_groups_whenOneGroupInGarbageOneNotIn_returns3(self):
        actual = score_groups('{<{}>{}}')
        self.assertEquals(actual, 3)

    def test_score_groups_whenFirstClosingGarbageCharacterIgnored_ignoresFirstClosingCharacter(self):
        actual = score_groups('{<{!>{}>}')
        self.assertEquals(actual, 1)


def score_groups(input_text):
    score = 0
    level = 0
    in_garbage = False
    ignore_next_character = False
    for character in input_text:
        if ignore_next_character:
            ignore_next_character = False
            continue
        if in_garbage:
            if character == '!':
                ignore_next_character = True
            elif character == '>':
                in_garbage = False
            continue
        if character == '<':
            in_garbage = True
        if character == '{':
            level += 1
            score += level
        elif character == '}':
            level -= 1
    return score


def main():
    file_path = get_input_file_path('day09.txt')
    with open(file_path, 'r') as input_file:
        input_text = input_file.read()
    groups_score = score_groups(input_text)
    print('groups score: ', groups_score)


if __name__ == '__main__':
    main()
