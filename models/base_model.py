#!/usr/bin/python3
""" BaseModel file. """
import uuid
import datetime


class BaseModel:
    """ a class BaseModel that defines all common attributes/methods
        for other classes. """
    def __init__(self, *args, **kwargs):
        """ initialize the elements.
            args:
                id: it has the id generated using uuid version 4.
                created_at: it has the current datetime.
                updated_at: it update the current dattime. """
        self.updated_at = datetime.datetime.now()
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.today()
        else:
            for key, value in kwargs.items()

    def __str__(self):
        """ return this format '[<class name>] (<self.id>) <self.__dict__>'"""
        cls = self.__class__.__name__
        return f"[{cls}] ({self.id}) {self.__dict__}"

    def save(self):
        """ update the datetime with the current datetime. """
        self.updated_at = datetime.datetime.today()

    def to_dict(self):
        """ returns a dictionary containing all keys/values
        of __dict__ of the instance. """
        r_dict = self.__dict__.copy()
        r_dict['__class__'] = self.__class__.__name__
        r_dict['created_at'] = self.created_at.isoformat()
        r_dict['updated_at'] = self.updated_at.isoformat()
        return r_dict
