import unittest
from .singleton import singleton


@singleton
class Singleton:
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.singleton = Singleton('1', '2')
        self.singleton_two = Singleton('1', '3')

    def test_singleton_address(self):
        assert self.singleton is self.singleton_two

    def test_singleton_init_immutability(self):
        assert self.singleton_two.arg2 == '2'


if __name__ == '__main__':
    unittest.main()
