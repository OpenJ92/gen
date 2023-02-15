from src.typeclass.VFF import VFF

from numpy import array, concatenate, stack

class Bezier(VFF):
    def __init__(self, shape_in: array, shape_out: array, control_points: array, callparam=lambda t:t):
        self.shape_in = shape_in
        self.shape_out = shape_out
        self.control_points = control_points

    @classmethod
    def make_closed(self, _spine: array, _loop: array, _control_points: array):
        pass

    @classmethod
    def make_random(self):
        pass

    @classmethod
    def make_random_closed(self):
        pass

    def __call__(self, t):
        return self.evaluate(t)

    def evaluate(self, t):
        t = self.callparam(t)
        convolve = lambda t, c1, c2: (1-t)*c1 + t*c2
        a = [
                self.shape_in.reshape(self.control_points.shape[0],1),
                self.control_points,
                self.shape_out.reshape(self.control_points.shape[0],1)
            ]
        ## map lambda _: cn over the temp control axis so that below can be a functional
        ## ie return a nested lambda function of t. When moving to multi-dimensional forms
        ## then it'll be lambda t1: lambda t2: ... lambda tn: ?? . Think about this! There's
        ## could be some really interesting shapes here.
        temp_control = concatenate(a, axis=1)
        while temp_control.shape[1] > 1:
            A = [
                    convolve(t, temp_control[:, i], temp_control[:, i+1])
                    for i
                    in range(temp_control.shape[1] - 1)
                ]
            temp_control = stack(A, axis = 1)
        return tuple(temp_control.T.reshape(self.control_points.shape[0]))

    def _evaluate(self, t, arr):
        pass

    ## there may be a problem with this over many splits.
    def split(self, t):
        return [ Bezier(
            self.shape_in, self.shape_out, self.control_points, callparam=lambda nt: t*nt)
               , Bezier(
            self.shape_in, self.shape_out, self.control_points, callparam=lambda nt: (1-t)*nt+t)
               ]
