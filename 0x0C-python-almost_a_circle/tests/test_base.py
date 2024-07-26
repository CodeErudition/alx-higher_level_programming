#!/usr/bin/python3
"""
This module defines a TestBase class that tests
the base class
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """
    Represent the TestBase class
    """
    def test_id_auto_assignment(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, b1.id + 1)

    def test_id_manual_assignment(self):
        b1 = Base(89)
        self.assertEqual(b1.id, 89)

    def test_to_json_string_none(self):
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_empty_list(self):
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string(self):
        dict_list = [{'id': 12}]
        json_str = Base.to_json_string(dict_list)
        self.assertEqual(json_str, '[{"id": 12}]')

    def test_from_json_string_none(self):
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_empty(self):
        self.assertEqual(Base.from_json_string("[]"), [])

    def test_from_json_string(self):
        json_str = '[{"id": 89}]'
        dict_list = Base.from_json_string(json_str)
        self.assertEqual(dict_list, [{"id": 89}])

if __name__ == '__main__':
    unittest.main()
