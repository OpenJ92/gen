from abc import ABC, abstractmethod

class Sample_Method(ABC):

    # (Num a) => () -> [0,1]
    @abstractmethod
    def values(self):
        pass
