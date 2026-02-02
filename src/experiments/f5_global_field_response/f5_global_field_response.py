import numpy as np

def global_field_response(local_fields):
    return float(np.mean(np.array(local_fields)))
