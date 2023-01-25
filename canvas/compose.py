from src.typeclass.canvas import Canvas
from src.typeclass.many import Many

class Compose(Many, Canvas):
    def __init__(manys, datas):
        self.synam = manys
        self.datas = datas

    def many(self):
        pass

    def drawable(self):
        pass
