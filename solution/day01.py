import unittest
import os


class TestDay01(unittest.TestCase):
    def test_solve_captcha_whenNoMatchingDigits_returns0(self):
        actual = solve_captcha('1234')
        self.assertEquals(actual, 0)

    def test_solve_captcha_whenMatchingDigits1InMiddle_returnsSum(self):
        actual = solve_captcha('1123')
        self.assertEquals(actual, 1)

    def test_solve_captcha_whenMultipleNon1MatchingDigitsInMiddle_returnsSum(self):
        actual = solve_captcha('11233')
        self.assertEquals(actual, 4)

    def test_solve_captcha_whenLastDigitMatchesFirstDigit_returnsSum(self):
        actual = solve_captcha('34563')
        self.assertEquals(actual, 3)

    def test_solve_captcha_whenLastTwoDigitsMatchFirstDigit_returnsSum(self):
        actual = solve_captcha('345633')
        self.assertEquals(actual, 6)

    def test_solve_captcha_whenAllDigitsEqual_returnsSum(self):
        actual = solve_captcha('222')
        self.assertEquals(actual, 6)


def solve_captcha(captcha):
    current_character = None
    result = 0
    for character in captcha[-1] + captcha:
        if current_character == character:
            result += int(current_character)
        current_character = character
    return result


def main():
    captcha_string = ''
    file_path = os.path.join("..", "input", "day01.txt")
    with open(file_path, 'r') as input_file:
        for line in input_file:
            captcha_string += line
    result = solve_captcha(captcha_string)
    print('captcha: ', result)


if __name__ == '__main__':
    main()