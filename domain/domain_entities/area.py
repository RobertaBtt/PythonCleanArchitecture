from abc import ABC, abstractmethod

class Area(ABC):

    @abstractmethod
    def deploy(self):
        pass

    @abstractmethod
    def point_is_inside(self, **kwargs):
        pass
