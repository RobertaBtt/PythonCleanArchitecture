from abc import ABC,abstractmethod

class Area(ABC):
    @abstractmethod
    def is_coherent(self):
        pass

    @abstractmethod
    def point_is_inside(self,**kwargs):
        pass

