#!/usr/bin/env python3
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

        tmp_dict = {}
        for k, v in self.__objects.items():
            tmp_dict[k] = v.to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as written_file:
            json.dump(tmp_dict, written_file)

    def reload(self):
        """deserializes the JSON file to __objects"""

        try:
            temp_dict = {}
            with(self.__file_path, "r") as r:
                json.load(temp_dict, r)

            self.__objects = temp_dict
        except Exception:
            pass
