import unittest
import os


class TestDay05(unittest.TestCase):
    def test_count_jumps_to_exit_when5JumpsToExit_returns5(self):
        instructions = [0, 3, 0, 1, -3]
        actual = count_jumps_to_exit(instructions)
        self.assertEquals(actual, 5)


def count_jumps_to_exit(instructions):
    instructions_count = len(instructions)
    current_index = 0
    jumps_count = 0
    while current_index < instructions_count:
        jumps_count += 1
        current_jump = instructions[current_index]
        instructions[current_index] = current_jump + 1
        current_index += current_jump
    return jumps_count


def main():
    filepath = os.path.join('..', 'input', 'day05.txt')
    with open(filepath, 'r') as input_file:
        instructions = [int(x.strip()) for x in input_file]
    number_of_jumps = count_jumps_to_exit(instructions)
    print('number of jumps: ', number_of_jumps)


if __name__ == '__main__':
    main()
