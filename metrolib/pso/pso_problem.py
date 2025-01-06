
# pylint: disable=too-many-instance-attributes

import logging

from .particle import Particle
from ..util.base_visualizer import BaseVisualizer
from ..util.problem_base import ProblemBase

LOGGER = logging.getLogger(__name__)


class PSOProblem(ProblemBase):
    def __init__(self, **kwargs):
        """
        Initialize a new particle swarm optimization problem.
        """
        super().__init__(**kwargs)
        self.__iteration_number = kwargs['iteration_number']
        self.__particles = [
            Particle(**kwargs, bit_generator=self._random)
            for _ in range(kwargs['particles'])
        ]

        # Initialize visualizer for plotting
        positions = [particle.position for particle in self.__particles]
        self._visualizer = BaseVisualizer(**kwargs)
        self._visualizer.add_data(positions=positions)

   
