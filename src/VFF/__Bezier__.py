from src.typeclass.VFF import VFF

from numpy import array, array_split, squeeze

class Bezier(VFF):
    def __init__(self, control_points, collapse_axes, callparam=lambda t:t):
        self.control_points = control_points
        self.collapse_axes = collapse_axes
        self.callparam = callparam

    def __call__(self, ts):
        ## Extract domain value and axis indicator.
        t, *ts = ts
        m, *ms = self.collapse_axes

        ## Along the given axis, gather sub-arrays from control points
        scp = array_split(self.control_points, self.control_points.shape[m], m)

        ## condense sub-arrays with convolution 
        while len(scp) > 1:
            temp_scp = []
            for prev, current in zip(scp, scp[1:]):
                temp_scp.append(self.convolve(t,prev,current))
            scp = temp_scp

        ## collect result of above computation and remove the condensed axis
        retv, *_ = scp
        retv = squeeze(retv, axis=m)

        ## recur computation if there're more axes to compress
        if ms:
            ms = list(map(lambda x: x if x < m else x - 1, ms))
            retv = Bezier(retv, ms, self.callparam).__call__(ts)

        return retv

    def convolve(self, t, slice_one, slice_two):
        return (1-t)*slice_one + t*slice_two
