
import numpy as np
from ..util.base_visualizer import BaseVisualizer


class Visualizer(BaseVisualizer):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__best_wolf_indices = []

   
