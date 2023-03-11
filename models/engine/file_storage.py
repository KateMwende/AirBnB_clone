#!/usr/bin/env bash
"""serializes instances to a JSON file and deserializes JSON file to instances"""

from models.basemodel import BaseModel
import json

class FileStorage:
    """serializes instances to a JSON file and deserializes JSON file to instances"""

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """returns dictionary __object"""

        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id
        Args:
           obj - the class type
        """

        key = "{}.{}",format(obj.__class.__name__,obj.id)
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""


