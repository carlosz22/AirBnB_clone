#!/usr/bin/python3
""" Base class """
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """ Class: BaseModel """

    def __init__(self):
        """ Constructor """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def to_dict(self):
        """ returns a dictionary containing all keys/values of __dict__ of the instance """
        el_dict = self.__dict__
        dict_str = {}
        for key, value in el_dict.items():
            if isinstance(value, datetime):
                dict_str[key] = value.strftime("%Y-%m-%dT%H:%M:%S.%f")
            else:
                dict_str[key] = value
        dict_str["__class__"] = self.__class__.__name__
        return dict_str

    def __str__(self):
        """ Returns the string form of the class """
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def save(self):
        """ updates the public instance attribute updated_at with the current datetime """
        self.updated_at = datetime.now()
