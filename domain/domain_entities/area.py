from abc import ABC,abstractmethod

class Area(ABC):
    @abstractmethod
    def __check_integrity__(self):
        pass

    @abstractmethod
    def point_is_inside(self,**args):
        pass

