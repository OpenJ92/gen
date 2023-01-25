import ABC

class Control(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def execute(self):
        pass
