from shared.utils import get_multiple_sequence
import pytest


class TestMultipleSequence:
    def test_bad_start_end(self):
        """ get_multiple_sequences raises a ValueError if a valid start
            and end are not provided """
        with pytest.raises(ValueError):
            get_multiple_sequence(**{})

    def test_sequences(self):
        test_tuples = [(0, 10, 5, [5, 10])]
        for tt in test_tuples:
            ms_args = {'start': tt[0], 'end': tt[1], 'multiple': tt[2]}
            assert get_multiple_sequence(**ms_args) == tt[3]

