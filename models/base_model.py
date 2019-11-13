#!/usr/bin/python3
""" Base class """
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """ Class: BaseModel """

    def __init__(self, *args, **kwargs):
        """ Constructor """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if len(kwargs) > 0:
            convert = ["created_at", "updated_at"]
            for key, value in kwargs.items():
                if key in convert:
                    setattr(self, key, datetime.strptime(value,
                                                         "%Y-%m-%dT%H:%M:%S.%f"))
                elif key == "__class__":
                    continue
                else:
                    setattr(self, key, value)
        else:
            models.storage.new(self)

    def to_dict(self):
        """ returns a dictionary containing all keys/values of __dict__"""
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
        """ updates the attr updated_at with current datetime """
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    @classmethod
    def all(cls):
        """ Prints all instances of the class by the console"""
        return "all {}".format(cls.__name__)

    @classmethod
    def count(cls):
        """ Returns the number of instances of a class """
        return "count {}".format(cls.__name__)

    @classmethod
    def show(cls, __id=''):
        """Returns the string representation of an instance"""
        return "show {} {}".format(cls.__name__, __id)

    @classmethod
    def destroy(cls, _id=''):
        """Destroys an instance"""
        return "destroy {} {}".format(cls.__name__, _id)

    @classmethod
    def update(cls, _id='', attribute_name='', attribute_value=''):
        """Updates an instance"""
        return "update {} {} {} {}".format(cls.__name__, _id, attribute_name,
                                           attribute_value)
