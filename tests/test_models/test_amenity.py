#!/usr/bin/python3
"""
Unittest for BaseModel class
"""
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """ Test cases for Amenity class """

    def test_instance_BaseModel(self):
        """ Tests inheritance """
        amenity = Amenity()
        self.assertTrue(isinstance(amenity, BaseModel))

    def test_instaciacion(self):
        """ Tests correct instatiation of the class """
        am = Amenity()
        am.name = "Charlie"
        self.assertIn("name", am.to_dict())



