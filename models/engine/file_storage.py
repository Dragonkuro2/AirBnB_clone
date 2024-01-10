#!/usr/bin/python3
""" class FileStorage that serializes instances to a JSON file and deserializes
    JSON file to instances. """
from models.base_model import BaseModel
import json


class FileStorage(BaseModel):
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        obj = FileStorage.__objects
        objdict = {objt: obj[objt].to_dict() for objt in obj.keys()}
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(objdict, f)

    def reload(self):
        if with open(FileStorage.__file_path, 'r') as f:
            data = json.load(f)
            FileStorage.__objects += data

