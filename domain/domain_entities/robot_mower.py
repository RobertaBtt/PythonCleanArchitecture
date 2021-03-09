from . import robot
from domain.data_classes import coordinates as c
from domain.domain_entities import area as a

ORIENTATIONS = ['N', 'S', 'E', 'W']

class RobotMower(robot.Robot):

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        self._position = value

    @property
    def orientation(self):
        return self._orientation

    @orientation.setter
    def orientation(self, value):
        self._orientation = value

    @property
    def area(self):
        return self._area

    @area.setter
    def area(self, value):
        self._area = value

    def deploy(self, coordinates_: c.Coordinates, orientation_: str, area_: a.Area):

        if area_.point_is_inside(x=coordinates_.x, y=coordinates_.y) and orientation_ in ORIENTATIONS:
            self._position = coordinates_
            self._orientation = orientation_
            self._area = area_

            return True
        return False

    def move(self, area_robot: a.Area):
        if self._orientation == 'N':
            new_position = c.Coordinates(self.position.x, self.position.y + 1)
        elif self._orientation == 'S':
            new_position = c.Coordinates(self.position.x, self.position.y - 1)
        elif self._orientation == 'E':
            new_position = c.Coordinates(self.position.x + 1, self.position.y)
        elif self._orientation == 'W':
            new_position = c.Coordinates(self.position.x - 1, self.position.y)
        else:
            return False

        if area_robot.point_is_inside(x=new_position.x, y=new_position.y):
            self.position = new_position
            return True
        return False

    def turn(self, direction: str):

        if direction == 'L':
            self._turn_left()
        elif direction == 'R':
            self._turn_right()

    def _turn_left(self):

        if self._orientation == 'N':
            self._orientation = 'W'
        elif self._orientation == 'W':
            self._orientation = 'S'
        elif self._orientation == 'S':
            self._orientation = 'E'
        elif self.orientation == 'E':
            self._orientation = 'N'

    def _turn_right(self):
        if self._orientation == 'N':
            self._orientation = 'E'
        elif self._orientation == 'E':
            self._orientation = 'S'
        elif self._orientation == 'S':
            self._orientation = 'W'
        elif self.orientation == 'W':
            self._orientation = 'N'

    def process_instructions(self, instructions: str):

        for instruction in instructions:
            if instruction == 'M':
                self.move(self.area)
            elif instruction == 'L':
                self._turn_left()
            elif instruction == 'R':
                self._turn_right()
