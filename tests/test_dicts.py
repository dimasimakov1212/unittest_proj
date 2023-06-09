import unittest
from utils import dicts


class TestArrs(unittest.TestCase):

    def test_get_val(self):
        data = {"name": "Max", "age": "26"}
        self.assertEqual(dicts.get_val(data, "name", "test"), "Max")
        self.assertEqual(dicts.get_val(data, "n", "test"), "test")
        self.assertEqual(dicts.get_val(data, "a"), "git")
        self.assertEqual(dicts.get_val({}, "name", "test"), "test")
