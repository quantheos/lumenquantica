import numpy as np

def probability_shift(before, after):
    before = np.array(before)
    after = np.array(after)
    return float(np.sum(np.abs(after - before)))
