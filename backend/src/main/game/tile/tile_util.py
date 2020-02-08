class TileUtility:
    @staticmethod
    def remove_tile_by_type(room, card_type):
        tiles = room.get_tiles()
        tile_to_remove = TileUtility.get_tile_by_type(room, card_type)
        new_tiles = [tile for tile in tiles if tile != tile_to_remove]
        new_room = room.clone()
        new_room.set_tiles(new_tiles)
        return new_room

    @staticmethod
    def get_tile_by_type(room, card_type):
        for tile in room.get_tiles():
            if TileUtility.is_tile_of_type(tile, card_type):
                return tile
        return None

    @staticmethod
    def has_tile_of_type(room, card_type):
        for tile in room.get_tiles():
            if TileUtility.is_tile_of_type(tile, card_type):
                return True
        return False

    @staticmethod
    def is_tile_of_type(tile, card_type):
        return tile.get_character_number() == card_type
