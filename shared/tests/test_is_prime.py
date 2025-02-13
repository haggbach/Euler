from shared.utils import is_prime


class TestIsPrime:
    def test_is_prime(self):
        test_tuples = [(1, False),
                       (2, True),
                       (3, True),
                       (4, False),
                       (5, True),
                       (6, False),
                       (7, True),
                       (17, True),
                       (6857, True)]
        for tt in test_tuples:
            assert is_prime(**{'input_num': tt[0]}) == tt[1]

