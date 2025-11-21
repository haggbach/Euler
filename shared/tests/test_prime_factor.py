from shared.utils import factor_prime


class TestPrimeFactor:
    def test_factor_prime(self):
        test_tuples = [(1, [1]),
                       (2, [2]),
                       (3, [3]),
                       (4, [2, 2]),
                       (5, [5]),
                       (6, [2, 3]),
                       (8, [2, 2, 2]),
                       (10, [2, 5]),
                       (13, [13]),
                       (15, [3, 5]),
                       (20, [2, 2, 5]),
                       (100, [2, 2, 5, 5]),
                       (97, [97]),
                       (144, [2, 2, 2, 2, 3, 3])]
        for tt in test_tuples:
            assert factor_prime(tt[0]) == tt[1]
