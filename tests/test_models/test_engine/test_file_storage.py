#!/usr/bin/python3
"""
Unittest for FileStorage class
"""
import unittest
import models
import pep8
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """ Test cases for FileStorage Class """

    def test_pep8_conformance_model_files(self):
        """
        Test that we conform to PEP8.
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0, "Please fix pep8")

    def test_docstring(self):
        """
        Testing docstring
        """
        self.assertIsNotNone(FileStorage.__doc__)
        self.assertIsNotNone(FileStorage.all.__doc__)
        self.assertIsNotNone(FileStorage.new.__doc__)
        self.assertIsNotNone(FileStorage.save.__doc__)
        self.assertIsNotNone(FileStorage.reload.__doc__)

    def test_class(self):
        """ Tests instance of a class """
        storage = FileStorage()
        self.assertTrue(isinstance(storage, FileStorage))

    def test_all(self):
        """Tests all() function"""
        storage = FileStorage()
        dict_all = storage.all()
        self.assertTrue(isinstance(dict_all, dict))
