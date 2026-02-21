
NORTH, SOUTH, EAST, WEST = 0, 180, 90, 270
class Robot:
    def __init__(self, direction=NORTH, x=0, y=0):
        self._x = x
        self._y = y
        self.direction = direction
        self._instructions = {'A': self.advance,
                              'L': self.turn_left,
                              'R': self.turn_right}
    @property
    def coordinates(self):
        return (self._x, self._y)
    def advance(self):
        moves = {NORTH: 1, SOUTH: -1, EAST: 1, WEST: -1}
        if self.direction in (NORTH, SOUTH):
            self._y += moves[self.direction]
        if self.direction in (EAST, WEST):
            self._x += moves[self.direction]
    def turn_left(self):
        self.direction = (self.direction -90) % 360
    def turn_right(self):
        self.direction = (self.direction + 90) % 360
    def move(self, directions):
        for item in directions:
            self._instructions[item]()