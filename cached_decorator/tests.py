import unittest
from lab2.cached_decorator.cached import cached


class MyTestCase(unittest.TestCase):

    def test_cache(self):
        counter = 0

        @cached
        def inc_counter(*args):
            nonlocal counter
            counter += 1

        inc_counter(1, 2, 3)
        assert counter == 1

        inc_counter("one", "twp")
        assert counter == 2

        inc_counter(1, 2, 3)
        inc_counter("one", "two")
        assert counter == 2

        counter = 0


if __name__ == '__main__':
    unittest.main()
