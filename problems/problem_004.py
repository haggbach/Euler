from datetime import datetime

from shared.utils import LogHelper

logger = LogHelper.get_logger(__name__)


def calculate():
    """ A palindromic number reads the same both ways. The largest palindrome made from the product of
    of two 2-digit numbers is 9009 = 91x99.
    Find the largest palindrome made from the product of two 3-digit numbers
    """
    palindromes = list()
    largest = None

    start_time = datetime.now()
    max_3_digit = generate_largest_n_digit_number(3)

    outer_number = max_3_digit

    while outer_number > 0:
        inner_number = max_3_digit
        while inner_number > 0:
            potential_palindrome = outer_number * inner_number
            if is_palindromic(potential_palindrome):
                palindromes.append(potential_palindrome)
            inner_number -= 1

        outer_number -= 1

    if palindromes:
        palindromes = sorted(palindromes, reverse=True)
        largest = palindromes[0]

    end_time = datetime.now()
    logger.info('Project Euler 004: %s in %s', largest, end_time - start_time)


def generate_largest_n_digit_number(n_digits):
    i = 0
    n_number = 0
    while i < n_digits:
        n_number += 9*10**i
        i += 1

    return n_number


def is_palindromic(input_number):
    # TODO: might want to add this to utils and tests, depending upon how popular the
    # concept of palindromic numbers is in the problem set
    # TODO: if we're adding tests, is a single-digit number palindromic?

    is_pal = False

    forward_str = str(input_number)
    backward_str = forward_str[::-1]
    if forward_str == backward_str:
        is_pal = True

    return is_pal


if __name__ == '__main__':
    calculate()
