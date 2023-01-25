from src.typeclass.VFF import VFF

class LineND(VFF):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __call__(self, t):
        dpi  = tuple(map(lambda u: u[1] - u[0], zip(self.p1, self.p2)))
        return tuple(map(lambda u: u[0] + t * u[1], zip(self.p1, dpi)))

    ## Think about how we can begin to introduce VFFs of a 
    ## higher order with respect to the domain. Partial application
    ## to first order form will do nicely I think.
