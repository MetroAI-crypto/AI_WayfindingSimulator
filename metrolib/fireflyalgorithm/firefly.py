

# pylint: disable=too-many-arguments

import numpy as np

from ..util.coordinate import Coordinate


class Firefly(Coordinate):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.__alpha = kwargs.get('alpha', 0.25)
        self.__beta = kwargs.get('beta', 1)
        self.__gamma = kwargs.get('gamma', 0.97)

   

    def random_walk(self, area):
        self._position = np.array([self._random.uniform(cord-area, cord+area) for cord in self._position])
