from src.typeclass.VFF import VFF

from numpy import array, concatenate, stack

class Bezier(VFF):
    def __init__(self, shape_in: array, shape_out: array, control_points: array, callparam=lambda t:t):
        self.shape_in = shape_in
        self.shape_out = shape_out
        self.control_points = control_points

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
        temp_control = concatenate(a, axis=1)
        while temp_control.shape[1] > 1:
            A = [
                    convolve(t, temp_control[:, i], temp_control[:, i+1])
                    for i
                    in range(temp_control.shape[1] - 1)
                ]
            temp_control = stack(A, axis = 1)
        return tuple(temp_control.T.reshape(self.control_points.shape[0]))

    def split(self, t):
        return [ Bezier(
            self.shape_in, self.shape_out, self.control_points, callparam=lambda nt: t*nt)
               , Bezier(
            self.shape_in, self.shape_out, self.control_points, callparam=lambda nt: (1-t)*nt+t)
               ]
