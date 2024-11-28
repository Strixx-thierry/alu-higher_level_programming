#!/usr/bin/python3
"""Defines unittests for the base.py module.

Unittest classes:
    TestBase_instantiation - tests for instantiation of the Base class.
    TestBase_to_json_string - tests for the to_json_string method.
    TestBase_save_to_file - tests for the save_to_file method.
    TestBase_from_json_string - tests for the from_json_string method.
    TestBase_create - tests for the create method.
    TestBase_load_from_file - tests for the load_from_file method.
    TestBase_save_to_file_csv - tests for the save_to_file_csv method.
    TestBase_load_from_file_csv - tests for the load_from_file_csv method.
"""
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase_instantiation(unittest.TestCase):
    """Tests for the instantiation of the Base class."""

    def test_no_arg(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_three_bases(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 2)

    def test_None_id(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def test_unique_id(self):
        self.assertEqual(12, Base(12).id)

    def test_nb_instances_after_unique_id(self):
        b1 = Base()
        b2 = Base(12)
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 1)

    def test_id_public(self):
        b = Base(12)
        b.id = 15
        self.assertEqual(15, b.id)

    def test_nb_instances_private(self):
        with self.assertRaises(AttributeError):
            print(Base(12).__nb_instances)

    def test_str_id(self):
        self.assertEqual("hello", Base("hello").id)

    def test_float_id(self):
        self.assertEqual(5.5, Base(5.5).id)

    def test_complex_id(self):
        self.assertEqual(complex(5), Base(complex(5)).id)

    def test_dict_id(self):
        self.assertEqual({"a": 1, "b": 2}, Base({"a": 1, "b": 2}).id)

    def test_bool_id(self):
        self.assertEqual
