
import numpy as np
from ..util.coordinate import Coordinate


class Whale(Coordinate):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__a = kwargs.get('a', 1.)
        self.__a_step_size = self.__a / kwargs['iteration_number']
        self.__b = kwargs.get('b', .5)

    def step(self, prey: Coordinate, rand_whale: Coordinate) -> None:
        """
        Execute a whale optimization step.
        Update the whale's position and value.

        Arguments:
            prey {Coordinate} -- The prey (global best whale)
            rand_whale {Coordinate} -- Randomly selected whale
        """
        prob: float = self._random.uniform()
        r_vec = self._random.uniform(size=2)  # Here r is in [0, 1) although the paper suggests [0, 1]
        a_vec = 2 * self.__a * r_vec - self.__a  # Equation 2.3
        c_vec = 2 * r_vec  # Equation 2.4

       
   
   
    def __attack_prey(self, prey: Coordinate):
        d_vec = np.linalg.norm(prey.position - self._position)
        l_vec = self._random.uniform(size=2) # Here l is in [0, 1) although the paper suggests [0, 1]
        self._position = d_vec * np.exp(self.__b * l_vec) * np.cos(2 * np.pi * l_vec) + prey.position  # Equation 2.5
