from shared.log_helpers import LogHelper


logger = LogHelper.get_logger(__name__)


def get_multiple_sequence(**kwargs):
    """
    For a start and end index, get a list of all multiples
        of the input multiple (a.k.a count by multiple)
    Multiple can be negative, but then end must be less than
        start
    :param kwargs:
        start - the number to start counting at (inclusive)
        end - the number ot end counting at (inclusive)
        multiple - the number to count by

    Raises ValueError if end is not greater than start
    :return:
    """
    start = kwargs.get('start', 0)
    end = kwargs.get('end', 0)
    multiple = kwargs.get('multiple', 0)

    mult_list = list()

    if multiple == 0:
        raise ValueError('INFINITE LOOP ALERT: %s needs to be a non-zero number')
    elif end <= start and multiple > 0:
        raise ValueError('INFINITE LOOP ALERT: %s (end) is not greater than %s (start) for multiple %s',
                         end, start, multiple)
    elif start <= end and multiple < 0:
        raise ValueError('INFINITE LOOP ALERT: %s (end) is not less than %s (start) for multiple %s',
                         end, start, multiple)

    # sort out start and end - we want to always be adding, for consistency
    counter = start if multiple > 0 else end
    stop = end if multiple > 0 else start
    multiple = abs(multiple)

    # sort out the counter so that it starts at a multiple, then
    # count (instead of looping and checking mod operators)
    counter = get_nearest_geq_multiple(**{'start_num': counter, 'multiple': multiple})
    while counter <= stop:
        mult_list.append(counter)
        counter += multiple

    return mult_list



def get_nearest_geq_multiple(**kwargs):
    """
    Advance the start number to the nearest multiple
    0 is not considered a "multiple"
    :param kwargs:
        start_num
        multiple
    :return:
    """
    start_num = kwargs.get('start_num')
    multiple = kwargs.get('multiple')

    if start_num == 0:
        start_num += multiple
    else:
        start_mod = start_num % multiple

        if start_mod != 0:
            start_num += (multiple-start_mod)

    return start_num


def is_prime(**kwargs):
    """ Prime numbers are only divisible by themselves and 1
        1 is not a prime number
    """
    prime_candidate = kwargs.get('input_num')
    input_is_prime = False if prime_candidate == 1 else True

    if prime_candidate > 3:
        curr_challenge = 2
        while input_is_prime and curr_challenge <= int(prime_candidate/2)+1:
            if prime_candidate % curr_challenge == 0:
                input_is_prime = False
            curr_challenge += 1

    return input_is_prime


