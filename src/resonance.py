import numpy as np

class ResonanceField:
    def __init__(self, alpha=0.8, beta=0.2):
        self.alpha = alpha
        self.beta = beta

    def omega(self, entropy_flow, meaning_flow):
        entropy_flow = np.array(entropy_flow)
        meaning_flow = np.array(meaning_flow)
        dS = -np.diff(entropy_flow)
        dA = np.diff(meaning_flow)
        return self.alpha * dS + self.beta * dA
