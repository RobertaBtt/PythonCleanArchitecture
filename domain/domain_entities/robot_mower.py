from abc import abstractmethod
from . import robot
from domain.data_classes import coordinates
from domain.data_classes import orientation
from domain.domain_entities import area

class RobotMower(robot.Robot):
    def __init__(self,
                 position: coordinates.Coordinates,
                 orientation: orientation.Orientation):

        self._position = position

    def deploy(self, at: area.Area):
        if at.point_is_inside(x=self.position.x, y=self.position.y):
            return True
        return False

    def move(self):
        pass

    @property
    def position(self):
        return self._position

