import unittest

import sys
from day11files.HexDirection import HexDirection


class TestHexDirectionOpposite(unittest.TestCase):
    def test_hex_direction_opposite_when_north_returns_south(self):
        actual = hex_direction_opposite(HexDirection.North)
        self.assertEquals(actual, HexDirection.South)

    def test_hex_direction_opposite_when_northeast_returns_southwest(self):
        actual = hex_direction_opposite(HexDirection.NorthEast)
        self.assertEquals(actual, HexDirection.SouthWest)

    def test_hex_direction_opposite_when_southeast_returns_northwest(self):
        actual = hex_direction_opposite(HexDirection.SouthEast)
        self.assertEquals(actual, HexDirection.NorthWest)

    def test_hex_direction_opposite_when_south_returns_north(self):
        actual = hex_direction_opposite(HexDirection.South)
        self.assertEquals(actual, HexDirection.North)

    def test_hex_direction_opposite_when_southwest_returns_northeast(self):
        actual = hex_direction_opposite(HexDirection.SouthWest)
        self.assertEquals(actual, HexDirection.NorthEast)

    def test_hex_direction_opposite_when_northwest_returns_southeast(self):
        actual = hex_direction_opposite(HexDirection.NorthWest)
        self.assertEquals(actual, HexDirection.SouthEast)


this = sys.modules[__name__]
this.__hex_direction_opposites__ = None


def hex_direction_opposite(direction):
    if this.__hex_direction_opposites__ is None:
        this.__hex_direction_opposites__ = __init_hex_direction_opposites()
    return this.__hex_direction_opposites__[direction]


def __init_hex_direction_opposites():
    return {HexDirection.North : HexDirection.South,
                                   HexDirection.NorthEast : HexDirection.SouthWest,
                                   HexDirection.SouthEast : HexDirection.NorthWest,
                                   HexDirection.South : HexDirection.North,
                                   HexDirection.SouthWest : HexDirection.NorthEast,
                                   HexDirection.NorthWest : HexDirection.SouthEast}
