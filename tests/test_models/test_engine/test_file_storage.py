#!/usr/bin/python3
"""
Unittest for FileStorage class
"""
import unittest
import pep8
import os
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """ Test cases for FileStorage Class """

    def tearDown(self):
        """Deleting everything at the end"""
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__path_file):
            os.remove(FileStorage._FileStorage__path_file)

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

    def test__file_path_exists(self):
        """Tests for the file path existance"""
        storage = FileStorage()
        self.assertTrue(isinstance(storage._FileStorage__file_path, str))

    def test_all(self):
        """Tests all() function"""
        storage = FileStorage()
        dict_all = storage.all()
        self.assertTrue(isinstance(dict_all, dict))
