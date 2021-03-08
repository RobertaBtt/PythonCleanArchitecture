from abc import ABC,abstractmethod
# An Area is an Entity because  it has a long-lived identity
# It will be always in the same coordinates/position
# and could have a name/identificator.

class Area(ABC):
    @abstractmethod
    def __check_integrity__(self):
        pass

    @abstractmethod
    def point_is_inside(self,**args):
        pass

