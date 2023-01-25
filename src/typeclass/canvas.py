from abc import ABC, abstractmethod

from src.typeclass.drawable import Drawable

def canvas(width, height):
    class Canvas(Drawable, ABC):
        WIDTH = width
        HEIGHT = height


        ## WIDTH  = 841
        ## HEIGHT = 1188

        ## :ef __init__(self, height, width):
        ##     self.height = height
        ##     self.width = width

        def svg(self):
            work = ""
            for element in self.drawable():
                work += element.svg()
            return self.wrap(work)

        def wrap(self, work):
            header = f"<svg width=\"{Canvas.WIDTH}mm\" height=\"{Canvas.HEIGHT}mm\" viewBox=\"0 0 {Canvas.WIDTH} {Canvas.HEIGHT}\" xmlns=\"http://www.w3.org/2000/svg\">"
            footer = "</svg>"
            return header + work + footer

        def write_to_file(self, name):
            print(f"examples/{hash(str(self))}.svg", str(self))
            with open(f"examples/{hash(str(self))}.svg", 'x') as file:
                file.write(self.svg())

        def __name__(cls):
            return f"Canvas({cls.WIDTH}, {cls.HEIGHT})"

        def __str__(cls):
            return f"src.typeclass.canvas.canvas.{Canvas.__name__}"


        ## () -> [Drawable]
        @abstractmethod
        def drawable(self):
            pass

    ##Canvas.__name__ = f"Canvas({Canvas.WIDTH}, {Canvas.HEIGHT})"
    ##Canvas.__str__  = f"src.typeclass.canvas.canvas.{Canvas.__name__}"

    return Canvas

Canvas = canvas(297, 210)
A0     = canvas(1188, 841)
A1     = canvas(841, 594)
A2     = canvas(594, 420)
A3     = canvas(420, 297)
A4     = canvas(297, 210)
c30x40 = canvas(1016, 762)
c30x30 = canvas(762, 762)

#Instagram
profilePhoto = canvas(9.31, 9.31)
squareImage = canvas(91.44, 91.44)
images = canvas(91.44, 114.3)
story = canvas(91.44, 162.56)

    ## look to make save locations for canvas objects. Write to text file the file name
    ## and the literal function call that produced the image. This way we can manipulate
    ## the call internally.
    ## @property
    ## @abstractmethod
    ## def save_location(self):
    ##     pass
