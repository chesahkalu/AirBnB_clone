#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
from models.base_model import BaseModel

class FileStorage:
    """Represent an abstracted storage engine which
    serializes instances to a JSON file & deserializes back to instances"""

    """Attributes:
        __file_path (str):path name to JSON file saving objects.
        __objects (dict): Empty dictionary to store object by class name.id"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects
    
    def new(self, obj):
        """sets inside __objects the obj as value,with key <obj class name>.id"""
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj
    
    def save(self):
        """sets objects dict data(atributes and values) as value for each object
        and serializes __objects to the JSON file (path: __file_path)"""
        new_objects = {}
        for key in self.__objects:
            new_objects[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(new_objects, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as f:
                obj_d = json.load(f)
            for obj in obj_d.values():
                    cls_name = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(cls_name)(**obj))
        except:
            pass
