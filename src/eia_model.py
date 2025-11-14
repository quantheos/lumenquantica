import numpy as np

class EIAModel:
    def __init__(self, E0=1.0, I0=1.0, lam=1.0):
        self.E0 = E0
        self.I0 = I0
        self.lam = lam

    def conservation(self, E, I, A):
        E = np.array(E)
        I = np.array(I)
        A = np.array(A)
        val = (E / self.E0) + (I / self.I0) + (self.lam * A)
        return np.diff(val)
