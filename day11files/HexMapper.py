class HexMapper():
    def expand_map(self, hex_map):
        new_depth = self.__get_new_depth(hex_map)
        self.__create_new_tile(hex_map, HexDirection.North, new_depth)
        self.__create_new_tile(hex_map, HexDirection.NorthEast, new_depth)
        self.__create_new_tile(hex_map, HexDirection.SouthEast, new_depth)
        self.__create_new_tile(hex_map, HexDirection.South, new_depth)
        self.__create_new_tile(hex_map, HexDirection.SouthWest, new_depth)
        self.__create_new_tile(hex_map, HexDirection.NorthWest, new_depth)

    def __get_new_depth(self, hex_map):
        current_tile = hex_map[HexDirection.North]
        new_depth = 1
        while current_tile is not None:
            current_tile = current_tile[HexDirection.North]
            new_depth += 1
        return new_depth

    def __create_new_tile(self, hex_map, direction, new_depth):
        new_tile = HexTile(new_depth)
        new_tile_link_direction = hex_direction_opposite(direction)
        self.__set_link(new_tile, hex_map, new_tile_link_direction, direction)

    def __set_link(self, new_tile, old_tile, new_tile_link_direction, old_tile_link_direction):
        self.__set_tile_links(new_tile, new_tile_link_direction, old_tile, old_tile_link_direction)
        self.__set_links_for_linked_tiles(new_tile, old_tile, new_tile_link_direction)

    def __set_tile_links(self, new_tile, new_tile_link_direction, old_tile, old_tile_link_direction):
        new_tile[new_tile_link_direction] = old_tile
        old_tile[old_tile_link_direction] = new_tile

    def __set_links_for_linked_tiles(self, new_tile, old_tile, new_tile_link_direction):
        new_tile_link_map = self.__create_links_map[new_tile_link_direction]
        for new_tile_linked_link_direction, old_tile_linked_link_direction in new_tile_link_map.items():
            self.__set_links_for_link_map_direction(new_tile, new_tile_linked_link_direction, old_tile,
                                                    old_tile_linked_link_direction)

    def __set_links_for_link_map_direction(self, new_tile, new_tile_linked_link_direction, old_tile,
                                           old_tile_linked_link_direction):
        if new_tile[new_tile_linked_link_direction] is None:
            linked_tile = old_tile[old_tile_linked_link_direction]
            if linked_tile is not None:
                linked_tile_link_direction = hex_direction_opposite(new_tile_linked_link_direction)
                self.__set_link(new_tile, linked_tile, new_tile_linked_link_direction, linked_tile_link_direction)
