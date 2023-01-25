## Should this be a metaclass like those seen in sqlalchemy? Or those seen in typeclass module? Then one inherits canvas into a class describing the elements of the drawing. 
## Upon consideration this indeed should be a metaclass which inherited forces the construction of a function drawables in which a user specifies drawables to be rendered. Init function serves to parameterize the canvas.

class Canvas:
    def __init__(self, drawables):
        self.drawables = drawables

    def build(self):
        work = ""
        for element in self.drawables:
            work += element.svg()
        return self.wrap(work)

    def wrap(self, work):
        header = "<svg width=\"297mm\" height=\"210mm\" viewBox=\"0 0 297 210\" xmlns=\"http://www.w3.org/2000/svg\">"
        footer = "</svg>"
        return header + work + footer

    def write_to_file(self, name):
        with open(name, 'x') as file:
            file.write(self.build())
