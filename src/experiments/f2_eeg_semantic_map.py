import numpy as np

def eeg_semantic_map(signal):
    fft = np.abs(np.fft.rfft(signal))
    meaning_density = np.std(fft) / (np.mean(fft) + 1e-9)
    return float(meaning_density)
