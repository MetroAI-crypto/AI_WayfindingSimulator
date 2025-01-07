
from abc import ABC, abstractmethod
from numpy.random import default_rng



class ProblemBase(ABC):
    def __init__(self, **kwargs) -> None:
        self._random = default_rng(kwargs.get('seed', None))
        self._visualizer: VisualizerBase = None

    @abstractmethod
    def solve(self) -> Coordinate:
        pass

   