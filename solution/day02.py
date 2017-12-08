import unittest
import os


class TestDay02(unittest.TestCase):
    def test_get_spreadsheet_row_numbers_whenInvoked_returnsNumbersInList(self):
        test_row = '3458	3471	163	1299	170	4200	2425	167	3636	4001	4162	115	2859	130	4075	4269'
        expected = [3458, 3471, 163, 1299, 170, 4200, 2425, 167, 3636, 4001, 4162, 115, 2859, 130, 4075, 4269]
        actual = get_spreadsheet_row_numbers(test_row)
        self.assertListEqual(actual, expected)

    def test_get_row_difference_whenLargest8AndSmallest3_Returns5(self):
        test_row_numbers = [4, 5, 4, 3, 6, 8, 4, 3]
        actual = get_row_difference(test_row_numbers)
        self.assertEquals(actual, 5)

    def test_get_checksum_whenThreeRowsDifference8And4And6_returns18(self):
        test_row_1 = [5, 1, 9, 5]
        test_row_2 = [7, 5, 3]
        test_row_3 = [2, 4, 6, 8]
        test_rows = [test_row_1, test_row_2, test_row_3]
        actual = get_checksum(test_rows)
        self.assertEquals(actual, 18)


def get_spreadsheet_row_numbers(row):
    return [int(x) for x in row.split('\t')]


def get_row_difference(row_numbers):
    min_number = min(row_numbers)
    max_number = max(row_numbers)
    return max_number - min_number

def get_checksum(rows):
    result = 0
    for row in rows:
        difference = get_row_difference(row)
        result += difference
    return result


def main():
    rows = []
    file_path = os.path.join('..', 'input', 'day02.txt')
    with open(file_path, 'r') as input_file:
        for line in input_file:
            row = get_spreadsheet_row_numbers(line)
            rows.append(row)
    checksum = get_checksum(rows)
    print('checksum: ', checksum)


if __name__ == '__main__':
    main()
