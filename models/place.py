#!/usr/bin/python3
""" User class """
from uuid import uuid4
from datetime import datetime
import models


class User(models.base_model.BaseModel):
    """ Class: User """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
