
import logging
from copy import deepcopy

import numpy as np

from .whale import Whale
from ..util.base_visualizer import BaseVisualizer
from ..util.problem_base import ProblemBase

LOGGER = logging.getLogger(__name__)


class WOAProblem(ProblemBase):
    def __init__(self, **kwargs):
        """
        Initialize a new whale optimization algorithm problem.
        """
        

        self._visualizer = BaseVisualizer(**kwargs)
        # Initialize visualizer for plotting
        positions = [whale.position for whale in self.__whales]
        self._visualizer.add_data(positions=positions)

    def solve(self) -> Whale:
        global_best_whale = None

        # And also update global_best_whale
        for _ in range(self.__iteration_number):

     

            random_whales = deepcopy(self._random.choice(self.__whales, size=len(self.__whales)))
            for whale, random_whale in zip(self.__whales, random_whales):
                whale.step(global_best_whale, random_whale)

            # Add data for plot
            self._visualizer.add_data(positions=[whale.position for whale in self.__whales])

        return global_best_whale
