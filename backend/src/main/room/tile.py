class Tile:  # pylint: disable=too-few-public-methods
    def __init__(self, x, y, character_number):
        self.x_coordinate = x
        self.y_coordinate = y
        self.character_number = character_number

    def get_x(self):
        return self.x_coordinate

    def get_y(self):
        return self.y_coordinate

    def get_character_number(self):
        return self.character_number
