#!/usr/bin/python3
"""
Unittest for BaseModel class
"""
import unittest
import models
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

    def test_to_dict(self):
        """ Tests that the function retrieves a dictionary """
        base = BaseModel()
        ret_dict = base.to_dict()
        self.assertTrue(isinstance(ret_dict, dict))

    def test_str(self):
        """ Tests the str repr. of an object """
        base = BaseModel()
        base_str = base.__str__()
        self.assertTrue(isinstance(base_str, str))

    def test_save(self):
        """ Tests the save method """
        base = BaseModel()
        base.name = "Plankton"
        time1 = base.updated_at
        base.save()
        time2 = base.updated_at
        self.assertNotEqual(time1, time2)
        obj_name = base.to_dict()['name']
        self.assertEqual(obj_name, "Plankton")
