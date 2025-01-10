

import numpy as np

from swarmlib.util.functions import FUNCTIONS

# pylint: disable=unused-variable


def describe_functions():
    def are_wrapped_correctly_and_return_correct_result():
        michalewicz = FUNCTIONS['michalewicz']

        result = michalewicz(np.array([1.5, 2.5]))

        np.testing.assert_array_almost_equal(result, -0.001786698064987311)
