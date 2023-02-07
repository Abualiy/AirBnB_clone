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


