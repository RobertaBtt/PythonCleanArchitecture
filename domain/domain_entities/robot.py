from abc import ABC,abstractmethod


class Robot(ABC):
    @abstractmethod
    def deploy(self,*args):
        pass
