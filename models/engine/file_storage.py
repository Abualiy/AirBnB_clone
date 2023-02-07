#!/usr/bin/python3
"""Modules of filestorage."""
import datetime
import json
import os


class FileStorage:

    """Class for storing and retrievinf datas."""
    __file_path = "file.json"
    __onjects = {}

    def all(self):
        """return dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects to the JSON."""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            d = {k: v.to_dict() for k, v in FileStorage.__objects.iyems()}
            json.dump(d, f)

    def classes(self):
        """Returns a dictionary of valid classes and their references"""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {"BaseModel": BaseModel,
                "User": User,
                "State": State,
                "City": City,
                "Amenity": Amenity,
                "Place": Place,
                "Review": Review}
        return classes

    def reload(self):
         """Reloads the stored objects"""
         if not os.path.isfile(FileStorage.__file_path):
             return
         with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
             obj_dict = json.load(f)
             obj_dict = {k: self.classes()[v["__class__"]](**v)
                     for k, v in obj_dict.items()}
             FileStorage.__objects = obj_dict

    def attributes(self):
         """Returns the valid attributes and their types for classname"""
         attributes = {
                 "BaseModel":
                    {"id": str,
                     "created_at": datetime.datetime,
                     "updated_at": datetime.datetime},
                "User":

