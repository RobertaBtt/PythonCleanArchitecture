from abc import ABC, abstractmethod
from . import area as a


class Robot(ABC):
    @abstractmethod
    def deploy(self,**kwargs):
        pass

    @abstractmethod
    def move(self, area_robot: a.Area):
        pass

    @abstractmethod
    def turn(self, direction: str):
        pass

    @abstractmethod
    def process_instructions(self, instructions: str):
        pass
