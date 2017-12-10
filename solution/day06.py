import unittest
import os
from operator import itemgetter
from input_utilities.inputfilepath import get_input_file_path


class TestDay06(unittest.TestCase):
    def test_reallocate_blocks_when1000_returns0100(self):
        blocks = [1, 0, 0, 0]
        actual = reallocate_blocks(blocks)
        self.assertListEqual(actual, [0, 1, 0, 0])

    def test_reallocate_blocks_when2000_returns0110(self):
        blocks = [2, 0, 0, 0]
        actual = reallocate_blocks(blocks)
        self.assertListEqual(actual, [0, 1, 1, 0])

    def test_reallocate_blocks_whenOtherBlocksNonZero_incrementsOtherBlocks(self):
        blocks = [2, 1, 1, 0]
        actual = reallocate_blocks(blocks)
        self.assertListEqual(actual, [0, 2, 2, 0])

    def test_reallocate_blocks_whenMaxValueInMiddleOfList_startsWithMaxValueIndex(self):
        blocks = [0, 1, 0, 0]
        actual = reallocate_blocks(blocks)
        self.assertListEqual(actual, [0, 0, 1, 0])

    def test_reallocate_blocks_whenValueEnoughToPassEnd_loopsToBeginning(self):
        blocks = [0, 0, 4, 0]
        actual = reallocate_blocks(blocks)
        self.assertListEqual(actual, [1, 1, 1, 1])

    def test_reallocate_blocks_whenMaxValueLastBlock_loopsToBeginning(self):
        blocks = [0, 2, 3, 4]
        actual = reallocate_blocks(blocks)
        self.assertListEqual(actual, [1, 3, 4, 1])

    def test_find_duplicate_reallocation_cycle_count_when0270_returns5(self):
        blocks = [0, 2, 7, 0]
        actual = find_duplicate_reallocation_cycle_count(blocks)
        self.assertEquals(actual, 5)


def add_blocks_to_history(blocks, block_history):
    block_history.add(tuple(blocks))


def blocks_in_block_history(blocks, block_history):
    return tuple(blocks) in block_history


def find_duplicate_reallocation_cycle_count(blocks):
    block_history = set()
    add_blocks_to_history(blocks, block_history)
    reallocation_count = 1
    new_blocks = reallocate_blocks(blocks)
    while not blocks_in_block_history(new_blocks, block_history):
        add_blocks_to_history(new_blocks, block_history)
        reallocation_count += 1
        new_blocks = reallocate_blocks(new_blocks)
    return reallocation_count


def reallocate_blocks(blocks):
    new_blocks = list(blocks)
    max_item = get_max_index_and_value(new_blocks)
    index = max_item[0]
    value = max_item[1]
    new_blocks[index] = 0
    index += 1
    max_allowable_index = len(new_blocks) - 1
    while value > 0:
        if index > max_allowable_index:
            index = 0
        new_blocks[index] = new_blocks[index] + 1
        value -= 1
        index += 1
    return new_blocks


def get_max_index_and_value(blocks):
    enumeration = enumerate(blocks)
    return max(enumeration, key=itemgetter(1))


def main():
    file_path = get_input_file_path('day06.txt')
    with open(file_path) as input_file:
        line = input_file.readline()
        blocks = list(map(int, line.split()))
    reallocation_count = find_duplicate_reallocation_cycle_count(blocks)
    print('reallocation count: ', reallocation_count)


if __name__ == '__main__':
    main()
