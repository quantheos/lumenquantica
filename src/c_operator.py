import numpy as np

class COperator:
    @staticmethod
    def compute(delta_A: float, delta_I: float, eps: float = 1e-9) -> float:
        if abs(delta_I) < eps:
            return 0.0
        return delta_A / delta_I

    @staticmethod
    def time_series(A_series, I_series):
        A_series = np.array(A_series)
        I_series = np.array(I_series)
        dA = np.diff(A_series)
        dI = np.diff(I_series)
        with np.errstate(divide='ignore', invalid='ignore'):
            C_values = np.where(dI != 0, dA / dI, 0)
        return C_values
