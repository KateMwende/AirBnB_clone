#!/usr/bin/env bash
"""Base class to inherit from"""


from datetime import datetime
import uuid


class BaseModel:
    def __init__(self):
        """Initializes the Base model class attributes
        Args:
            id - identification number
        """

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Return strings of class name, id and dictionary of attributes"""

        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def save(self):
        """update updated_at with the current datetime"""

        self.updated_at = datetime.now()

    def to_dict(self):
        """returns all keys/values of __dict__ of the instance"""

        d = self.__dict__.copy()
        d['__class'] = self.__class__.__name__
        d['created_at'] = self.created_at.isoformat()
        d['updated_at'] = self.updated_at.isoformat()

        return d
