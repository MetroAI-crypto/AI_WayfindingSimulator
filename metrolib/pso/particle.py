
from typing import Tuple
import numpy as np

from ..util.coordinate import Coordinate

# pylint: disable=too-many-instance-attributes


class Particle(Coordinate):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__w = kwargs.get('weight', .5)
        
        self.__max_velocity = kwargs.get('maximum_velocity', 2)

        # Randomly create a new particle properties
        self.__velocity = self._random.uniform(-1, 1, size=2)
        self.__clip_velocity()

        # Local best
        self.__best_position = self._position
        self.__best_value = self.value

    @property
    def velocity(self) -> float:
        return self.__velocity

    

    def __clip_velocity(self):
        norm = np.linalg.norm(self.__velocity)
        if norm > self.__max_velocity:
            self.__velocity *= self.__max_velocity/norm
