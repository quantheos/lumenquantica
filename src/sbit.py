import numpy as np

class SBit:
    def __init__(self, threshold: float = 0.015):
        self.threshold = threshold

    def measure(self, meaning_signal):
        arr = np.array(meaning_signal)
        diffs = np.abs(np.diff(arr))
        sbits = np.sum(diffs > self.threshold)
        return sbits

    def semantic_density(self, meaning_signal):
        arr = np.array(meaning_signal)
        return float(np.std(arr) / (np.mean(arr) + 1e-9))
