
from math import gamma

import numpy as np


def levy_flight(start: np.ndarray, alpha: float, param_lambda: float, gen: np.random.Generator) -> np.ndarray:
    """
    Perform a levy flight step.

    Arguments:
        start {numpy.ndarray} -- The cuckoo's start position
        alpha {float} -- The step size
        param_lambda {float} -- lambda parameter of the levy distribution
        gen {Generator} -- the generator used to generate pseudo random numbers

    Returns:
        numpy.ndarray -- The new position
    """

    dividend = gamma(1 + param_lambda) * np.sin(np.pi * param_lambda / 2)
    divisor = gamma((1 + param_lambda) / 2) * param_lambda * np.power(2, (param_lambda - 1) / 2)
    sigma1 = np.power(dividend / divisor, 1 / param_lambda)

    sigma2 = 1


    return start + alpha * step_length
