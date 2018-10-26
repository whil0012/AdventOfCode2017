import unittest
from input_utilities.inputfilepath import get_input_file_path
from functools import reduce


class TestDay10(unittest.TestCase):
    def test_twist_iteration_whentwistLengthLessThanSeed_reversesLengthItems(self):
        actual = twist_iteration([0, 1, 2, 3, 4], 0, 3)
        self.assertListEqual(actual, [2, 1, 0, 3, 4])

    def test_twist_iteration_whentwistLength0_returnsOriginalSeed(self):
        actual = twist_iteration([0, 1, 2, 3, 4], 0, 0)
        self.assertEquals(actual, [0, 1, 2, 3, 4])

    def test_twist_iteration_whentwistLengthAndPositionWrapsAround_reversesItemsWrappedAround(self):
        actual = twist_iteration([0, 1, 2, 3, 4], 3, 4)
        self.assertEquals(actual, [4, 3, 2, 1, 0])

    def test_twist_iteration_whentwistLength1_returnsOriginalSeed(self):
        actual = twist_iteration([0, 1, 2, 3, 4], 1, 1)
        self.assertEquals(actual, [0, 1, 2, 3, 4])
    
    def test_twist_whenInvoked_returnsResultOftwistedLengths(self):
        actual = twist([0, 1, 2, 3, 4], [3, 4, 1, 5])
        self.assertEquals(actual, [3, 4, 2, 1, 0])

    def test_twist_whenNumberOfRounds2_returnsResultOfTwoRounds(self):
        actual = twist([0, 1, 2, 3, 4], [3, 4, 1, 5], 2)
        self.assertEquals(actual, [2, 1, 4, 3, 0])

    def test_dense_hash_whenOneBlock_returnsDenseHash(self):
        actual = dense_hash([65, 27, 9, 1, 4, 3, 40, 50, 91, 7, 6, 0, 2, 5, 68, 22])
        self.assertEquals(actual, [64])

    def test_dense_hash_whenTwoBlocks_returnsDenseHash(self):
        actual = dense_hash([65, 27, 9, 1, 4, 3, 40, 50, 91, 7, 6, 0, 2, 5, 68, 22, 65, 27, 9, 1, 4, 3, 40, 50, 91, 7, 6, 0, 2, 5, 68, 22])
        self.assertEquals(actual, [64, 64])


def dense_hash(values, block_size = 16):
    block_count = int(len(values) / block_size)
    blocks = [values[x * block_size:(x * block_size) + block_size] for x in range(block_count)]
    return list(map((lambda x: dense_hash_internal(x)), blocks))


def dense_hash_internal(values):
    return reduce((lambda x, y: x ^ y), values)


def twist_iteration(seed, position, length):
    if length <= 1:
        return seed.copy()
    result = seed.copy()
    sub_seed = seed[position:position + length]
    length_of_seed = len(seed)
    if position + length > length_of_seed:
        sub_seed += seed[0:position + length - length_of_seed]
    sub_seed.reverse()
    for x in range(position, position + length):
        result[x % length_of_seed] = sub_seed[x - position]
    return result


def twist(seed, lengths, number_of_rounds = 1):
    result = seed.copy()
    position = 0
    skip = 0
    seed_length = len(seed)
    for length in range(number_of_rounds):
        for length in lengths:
            result = twist_iteration(result, position, length)
            position += length + skip
            position = position % seed_length
            skip += 1
    return result


def main():
    file_path = get_input_file_path('day10.txt')
    with open(file_path, 'r') as input_file:
        input_text = input_file.read()
    seed = [x for x in range(256)]
    lengths = [int(x) for x in input_text.split(',')]
    hashed = twist(seed, lengths)
    print('first number: ', hashed[0])
    print('second number: ', hashed[1])
    print('multiplied result: ', hashed[0] * hashed[1])
    print('')
    lengths_bytes = [ord(x) for x in input_text] + [17, 31, 73, 47, 23]
    hashed_bytes = twist(seed, lengths_bytes, 64)
    dense_hash_bytes = dense_hash(hashed_bytes)
    dense_hash_hex = [format(x, "02x") for x in dense_hash_bytes]
    dense_hash_hex_str = ''.join(dense_hash_hex)
    print('dense hash: ', dense_hash_hex_str)


if __name__ == '__main__':
    main()