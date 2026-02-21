"""
Robot simulator module for testing robot movements on an infinite grid.

This module simulates a robot that can turn left, turn right, and advance
on a 2D grid with coordinates increasing to the north and east.
"""

NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3


class Robot:
    """
    A robot that moves on an infinite 2D grid.
    
    The robot can face four directions (NORTH, EAST, SOUTH, WEST) and
    execute three commands: turn right (R), turn left (L), and advance (A).
    """
    
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        """
        Initialize the robot with a direction and position.
        
        Args:
            direction (int): Initial direction (NORTH, EAST, SOUTH, or WEST).
            x_pos (int): Initial x-coordinate.
            y_pos (int): Initial y-coordinate.
        """
        self.direction = direction
        self.coordinates = (x_pos, y_pos)
    
    def move(self, instructions):
        """
        Execute a series of movement instructions.
        
        Args:
            instructions (str): String of commands where:
                'R' = turn right
                'L' = turn left
                'A' = advance one step in current direction
        """
        for instruction in instructions:
            if instruction == 'R':
                self._turn_right()
            elif instruction == 'L':
                self._turn_left()
            elif instruction == 'A':
                self._advance()
    
    def _turn_right(self):
        """Turn the robot 90 degrees clockwise."""
        self.direction = (self.direction + 1) % 4
    
    def _turn_left(self):
        """Turn the robot 90 degrees counter-clockwise."""
        self.direction = (self.direction - 1) % 4
    
    def _advance(self):
        """Move the robot one step forward in its current direction."""
        current_x, current_y = self.coordinates
        
        if self.direction == NORTH:
            current_y += 1
        elif self.direction == EAST:
            current_x += 1
        elif self.direction == SOUTH:
            current_y -= 1
        elif self.direction == WEST:
            current_x -= 1
        
        self.coordinates = (current_x, current_y)