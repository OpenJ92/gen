from abc import ABC, abstractmethod

class Samplable(ABC):

    ## Sample_Method -> [(,)]
    @abstractmethod
    def sampl(self, samplemethod):
        pass
