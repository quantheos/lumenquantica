import numpy as np

def ai_entropy_test(pred_probs):
    pred_probs = np.array(pred_probs)
    entropy = -np.sum(pred_probs * np.log(pred_probs + 1e-9))
    return float(entropy)
