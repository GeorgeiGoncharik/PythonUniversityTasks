import unittest
import json
from .json_serializer import to_string


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.int_type = 9999
        self.float_type = 123.
        self.boolean_true = True
        self.boolean_false = False
        self.none_type = None
        self.string_type = "bla-bla! bla? bla "
        self.tuple_type = (1, "string", True, False, 123., None)
        self.dict_type = {"uaz": 1980, "lambo": 2000, "honda": 2020}
        self.list_type = [10000000, False, 209.85, "one", "two"]

    def test_string(self):
        assert to_string(self.string_type) == json.dumps(self.string_type)

    def test_int(self):
        assert to_string(self.int_type) == json.dumps(self.int_type)

    def test_float(self):
        assert to_string(self.float_type) == json.dumps(self.float_type)

    def test_bool_true(self):
        assert to_string(self.boolean_true) == json.dumps(self.boolean_true)

    def test_bool_false(self):
        assert to_string(self.boolean_false) == json.dumps(self.boolean_false)

    def test_none(self):
        assert to_string(self.none_type) == json.dumps(self.none_type)

    def test_tuple(self):
        assert to_string(self.tuple_type) == json.dumps(self.tuple_type)

    def test_dict(self):
        assert to_string(self.dict_type) == json.dumps(self.dict_type)

    def test_list(self):
        assert to_string(self.list_type) == json.dumps(self.list_type)


if __name__ == '__main__':
    unittest.main()
