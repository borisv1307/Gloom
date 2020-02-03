class Tile:  # pylint: disable=too-few-public-methods
    def __init__(self, x, y, character_number):
        self.x_coordinate = x
        self.y_coordinate = y
        self.character_number = character_number

    def rotate(self):
        new_x = - self.get_z()
        new_y = - self.get_x()
        return Tile(new_x, new_y, self.get_character_number())

    def get_z(self):
        return - (self.get_x() + self.get_y())

    def get_x(self):
        return self.x_coordinate

    def get_y(self):
        return self.y_coordinate

    def get_character_number(self):
        return self.character_number

    def __eq__(self, other):
        if not isinstance(other, Tile):
            return False
        return self.has_same_coordinates(other) and other.character_number == self.character_number

    def has_same_coordinates(self, other) -> bool:
        return other.x_coordinate == self.x_coordinate and other.y_coordinate == self.y_coordinate

    def __repr__(self):
        return "{} {} {}".format(self.x_coordinate, self.y_coordinate, self.character_number)

    def __hash__(self):
        return hash((self.x_coordinate, self.y_coordinate, self.character_number))
