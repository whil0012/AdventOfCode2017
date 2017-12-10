import unittest
from operator import itemgetter
from input_utilities.inputfilepath import get_input_file_path
from collections import namedtuple


ReallocationCycle = namedtuple('ReallocationCycle', ['from_start', 'cycle_count'])


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

    def test_find_duplicate_reallocation_cycle_count_when0270_returns_from_start_5(self):
        blocks = [0, 2, 7, 0]
        actual = find_duplicate_reallocation_cycle(blocks)
        self.assertEquals(actual.from_start, 5)

    def test_find_duplicate_reallocation_cycle_count_when0270_returns_cycle_count_4(self):
        blocks = [0, 2, 7, 0]
        actual = find_duplicate_reallocation_cycle(blocks)
        self.assertEquals(actual.cycle_count, 4)


def add_blocks_to_history(blocks, reallocation_count, block_history):
    block_history[tuple(blocks)] = reallocation_count


def find_block_in_block_history(blocks, block_history):
    if tuple(blocks) in block_history:
        return (blocks, block_history[tuple(blocks)])
    return None


def create_new_block_history(blocks):
    return {tuple(blocks): 0}


def find_duplicate_reallocation_cycle(blocks):
    block_history = create_new_block_history(blocks)
    reallocation_count = 1
    new_blocks = reallocate_blocks(blocks)
    found_block = find_block_in_block_history(new_blocks, block_history)
    while found_block is None:
        add_blocks_to_history(new_blocks, reallocation_count, block_history)
        reallocation_count += 1
        new_blocks = reallocate_blocks(new_blocks)
        found_block = find_block_in_block_history(new_blocks, block_history)
    cycle_count = reallocation_count - found_block[1]
    return ReallocationCycle(reallocation_count, cycle_count)


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
    reallocation_cycle = find_duplicate_reallocation_cycle(blocks)
    print('reallocation count: ', reallocation_cycle.from_start)
    print('infinite cycle count: ', reallocation_cycle.cycle_count)


if __name__ == '__main__':
    main()
