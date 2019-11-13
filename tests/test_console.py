#!/usr/bin/python3
"""
Unittest for FileStorage class
"""
import unittest
from unittest import mock
import pep8
import os
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestConsole(unittest.TestCase):
    """ Test cases for the console """

    def test_pep8(self):
        """
        Test that we conform to PEP8.
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['console.py'])
        self.assertEqual(result.total_errors, 0, "Please fix pep8")
