#!/usr/bin/python3
"""
Unittest for BaseModel class
"""
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """ Test cases for BaseModel Class """

    def test_class(self):
        """ Tests instance of a class """
        base = BaseModel()
        self.assertTrue(isinstance(base, BaseModel))

    def test_id(self):
        """ Tests that ids are unique """
        base1 = BaseModel()
        base2 = BaseModel()
        self.assertTrue(base1.id != base2.id)

    def test_kwargs(self):
        """ Tests instanciation with kwargs"""
        base = BaseModel()
        base.name = "Dani"
        dicty = base.to_dict()
        self.assertTrue("name" in dicty)
