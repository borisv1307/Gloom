class AbstractRoomCard:
    EMPTY_TILE = 0

    def __init__(self, name):
        self.name = name
        self.hexes = {}

    def add_tile(self, character_number, x, y):
        coordinates = (x, y)
        if character_number in self.hexes.values() and character_number is not self.EMPTY_TILE:
            raise DuplicateTileError
        if coordinates in self.hexes:
            raise DuplicateTileError
        self.hexes[coordinates] = character_number


class DuplicateTileError(Exception):
    pass
