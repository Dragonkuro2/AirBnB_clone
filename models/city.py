#!/usr/bin/python3
""" class City module """

from models.base_model import BaseModel


class City(BaseModel):
    """
    City class that inherits from BaseModel class
    """
    state_id = ""
    name = ""
