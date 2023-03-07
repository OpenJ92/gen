from src.typeclass.VFF import VFF

from numpy import array, concatenate, stack, array_split, squeeze

class Bezier(VFF):
    def __init__(self, control_points, collapse_axes, callparam=lambda t:t):
        self.control_points = control_points
        self.collapse_axes = collapse_axes
        self.callparam = callparam

    def __call__(self, ts):
        t, *ts = ts
        m, *ms = self.collapse_axes

        scp = array_split(self.control_points, self.control_points.shape[m], m)

        while len(scp) > 1:
            temp_scp = []
            for prev, current in zip(scp, scp[1:]):
                temp_scp.append(self.convolve(t,prev,current))
            scp = temp_scp

        retv, *_ = scp
        retv = squeeze(retv, axis=m)
        if ms:
            ms = list(map(lambda x: x if x < m else x - 1, ms))
            retv = Bezier(retv, ms, self.callparam)(ts)

        return retv

    def convolve(self, t, slice_one, slice_two):
        return (1-t)*slice_one + t*slice_two
