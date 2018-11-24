from day11files.HexDirection import HexDirection


class HexTile():
    def __init__(self, depth = 0):
        self.__depth = depth
        self.__neighbors = {HexDirection.North : None,
                            HexDirection.NorthEast : None,
                            HexDirection.SouthEast : None,
                            HexDirection.South : None,
                            HexDirection.SouthWest : None,
                            HexDirection.NorthWest : None}

    def __getitem__(self, direction):
        return self.__neighbors[direction]

    def __setitem__(self, direction, hex_tile):
        self.__neighbors[direction] = hex_tile

    @property
    def depth(self):
        return self.__depth
