import unittest
from input_utilities.inputfilepath import get_input_file_path


class TestDay09(unittest.TestCase):
    def test_score_groups_whenOneGroup_returns1(self):
        actual = score_groups('{}')
        self.assertEquals(actual[0], 1)

    def test_score_groups_whenTwoGroupsNotNested_returns2(self):
        actual = score_groups('{}{}')
        self.assertEquals(actual[0], 2)

    def test_score_groups_whenTwoGroupsOneNested_returns3(self):
        actual = score_groups('{{}}')
        self.assertEquals(actual[0], 3)

    def test_score_groups_whenThreeGroupsNestedAtOneLevel_returns5(self):
        actual = score_groups('{{}{}}')
        self.assertEquals(actual[0], 5)

    def test_score_groups_whenOneGroupNestedIsInGarbage_returns1(self):
        actual = score_groups('{<{}>}')
        self.assertEquals(actual[0], 1)

    def test_score_groups_whenOneGroupInGarbageOneNotIn_returns3(self):
        actual = score_groups('{<{}>{}}')
        self.assertEquals(actual[0], 3)

    def test_score_groups_whenFirstClosingGarbageCharacterIgnored_ignoresFirstClosingCharacter(self):
        actual = score_groups('{<{!>{}>}')
        self.assertEquals(actual[0], 1)

    def test_score_groups_whenNoGarbageGroups_returns0(self):
        actual = score_groups('{{{}}}')
        self.assertEquals(actual[1], 0)

    def test_score_groups_whenEmptyGabageGroup_returns0(self):
        actual = score_groups('{<>}')
        self.assertEquals(actual[1], 0)

    def test_score_groups_when3GarbageCharacters_returns3(self):
        actual = score_groups('{<123>}')
        self.assertEquals(actual[1], 3)

    def test_score_groups_whenCancelledCharacters_doesNotCountCancelledCharacters(self):
        actual = score_groups('{<12!3>}')
        self.assertEquals(actual[1], 2)


def score_groups(input_text):
    score = 0
    level = 0
    garbage_characters_count = 0
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
            else:
                garbage_characters_count += 1
            continue
        if character == '<':
            in_garbage = True
        if character == '{':
            level += 1
            score += level
        elif character == '}':
            level -= 1
    return (score, garbage_characters_count)


def main():
    file_path = get_input_file_path('day09.txt')
    with open(file_path, 'r') as input_file:
        input_text = input_file.read()
    groups_score = score_groups(input_text)
    print('groups score: ', groups_score[0])
    print('garbage characters count: ', groups_score[1])


if __name__ == '__main__':
    main()
