
class Alien:
    health = 3
    total_aliens_created = 0
    def __init__(self, x_coordinate, y_coordinate):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        Alien.total_aliens_created += 1

    def hit(self):
        self.health -= 1

    def is_alive(self):
        return self.health > 0

    def teleport(self, x_coordinate, y_coordinate):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate

    def collision_detection(self, col_object):
        pass


def new_aliens_collection(alien_start_positions):
    return [Alien(x, y) for x, y in alien_start_positions]
