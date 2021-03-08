from abc import abstractmethod
from . import robot
from domain.data_classes import coordinates

class RobotMower(robot.Robot):
    def __init__(self, position: coordinates.Coordinates):
        self._position = position

    @property
    def position(self):
        return self._position

    def deploy(self,*args):
        pass