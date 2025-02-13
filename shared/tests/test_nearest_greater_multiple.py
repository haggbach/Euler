import pytest
from shared.utils import get_nearest_geq_multiple


class TestNearestGEQMultiple:
    def test_ngm(self):
        test_tuples = [
            # start, multiple, expected
            (0, 5, 5),
            (1, 5, 5),
            (2, 5, 5),
            (3, 5, 5),
            (4, 5, 5),
            (5, 5, 5),
            (-7, 5, -5)
        ]
        for tt in test_tuples:
            assert get_nearest_geq_multiple(**{'start_num': tt[0], 'multiple': tt[1]}) == tt[2]

