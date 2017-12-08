import unittest
import os


class TestDay05(unittest.TestCase):
    def test_count_jumps_to_exit_basic_when5JumpsToExit_returns5(self):
        instructions = [0, 3, 0, 1, -3]
        actual = count_jumps_to_exit_basic(instructions)
        self.assertEquals(actual, 5)

    def test_count_jumps_to_exit_complex_when10JumpsToExit_returns10(self):
        instructions = [0, 3, 0, 1, -3]
        actual = count_jumps_to_exit_complex(instructions)
        self.assertEquals(actual, 10)


def count_jumps_to_exit_basic(instructions):
    return count_jumps_to_exit(instructions, basic_instruction_increment)


def basic_instruction_increment(instruction):
    return instruction + 1


def count_jumps_to_exit_complex(instructions):
    return count_jumps_to_exit(instructions, complex_instruction_increment)


def complex_instruction_increment(instruction):
    if instruction > 2:
        return instruction - 1
    else:
        return instruction + 1


def count_jumps_to_exit(instructions, instruction_increment_func):
    instructions_copy = list(instructions)
    instructions_count = len(instructions_copy)
    current_index = 0
    jumps_count = 0
    while current_index < instructions_count:
        jumps_count += 1
        current_jump = instructions_copy[current_index]
        instructions_copy[current_index] = instruction_increment_func(current_jump)
        current_index += current_jump
    return jumps_count


def main():
    filepath = os.path.join('..', 'input', 'day05.txt')
    with open(filepath, 'r') as input_file:
        instructions = [int(x.strip()) for x in input_file]
    number_of_jumps = count_jumps_to_exit_basic(instructions)
    print('number of jumps: ', number_of_jumps)
    number_of_jumps_complex = count_jumps_to_exit_complex(instructions)
    print('number of jumps complex: ', number_of_jumps_complex)


if __name__ == '__main__':
    main()
