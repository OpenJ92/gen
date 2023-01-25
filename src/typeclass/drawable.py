from abc import ABC, abstractmethod

class Drawable(ABC):

    ## () -> String
    @abstractmethod
    def svg(self):
        pass
