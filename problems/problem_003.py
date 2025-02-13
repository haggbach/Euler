from datetime import datetime

from shared.log_helpers import LogHelper
from shared.utils import is_prime

logger = LogHelper.get_logger(__name__)


def calculate(input_number):
    """
    The prime factors of 13195 are 5, 7, 13 and 29
    What is the largest prime factor of the number 600851475143?
    """
    largest = 0

    start_time = datetime.now()
    factor_list = list()
    if input_number % 2 == 0:
        factor_list.append(2)
        factor_list.append(input_number/2)

    max_check = int(input_number/2) + 1
    attempt = 3
    while attempt < max_check:
        factor = False
        if input_number % attempt == 0:
            factor = True
            factor_list.append(attempt)
            factor_list.append(input_number/attempt)

        # NAIVE: only need to check up to the input_number divided by
        # the most recent factor attempt (factor PAIRS are added)
        # (rounding UP if it's not a precise factor)
        max_check = int(input_number/attempt) + (0 if factor else 1)

        # NAIVE: attempt only odd numbers, as we're looking for
        # PRIME factors
        attempt += 2
        logger.info('attempt %s, max check %s', attempt, max_check)

    # sort factors desc
    factor_list = sorted(factor_list, reverse=True)

    # check factors from largest to smallest to find the first prime
    for factor in factor_list:
        if is_prime(**{'input_num': factor}):
            largest = factor
            break

    end_time = datetime.now()

    # correct answer in 44 seconds, happy with this for now
    logger.info('Project Euler 003: %s in %s' % (largest, end_time-start_time))

    return largest


if __name__ == "__main__":
    calculate(600851475143)
