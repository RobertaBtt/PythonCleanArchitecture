from abc import ABC, abstractmethod
from . import area


class Robot(ABC):
    @abstractmethod
    def deploy(self, at: area.Area):
        pass

    @abstractmethod
    def move(self):
        pass