from abc import ABC, abstractmethod
from . import area
from typing import List
from domain.data_classes import coordinates
from domain.data_classes import orientation


class Robot(ABC):
    @abstractmethod
    def deploy(self, coordinates_: coordinates, orientation_: orientation, area_: area.Area):
        pass

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def turn(self, direction: str):
        pass

    @abstractmethod
    def process_instructions(self, instructions: str):
        pass
