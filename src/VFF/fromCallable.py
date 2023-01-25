class fromCallable():
    def __init__(self, call, callparam=lambda t:t):
        self.call = call
        self.callparam = callparam

    def __call__(self, t):
        return self.call(self.callparam(t))

