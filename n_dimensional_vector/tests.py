import unittest
from .vector import Vector, VectorException


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.vector_one = Vector(1, 2, 3)
        self.vector_two = Vector(4, 5, 6.5)
        self.vector_three = Vector(7.5, 8)

    def test_init_raises(self):
        self.assertRaises(VectorException, Vector, 'arg1', 'arg2')

    def test_add(self):
        assert self.vector_one + self.vector_two == Vector(5, 7, 9.5)

    def test_add_raises(self):
        self.assertRaises(VectorException, self.vector_one.__add__, self.vector_three)

    def test_mul_const(self):
        assert self.vector_one * 2 == Vector(2, 4, 6)

    def test_mul(self):
        assert self.vector_one * self.vector_two == 33.5

    def test_imul(self):
        self.vector_one *= 2
        assert self.vector_one == Vector(2, 4, 6)

    def test_len(self):
        assert len(self.vector_one) == 3
        assert len(self.vector_three) == 2

#     and so on


if __name__ == '__main__':
    unittest.main()
