#!/usr/bin/python3
""" module of the class Review"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review class that inherits from BaseModel class
    """
    place_id = ""
    user_id = ""
    text = ""
