import unittest
from unittest import mock

from day11files.HexDirection import HexDirection
from day11files.HexMapper import HexMapper
from day11files.HexTile import HexTile


class TestHexMapTraverser(unittest.TestCase):
    def setUp(self):
        self.hex_mapper_mock = mock.create_autospec(HexMapper)
        self.system_under_test = HexMapTraverser(self.hex_mapper_mock)

    def __invoke_get_current_distance(self):
        return self.system_under_test.get_current_distance()

    def __invoke_move(self, direction):
        self.system_under_test.move(direction)

    def __set_up_tile(self, hex_tile, hex_tiles_dict):
        for direction, neighbor in hex_tiles_dict.items():
            hex_tile[direction] = neighbor

    def __hex_mapper_side_effect_one_level(self, *args, **kwargs):
        hex_map = args[0]
        north_tile = HexTile(1)
        northeast_tile = HexTile(1)
        southeast_tile = HexTile(1)
        south_tile = HexTile(1)
        southwest_tile = HexTile(1)
        northwest_tile = HexTile(1)

        self.__set_up_tile(north_tile, {HexDirection.South: hex_map, HexDirection.SouthEast: northeast_tile,
                                        HexDirection.SouthWest: northwest_tile})
        self.__set_up_tile(northeast_tile, {HexDirection.SouthWest: hex_map, HexDirection.NorthWest: north_tile,
                                            HexDirection.South: southeast_tile})
        self.__set_up_tile(southeast_tile, {HexDirection.NorthWest: hex_map, HexDirection.North: northeast_tile,
                                            HexDirection.SouthWest: south_tile})
        self.__set_up_tile(south_tile, {HexDirection.North: hex_map, HexDirection.NorthEast: southeast_tile,
                                        HexDirection.NorthWest: southwest_tile})
        self.__set_up_tile(southwest_tile, {HexDirection.NorthEast: hex_map, HexDirection.SouthEast: south_tile,
                                            HexDirection.North: northwest_tile})
        self.__set_up_tile(northwest_tile, {HexDirection.SouthEast: hex_map, HexDirection.South: southwest_tile,
                                            HexDirection.NorthEast: north_tile})

        hex_map[HexDirection.North] = north_tile
        hex_map[HexDirection.NorthEast] = northeast_tile
        hex_map[HexDirection.SouthEast] = southeast_tile
        hex_map[HexDirection.South] = south_tile
        hex_map[HexDirection.SouthWest] = southwest_tile
        hex_map[HexDirection.NorthWest] = northwest_tile

    def __set_up_hex_mapper_for_one_level(self):
        self.hex_mapper_mock.expand_map.side_effect = self.__hex_mapper_side_effect_one_level

    def test_get_current_distance_when_no_moves_returns_0(self):
        actual = self.__invoke_get_current_distance()
        self.assertEquals(actual, 0)

    def test_get_current_distance_when_moved_once_returns_1(self):
        self.__set_up_hex_mapper_for_one_level()
        self.__invoke_move(HexDirection.North)
        actual = self.__invoke_get_current_distance()
        self.assertEquals(actual, 1)

    def test_get_current_distance_when_moved_back_to_center_returns_0(self):
        self.__set_up_hex_mapper_for_one_level()
        self.__invoke_move(HexDirection.North)
        self.__invoke_move(HexDirection.South)
        actual = self.__invoke_get_current_distance()
        self.assertEquals(actual, 0)

    def test_move_when_moved_back_to_center_does_not_invoke_expand_map(self):
        self.__set_up_hex_mapper_for_one_level()
        self.__invoke_move(HexDirection.North)
        self.__invoke_move(HexDirection.South)
        self.hex_mapper_mock.expand_map.assert_called_once()


class HexMapTraverser:
    def __init__(self, hex_mapper):
        self.__hex_map = HexTile()
        self.__current_tile = self.__hex_map
        self.__hex_mapper = hex_mapper

    def __expand_map(self):
        self.__hex_mapper.expand_map(self.__hex_map)

    def get_current_distance(self):
        return self.__current_tile.depth

    def move(self, direction):
        next_tile = self.__current_tile[direction]
        if next_tile is None:
            self.__expand_map()
            next_tile = self.__current_tile[direction]
        self.__current_tile = next_tile
