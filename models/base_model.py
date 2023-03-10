#!/usr/bin/python3
"""This script is the base model"""
from datetime import datetime
from models import storage
import uuid

class BaseModel:
    """This represents the BaseModel class"""
    def __str__(self):
        """Returs the official string representation"""
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)
    def save(self):
        """updates the public instance attribute updated_at"""
        self.updated_at = datetime.now()
        storage.save()
    def to_dict(self):
        """return a dictionary containing all keys/values of __dict__"""
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = type(self).__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat
        my_dict["updated_at"] = my_dict["updated_at"].isoformat
        return my_dict
    def __init__(self, *args, **kwargs):
        """Initializes instance attributes
        Args:
            - *args: list of arguments
            - **kwargs: dict of key value arguments
        """
        if kwargs is not None and kwargs != {}:
            for keys in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(kwargs["create_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict[key] = kwargs[key]
        else:
            self.__dict__ = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
