import numpy as np

def smooth(signal, window=5):
    return np.convolve(signal, np.ones(window)/window, mode='same')
