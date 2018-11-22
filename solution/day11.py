import unittest
from unittest import mock
from unittest.mock import call

from day11files.HexDirection import HexDirection
from day11files.HexMapTraverser import HexMapTraverser
from input_utilities.inputfilepath import get_input_file_path


def get_directions_from_string(input_string):
    direction_mapping_dict = {'n': HexDirection.North,
                              'ne': HexDirection.NorthEast,
                              'se': HexDirection.SouthEast,
                              's': HexDirection.South,
                              'sw': HexDirection.SouthWest,
                              'nw': HexDirection.NortWest}
    directions_strings = input_string.lower().split(',')
    return [direction_mapping_dict[direction_string.strip()] for direction_string in directions_strings]


class DistanceFinder:
    def __init__(self, hex_map_traverser):
        self.hex_map_traverser = hex_map_traverser

    def get_distance(self, directions):
        self.__move_directions(directions)
        return self.__get_current_distance()

    def __move_directions(self, directions):
        for direction in directions:
            self.__move_direction(direction)

    def __move_direction(self, direction):
        self.hex_map_traverser.move(direction)

    def __get_current_distance(self):
        return self.hex_map_traverser.get_current_distance()


class TestDay11DistanceFinder(unittest.TestCase):
    mock_hex_map_traverser: HexMapTraverser

    def setUp(self):
        self.mock_hex_map_traverser = mock.create_autospec(HexMapTraverser)
        self.system_under_test = DistanceFinder(self.mock_hex_map_traverser)

    def set_up_hex_map_traverser_get_current_distance(self, result):
        self.mock_hex_map_traverser.get_current_distance.return_value = result

    def invoke_get_distance(self, directions):
        return self.system_under_test.get_distance(directions)

    def assert_move_invoked_for_each(self, directions):
        calls = [call(direction) for direction in directions]
        self.mock_hex_map_traverser.move.assert_has_calls(calls, any_order = False)

    def test_get_distance_when_invoked_invokes_move_for_each_direction(self):
        directions = [HexDirection.North, HexDirection.NorthEast]
        self.invoke_get_distance(directions)
        self.assert_move_invoked_for_each(directions)

    def test_get_distance_when_invoked_returns_distance_from_hex_map_traverser(self):
        self.set_up_hex_map_traverser_get_current_distance(42)
        actual = self.invoke_get_distance([HexDirection.NorthEast])
        self.assertEquals(actual, 42)


class TestGetDirectionsFromString(unittest.TestCase):
    def test_get_directions_from_string_when_only_north_returns_north(self):
        actual = get_directions_from_string('n')
        self.assertListEqual(actual, [HexDirection.North])

    def test_get_directions_from_string_when_north_and_southeast_returns_directions(self):
        actual = get_directions_from_string('n,se')
        self.assertListEqual(actual, [HexDirection.North, HexDirection.SouthEast])

    def test_get_directions_from_string_when_north_and_southwest_returns_directions(self):
        actual = get_directions_from_string('n,sw')
        self.assertListEqual(actual, [HexDirection.North, HexDirection.SouthWest])

    def test_get_directions_from_string_when_north_and_south_returns_directions(self):
        actual = get_directions_from_string('n,s')
        self.assertListEqual(actual, [HexDirection.North, HexDirection.South])

    def test_get_directions_from_string_when_north_and_northeast_returns_directions(self):
        actual = get_directions_from_string('n,ne')
        self.assertListEqual(actual, [HexDirection.North, HexDirection.NorthEast])

    def test_get_directions_from_string_when_north_and_northwest_returns_directions(self):
        actual = get_directions_from_string('n,nw')
        self.assertListEqual(actual, [HexDirection.North, HexDirection.NortWest])

    def test_get_directions_from_string_when_uppercase_returns_directions(self):
        actual = get_directions_from_string('N,NW,Sw,S,Se,NE')
        self.assertListEqual(actual, [HexDirection.North, HexDirection.NortWest, HexDirection.SouthWest,
                                      HexDirection.South, HexDirection.SouthEast, HexDirection.NorthEast])

    def test_get_directions_from_string_when_spaces_returns_directions(self):
        actual = get_directions_from_string('N, sw,se ,s')
        self.assertListEqual(actual, [HexDirection.North, HexDirection.SouthWest, HexDirection.SouthEast,
                                      HexDirection.South])


def main():
    file_path = get_input_file_path('day11.txt')
    with open(file_path, 'r') as input_file:
        input_text = input_file.read()
    print('inputText: ', input_text)


if __name__ == '__main__':
    main()
