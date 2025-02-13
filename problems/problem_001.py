"""If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6, and 9.
The sum of these multiples is 23
Find the sum of all the multiples of 3 or 5 below 1000"""

from shared.log_helpers import LogHelper
from shared.utils import get_multiple_sequence

logger = LogHelper.get_logger(__name__)


def calculate():
    logger.info('Starting Project Euler 001')
    # get list of multiples of 3
    list_3 = get_multiple_sequence(**{'start': 1, 'end': 1000-1, 'multiple': 3})
    # get list of multiples of 5
    list_5 = get_multiple_sequence(**{'start': 1, 'end': 1000-1, 'multiple': 5})
    # combine / dedup lists
    list_combined = list(set(list_3 + list_5))

    calc = sum(list_combined)

    logger.info('Project Euler 001: %s', calc)

    return calc


if __name__ == "__main__":
    calculate()
