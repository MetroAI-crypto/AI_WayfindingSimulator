
import logging

from .gwo_problem import GWOProblem
from ..util.functions import FUNCTIONS

LOGGER = logging.getLogger(__name__)


def _run_gwo(args):
    LOGGER.info('Start grey wolf optimization with parameters="%s"', args)
    args['function'] = FUNCTIONS[args['function']]

    problem = GWOProblem(**args)
    problem.solve()
    problem.replay()

