class AbstractRoomCard:
    EMPTY_TILE = 0

    def __init__(self, name, hexes={}):
        self.name = name
        self.hexes = hexes

    def add_tile(self, character_number, x, y):
        coordinates = (x, y)
        if character_number in self.hexes.values() and character_number is not self.EMPTY_TILE:
            raise DuplicateTileError
        if coordinates in self.hexes:
            raise DuplicateTileError
        self.hexes[coordinates] = character_number

    def create_room(self, name):
        if name == "Den":
            self.add_tile(self.EMPTY_TILE, 0, 2)
            self.add_tile(2, 0, 4)
            self.add_tile(3, 0, 6)
            self.add_tile(self.EMPTY_TILE, 1, 1)
            self.add_tile(self.EMPTY_TILE, 1, 3)
            self.add_tile(9, 1, 5)
            self.add_tile(11, 1, 7)
            self.add_tile(self.EMPTY_TILE, 2, 0)
            self.add_tile(self.EMPTY_TILE, 2, 2)
            self.add_tile(6, 2, 4)
            self.add_tile(10, 2, 6)
            self.add_tile(12, 2, 8)
            self.add_tile(8, 3, 1)
            self.add_tile(7, 3, 3)
            self.add_tile(99, 3, 5)
            self.add_tile(1, 3, 7)
            self.add_tile(self.EMPTY_TILE, 4, 2)
            self.add_tile(4, 4, 4)
            self.add_tile(5, 4, 6)


class DuplicateTileError(Exception):
    pass
