import unittest
import os


class TestDay01(unittest.TestCase):
    def test_solve_captcha_whenNoMatchingDigits_returns0(self):
        actual = solve_captcha_next_digit('1234')
        self.assertEquals(actual, 0)

    def test_solve_captcha_whenMatchingDigits1InMiddle_returnsSum(self):
        actual = solve_captcha_next_digit('1123')
        self.assertEquals(actual, 1)

    def test_solve_captcha_whenMultipleNon1MatchingDigitsInMiddle_returnsSum(self):
        actual = solve_captcha_next_digit('11233')
        self.assertEquals(actual, 4)

    def test_solve_captcha_whenLastDigitMatchesFirstDigit_returnsSum(self):
        actual = solve_captcha_next_digit('34563')
        self.assertEquals(actual, 3)

    def test_solve_captcha_whenLastTwoDigitsMatchFirstDigit_returnsSum(self):
        actual = solve_captcha_next_digit('345633')
        self.assertEquals(actual, 6)

    def test_solve_captcha_whenAllDigitsEqual_returnsSum(self):
        actual = solve_captcha_next_digit('222')
        self.assertEquals(actual, 6)

    def test_solve_captcha_half_step_whenNoDigitsMatch_returns0(self):
        actual = solve_captcha_half_step('1234')
        self.assertEquals(actual, 0)

    def test_solve_captcha_half_step_whenOneDigit1Matches_returns2(self):
        actual = solve_captcha_half_step('123145')
        self.assertEquals(actual, 2)

    def test_solve_captcha_half_step_whenDigitsMatch_returnsSum(self):
        actual = solve_captcha_half_step('12341234')
        self.assertEquals(actual, 20)


def solve_captcha_next_digit(captcha):
    current_character = None
    result = 0
    for character in captcha[-1] + captcha:
        if current_character == character:
            result += int(current_character)
        current_character = character
    return result


def solve_captcha_half_step(captcha):
    half_length = int(len(captcha) / 2)
    first_half = captcha[0:half_length]
    second_half = captcha[half_length:]
    matches = [int(i) for i, j in zip(first_half, second_half) if i == j]
    return sum(matches) * 2


def main():
    captcha_string = ''
    file_path = os.path.join("..", "input", "day01.txt")
    with open(file_path, 'r') as input_file:
        for line in input_file:
            captcha_string += line
    result = solve_captcha_next_digit(captcha_string)
    print('captcha: ', result)
    result = solve_captcha_half_step(captcha_string)
    print('captcha half step: ', result)


if __name__ == '__main__':
    main()